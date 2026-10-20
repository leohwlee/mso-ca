const {chromium}=require('C:/Users/leohw/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const fs=require('node:fs'),path=require('node:path'),{pathToFileURL}=require('node:url');
const ids=['three-stages','inspection-versus-investigation','ownership-boundary','three-places','risk-levels','cdd-trigger-tree','reporting-route'];
const settle=async p=>{await p.evaluate(()=>document.fonts.ready);await p.evaluate(()=>new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r))))};
const state=(p,id)=>p.evaluate(id=>{const el=document.getElementById(id),r=el.getBoundingClientRect(),h=document.querySelector('.toolbar').getBoundingClientRect();return{lang:document.body.dataset.lang,top:r.top,headerBottom:h.bottom,gap:r.top-h.bottom,scrollY,visible:r.top>=h.bottom-1&&r.top<innerHeight}},id);
(async()=>{
const browser=await chromium.launch({headless:true,executablePath:'C:/Users/leohw/AppData/Local/ms-playwright/chromium-1228/chrome-win64/chrome.exe'});
const results=[],scrolled=[];
try{
 for(const width of [390,900,1440]){
  const context=await browser.newContext({viewport:{width,height:1000},reducedMotion:'reduce'});
  const page=await context.newPage();await page.route(/^https?:/,r=>r.abort());
  for(let n=1;n<=7;n++)for(const from of ['tc','en','both'])for(const to of ['tc','en','both'].filter(l=>l!==from)){
   const id='memory-'+ids[n-1];
   await page.goto(pathToFileURL(path.resolve(__dirname,`../part-${n}.html`)).href+`?lang=${from}&test=${to}#${id}`);await settle(page);
   const before=await state(page,id),b=await page.locator(`[data-language="${to}"]`).boundingBox();
   await page.mouse.click(b.x+b.width/2,b.y+b.height/2);await settle(page);
   const after=await state(page,id);results.push({part:n,width,from,to,before,after});
   if(!after.visible||after.lang!==to)await page.screenshot({path:path.join(__dirname,'previews-b',`final-real-language-${n}-${from}-${to}-${width}.png`)});
  }
  // An old hash should not force the user backwards after they have read onward.
  await page.goto(pathToFileURL(path.resolve(__dirname,'../part-6.html')).href+'?lang=tc#memory-cdd-trigger-tree');await settle(page);
  await page.evaluate(()=>window.scrollBy(0,650));
  const before=await state(page,'memory-cdd-trigger-tree'),b=await page.locator('[data-language=both]').boundingBox();
  await page.mouse.click(b.x+b.width/2,b.y+b.height/2);await settle(page);
  const after=await state(page,'memory-cdd-trigger-tree');scrolled.push({width,before,after,jumpedBack:after.visible});
  await context.close();console.log(`Completed visible-coordinate language switching at ${width}`);
 }
}finally{await browser.close()}
const failures=results.filter(r=>!r.after.visible||r.after.lang!==r.to);
fs.writeFileSync(path.join(__dirname,'final-assessment-b-language.json'),JSON.stringify({method:'coordinate click on observed visible button bounding box; avoids locator auto-scroll',results,scrolled,failures},null,2));
console.log(JSON.stringify({cases:results.length,failures,scrolled},null,2));
})();
