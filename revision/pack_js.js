
(function(){
  var root=document.documentElement;
  var L={en:{recall:'Recall mode',recallOn:'Recall mode: on'},
         tc:{recall:'自測模式',recallOn:'自測模式：開'}};
  var lang=root.getAttribute('data-lang')||'both';
  function t(k){ return lang==='both' ? L.en[k]+' · '+L.tc[k] : L[lang][k]; }
  function all(sel,ctx){ return Array.prototype.slice.call((ctx||document).querySelectorAll(sel)); }

  var bar=document.querySelector('.bar');
  var docs=all('.doc'), docBtns=all('.docnav button');
  var rc=document.getElementById('recall');
  var on=false; try{ on=localStorage.getItem('pack-recall')==='1'; }catch(e){}

  function setBarHeight(){ root.style.setProperty('--barh', (bar.offsetHeight||52)+'px'); }

  var toggle=document.getElementById('outline-toggle');
  var wide=function(){ return window.innerWidth>=1180; };
  var open;
  try{ var saved=localStorage.getItem('pack-outline'); open = saved===null ? wide() : saved==='1'; }
  catch(e){ open=wide(); }
  function paintOutline(){
    root.setAttribute('data-outline', open?'open':'closed');
    toggle.setAttribute('aria-expanded', open?'true':'false');
  }
  toggle.addEventListener('click',function(){
    open=!open;
    try{ localStorage.setItem('pack-outline', open?'1':'0'); }catch(e){}
    paintOutline(); markChapter();
  });
  document.addEventListener('click',function(ev){
    var a=ev.target.closest?ev.target.closest('.chapnav a'):null;
    if(a && !wide()){ open=false; paintOutline(); }
  });
  paintOutline();

  function markChapter(){
    var id=root.getAttribute('data-doc');
    var nav=document.querySelector('.chapnav[data-for="'+id+'"]');
    if(!nav) return;
    var offset=(bar.offsetHeight||52)+26;
    var secs=all('#'+id+' .sec'), active=secs.length?secs[0].id:null;
    secs.forEach(function(s){ if(s.getBoundingClientRect().top<=offset) active=s.id; });
    all('a',nav).forEach(function(a){
      a.setAttribute('aria-current', a.getAttribute('href')==='#'+active ? 'true' : 'false');
    });
  }

  function paint(){
    root.classList.toggle('recall',on);
    rc.setAttribute('aria-pressed',on?'true':'false');
    rc.textContent=on?t('recallOn'):t('recall');
    all('.seg button').forEach(function(b){ b.setAttribute('aria-pressed',b.getAttribute('data-lang')===lang?'true':'false'); });
    all('svg.fig').forEach(function(s){
      var a=s.getAttribute(lang==='tc'?'data-aria-tc':'data-aria-en');
      if(a) s.setAttribute('aria-label',a);
    });
    root.setAttribute('lang',lang==='tc'?'zh-Hant':'en');
    setBarHeight(); markChapter();
  }

  function setLang(l){ lang=l; root.setAttribute('data-lang',l); try{ localStorage.setItem('pack-lang',l); }catch(e){} paint(); }
  all('.seg button').forEach(function(b){ b.addEventListener('click',function(){ setLang(b.getAttribute('data-lang')); }); });

  function showDoc(id,scroll){
    if(!docs.some(function(d){ return d.id===id; })) id=docs[0].id;
    docs.forEach(function(d){ d.hidden = d.id!==id; });
    docBtns.forEach(function(b){ b.setAttribute('aria-pressed',b.getAttribute('data-doc')===id?'true':'false'); });
    root.setAttribute('data-doc',id);
    try{ localStorage.setItem('pack-doc',id); }catch(e){}
    if(scroll) window.scrollTo(0,0);
    setBarHeight(); markChapter();
    return id;
  }
  docBtns.forEach(function(b){ b.addEventListener('click',function(){
    var id=b.getAttribute('data-doc');
    showDoc(id,true);
    if(history.replaceState) history.replaceState(null,'','#'+id); else location.hash=id;
  }); });

  function target(){
    var h=(location.hash||'').slice(1);
    if(!h) return null;
    if(h==='doc-cdd') h='doc-s2'; else if(h.indexOf('cdd-')===0) h='s2-'+h.slice(4);
    var el=document.getElementById(h);
    if(!el) return null;
    var d=el.classList.contains('doc')?el:(el.closest?el.closest('.doc'):null);
    return d?{doc:d.id, el:el}:null;
  }
  function route(scroll){
    var tg=target();
    if(tg){ showDoc(tg.doc,false); if(scroll&&tg.el.scrollIntoView) tg.el.scrollIntoView(); return; }
    var saved=null; try{ saved=localStorage.getItem('pack-doc'); }catch(e){}
    showDoc(saved||docs[0].id,false);
  }
  window.addEventListener('hashchange',function(){ route(true); });

  rc.addEventListener('click',function(){
    on=!on; try{ localStorage.setItem('pack-recall',on?'1':'0'); }catch(e){}
    if(!on) all('.answer.shown').forEach(function(el){ el.classList.remove('shown'); });
    paint();
  });
  document.addEventListener('click',function(ev){
    if(!on) return;
    var a=ev.target.closest?ev.target.closest('.answer'):null;
    if(a) a.classList.toggle('shown');
  });
  document.addEventListener('keydown',function(ev){
    if(ev.key!=='Enter'&&ev.key!==' ') return;
    var a=ev.target.closest&&ev.target.closest('.answer');
    if(a&&on){ ev.preventDefault(); a.classList.toggle('shown'); }
  });

  var ticking=false;
  window.addEventListener('scroll',function(){
    if(ticking) return;
    ticking=true;
    requestAnimationFrame(function(){ markChapter(); ticking=false; });
  },{passive:true});
  window.addEventListener('resize',function(){ setBarHeight(); markChapter(); });

  route(true);
  paint();
})();
