# Extract the revision pack into one text file per section, with an English view and
# a Chinese view, so reviewers can check every claim without reading raw HTML.
import copy
import io
import os
import re
import sys
from bs4 import BeautifulSoup, NavigableString, Tag

SP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(SP, 'mso-revision-pack.html')
OUT = os.path.join(SP, 'review', os.environ.get('EXTRACT_DIR', 'sections'))
os.makedirs(OUT, exist_ok=True)

soup = BeautifulSoup(io.open(SRC, encoding='utf-8').read(), 'lxml')


def has_cls(el, *names):
    c = el.get('class') or []
    return any(n in c for n in names)


def strip_lang(root, lang):
    """Remove the other language's elements from a copy of root."""
    r = copy.copy(root)
    drop_html = ('l-tc', 'c-tc', 'only-tc') if lang == 'en' else ('l-en', 'c-en', 'only-en')
    drop_svg = ('s-tc', 's-both') if lang == 'en' else ('s-en', 's-both')
    for el in r.find_all(True):
        if el.parent is None:
            continue
        if has_cls(el, *drop_html) or has_cls(el, *drop_svg):
            el.decompose()
    return r


def svg_text(svg, lang):
    lines = []
    aria = svg.get('data-aria-en' if lang == 'en' else 'data-aria-tc', '')
    for child in svg.children:
        if not isinstance(child, Tag) or child.name in ('defs',):
            continue
        texts = []
        for t in ([child] if child.name == 'text' else child.find_all('text')):
            s = ' '.join(ts.get_text(' ', strip=True) for ts in t.find_all('tspan')) or t.get_text(' ', strip=True)
            if s:
                texts.append(s)
        if texts:
            kind = ''
            rect = child.find(['rect', 'polygon']) if child.name != 'text' else None
            if rect is not None and rect.get('class'):
                kind = '[' + ' '.join(c for c in rect['class'] if c.startswith('n-')) + '] '
            href = ''
            if child.name == 'a' and child.get('href'):
                href = f" (link {child['href']})"
            lines.append('  - ' + kind + ' / '.join(texts) + href)
    return '  FIGURE (description: ' + aria + ')\n' + '\n'.join(lines)


def cell_text(el):
    return re.sub(r'\s+', ' ', el.get_text(' ', strip=True))


def render(node, lang, out):
    for el in node.children:
        if isinstance(el, NavigableString):
            s = str(el).strip()
            if s:
                out.append(s)
            continue
        if not isinstance(el, Tag):
            continue
        if el.name == 'svg':
            out.append(svg_text(el, lang))
        elif el.name == 'table':
            for tr in el.find_all('tr'):
                cells = [cell_text(c) for c in tr.find_all(['th', 'td'], recursive=False)]
                if any(cells):
                    out.append('  | ' + ' | '.join(cells) + ' |')
        elif el.name in ('p', 'h2', 'h3', 'figcaption') or has_cls(el, 'legend'):
            t = cell_text(el)
            if t:
                prefix = {'h2': '## ', 'h3': '### ', 'figcaption': 'CAPTION: '}.get(el.name, '')
                if has_cls(el, 'legend'):
                    prefix = 'KEY: '
                out.append(prefix + t)
        elif has_cls(el, 'trap'):
            out.append('EASY-TO-CONFUSE BOX: ' + cell_text(el))
        else:
            render(el, lang, out)


docs = soup.select('section.doc')
index = []
for doc in docs:
    did = doc['id']
    title_en = cell_text(strip_lang(doc.select_one('header h1'), 'en'))
    for sec in doc.select('section.sec'):
        sid = sec['id']
        parts = [f'# {did} / {sid}   ({title_en})']
        for lang in ('en', 'tc'):
            s = strip_lang(sec, lang)
            margin = cell_text(s.select_one('.margin'))
            out = []
            render(s.select_one('.body'), lang, out)
            parts.append(f'\n===== {lang.upper()} VIEW =====\nMARGIN: {margin}\n' + '\n'.join(out))
        # the document lede and footer travel with the first section of each doc
        if sec is doc.select('section.sec')[0]:
            for lang in ('en', 'tc'):
                h = strip_lang(doc.select_one('header'), lang)
                f = strip_lang(doc.select_one('footer'), lang)
                parts.append(f'\n===== DOC HEADER/FOOTER {lang.upper()} =====\n{cell_text(h)}\nFOOTER: {cell_text(f)}')
        text = '\n'.join(parts)
        fn = f'{did[4:]}__{sid}.txt'
        io.open(os.path.join(OUT, fn), 'w', encoding='utf-8').write(text)
        index.append((fn, len(text)))
io.open(os.path.join(OUT, '_index.txt'), 'w', encoding='utf-8').write('\n'.join(f'{a}\t{b}' for a, b in index))
print(len(index), 'sections; total chars', sum(b for _, b in index))
