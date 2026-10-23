"""Render source-authored manuscripts. This builder never reads the bank.

Run gap_check.py separately after authoring; it does not supply page content.
"""
from __future__ import annotations
import argparse, base64, copy, hashlib, html, importlib, json, re
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit
from html.parser import HTMLParser

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
PARTS={n:copy.deepcopy(importlib.import_module(f'part{n}').PART) for n in range(1,8)}
from memory_panels import PANELS, EMPHASIS
from essentials import ADDITIONS
from visual_panels import apply as apply_visuals
from visual_render import render as render_visual
from traps import TRAPS
from tiers import TIERS, LABELS as TIER_LABELS, PREFIXES as TIER_PREFIXES
from rulings import MARKS as RULING_MARKS, ISSUES as RULING_ISSUES, DECISIONS as RULING_DECISIONS, RECORDS as RULING_RECORDS
from amounts import GROUPS as AMOUNT_GROUPS
for number, additions in ADDITIONS.items():
    for topic, blocks in additions.items():
        next(section for section in PARTS[number]['sections'] if section['id']==topic)['blocks'].extend(blocks)
PANELS=apply_visuals(PANELS,PARTS)
CATALOG=json.loads((ROOT/'docs/catalog.json').read_text(encoding='utf-8'))
DOCS={d['id']:d for d in CATALOG['documents']}
CALLS_TEXT=(ROOT/'revision/CONFLICT-CALLS.md').read_text(encoding='utf-8')
def conflict_rows():
    rows={}
    for line in CALLS_TEXT.splitlines():
        if re.match(r'^\| [BWEN]\d+ \|',line):
            cells=line[2:-2].split(' | ');assert len(cells)==4,line
            rows[cells[0]]=dict(question=cells[1],sources=cells[2].split('<br>'),decision=cells[3])
    return rows
CALLS=conflict_rows()
def resolve_rulings():
    """Tie each ruling mark to exactly one manuscript point, or to a whole figure."""
    points,panels={},{}
    for n,sections in RULING_MARKS.items():
        for sid,marks in sections.items():
            section=next(s for s in PARTS[n]['sections'] if s['id']==sid)
            for mark in marks:
                if mark['anchor'].startswith('panel:'):
                    key=mark['anchor'][6:]
                    assert key in {panel['id'] for panel in PANELS[n].get(sid,[])} and key not in panels,(n,sid,key)
                    panels[key]=mark
                    continue
                hits=[(bi,pi) for bi,b in enumerate(section['blocks']) for pi,point in enumerate(b['points']) if mark['anchor'] in point['en']]
                assert len(hits)==1,(n,sid,mark['anchor'],hits)
                assert (n,sid,*hits[0]) not in points,(n,sid,mark['anchor'])
                points[(n,sid,*hits[0])]=mark
    return points,panels
RULED_POINTS,RULED_PANELS=resolve_rulings()
e=html.escape
def normal(text):return re.sub(r'\s+',' ',text).casefold()
def keep_units(markup):
    # Keep the mathematical boundary with its value; neither means the same alone.
    return re.sub(r'(?:≥|≤|&gt;|&lt;)\s*(?:HK\$\s*)?\d[\d,]*(?:\.\d+)?%?',lambda m:'<span class="numeric-unit">'+m.group()+'</span>',markup)
def pair(value):
    if value['tc']==value['en']:return '<span class="shared">'+keep_units(e(value['tc']))+'</span>'
    return ''.join(f'<span class="{lang}" lang="{"zh-Hant" if lang=="tc" else "en"}">'+keep_units(e(value[lang]))+'</span>' for lang in ('tc','en'))
def label(tc,en):return pair(dict(tc=tc,en=en))

def emphasized_pair(value,suffix=None):
    """Add a few exact lexical anchors without rewriting any source-authored text."""
    out=[];suffix=suffix or {}
    for lang in ('tc','en'):
        terms=sorted(EMPHASIS[lang],key=len,reverse=True)
        pattern='|'.join(re.escape(t) for t in terms)
        if lang=='en':pattern=r'(?<![A-Za-z])(?:'+pattern+r')(?![A-Za-z])'
        chunks=[];end=0
        for i,m in enumerate(re.finditer(pattern,value[lang],re.I)):
            if i==3:break
            chunks.extend((e(value[lang][end:m.start()]),'<strong class="recall-term">'+e(m.group())+'</strong>'));end=m.end()
        chunks.append(e(value[lang][end:]))
        out.append(f'<span class="{lang}" lang="{"zh-Hant" if lang=="tc" else "en"}">'+keep_units(''.join(chunks))+suffix.get(lang,'')+'</span>')
    return ''.join(out)

def compact_citations(refs):
    grouped={}
    for r in refs:
        grouped.setdefault(r['doc'],{'tc':[],'en':[]})
        for lang in ('tc','en'):
            if r['locator'][lang] not in grouped[r['doc']][lang]:grouped[r['doc']][lang].append(r['locator'][lang])
    return citations([dict(doc=doc,locator={lang:'; '.join(v[lang]) for lang in ('tc','en')}) for doc,v in grouped.items()])

def citations(refs):
    out=[]
    for r in refs:
        entries=[]
        for lang in ('tc','en'):
            ed=DOCS[r['doc']]['editions']['EN' if r['doc']=='24' else lang.upper()]
            translated=' · 中文為學習譯文；來源為英文原件' if r['doc']=='24' and lang=='tc' else ''
            entries.append(f'<div class="{lang}" lang="{"zh-Hant" if lang=="tc" else "en"}"><a href="../../docs/{e(quote(ed["path"],safe="/"))}" target="_blank" rel="noopener">{e(ed["file"])}</a><span class="locator">{e(r["locator"][lang]+translated)}</span></div>')
        out.append('<div class="source-citation">'+''.join(entries)+'</div>')
    return '<div class="citations">'+''.join(out)+'</div>'

def validate():
    used=set()
    for n,part in PARTS.items():
        ids=[]
        for s in part['sections']:
            ids.append(s['id'])
            for title in (s['title'],*(b['title'] for b in s['blocks'])):
                assert not re.search(r'which of the following|以下哪|下列哪|[?？]',title['tc']+' '+title['en'],re.I),title
            for b in s['blocks']:
                assert b['points'] and b['refs'],(n,s['id'])
                for point in b['points']:assert point['tc'].strip() and point['en'].strip()
                for r in b['refs']:
                    doc=r['doc'];assert '01'<=doc<='26',doc;used.add(doc)
                    assert normal(r['anchor']) in normal((ROOT/f'docs/text/EN/{doc}.txt').read_text(encoding='utf-8')),(n,s['id'],r)
                    for lang in ('TC','EN'):
                        ed=DOCS[doc]['editions']['EN' if doc=='24' else lang]
                        assert (ROOT/'docs'/ed['path']).is_file(),ed
        assert len(ids)==len(set(ids)),n
    assert used=={f'{n:02d}' for n in range(1,27)},sorted(used)
    panel_ids=[]
    def check_pairs(value):
        if isinstance(value,dict):
            if 'tc' in value or 'en' in value:
                assert value.get('tc','').strip() and value.get('en','').strip(),value
            for item in value.values():check_pairs(item)
        elif isinstance(value,list):
            for item in value:check_pairs(item)
    for n,sections in PANELS.items():
        for sid,panels in sections.items():
            assert sid in {s['id'] for s in PARTS[n]['sections']},(n,sid)
            for panel in panels:
                panel_ids.append(panel['id'])
                check_pairs(panel)
                assert panel['refs']
                if panel['kind']=='table':
                    assert 3 <= len(panel['headers']) <= 4
                    assert all(len(row)==len(panel['headers']) and all(cell['tc'] and cell['en'] for cell in row) for row in panel['rows'])
                if panel['kind']=='decision':
                    assert panel['nodes'][-1].get('no') or panel.get('end'),panel['id']
                    assert all(node.get('test') and node.get('yes') for node in panel['nodes'])
                if panel['kind']=='checklist':
                    # The count shown on a list card is the number of items, so every group needs some.
                    assert all(g['items'] for g in panel.get('groups') or [dict(items=panel['items'])]),panel['id']
                for row in panel.get('paths',[]):
                    assert len(row['nodes'])==len(row['edges'])+1,panel['id']
                for r in panel['refs']:
                    assert '01'<=r['doc']<='26'
                    assert normal(r['anchor']) in normal((ROOT/f'docs/text/EN/{r["doc"]}.txt').read_text(encoding='utf-8'))
    assert len(panel_ids)==len(set(panel_ids)),panel_ids
    # Every numbers-page row points at a real section and cites an anchored passage.
    for group in AMOUNT_GROUPS:
        check_pairs(group)
        for row in group['rows']:
            assert any(s['id']==row['section'] for s in PARTS[row['part']]['sections']),(group['id'],row['value']['en'])
            for r in row['refs']:
                assert '01'<=r['doc']<='26' and normal(r['anchor']) in normal((ROOT/f'docs/text/EN/{r["doc"]}.txt').read_text(encoding='utf-8')),(row['value']['en'],r)
    # Every block has one study tier; a title that already names a tier must agree.
    for n,part in PARTS.items():
        assert set(TIERS[n])=={s['id'] for s in part['sections']},n
        for s in part['sections']:
            letters=TIERS[n][s['id']]
            assert len(letters)==len(s['blocks']) and set(letters)<=set(TIER_LABELS),(n,s['id'])
            for letter,b in zip(letters,s['blocks']):
                for other,prefixes in TIER_PREFIXES.items():
                    if any(b['title'][lang].startswith(prefixes[lang]) for lang in ('tc','en')):assert other==letter,(n,s['id'],b['title']['en'])
    # Exam traps restate owner decisions, so each ID must exist in CONFLICT-CALLS.
    decisions=set(re.findall(r'^\| ([BWEN]\d+) \|',(ROOT/'revision/CONFLICT-CALLS.md').read_text(encoding='utf-8'),re.M))
    trap_ids=[]
    for n,sections in TRAPS.items():
        for sid,traps in sections.items():
            assert sid in {s['id'] for s in PARTS[n]['sections']},(n,sid)
            for trap in traps:
                check_pairs(trap['text']);trap_ids+=trap['ids']
                assert set(trap['ids'])<=decisions,trap['ids']
    assert len(trap_ids)==len(set(trap_ids)),trap_ids
    # Ruling marks name recorded decisions, or U notes that carry their own record.
    assert 'D26-20261020' in CALLS_TEXT
    marked=[i for mark in [*RULED_POINTS.values(),*RULED_PANELS.values()] for i in mark['ids']]
    for rid in set(marked)|set(trap_ids):
        assert rid in CALLS or rid=='D26' or (rid.startswith('U') and rid in RULING_RECORDS),rid
        assert rid in RULING_ISSUES and ruling_decision(rid),rid
        check_pairs(RULING_ISSUES[rid]);check_pairs(ruling_decision(rid))
    for mark in [*RULED_POINTS.values(),*RULED_PANELS.values()]:
        assert len(mark['ids'])==len(set(mark['ids'])),mark
        if mark['check']:check_pairs(mark['check'])
    assert all(not mark['check'] for mark in RULED_PANELS.values())

SCRIPT=r"""
(()=>{
const buttons=[...document.querySelectorAll('[data-language]')];
const tierButtons=[...document.querySelectorAll('[data-tier]')];
const rulingsButton=document.querySelector('.toggle-rulings');
const toolbar=document.querySelector('.toolbar');
const params=new URLSearchParams(location.search);
function remember(key,value){try{sessionStorage.setItem('mso-study-'+key,value)}catch{}}
function recall(key){let v=params.get(key);try{v=v||sessionStorage.getItem('mso-study-'+key)}catch{}return v}
// Study tier filter: show every block, hide Recognise/Reference, or show Remember only.
function tier(t){
 if(!['all','MU','M'].includes(t))t='all';
 document.body.dataset.tier=t;
 tierButtons.forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.tier===t)));
 remember('tier',t);
}
// Ruling marks are a verification aid; they stay hidden until asked for.
function rulings(on){
 document.body.dataset.rulings=on?'on':'off';
 if(rulingsButton)rulingsButton.setAttribute('aria-pressed',String(on));
 remember('rulings',on?'on':'off');
}
function anchorOffset(){
 document.documentElement.style.setProperty('--anchor-offset',(Math.ceil(toolbar.getBoundingClientRect().height)+16)+'px');
}
function revealHash(){
 const target=document.getElementById(decodeURIComponent(location.hash.slice(1)));
 if(target)target.scrollIntoView({block:'start'});
}
function language(lang){
 if(!['tc','en','both'].includes(lang))lang='tc';
 const destination=document.getElementById(decodeURIComponent(location.hash.slice(1)));
 const offset=parseFloat(getComputedStyle(document.documentElement).scrollPaddingTop)||0;
 const atDestination=destination&&Math.abs(destination.getBoundingClientRect().top-offset-(parseFloat(getComputedStyle(destination).scrollMarginTop)||0))<32;
 document.body.dataset.lang=lang;document.documentElement.lang=lang==='en'?'en':'zh-Hant';
 buttons.forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.language===lang)));
 try{sessionStorage.setItem('mso-study-language',lang)}catch{}
 document.querySelectorAll('.part-nav a,.practice-link,footer a,.visual-links a,.ruling-elsewhere a').forEach(a=>{
  const u=new URL(a.href);u.searchParams.set('lang',lang);a.href=u.href;
 });
 anchorOffset();
 // Preserve a just-followed reference without jumping back to an old hash after scrolling.
 if(atDestination)requestAnimationFrame(()=>{anchorOffset();revealHash()});
}
buttons.forEach(b=>b.addEventListener('click',()=>language(b.dataset.language)));
tierButtons.forEach(b=>b.addEventListener('click',()=>tier(b.dataset.tier)));
if(rulingsButton)rulingsButton.addEventListener('click',()=>rulings(document.body.dataset.rulings!=='on'));
// Following a ruling link needs the marks on screen.
document.addEventListener('click',e=>{const a=e.target.closest('a[href^="#ruling"]');if(a&&document.body.dataset.rulings!=='on')rulings(true)});
let saved=params.get('lang');
try{saved=saved||sessionStorage.getItem('mso-study-language')}catch{}
language(saved||'tc');
tier(recall('tier')||'all');
rulings(recall('rulings')==='on'||/^#ruling/.test(location.hash));
if('ResizeObserver' in window)new ResizeObserver(anchorOffset).observe(toolbar);
window.addEventListener('resize',anchorOffset);
// Resolve the initial hash only after fonts and the chosen language determine height.
document.fonts.ready.then(()=>{anchorOffset();if(location.hash)revealHash()});
window.addEventListener('hashchange',()=>{anchorOffset();revealHash()});
const nav=[...document.querySelectorAll('[data-section]')];
function current(id){nav.forEach(a=>a.setAttribute('aria-current',a.dataset.section===id?'location':'false'))}
nav.forEach(a=>a.addEventListener('click',()=>current(a.dataset.section)));
if('IntersectionObserver' in window){
 const observer=new IntersectionObserver(entries=>{
  for(const entry of entries)if(entry.isIntersecting)current(entry.target.id);
 },{rootMargin:'-145px 0px -65% 0px',threshold:0});
 document.querySelectorAll('.chapter').forEach(s=>observer.observe(s));
}
current(location.hash.slice(1)||nav[0]?.dataset.section);
})();
"""
def part_nav(n):return '<nav class="part-nav" aria-label="章節導覽 / Parts">'+''.join(f'<a href="part-{i}.html"'+(' aria-current="page"' if n==i else '')+'>'+label(f'第{i}部分',f'Part {i}')+'</a>' for i in PARTS)+'</nav>'
def tier_title(b,letter):
    title=dict(b['title'])
    for lang in ('tc','en'):
        for prefix in TIER_PREFIXES[letter][lang]:
            if title[lang].startswith(prefix):title[lang]=title[lang][len(prefix):]
    return '<span class="tier-chip tier-'+letter+'">'+pair(TIER_LABELS[letter])+'</span>'+pair(title)

def render_traps(traps,sid):
    if not traps:return ''
    items=''.join('<li><span class="trap-ids">'+' '.join(f'<a href="#ruling-{i}">{i}</a>' for i in trap['ids'])+'</span>'+pair(trap['text'])+'</li>' for trap in traps)
    return f'<aside class="exam-traps" id="traps-{sid}"><h3>'+label('易錯提示','Exam traps')+'</h3><ul>'+items+'</ul><p class="trap-source">'+label('編號對應repo內《CONFLICT-CALLS》的擁有人裁決；按編號可看本部分末的裁決詳情。','Numbers refer to the owner decisions in the repository’s CONFLICT-CALLS file; select one for the ruling at the end of this part.')+'</p></aside>'

# Ruling marks: a number beside each point or figure that applies a recorded ruling.
RULING_KINDS={
    'between':label('兩份文件之間','Between two documents'),
    'within':label('同一文件內','Within one document'),
    'one':label('中英文本・兩語同一答案','English and Chinese texts · one answer in both'),
    'lang':label('中英文本・各按本身語文','English and Chinese texts · each language keeps its own'),
    'checked':label('核對後不屬矛盾','Checked: not a conflict'),
    'owner':label('擁有人2026年10月20日決定','Owner decision, 20 October 2026'),
    'unlisted':label('未列入CONFLICT-CALLS','Not in CONFLICT-CALLS'),
}
def ruling_kind(rid):
    if rid.startswith('U'):return 'unlisted'
    if rid=='D26':return 'owner'
    if rid[0]=='E':return 'one' if 'One answer in both language views' in CALLS[rid]['decision'] else 'lang'
    return {'B':'between','W':'within','N':'checked'}[rid[0]]
def ruling_order(rid):return ('BWENDU'.index(rid[0]),int(re.sub(r'\D','',rid)))
def ruling_decision(rid):
    # A single-number exam trap already restates the decision in both languages.
    single=[trap['text'] for sections in TRAPS.values() for traps in sections.values() for trap in traps if trap['ids']==[rid]]
    return RULING_DECISIONS.get(rid) or (single[0] if single else None)
def ruling_chips(ids):
    out={}
    for lang,word,colon in (('tc','裁決','：'),('en','Ruling',': ')):
        out[lang]=''.join(f'<a class="ruling-chip kind-{ruling_kind(i)}" href="#ruling-{i}" title="{e(word+" "+i+colon+RULING_ISSUES[i][lang])}"><span aria-hidden="true">⚖</span>{i}</a>' for i in ids)
    return out
def ruling_strip(mark):
    chips=ruling_chips(mark['ids'])
    return '<p class="ruling-strip">'+''.join(f'<span class="{lang}" lang="{"zh-Hant" if lang=="tc" else "en"}">'+('本圖表套用的裁決' if lang=='tc' else 'Rulings applied in this figure')+chips[lang]+'</span>' for lang in ('tc','en'))+'</p>'

def render_point(p,mark,anchor):
    if not mark:return '<li>'+emphasized_pair(p)+'</li>'
    check=('<p class="ruling-check" role="note">'+pair(dict(tc='核對：'+mark['check']['tc'],en='Check: '+mark['check']['en']))+'</p>') if mark['check'] else ''
    return f'<li class="ruled" id="{anchor}">'+emphasized_pair(p,ruling_chips(mark['ids']))+check+'</li>'

def render_block(b,letter,n=None,sid=None,bi=None):
    title='<h3>'+tier_title(b,letter)+'</h3>'
    marks=[RULED_POINTS.get((n,sid,bi,pi)) for pi in range(len(b['points']))]
    assert b['kind']!='flow' or not any(marks),(n,sid,bi)
    if b['kind']=='flow':
        points='<div class="flow-stack">'+'<div class="arrow" aria-hidden="true"></div>'.join('<div class="flow-node">'+pair(p)+'</div>' for p in b['points'])+'</div>'
    else:points='<ul class="concept-list">'+''.join(render_point(p,mark,f'rule-{sid}-{bi}-{pi}') for pi,(p,mark) in enumerate(zip(b['points'],marks)))+'</ul>'
    return '<div class="concept-block tier-block-'+letter+(' '+b['kind'] if b['kind'] in ('flow','reference') else '')+'">'+title+points+citations(b['refs'])+'</div>'

def plain_title(title):
    out=dict(title)
    for prefixes in TIER_PREFIXES.values():
        for lang in ('tc','en'):
            for prefix in prefixes[lang]:
                if out[lang].startswith(prefix):out[lang]=out[lang][len(prefix):]
    return out
def ruling_places(n):
    """Every place in Part n that applies a ruling, in reading order."""
    places={}
    for i,s in enumerate(PARTS[n]['sections'],1):
        number=f'<span class="place-number">{i:02d}</span>'
        for panel in PANELS[n].get(s['id'],[]):
            for rid in (RULED_PANELS.get(panel['id']) or {'ids':[]})['ids']:
                places.setdefault(rid,[]).append(f'<a href="#memory-{panel["id"]}">'+number+label('圖表：'+panel['title']['tc'],'Figure: '+panel['title']['en'])+'</a>')
        for bi,b in enumerate(s['blocks']):
            for pi in range(len(b['points'])):
                for rid in (RULED_POINTS.get((n,s['id'],bi,pi)) or {'ids':[]})['ids']:
                    title=plain_title(b['title'])
                    places.setdefault(rid,[]).append(f'<a href="#rule-{s["id"]}-{bi}-{pi}">'+number+label(f'{title["tc"]} · 第{pi+1}點',f'{title["en"]} · point {pi+1}')+'</a>')
        for trap in TRAPS.get(n,{}).get(s['id'],[]):
            for rid in trap['ids']:
                places.setdefault(rid,[]).append(f'<a href="#traps-{s["id"]}">'+number+label('易錯提示：'+s['title']['tc'],'Exam traps: '+s['title']['en'])+'</a>')
    return places
RULING_PARTS={}
for _n in PARTS:
    for _rid in ruling_places(_n):RULING_PARTS.setdefault(_rid,[]).append(_n)

def record_text(text):
    """Quote a CONFLICT-CALLS cell as recorded; link the cited 01–26 originals."""
    def link(match):
        doc,chinese=match.group(1),bool(match.group(2))
        if not '01'<=doc<='26':return match.group(0)
        ed=DOCS[doc]['editions']['TC' if chinese and doc!='24' else 'EN']
        return f'(<a href="../../docs/{e(quote(ed["path"],safe="/"))}" target="_blank" rel="noopener">{doc}</a>)'+(match.group(2) or '')
    out=re.sub(r'\((\d{2})\)( \(Chinese\))?',link,e(text.strip().lstrip('•').strip(),quote=False))
    return re.sub(r'\*([^*]+)\*',r'<em>\1</em>',out)

def render_record(rid):
    field=lambda tc,en,body:'<dt>'+label(tc,en)+'</dt><dd lang="en">'+body+'</dd>'
    if rid in RULING_RECORDS:
        r=RULING_RECORDS[rid];origin=pair(r['record'])
        sources=''.join('<li>'+(f'<a href="../../docs/{e(quote(DOCS[doc]["editions"][lang]["path"],safe="/"))}" target="_blank" rel="noopener">{doc}</a> · ')+e(text)+'</li>' for doc,lang,text in r['sources'])
        body=field('來源','Sources','<ul>'+sources+'</ul>')+(field('裁決','Decision',e(r['decision'])) if r['decision'] else '')
    else:
        row=CALLS[rid];origin=label(f'revision/CONFLICT-CALLS.md，{rid}',f'revision/CONFLICT-CALLS.md, {rid}')
        body=field('問題','Question',record_text(row['question']))+field('來源','Sources','<ul>'+''.join('<li>'+record_text(s)+'</li>' for s in row['sources'])+'</ul>')+field('裁決','Decision',record_text(row['decision']))
    return '<details class="ruling-record"><summary>'+label('裁決記錄原文','Recorded entry')+'</summary><p class="record-origin">'+origin+'</p><dl>'+body+'</dl></details>'

def render_ruling(rid,places,n):
    kind=ruling_kind(rid)
    out=[f'<article class="ruling-entry kind-{kind}" id="ruling-{rid}" aria-labelledby="ruling-title-{rid}"><p class="ruling-head"><span class="ruling-id">{rid}</span><span class="ruling-kind">'+RULING_KINDS[kind]+'</span></p>']
    out.append(f'<h3 id="ruling-title-{rid}">'+pair(RULING_ISSUES[rid])+'</h3>')
    out.append('<div class="ruling-decision"><span class="ruling-label">'+label('裁決','Decision')+'</span>'+pair(ruling_decision(rid))+'</div>')
    out.append('<p class="ruling-where"><span class="ruling-label">'+label('本部分位置','Where in this part')+'</span>'+''.join(places)+'</p>')
    others=[m for m in RULING_PARTS[rid] if m!=n]
    if others:out.append('<p class="ruling-elsewhere"><span class="ruling-label">'+label('其他部分','Other parts')+'</span>'+''.join(f'<a href="part-{m}.html#ruling-{rid}">'+label(f'第{m}部分',f'Part {m}')+'</a>' for m in others)+'</p>')
    out.append(render_record(rid)+'</article>')
    return ''.join(out)

def render_register(n):
    places=ruling_places(n)
    checks=any(mark['check'] for (m,*_),mark in RULED_POINTS.items() if m==n)
    intro=label('以下是本部分正文、圖表及易錯提示套用的裁決。紫色編號標在套用裁決的要點旁；按編號可回到這裏，核對裁決、出現位置及裁決記錄原文。B＝兩份文件之間，W＝同一文件內，E＝中英文本之間，N＝核對後不屬矛盾，D26＝擁有人2026年10月20日決定；U＝正文已處理、但未列入CONFLICT-CALLS的兩語差異。虛線編號表示兩語各按本身語文。'+('黃色「核對」提示表示該句可能與所套用的裁決不一致。' if checks else ''),
        'These are the rulings applied in this part’s text, figures and exam traps. A purple number marks each point that applies one; select it to come here and check the decision, where it is used and the recorded entry. B = between two documents, W = within one document, E = English and Chinese texts, N = checked, not a conflict, D26 = the owner decision of 20 October 2026; U = a language difference the text handles that is not in CONFLICT-CALLS. A dashed number means each language keeps its own wording.'+(' An amber “Check” note means the point may not match the ruling it applies.' if checks else ''))
    entries=''.join(render_ruling(rid,places[rid],n) for rid in sorted(places,key=ruling_order))
    return '<section class="chapter rulings-register" id="rulings" aria-labelledby="title-rulings"><div class="section-heading"><span class="section-number" aria-hidden="true">⚖</span><h2 id="title-rulings">'+label('本部分的裁決','Rulings in this part')+'</h2></div><p class="register-intro">'+intro+'</p>'+entries+'</section>'

def render_panel(panel):
    key=panel['id'];title=pair(panel['title'])
    out=[f'<figure class="memory-panel" id="memory-{key}" aria-labelledby="memory-title-{key}"><h3 id="memory-title-{key}">'+title+'</h3>'+(ruling_strip(RULED_PANELS[key]) if key in RULED_PANELS and not panel.get('table_label') else '')]
    if panel['kind']=='table':
        if panel.get('groups'):
            for group_number,group in enumerate(panel['groups'],1):
                group_id=f'memory-title-{key}-group-{group_number}'
                subset=dict(panel,rows=group['rows'],table_label=group_id);subset.pop('groups',None)
                out.append('<h4 class="table-group-title" id="'+group_id+'">'+pair(group['title'])+'</h4>')
                rendered=render_panel(subset)
                out.append(rendered[rendered.index('<table'):rendered.index('</table>')+8])
            if panel.get('note'):out.append('<p class="memory-note">'+pair(panel['note'])+'</p>')
            out.append(compact_citations(panel['refs'])+'</figure>')
            return ''.join(out)
        table_class='memory-table columns-'+str(len(panel['headers']))+(' peer-comparison' if panel.get('peers') else '')
        table_label=panel.get('table_label','memory-title-'+key)
        out.append('<table class="'+table_class+'" role="table" aria-labelledby="'+table_label+'"><thead role="rowgroup"><tr role="row">'+''.join('<th scope="col" role="columnheader">'+pair(h)+'</th>' for h in panel['headers'])+'</tr></thead>')
        for row in panel['rows']:
            out.append('<tbody role="rowgroup"><tr role="row"><th scope="row" role="rowheader">'+pair(row[0])+'</th>')
            for i,cell in enumerate(row[1:],1):
                out.append('<td role="cell"'+(' class="memory-value"' if i==1 else '')+'><span class="cell-label" aria-hidden="true">'+pair(panel['headers'][i])+'</span>'+emphasized_pair(cell)+'</td>')
            out.append('</tr></tbody>')
        out.append('</table>')
    elif panel['kind']=='stages':
        out.append('<ul class="stage-sequence">')
        for i,step in enumerate(panel['steps']):
            out.append('<li><h4>'+pair(step['term'])+'</h4><p>'+pair(step['meaning'])+'</p>')
            if panel.get('examples'):out.append(render_visual(dict(kind='paths',paths=[panel['examples'][i]]),pair))
            out.append('</li>')
        out.append('</ul>')
    elif panel['kind']=='pass-rule':
        out.append('<p class="exam-facts">'+pair(panel['facts'])+'</p><div class="pass-gates">')
        out.append('<p>'+pair(panel['gates'][0])+'</p><span class="gate-join">'+label('而且','AND')+'</span><p>'+pair(panel['gates'][1])+'</p></div>')
    else:out.append(render_visual(panel,pair))
    if panel.get('links'):out.append('<nav class="visual-links">'+''.join('<a href="'+e(v['href'])+'">'+pair(v['label'])+'</a>' for v in panel['links'])+'</nav>')
    if panel.get('note'):out.append('<p class="memory-note">'+emphasized_pair(panel['note'])+'</p>')
    out.append(compact_citations(panel['refs'])+'</figure>')
    return ''.join(out)

def study_key(n):
    letters=''.join(TIERS[n].values());traps=sum(len(v) for v in TRAPS.get(n,{}).values())
    chips=''.join('<span class="tier-chip tier-'+k+'">'+pair(v)+'</span><span class="key-count">'+str(letters.count(k))+'</span>' for k,v in TIER_LABELS.items())
    marks=sum(len(v) for v in RULING_MARKS.get(n,{}).values());rulings=len(ruling_places(n))
    return '<div class="study-key">'+chips+'<span class="key-traps">'+label(f'易錯提示 {traps} 項',f'{traps} exam traps')+'</span><a class="key-rulings" href="#rulings">'+label(f'⚖ 裁決標記 {marks} 處 · {rulings} 項裁決',f'⚖ {marks} ruling marks · {rulings} rulings')+'</a></div>'

def toolbar(n=None):
    """Language, study-tier and ruling-mark controls; the numbers page has no tiers or marks."""
    languages='<div class="languages" role="group" aria-label="閱讀語言 / Reading language"><button data-language="tc" aria-pressed="true">繁體中文</button><button data-language="en" aria-pressed="false">English</button><button data-language="both" aria-pressed="false">雙語 / Both</button></div>'
    tiers=''.join(f'<button type="button" data-tier="{t}" aria-pressed="false">'+label(tc,en)+'</button>' for t,tc,en in (('all','全部','All'),('MU','必記＋理解','Remember + Understand'),('M','只看必記','Remember only')))
    controls=('<div class="tiers" role="group" aria-label="學習層次 / Study tiers">'+tiers+'</div><button type="button" class="toggle-rulings" aria-pressed="false"><span aria-hidden="true">⚖ </span>'+label('裁決標記','Ruling marks')+'</button>') if n else ''
    numbers='<a class="numbers-link" href="amounts.html"'+('' if n else ' aria-current="page"')+'>'+label('數字總表','Numbers')+'</a>'
    practice='<a class="practice-link" href="../../dist/mso-ca.html?part='+str(n or 1)+'">'+label('練習','Practice')+'</a>'
    return '<header class="toolbar"><div class="toolbar-inner"><div class="brand">MSO Competence Assessment Study Note</div>'+languages+controls+numbers+practice+'</div>'+part_nav(n)+'</header>'

def shell(title,n,nav,main):
    font=base64.b64encode((ROOT/'web/fonts/dmsans.woff2').read_bytes()).decode('ascii')
    css='@font-face{font-family:"Study Sans";src:url(data:font/woff2;base64,'+font+') format("woff2");font-weight:100 900;font-style:normal;font-display:swap;}'+(HERE/'style.css').read_text(encoding='utf-8')
    return '<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+title+'</title><style>'+css+'</style></head><body data-lang="tc"><a class="skip-link" href="#content">'+label('跳至正文','Skip to content')+'</a>'+toolbar(n)+'<div class="layout"><aside class="sidebar"><h2>'+label('本章目錄','In this part')+'</h2><nav>'+nav+'</nav></aside><main id="content" tabindex="-1">'+main+'</main></div><script>'+SCRIPT+'</script></body></html>\n'

def page(n):
    part=PARTS[n];nav=[];body=[]
    for i,s in enumerate(part['sections'],1):
        nav.append(f'<a href="#{s["id"]}" data-section="{s["id"]}"><span class="nav-number">{i:02d}</span><span>'+pair(s['title'])+'</span></a>')
        body.append(f'<section class="chapter" id="{s["id"]}" aria-labelledby="title-{s["id"]}"><div class="section-heading"><span class="section-number">{i:02d}</span><h2 id="title-{s["id"]}">'+pair(s['title'])+'</h2></div>'+''.join(render_panel(panel) for panel in PANELS[n].get(s['id'],[]))+''.join(render_block(b,letter,n,s['id'],bi) for bi,(b,letter) in enumerate(zip(s['blocks'],TIERS[n][s['id']])))+render_traps(TRAPS.get(n,{}).get(s['id'],[]),s['id'])+'</section>')
    nav.append('<a href="#rulings" data-section="rulings"><span class="nav-number" aria-hidden="true">⚖</span><span>'+label('本部分的裁決','Rulings in this part')+'</span></a>')
    body.append(render_register(n))
    main='<header class="hero"><h1>'+label('第'+str(n)+'部分 · '+part['title']['tc'],'Part '+str(n)+' · '+part['title']['en'])+'</h1></header><p class="part-intro">'+pair(part['intro'])+'</p>'+study_key(n)+''.join(body)+'<footer><a href="../../dist/mso-ca.html?part='+str(n)+'">'+label('前往本部分練習','Practise this part')+'</a></footer>'
    return shell('MSO · Part '+str(n)+' · Study Notes',n,''.join(nav),main)

AMOUNT_HEADERS=[dict(tc='數值',en='Value'),dict(tc='適用情形',en='Applies to'),dict(tc='起算點／條件',en='Starting point / condition'),dict(tc='筆記與出處',en='Notes and source')]
def amounts_page():
    """Every amount, share, period, fee and penalty on one page, each linked to its notes section."""
    nav=[];body=[]
    for i,g in enumerate(AMOUNT_GROUPS,1):
        nav.append(f'<a href="#{g["id"]}" data-section="{g["id"]}"><span class="nav-number">{i:02d}</span><span>'+pair(g['title'])+'</span></a>')
        rows=[]
        for row in g['rows']:
            section=next(s for s in PARTS[row['part']]['sections'] if s['id']==row['section'])
            where=f'<a class="amount-where" href="part-{row["part"]}.html#{row["section"]}">'+label(f'第{row["part"]}部分 · '+section['title']['tc'],f'Part {row["part"]} · '+section['title']['en'])+'</a>'
            cells=[('memory-value',emphasized_pair(row['what'])),('',emphasized_pair(row['basis'])),('',where+compact_citations(row['refs']))]
            rows.append('<tbody role="rowgroup"><tr role="row"><th scope="row" role="rowheader">'+pair(row['value'])+'</th>'+''.join('<td role="cell"'+(f' class="{cls}"' if cls else '')+'><span class="cell-label" aria-hidden="true">'+pair(AMOUNT_HEADERS[k+1])+'</span>'+html_ for k,(cls,html_) in enumerate(cells))+'</tr></tbody>')
        table='<figure class="memory-panel amounts"><table class="memory-table columns-4" role="table" aria-labelledby="title-'+g['id']+'"><thead role="rowgroup"><tr role="row">'+''.join('<th scope="col" role="columnheader">'+pair(h)+'</th>' for h in AMOUNT_HEADERS)+'</tr></thead>'+''.join(rows)+'</table></figure>'
        body.append(f'<section class="chapter" id="{g["id"]}" aria-labelledby="title-{g["id"]}"><div class="section-heading"><span class="section-number">{i:02d}</span><h2 id="title-{g["id"]}">'+pair(g['title'])+'</h2></div><p class="intro">'+pair(g['intro'])+'</p>'+table+'</section>')
    main='<header class="hero"><h1>'+label('數字與期限總表','Numbers and deadlines')+'</h1></header><p class="part-intro">'+label('七個部分的金額、百分比、日數、年期、費用及刑罰集中在一頁：每行寫明適用情形、起算點或條件，並連到筆記小節及原文。相近的數字放在一起，方便比較。','Every amount, percentage, number of days, period, fee and penalty from the seven parts on one page: each row says when it applies, where its clock starts or what it requires, and links to the notes section and the source. Similar figures sit together for comparison.')+'</p>'+''.join(body)+'<footer><a href="index.html">'+label('返回筆記','Back to the notes')+'</a></footer>'
    return shell('MSO · Numbers · Study Notes',None,''.join(nav),main)

class Inspector(HTMLParser):
    def __init__(self):super().__init__();self.ids=[];self.links=[]
    def handle_starttag(self,tag,attrs):
        attrs=dict(attrs)
        if 'id' in attrs:self.ids.append(attrs['id'])
        if tag=='a':self.links.append(attrs.get('href',''))

def manifest():
    parts=[];documents={f'{n:02d}':[] for n in range(1,27)}
    for n,p in PARTS.items():
        entries=[]
        for s in p['sections']:
            panels=PANELS[n].get(s['id'],[])
            refs=[r for b in s['blocks'] for r in b['refs']]+[r for panel in panels for r in panel['refs']]
            for doc in sorted({r['doc'] for r in refs}):documents[doc].append(f'part-{n}.html#{s["id"]}')
            entries.append(dict(id=s['id'],title=s['title'],points=sum(len(b['points']) for b in s['blocks']),memory_panels=[dict(id=panel['id'],kind=panel['kind'],rows=len(panel.get('rows',[]))) for panel in panels],refs=refs))
        parts.append(dict(part=n,title=p['title'],sections=entries,points=sum(e['points'] for e in entries)))
    recall=dict(sha256=hashlib.sha256((HERE/'memory_panels.py').read_bytes()).hexdigest(),tables=sum(panel['kind']=='table' for sections in PANELS.values() for panels in sections.values() for panel in panels),diagrams=sum(panel['kind']!='table' for sections in PANELS.values() for panels in sections.values() for panel in panels))
    recall['visual_sources']={name:hashlib.sha256((HERE/name).read_bytes()).hexdigest() for name in ('visual_panels.py','visual_render.py')}
    exam_focus=dict(traps=sum(len(v) for sections in TRAPS.values() for v in sections.values()),tiers={k:''.join(t for sections in TIERS.values() for t in sections.values()).count(k) for k in TIER_LABELS},sources={name:hashlib.sha256((HERE/name).read_bytes()).hexdigest() for name in ('traps.py','tiers.py')})
    exam_focus['ruling_marks']=dict(marks={str(n):sum(len(v) for v in RULING_MARKS.get(n,{}).values()) for n in PARTS},checks=sum(bool(mark['check']) for mark in [*RULED_POINTS.values(),*RULED_PANELS.values()]),rulings=sorted(RULING_PARTS,key=ruling_order),sha256=hashlib.sha256((HERE/'rulings.py').read_bytes()).hexdigest())
    essentials=dict(sha256=hashlib.sha256((HERE/'essentials.py').read_bytes()).hexdigest(),blocks=sum(len(blocks) for topics in ADDITIONS.values() for blocks in topics.values()),points=sum(len(block['points']) for topics in ADDITIONS.values() for blocks in topics.values() for block in blocks))
    amounts=dict(sha256=hashlib.sha256((HERE/'amounts.py').read_bytes()).hexdigest(),groups=len(AMOUNT_GROUPS),rows=sum(len(g['rows']) for g in AMOUNT_GROUPS))
    return dict(scope='Repository originals 01–26; source-authored seven-part revision notes',method='Original passages -> concepts, definitions, requirements, conditions and exceptions. Source-bound recall comparisons supplement full visible prose. The bank is used only by the separate gap audit.',limitations='Anchors prove source location, not semantic completeness. See depth-review-2026-10-20/REPORT.md and its per-source inventories for the current depth review, bilingual meaning checks, source-selected statutory coverage, reference-detail decisions and unresolved verification boundaries. This is not a line-by-line bilingual audit of every full volume or a guarantee about unknown official questions. Official source categories extend beyond the owner-selected 01–26. Historical reviews remain preserved, not proof of this review. Dated findings/lists retain their publication date.',manuscripts={f'part{n}.py':hashlib.sha256((HERE/f'part{n}.py').read_bytes()).hexdigest() for n in PARTS},essentials=essentials,recall=recall,exam_focus=exam_focus,amounts=amounts,source_text_sha256={doc:{lang:hashlib.sha256((ROOT/f'docs/text/{lang}/{doc}.txt').read_bytes()).hexdigest() for lang in (('EN',) if doc=='24' else ('TC','EN'))} for doc in documents},documents=documents,parts=parts)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--check',action='store_true');args=ap.parse_args();validate()
    outputs={HERE/f'part-{n}.html':page(n) for n in PARTS};outputs[HERE/'index.html']=outputs[HERE/'part-1.html'];outputs[HERE/'amounts.html']=amounts_page()
    data=manifest();outputs[HERE/'coverage.json']=json.dumps(data,ensure_ascii=False,indent=2)+'\n'
    for path,text in outputs.items():
        if path.suffix=='.html':
            parser=Inspector();parser.feed(text);assert len(parser.ids)==len(set(parser.ids)),path
            for link in parser.links:
                if link.startswith('#'):assert link[1:] in parser.ids,(path,link)
                else:
                    target=(path.parent/unquote(urlsplit(link).path)).resolve()
                    assert target in outputs or target.is_file(),(path,link)
        if args.check:assert path.read_text(encoding='utf-8')==text,f'Stale: {path}'
        else:path.write_text(text,encoding='utf-8',newline='\n')
    print(json.dumps(dict(status='checked' if args.check else 'built',parts=7,sections=sum(len(p['sections']) for p in data['parts']),points=sum(p['points'] for p in data['parts']),sources=len(data['documents']))))

if __name__=='__main__':main()
