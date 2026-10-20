const {chromium}=require('C:/Users/leohw/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const fs=require('node:fs'),path=require('node:path'),{pathToFileURL}=require('node:url');
(async()=>{
 const browser=await chromium.launch({headless:true,executablePath:'C:/Users/leohw/AppData/Local/ms-playwright/chromium-1228/chrome-win64/chrome.exe'});
 const results=[];
 try{
  for(const width of [390,900,1440]){
   const context=await browser.newContext({viewport:{width,height:900},reducedMotion:'reduce'});
   const page=await context.newPage();await page.route(/^https?:/,r=>r.abort());
   for(let n=1;n<=7;n++){
    await page.goto(pathToFileURL(path.resolve(__dirname,`../part-${n}.html`)).href+'?lang=both');
    await page.evaluate(()=>document.fonts.ready);
    await page.keyboard.press('Tab');await page.keyboard.press('Enter');
    const skip=await page.evaluate(()=>({active:document.activeElement.tagName,id:document.activeElement.id,top:document.activeElement.getBoundingClientRect().top,headerBottom:document.querySelector('header').getBoundingClientRect().bottom}));
    await page.goto(pathToFileURL(path.resolve(__dirname,`../part-${n}.html`)).href+'?lang=both');
    await page.keyboard.press('Tab');await page.keyboard.press('Tab');await page.keyboard.press('Tab');await page.keyboard.press('Enter');
    const switched=await page.locator('body').getAttribute('data-lang');
    const cdp=await context.newCDPSession(page);
    const ax=await cdp.send('Accessibility.getFullAXTree');
    const cols=ax.nodes.filter(n=>n.role?.value==='columnheader'&&!n.ignored).map(n=>n.name.value);
    const data=await page.evaluate(()=>{
     const tableData=[...document.querySelectorAll('table')].map(t=>({figure:t.closest('figure')?.id,columnCount:t.querySelectorAll('thead th').length,headDisplay:getComputedStyle(t.querySelector('thead')).display,cellLabels:[...t.querySelectorAll('.cell-label')].map(e=>({text:e.innerText,hidden:e.getAttribute('aria-hidden')})),labelledby:t.getAttribute('aria-labelledby')}));
     const decisions=[...document.querySelectorAll('.decision-tree')].map(t=>({figure:t.closest('figure')?.id,nodes:[...t.children].map(e=>({childOrder:[...e.children].map(n=>n.className),test:e.querySelector('.decision-condition')?.innerText,yes:e.querySelector('.decision-outcome')?.innerText,no:e.querySelector('.decision-continue')?.innerText}))}));
     return {tableData,decisions};
    });
    results.push({part:n,width,skip,keyboardSwitched:switched,accessibleColumnHeaders:cols,...data});
    if(n===3&&width===900){
     await page.locator('#memory-money-boundaries').evaluate(e=>window.scrollTo(0,e.getBoundingClientRect().top+scrollY-145));
     await page.screenshot({path:path.join(__dirname,'previews-b','threshold-wrap-en-900-viewport.png')});
    }
    await cdp.detach();
   }
   await context.close();
  }
 }finally{await browser.close();}
 fs.writeFileSync(path.join(__dirname,'assessment-b-accessibility.json'),JSON.stringify(results,null,2));
 console.log(JSON.stringify({cases:results.length,skipFailures:results.filter(r=>r.skip.id!=='content').map(r=>({part:r.part,width:r.width,skip:r.skip})),switchFailures:results.filter(r=>r.keyboardSwitched!=='en').map(r=>({part:r.part,width:r.width})),tableHeaders:results.filter(r=>r.tableData.length).map(r=>({part:r.part,width:r.width,expected:r.tableData.reduce((a,t)=>a+t.columnCount,0),exposed:r.accessibleColumnHeaders.length}))},null,2));
})().catch(e=>{console.error(e);process.exitCode=1});
