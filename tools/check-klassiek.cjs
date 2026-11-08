// Browsercontrole klassiek: foto's, breedtes, schuif, projectknoppen, filter.
const { chromium } = require('playwright');
const assert = require('node:assert/strict');
(async () => {
  const browser = await chromium.launch(process.platform === 'darwin' ? { executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', headless: true } : { channel: 'chrome', headless: true });
  for (const width of [1440, 768, 390, 360]) {
    const page = await browser.newPage({ viewport: { width, height: 900 } });
    const fouten = [];
    page.on('pageerror', e => fouten.push(e.message));
    page.on('response', r => { if (r.status() >= 400) fouten.push(r.status() + ' ' + r.url()); });
    await page.goto('http://127.0.0.1:8765/claude/klassiek/', { waitUntil: 'networkidle' });
    // alle projectfoto's en alle stapfoto's laden
    const srcs = await page.$$eval('[data-werk-stappen] button', b => b.map(x => x.dataset.src));
    assert.equal(srcs.length, 33, 'aantal stapfoto\'s');
    for (const s of srcs) {
      const ok = await page.evaluate(src => new Promise(r => { const i = new Image(); i.onload = () => r(i.naturalWidth > 0); i.onerror = () => r(false); i.src = src; }), s);
      assert.ok(ok, `${width}: foto laadt niet: ${s}`);
    }
    await page.evaluate(() => window.scrollTo(0, document.body.scrollHeight));
    await page.waitForTimeout(300);
    const kapot = await page.$$eval('img', is => is.filter(i => i.complete && i.naturalWidth === 0).map(i => i.src));
    assert.deepEqual(kapot, [], `${width}: kapotte img`);
    assert.equal(await page.evaluate(() => document.documentElement.scrollWidth), width, `${width}: zijwaarts scrollen`);
    // schuif
    await page.locator('.ba-range').fill('20');
    assert.match(await page.locator('.ba').getAttribute('style'), /--pos:\s*20%/, `${width}: schuif`);
    // projectknoppen en filter
    assert.equal(await page.locator('.werk').count(), 13);
    const eerste = page.locator('.werk').first(), img = eerste.locator('[data-werk-img]');
    const voor = await img.getAttribute('src');
    await eerste.locator('[data-werk-stappen] button').first().click();
    assert.notEqual(await img.getAttribute('src'), voor, `${width}: stap wisselt niet`);
    for (const [d, n] of [['houtrot', 1], ['boeilijsten', 2], ['ramen', 6], ['overig', 4]]) {
      await page.locator(`[data-werk-filter] button[data-dienst="${d}"]`).click();
      assert.equal(await page.locator('.werk:visible').count(), n, `${width}: filter ${d}`);
    }
    await page.locator('[data-werk-filter] button[data-dienst=""]').click();
    assert.equal(await page.locator('.werk:visible').count(), 13, `${width}: filter alles`);
    assert.deepEqual(fouten, [], `${width}: fouten`);
    
    console.log(width, 'OK');
    await page.close();
  }
  await browser.close();
})().catch(e => { console.error(e.message); process.exit(1); });
