// Local rendered checks: all panels, each reading mode and intermediate widths.
const { chromium } = require('C:/Users/leohw/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const { pathToFileURL } = require('node:url');
const path = require('node:path'), fs = require('node:fs');
const stage = process.argv.includes('--before') ? 'before' : 'after';
const pilot = process.argv.includes('--pilot');
(async () => {
  const browser = await chromium.launch({ headless: true, executablePath: 'C:/Users/leohw/AppData/Local/ms-playwright/chromium-1228/chrome-win64/chrome.exe' });
  const dir = path.join(__dirname, `previews-${stage}`);
  fs.mkdirSync(dir, { recursive: true });
  const results = [], errors = [], remote = [];
  const page = await browser.newPage();
  page.on('pageerror', e => errors.push(e.message));
  await page.route(/^https?:/, r => { remote.push(r.request().url()); return r.abort(); });
  for (const width of (pilot ? [390, 900] : [390, 600, 768, 900, 1440])) {
    await page.setViewportSize({ width, height: 1000 });
    for (const n of (pilot ? [1, 6] : [1, 2, 3, 4, 5, 6, 7])) for (const lang of ['tc', 'en', 'both']) {
      await page.goto(pathToFileURL(path.resolve(__dirname, `../part-${n}.html`)).href + `?lang=${lang}`);
      await page.evaluate(() => document.fonts.ready);
      const observations = await page.locator('.memory-panel').evaluateAll(figures => figures.map(f => {
        const rect = f.getBoundingClientRect();
        const visible = e => { const r = e.getBoundingClientRect(); return r.width > 0 && r.height > 0 && getComputedStyle(e).display !== 'none'; };
        return {
          id: f.id, width: Math.round(rect.width), height: Math.round(rect.height),
          overflow: f.scrollWidth > f.clientWidth + 2,
          spills: [...f.querySelectorAll('*')].filter(e => {
            const r = e.getBoundingClientRect(), s = getComputedStyle(e);
            const heading = e.closest('thead');
            if (heading && getComputedStyle(heading).clipPath === 'inset(50%)') return false;
            return visible(e) && s.position !== 'absolute' && (r.right > rect.right + 2 || r.left < rect.left - 2);
          }).map(e => `${e.tagName}.${e.className}`).slice(0, 8),
          hiddenWrongLanguage: [...f.querySelectorAll(document.body.dataset.lang === 'tc' ? '.en' : document.body.dataset.lang === 'en' ? '.tc' : '[data-never]')].every(e => !visible(e)),
          columns: [...f.querySelectorAll('table')].map(t => ({
            labelled: !!document.getElementById(t.getAttribute('aria-labelledby')),
            expectedHeaders: t.querySelectorAll('thead th').length,
            headerDisplay: getComputedStyle(t.querySelector('thead')).display,
            rowDisplay: getComputedStyle(t.querySelector('tbody tr')).display,
            firstDataCellWidth: Math.round(t.querySelector('tbody td').getBoundingClientRect().width)
          }))
        };
      }));
      for (const observation of observations) {
        const table = page.locator(`#${observation.id} table`);
        for (let i = 0; i < observation.columns.length; i++)
          observation.columns[i].accessibleHeaders = await table.nth(i).getByRole('columnheader').count();
      }
      results.push({ part: n, lang, width, pageOverflow: await page.evaluate(() => document.documentElement.scrollWidth > innerWidth + 2), panels: observations });
      // All 33 panels in each of two language/device combinations, plus bilingual samples.
      const capture = !process.argv.includes('--no-captures') && ((width === 1440 && lang === 'tc') || (width === 390 && lang === 'en') || (lang === 'both' && [390, 900].includes(width)));
      if (capture) {
        // Export-only adjustment: sticky chrome must not cover the content in a long image.
        await page.addStyleTag({ content: 'header.toolbar,.skip-link{visibility:hidden!important}' });
        const targets = lang === 'both'
          ? observations.filter(o => ['memory-ml-tf-pf', 'memory-licence-clocks', 'memory-money-boundaries', 'memory-assessment-clocks', 'memory-control-responsibilities', 'memory-cdd-trigger-tree', 'memory-retention-clocks'].includes(o.id))
          : observations;
        for (const o of targets)
          await page.locator(`#${o.id}`).screenshot({ path: path.join(dir, `part-${n}-${o.id}-${lang}-${width}.png`) });
      }
    }
  }
  await browser.close();
  const failures = results.filter(r => r.pageOverflow || r.panels.some(p => p.overflow || p.spills.length || !p.hiddenWrongLanguage || (stage === 'after' && p.columns.some(t => !t.labelled || t.accessibleHeaders !== t.expectedHeaders))));
  const summary = { stage, pilot, pageCases: results.length, panelCases: results.reduce((n, r) => n + r.panels.length, 0), failures: failures.map(r => ({part:r.part,lang:r.lang,width:r.width,panels:r.panels.filter(p=>p.overflow||p.spills.length||!p.hiddenWrongLanguage||p.columns.some(t=>!t.labelled||t.accessibleHeaders!==t.expectedHeaders))})), errors, remote };
  const hashes = Object.fromEntries([1,2,3,4,5,6,7].map(n => [`part-${n}.html`,require('node:crypto').createHash('sha256').update(fs.readFileSync(path.resolve(__dirname,`../part-${n}.html`))).digest('hex')]));
  fs.writeFileSync(path.join(__dirname, `visual-checks-${stage}${pilot ? '-pilot' : ''}.json`), JSON.stringify({ summary, hashes, results }, null, 2));
  console.log(JSON.stringify(summary));
  process.exitCode = failures.length || errors.length || remote.length ? 1 : 0;
})();
