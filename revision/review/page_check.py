# Build one page module on its own, run the language and link checks, and render
# its figures and the page to PNG so an author can look at what they made.
#   python review/page_check.py MODULE BODYVAR NAVVAR [pagekey]
# e.g. python review/page_check.py g6 G6_BODY G6_NAV g6
import importlib
import io
import os
import re
import subprocess
import sys

SP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, SP)
os.chdir(SP)
mod, bodyvar, navvar = sys.argv[1:4]
key = sys.argv[4] if len(sys.argv) > 4 else mod
# PC_TAG names the output files, so two authors checking the same page do not overwrite each other
tag = os.environ.get('PC_TAG', key)
OUT = os.path.join(SP, 'review', 'preview')
os.makedirs(OUT, exist_ok=True)

m = importlib.import_module(mod)
body, nav = getattr(m, bodyvar), getattr(m, navvar)
ids = [i for i, _, _ in nav]
for i in sorted(ids, key=len, reverse=True):
    body = body.replace(f'id="{i}"', f'id="{key}-{i}"').replace(f'href="#{i}"', f'href="#{key}-{i}"')

problems = []
secs = re.findall(r'<section class="sec" id="([^"]+)"', body)
if len(secs) != len(ids):
    problems.append(f'{len(secs)} sections but {len(ids)} nav entries')
for s in secs:
    if s.replace(key + '-', '') not in ids:
        problems.append(f'section {s} missing from NAV')
allids = re.findall(r'id="([^"]+)"', body)
d = sorted({x for x in allids if allids.count(x) > 1})
if d:
    problems.append(f'duplicate ids {d}')
# links must resolve inside this page or to an id that exists in the current pack
pack = io.open(os.path.join(SP, 'mso-revision-pack.html'), encoding='utf-8').read()
packids = set(re.findall(r'id="([^"]+)"', pack))
for h in set(re.findall(r'href="#([^"]+)"', body)):
    if h not in allids and h not in packids:
        problems.append(f'dead link #{h}')
LAT = re.compile(r'[A-Za-z]{3,}')
ROMAN = re.compile(r'^(i|ii|iii|iv|v|vi|vii|viii|ix|x)$', re.I)
for t in re.findall(r'<span class="l-tc[^"]*" lang="zh-Hant">(.*?)</span>', body):
    words = [w for w in LAT.findall(re.sub(r'<[^>]+>', '', t)) if not ROMAN.match(w)]
    if words:
        problems.append(f'English in Chinese view: {words} in "{re.sub("<[^>]+>", "", t)[:80]}"')
for t in re.findall(r'<span class="c-tc"[^>]*>([^<]*)</span>', body):
    words = [w for w in LAT.findall(t) if not ROMAN.match(w)]
    if words:
        problems.append(f'English in Chinese citation: "{t}"')
CJK = re.compile(r'[\u2E80-\u9FFF\uF900-\uFAFF\uFF00-\uFFEF\u3000-\u303F]')
for t in re.findall(r'<span class="l-en">(.*?)</span>', body):
    if CJK.search(re.sub(r'<[^>]+>', '', t)):
        problems.append(f'Chinese in English view: "{re.sub("<[^>]+>", "", t)[:80]}"')
for t in re.findall(r'<span class="c-en">([^<]*)</span>', body):
    if CJK.search(t):
        problems.append(f'Chinese in English citation: "{t}"')
# every figure must come in three language drawings with no leaked variants
svgs = re.findall(r'<svg class="(fig[^"]*)"(.*?)</svg>', body, re.S)
if len(svgs) % 3:
    problems.append('a figure is not drawn three times: pass the figure FUNCTION to fig(), not its result')
for cls, sv in svgs:
    v = cls.split()[-1][2:] if ' ' in cls else None
    if not v:
        problems.append('figure drawn without language views (call fig(fn, ...) with the function)')
        continue
    for o in ('en', 'tc', 'both'):
        if o != v and re.search(r'class="(?:[^"]* )?s-%s(?: [^"]*)?"' % o, sv):
            problems.append(f'{v} drawing contains {o} text')
            break
    txt = ' '.join(re.findall(r'>([^<>]+)</tspan>', sv))
    if v == 'en' and CJK.search(txt):
        problems.append('Chinese text inside the English drawing of a figure')
    if v == 'tc':
        w = [x for x in LAT.findall(txt) if not ROMAN.match(x)]
        if w:
            problems.append(f'English inside the Chinese drawing of a figure: {sorted(set(w))[:8]}')
bullets = len(re.findall(r'<li>', body))
if bullets:
    problems.append(f'{bullets} bullet list items: use tables or figures instead')

css = io.open(os.path.join(SP, 'pack_css.css'), encoding='utf-8').read().replace('%DARK%', '')
fonts = ('<link href="https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=DM+Sans:opsz,wght@9..40,400..700'
         '&display=swap" rel="stylesheet">')
for lang in ('en', 'tc', 'both'):
    page = (f'<!doctype html><html data-lang="{lang}" data-doc="doc-{key}" data-outline="closed"><head><meta charset="utf-8">{fonts}'
            f'<style>{css}</style></head><body><section class="doc" id="doc-{key}"><main class="wrap">{body}</main></section></body></html>')
    io.open(os.path.join(OUT, f'{tag}_{lang}.html'), 'w', encoding='utf-8').write(page)

chrome = os.environ.get('CHROME', r"C:\Program Files\Google\Chrome\Application\chrome.exe")
prof = os.path.join(SP, 'chrome-prof-' + tag)


def shot(url, png, w, h):
    subprocess.run([chrome, '--headless=new', '--disable-gpu', '--hide-scrollbars', f'--user-data-dir={prof}',
                    f'--window-size={w},{h}', '--virtual-time-budget=3000', f'--screenshot={png}', url],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=120)


# figures: one PNG per drawing, at the width a desktop reader sees (870px)
figs = re.findall(r'(<figure>.*?</figure>)', body, re.S)
made = []
for k, f in enumerate(figs):
    for lang in ('en', 'tc', 'both'):
        vb = re.search(rf'<svg class="fig s-{lang}" viewBox="0 0 ([\d.]+) ([\d.]+)"', f)
        if not vb:
            continue
        h = int(float(vb.group(2)) * 870 / float(vb.group(1))) + 220
        page = (f'<!doctype html><html data-lang="{lang}"><head><meta charset="utf-8">{fonts}<style>{css}</style>'
                f'<style>body{{margin:0;padding:10px;width:892px}} .figwrap{{overflow:visible}} svg.fig{{min-width:0!important}}</style>'
                f'</head><body>{f}</body></html>')
        hp = os.path.join(OUT, f'{tag}_fig{k}_{lang}.html')
        io.open(hp, 'w', encoding='utf-8').write(page)
        png = hp[:-5] + '.png'
        shot('file:///' + hp.replace('\\', '/'), png, 912, h)
        made.append(png)

print('PROBLEMS:' if problems else 'No problems found by the checks.')
for p in problems:
    print('  -', p)
print(f'{len(secs)} sections, {len(figs)} figures; figure renders:')
for p in made:
    print('  ', p)
print('Full-page previews (open in a browser or screenshot):', os.path.join(OUT, f'{tag}_en.html'), os.path.join(OUT, f'{tag}_tc.html'))
