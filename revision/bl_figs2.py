# The PEP and intermediary figures of the Schedule 2 page.
from bl_core import *
from bl_core import need_h
from ui import Card
from bl_figs import lines_down, stack_down


def paras(node, en, tc):
    """Re-wrap a Node's text so each phrase in en / tc starts a new line (no split words)."""
    inner = node.w - 22 if node.shape == 'rect' else node.w - 56
    le = [l for p in en for l in wrap(p, inner, node.size)]
    # CJK glyphs render wider than wrap() estimates: keep Chinese clear of the border
    lt = [l for p in tc for l in wrap(p, inner - (12 if node.shape == 'rect' else 0), node.size)]
    node.v = {'en': le, 'tc': lt, 'both': le + lt}
    node.h = need_h(node.v, node.size, node.cite) + (6 if node.shape == 'hex' else 0)
    return node


def N(x, w, en, tc, cite=None, kind='plain', shape='rect', answer=False):
    n = Node(x, w, (' '.join(en), ''.join(tc)), cite, kind, shape=shape, answer=answer)
    return paras(n, en, tc)


def ml(x, y, en, tc, anchor='start', lh=17):
    """Edge label of one or more lines; the combined view stacks English over Chinese.
    y is the baseline of the first line."""
    out = []
    for v, ls in (('en', en), ('tc', tc), ('both', en + tc)):
        g = [f'<text class="lbl s-{v}" text-anchor="{anchor}">']
        for i, l in enumerate(ls):
            g.append(f'<tspan x="{x}" y="{y + i * lh:.1f}">{esc(l)}</tspan>')
        g.append('</text>')
        out.append(''.join(g))
    return ''.join(out)


def nlines(en, tc):
    return {'en': len(en), 'tc': len(tc), 'both': len(en) + len(tc)}[lay()]


def top_row(nodes, y):
    for n in nodes:
        n.y = y
    return max(n.y + n.h for n in nodes)


# ---------------------------------------------------------------- Figure 4: PEPs
def fig4():
    W = 1000
    m = 'a4'
    D1 = N(260, 480, ["Is the customer, or any beneficial owner", "of the customer, a politically exposed person?"],
           ["客戶或客戶的任何實益擁有人是否政治人物？"], "¶4.9.9, 4.9.16 · s.19(1) Sch. 2", shape='hex')
    N0 = N(20, 260, ["No. Assess risk as usual,", "and keep screening:", "PEP status can appear later."],
           ["否。照常評估風險，並持續篩查：", "政治人物身分可能其後才出現。"], "¶4.9.10, 4.9.17(c)", answer=True)
    D2 = N(360, 280, ["Which kind of PEP?"], ["屬哪一類政治人物？"], "¶4.9.7, 4.9.13, 4.9.14", shape='hex')
    F = N(35, 300, ["Non-Hong Kong PEP,", "including family members", "and close associates"],
          ["非香港政治人物，", "包括其家庭成員及關係密切的人"], "¶4.9.7–4.9.8 · s.1 Sch. 2")
    Hn = N(370, 260, ["Hong Kong PEP, or", "international", "organisation PEP"], ["香港政治人物或", "國際組織政治人物"], "¶4.9.13–4.9.15")
    R = N(665, 300, ["Former PEP of any kind"], ["任何類別的前政治人物"], "¶4.9.11, 4.9.18")
    D3 = N(390, 220, ["Is the relationship", "high risk?"], ["業務關係是否屬高風險？"], "¶4.9.17 · fn 40", shape='hex')
    EDD = N(15, 340, ["Before establishing or continuing", "the relationship, apply all", "three EDD measures:",
                      "(a) senior management approval;", "(b) reasonable measures to establish source of wealth and source of funds;",
                      "(c) enhanced ongoing monitoring."],
            ["在建立或維持業務關係之前，", "執行全部三項更嚴格的盡職審查措施：", "(a) 取得高級管理層批准；",
             "(b) 採取合理措施確立財富來源及資金來源；", "(c) 執行更嚴格的持續監察。"],
            "¶4.9.10 · s.5(3)(b), 10, 15 Sch. 2", 'must', answer=True)
    NO = N(368, 262, ["Standard CDD under the risk-based approach.", "The PEP EDD package applies only if the relationship is or becomes high risk."],
           ["按風險為本方法執行標準盡職審查。", "業務關係屬於或其後變為高風險時，", "才須執行政治人物的更嚴格措施。"],
           "¶4.9.17(a)–(c)", 'ok', answer=True)
    R2 = N(640, 350, ["Risk-based, not merely a time limit.",
                      "For a former Hong Kong or international-organisation PEP this arises only in a high-risk relationship.",
                      "EDD may be dropped only with senior management approval, based on an appropriate assessment (influence, seniority, linked functions) that the risk is no longer high.",
                      "Keep that assessment on record."],
           ["按風險評估處理，不應僅以時限決定。", "前香港或國際組織政治人物只在高風險業務關係中才涉及此情況。",
            "須經高級管理層批准，並以適當評估（影響力、職位等級、職能連繫）證明風險不再屬高，方可不採取更嚴格措施。",
            "須保存評估紀錄。"],
           "¶4.9.12, 4.9.18 · s.5(5), 10(3), 15 Sch. 2", 'may', answer=True)

    D1.y = 16
    y2 = D1.y + D1.h + 50
    top_row([N0, D2], y2)
    jy = max(D2.y + D2.h + 26, N0.y + N0.h + 22)
    y3 = jy + 34
    b3 = top_row([F, Hn, R], y3)
    D3.y = Hn.y + Hn.h + 40
    y5 = max(D3.y + D3.h + 52, F.y + F.h + 4 * 17 + 40)
    H = top_row([EDD, NO, R2], y5)

    b = [n.render() for n in (D1, N0, D2, F, Hn, R, D3, EDD, NO, R2)]
    # connectors first, labels last, so a label's halo always sits over any line
    b.append(edge([D1.left, (N0.cx, D1.cy), N0.top], mid=m))
    b.append(edge([D1.bottom, D2.top], mid=m))
    b.append(edge([D2.bottom, (D2.cx, jy), (F.cx, jy), F.top], mid=m))
    b.append(edge([D2.bottom, Hn.top], mid=m))
    b.append(edge([D2.bottom, (D2.cx, jy), (R.cx, jy), R.top], mid=m))
    b.append(edge([F.bottom, EDD.top], mid=m))
    b.append(edge([Hn.bottom, D3.top], mid=m))
    yx = 300
    b.append(edge([D3.left, (yx, D3.cy), (yx, EDD.y)], mid=m))
    b.append(edge([D3.bottom, (D3.cx, NO.y)], mid=m))
    b.append(edge([R.bottom, (R.cx, R2.y)], mid=m))
    up = (nlines(["x"], ["x"]) - 1) * 17   # stack a two-line label upward, clear of a horizontal line
    b.append(ml((D1.x + N0.cx) / 2, D1.cy - 8 - up, ["no"], ["否"], 'middle'))
    b.append(ml(D2.cx + 9, (D1.y + D1.h + D2.y) / 2 + 5 - up / 2, ["yes"], ["是"]))
    b.append(ml(F.cx - 9, F.y + F.h + 24, ["always,", "whatever the risk"], ["一律執行，", "不論風險評級"], 'end'))
    b.append(ml((D3.x + yx) / 2, D3.cy - 8 - up, ["yes"], ["是"], 'middle'))
    b.append(ml(D3.cx + 9, (D3.y + D3.h + NO.y) / 2 + 5 - up / 2, ["no"], ["否"]))
    aria = ("Decision tree for politically exposed persons: screen the customer and every beneficial owner; a non-Hong Kong PEP always gets the three EDD measures; a Hong Kong or international-organisation PEP gets them only when the relationship is high risk; a former PEP is handled on risk, not merely on a fixed time limit (for a former Hong Kong or international-organisation PEP, only within a high-risk relationship), with senior management approval and a recorded assessment.",
            "政治人物決策樹：篩查客戶及所有實益擁有人；非香港政治人物一律執行三項更嚴格措施；香港或國際組織政治人物僅在業務關係屬高風險時執行；前政治人物按風險評估處理，不應僅以時限決定（前香港或國際組織政治人物只在高風險業務關係中才涉及此情況），並須經高級管理層批准及保存評估紀錄。")
    return svg(W, H + 16, ''.join(b), aria, m, 860)


# ---------------------------------------------------------------- Figure 8: intermediary
STEPS = [
    ('in', "1 · Written confirmation that it agrees to act as your intermediary, and which CDD measures it will perform",
     "1 · 書面確認同意擔任你的中介人，並列明執行哪些盡職審查措施", "s.18(1)(a) Sch. 2 · ¶4.11.3(a)"),
    ('in', "2 · Immediately after each measure: the data and information it obtained (copies of the documents need not come at the same time)",
     "2 · 每項措施執行後，立刻取得中介人所得的數據或資料（毋須同時取得文件複本）", "s.18(4)(a) Sch. 2 · ¶4.11.4"),
    ('in', "3 · On request, without delay: a copy of any document, or a record of any data or information, it obtained",
     "3 · 應要求沒有延誤地提供所取得的任何文件的複本，或數據或資料的紀錄", "s.18(1)(b) Sch. 2 · ¶4.11.3(b)"),
    ('in', "4 · Its undertakings: keep all the underlying CDD information for the whole relationship and at least 5 years after it ends (or as the CCE specifies); hand over copies of all of it if it is about to cease trading or stops acting for you",
     "4 · 中介人的承諾：在業務關係持續期間及終止後至少5年內（或直至關長指明的時間）備存所有相關盡職審查資料；即將結業或不再代你行事時，提供全部資料的複本",
     "¶4.11.5 · s.18(4)(b) Sch. 2"),
    ('out', "5 · You sample-test from time to time that it produces CDD information on demand without undue delay; if you doubt its reliability, review its ability",
     "5 · 你不時抽樣測試中介人會否應要求盡快提供資料；如對其可靠性有懷疑，覆核其能力", "¶4.11.6–4.11.7"),
    ('in', "6 · If you end the arrangement: all the CDD information, immediately",
     "6 · 如你終止與中介人的關係：立即取得所有盡職審查資料", "¶4.11.7"),
]


def fig8():
    W = 1000
    m = 'a8'
    xi, xm = 165, 835            # the two lifelines
    lx, lw = (xi + xm) / 2, 600  # label centre and wrap width between them
    S = 11.5 * FS
    cust = Card(40, 250, ("Customer", "客戶"), ("usually already the intermediary's client", "通常已是中介人的客戶"), 'plain', "¶4.11.1")
    inter = Card(40, 250, ("Intermediary", "中介人"), ("performs part of CDD under its own procedures", "按本身程序執行部分盡職審查措施"), 'plain', "¶4.11.1")
    mso = Card(690, 290, ("The MSO (you)", "金錢服務經營者（你）"), ("keeps the ultimate responsibility for CDD being met", "承擔確保符合盡職審查規定的最終責任"), 'must', "¶4.11.1 · s.18(2) Sch. 2")
    cust.y = 16
    hy = cust.y + cust.h + 56
    hh = max(inter.h, mso.h)
    inter.h = mso.h = hh
    inter.y = mso.y = hy
    b = [cust.render(), inter.render(), mso.render()]
    labels = []
    # customer to intermediary: an existing relationship, not a data flow
    b.append(f'<line class="e" x1="{cust.cx:.0f}" y1="{cust.y + cust.h:.0f}" x2="{inter.cx:.0f}" y2="{hy:.0f}"/>')
    labels.append(ml(cust.cx + 10, cust.y + cust.h + 24, ["existing, separate relationship"], ["既有而獨立的業務關係"]))
    # customer will also become the MSO's customer
    b.append(edge([cust.right, (mso.cx, cust.cy), (mso.cx, hy)], mid=m).replace('class="e"', 'class="e e-dash"'))
    n = nlines(["x"], ["x"])
    labels.append(ml((cust.x + cust.w + mso.cx) / 2, cust.cy - 8 - (n - 1) * 17, ["will also become your customer"], ["亦將成為你的客戶"], 'middle'))

    y = hy + hh + 26
    v = lay()
    for d, en, tc, cite in STEPS:
        le, lt = wrap(en, lw, S), wrap(tc, lw, S)
        ls = {'en': le, 'tc': lt, 'both': le + lt}
        for vv in ('en', 'tc', 'both'):
            g = [f'<g class="s-{vv}"><text class="t" font-size="{S}" text-anchor="middle">']
            for i, l in enumerate(ls[vv]):
                g.append(f'<tspan x="{lx}" y="{y + S * 0.95 + i * S * LH:.1f}">{esc(l)}</tspan>')
            g.append('</text>')
            cy_ = y + len(ls[vv]) * S * LH + CS * 0.95
            g.append(f'<text class="c" font-size="{CS}" text-anchor="middle"><tspan x="{lx}" y="{cy_:.1f}">{esc(cite_txt(cite, vv))}</tspan></text></g>')
            labels.append(''.join(g))
        ay = y + len(ls[v]) * S * LH + CS * LH + 8
        pts = [(xi, ay), (xm, ay)] if d == 'in' else [(xm, ay), (xi, ay)]
        b.append(edge(pts, mid=m))
        y = ay + 22
    end = y + 4
    b.append(f'<line class="e e-dash" x1="{xi}" y1="{hy + hh:.0f}" x2="{xi}" y2="{end:.0f}"/>')
    b.append(f'<line class="e e-dash" x1="{xm}" y1="{hy + hh:.0f}" x2="{xm}" y2="{end:.0f}"/>')
    aria = ("Sequence when relying on an intermediary: the customer usually already has its own relationship with the intermediary and will also become the MSO's customer. The intermediary gives written confirmation, then the data immediately after each measure, copies on request without delay, and undertakings to keep records at least five years after the relationship ends and to hand them over if it stops acting. The MSO sample-tests the arrangement, obtains everything immediately if it ends the arrangement, and remains ultimately responsible.",
            "依賴中介人的次序：客戶通常已與中介人有本身的業務關係，並將成為金錢服務經營者的客戶。中介人提供書面確認、每項措施後立刻提供數據、應要求沒有延誤地提供複本，並承諾在業務關係終止後備存紀錄至少5年及在不再代行時交出全部資料。金錢服務經營者不時抽樣測試，終止安排時立即取得全部資料，並承擔最終責任。")
    return svg(W, end + 12, ''.join(b + labels), aria, m, 860)
