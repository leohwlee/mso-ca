const { chromium } = require('C:/Users/leohw/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const {pathToFileURL}=require('node:url');
const path=require('node:path');
(async()=>{
 const browser=await chromium.launch({headless:true,executablePath:'C:/Users/leohw/AppData/Local/ms-playwright/chromium-1228/chrome-win64/chrome.exe'});
 const page=await browser.newPage({viewport:{width:1440,height:1000}});
 await page.route(/^https?:/,r=>r.abort());
 await page.goto(pathToFileURL(path.resolve(__dirname,'../part-6.html')).href+'?lang=both#triggers');
 await page.screenshot({path:path.join(__dirname,'before-desktop.png')});
 await page.setViewportSize({width:390,height:844});
 await page.locator('#triggers').scrollIntoViewIfNeeded();
 await page.screenshot({path:path.join(__dirname,'before-mobile.png')});
 await browser.close();
})();
