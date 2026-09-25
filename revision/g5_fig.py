# Figures for the Guideline Chapter 5 page: what the monitoring system should do and
# the two checks on it, and the route from an unusual transaction to a decision.
from ui import *
from ci_fig import TB


def cc(*cs):
    """Join several citations into one (en, tc) pair."""
    pairs = [cite_pair(c) for c in cs]
    return (' · '.join(p[0] for p in pairs), ' · '.join(p[1] for p in pairs))


def FAQ(q):
    return (f"FAQ Q{q}", f"常見問題第{q}問")


def lab(x, y, en, tc, anchor='middle'):
    """Edge or frame label. In the combined view English sits over Chinese, spaced so
    that English descenders stay clear of the Chinese line; y is the last line's baseline."""
    out = []
    for v, ls in (('en', [en]), ('tc', [tc]), ('both', [en, tc])):
        n = len(ls)
        g = [f'<text class="lbl s-{v}" text-anchor="{anchor}">']
        for i, l in enumerate(ls):
            g.append(f'<tspan x="{x}" y="{y - (n - 1 - i) * 18:.1f}">{esc(l)}</tspan>')
        g.append('</text>')
        out.append(''.join(g))
    return ''.join(out)


def frame(x, y, w, h):
    return f'<rect class="n n-faint" x="{x}" y="{y:.1f}" width="{w}" height="{h:.1f}" rx="8"/>'


# ---------------------------------------------------------------- 1. the monitoring system
def fig_system():
    W = 1000
    both = lay() == 'both'
    band = 52 if both else 34            # room for a frame's own title above its cards
    CW, X = 226, (24, 268, 512, 756)
    D1 = Card(X[0], CW, ("Fit it to your business", "按你的業務設計系統"),
              ("Its design, degree of automation and sophistication should be developed having regard to five factors about your own business: left column of the table below",
               "系統的設計、自動化程度及精密程度應適當地因應五項關於你本身業務的因素開發：見下表左欄"), 'must', "¶5.4")
    D2 = Card(X[1], CW, ("Set the parameters and thresholds", "設定參數及門檻"),
              ("Taking into account the transaction characteristics: right column of the table below",
               "顧及交易的特徵：見下表右欄"), 'must', "¶5.7")
    R2 = Card(X[2], CW, ("Give staff timely, sufficient information", "適時向職員提供充分資料"),
              ("Everyone who monitors or investigates gets what is needed to identify, analyse and effectively monitor customers' transactions",
               "所有負責交易監察及調查的相關職員，均獲得足以識別、分析及有效監察客戶交易的資料"), 'must', "¶5.5")
    R1 = Card(X[3], CW, ("Watch the whole relationship", "監察整段業務關係"),
              ("Preferably relationship-based, not transaction by transaction: a customer's several accounts and related customers' accounts, within or across lines of business",
               "應盡可能以關係為本，而非以個別交易為本：客戶在業務範圍內或跨業務的多個戶口，以及相關客戶的戶口"), 'must', "¶5.6")
    V = Card(170, 380, ("Document the parameters and thresholds, and have them independently validated", "把參數及門檻記錄在案，並經獨立驗證"),
             ("So that they are appropriate to your operations and context",
              "以確保其有效運作及符合實際情況"), 'must', "¶5.8")
    RV = Card(590, 380, ("Review the system regularly", "定期覆核系統"),
              ("Are the systems and processes, parameters and thresholds included, still adequate and effective?",
               "交易監察系統及程序（包括採用的參數及門檻）是否仍然合適及有效？"), 'must', "¶5.8")
    top_y = 12
    GAP = 70                              # between the two frames, where the arrow labels sit
    place([([D1, D2, R2, R1], 0)], y0=top_y + band)
    h = max(n.h for n in (D1, D2, R2, R1))
    for n in (D1, D2, R2, R1):
        n.h, n.y = h, top_y + band
    top_h = band + h + 26                  # room under the cards for the bracket
    bot_y = top_y + top_h + GAP
    place([([V, RV], 0)], y0=bot_y + band)
    h2 = max(n.h for n in (V, RV))
    for n in (V, RV):
        n.h, n.y = h2, bot_y + band
    bot_h = band + h2 + 14
    H = bot_y + bot_h
    b = [frame(10, top_y, 980, top_h), frame(10, bot_y, 980, bot_h)]
    b.append(lab(24, top_y + (40 if both else 23), "What the system should do", "系統應能做到的事", anchor='start'))
    b.append(lab(24, bot_y + (40 if both else 23), "The checks on the system itself", "對系統本身的查核", anchor='start'))
    b += [n.render() for n in (D1, D2, R2, R1, V, RV)]
    m = 'g5s'
    # validation is of the parameters and thresholds; the review covers the whole system
    b.append(edge([(D2.cx, V.y), (D2.cx, D2.y + D2.h)], mid=m))
    ly = top_y + top_h + GAP / 2 + 6
    b.append(lab(D2.cx - 12, ly + (9 if both else 0), "the parameters and thresholds", "參數及門檻", anchor='end'))
    # a bracket under all four cards is the review's target; it breaks where the
    # validation arrow passes through to its own card
    yb = D1.y + h + 13
    g1, g2 = D2.cx - 9, D2.cx + 9
    b.append(f'<polyline class="e" points="{D1.x},{yb - 9} {D1.x},{yb} {g1},{yb}"/>')
    b.append(f'<polyline class="e" points="{g2},{yb} {R1.x + CW},{yb} {R1.x + CW},{yb - 9}"/>')
    rx = 747                              # in the gap between the last two cards
    b.append(edge([(rx, RV.y), (rx, yb + 1)], mid=m))
    b.append(lab(rx - 12, ly + (9 if both else 0), "the whole system: all four boxes", "整個系統：上框四個方格", anchor='end'))
    aria = ("What a transaction monitoring system should do, and the two checks on it. The system should be designed to fit your business, having regard to five factors about your own business; its parameters and thresholds set taking into account the transaction characteristics; it should give the staff who monitor and investigate timely and sufficient information; and it should watch the whole relationship, preferably relationship-based rather than transaction by transaction. The checks: the parameters and thresholds should be properly documented and independently validated, and the whole system, parameters and thresholds included, should be reviewed regularly for adequacy and effectiveness.",
            "交易監察系統應能做到的事，以及對系統的兩項查核。系統應因應五項關於你本身業務的因素設計；參數及門檻應顧及交易的特徵設定；系統應向負責監察及調查的職員提供適時而充分的資料；並應監察整段業務關係，盡可能以關係為本而非以個別交易為本。查核方面：參數及門檻應妥為記錄在案並經獨立驗證；整個系統（包括參數及門檻）應定期覆核是否合適及有效。")
    return svg(W, H + 12, ''.join(b), aria, m, 860)


SYSTEM_KEY = legend([('must', ("a duty for you: every box is a &lsquo;should&rsquo; in the Guideline",
                               "你的責任：每個方格在指引中均屬「應」"))])


# ---------------------------------------------------------------- 2. an unusual transaction
def fig_unusual():
    W = 1000
    both = lay() == 'both'
    Ta = Card(40, 290, ("It does not fit what you know", "與你的認知不符"),
              ("The customer's transactions are inconsistent with your knowledge of the customer, its business, risk profile or source of funds",
               "客戶的交易不符合你對該客戶、客戶的業務、風險狀況或資金來源的認知"), 'plain', "¶5.10(a)")
    Tb = Card(355, 290, ("Unusual, no apparent purpose", "異乎尋常，又無明顯目的"),
              ("Complex, unusually large in amount or of an unusual pattern, and with no apparent economic or lawful purpose",
               "複雜、款額大得異乎尋常或進行模式異乎尋常，並且沒有明顯經濟或合法目的"), 'plain', "¶5.10(b)")
    Tc = Card(670, 290, ("Your system raises an alert", "監察交易系統發出警報"),
              ("Take the steps below instead of closing it without sufficient justification and analysis",
               "採取下列步驟，而非在沒有充分理由及分析的情況下消除警報"), 'plain', TB("3"))
    S = Card(40, 920, ("Take appropriate steps to find out whether there are grounds for suspicion", "採取適當步驟，以識辨有否懷疑的理由"),
             ("For example: examine the background and purposes of the transactions; make appropriate enquiries of the customer; obtain additional CDD information from the customer",
              "例如：審查交易的背景及目的；適當地詢問客戶；向客戶索取額外的盡職審查資料"), 'must', "¶5.10 · fn 55")
    Q1 = Node(40, 520, ("Do you reasonably believe that performing the CDD process will tip off the customer?",
                        "你是否合理地相信執行盡職審查程序會向客戶通風報訊？"), "¶5.13", shape='hex')
    X1 = Card(620, 340, ("Document the basis for your assessment and file an STR", "把評估的基礎記錄在案，並提交可疑交易報告"),
              ("The STR goes to the JFIU. You may stop pursuing the CDD process",
               "報告提交予財富情報組。可停止繼續跟進該程序"), 'must', "¶5.13", answer=True)
    Q2 = Node(40, 520, ("Did your enquiries produce what you consider a satisfactory explanation?",
                        "查詢後是否取得你認為屬可信納的解釋？"), "¶5.11–5.12", shape='hex')
    OK = Card(40, 420, ("No grounds for suspicion", "沒有懷疑的理由"),
              ("You may conclude this and take no further action. Even so, consider updating the customer's risk profile with any relevant information obtained",
               "可如此斷定，並不再採取進一步行動。即使未有識辨出可懷疑之處，仍應考慮根據取得的相關資料更新客戶的風險狀況"), 'ok', "¶5.11", answer=True)
    NS = Card(540, 420, ("Grounds for suspicion: make an STR to the JFIU", "有懷疑的理由：向財富情報組提交可疑交易報告"),
              ("Without a satisfactory explanation you may conclude there are grounds for suspicion, and a suspicion identified means an STR",
               "未能取得可信納的解釋，可斷定為有懷疑的理由；識別出可懷疑之處，便應提交可疑交易報告"), 'must', "¶5.12", answer=True)
    REC = Card(40, 920, ("Whatever the route, put it in writing", "不論經哪條路線，均應以書面記錄"),
               ("The findings and outcomes of the steps, and the rationale for any decision made after them, properly documented and available to the CCE, other competent authorities and auditors",
                "所採取步驟的發現及結果、其後作出任何決定的理由，均應以書面妥為記錄，以便提交予關長、其他主管當局及核數師"), 'must', "¶5.14")
    ANY = Card(40, 920, ("At any point, a suspicion identified means an STR to the JFIU", "在任何時候，識別出可懷疑之處便應向財富情報組提交可疑交易報告"),
               ("Not only after an explanation fails: in any event, wherever suspicion is identified during transaction monitoring, an STR should be made",
                "不只在未能取得解釋之後：在任何情況下，如在交易監察的過程中識別出可懷疑之處，便應提交可疑交易報告"), 'must', "¶5.12")
    H = place([([Ta, Tb, Tc], 64 if both else 48), ([S], 40), ([Q1, X1], 46), ([Q2], 84), ([OK, NS], 44), ([REC], 70 if both else 52), ([ANY], 0)], y0=14)
    for row in ((Ta, Tb, Tc), (OK, NS)):
        h = max(n.h for n in row)
        y = min(n.y for n in row)
        for n in row:
            n.h, n.y = h, y
    b = [n.render() for n in (Ta, Tb, Tc, S, Q1, X1, Q2, OK, NS, REC)]
    # the standing rule is not a next step: set apart by a rule and a heading, with the same solid red border as every duty box
    b.append(ANY.render())
    yr = REC.y + REC.h + 16
    b.append(f'<line class="n n-faint" x1="{REC.x}" y1="{yr}" x2="{REC.x + REC.w}" y2="{yr}"/>')
    b.append(lab(REC.x, ANY.y - 9, "Applies throughout, not a next step", "適用於整個過程，並非下一步", anchor='start'))
    m = 'g5u'
    # the Guideline's two situations meet at one joint, marked with the word each view's text
    # joins them by, and go on as one arrow; the alert box (from the circular) keeps its own
    tb = Ta.y + Ta.h
    jy = tb + (42 if both else 24)
    mx = (Ta.cx + Tb.cx) / 2
    b.append(f'<polyline class="e" points="{Ta.cx:.0f},{tb:.0f} {Ta.cx:.0f},{jy:.0f} {Tb.cx:.0f},{jy:.0f} {Tb.cx:.0f},{tb:.0f}"/>')
    b.append(lab(mx, jy - 9, "or", "及"))
    b.append(edge([(mx, jy), (mx, S.y)], mid=m))
    b.append(edge([(Tc.cx, tb), (Tc.cx, S.y)], mid=m))
    b.append(edge([(Q1.cx, S.y + S.h), Q1.top], mid=m))
    # tipping off: yes to the right, no straight down
    b.append(edge([Q1.right, X1.left], mid=m))
    b.append(lab((Q1.x + Q1.w + X1.x) / 2, Q1.cy - 10, "yes", "是"))
    b.append(edge([Q1.bottom, Q2.top], mid=m))
    b.append(lab(Q1.cx + 10, (Q1.y + Q1.h + Q2.y) / 2 + (14 if both else 5), "no", "否", anchor='start'))
    # satisfactory explanation
    j2 = Q2.y + Q2.h + 22
    b.append(edge([Q2.bottom, (Q2.cx, j2), (OK.cx, j2), (OK.cx, OK.y)], mid=m))
    b.append(edge([Q2.bottom, (Q2.cx, j2), (NS.cx, j2), (NS.cx, NS.y)], mid=m))
    off = 18 if both else 0   # a stacked label grows upward: keep it clear of the junction line
    b.append(lab(OK.cx - 10, j2 + 19 + off, "yes", "是", anchor='end'))
    b.append(lab(NS.cx + 10, j2 + 19 + off, "no", "否", anchor='start'))
    for n in (OK, NS):
        b.append(edge([(n.cx, n.y + n.h), (n.cx, REC.y)], mid=m))
    # stopping CDD is still recorded: down the right margin, clear of the outcome boxes
    b.append(edge([X1.right, (982, X1.cy), (982, REC.cy), (REC.x + REC.w, REC.cy)], mid=m))
    aria = ("What to do when a transaction does not add up. Three situations send you into the steps: the customer's transactions do not fit what you know of the customer, its business, risk profile or source of funds; a transaction is complex, unusually large or of an unusual pattern and has no apparent economic or lawful purpose; or your monitoring system raises an alert, which you should not close without sufficient justification and analysis. Take appropriate steps to find out whether there are grounds for suspicion, such as examining the background and purposes, making enquiries of the customer, or obtaining more CDD information. If you reasonably believe that performing the CDD process will tip off the customer, document the basis for that assessment and file an STR with the JFIU; you may stop pursuing the process. Otherwise, if the enquiries give a satisfactory explanation you may conclude there are no grounds for suspicion and take no further action, still considering an update to the customer's risk profile. If they do not, you may conclude there are grounds for suspicion, and an STR should be made. Every route ends in a written record of the findings, outcomes and the rationale for any decision, available to the CCE, other competent authorities and auditors. At any point, any suspicion identified during transaction monitoring means an STR to the JFIU.",
            "交易不合情理時應怎樣做。指引指在以下情況應採取步驟：客戶的交易不符合你對該客戶、其業務、風險狀況或資金來源的認知；及交易複雜、款額大得異乎尋常或模式異乎尋常，並且沒有明顯經濟或合法目的。通函另指，監察交易系統發出警報時，應採取步驟，而非在沒有充分理由及分析的情況下消除警報。你應採取適當步驟以識辨有否懷疑的理由，例如審查交易的背景及目的、詢問客戶或索取額外的盡職審查資料。如你合理地相信執行盡職審查程序會向客戶通風報訊，應把評估的基礎記錄在案並向財富情報組提交可疑交易報告；你可停止繼續跟進該程序。否則，如查詢取得可信納的解釋，可斷定沒有懷疑的理由而不再採取行動，但仍應考慮更新客戶的風險狀況；如未能取得，可斷定為有懷疑的理由，並應提交可疑交易報告。每條路線均以書面記錄告終：發現、結果及任何決定的理由，以便提交予關長、其他主管當局及核數師。在任何時候，如在交易監察過程中識別出可懷疑之處，便應提交可疑交易報告。")
    return svg(W, H + 14, ''.join(b), aria, m, 860)


UNUSUAL_KEY = legend([('', ("a situation that calls for steps", "應採取步驟的情況")), ('hex', ("a question you answer", "你須回答的問題")),
                      ('must', ("a duty for you: a &lsquo;should&rsquo; in the Guideline", "你的責任：指引所說的「應」")),
                      ('ok', ("an ending with no further action", "毋須再採取行動的結果"))])
