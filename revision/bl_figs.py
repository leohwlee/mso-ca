# Figures for Schedule 2 sections 1-4 (map, beneficial owner, timing), bilingual, laid out
# per language view. lines_down and stack_down are shared with other pages: keep their signatures.
from bl_core import *


# ---------------------------------------------------------------- shared helpers
def lines_down(cx, y_top, en, tc, cls, size=11):
    size = size * FS
    out = []
    for v, ls in (('en', en), ('tc', tc), ('both', en + tc)):
        g = [f'<text class="{cls} s-{v}" font-size="{size}" text-anchor="middle">']
        for i, l in enumerate(ls):
            g.append(f'<tspan x="{cx}" y="{y_top + size + i * size * 1.3:.1f}">{esc(l)}</tspan>')
        g.append('</text>')
        out.append(''.join(g))
    return ''.join(out)


def stack_down(cx, y_top, blocks):
    """Several text blocks stacked downward; each language variant keeps its own running height."""
    out = []
    for v in ('en', 'tc', 'both'):
        y = y_top
        for en, tc, cls, size in blocks:
            size = size * FS
            ls = en if v == 'en' else tc if v == 'tc' else en + tc
            g = [f'<text class="{cls} s-{v}" font-size="{size}" text-anchor="middle">']
            for i, l in enumerate(ls):
                g.append(f'<tspan x="{cx}" y="{y + size + i * size * 1.3:.1f}">{esc(l)}</tspan>')
            g.append('</text>')
            out.append(''.join(g))
            y += len(ls) * size * 1.3 + 6
    return ''.join(out)


# Chinese terms that must never be split across two lines.
PROTECT = sorted(['盡職審查', '高級管理層', '財富情報組', '之前', '之後', '若干次', '資金籌集', '業務關係', '非經常交易',
                  '實益擁有人', '可疑交易報告', '身分資料', '恐怖分子', '電傳轉帳', '虛擬資產', '持續監察', '有關連',
                  '金錢服務經營者', '門檻', '合併計算', '風險', '措施', '核實', '身分', '交易', '款額', '同等',
                  '資金來源', '財富來源', '批准', '簡化', '終止', '建立', '進行', '執行',
                  '8,000元', '120,000元', '應合併計算', '須穿透'], key=len, reverse=True)


def _toks(text):
    """tokens(), but a protected Chinese term is one unbreakable token."""
    out, cur, i = [], '', 0
    while i < len(text):
        term = next((p for p in PROTECT if text.startswith(p, i)), None)
        ch = text[i]
        if term or is_cjk(ch) or ch == ' ':
            if cur:
                out.append(cur); cur = ''
            tok = term or ch
            out.append(tok)
            i += len(tok)
        else:
            cur += ch
            i += 1
    if cur:
        out.append(cur)
    return out


def _wrap(text, width_px, size):
    lines, cur, cw = [], '', 0.0
    for tok in _toks(text):
        w = tw(tok, size)
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


def wrap_bal(text, width, size):
    """Wrap without splitting protected Chinese terms, then pull words down so the last line is
    neither a lone English word nor a character or two. Prefers the same number of lines; accepts one
    more line only when that is the only way to avoid a lone last word."""
    lines = _wrap(text, width, size)
    if len(lines) < 2:
        return lines

    def short(ls):
        last = ls[-1]
        lone = ' ' not in last and not any(is_cjk(c) for c in last)
        return lone or tw(last, size) < 0.3 * width

    if not short(lines):
        return lines
    alts = [_wrap(text, width * (1 - 0.025 * k), size) for k in range(1, 17)]
    for n in (len(lines), len(lines) + 1):
        for alt in alts:
            if len(alt) == n and not short(alt):
                return alt
    return lines


class Box(Node):
    """A rectangle with an optional bold title and body paragraphs, each wrapped separately.

    In the combined view a small gap separates the English block from the Chinese one.
    """

    def __init__(self, x, w, title=None, paras=(), kind='plain', cite=None, size=11.5, tsize=12, answer=False, minh=0):
        size, tsize = size * FS, tsize * FS
        self.x, self.w, self.kind, self.cite, self.answer = x, w, kind, cite, answer
        self.shape, self.size, self.text = 'rect', size, title
        inv = kind == 'stop'
        tcls = 't-inv t-b' if inv else ('t t-b t-faint' if kind == 'faint' else 't t-b')
        bcls = 't-inv' if inv else ('t t-faint' if kind == 'faint' else 't')
        inner = w - 26
        self.seg = {}
        for i, v in enumerate(('en', 'tc')):
            s = [(l, tcls, tsize) for l in wrap_bal(title[i], inner, tsize)] if title else []
            for p in paras:
                s += [(l, bcls, size) for l in wrap_bal(p[i], inner, size)]
            self.seg[v] = s
        self.seg['both'] = self.seg['en'] + [('', bcls, 6)] + self.seg['tc']
        self.h = max(minh, self._hh(self.seg[lay()]) + 20)
        self.y = None

    def _hh(self, seg):
        return sum(s * LH for _, _, s in seg) + (CS * LH if self.cite else 0)

    def render(self):
        out = [f'<rect class="n n-{self.kind}" x="{self.x}" y="{self.y}" width="{self.w}" height="{self.h}" rx="6"/>']
        for v, seg in self.seg.items():
            y = self.cy - self._hh(seg) / 2
            g = [f'<g class="s-{v}">']
            for t, cls, s in seg:
                if t:
                    g.append(f'<text class="{cls}" font-size="{s}" text-anchor="middle"><tspan x="{self.cx}" y="{y + s * 0.95:.1f}">{esc(t)}</tspan></text>')
                y += s * LH
            if self.cite:
                ccls = 'c-inv' if self.kind == 'stop' else 'c'
                g.append(f'<text class="{ccls}" font-size="{CS}" text-anchor="middle"><tspan x="{self.cx}" y="{y + CS * 0.95:.1f}">{esc(cite_txt(self.cite, v))}</tspan></text>')
            g.append('</g>')
            out.append(''.join(g))
        body = ''.join(out)
        return f'<g class="answer" tabindex="0">{body}</g>' if self.answer else f'<g>{body}</g>'


class Hex(Node):
    """A question node whose lines are balanced so no word or character is left alone.

    In the combined view the same 6-unit gap as in Box separates English from Chinese.
    """
    GAP = 6

    def __init__(self, x, w, text, cite=None, size=12):
        super().__init__(x, w, text, cite, shape='hex', size=size)
        en, tc = text
        inner = w - 56
        le, lt = wrap_bal(en, inner, self.size), wrap_bal(tc, inner, self.size)
        self.v = {'en': le, 'tc': lt, 'both': le + lt}
        self.split = {'en': len(le), 'tc': len(lt), 'both': len(le)}
        self.h = need_h(self.v, self.size, cite) + 6 + (self.GAP if lay() == 'both' else 0)

    def render(self):
        k = 16
        x, y, w, h = self.x, self.y, self.w, self.h
        out = [f'<polygon class="n n-dec" points="{x},{y+h/2} {x+k},{y} {x+w-k},{y} {x+w},{y+h/2} {x+w-k},{y+h} {x+k},{y+h}"/>']
        lh, clh = self.size * LH, CS * LH
        for v, lines in self.v.items():
            gap = self.GAP if v == 'both' and self.split['both'] < len(lines) else 0
            top = self.cy - (len(lines) * lh + gap + (clh if self.cite else 0)) / 2
            g = [f'<g class="s-{v}">', f'<text class="t" font-size="{self.size}" text-anchor="middle">']
            yy = top
            for i, l in enumerate(lines):
                if i == self.split['both'] and v == 'both':
                    yy += gap
                g.append(f'<tspan x="{self.cx}" y="{yy + self.size * 0.85:.1f}">{esc(l)}</tspan>')
                yy += lh
            g.append('</text>')
            if self.cite:
                g.append(f'<text class="c" font-size="{CS}" text-anchor="middle"><tspan x="{self.cx}" y="{yy + CS * 0.9:.1f}">{esc(cite_txt(self.cite, v))}</tspan></text>')
            g.append('</g>')
            out.append(''.join(g))
        return '<g>' + ''.join(out) + '</g>'


def place_top(rows, y0=16):
    """Like place(), but siblings in a row share the same top edge."""
    y = y0
    for nodes, g in rows:
        for n in nodes:
            n.y = y
        y += max(n.h for n in nodes) + g
    return y


def place_bottom(nodes, y0):
    """Siblings share the same bottom edge; returns that bottom."""
    hmax = max(n.h for n in nodes)
    for n in nodes:
        n.y = y0 + hmax - n.h
    return y0 + hmax


def block_h(lines_en, lines_tc, size):
    n = {'en': len(lines_en), 'tc': len(lines_tc), 'both': len(lines_en) + len(lines_tc)}[lay()]
    return n * size * FS * 1.3


# ---------------------------------------------------------------- Figure 1: the map
def fig1():
    W = 1040
    start = Box(370, 300, None, [("Someone asks the MSO for a service", "有人向金錢服務經營者要求服務")])
    D1 = Hex(290, 460, ("Will there be a business relationship — one with an element of duration, or expected to have one?", "會否建立業務關係——即延續一段時間是該關係的元素，或預期如此？"), "¶4.2.2 · s.1 Sch. 2")
    A = Box(20, 250, None, [("Carry out CDD before the relationship is established", "在建立業務關係之前執行盡職審查措施")], 'must', "¶4.2.1(a) · s.3(1)(a) Sch. 2", answer=True)
    D2 = Hex(430, 440, ("It is an occasional transaction. Which kind, counting linked operations together?", "這是非經常交易。屬哪一類？有關連的若干次操作須合併計算"), "¶4.2.3–4.2.5 · s.3(1)(b), (1A) Sch. 2")
    C1 = Box(280, 230, None, [("Wire transfer or virtual-asset transfer of HK$8,000 or more, or the equivalent", "電傳轉帳或虛擬資產轉帳，款額達8,000元或以上（或其他貨幣的同等款額）")], 'must', "¶4.2.1(b)(ii)–(iii)", answer=True)
    C2 = Box(535, 230, None, [("Any other transaction of HK$120,000 or more, or the equivalent", "其他任何交易，款額達120,000元或以上（或同等款額）")], 'must', "¶4.2.1(b)(i)", answer=True)
    C3 = Box(770, 260, None, [("Below the threshold that applies to it", "低於適用門檻")])
    D3 = Hex(770, 260, ("Any suspicion of ML/TF, or doubt about identity information obtained earlier?", "有否懷疑涉及洗錢／恐怖分子資金籌集，或懷疑過往取得的身分資料是否真實或充分？"), "¶4.2.1(c)–(d) · fn 15")
    K = Box(280, 420, None, [("CDD is required. Apply all four measures before the relationship or the transaction.", "須執行盡職審查：在建立業務關係或進行交易之前，執行全部四項措施。")], 'plain', "¶4.1.3, 4.8.1 · s.2(1) Sch. 2")
    N = Box(770, 260, None, [("No CDD trigger. Stay alert: linked occasional transactions that together reach the threshold should be added up.", "毋須執行盡職審查。但應留意：有關連的非經常交易合計達門檻，應合併計算。")], 'plain', "¶4.2.4–4.2.5", answer=True)
    D4 = Hex(280, 420, ("How much ML/TF risk do this customer and relationship carry?", "這名客戶及業務關係的洗錢／恐怖分子資金籌集風險有多高？"), ("risk-based approach · ¶4.1.2, 4.8.1", "風險為本的方法 · 第4.1.2、4.8.1段"))
    S = Box(20, 310, None, [("Low risk: simplified due diligence is permitted. Simplify the measures, never the ongoing monitoring. Stop SDD if the risk rises, suspicion arises or documents are doubted.", "低風險：可執行簡化盡職審查。可簡化措施，但持續監察絕不可免。風險上升、有懷疑或對文件存疑時，即停止簡化。")], 'may', "¶4.8.2–4.8.3, 4.8.6 · s.5(1) Sch. 2", answer=True)
    M = Box(360, 260, None, [("All four CDD measures, to an extent that matches the risk.", "全部四項盡職審查措施，程度與風險相稱。")], 'plain', "¶4.8.1", answer=True)
    E = Box(690, 330, None, [("High risk: enhanced due diligence is mandatory. Senior management approves the relationship; monitoring is enhanced; add measures such as source of funds and wealth.", "高風險：必須執行更嚴格的盡職審查。高級管理層批准業務關係；加強持續監察；增加措施，例如查明資金來源及財富來源。")], 'must', "¶4.9.1–4.9.4, 4.9.6 · s.15 Sch. 2", answer=True)
    D5 = Hex(310, 360, ("Can you actually complete these measures?", "能否切實完成這些措施？"), "¶4.13.1 · s.3(4) Sch. 2")
    Pn = Box(30, 440, None, [("Proceed. Verify identity before or during establishment; only exceptionally afterwards, under the ¶4.7 controls. Then monitor the relationship continuously.", "可以進行。在建立業務關係之前或過程中核實身分；只可在例外情況下、按第4.7段的管控措施於其後核實。此後持續監察業務關係。")], 'ok', "¶4.7.1, 4.7.3 · Ch. 5 · s.5 Sch. 2", answer=True)
    X = Box(560, 450, None, [("Must not establish the relationship or carry out the transaction; terminate an existing relationship as soon as reasonably practicable; where there is relevant knowledge or suspicion, make an STR to the JFIU.", "不可建立業務關係或進行交易；現有業務關係須在合理地切實可行的範圍內盡快結束；如有相關知悉或懷疑，應向財富情報組提交可疑交易報告。")], 'stop', "¶4.13.1 · s.3(4) Sch. 2", answer=True)
    H = place_top([([start], 36), ([D1], 50), ([A, D2], 56), ([C1, C2, C3], 40), ([D3], 48), ([K, N], 56), ([D4], 62), ([S, M, E], 38), ([D5], 60), ([Pn, X], 0)])
    b = [n.render() for n in (start, D1, A, D2, C1, C2, C3, D3, N, K, D4, S, M, E, D5, Pn, X)]
    m = 'a1'
    YES, NO = ("yes", "是"), ("no", "否")
    b.append(edge([start.bottom, D1.top], mid=m))
    b.append(edge([D1.left, (A.cx, D1.cy), A.top], YES, (D1.x + A.cx) / 2, D1.cy - 7, mid=m))
    jy = D1.bottom[1] + 24
    b.append(edge([D1.bottom, (D1.cx, jy), (D2.cx, jy), D2.top], NO, (D1.cx + D2.cx) / 2, jy - 7, mid=m))
    fy = D2.bottom[1] + 24
    b.append(edge([D2.bottom, (D2.cx, fy), (C1.cx, fy), C1.top], mid=m))
    b.append(edge([D2.bottom, C2.top], mid=m))
    b.append(edge([D2.bottom, (D2.cx, fy), (C3.cx, fy), C3.top], mid=m))
    b.append(edge([C3.bottom, D3.top], mid=m))
    b.append(edge([D3.bottom, N.top], NO, D3.cx + 10, (D3.bottom[1] + N.top[1]) / 2 + 5, 'start', mid=m))
    vx = 735   # midway between K's right edge (700) and N's left edge (770)
    b.append(edge([D3.left, (vx, D3.cy), (vx, K.cy), K.right], YES, vx - 6, D3.cy - 7, 'end', mid=m))
    b.append(edge([A.bottom, (A.cx, K.cy), K.left], mid=m))
    b.append(edge([C1.bottom, (C1.cx, K.top[1])], mid=m))
    b.append(edge([C2.bottom, (C2.cx, K.top[1])], mid=m))
    b.append(edge([K.bottom, D4.top], mid=m))
    b.append(edge([D4.left, (S.cx, D4.cy), S.top], ("low", "低"), (D4.x + S.cx) / 2, D4.cy - 7, mid=m))
    b.append(edge([D4.bottom, M.top], ("otherwise", "其他"), D4.cx + 10, (D4.bottom[1] + M.top[1]) / 2 + 5, 'start', mid=m))
    b.append(edge([D4.right, (E.cx, D4.cy), E.top], ("high", "高"), (D4.x + D4.w + E.cx) / 2, D4.cy - 7, mid=m))
    jy2 = max(S.bottom[1], M.bottom[1], E.bottom[1]) + 14
    b.append(edge([S.bottom, (S.cx, jy2), (M.cx, jy2)], marker=False))
    b.append(edge([E.bottom, (E.cx, jy2), (M.cx, jy2)], marker=False))
    b.append(edge([M.bottom, D5.top], mid=m))
    b.append(edge([D5.left, (Pn.cx, D5.cy), Pn.top], YES, (D5.x + Pn.cx) / 2, D5.cy - 7, mid=m))
    b.append(edge([D5.right, (X.cx, D5.cy), X.top], NO, (D5.x + D5.w + X.cx) / 2, D5.cy - 7, mid=m))
    aria = ("Decision tree: a business relationship needs CDD before it is established; an occasional transaction needs CDD at HK$8,000 for wire or virtual-asset transfers and HK$120,000 otherwise, or whenever ML/TF is suspected or earlier identity information is doubted. All paths then meet a risk assessment that selects simplified due diligence, all four CDD measures or enhanced due diligence, and finally a check on whether CDD can be completed.",
            "決策樹：建立業務關係前須執行盡職審查；非經常交易在電傳轉帳或虛擬資產轉帳達8,000元、其他交易達120,000元時，或有懷疑時，須執行盡職審查；其後按風險選擇簡化盡職審查措施、全部四項盡職審查措施或更嚴格的盡職審查措施，最後判斷能否完成。")
    return svg(W, H + 16, ''.join(b), aria, m, 860)


# ---------------------------------------------------------------- Figure 3: beneficial owner chain
PARAS_WH = [("Holds 50% of Peak", "持有峰匯50%"), ("50% × 60% = 30% indirect", "50% × 60% = 間接持有30%"), ("→ beneficial owner", "→ 實益擁有人")]


def fig3():
    W = 1040
    wong = Box(30, 240, ("Mr Wong · natural person", "王先生 · 自然人"),
               PARAS_WH, 'ok', answer=True)
    ho = Box(290, 240, ("Ms Ho · natural person", "何女士 · 自然人"),
             PARAS_WH, 'ok', answer=True)
    peak = Box(30, 480, ("Peak Holdings Ltd · corporate shareholder", "峰匯控股有限公司 · 法團股東"),
               [("An intermediate layer, not a beneficial owner itself: a beneficial owner is a natural person. Look through it to the individuals behind it.", "屬中介層，本身並非實益擁有人：實益擁有人是自然人。須穿透至其背後的個人。")], 'faint', "¶4.4.1, 4.4.6, 4.4.13 · s.1 Sch. 2", answer=True)
    chan = Box(530, 190, ("Ms Chan", "陳女士"), [("natural person", "自然人"), ("30% direct", "直接持有30%"), ("→ beneficial owner", "→ 實益擁有人")], 'ok', answer=True)
    lee = Box(740, 290, ("Mr Lee · sole director", "李先生 · 唯一董事"),
              [("10%: not a beneficial owner by ownership.", "持有10%："), ("", "以擁有權計並非實益擁有人。"),
               ("As a director he is a connected party: record his name.", "身為董事，屬有關連者：記錄其姓名。"),
               ("A beneficial owner only if he exercises ultimate control over management.", "只有對管理行使最終控制權時，"), ("", "才屬實益擁有人。")],
              'plain', "¶4.3.19 · ¶4.4.6(a)(iii)", answer=True)
    cust = Box(300, 460, ("Harbour Trading Ltd: the customer", "港灣貿易有限公司（客戶）"), [("a corporation", "法團")], 'plain', "¶4.4.6")
    y = place_top([([wong, ho], 58)])
    y = place_top([([peak, chan, lee], 0)], y0=y)
    my = y + 34
    cust.y = my + 30
    H = cust.y + cust.h
    b = [n.render() for n in (wong, ho, peak, chan, lee, cust)]
    m = 'a3'
    ly = wong.bottom[1] + 26
    b.append(edge([wong.bottom, (wong.cx, peak.top[1])], ("50%", "50%"), wong.cx + 8, ly, 'start', mid=m))
    b.append(edge([ho.bottom, (ho.cx, peak.top[1])], ("50%", "50%"), ho.cx + 8, ly, 'start', mid=m))
    b.append(edge([peak.bottom, (peak.cx, my), (400, my), (400, cust.top[1])], ("60%", "60%"), peak.cx + 8, peak.bottom[1] + 20, 'start', mid=m))
    b.append(edge([chan.bottom, (chan.cx, cust.top[1])], ("30%", "30%"), chan.cx + 8, chan.bottom[1] + 20, 'start', mid=m))
    b.append(edge([lee.bottom, (lee.cx, my), (730, my), (730, cust.top[1])], ("10%", "10%"), lee.cx + 8, lee.bottom[1] + 20, 'start', mid=m))
    aria = ("Ownership chart: two people each hold half of a holding company that owns 60% of the customer, so each holds 30% indirectly and is a beneficial owner; a 30% direct shareholder is a beneficial owner; a 10% shareholder who is sole director is a connected party.",
            "擁有權架構圖：兩人各持有一間控股公司一半股份，該公司持有客戶60%，故兩人各間接持有30%，屬實益擁有人；直接持有30%者亦屬實益擁有人；持有10%的唯一董事屬有關連者。")
    return svg(W, H + 16, ''.join(b), aria, m, 860)


# ---------------------------------------------------------------- Figure 5: timing
def _track(y, title, boxes, ticks, m):
    """One timeline: a label, boxes resting on the axis, ticks with text below. Returns (svg, bottom)."""
    out = [label(40, y + 14, title, 'start')]
    bottom = place_bottom(boxes, y + 26)
    out += [n.render() for n in boxes]
    ay = bottom + 16
    out.append(f'<line class="e" x1="30" y1="{ay}" x2="{W5 - 20}" y2="{ay}" marker-end="url(#{mref(m)})"/>')
    low = ay
    for tk in ticks:
        x, blocks = tk[0], tk[1]
        out.append(f'<line class="e" x1="{x}" y1="{ay - 8}" x2="{x}" y2="{ay + 8}"/>')
        yy = ay + 12
        if len(tk) > 2:                      # a box hanging from the tick
            bx = tk[2]
            bx.y = ay + 16
            out.append(edge([(x, ay + 8), (x, bx.y)], marker=False))
            out.append(bx.render())
            yy = bx.y + bx.h + 6
        for en, tc, cls, size in blocks:
            tc_both = [] if cls == 'c' else tc      # a citation shows once, in English, in the combined view
            fs = size * FS
            for v, ls in (('en', en), ('tc', tc), ('both', en + tc_both)):
                g = [f'<text class="{cls} s-{v}" font-size="{fs}" text-anchor="middle">']
                for i, l in enumerate(ls):
                    g.append(f'<tspan x="{x}" y="{yy + fs + i * fs * 1.3:.1f}">{esc(l)}</tspan>')
                out.append(''.join(g) + '</text>')
            yy += block_h(en, tc_both, size) + 6
        low = max(low, yy)
    return ''.join(out), low


W5 = 980


def fig5():
    m = 'a5'
    g1 = Box(60, 360, None, [("Normal case: verify the identity of the customer and any beneficial owner before or during establishing the relationship.", "一般情況：在建立業務關係之前或過程中，核實客戶及任何實益擁有人的身分。")], 'ok', "¶4.7.1 · s.3(1)(a) Sch. 2", answer=True)
    a1 = Box(440, 370, ("Exception: verify after the relationship is established", "例外情況：在建立業務關係之後才核實"),
             [("only if all three hold:", "只限以下三項同時符合："),
              ("(a) the ML/TF risk arising from the delay can be effectively managed;", "(a) 延遲核實而可能引致的風險已獲有效管理；"),
              ("(b) it is necessary not to interrupt the normal conduct of business;", "(b) 為不干擾業務正常運作而有此必要；"),
              ("(c) verification is completed as soon as reasonably practicable.", "(c) 在合理地切實可行的範圍內盡快完成核實。")],
             'may', "¶4.7.1 · s.3(2)–(3) Sch. 2", answer=True)
    t1, low1 = _track(14, ("A business relationship", "業務關係"), [g1, a1], [
        (60, [(["first contact"], ["首次接觸"], 'c-sans', 11)]),
        (430, [(["relationship established"], ["建立業務關係"], 'c-sans', 11)]),
        (810, [], Box(640, 330, ("The reasonable timeframe passes", "合理時限屆滿"),
                      [("Terminate as soon as reasonably practicable; return funds or other assets in their original form as far as possible; consider an STR.", "在合理地切實可行的情況下盡快終止業務關係；"),
                       ("", "在可行情況下將資金或其他資產以原狀退回；"), ("", "考慮提交可疑交易報告。")],
                      'must', "¶4.7.4", answer=True)),
    ], m)
    g2 = Box(60, 360, None, [("Verify the identity of the customer and any beneficial owner before or during the transaction.", "在執行交易之前或過程中，核實客戶及任何實益擁有人的身分。")], 'ok', "¶4.7.1 · s.3(1)(b), (1A) Sch. 2", answer=True)
    s2 = Box(440, 370, ("No exception", "沒有例外"), [("Verification cannot wait until after an occasional transaction: the delayed-verification exception covers business relationships only.", "非經常交易不可在交易後才核實：延後核實的例外只適用於業務關係。")], 'stop', "s.3(1)(b), (1A), (2) Sch. 2", answer=True)
    t2, low2 = _track(low1 + 24, ("An occasional transaction", "非經常交易"), [g2, s2], [
        (60, [(["first contact"], ["首次接觸"], 'c-sans', 11)]),
        (430, [(["transaction carried out"], ["執行交易"], 'c-sans', 11)]),
    ], m)
    aria = ("Two timelines. For a business relationship, verification normally happens before or during establishment; exceptionally afterwards on three conditions within a reasonable timeframe, after which the MSO terminates, returns funds and considers an STR. For an occasional transaction there is no exception: verify before or during the transaction.",
            "兩條時間線。業務關係：一般在建立之前或過程中核實；例外情況下可在合理時限內於其後核實，逾期則終止關係、退回資金並考慮提交可疑交易報告。非經常交易：沒有例外，須在交易之前或過程中核實。")
    return svg(W5, low2 + 10, t1 + t2, aria, m, 860)
