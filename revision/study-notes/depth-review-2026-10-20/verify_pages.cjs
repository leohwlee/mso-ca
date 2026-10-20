const { chromium } = require('C:/Users/leohw/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const {pathToFileURL}=require('node:url');
const path=require('node:path'),fs=require('node:fs');
(async()=>{
 const browser=await chromium.launch({headless:true,executablePath:'C:/Users/leohw/AppData/Local/ms-playwright/chromium-1228/chrome-win64/chrome.exe'});
 if(process.argv.includes('--corrections')){
  const checks=[],dir=path.join(__dirname,'previews');fs.mkdirSync(dir,{recursive:true});
  for(const [device,width] of [['desktop',1440],['mobile',390]]){
   const page=await browser.newPage({viewport:{width,height:1050}});page.setDefaultTimeout(15000);
   await page.route(/^https?:/,r=>r.abort());
   for(const [n,selector,label] of [[1,'#terrorist-financing .concept-block:last-child','npo'],[2,'#inspection-investigation .concept-block:nth-of-type(3) .concept-list > li:nth-child(6)','retained-records'],[3,'#memory-ownership-boundary','trust'],[3,'#sector-specific .concept-block:last-child','applicability']])for(const lang of ['tc','en','both']){
    await page.goto(pathToFileURL(path.resolve(__dirname,`../part-${n}.html`)).href+`?lang=${lang}`);
    await page.evaluate(()=>document.fonts.ready);
    const target=page.locator(selector);
    checks.push({part:n,label,lang,device,visible:await target.isVisible(),overflow:await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth+2)});
    await page.addStyleTag({content:'header,.skip-link{visibility:hidden!important}'});
    await target.screenshot({path:path.join(dir,`correction-${label}-${lang}-${device}.png`)});
   }
   await page.close();
  }
  await browser.close();fs.writeFileSync(path.join(__dirname,'correction-display.json'),JSON.stringify(checks,null,2));
  const failed=checks.filter(x=>!x.visible||x.overflow);console.log(JSON.stringify({cases:checks.length,failed}));process.exitCode=failed.length?1:0;return;
 }
 if(process.argv.includes('--additions')){
  const checks=[];
  for(const [device,width] of [['desktop',1440],['mobile',390]]){
   const page=await browser.newPage({viewport:{width,height:1050}});
   await page.route(/^https?:/,r=>r.abort());
   for(const [n,selector,label] of [[1,'#money-laundering .concept-block:last-child','predicate'],[1,'#risk-assessment .concept-block:last-child','securities'],[2,'#other-sector-regimes .concept-block >> nth=3','assets'],[2,'#other-sector-regimes .concept-block >> nth=5','cooperation'],[2,'#other-sector-regimes .concept-block:last-child','dpms-report'],[5,'#risk-based .concept-block:last-child','derisking'],[6,'#beneficial-owners .concept-block:last-child','scr'],[7,'#reporting-duty .concept-block:last-child','intelligence']])for(const lang of ['tc','en','both']){
    await page.goto(pathToFileURL(path.resolve(__dirname,`../part-${n}.html`)).href+`?lang=${lang}`);
    await page.evaluate(()=>document.fonts.ready);
    const target=page.locator(selector);
    const heading=await target.locator('h3').textContent();
    const expected={assets:'limits of VA client-asset protection',cooperation:'SFC cross-border VA cooperation conditions'}[label];
    if(expected&&!heading.includes(expected))throw new Error('Wrong preview target: '+label+' / '+heading);
    checks.push({part:n,label,heading,lang,device,visible:await target.isVisible(),overflow:await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth+2)});
    // Content-only export: sticky navigation otherwise overlays a long element capture.
    // All display assertions above run before this screenshot-only adjustment.
    await page.addStyleTag({content:'header,.skip-link{visibility:hidden!important}'});
    await target.screenshot({path:path.join(__dirname,'previews',`source-${label}-${lang}-${device}.png`)});
   }
   await page.close();
  }
  await browser.close();fs.writeFileSync(path.join(__dirname,'source-additions-display.json'),JSON.stringify(checks,null,2));
  const failed=checks.filter(x=>!x.visible||x.overflow);console.log(JSON.stringify({cases:checks.length,failed}));process.exitCode=failed.length?1:0;return;
 }
 const targets=['international','grant-renewal','core-duties','licensing-actions','roles','representatives','training'];
 const partial=process.argv.includes('--part4'),numbers=partial?[4]:[1,2,3,4,5,6,7],suffix=partial?'-final-part4':'';
 const results=[],dir=path.join(__dirname,'previews');fs.mkdirSync(dir,{recursive:true});
 for(const [device,width,height] of [['desktop',1440,1050],['mobile',390,844]]){
  const page=await browser.newPage({viewport:{width,height}});const errors=[],remote=[];
  page.on('pageerror',e=>errors.push(e.message));await page.route(/^https?:/,r=>{remote.push(r.request().url());return r.abort()});
  for(const n of numbers)for(const lang of ['tc','en','both']){
   await page.goto(pathToFileURL(path.resolve(__dirname,`../part-${n}.html`)).href+`?lang=${lang}`);
   await page.evaluate(()=>document.fonts.ready);
   const state=await page.evaluate(({lang,n})=>{
    const root=document.documentElement;
    const spills=[...document.querySelectorAll('main *,header *,aside *')].filter(e=>{const r=e.getBoundingClientRect();const scrollParent=(()=>{for(let p=e.parentElement;p;p=p.parentElement){const s=getComputedStyle(p);if(['auto','scroll'].includes(s.overflowX)&&p.scrollWidth>p.clientWidth+2)return true}return false})();return !scrollParent&&r.width>0&&(r.right>innerWidth+2||r.left < -2)&&getComputedStyle(e).position!=='absolute'}).map(e=>({tag:e.tagName,class:e.className,text:e.textContent.slice(0,45)}));
    const wrong=[...document.querySelectorAll(lang==='tc'?'.en':lang==='en'?'.tc':'[data-no-match]')].filter(e=>getComputedStyle(e).display!=='none'&&e.getBoundingClientRect().height>0).length;
    return {language:document.body.dataset.lang,wrongLanguageVisible:wrong,overflow:root.scrollWidth>innerWidth+2,spills:spills.slice(0,8),sections:document.querySelectorAll('.chapter').length,citations:document.querySelectorAll('.source-citation a').length,practice:document.querySelector('.practice-link').href,partLinks:[...document.querySelectorAll('.part-nav a')].every(a=>a.href.includes('lang='+lang))};
   },{lang,n});
   await page.locator('#'+targets[n-1]).evaluate(e=>window.scrollTo(0,e.getBoundingClientRect().top+scrollY-150));
   await page.screenshot({path:path.join(dir,`part-${n}-${lang}-${device}.png`)});
   // Exercise visible language controls, not just query parameters.
   await page.getByRole('button',{name:lang==='tc'?'English':'繁體中文',exact:true}).click();
   const switched=await page.locator('body').getAttribute('data-lang');
   results.push({part:n,lang,device,...state,switched,errors:[...errors],remoteRequests:[...remote]});
  }
  await page.close();
 }
 const integration=[];
 const page=await browser.newPage({viewport:{width:390,height:844}});
 const errors=[],remote=[];
 page.on('pageerror',e=>errors.push(e.message));
 await page.route(/^https?:/,r=>{remote.push(r.request().url());return r.abort()});
 for(const n of numbers)for(const lang of ['tc','en','both']){
  await page.goto(pathToFileURL(path.resolve(__dirname,`../part-${n}.html`)).href+`?lang=${lang}`);
  await page.locator('.practice-link').click();
  await page.locator('#btn-practice').waitFor();
  const selected=await page.locator('#pmods .chip[aria-pressed="true"]').evaluateAll(es=>es.map(e=>Number(e.dataset.pm)));
  const appLang=await page.locator('#langseg .on').getAttribute('data-lang');
  await page.locator('#btn-practice').click();
  await page.locator('#opts .opt').first().waitFor();
  const returnLink=await page.locator('.study-entry').getAttribute('href');
  integration.push({part:n,lang,selected,appLang,started:true,returnLink,errors:[...errors],remoteRequests:[...remote]});
 }
 const indexChecks=[];
 for(const width of (partial?[]:[390,1440]))for(const lang of ['tc','en','both']){
  await page.setViewportSize({width,height:900});
  await page.goto(pathToFileURL(path.resolve(__dirname,'../index.html')).href+`?lang=${lang}`);
  indexChecks.push(await page.evaluate(({width,lang})=>({width,lang,actual:document.body.dataset.lang,overflow:document.documentElement.scrollWidth>innerWidth+2,partLinks:[...document.querySelectorAll('a[href*="part-"]')].map(a=>a.getAttribute('href'))}),{width,lang}));
 }
 await page.close();await browser.close();
 fs.writeFileSync(path.join(__dirname,'integration-checks'+suffix+'.json'),JSON.stringify({integration,indexChecks},null,2));
 fs.writeFileSync(path.join(__dirname,'browser-checks'+suffix+'.json'),JSON.stringify(results,null,2));
 const failures=results.filter(r=>r.overflow||r.spills.length||r.wrongLanguageVisible||r.errors.length||r.remoteRequests.length||r.language!==r.lang||!r.partLinks||!r.practice.includes('part='+r.part)||!r.practice.includes('lang='+r.lang)||r.switched==r.lang);
 const integrationFailures=integration.filter(r=>r.appLang!==r.lang||r.selected.join(',')!==String(r.part)||!r.returnLink.includes('part-'+r.part+'.html')||!r.returnLink.includes('lang='+r.lang)||r.errors.length||r.remoteRequests.length);
 const indexFailures=indexChecks.filter(r=>r.actual!==r.lang||r.overflow||r.partLinks.length<7||r.partLinks.some(l=>!l.includes('lang='+r.lang)));
 console.log(JSON.stringify({cases:results.length,failures,practiceCases:integration.length,integrationFailures,indexCases:indexChecks.length,indexFailures},null,2));process.exitCode=failures.length||integrationFailures.length||indexFailures.length?1:0;
})();
