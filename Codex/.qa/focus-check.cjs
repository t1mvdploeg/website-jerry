const { chromium } = require('playwright');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { pathToFileURL } = require('node:url');
const root = path.resolve(__dirname, '..');
assert.equal(path.basename(root), 'Codex');
const luminosity = rgb => rgb.map(v => v / 255).map(v => v <= .04045 ? v / 12.92 : ((v + .055) / 1.055) ** 2.4).reduce((sum, v, i) => sum + v * [.2126, .7152, .0722][i], 0);
(async () => {
  const browser = await chromium.launch({ executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', headless: true, args: ['--disable-crash-reporter', '--disable-breakpad'] });
  const report = [];
  try {
    for (const variant of ['werkplaats', 'kust']) {
      const page = await browser.newPage({ viewport: { width: 1440, height: 1000 }, reducedMotion: 'reduce' });
      await page.goto(pathToFileURL(path.join(root, variant, 'index.html')).href);
      await page.evaluate(() => document.fonts.ready);
      await page.keyboard.press('Tab');
      for (const [name, selector] of [['hero', '.hero .button'], ['contact', variant === 'werkplaats' ? '.contact .button' : '.contact-section .button'], ['range', '[data-comparison]']]) {
        const control = page.locator(selector);
        await control.focus();
        const data = await control.evaluate(el => {
          const style = getComputedStyle(el);
          let ancestor = el.parentElement;
          while (ancestor && getComputedStyle(ancestor).backgroundColor === 'rgba(0, 0, 0, 0)') ancestor = ancestor.parentElement;
          return { focused: el.matches(':focus-visible'), outline: style.outlineColor, width: style.outlineWidth, background: getComputedStyle(ancestor).backgroundColor };
        });
        assert.ok(data.focused, `${variant}/${name}: geen focus-visible`);
        assert.equal(data.width, '3px');
        const values = [data.outline, data.background].map(color => color.match(/[\d.]+/g).slice(0, 3).map(Number)).map(luminosity).sort((a, b) => a - b);
        const contrast = (values[1] + .05) / (values[0] + .05);
        assert.ok(contrast >= 3, `${variant}/${name}: focuscontrast ${contrast}`);
        if (name !== 'range') await page.screenshot({ path: path.join(root, '.qa', `${variant}-${name}-focus.png`) });
        report.push({ variant, control: name, ...data, contrast });
      }
      await page.close();
    }
    fs.writeFileSync(path.join(root, '.qa', 'focus-report.json'), JSON.stringify(report, null, 2));
    console.log('OK: alle zes focusindicatoren minimaal 3:1; knoppen en sliders toetsenbordzichtbaar.');
  } finally { await browser.close(); }
})().catch(error => { console.error(error); process.exitCode = 1; });
