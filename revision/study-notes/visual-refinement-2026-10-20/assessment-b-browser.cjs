const { chromium } = require('C:/Users/leohw/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const {pathToFileURL} = require('node:url');
const root = path.resolve(__dirname, '..');
const out = path.join(__dirname, 'previews-b');
fs.mkdirSync(out, {recursive: true});
const targets = Array.from({length:7}, (_,i)=>`part-${i+1}.html`);
const fingerprints = Object.fromEntries([...targets,'style.css','visual_render.py'].map(f=>[f,crypto.createHash('sha256').update(fs.readFileSync(path.join(root,f))).digest('hex')]));
const visible = el => {
  const b=el.getBoundingClientRect(), s=getComputedStyle(el);
  return b.width>0 && b.height>0 && s.display!=='none' && s.visibility!=='hidden';
};
(async()=>{
 const browser=await chromium.launch({headless:true,executablePath:'C:/Users/leohw/AppData/Local/ms-playwright/chromium-1228/chrome-win64/chrome.exe'});
 const results=[], keyboard=[], screenshots=[];
 try {
  for(const [device,width,height] of [['desktop',1440,1000],['intermediate',900,1000],['mobile',390,844]]) {
   const context=await browser.newContext({viewport:{width,height},reducedMotion:'reduce'});
   const page=await context.newPage();
   let errors=[],requests=[];
   page.on('pageerror',e=>errors.push(e.message));
   await page.route(/^https?:/,r=>{requests.push(r.request().url());return r.abort()});
   for(let n=1;n<=7;n++)for(const lang of ['tc','en','both']){
    errors=[];requests=[];
    await page.goto(pathToFileURL(path.join(root,`part-${n}.html`)).href+`?lang=${lang}`);
    await page.evaluate(()=>document.fonts.ready);
    const state=await page.evaluate(({n,lang,width,device})=>{
     const visible = el => {const b=el.getBoundingClientRect(),s=getComputedStyle(el);return b.width>0&&b.height>0&&s.display!=='none'&&s.visibility!=='hidden'};
     const rect = el => {const r=el.getBoundingClientRect();return {x:r.x,y:r.y,width:r.width,height:r.height,right:r.right,bottom:r.bottom}};
     const panels=[...document.querySelectorAll('.memory-panel')].map(p=>{
      const pr=p.getBoundingClientRect();
      const all=[...p.querySelectorAll('*')].filter(visible);
      const spills=all.filter(e=>{const r=e.getBoundingClientRect();return r.left<pr.left-2||r.right>pr.right+2}).map(e=>({tag:e.tagName,class:e.className,text:e.textContent.trim().slice(0,100),rect:rect(e)}));
      const overflow=all.filter(e=>e.clientWidth>0&&e.scrollWidth>e.clientWidth+2&&getComputedStyle(e).overflowX!=='visible').map(e=>({tag:e.tagName,class:e.className,client:e.clientWidth,scroll:e.scrollWidth,text:e.textContent.trim().slice(0,100)}));
      const textNodes=all.filter(e=>[...e.childNodes].some(c=>c.nodeType===3&&c.textContent.trim()));
      const small=textNodes.filter(e=>parseFloat(getComputedStyle(e).fontSize)<13).map(e=>({tag:e.tagName,class:e.className,size:getComputedStyle(e).fontSize,text:e.textContent.trim().slice(0,70)}));
      const narrow=all.filter(e=>e.matches('th,td,.path-node,.relation-entity')&&e.getBoundingClientRect().width<100).map(e=>({tag:e.tagName,class:e.className,width:e.getBoundingClientRect().width,text:e.textContent.trim().slice(0,110)}));
      const tables=[...p.querySelectorAll('table')].map(t=>({caption:!!t.querySelector('caption'),ariaLabel:t.getAttribute('aria-label'),labelledby:t.getAttribute('aria-labelledby'),heads:[...t.querySelectorAll('thead th')].map(h=>({text:h.innerText,scope:h.getAttribute('scope'),visible:visible(h)})),rowHeads:[...t.querySelectorAll('tbody th')].map(h=>({scope:h.getAttribute('scope'),text:h.innerText.slice(0,100)}))}));
      return {id:p.id,heading:p.querySelector('h3')?.innerText,rect:rect(p),spills,overflow,small,narrow,tables,branchCount:p.querySelectorAll('.decision-node').length,hasCitation:!!p.querySelector('.source-citation a')};
     });
     const scrollParents=el=>{for(let p=el.parentElement;p;p=p.parentElement){const s=getComputedStyle(p);if(['auto','scroll'].includes(s.overflowX)&&p.scrollWidth>p.clientWidth+2)return true}return false};
     const spills=[...document.querySelectorAll('main *, header *, aside *')].filter(visible).filter(e=>{const r=e.getBoundingClientRect();return !scrollParents(e)&&(r.right>innerWidth+2||r.left<-2)&&getComputedStyle(e).position!=='absolute'}).map(e=>({tag:e.tagName,class:e.className,text:e.textContent.trim().slice(0,80)}));
     const wrong=lang==='both'?[]:[...document.querySelectorAll(lang==='tc'?'.en':'.tc')].filter(visible);
     return {part:n,lang,width,device,actualLang:document.body.dataset.lang,rootWidth:document.documentElement.scrollWidth,viewport:innerWidth,spills,wrongLanguage:wrong.length,panels,controls:[...document.querySelectorAll('.languages button')].map(b=>({text:b.innerText,pressed:b.getAttribute('aria-pressed'),rect:rect(b)}))};
    },{n,lang,width,device});
    state.errors=[...errors]; state.remoteRequests=[...requests];results.push(state);
    // Preserve actual sticky header in viewport captures.
    const first=page.locator('.memory-panel').first();
    await first.evaluate(el=>window.scrollTo(0,el.getBoundingClientRect().top+scrollY-175));
    const shot=`part-${n}-${lang}-${device}.png`;
    await page.screenshot({path:path.join(out,shot)});
    screenshots.push({file:shot,part:n,lang,device,type:'viewport'});
    // Element captures of every bilingual figure, plus all mono-language figures
    // at the intermediate width where available width is most constrained.
    if(lang==='both'||device==='intermediate'){
     // Screenshot-only unstick: assertions above use the shipped CSS.
     await page.addStyleTag({content:'.toolbar,.skip-link{visibility:hidden!important}'});
     for(const panel of state.panels){
      const name=`figure-p${n}-${panel.id}-${lang}-${device}.png`;
      await page.locator('#'+panel.id).screenshot({path:path.join(out,name)});
      screenshots.push({file:name,part:n,lang,device,panel:panel.id,type:'content-only'});
     }
    }
    if(lang==='both'&&[1,6,7].includes(n)){
     await page.goto(pathToFileURL(path.join(root,`part-${n}.html`)).href+'?lang=both');
     const steps=[];
     for(let t=0;t<13;t++){
      await page.keyboard.press('Tab');
      steps.push(await page.evaluate(()=>{
       const e=document.activeElement,r=e.getBoundingClientRect(),s=getComputedStyle(e);
       return {tag:e.tagName,class:e.className,text:e.innerText?.slice(0,90),outline:s.outline,offset:s.outlineOffset,rect:{x:r.x,y:r.y,width:r.width,height:r.height},focusVisible:e.matches(':focus-visible')};
      }));
     }
     const cdp=await context.newCDPSession(page);
     const ax=await cdp.send('Accessibility.getFullAXTree');
     const roles=ax.nodes.filter(n=>['table','row','rowheader','columnheader','cell'].includes(n.role?.value)).map(n=>({role:n.role?.value,name:n.name?.value,ignored:n.ignored}));
     keyboard.push({part:n,device,steps,tableRoles:roles});
     await cdp.detach();
    }
    console.log(`Checked part ${n} ${lang} ${device}`);
   }
   await context.close();
  }
 }finally{await browser.close();}
 fs.writeFileSync(path.join(__dirname,'assessment-b-browser.json'),JSON.stringify({fingerprints,results,keyboard,screenshots},null,2));
 const summary={cases:results.length,panels:results.reduce((a,r)=>a+r.panels.length,0),screenshots:screenshots.length,rootOverflow:results.filter(r=>r.rootWidth>r.viewport+2).map(r=>[r.part,r.lang,r.device]),pageSpills:results.filter(r=>r.spills.length).map(r=>[r.part,r.lang,r.device,r.spills]),panelSpills:results.flatMap(r=>r.panels.filter(p=>p.spills.length).map(p=>({part:r.part,lang:r.lang,device:r.device,id:p.id,spills:p.spills}))),clipped:results.flatMap(r=>r.panels.filter(p=>p.overflow.length).map(p=>({part:r.part,lang:r.lang,device:r.device,id:p.id,overflow:p.overflow}))),languageErrors:results.filter(r=>r.wrongLanguage||r.actualLang!==r.lang),errors:results.filter(r=>r.errors.length||r.remoteRequests.length)};
 fs.writeFileSync(path.join(__dirname,'assessment-b-browser-summary.json'),JSON.stringify(summary,null,2));
 console.log(JSON.stringify(summary,null,2));
})().catch(e=>{console.error(e);process.exitCode=1});
