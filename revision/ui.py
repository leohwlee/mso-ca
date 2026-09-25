# Shared building blocks for the Part and Schedule pages: tables, the
# "easy to confuse" callout, and a figure box with a bold title over body text.
from bl_core import *

ICON = ('<svg class="ico" viewBox="0 0 16 16" width="12" height="12" aria-hidden="true">'
        '<path d="M8 1.6 15 14.2H1z" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/>'
        '<path d="M8 6.2v3.9" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/>'
        '<circle cx="8" cy="12.1" r=".95" fill="currentColor"/></svg>')

TAG = f'<span class="trap-tag">{ICON}{B("Easy to confuse", "易混淆", True)}</span>'


def trap(title, body=None, cite=None, vs=None):
    """A callout for a point that is easy to get wrong. title/body are (en, tc) pairs.

    vs is an optional list of ((label_en, label_tc), (text_en, text_tc)) shown side by side.
    """
    inner = P(*body) if body else ''
    if vs:
        inner += '<div class="vs">' + ''.join(
            f'<div><b class="vs-h">{B(*lab, True)}</b>{P(*txt)}</div>' for lab, txt in vs) + '</div>'
    return f'<div class="trap">{TAG}<h3>{B(*title)}</h3>{inner}{cite_html(cite)}</div>'


def traps(*items):
    return '<div class="traps">' + ''.join(items) + '</div>'


def flag():
    """Inline marker for a table cell whose content is easy to confuse."""
    return f'<span class="ttag">{ICON}{B("easy to confuse", "易混淆", True)}</span>'


def th(en, tc):
    return f'<th>{B(en, tc)}</th>'


def rh(en, tc, cite=None):
    return f'<th class="rowh">{B(en, tc)}{cite_html(cite)}</th>'


def td(en, tc, cite=None, cls='', pre='', post=''):
    k = f' class="{cls}"' if cls else ''
    body = B(en, tc)
    if 'pen' in cls.split():
        body = f'<span class="answer" tabindex="0">{body}</span>'
    return f'<td{k}>{pre}{body}{post}{cite_html(cite)}</td>'


def tr(*cells, cls=''):
    k = f' class="{cls}"' if cls else ''
    return f'<tr{k}>' + ''.join(cells) + '</tr>'


def table(head, rows, note=None, minw=720, cls=''):
    t = '<thead><tr>' + ''.join(head) + '</tr></thead>' if head else ''
    # the note spans exactly the real columns: a wider span breaks fixed-layout tables
    n = f'<tr class="note"><td colspan="{len(head) if head else 9}">{note}</td></tr>' if note else ''
    k = f' {cls}' if cls else ''
    return f'<div class="tbl{k}"><table style="min-width:{minw}px">{t}<tbody>{"".join(rows)}{n}</tbody></table></div>'


def h3(en, tc):
    return f'<h3>{B(en, tc)}</h3>'


def fig(svg_html, caption=None, legend=''):
    if callable(svg_html):
        svg_html = tri(svg_html)
    cap = f'<figcaption>{B(*caption)}</figcaption>' if caption else ''
    return f'<figure><div class="figwrap">{svg_html}</div>{legend}{cap}</figure>'


def legend(items):
    """items: list of (css class, (en, tc))."""
    return '<div class="legend">' + ''.join(
        f'<span><i class="{c}"></i>{B(en, tc, True)}</span>' for c, (en, tc) in items) + '</div>'


def chip(en, tc, cls=''):
    return f'<span class="chip {cls}">{B(en, tc, True)}</span>'


YES = chip("yes", "是", 'ink')
NO = chip("no", "否")


class Card(Node):
    """A figure box with a bold title over wrapped body text, per language variant."""

    def __init__(self, x, w, title, body=None, kind='plain', cite=None, href=None,
                 size=11.5, tsize=12.5, minh=0, answer=False):
        size, tsize = size * FS, tsize * FS
        self.x, self.w, self.kind, self.cite, self.href = x, w, kind, cite, href
        self.shape, self.answer, self.size = 'rect', answer, size
        self.text = title
        inner = w - 24
        self.seg = {}
        for i, v in enumerate(('en', 'tc')):
            tl = wrap(title[i], inner, tsize) if title and title[i] else []
            bl = wrap(body[i], inner, size) if body and body[i] else []
            tcls = 't-inv t-b' if kind == 'stop' else ('t t-b t-faint' if kind == 'faint' else 't t-b')
            bcls = 't-inv' if kind == 'stop' else ('t t-faint' if kind == 'faint' else 't')
            self.seg[v] = [(l, tcls, tsize) for l in tl] + [(l, bcls, size) for l in bl]
        self.seg['both'] = self.seg['en'] + self.seg['tc']

        def hh(seg):
            return sum(s * LH for _, _, s in seg)
        self.h = max(minh, hh(self.seg[lay()]) + 16 + (CS * LH if cite else 0))
        self.y = None

    def render(self):
        k = self.kind
        rect = f'<rect class="n n-{k}" x="{self.x}" y="{self.y}" width="{self.w}" height="{self.h}" rx="6"/>'
        out = [rect]
        for v, seg in self.seg.items():
            total = sum(s * LH for _, _, s in seg) + (CS * LH if self.cite else 0)
            y = self.cy - total / 2
            g = [f'<g class="s-{v}">']
            for t, cls, s in seg:
                g.append(f'<text class="{cls}" font-size="{s}" text-anchor="middle"><tspan x="{self.cx}" y="{y + s * 0.95:.1f}">{esc(t)}</tspan></text>')
                y += s * LH
            if self.cite:
                ccls = 'c-inv' if k == 'stop' else 'c'
                g.append(f'<text class="{ccls}" font-size="{CS}" text-anchor="middle"><tspan x="{self.cx}" y="{y + CS * 0.95:.1f}">{esc(cite_txt(self.cite, v))}</tspan></text>')
            g.append('</g>')
            out.append(''.join(g))
        body = ''.join(out)
        if self.answer:
            body = f'<g class="answer" tabindex="0">{body}</g>'
        else:
            body = f'<g>{body}</g>'
        if self.href:
            body = f'<a class="figlink" href="{self.href}">{body}</a>'
        return body


def mlabel(x, y, en, tc, anchor='middle'):
    """Edge label whose bilingual variant stacks English over Chinese instead of joining them."""
    out = []
    for v, ls in (('en', [en]), ('tc', [tc]), ('both', [en, tc])):
        n = len(ls)
        g = [f'<text class="lbl s-{v}" text-anchor="{anchor}">']
        for i, l in enumerate(ls):
            g.append(f'<tspan x="{x}" y="{y - (n - 1 - i) * 13:.1f}">{esc(l)}</tspan>')
        g.append('</text>')
        out.append(''.join(g))
    return ''.join(out)


def hline(x1, x2, y, lab=None, mid=None):
    """A plain connector with an optional label above its middle."""
    s = f'<line class="e" x1="{x1:.0f}" y1="{y:.0f}" x2="{x2:.0f}" y2="{y:.0f}"/>'
    if lab:
        s += label((x1 + x2) / 2, y - 6, lab)
    return s
