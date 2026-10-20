// Capture real, offline UI for the bilingual README after building dist/mso-ca.html.
// Requires Playwright. Optional PLAYWRIGHT_MODULE and CHROMIUM_EXECUTABLE select
// an existing local installation; this script does not install dependencies.
const { chromium } = require(process.env.PLAYWRIGHT_MODULE || 'playwright');
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const { pathToFileURL } = require('node:url');
const { execFileSync } = require('node:child_process');
const root = path.resolve(__dirname, '..');
const version = fs.readFileSync(path.join(root, 'CHANGELOG.md'), 'utf8').match(/^## (v[\d.]+) /m)[1];
const output = path.join(root, 'docs/images');
const hash = data => crypto.createHash('sha256').update(data).digest('hex');

(async () => {
  fs.mkdirSync(output, { recursive: true });
  const browser = await chromium.launch({
    headless: true,
    ...(process.env.CHROMIUM_EXECUTABLE ? {executablePath: process.env.CHROMIUM_EXECUTABLE} : {})
  });
  const captures = [], errors = [], remote = [];
  try {
    for (const lang of ['en', 'tc']) {
      const context = await browser.newContext({
        viewport: {width: 1280, height: 1000},
        deviceScaleFactor: 1,
        colorScheme: 'light',
        reducedMotion: 'reduce',
        offline: true
      });
      const page = await context.newPage();
      page.on('pageerror', e => errors.push(e.message));
      await page.route(/^https?:/, r => {remote.push(r.request().url()); return r.abort();});
      for (const [kind, source, anchor] of [
        ['app', 'dist/mso-ca.html', ''],
        ['study', 'revision/study-notes/part-6.html', '#memory-cdd-trigger-tree']
      ]) {
        await page.setViewportSize(kind === 'app' ? {width:1280,height:1000} : {width:1440,height:1120});
        await page.goto(pathToFileURL(path.join(root, source)).href + `?lang=${lang}${anchor}`);
        await page.evaluate(() => document.fonts.ready);
        if (kind === 'app') {
          await page.locator('#btn-start').waitFor({state:'visible'});
          const count = await page.evaluate(() => window.BANK.length);
          if (count !== 525) throw new Error(`Unexpected bank count ${count}`);
        } else {
          await page.locator('#memory-cdd-trigger-tree').waitFor({state:'visible'});
          await page.evaluate(() => document.getElementById('memory-cdd-trigger-tree').scrollIntoView());
          const box = await page.locator('#memory-cdd-trigger-tree').boundingBox();
          await page.setViewportSize({width:1440,height:Math.ceil(box.y+box.height+16)});
          await page.evaluate(() => document.getElementById('memory-cdd-trigger-tree').scrollIntoView());
        }
        const overflow = await page.evaluate(() => document.documentElement.scrollWidth > innerWidth + 2);
        if (overflow) throw new Error(`Overflow: ${kind} ${lang}`);
        const file = `${kind}-${version}-${lang}.png`;
        await page.screenshot({path:path.join(output,file), animations:'disabled', fullPage:kind === 'app'});
        captures.push({
          file: `docs/images/${file}`, source, lang, anchor,
          viewport: page.viewportSize(),
          full_page: kind === 'app',
          source_sha256: hash(fs.readFileSync(path.join(root,source))),
          image_sha256: hash(fs.readFileSync(path.join(output,file)))
        });
      }
      await context.close();
    }
  } finally {
    await browser.close();
  }
  if (errors.length || remote.length) throw new Error(JSON.stringify({errors,remote}));
  const record = {
    version, captured_at: new Date().toISOString(),
    source_commit: execFileSync('git',['rev-parse','HEAD'],{cwd:root,encoding:'utf8'}).trim(),
    method: 'Fresh isolated browser contexts; actual offline pages; no synthetic scores or image edits.',
    captures, errors, remote_requests: remote
  };
  fs.writeFileSync(path.join(output,'readme-previews.json'),JSON.stringify(record,null,2)+'\n');
  console.log(JSON.stringify(record,null,2));
})().catch(e => {console.error(e);process.exit(1);});
