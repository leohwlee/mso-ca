# Figures for the Guideline Chapter 3 page: the shape of the AML/CFT Systems, the
# three conditions for simplifying them, the lines between senior management and
# the officers, the MLRO's review of an internal disclosure, and the group-wide rule.
from ui import *
from bl_core import tw, need_h, lay, LH, CS


def mlabels(x, y, en_lines, tc_lines, anchor='middle'):
    """Edge label of several lines; y is the baseline of the last line. 'both' stacks English over
    Chinese, with a wider step before the Chinese so its halo clears the English descenders. The halo
    is painted as a separate stroke-only copy under the fills, so no line's halo can cover another line."""
    out = []
    for v, ls in (('en', en_lines), ('tc', tc_lines), ('both', list(en_lines) + list(tc_lines))):
        steps = [14.5] * (len(ls) - 1)
        if v == 'both' and en_lines and tc_lines:
            steps[len(en_lines) - 1] = 17
        ys, yy = [], y
        for i in range(len(ls) - 1, -1, -1):
            ys.insert(0, yy)
            if i:
                yy -= steps[i - 1]
        for paint in ('fill:none', 'stroke:none'):
            g = [f'<text class="lbl s-{v}" text-anchor="{anchor}" style="{paint}">']
            for l, ly in zip(ls, ys):
                g.append(f'<tspan x="{x}" y="{ly:.1f}">{esc(l)}</tspan>')
            g.append('</text>')
            out.append(''.join(g))
    return ''.join(out)


def mlabel(x, y, en, tc, anchor='middle'):
    """One-line edge label (replaces ui.mlabel for this page): the same stack and halo rules as mlabels."""
    return mlabels(x, y, [en], [tc], anchor)


def _fits(lines, inner, size):
    for l in lines:
        assert tw(l, size) <= inner + 0.5, (l, tw(l, size), inner)


def set_tc(n, lines, title=None):
    """Hand-set the Chinese line breaks of a Node or Card so no term is split across lines.
    For a Card, `title` gives the title lines and `lines` the body lines."""
    if isinstance(n, Card):
        tsize = n.seg['tc'][0][2]
        tcls = n.seg['tc'][0][1]
        bl = [s for s in n.seg['tc'] if s[2] == n.size]
        bcls = bl[0][1] if bl else ('t-inv' if n.kind == 'stop' else 't')
        tl = title if title is not None else [t for t, c, z in n.seg['tc'] if z != n.size]
        _fits(tl, n.w - 24, tsize)
        _fits(lines, n.w - 24, n.size)
        n.seg['tc'] = [(l, tcls, tsize) for l in tl] + [(l, bcls, n.size) for l in lines]
        n.seg['both'] = n.seg['en'] + n.seg['tc']
        n.h = sum(z * LH for _, _, z in n.seg[lay()]) + 16 + (CS * LH if n.cite else 0)
    else:
        _fits(lines, n.w - (22 if n.shape == 'rect' else 56), n.size)
        n.v['tc'] = list(lines)
        n.v['both'] = n.v['en'] + n.v['tc']
        n.h = need_h(n.v, n.size, n.cite) + (6 if n.shape == 'hex' else 0)


def set_en_title(c, tl):
    """Hand-set the English title lines of a Card."""
    tsize, tcls = c.seg['en'][0][2], c.seg['en'][0][1]
    rest = [s for s in c.seg['en'] if not (s[2] == tsize and s[1] == tcls)]
    _fits(tl, c.w - 34, tsize)
    c.seg['en'] = [(l, tcls, tsize) for l in tl] + rest
    c.seg['both'] = c.seg['en'] + c.seg['tc']
    c.h = sum(z * LH for _, _, z in c.seg[lay()]) + 16 + (CS * LH if c.cite else 0)


def dash(pts):
    d = ' '.join(f'{x:.0f},{y:.0f}' for x, y in pts)
    return f'<polyline class="e e-dash" points="{d}"/>'


# ---------------------------------------------------------------- 1. the four parts
def fig_build():
    W = 1000
    A = Card(40, 920, ("The legal floor: all reasonable measures", "法定底線：採取一切合理措施"),
             ("Proper safeguards to mitigate ML/TF risks and to prevent any breach of Part 2 or 3 of Schedule 2, met by internal AML/CFT Systems built on the risk-based approach",
              "確保設有合適的保障措施，以減低洗錢／恐怖分子資金籌集風險，並防止違反附表2第2或3部的任何規定；方法是按風險為本的方法執行內部打擊洗錢／恐怖分子資金籌集制度"),
             'must', "s.23 Sch. 2 · ¶3.1")
    Bx = Card(40, 920, ("Senior management approves the systems; you monitor them and enhance them if necessary", "制度經高級管理層審批；你須監察其推行情況，並視乎需要優化"),
              ("Enhanced measures where higher risks are identified; sized to your business. See the table below",
               "識別出較高風險時採取更嚴格的措施；按業務規模釐定。見下表"),
              'must', "¶3.2, 3.4")
    xs = [40, 272, 504, 736]
    C = [Card(xs[0], 222, ("(a) Compliance management arrangements", "(a) 合規管理安排"),
              ("At the least: senior management oversight, a CO and an MLRO", "最低限度：高級管理層監督，以及合規主任和洗錢報告主任"), 'plain', "¶3.4(a), 3.5", href="#oversight"),
         Card(xs[1], 222, ("(b) An independent audit function", "(b) 獨立的審核職能"),
              ("A direct line to senior management; regular reviews", "與高級管理層直接溝通；定期覆核"), 'plain', "¶3.4(b), 3.11", href="#audit"),
         Card(xs[2], 222, ("(c) Employee screening procedures", "(c) 僱員甄選程序"),
              ("High standards when hiring", "聘用僱員時採用崇高標準"), 'plain', "¶3.4(c), 3.14", href="#audit"),
         Card(xs[3], 222, ("(d) An ongoing employee training programme", "(d) 持續的僱員培訓計劃"),
              ("The detail is in Chapter 9", "詳情見第9章"), 'plain', "¶3.4(d) · Ch. 9")]
    # The bold title of (a) is wider than wrap() estimates; break it by hand so it clears the borders.
    set_en_title(C[0], ["(a) Compliance", "management", "arrangements"])
    set_tc(C[1], ["與高級管理層直接溝通；", "定期覆核"])
    mh = max(c.h for c in C)
    for c in C:
        c.h = mh
    H = place([([A], 34), ([Bx], 86), (C, 0)], y0=14)
    m = 'g3b'
    b = [n.render() for n in [A, Bx] + C]
    b.append(edge([A.bottom, Bx.top], mid=m))
    jy = Bx.y + Bx.h + 50
    b.append(edge([Bx.bottom, (Bx.cx, jy)], marker=False, mid=m))
    b.append(f'<line class="e" x1="{C[0].cx:.0f}" y1="{jy:.0f}" x2="{C[3].cx:.0f}" y2="{jy:.0f}"/>')
    for c in C:
        b.append(edge([(c.cx, jy), c.top], mid=m))
    b.append(mlabel(Bx.cx + 10, Bx.y + Bx.h + 38, "should include all four", "其中應包括四項", 'start'))
    aria = ("The shape of the AML/CFT Systems. At the top is the statutory duty to take all reasonable measures to ensure proper safeguards exist to mitigate ML/TF risks and prevent breaches of Parts 2 and 3 of Schedule 2, met by internal systems built on the risk-based approach. Below it, senior management approves the systems, which are monitored and enhanced if necessary, with enhanced measures for higher risks, and sized to the business. The systems should include four parts: compliance management arrangements, meaning at least senior management oversight and a compliance officer and an MLRO; an independent audit function; employee screening procedures; and an ongoing employee training programme, detailed in Chapter 9.",
            "打擊洗錢／恐怖分子資金籌集制度的結構。頂部是法定責任：採取一切合理措施，確保設有合適的保障措施以減低風險及防止違反附表2第2或3部，方法是按風險為本的方法執行內部制度。其下是高級管理層審批制度，並須監察及視乎需要優化，在識別出較高風險時採取更嚴格的措施，並按業務規模釐定。制度應包括四個部分：合規管理安排（最低限度包括高級管理層監督，以及委任合規主任和洗錢報告主任）；獨立的審核職能；僱員甄選程序；以及持續的僱員培訓計劃（詳見第9章）。")
    return svg(W, H + 14, ''.join(b), aria, m, 860)


BUILD_KEY = legend([('must', ("a duty on you: the statute's, then the Guideline's", "你的責任：先是條例的，再是指引的")),
                    ('', ("the four parts the systems should include (select (a) to (c) to jump to them)", "制度應包括的四個部分（可點選(a)至(c)跳往相關部分）"))])


# ---------------------------------------------------------------- 2. simplifying
def fig_simplify():
    W = 1000
    Q = [Node(40, 580, ("Is there any suspicion of ML/TF?", "是否懷疑有洗錢／恐怖分子資金籌集的情況？"), "¶3.3", shape='hex'),
         Node(40, 580, ("(a) Do you still comply with Schedule 2, the institutional risk assessment steps and the three duties in paragraph 3.2?",
                        "(a) 你是否仍符合附表2的法定規定、機構層面風險評估的步驟，以及第3.2段的三項責任？"), "¶3.3(a) · ¶2.2–2.3, 3.2", shape='hex'),
         Node(40, 580, ("(b) Was the lower risk identified through an appropriate risk assessment, such as the institutional ML/TF risk assessment?",
                        "(b) 較低風險是否基於適當的風險評估（例如機構層面的洗錢／恐怖分子資金籌集風險評估）而識別出來？"), "¶3.3(b)", shape='hex'),
         Node(40, 580, ("(c) Are the simplified systems approved by senior management and reviewed from time to time?",
                        "(c) 簡化制度是否經高級管理層審批，並不時覆核？"), "¶3.3(c)", shape='hex')]
    OK = Card(40, 580, ("You may simplify the nature, scale and complexity of your systems", "可簡化制度的性質、規模及複雜程度"),
              None, 'ok', "¶3.3", answer=True)
    ST = Card(720, 240, ("The systems may not be simplified", "不得簡化制度"),
              ("Any suspicion, or any one condition not met, is enough", "只要懷疑有洗錢／恐怖分子資金籌集，或任何一項條件未符合，即不得簡化"),
              'stop', "¶3.3", answer=True)
    set_tc(ST, ["只要懷疑有洗錢／", "恐怖分子資金籌集，", "或任何一項條件未符合，", "即不得簡化"])
    set_tc(Q[2], ["(b) 較低風險是否基於適當的風險評估（例如機構層面的", "洗錢／恐怖分子資金籌集風險評估）而識別出來？"])
    H = place([([Q[0]], 52), ([Q[1]], 52), ([Q[2]], 52), ([Q[3]], 52), ([OK], 0)], y0=14)
    # The black box keeps its content height, centred on the question column; the four
    # side exits run into one collector line that enters it once.
    top, bot = Q[0].y, Q[3].y + Q[3].h
    ST.y = (top + bot) / 2 - ST.h / 2
    xc = 680
    m = 'g3s'
    b = [n.render() for n in Q + [OK, ST]]
    for i in range(4):
        q = Q[i]
        nxt = Q[i + 1] if i < 3 else OK
        b.append(edge([q.bottom, nxt.top], mid=m))
        down = ("no", "否") if i == 0 else ("yes", "是")
        b.append(mlabel(q.cx + 10, q.y + q.h + 34, down[0], down[1], 'start'))
        side = ("yes", "是") if i == 0 else ("no", "否")
        b.append(edge([q.right, (xc, q.cy)], marker=False, mid=m))
        b.append(mlabel((q.x + q.w + xc) / 2, q.cy - 8, side[0], side[1]))
    b.append(f'<line class="e" x1="{xc}" y1="{Q[0].cy:.0f}" x2="{xc}" y2="{Q[3].cy:.0f}"/>')
    b.append(edge([(xc, ST.cy), ST.left], mid=m))
    aria = ("When the AML/CFT Systems may be simplified. First, if there is any suspicion of ML/TF, the systems may not be simplified. Otherwise three conditions must all be met: the MSO still complies with Schedule 2 and with paragraphs 2.2, 2.3 and 3.2; the lower risk was identified through an appropriate risk assessment such as the institutional ML/TF risk assessment; and the simplified systems are approved by senior management and reviewed from time to time. If all are met, the nature, scale and complexity of the systems may be simplified; if any fails, they may not.",
            "何時可簡化打擊洗錢／恐怖分子資金籌集制度。首先，如懷疑有洗錢／恐怖分子資金籌集的情況，即不得簡化。否則須同時符合三項條件：金錢服務經營者仍符合附表2及第2.2、2.3及3.2段的規定；較低風險是基於適當的風險評估（例如機構層面的風險評估）識別出來；以及簡化制度經高級管理層審批並不時覆核。三項均符合，即可簡化制度的性質、規模及複雜程度；任何一項不符合，即不得簡化。")
    return svg(W, H + 14, ''.join(b), aria, m, 860)


SIMPLIFY_KEY = legend([('hex', ("a question you must answer", "你須回答的問題")), ('ok', ("you may simplify", "可以簡化")),
                       ('stop', ("no simplification", "不得簡化"))])


# ---------------------------------------------------------------- 3. lines of oversight
def fig_lines():
    W = 1000
    SM = Card(40, 920, ("The board or its delegated committee (where applicable), and senior management", "董事會或獲其授權的委員會（如適用）及高級管理層"),
              ("Understand the ML/TF risks and ensure they are adequately managed. Senior management is responsible for implementing effective AML/CFT Systems. Management information should reach them in a timely, complete, understandable and accurate manner",
               "清楚了解洗錢／恐怖分子資金籌集風險，並確保已妥善管理。高級管理層有責任推行有效的制度。管理資料應以合時、完整、易於理解及準確的方式通知高級管理層"),
              'must', "¶3.6–3.7")
    CO = Card(40, 280, ("Compliance officer (CO)", "合規主任"),
              ("At the management level. Overall responsibility for establishing and maintaining the systems", "屬管理層。全面負責建立及維持制度"),
              'plain', "¶3.7, 3.8(e), 3.9", href="#roles")
    ML = Card(360, 280, ("MLRO", "洗錢報告主任"),
              ("A senior staff member. The central reference point for suspicious transaction reporting", "一名高級職員。報告可疑交易的中央聯絡點"),
              'plain', "¶3.7, 3.8(e), 3.10", href="#roles")
    set_tc(ML, ["一名高級職員。", "報告可疑交易的中央聯絡點"])
    AU = Card(680, 280, ("Independent audit function", "獨立的審核職能"),
              ("Enough expertise and resources to review the systems independently", "具備充足的專門知識及資源，對制度作出獨立覆核"),
              'plain', "¶3.11", href="#audit")
    set_tc(AU, ["具備充足的專門知識及資源，", "對制度作出獨立覆核"])
    JF = Card(360, 280, ("JFIU and law enforcement agencies", "財富情報組及執法機構"), None, 'faint', "¶3.10")
    mh = max(CO.h, ML.h, AU.h)
    for c in (CO, ML, AU):
        c.h = mh
    H = place([([SM], 112), ([CO, ML, AU], 76), ([JF], 0)], y0=14)
    m = 'g3l'
    b = [n.render() for n in (SM, CO, ML, AU, JF)]
    y1, y2 = SM.y + SM.h, CO.y
    for c in (CO, ML):
        xd, xu = c.cx - 50, c.cx + 50
        b.append(edge([(xd, y1), (xd, y2)], mid=m))
        b.append(mlabel(xd - 8, y1 + 34, "appoints", "委任", 'end'))
        b.append(edge([(xu, y2), (xu, y1)], mid=m))
        b.append(mlabels(xu + 8, y1 + 94, ["regular contact;", "direct access", "when required"], ["定期聯絡；", "有需要時直接聯絡"], 'start'))
    b.append(edge([(AU.cx, y2), (AU.cx, y1)], mid=m))
    b.append(mlabels(AU.cx + 8, y1 + 60, ["direct line of", "communication"], ["直接溝通"], 'start'))
    b.append(edge([ML.bottom, JF.top], mid=m, mstart=True))
    b.append(mlabel(ML.cx + 10, ML.y + ML.h + 46, "main point of contact", "主要聯絡點", 'start'))
    aria = ("Who answers to whom. At the top, the board or its delegated committee where applicable, and senior management, understand the ML/TF risks and ensure they are managed; senior management is responsible for effective systems, and management information should reach them in a timely, complete, understandable and accurate manner. Senior management appoints the compliance officer, at the management level, with overall responsibility for establishing and maintaining the systems, and the MLRO, a senior staff member who is the central reference point for suspicious transaction reporting. Both have regular contact with senior management and direct access when required. The independent audit function has a direct line of communication to senior management. The MLRO is the main point of contact with the JFIU and law enforcement agencies.",
            "誰向誰負責。頂部是董事會或獲其授權的委員會（如適用）及高級管理層：他們須清楚了解洗錢／恐怖分子資金籌集風險並確保妥善管理；高級管理層有責任推行有效的制度，而管理資料應以合時、完整、易於理解及準確的方式通知高級管理層。高級管理層委任屬管理層的合規主任，全面負責建立及維持制度；並委任一名高級職員擔任洗錢報告主任，作為報告可疑交易的中央聯絡點。兩者均與高級管理層保持定期聯絡，並在有需要時直接聯絡。獨立的審核職能能與高級管理層直接溝通。洗錢報告主任是與財富情報組及執法機構的主要聯絡點。")
    return svg(W, H + 14, ''.join(b), aria, m, 860)


LINES_KEY = legend([('must', ("carries responsibility for the systems", "承擔制度責任")),
                    ('', ("appointed or set up by the MSO (select one to jump to it)", "由金錢服務經營者委任或設立（可點選跳往相關部分）")),
                    ('faint', ("outside the MSO", "金錢服務經營者以外"))])


# ---------------------------------------------------------------- 4. the MLRO's review
def fig_mlro():
    W = 1000
    S1 = Card(40, 580, ("An internal disclosure or an exception report comes in", "收到內部披露或例外情況報告"), None, 'plain', "¶3.10(a)")
    S2 = Card(40, 580, ("It is reviewed under the MLRO's oversight, in light of all available relevant information", "在洗錢報告主任監督下，根據一切知悉的資料作出覆核"),
              None, 'plain', "¶3.10(a)")
    D = Node(40, 580, ("Is it necessary to make a report to the JFIU?", "是否有需要向財富情報組作出報告？"), "¶3.10(a)", shape='hex')
    Y = Card(40, 270, ("Report to the JFIU", "向財富情報組作出報告"), ("How and when: Chapter 7", "方式及時間：見第7章"), 'must', "¶3.10(a) · Ch. 7", answer=True)
    N = Card(350, 270, ("No report", "不作報告"), ("The decision is still recorded", "有關決定仍須記錄"), 'plain', "¶3.10(a)–(b)", answer=True)
    R = Card(40, 580, ("Keep all records of the internal review", "備存該等內部覆核的所有紀錄"), None, 'must', "¶3.10(b)")
    T = Card(680, 280, ("Guidance on how to avoid tipping off", "如何避免「通風報訊」的導引"),
             ("The third item under the MLRO's oversight. It is not a step in the sequence", "洗錢報告主任監督的第三項職能，並非流程中的一個步驟"), 'must', "¶3.10(c)")
    mh = max(Y.h, N.h)
    Y.h = N.h = mh
    H = place([([S1], 40), ([S2], 40), ([D], 70), ([Y, N], 44), ([R], 0)], y0=14)
    T.y = S2.y
    T.h = D.y + D.h - S2.y
    m = 'g3m'
    b = [n.render() for n in (S1, S2, D, Y, N, R, T)]
    b.append(edge([S1.bottom, S2.top], mid=m))
    b.append(edge([S2.bottom, D.top], mid=m))
    jy = D.y + D.h + 26
    b.append(edge([D.bottom, (D.cx, jy), (Y.cx, jy), Y.top], mid=m))
    b.append(edge([(D.cx, jy), (N.cx, jy), N.top], mid=m))
    b.append(mlabel(Y.cx - 10, jy + 36, "yes", "是", 'end'))
    b.append(mlabel(N.cx + 10, jy + 36, "no", "否", 'start'))
    b.append(edge([Y.bottom, (Y.cx, R.y)], mid=m))
    b.append(edge([N.bottom, (N.cx, R.y)], mid=m))
    aria = ("The MLRO's review of an internal report. An internal disclosure or an exception report comes in; it is reviewed under the MLRO's oversight in light of all available relevant information; the MLRO determines whether it is necessary to report to the JFIU. Yes leads to a report, done as Chapter 7 describes; no leads to no report. Either way all records of the internal review are kept. Separately, the third item the MLRO oversees is guidance on how to avoid tipping off.",
            "洗錢報告主任覆核內部報告的流程。收到內部披露或例外情況報告後，在洗錢報告主任監督下根據一切知悉的資料作出覆核，並決定是否有需要向財富情報組作出報告。需要的話便作出報告（方式見第7章）；不需要則不作報告。不論結果，均須備存內部覆核的所有紀錄。另外，洗錢報告主任監督的第三項職能是提供有關如何避免通風報訊的導引。")
    return svg(W, H + 14, ''.join(b), aria, m, 860)


MLRO_KEY = legend([('', ("a step", "步驟")), ('hex', ("the MLRO's decision", "洗錢報告主任的決定")),
                   ('must', ("a duty the MLRO oversees", "洗錢報告主任監督的責任"))])


# ---------------------------------------------------------------- 5. the group
def fig_group():
    W = 1000
    S = Card(40, 580, ("You are a Hong Kong-incorporated MSO with overseas branches, or subsidiary undertakings in the same business as a financial institution",
                       "你是在香港成立為法團的金錢服務經營者，設有外地分行，或經營與金融機構相同業務的附屬企業"), None, 'plain', "¶3.15")
    G = Card(40, 580, ("Run group-wide AML/CFT Systems", "推行集團層面的打擊洗錢／恐怖分子資金籌集制度"),
             ("The Guideline's requirements, including the four parts in paragraph 3.4, wherever relevant and applicable. In particular, CDD and record-keeping procedures similar to Schedule 2 Parts 2 and 3, as far as local law permits",
              "在相關及適用時執行本指引的規定，包括第3.4段的四個部分；尤其須設有程序，在當地法律准許的範圍內遵守與附表2第2及3部相類似的盡職審查及備存紀錄規定"),
             'must', "¶3.15–3.16 · fn 10 · s.22(1) Sch. 2")
    SH = Card(680, 280, ("Alongside: share information within the group", "同時：在集團內共用資料"),
              ("As far as the laws allow, with safeguards on confidentiality and use, including against tipping off", "在法律准許的範圍內，並妥善保障資料的保密及用途（包括防止通風報訊）"),
              'must', "¶3.17")
    Q = Node(40, 580, ("Do the host jurisdiction's AML/CFT requirements differ from the requirements in paragraph 3.15?",
                       "所在的司法管轄區對打擊洗錢／恐怖分子資金籌集的規定，是否與第3.15段所述的規定有所不同？"), "¶3.18", shape='hex')
    NF = Card(680, 280, ("No further step", "無須再採取步驟"), ("The group-wide systems apply", "上述集團層面的制度照常適用"), 'plain', "¶3.15")
    D = Node(40, 580, ("Does host law permit the branch or subsidiary to apply the higher requirements, particularly CDD and record keeping?",
                       "所在的司法管轄區的法律是否准許分行或附屬企業執行較嚴格的規定，尤其是盡職審查及備存紀錄規定？"), "¶3.18–3.19", shape='hex')
    OK = Card(40, 250, ("Require it to apply the higher of the two sets", "規定其執行兩者中較嚴格的規定"), None, 'ok', "¶3.18", answer=True)
    NO = Card(320, 300, ("Inform the CCE, and take additional measures", "通知關長，並採取額外措施"),
              ("To mitigate the ML/TF risks the branch or subsidiary faces because it cannot comply", "以有效減低分行或附屬企業因不能遵從規定而面對的洗錢／恐怖分子資金籌集風險"),
              'must', "¶3.19 · s.22(2) Sch. 2", answer=True)
    set_tc(S, [], title=["你是在香港成立為法團的金錢服務經營者，設有外地分行，", "或經營與金融機構相同業務的附屬企業"])
    set_tc(Q, ["所在的司法管轄區對打擊洗錢／恐怖分子資金籌集的規定，", "是否與第3.15段所述的規定有所不同？"])
    set_tc(G, ["在相關及適用時執行本指引的規定，包括第3.4段的四個部分；", "尤其須設有程序，在當地法律准許的範圍內遵守",
               "與附表2第2及3部相類似的盡職審查及備存紀錄規定"])
    set_tc(SH, ["在法律准許的範圍內，", "並妥善保障資料的保密及用途", "（包括防止通風報訊）"])
    OK.h = NO.h = max(OK.h, NO.h)
    H = place([([S], 40), ([G, SH], 40), ([Q, NF], 56), ([D], 70), ([OK, NO], 0)], y0=14)
    m = 'g3g'
    b = [n.render() for n in (S, G, SH, Q, NF, D, OK, NO)]
    for a, c in ((S, G), (G, Q), (Q, D)):
        b.append(edge([a.bottom, c.top], mid=m))
    b.append(mlabel(Q.cx + 10, Q.y + Q.h + 34, "yes", "是", 'start'))
    b.append(dash([(G.x + G.w, G.cy), (SH.x, G.cy)]))
    b.append(edge([Q.right, (NF.x, Q.cy)], mid=m))
    b.append(mlabel((Q.x + Q.w + NF.x) / 2, Q.cy - 8, "no", "否"))
    jy = D.y + D.h + 26
    b.append(edge([D.bottom, (D.cx, jy), (OK.cx, jy), OK.top], mid=m))
    b.append(edge([(D.cx, jy), (NO.cx, jy), NO.top], mid=m))
    b.append(mlabel(OK.cx - 10, jy + 36, "yes", "是", 'end'))
    b.append(mlabel(NO.cx + 10, jy + 36, "no", "否", 'start'))
    aria = ("The group-wide rule. A Hong Kong-incorporated MSO with overseas branches or subsidiary undertakings in the same business as a financial institution runs group-wide AML/CFT Systems applying the Guideline's requirements, including the four parts in paragraph 3.4, wherever relevant and applicable, and in particular CDD and record-keeping procedures similar to Schedule 2 Parts 2 and 3 as far as local law permits. Alongside, it shares information within the group as far as the laws allow, with safeguards including against tipping off. First question: do the host jurisdiction's requirements differ? If not, the group-wide systems apply and there is no further step. If they do, second question: does host law permit the higher requirements, particularly CDD and record keeping? If yes, the MSO requires the branch or subsidiary to apply the higher of the two sets. If no, the MSO informs the CCE and takes additional measures to mitigate the risks.",
            "集團層面的規則。在香港成立為法團的金錢服務經營者如設有外地分行或經營與金融機構相同業務的附屬企業，須推行集團層面的制度，在相關及適用時執行本指引的規定（包括第3.4段的四個部分），尤其須在當地法律准許的範圍內遵守與附表2第2及3部相類似的盡職審查及備存紀錄規定。同時在法律准許的範圍內於集團內共用資料，並設有保障措施，包括防止通風報訊。第一個問題：所在的司法管轄區的規定是否有所不同？如沒有不同，集團層面的制度照常適用，無須再採取步驟。如有不同，第二個問題：當地法律是否准許執行較嚴格的規定（尤其是盡職審查及備存紀錄規定）？如准許，金錢服務經營者須規定分行或附屬企業執行兩者中較嚴格的規定；如不准許，須通知關長，並採取額外措施減低風險。")
    return svg(W, H + 14, ''.join(b), aria, m, 860)


GROUP_KEY = legend([('', ("the starting point, or no further step", "起點，或無須再採取步驟")), ('must', ("a duty on you", "你的責任")),
                    ('hex', ("a question", "問題")), ('ok', ("host law allows the higher set", "當地法律准許較嚴格的規定"))])

