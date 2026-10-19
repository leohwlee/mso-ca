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
for number, additions in ADDITIONS.items():
    for topic, blocks in additions.items():
        next(section for section in PARTS[number]['sections'] if section['id']==topic)['blocks'].extend(blocks)
PANELS=apply_visuals(PANELS,PARTS)
CATALOG=json.loads((ROOT/'docs/catalog.json').read_text(encoding='utf-8'))
DOCS={d['id']:d for d in CATALOG['documents']}
e=html.escape
def normal(text):return re.sub(r'\s+',' ',text).casefold()
def pair(value):
    if value['tc']==value['en']:return '<span class="shared">'+e(value['tc'])+'</span>'
    return ''.join(f'<span class="{lang}" lang="{"zh-Hant" if lang=="tc" else "en"}">{e(value[lang])}</span>' for lang in ('tc','en'))
def label(tc,en):return pair(dict(tc=tc,en=en))

def emphasized_pair(value):
    """Add a few exact lexical anchors without rewriting any source-authored text."""
    out=[]
    for lang in ('tc','en'):
        terms=sorted(EMPHASIS[lang],key=len,reverse=True)
        pattern='|'.join(re.escape(t) for t in terms)
        if lang=='en':pattern=r'(?<![A-Za-z])(?:'+pattern+r')(?![A-Za-z])'
        chunks=[];end=0
        for i,m in enumerate(re.finditer(pattern,value[lang],re.I)):
            if i==3:break
            chunks.extend((e(value[lang][end:m.start()]),'<strong class="recall-term">'+e(m.group())+'</strong>'));end=m.end()
        chunks.append(e(value[lang][end:]))
        out.append(f'<span class="{lang}" lang="{"zh-Hant" if lang=="tc" else "en"}">'+''.join(chunks)+'</span>')
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
                for row in panel.get('paths',[]):
                    assert len(row['nodes'])==len(row['edges'])+1,panel['id']
                for r in panel['refs']:
                    assert '01'<=r['doc']<='26'
                    assert normal(r['anchor']) in normal((ROOT/f'docs/text/EN/{r["doc"]}.txt').read_text(encoding='utf-8'))
    assert len(panel_ids)==len(set(panel_ids)),panel_ids

SCRIPT=r"""
(()=>{
const buttons=[...document.querySelectorAll('[data-language]')];
function language(lang){
 if(!['tc','en','both'].includes(lang))lang='tc';
 document.body.dataset.lang=lang;document.documentElement.lang=lang==='en'?'en':'zh-Hant';
 buttons.forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.language===lang)));
 try{sessionStorage.setItem('mso-study-language',lang)}catch{}
 document.querySelectorAll('.part-nav a,.practice-link,footer a,.visual-links a').forEach(a=>{
  const u=new URL(a.href);u.searchParams.set('lang',lang);a.href=u.href;
 });
}
buttons.forEach(b=>b.addEventListener('click',()=>language(b.dataset.language)));
let saved=new URLSearchParams(location.search).get('lang');
try{saved=saved||sessionStorage.getItem('mso-study-language')}catch{}
language(saved||'tc');
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
def part_nav(n):return '<nav class="part-nav" aria-label="Parts">'+''.join(f'<a href="part-{i}.html"'+(' aria-current="page"' if n==i else '')+f'>Part {i}</a>' for i in PARTS)+'</nav>'
def render_block(b):
    title='<h3>'+pair(b['title'])+'</h3>'
    if b['kind']=='flow':
        points='<div class="flow-stack">'+'<div class="arrow" aria-hidden="true"></div>'.join('<div class="flow-node">'+pair(p)+'</div>' for p in b['points'])+'</div>'
    else:points='<ul class="concept-list">'+''.join('<li>'+emphasized_pair(p)+'</li>' for p in b['points'])+'</ul>'
    return '<div class="concept-block'+(' '+b['kind'] if b['kind'] in ('flow','reference') else '')+'">'+title+points+citations(b['refs'])+'</div>'

def render_panel(panel):
    key=panel['id'];title=pair(panel['title'])
    out=[f'<figure class="memory-panel" id="memory-{key}" aria-labelledby="memory-title-{key}"><h3 id="memory-title-{key}">'+title+'</h3>']
    if panel['kind']=='table':
        if panel.get('groups'):
            for group in panel['groups']:
                subset=dict(panel,rows=group['rows']);subset.pop('groups',None)
                out.append('<h4 class="table-group-title">'+pair(group['title'])+'</h4>')
                rendered=render_panel(subset)
                out.append(rendered[rendered.index('<table'):rendered.index('</table>')+8])
            if panel.get('note'):out.append('<p class="memory-note">'+pair(panel['note'])+'</p>')
            out.append(compact_citations(panel['refs'])+'</figure>')
            return ''.join(out)
        out.append('<table class="memory-table columns-'+str(len(panel['headers']))+'" role="table"><thead role="rowgroup"><tr role="row">'+''.join('<th scope="col" role="columnheader">'+pair(h)+'</th>' for h in panel['headers'])+'</tr></thead>')
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

def page(n):
    part=PARTS[n];nav=[];body=[]
    for i,s in enumerate(part['sections'],1):
        nav.append(f'<a href="#{s["id"]}" data-section="{s["id"]}"><span class="nav-number">{i:02d}</span><span>'+pair(s['title'])+'</span></a>')
        body.append(f'<section class="chapter" id="{s["id"]}" aria-labelledby="title-{s["id"]}"><div class="section-heading"><span class="section-number">{i:02d}</span><h2 id="title-{s["id"]}">'+pair(s['title'])+'</h2></div>'+''.join(render_panel(panel) for panel in PANELS[n].get(s['id'],[]))+''.join(render_block(b) for b in s['blocks'])+'</section>')
    font=base64.b64encode((ROOT/'web/fonts/dmsans.woff2').read_bytes()).decode('ascii')
    css='@font-face{font-family:"Study Sans";src:url(data:font/woff2;base64,'+font+') format("woff2");font-weight:100 900;font-style:normal;font-display:swap;}'+(HERE/'style.css').read_text(encoding='utf-8')
    return '<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>MSO · Part '+str(n)+' · Study Notes</title><style>'+css+'</style></head><body data-lang="tc"><a class="skip-link" href="#content">'+label('跳至正文','Skip to content')+'</a><header class="toolbar"><div class="toolbar-inner"><div class="brand">MSO Competence Assessment Study Note</div><div class="languages" role="group" aria-label="閱讀語言 / Reading language"><button data-language="tc" aria-pressed="true">繁體中文</button><button data-language="en" aria-pressed="false">English</button><button data-language="both" aria-pressed="false">雙語 / Both</button></div><a class="practice-link" href="../../dist/mso-ca.html?part='+str(n)+'">'+label('練習','Practice')+'</a></div>'+part_nav(n)+'</header><div class="layout"><aside class="sidebar"><h2>'+label('本章目錄','In this part')+'</h2><nav>'+''.join(nav)+'</nav></aside><main id="content" tabindex="-1"><header class="hero"><h1>'+label('第'+str(n)+'部分 · '+part['title']['tc'],'Part '+str(n)+' · '+part['title']['en'])+'</h1></header><p class="part-intro">'+pair(part['intro'])+'</p>'+''.join(body)+'<footer><a href="../../dist/mso-ca.html?part='+str(n)+'">'+label('前往本部分練習','Practise this part')+'</a></footer></main></div><script>'+SCRIPT+'</script></body></html>\n'

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
    essentials=dict(sha256=hashlib.sha256((HERE/'essentials.py').read_bytes()).hexdigest(),blocks=sum(len(blocks) for topics in ADDITIONS.values() for blocks in topics.values()),points=sum(len(block['points']) for topics in ADDITIONS.values() for blocks in topics.values() for block in blocks))
    return dict(scope='Repository originals 01–26; source-authored seven-part revision notes',method='Original passages -> concepts, definitions, requirements, conditions and exceptions. Source-bound recall comparisons supplement full visible prose. The bank is used only by the separate gap audit.',limitations='Anchors prove source location, not semantic completeness. Documents 04 and 25 were read throughout in English and reassessed for learning scope. Chinese checks cover core and added material, not a line-by-line full-volume translation audit. Other-sector regimes and cross-sector mechanisms are included selectively; detailed administrative procedures and statistics remain source references. See approval-closeout-2026-10-19/REPORT.md for the latest omitted-content decisions and boundaries; earlier reports remain historical evidence. Dated findings/lists retain their publication date.',manuscripts={f'part{n}.py':hashlib.sha256((HERE/f'part{n}.py').read_bytes()).hexdigest() for n in PARTS},essentials=essentials,recall=recall,source_text_sha256={doc:{lang:hashlib.sha256((ROOT/f'docs/text/{lang}/{doc}.txt').read_bytes()).hexdigest() for lang in (('EN',) if doc=='24' else ('TC','EN'))} for doc in documents},documents=documents,parts=parts)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--check',action='store_true');args=ap.parse_args();validate()
    outputs={HERE/f'part-{n}.html':page(n) for n in PARTS};outputs[HERE/'index.html']=outputs[HERE/'part-1.html']
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
