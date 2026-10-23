const { chromium } = require('playwright');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { pathToFileURL } = require('node:url');

const root = path.resolve(__dirname, '..');
assert.equal(path.basename(root), 'Codex');
const report = [];

(async () => {
  const browser = await chromium.launch({
    executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    headless: true,
    args: ['--disable-crash-reporter', '--disable-breakpad'],
  });
  try {
    for (const variant of ['werkplaats', 'kust']) {
      for (const width of [1440, 390, 360, 768]) {
        const page = await browser.newPage({ viewport: { width, height: 1000 }, reducedMotion: 'reduce' });
        const errors = [];
        page.on('pageerror', error => errors.push(error.message));
        page.on('requestfailed', request => errors.push(request.url()));
        await page.goto(pathToFileURL(path.join(root, variant, 'index.html')).href);
        await page.evaluate(async () => {
          await document.fonts.ready;
          await Promise.all([...document.images].map(img => {
            img.loading = 'eager';
            return img.decode();
          }));
        });
        const layout = await page.evaluate(() => ({
          width: innerWidth,
          scrollWidth: document.documentElement.scrollWidth,
          brokenImages: [...document.images].filter(img => !img.naturalWidth).length,
          headingCount: document.querySelectorAll('h1').length,
          fonts: [...document.fonts].map(font => ({ family: font.family, status: font.status })),
          overflow: [...document.querySelectorAll('main *')].filter(el => {
            const r = el.getBoundingClientRect();
            return r.width && (r.right > innerWidth + 1 || r.left < -1);
          }).map(el => el.className),
          missingAnchors: [...document.querySelectorAll('a[href^="#"]')].filter(a => !document.getElementById(a.hash.slice(1))).map(a => a.hash),
          bodyLineHeight: getComputedStyle(document.body).lineHeight,
        }));
        assert.equal(layout.scrollWidth, width, `${variant}/${width}: horizontale overflow`);
        assert.equal(layout.brokenImages, 0, `${variant}/${width}: ontbrekende foto's`);
        assert.equal(layout.headingCount, 1);
        assert.deepEqual(layout.overflow, [], `${variant}/${width}: element buiten beeld`);
        assert.deepEqual(layout.missingAnchors, []);
        assert.ok(layout.fonts.every(font => font.status === 'loaded'), 'Font niet geladen');
        assert.deepEqual(errors, [], `${variant}/${width}: browserfouten`);
        for (const href of ['tel:+31621193640', 'https://wa.me/31621193640', 'mailto:atoadvies@live.nl']) {
          assert.ok(await page.locator(`a[href="${href}"]`).count(), `${variant}: ontbrekende contactlink ${href}`);
        }
        const input = page.locator('[data-comparison]');
        await input.focus();
        await input.press('ArrowRight');
        assert.equal(await input.inputValue(), '51');
        assert.equal(await page.locator('.comparison').evaluate(el => el.style.getPropertyValue('--position')), '51%');
        assert.match(await input.getAttribute('aria-valuetext'), /51/);
        await input.press('Home');
        assert.equal(await input.inputValue(), '0');
        await input.press('End');
        assert.equal(await input.inputValue(), '100');
        await input.fill('50');
        await input.dispatchEvent('input');
        if (variant === 'kust') {
          const details = page.locator('.service-details details');
          assert.equal(await details.count(), 6);
          const target = details.nth(1);
          await target.locator('summary').click();
          assert.equal(await target.getAttribute('open'), '');
          assert.ok(await target.locator('a').isVisible());
          await target.locator('summary').focus();
          await target.locator('summary').press('Enter');
          assert.equal(await target.getAttribute('open'), null);
        } else {
          assert.equal(await page.locator('.service-list .service').count(), 6);
        }
        await page.evaluate(() => { document.activeElement.blur(); window.scrollTo(0, 0); });
        if (width === 1440 || width === 390) {
          const suffix = width === 1440 ? 'desktop' : 'mobile';
          await page.screenshot({ path: path.join(root, 'previews', `${variant}-${suffix}.png`) });
          await page.screenshot({ path: path.join(root, 'previews', `${variant}-${suffix}-full.png`), fullPage: true });
        }
        const quote = page.locator('[data-offerte]');
        assert.ok(await quote.isVisible(), `${variant}/${width}: offerte-hulp niet zichtbaar`);
        await quote.locator('input[name="klus"]').nth(3).check({ force: true });
        await quote.locator('input[name="plaats"]').nth(1).check({ force: true });
        const quoteHref = decodeURIComponent(await page.locator('[data-offerte-link]').getAttribute('href'));
        assert.match(quoteHref, /text=Hallo.*\nKlus: Houtrotherstel\nPlaats: Spijkenisse\nIk stuur/, `${variant}/${width}: WhatsApp-bericht klopt niet`);
        assert.match(await quote.locator('[data-offerte-bericht]').textContent(), /Plaats: Spijkenisse/);
        assert.equal(await page.evaluate(() => document.documentElement.scrollWidth), width, `${variant}/${width}: overflow na keuze in offerte-hulp`);
        const firstJob = page.locator('.werk').first();
        const jobPhoto = firstJob.locator('[data-werk-img]');
        const resultSrc = await jobPhoto.getAttribute('src');
        await firstJob.locator('[data-werk-stappen] button').first().click();
        assert.notEqual(await jobPhoto.getAttribute('src'), resultSrc, `${variant}/${width}: projectfoto wisselt niet`);
        await page.waitForFunction(() => { const img = document.querySelector('[data-werk-img]'); return img.complete && img.naturalWidth > 0; });
        await page.locator('[data-werk-filter] button[data-dienst="houtrot"]').click();
        assert.equal(await page.locator('.werk:visible').count(), 1, `${variant}/${width}: filter op houtrot`);
        assert.equal(await page.evaluate(() => document.documentElement.scrollWidth), width, `${variant}/${width}: overflow in projectenoverzicht`);
        report.push({ variant, width, ...layout, interaction: 'OK', errors });
        await page.close();
      }
    }
    const page = await browser.newPage({ viewport: { width: 1440, height: 1000 } });
    await page.goto(pathToFileURL(path.join(root, 'index.html')).href);
    assert.equal(await page.locator('.preview').count(), 2);
    await page.locator('a.open-design').first().click();
    assert.ok(page.url().endsWith('/werkplaats/index.html'));
    await page.goBack();
    await page.locator('a.open-design').last().click();
    assert.ok(page.url().endsWith('/kust/index.html'));
    await page.close();
    fs.writeFileSync(path.join(root, '.qa', 'report.json'), JSON.stringify(report, null, 2));
    console.log('OK: beide mockups op 1440, 768, 390 en 360 px; foto’s, fonts, links, schuif, toetsenbord, dienst-uitklappers en overzichtsnavigatie.');
  } finally {
    await browser.close();
  }
})().catch(error => { console.error(error); process.exitCode = 1; });
