const {chromium}=require('C:/Users/leohw/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto'),{pathToFileURL}=require('node:url');
const dir=__dirname,root=path.resolve(dir,'..'),shots=path.join(dir,'previews-b');
const norm=s=>s.replace(/\s+/g,' ').trim();
const fingerprint=Object.fromEntries([...Array.from({length:7},(_,i)=>`part-${i+1}.html`),'style.css','build.py','visual_render.py','visual_panels.py'].map(f=>[f,crypto.createHash('sha256').update(fs.readFileSync(path.join(root,f))).digest('hex')]));
const url=(n,lang,id='')=>pathToFileURL(path.join(root,`part-${n}.html`)).href+`?lang=${lang}`+(id?'#'+id:'');
const settle=async page=>{await page.evaluate(()=>document.fonts.ready);await page.evaluate(()=>new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r))))};
const position=async(page,id)=>page.evaluate(id=>{
 const el=document.getElementById(id),title=el?.querySelector('h2,h3')||el, r=title?.getBoundingClientRect(),h=document.querySelector('.toolbar').getBoundingClientRect();
 return {id,exists:!!el,title:title?.innerText,top:r?.top,bottom:r?.bottom,headerBottom:h.bottom,gap:r?r.top-h.bottom:null,visible:!!r&&r.top>=h.bottom-1&&r.top<innerHeight,actualLang:document.body.dataset.lang,offset:getComputedStyle(document.documentElement).getPropertyValue('--anchor-offset'),scrollY};
},id);
(async()=>{
 const browser=await chromium.launch({headless:true,executablePath:'C:/Users/leohw/AppData/Local/ms-playwright/chromium-1228/chrome-win64/chrome.exe'});
 const data={fingerprint,states:[],anchors:[],languageChanges:[],crossPart:[],trigger:[],screenshots:[]},fails=[];
 try{
  for(const width of [390,900,1440]){
   const context=await browser.newContext({viewport:{width,height:1000},reducedMotion:'reduce'});
   const page=await context.newPage();let errors=[],remote=[];
   page.on('pageerror',e=>errors.push(e.message));
   await page.route(/^https?:/,r=>{remote.push(r.request().url());return r.abort()});
   const cdp=await context.newCDPSession(page);
   for(const lang of ['tc','en','both'])for(let n=1;n<=7;n++){
    errors=[];remote=[];
    await page.goto(url(n,lang));await settle(page);
    const ax=(await cdp.send('Accessibility.getFullAXTree')).nodes;
    const expected=await page.evaluate(()=>{
     const isVisible=e=>{const r=e.getBoundingClientRect(),s=getComputedStyle(e);return r.width>0&&r.height>0&&s.display!=='none'&&s.visibility!=='hidden'};
     return {
      headers:[...document.querySelectorAll('thead th')].map(e=>e.innerText.replace(/\s+/g,' ').trim()),
      tables:[...document.querySelectorAll('table')].map(e=>({id:e.closest('figure').id,labelledby:e.getAttribute('aria-labelledby'),title:(document.getElementById(e.getAttribute('aria-labelledby'))?.innerText||'').replace(/\s+/g,' ').trim()})),
      units:[...document.querySelectorAll('.numeric-unit')].filter(isVisible).map(e=>{const r=document.createRange();r.selectNodeContents(e);return {text:e.innerText,tops:[...new Set([...r.getClientRects()].map(r=>Math.round(r.top)))],left:e.getBoundingClientRect().left,right:e.getBoundingClientRect().right,whiteSpace:getComputedStyle(e).whiteSpace}}),
      ids:[...document.querySelectorAll('.memory-panel')].map(e=>e.id),
      crossLinks:[...document.querySelectorAll('.visual-links a')].map(a=>({href:a.href,label:a.innerText})).filter(a=>new URL(a.href).pathname!==location.pathname&&new URL(a.href).hash),
      overflow:document.documentElement.scrollWidth>innerWidth+2
     };
    });
    const actualHeaders=ax.filter(n=>!n.ignored&&n.role?.value==='columnheader').map(n=>norm(n.name?.value||''));
    const actualTables=ax.filter(n=>!n.ignored&&n.role?.value==='table').map(n=>norm(n.name?.value||''));
    const state={part:n,lang,width,expectedHeaders:expected.headers,actualHeaders,expectedTables:expected.tables,actualTables,units:expected.units,overflow:expected.overflow,errors:[...errors],remote:[...remote]};
    data.states.push(state);
    if(JSON.stringify(expected.headers)!==JSON.stringify(actualHeaders))fails.push({type:'headers',part:n,lang,width,expected:expected.headers,actual:actualHeaders});
    if(JSON.stringify(expected.tables.map(t=>t.title))!==JSON.stringify(actualTables))fails.push({type:'table-names',part:n,lang,width,expected:expected.tables.map(t=>t.title),actual:actualTables});
    if(expected.units.some(u=>u.tops.length!==1||u.left<0||u.right>width))fails.push({type:'numeric-wrap',part:n,lang,width,units:expected.units.filter(u=>u.tops.length!==1||u.left<0||u.right>width)});
    for(const id of expected.ids){
     await page.goto(url(n,lang,id));await settle(page);
     const p=await position(page,id);data.anchors.push({part:n,lang,width,...p});
     if(!p.visible)fails.push({type:'direct-anchor',part:n,lang,width,...p});
    }
    const id=expected.ids[0], nextLang={tc:'both',both:'en',en:'tc'}[lang];
    await page.goto(url(n,lang,id));await settle(page);
    const before=await position(page,id);
    const languageButton=await page.locator(`[data-language="${nextLang}"]`).boundingBox();
    await page.mouse.click(languageButton.x+languageButton.width/2,languageButton.y+languageButton.height/2);await settle(page);
    const after=await position(page,id);
    const lc={part:n,width,from:lang,to:nextLang,before,after};
    data.languageChanges.push(lc);
    if(!after.visible){
     const file=`final-language-${n}-${lang}-to-${nextLang}-${width}.png`;
     await page.screenshot({path:path.join(shots,file)});data.screenshots.push(file);
     fails.push({type:'language-anchor',...lc,screenshot:file});
    }
    for(const link of expected.crossLinks){
     await page.goto(url(n,lang));await settle(page);
     await page.locator('.visual-links a[href="'+link.href.replaceAll('"','\\"')+'"]').first().click();
     await settle(page);
     const dest=new URL(page.url());const p=await position(page,decodeURIComponent(dest.hash.slice(1)));
     const cp={part:n,lang,width,href:dest.href,...p};data.crossPart.push(cp);
     if(!p.visible||p.actualLang!==lang)fails.push({type:'cross-part',...cp});
    }
    if(n===6){
     await page.goto(url(n,lang,'memory-cdd-trigger-tree'));await settle(page);
     data.trigger.push(await page.locator('#memory-cdd-trigger-tree').evaluate((e,{width,lang})=>({width,lang,caseCount:e.querySelectorAll('.trigger-case').length,crossCutting:e.querySelectorAll('.trigger-case.cross-cutting').length,decisionNodes:e.querySelectorAll('.decision-node').length,continuations:e.querySelectorAll('.decision-continue').length,intro:e.querySelector('.visual-intro')?.innerText,cases:[...e.querySelectorAll('.trigger-case')].map(c=>c.innerText)}),{width,lang}));
     if(lang==='both'&&width===900){
      const file='final-cdd-trigger-both-900.png';
      await page.screenshot({path:path.join(shots,file)});data.screenshots.push(file);
     }
    }
    console.log(`Verified ${n}/${lang}/${width}; issues so far ${fails.length}`);
   }
   await context.close();
  }
 }finally{await browser.close();data.failures=fails;fs.writeFileSync(path.join(dir,'final-assessment-b-browser.json'),JSON.stringify(data,null,2));}
 data.failures=fails;
 fs.writeFileSync(path.join(dir,'final-assessment-b-browser.json'),JSON.stringify(data,null,2));
 const summary={states:data.states.length,headersByMode:['tc','en','both'].flatMap(lang=>[390,900,1440].map(width=>({lang,width,count:data.states.filter(s=>s.lang===lang&&s.width===width).reduce((a,s)=>a+s.actualHeaders.length,0)}))),anchors:data.anchors.length,languageChanges:data.languageChanges.length,crossPart:data.crossPart.length,triggerStates:data.trigger.length,failures:fails};
 fs.writeFileSync(path.join(dir,'final-assessment-b-summary.json'),JSON.stringify(summary,null,2));
 console.log(JSON.stringify(summary,null,2));
})().catch(e=>{console.error(e);process.exitCode=1});
