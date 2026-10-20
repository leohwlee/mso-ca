const {chromium}=require('C:/Users/leohw/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const fs=require('node:fs'),path=require('node:path'),{pathToFileURL}=require('node:url');
(async()=>{
const browser=await chromium.launch({headless:true,executablePath:'C:/Users/leohw/AppData/Local/ms-playwright/chromium-1228/chrome-win64/chrome.exe'});
const page=await browser.newPage({viewport:{width:390,height:1000},reducedMotion:'reduce'});
const result=[];
for(const mode of ['locator','mouse']){
 await page.goto(pathToFileURL(path.resolve(__dirname,'../part-1.html')).href+'?lang=tc&trace='+mode+'#memory-three-stages');
 await page.evaluate(()=>document.fonts.ready);await page.evaluate(()=>new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r))));
 await page.evaluate(()=>{
  window.events=[];
  window.record=(type)=>{const d=document.getElementById('memory-three-stages'),off=parseFloat(getComputedStyle(document.documentElement).scrollPaddingTop),m=parseFloat(getComputedStyle(d).scrollMarginTop);window.events.push({type,y:scrollY,top:d.getBoundingClientRect().top,offset:off,margin:m,at:Math.abs(d.getBoundingClientRect().top-off-m)<32,lang:document.body.dataset.lang})};
  record('before');document.addEventListener('pointerdown',()=>record('pointerdown'),true);document.addEventListener('click',()=>record('click'),true);
 });
 const btn=page.locator('[data-language=both]');
 if(mode==='locator')await btn.click();else{const b=await btn.boundingBox();await page.mouse.click(b.x+b.width/2,b.y+b.height/2);}
 await page.evaluate(()=>new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r))));
 const events=await page.evaluate(()=>{record('after');return window.events});
 result.push({mode,events});
}
await browser.close();
fs.writeFileSync(path.join(__dirname,'final-assessment-b-click-trace.json'),JSON.stringify(result,null,2));console.log(JSON.stringify(result,null,2));
})();
