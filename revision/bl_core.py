# Bilingual core: text measuring, wrapping, SVG nodes with EN / TC / both variants.
import html
import re

warnings = []

# Figures are drawn once per language view. MODE['lang'] is the view being drawn;
# None means the old single drawing that carries all three variants.
MODE = {'lang': None}


def lay():
    """The language variant whose text sets box sizes."""
    return MODE['lang'] or 'both'


def mref(mid):
    """Marker id for the view being drawn, so the three drawings never share an id."""
    return mid + ({'en': '-e', 'tc': '-t', 'both': '-b'}[MODE['lang']] if MODE['lang'] else '')


def esc(s):
    return html.escape(s, quote=False)


# ---------------------------------------------------------------- citations
# A citation is either a plain English string, converted to Chinese automatically
# for the Chinese-only view, or an explicit (en, tc) pair when it carries words.
def _runs(body):
    return body.replace('–', '至').replace('—', '至').replace(', ', '、').replace(',', '、')


def _seg_cn(seg):
    seg = seg.strip()
    if not seg or seg == '—':
        return seg
    m = re.fullmatch(r'Sch\.\s*(\d+[A-Z]?)\s*Pt\s*(\d+)', seg)
    if m:
        return '附表%s第%s部' % (m.group(1), m.group(2))
    m = re.fullmatch(r'Part\s*(\d+[A-Z]?)', seg)
    if m:
        return '第%s部' % m.group(1)
    if seg == 'Appendix A':
        return '附錄A'
    m = re.fullmatch(r'Ch\.\s*([\d–, ]+)', seg)
    if m:
        return '第%s章' % _runs(m.group(1).strip())
    m = re.fullmatch(r'fn\s*(\d+)', seg)
    if m:
        return '註%s' % m.group(1)
    tail = ''
    m = re.match(r'^(.*?)\s+fn\s*(\d+)$', seg)
    if m:
        seg, tail = m.group(1), ' 註%s' % m.group(2)
    pre = ''
    m = re.match(r'^(.*?)\s*Sch\.\s*(\d+[A-Z]?)$', seg)
    if m and m.group(1):
        seg, pre = m.group(1).strip(), '附表%s' % m.group(2)
    elif re.fullmatch(r'Sch\.\s*\d+[A-Z]?', seg):
        return '附表%s' % seg.split('.')[-1].strip() + tail
    m = re.fullmatch(r'items?\s+(.+)', seg)
    if m:
        return pre + '第' + _runs(m.group(1)) + '項' + tail
    if seg.startswith('¶'):
        return pre + '第' + _runs(seg[1:]) + '段' + tail
    if seg.startswith('s.'):
        return pre + '第' + _runs(re.sub(r's\.\s*', '', seg)) + '條' + tail
    if re.fullmatch(r'[\d.]+[\d.()a-z–,\s]*', seg):
        return pre + '第' + _runs(seg) + '段' + tail
    return pre + seg + tail


def cn_cite(s):
    return ' · '.join(_seg_cn(p) for p in s.split('·'))


def cite_txt(c, v):
    """The citation string for one language variant. 'both' keeps the English form."""
    if not c:
        return None
    if isinstance(c, tuple):
        return c[1] if v == 'tc' else c[0]
    return cn_cite(c) if v == 'tc' else c


def cite_pair(c):
    return cite_txt(c, 'en'), cite_txt(c, 'tc')


def cite_html(c, cls='cite'):
    if not c:
        return ''
    en, tc = cite_pair(c)
    if en == tc:
        return f'<span class="{cls}">{esc(en)}</span>'
    return f'<span class="{cls}"><span class="c-en">{esc(en)}</span><span class="c-tc" lang="zh-Hant">{esc(tc)}</span></span>'


def is_cjk(ch):
    return ('⺀' <= ch <= '鿿') or ('豈' <= ch <= '﫿') or ('＀' <= ch <= '￯') or ('　' <= ch <= '〿')


NOSTART = set('，。；：、）」』！？】》')


def tokens(text):
    out, cur = [], ''
    for ch in text:
        if is_cjk(ch):
            if cur:
                out.append(cur); cur = ''
            out.append(ch)
        elif ch == ' ':
            if cur:
                out.append(cur); cur = ''
            out.append(' ')
        else:
            cur += ch
    if cur:
        out.append(cur)
    return out


def tw(tok, size, mono=False):
    lat = 0.64 if mono else 0.56
    return sum((1.0 if is_cjk(c) else (0.3 if c == ' ' else lat)) for c in tok) * size


def wrap(text, width_px, size, mono=False):
    lines, cur, cw = [], '', 0.0
    for tok in tokens(text):
        w = tw(tok, size, mono)
        if tok == ' ':
            if cur:
                cur += ' '; cw += w
            continue
        if cw + w <= width_px or not cur or (tok in NOSTART):
            cur += tok; cw += w
        else:
            lines.append(cur.rstrip()); cur, cw = tok, w
    if cur.strip():
        lines.append(cur.rstrip())
    return lines


LH = 1.3
# Figures are drawn about 1000 units wide but shown about 870px wide, so every size a
# figure asks for is scaled up by FS to keep text at 11px or more on screen.
FS = 1.25
CS = 10.5 * FS   # cite size


def block_lines(text, width_px, size):
    """text is (en, tc). Returns dict variant -> list of lines."""
    en, tc = text
    le = wrap(en, width_px, size) if en else []
    lt = wrap(tc, width_px, size) if tc else []
    return {'en': le, 'tc': lt, 'both': le + lt}


def text_variants(cx, cy, variants, size, cls, cite=None, ccls='c'):
    """Three <g> groups (l-en, l-tc, l-both), each vertically centred on cy."""
    out = []
    lh = size * LH
    clh = CS * LH
    for v, lines in variants.items():
        total = len(lines) * lh + (clh if cite else 0)
        top = cy - total / 2
        g = [f'<g class="s-{v}">', f'<text class="{cls}" font-size="{size}" text-anchor="middle">']
        for i, l in enumerate(lines):
            g.append(f'<tspan x="{cx}" y="{top + size * 0.85 + i * lh:.1f}">{esc(l)}</tspan>')
        g.append('</text>')
        if cite:
            g.append(f'<text class="{ccls}" font-size="{CS}" text-anchor="middle"><tspan x="{cx}" y="{top + len(lines) * lh + CS * 0.9:.1f}">{esc(cite_txt(cite, v))}</tspan></text>')
        g.append('</g>')
        out.append(''.join(g))
    return ''.join(out)


def need_h(variants, size, cite):
    n = len(variants[lay()])
    return n * size * LH + (CS * LH if cite else 0) + 14


class Node:
    def __init__(self, x, w, text, cite=None, kind='plain', size=12, answer=False, shape='rect', minh=0):
        size = size * FS
        self.x, self.w, self.text, self.cite, self.kind, self.size, self.answer, self.shape = x, w, text, cite, kind, size, answer, shape
        inner = w - 22 if shape == 'rect' else w - 56
        self.v = block_lines(text, inner, size)
        self.h = max(minh, need_h(self.v, size, cite))
        if shape == 'hex':
            self.h += 6
        self.y = None

    @property
    def cx(self): return self.x + self.w / 2
    @property
    def cy(self): return self.y + self.h / 2
    @property
    def top(self): return (self.cx, self.y)
    @property
    def bottom(self): return (self.cx, self.y + self.h)
    @property
    def left(self): return (self.x, self.cy)
    @property
    def right(self): return (self.x + self.w, self.cy)

    def render(self):
        inv = self.kind == 'stop'
        if self.shape == 'hex':
            k = 16
            x, y, w, h = self.x, self.y, self.w, self.h
            shape = f'<polygon class="n n-dec" points="{x},{y+h/2} {x+k},{y} {x+w-k},{y} {x+w},{y+h/2} {x+w-k},{y+h} {x+k},{y+h}"/>'
        else:
            shape = f'<rect class="n n-{self.kind}" x="{self.x}" y="{self.y}" width="{self.w}" height="{self.h}" rx="6"/>'
        txt = text_variants(self.cx, self.cy, self.v, self.size, 't-inv' if inv else 't', self.cite, 'c-inv' if inv else 'c')
        g = '<g class="answer" tabindex="0">' if self.answer else '<g>'
        return f'{g}{shape}{txt}</g>'


def place(rows, y0=16, gap=40):
    """rows: list of (list_of_nodes, gap_after). Sets y; returns total height."""
    y = y0
    for nodes, g in rows:
        hmax = max(n.h for n in nodes)
        for n in nodes:
            n.y = y + (hmax - n.h) / 2   # centre vertically within the row
        y += hmax + g
    return y


def label(x, y, text, anchor='middle'):
    """Bilingual edge label: text is (en, tc); 'both' shows 'en / tc'."""
    en, tc = text
    out = []
    for v, s in (('en', en), ('tc', tc), ('both', f'{en} / {tc}' if en != tc else en)):
        out.append(f'<text class="lbl s-{v}" x="{x}" y="{y}" text-anchor="{anchor}">{esc(s)}</text>')
    return ''.join(out)


def edge(pts, lab=None, lx=None, ly=None, anchor='middle', marker=True, mid='arr', mstart=False):
    d = ' '.join(f'{x:.0f},{y:.0f}' for x, y in pts)
    m = f' marker-end="url(#{mref(mid)})"' if marker else ''
    if mstart:
        m += f' marker-start="url(#{mref(mid)})"'
    s = f'<polyline class="e" points="{d}"{m}/>'
    if lab:
        s += label(lx, ly, lab, anchor)
    return s


def path(a, b, via=None):
    """Orthogonal polyline from point a to point b. via: list of intermediate points."""
    return [a] + (via or []) + [b]


def esca(s):
    return html.escape(s, quote=True)


def svg(w, h, body, aria, mid, minw):
    en, tc = aria
    v = MODE['lang']
    cls = f'fig s-{v}' if v else 'fig'
    label = tc if v == 'tc' else en
    return (f'<svg class="{cls}" viewBox="0 0 {w} {h:.0f}" role="img" aria-label="{esca(label)}" '
            f'data-aria-en="{esca(en)}" data-aria-tc="{esca(tc)}" style="min-width:{minw}px">'
            f'<defs><marker id="{mref(mid)}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" '
            f'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z"/></marker></defs>{body}</svg>')


def _keep_only(s, keep):
    """Drop the text variants of the other two views from one view's drawing."""
    for v in ('en', 'tc', 'both'):
        if v == keep:
            continue
        s = re.sub(r'<g class="s-%s">.*?</g>' % v, '', s, flags=re.S)
        s = re.sub(r'<text class="(?:[^"]* )?s-%s(?: [^"]*)?"[^>]*>.*?</text>' % v, '', s, flags=re.S)
    return s


def tri(fn):
    """Draw a figure three times, each laid out for one language view."""
    out = []
    for v in ('en', 'tc', 'both'):
        MODE['lang'] = v
        try:
            out.append(_keep_only(fn(), v))
        finally:
            MODE['lang'] = None
    return ''.join(out)


def lbl_lines(cx, y_bottom, lines_en, lines_tc, cls='lbl'):
    """Multi-line label near an edge; variants stacked upward from y_bottom."""
    out = []
    for v, lines in (('en', lines_en), ('tc', lines_tc), ('both', lines_en + lines_tc)):
        n = len(lines)
        g = [f'<text class="{cls} s-{v}" text-anchor="middle">']
        for i, l in enumerate(lines):
            g.append(f'<tspan x="{cx}" y="{y_bottom - (n - 1 - i) * 13:.1f}">{esc(l)}</tspan>')
        g.append('</text>')
        out.append(''.join(g))
    return ''.join(out)


# ---------------------------------------------------------------- HTML helpers
def B(en, tc, inl=False):
    if en == tc:
        return en
    c = 'l-tc inl' if inl else 'l-tc'
    return f'<span class="l-en">{en}</span><span class="{c}" lang="zh-Hant">{tc}</span>'


def P(en, tc, cls=None):
    c = f' class="{cls}"' if cls else ''
    return f'<p{c}>{B(en, tc)}</p>'


def li(items):
    return '<ul>' + ''.join(f'<li>{B(*x)}</li>' for x in items) + '</ul>'


def card(title, cite, body, kind='', tag=None):
    t = f'<span class="chip {tag[2]}">{B(tag[0], tag[1], True)}</span>' if tag else ''
    return f'<div class="card {kind}"><h3>{B(*title)}{t}</h3>{body}{cite_html(cite)}</div>'


def marg(x):
    en, tc = cite_pair(x) if isinstance(x, tuple) else (x, cn_cite(x))
    if en == tc:
        return f'<span>{esc(en)}</span>'
    return f'<span><span class="c-en">{esc(en)}</span><span class="c-tc" lang="zh-Hant">{esc(tc)}</span></span>'


def sec(id_, margin_lines, h2, body):
    m = ''.join(marg(x) for x in margin_lines)
    return f'<section class="sec" id="{id_}"><div class="margin">{m}</div><div class="body"><h2>{B(*h2)}</h2>{body}</div></section>'


def ans(x):
    return f'<span class="answer">{x}</span>'


def numreq(rows, minw=760, heading=True):
    """Numeric requirements: (number, requirement, when it applies, consequence, cite).

    Each element except the citation is an (en, tc) pair.
    """
    head = ('<thead><tr>'
            f'<th>{B("The number", "數字")}</th>'
            f'<th>{B("What it requires", "規定甚麼")}</th>'
            f'<th>{B("When it applies", "何時適用")}</th>'
            f'<th>{B("If it is missed", "未達標的後果")}</th>'
            '</tr></thead>')
    body = ''.join(
        '<tr>'
        f'<td class="numreq"><span class="answer" tabindex="0">{B(*num)}</span></td>'
        f'<td>{B(*req)}{cite_html(cite)}</td>'
        f'<td>{B(*when)}</td>'
        f'<td class="cons">{B(*cons)}</td>'
        '</tr>'
        for num, req, when, cons, cite in rows)
    h3 = '<h3>' + B("The numbers in this section, and what happens if you miss them",
                    "本節的數字，以及未達標的後果") + '</h3>' if heading else ''
    return h3 + f'<div class="tbl"><table style="min-width:{minw}px">{head}<tbody>{body}</tbody></table></div>'
