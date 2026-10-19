const {chromium}=require('C:/Users/leohw/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const {pathToFileURL}=require('node:url');
const fs=require('node:fs'),path=require('node:path');
(async()=>{
 const browser=await chromium.launch({headless:true,executablePath:'C:/Users/leohw/AppData/Local/ms-playwright/chromium-1228/chrome-win64/chrome.exe'});
 const results=[],dir=path.join(__dirname,'previews');fs.mkdirSync(dir,{recursive:true});
 for(const [device,width] of [['desktop',1440],['mobile',390]]){
  const page=await browser.newPage({viewport:{width,height:1000}}),errors=[],remote=[];
  page.on('pageerror',e=>errors.push(e.message));
  await page.route(/^https?:/,r=>{remote.push(r.request().url());return r.abort()});
  for(let n=1;n<=7;n++)for(const lang of ['tc','en','both']){
   await page.goto(pathToFileURL(path.resolve(__dirname,`../part-${n}.html`)).href+`?lang=${lang}`);
   await page.evaluate(()=>document.fonts.ready);
   const state=await page.locator('.memory-panel').evaluateAll((figs,{lang})=>figs.map(f=>{
    const r=f.getBoundingClientRect();
    const wrong=lang==='both'?[]:[...f.querySelectorAll(lang==='tc'?'.en':'.tc')].filter(e=>e.getBoundingClientRect().height>0);
    const spills=[...f.querySelectorAll('*')].filter(e=>{const b=e.getBoundingClientRect();return b.width>0&&(b.left<r.left-3||b.right>r.right+3)}).map(e=>e.className);
    return {id:f.id,height:r.height,width:r.width,wrong:wrong.length,spills,hasCitation:!!f.querySelector('.source-citation a'),visible:r.height>0};
   }),{lang});
   for(const f of state)results.push({part:n,lang,device,...f,errors:[...errors],remote:[...remote]});
   if((device==='desktop'&&lang==='tc')||(device==='mobile'&&lang==='both')){
    await page.addStyleTag({content:'.toolbar,.skip-link{visibility:hidden!important}'});
    for(const f of state)await page.locator('#'+f.id).screenshot({path:path.join(dir,`figure-p${n}-${f.id}-${lang}-${device}.png`)});
   }
   // Also capture both languages on desktop for the long decision branches.
   if(device==='desktop'&&lang==='both')for(const id of ['cdd-trigger-tree','cdd-extent-tree','review-commencement','reporting-route','party-roles','trade-value-paths']){
    const f=page.locator('#memory-'+id);if(await f.count()){
     await page.addStyleTag({content:'.toolbar,.skip-link{visibility:hidden!important}'});
     await f.screenshot({path:path.join(dir,`figure-p${n}-memory-${id}-both-desktop.png`)});
    }
   }
  }
  await page.close();
 }
 await browser.close();
 const failed=results.filter(r=>!r.visible||r.wrong||r.spills.length||!r.hasCitation||r.errors.length||r.remote.length);
 fs.writeFileSync(path.join(__dirname,'visual-display-checks.json'),JSON.stringify({results,failed},null,2));
 console.log(JSON.stringify({cases:results.length,failed},null,2));process.exitCode=failed.length?1:0;
})();
