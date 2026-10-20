const { chromium } = require('C:/Users/leohw/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const { pathToFileURL, fileURLToPath } = require('node:url');
const path = require('node:path'), fs = require('node:fs');
(async () => {
  const browser=await chromium.launch({headless:true,executablePath:'C:/Users/leohw/AppData/Local/ms-playwright/chromium-1228/chrome-win64/chrome.exe'});
  const page=await browser.newPage(), checks=[], errors=[], remote=[];
  page.on('pageerror',e=>errors.push(e.message));
  await page.route(/^https?:/,r=>{remote.push(r.request().url());return r.abort()});
  for(const width of [390,1440]){
    await page.setViewportSize({width,height:1000});
    await page.goto(pathToFileURL(path.join(__dirname,'preview.html')).href);
    const links=await page.locator('a').evaluateAll(es=>es.map(e=>e.href));
    const images=await page.locator('img').evaluateAll(es=>es.map(e=>e.src));
    checks.push({width,overflow:await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth+2),missing:[...links,...images].filter(u=>!fs.existsSync(fileURLToPath(new URL(u))))});
    await page.screenshot({path:path.join(__dirname,`preview-gallery-${width}.png`)});
  }
  await browser.close();
  const result={checks,errors,remote};
  fs.writeFileSync(path.join(__dirname,'preview-checks.json'),JSON.stringify(result,null,2));
  console.log(JSON.stringify(result));
  process.exitCode=checks.some(x=>x.overflow||x.missing.length)||errors.length||remote.length?1:0;
})();
