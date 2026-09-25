# Figures for the Guideline Chapter 7 page: spotting suspicion with SAFE, the
# internal route from staff to the MLRO's decision, what happens after an STR,
# and the court documents law enforcement may serve on you.
from ui import *
from bl_figs import lines_down
from gl_fig import dash


def mlabel(x, y, en, tc, anchor='middle'):
    """ui.mlabel with 17-unit leading, so the bold 13.5-unit English line and its
    white halo clear the Chinese line under it in the combined view."""
    out = []
    for v, ls in (('en', [en]), ('tc', [tc]), ('both', [en, tc])):
        n = len(ls)
        g = [f'<text class="lbl s-{v}" text-anchor="{anchor}">']
        for i, l in enumerate(ls):
            g.append(f'<tspan x="{x}" y="{y - (n - 1 - i) * 17:.1f}">{esc(l)}</tspan>')
        g.append('</text>')
        out.append(''.join(g))
    return ''.join(out)


def DO(s):
    """DTROP and OSCO section, as a citation pair."""
    return (f"DTROP & OSCO s.{s}", f"《販毒（追討得益）條例》及《有組織及嚴重罪行條例》第{s}條")


def UN(s):
    return (f"UNATMO s.{s}", f"《聯合國（反恐怖主義措施）條例》第{s}條")


def cc(*cs):
    """Join several citations into one."""
    pairs = [cite_pair(c) for c in cs]
    return (' · '.join(p[0] for p in pairs), ' · '.join(p[1] for p in pairs))


# ---------------------------------------------------------------- 1. SAFE
def fig_safe():
    W = 1000
    T = Card(230, 540, ("A red flag, or a transaction that does not fit what you know of the customer",
                        "出現可疑交易指標，或交易不符合你對客戶的認知"),
             ("Examine it further. Any relevant red flag should lead at least to initial enquiries about the source of funds and a request for more CDD documents",
              "進一步審查。偵察到任何相關的可疑交易訊號，應及時作進一步調查，這至少可促使你對資金來源作出初步查詢，並要求提供更多盡職審查證明文件"),
             'plain', "¶7.3 · ¶7.10")
    xs = [20, 270, 520, 770]
    S = Card(xs[0], 210, ("S · Screen", "S · 篩查"), ("the account for suspicious indicators", "篩查戶口識別可疑交易指標"), 'plain', "¶7.11(a)")
    A = Card(xs[1], 210, ("A · Ask", "A · 提問"), ("the customer appropriate questions", "向客戶作出恰當提問"), 'plain', "¶7.11(b)")
    F = Card(xs[2], 210, ("F · Find out", "F · 翻查"), ("the customer's records", "翻查客戶的已知紀錄"), 'plain', "¶7.11(c)")
    E = Card(xs[3], 210, ("E · Evaluate", "E · 評估"), ("all of the above information", "根據以上資料作出評估"), 'plain', "¶7.11(d)")
    D = Node(250, 440, ("Are there grounds for suspicion?", "是否有懷疑的理由？"), "¶5.11–5.12", shape='hex')
    Y = Card(20, 450, ("Yes: report it to the MLRO", "是：向洗錢報告主任報告"),
             ("An internal report, reaching the MLRO without undue delay. The next section follows it",
              "內部報告不得無故延誤送達洗錢報告主任。下一節續述"), 'must', "¶7.12(b) · ¶5.12", href="#internal")
    N = Card(530, 450, ("No: a satisfactory explanation", "否：取得可信納的解釋"),
             ("No further action is needed, but consider updating the customer's risk profile with what you learned",
              "無需採取進一步行動，但應考慮根據所得資料更新客戶的風險狀況"), 'ok', "¶5.11")
    # the SAFE row sits inside a dashed frame: an optional method, labelled at its top right
    lab_h = 17
    H = place([([T], 50 + lab_h), ([S, A, F, E], 58), ([D], 48), ([Y, N], 0)], y0=14)
    fy = S.y - lab_h - 14
    fb = S.y + S.h + 14
    b = [f'<rect class="n n-faint" x="8" y="{fy:.0f}" width="984" height="{fb - fy:.0f}" rx="8"/>',
         label(980, S.y - 10, ("The JFIU's SAFE approach: you may adopt it where it applies", "財富情報組的ＳＡＦＥ方法：可按情況採用"), 'end')]
    b += [n.render() for n in (T, S, A, F, E, D, Y, N)]
    m = 'g7s'
    ym = T.bottom[1] + 16
    b.append(edge([T.bottom, (T.cx, ym), (S.cx, ym), S.top], mid=m))
    for a, c in ((S, A), (A, F), (F, E)):
        b.append(edge([(a.x + a.w, a.cy), (c.x, c.cy)], mid=m))
    b.append(edge([E.bottom, (E.cx, D.cy), D.right], mid=m))
    jy = D.bottom[1] + 24
    b.append(edge([D.bottom, (D.cx, jy), (Y.cx, jy), Y.top], ("yes", "是"), Y.cx + 10, jy - 7, 'start', mid=m))
    b.append(edge([D.bottom, (D.cx, jy), (N.cx, jy), N.top], ("no", "否"), N.cx - 10, jy - 7, 'end', mid=m))
    aria = ("Spotting suspicion. A red flag, or a transaction that does not fit what you know of the customer, calls for further examination and at least initial enquiries about the source of funds. The JFIU's SAFE approach, which an MSO may adopt, runs in four steps: screen the account for suspicious indicators, ask the customer appropriate questions, find out the customer's records, and evaluate all of that information. If there are grounds for suspicion, the staff member makes an internal report that must reach the MLRO without undue delay. If there is a satisfactory explanation, no further action is needed, but the customer's risk profile should be considered for updating.",
            "識辨可疑交易。出現可疑交易指標，或交易不符合你對客戶的認知，便應進一步審查；偵察到可疑交易訊號，應及時作進一步調查，這至少可促使對資金來源作出初步查詢。財富情報組推廣的ＳＡＦＥ方法（金錢服務經營者可按情況採用）分四步：篩查戶口識別可疑交易指標、向客戶作出恰當提問、翻查客戶的已知紀錄，以及根據以上資料作出評估。如有懷疑的理由，職員須作出內部報告，不得無故延誤送達洗錢報告主任。如取得可信納的解釋，無需採取進一步行動，但應考慮更新客戶的風險狀況。")
    return svg(W, H + 14, ''.join(b), aria, m, 860)


SAFE_KEY = legend([('', ("a step you take", "你採取的步驟")), ('faint', ("an optional method (dashed frame)", "可選用的方法（虛線框）")),
                   ('hex', ("the question you answer", "你須回答的問題")),
                   ('must', ("a duty that follows", "隨之而來的責任")), ('ok', ("a safe outcome", "安全的結果"))])


# ---------------------------------------------------------------- 2. staff to the MLRO's decision
def fig_internal():
    W = 1000
    ST = Card(40, 510, ("A staff member forms a suspicion", "職員產生懷疑"),
              ("Your guidance to staff and agents should equip them to recognise the signs", "你為職員及代理人提供的導引，應讓他們能辨別有關跡象"), 'plain', "¶7.10")
    SUP = Card(665, 315, ("Consulting a supervisor first: allowed", "先諮詢主管或經理：可以"),
               ("But a supervisor or manager with no ML reporting or compliance role may never filter the report out",
                "但非負責洗錢報告／合規職能的主管或經理，在任何情況下均不得過濾報告"), 'plain', "¶7.13")
    IR = Card(40, 510, ("An internal report to the MLRO", "向洗錢報告主任作出內部報告"),
              ("Without undue delay, along the shortest line; with enough detail of the customer and of what gave rise to the suspicion",
               "不得無故延誤，流程越短越好；載有客戶的充分詳情，以及導致產生懷疑的全部資料"), 'must', "¶7.12(b) · ¶7.13 · ¶7.15")
    DONE = Card(665, 315, ("The staff member's statutory duty is now fully satisfied", "該職員已完全履行法定責任"),
                ("Provided the report followed your procedures", "但須按你訂立的程序作出報告"), 'ok', "¶7.14")
    ACK = Card(40, 510, ("The MLRO should acknowledge it, and remind the reporter about tipping off", "洗錢報告主任必須確認收到，並提醒報告職員不可通風報訊"),
               None, 'must', "¶7.16")
    EV = Card(40, 510, ("The MLRO evaluates the report", "洗錢報告主任評估報告"),
              ("Reasonable steps to consider all relevant information, CDD and ongoing monitoring included. This may include connected accounts, relationship by relationship; earlier instructions and the length of the relationship; questioning the customer the JFIU's way",
               "採取合理步驟考慮所有相關資料，包括盡職審查及持續監察資料；這可包括以關係為本覆核有關連戶口、參考先前的指示模式及業務關係年期，以及按財富情報組推薦的方法查問客戶"),
              'must', "¶7.17")
    BAL = Card(665, 315, ("Searching further takes time", "進一步搜尋需時"),
               ("Balance it against the duty to make a timely STR, and document the review and its conclusions",
                "應與及時提交報告的法定規定取得平衡，並記錄覆核過程及結論"), 'must', "¶7.18")
    D = Node(90, 420, ("Grounds for knowledge or suspicion?", "有知悉或懷疑的理由？"), "¶7.19–7.20", shape='hex')
    Y = Card(40, 450, ("Yes: an STR to the JFIU", "有：向財富情報組提交可疑交易報告"),
             ("As soon as reasonable once the evaluation is complete, with the information the knowledge or suspicion rests on",
              "評估完成後在合理範圍內盡快提交，連同知悉或懷疑所根據的資料"), 'must', "¶7.19", href="#jfiu")
    N = Card(530, 430, ("No: no STR, and a record of why", "沒有：不提交報告，並記錄原因"),
             ("A good-faith decision after weighing all available information makes criminal liability unlikely. Keep proper records of the deliberations and actions",
              "真誠地在考慮所有可獲取的資料後作出決定，則不大可能負上刑事責任。須把慎重考慮及採取的行動妥為記錄"), 'ok', "¶7.20")
    REG = Card(40, 940, ("Either way, the report goes in the register of internal reports", "不論結果，報告均記入內部報告紀錄冊"),
               None, 'faint', "¶7.29", href="#after")
    H = place([([ST, SUP], 38), ([IR, DONE], 38), ([ACK], 38), ([EV, BAL], 40), ([D], 48), ([Y, N], 38), ([REG], 0)], y0=14)
    b = [n.render() for n in (ST, SUP, IR, DONE, ACK, EV, BAL, D, Y, N, REG)]
    m = 'g7i'
    for a, c in ((ST, IR), (IR, ACK), (ACK, EV)):
        b.append(edge([a.bottom, c.top], mid=m))
    b.append(edge([(EV.cx, EV.y + EV.h), (EV.cx, D.y)], mid=m))
    # side boxes all hang off their step the same way: a dashed line with a word saying how
    for a, c, en, tc in ((ST, SUP, "may", "可"), (IR, DONE, "then", "此後"), (EV, BAL, "if you search", "如再搜尋")):
        b.append(dash([(a.x + a.w, a.cy), (c.x, c.cy)]))
        b.append(mlabel((a.x + a.w + c.x) / 2, a.cy - 8, en, tc))
    jy = D.bottom[1] + 24
    b.append(edge([D.bottom, (D.cx, jy), (Y.cx, jy), Y.top], ("yes", "有"), Y.cx - 10, jy - 7, 'end', mid=m))
    b.append(edge([D.bottom, (D.cx, jy), (N.cx, jy), N.top], ("no", "沒有"), N.cx - 10, jy - 7, 'end', mid=m))
    for n in (Y, N):
        b.append(edge([n.bottom, (n.cx, REG.y)], mid=m))
    aria = ("From a staff member's suspicion to the MLRO's decision. The staff member may consult a supervisor or manager first, but one with no money laundering reporting or compliance role may never filter the report out. The internal report must reach the MLRO without undue delay along the shortest line, with enough detail of the customer and the grounds for suspicion; once it is made under the MSO's procedures, the staff member's statutory duty is fully satisfied. The MLRO should acknowledge it and remind the reporter about tipping off, then takes reasonable steps to evaluate all relevant information, balancing any search of connected accounts against the need for a timely STR and documenting the review. If there are grounds for knowledge or suspicion, the MLRO files an STR with the JFIU as soon as reasonable after the evaluation. If not, a good-faith decision makes criminal liability unlikely, provided the deliberations are recorded. Either way the report goes in the register of internal reports.",
            "由職員產生懷疑至洗錢報告主任作出決定。職員可先諮詢主管或經理，但非負責洗錢報告或合規職能的主管或經理，在任何情況下均不得過濾報告。內部報告須經最短的報告流程、不得無故延誤送達洗錢報告主任，並載有客戶的充分詳情，以及導致產生懷疑的全部資料；職員按經營者的程序作出報告後，即已完全履行法定責任。洗錢報告主任必須確認收到報告，並提醒職員不可通風報訊，然後採取合理步驟評估所有相關資料，在搜尋有關連戶口與及時提交報告之間取得平衡，並記錄覆核過程。如有知悉或懷疑的理由，洗錢報告主任須在評估完成後在合理範圍內盡快向財富情報組提交可疑交易報告；如沒有，真誠作出的決定不大可能招致刑事責任，但須記錄慎重考慮的過程。不論結果，報告均記入內部報告紀錄冊。")
    return svg(W, H + 14, ''.join(b), aria, m, 860)


INTERNAL_KEY = legend([('', ("a step, or what is allowed", "步驟，或容許的做法")), ('must', ("a duty on you or your MLRO", "你或洗錢報告主任的責任")),
                       ('hex', ("the MLRO's decision", "洗錢報告主任的決定")),
                       ('ok', ("a protection", "保障")), ('faint', ("the record it leaves", "留下的紀錄"))])


# ---------------------------------------------------------------- 3. after the STR
def fig_after():
    W = 1000
    FILE = Card(40, 500, ("You file an STR with the JFIU", "你向財富情報組提交可疑交易報告"), None, 'plain', "¶7.19")
    DEF = Card(610, 370, ("Statutory defence for the acts disclosed", "就所披露的作為取得法定免責辯護"),
               ("On one of two conditions", "須符合以下兩項條件之一"), 'ok', "¶7.25")
    DB = Card(610, 370, ("Before the acts, with consent", "作為之前，並得到同意"),
              ("The report comes first, and the disclosed acts are then undertaken with the JFIU's consent",
               "報告在你作出所披露的作為之前作出，而該作為得到財富情報組的同意"), 'ok', "¶7.25(a)")
    DA = Card(610, 370, ("After the acts, on your own initiative", "作為之後，由你主動作出"),
              ("The report is made after you have performed the disclosed acts, on your own initiative and as soon as it is reasonable",
               "報告在你作出所披露的作為之後，由你主動及在合理範圍內盡快作出"), 'ok', "¶7.25(b)")
    ACK = Card(40, 500, ("The JFIU acknowledges receipt", "財富情報組確認收到報告"), None, 'plain', "¶7.24")
    D = Node(40, 500, ("Is imminent action needed, such as a restraint order?", "是否需要立即採取行動，例如發出限制令？"),
             "¶7.24", shape='hex')
    CON = Card(20, 460, ("No: consent is usually given", "否：一般會給予「同意」"),
               ("To operate the account, under DTROP and OSCO s.25A(2)(a) and UNATMO s.12(2B)(a)",
                "讓你根據《販毒（追討得益）條例》及《有組織及嚴重罪行條例》第25A(2)(a)條，以及《聯合國（反恐怖主義措施）條例》第12(2B)(a)條運作該戶口"),
               'may', "¶7.24")
    ACT = Card(520, 460, ("Yes: take appropriate action", "是：採取適當行動"),
               ("And seek legal advice where necessary", "並按需要徵詢法律意見"), 'must', "¶7.24")
    REV = Card(20, 960, ("Either way: review the relationship", "不論如何：覆核業務關係"),
               ("Whatever feedback the JFIU later gives, you should apply appropriate risk-mitigating measures. Filing and carrying on without further thought is not acceptable. If necessary, senior management decides how to handle the relationship",
                "不論財富情報組其後有否給予反饋，均應執行適當的減低風險措施。提交報告後繼續運作而不再考慮風險，是不可接受的。如有需要，上報高級管理層決定如何處理該關係"),
               'must', "¶7.27")
    MORE = Card(20, 960, ("Another suspicion about the same customer", "同一客戶再出現可疑情況"),
                ("Of the same nature or a different one: it goes to the MLRO again, who reports to the JFIU if appropriate",
                 "不論是否屬同一性質：均須再向洗錢報告主任報告，如恰當，他會再向財富情報組報告"), 'must', "¶7.28")
    lab = 26 if lay() == 'both' else 14
    H = place([([FILE, DEF], 30 + lab), ([ACK, DB], 30 + lab), ([D, DA], 50), ([CON, ACT], 40), ([REV], 34 + lab), ([MORE], 0)], y0=14)
    # each left-hand step sits at the top of its row, so the main line runs straight down
    for L, R in ((FILE, DEF), (ACK, DB), (D, DA)):
        L.y = R.y = min(L.y, R.y)
    b = [n.render() for n in (FILE, DEF, DB, DA, ACK, D, CON, ACT, REV, MORE)]
    m = 'g7a'
    b.append(edge([FILE.bottom, ACK.top], mid=m))
    b.append(edge([ACK.bottom, D.top], mid=m))
    b.append(dash([(FILE.x + FILE.w, FILE.cy), (DEF.x, FILE.cy)]))
    b.append(mlabel((FILE.x + FILE.w + DEF.x) / 2, FILE.cy - 8, "gives", "令你取得"))
    b.append(dash([DEF.bottom, DB.top]))
    b.append(mlabel(DEF.cx + 8, (DEF.y + DEF.h + DB.y) / 2 + 5, "either", "其一", 'start'))
    b.append(dash([DB.bottom, DA.top]))
    b.append(mlabel(DB.cx + 8, (DB.y + DB.h + DA.y) / 2 + 5, "or", "或", 'start'))
    row = max(D.y + D.h, DA.y + DA.h)
    jy = row + 25
    b.append(edge([D.bottom, (D.cx, jy), (CON.cx, jy), CON.top], ("no", "否"), CON.cx - 10, jy - 7, 'end', mid=m))
    b.append(edge([D.bottom, (D.cx, jy), (ACT.cx, jy), ACT.top], ("yes", "是"), ACT.cx - 10, jy - 7, 'end', mid=m))
    for n in (CON, ACT):
        b.append(edge([n.bottom, (n.cx, REV.y)], mid=m))
    b.append(dash([REV.bottom, MORE.top]))
    b.append(mlabel(REV.cx + 10, (REV.y + REV.h + MORE.y) / 2 + 5, "if further suspicious transactions or events arise", "如再出現可疑交易或事件", 'start'))
    aria = ("After an STR. Filing gives a statutory defence for the acts disclosed, on one of two conditions: a report made before the acts, which are then undertaken with the JFIU's consent; or a report made after the acts, on the MSO's own initiative and as soon as reasonable. The JFIU acknowledges receipt. If no imminent action such as a restraint order is needed, it will usually consent to the MSO operating the account; otherwise the MSO takes appropriate action and seeks legal advice where necessary. Either way the MSO should review the relationship and apply appropriate risk-mitigating measures, escalating to senior management if necessary. If a further suspicion about the same customer arises, it goes to the MLRO again.",
            "提交可疑交易報告之後。提交報告可就所披露的作為取得法定免責辯護，但須符合兩項條件之一：報告在作為之前作出，而該作為得到財富情報組的同意；或報告在作為之後，由經營者主動及在合理範圍內盡快作出。財富情報組確認收到報告；如無需立即採取行動（例如發出限制令），一般會同意經營者運作該戶口，否則經營者須採取適當行動，並按需要徵詢法律意見。不論如何，經營者均應覆核業務關係並執行適當的減低風險措施，如有需要，上報高級管理層。如同一客戶再出現可疑情況，須再向洗錢報告主任報告。")
    return svg(W, H + 14, ''.join(b), aria, m, 860)


AFTER_KEY = legend([('', ("a step", "步驟")), ('hex', ("the JFIU's question", "財富情報組的考慮")),
                    ('may', ("a discretion the JFIU holds", "財富情報組持有的酌情權")), ('must', ("a duty on you", "你的責任")),
                    ('ok', ("a protection for you", "你的保障"))])


# ---------------------------------------------------------------- 4. court documents
def fig_lea():
    W = 1000
    POL = Card(20, 960, ("Before anything arrives: clear policies and procedures", "事前準備：清晰的政策和程序"),
               ("To handle court documents effectively and in time: accurate information, sufficient resources, and a staff member appointed as the main point of contact with law enforcement agencies",
                "以有效及合時的方式處理法庭文件：提供準確資料、分配足夠資源，並委任一名人員作為與執法機構的中央聯絡點"),
               'must', "¶7.31")
    xs, w = [20, 345, 670], 310
    C1 = Card(xs[0], w, ("Search warrant or production order", "搜查令或提交令"),
              ("Court documents that help law enforcement agencies carry out investigations", "協助執法機構進行調查的法庭文件"), 'may', "¶7.31")
    C2 = Card(xs[1], w, ("Restraint order", "限制令"),
              ("Prohibits dealing with particular funds or property pending the outcome of an investigation", "調查有結果前，禁止處理某些資金或財產"),
              'may', "¶7.33")
    C3 = Card(xs[2], w, ("Confiscation, or forfeiture", "沒收令或充公"),
              ("Confiscation of criminal proceeds after a conviction; forfeiture of property the court is satisfied is terrorist property",
               "被告定罪後，法院可下令沒收其犯罪所得；法院信納屬恐怖分子財產的，可下令充公"), 'may', "¶7.34")
    D1 = Card(xs[0], w, ("Respond within the time limit", "在規定期限內回應"),
              ("With all information or material within the document's scope. Struggling with the timeframe: contact the officer-in-charge at the earliest opportunity",
               "提供一切屬該文件範圍內的資料或材料。難以遵守時限：第一時間聯絡調查的主管人員"), 'must', "¶7.32")
    D2 = Card(xs[1], w, ("Be able to withhold the restrained property", "確保能扣留受限制的財產"),
              ("The order may not cover everything in the relationship: consider what, if anything, may still be used, subject to Hong Kong law",
               "限制令不一定涵蓋業務關係的全部資金或財產；應考慮按香港法例可動用哪些（如有）"), 'must', "¶7.33")
    D3 = Card(xs[2], w, ("A confiscation order may be served on you", "你可能收到沒收令"),
              ("If you hold funds or other property of the defendant that the court deems to represent his benefit from the crime",
               "如你持有屬於被告、法院認為代表其犯罪得益的資金或其他財產"), 'plain', "¶7.34")
    ALL = Card(20, 960, ("Whatever arrives, an intelligence request such as a notification letter included", "不論收到甚麼，包括與罪行相關的情報要求（例如通知書）"),
               ("Assess the risks in good time, and whether to review the customer or relationship for suspicion. The customer it names may be a victim of crime",
                "適時評估所涉風險，並評估是否需要覆核該客戶或業務關係，以斷定是否有可懷疑之處。文件所涉的客戶可能是罪案的受害人"),
               'must', "¶7.35")
    heads = [(["While they investigate"], ["調查期間"]), (["Pending the outcome"], ["等候調查結果"]), (["When the court rules"], ["法院裁決時"])]
    POL.y = 14
    hy = POL.y + POL.h + 22
    hh = 2 * 14 * FS if lay() == 'both' else 14 * FS
    top = hy + hh + 14
    place([([C1, C2, C3], 44), ([D1, D2, D3], 44), ([ALL], 0)], y0=top)
    # top-align each row, so every column starts right under its heading
    for row in ((C1, C2, C3), (D1, D2, D3)):
        t = min(c.y for c in row)
        for c in row:
            c.y = t
    b = [n.render() for n in (POL, C1, C2, C3, D1, D2, D3, ALL)]
    m = 'g7l'
    for x, (en, tc) in zip(xs, heads):
        b.append(lines_down(x + w / 2, hy - 4, en, tc, 't t-b', 12.5))
    # the bottom band is a frame that applies whatever arrives, so nothing leads into it
    for c, d in ((C1, D1), (C2, D2), (C3, D3)):
        b.append(edge([c.bottom, (d.cx, d.y)], mid=m))
    H = ALL.y + ALL.h
    aria = ("Court documents and law enforcement requests. Before anything arrives, an MSO needs clear policies and procedures: accurate information, sufficient resources and a staff member as the main point of contact with law enforcement. While law enforcement investigates, a search warrant or production order must be answered within the time limit with everything in its scope, contacting the officer-in-charge early if the timeframe is a problem. Pending the outcome, a restraint order prohibits dealing with particular property, which the MSO must be able to withhold, though the order may not cover everything in the relationship. After a conviction, a court may order confiscation of criminal proceeds, served on an MSO holding the defendant's property; a court may also order property it is satisfied is terrorist property forfeited. Whatever arrives, including a notification letter, the MSO should assess the risks in good time, consider reviewing the customer for suspicion, and remember the customer may be a victim.",
            "法庭文件及執法機構的要求。在收到任何文件之前，經營者須有清晰的政策和程序：提供準確資料、分配足夠資源，並委任一名人員作為與執法機構的中央聯絡點。調查期間，搜查令或提交令須在規定期限內回應，提供一切屬其範圍內的資料；如難以遵守時限，應第一時間聯絡調查的主管人員。等候調查結果期間，限制令禁止處理某些財產，經營者必須能扣留有關財產，但限制令不一定涵蓋業務關係中的全部資金。被告定罪後，法院可下令沒收犯罪所得，持有被告財產的經營者可能收到沒收令；法院如信納某財產屬恐怖分子財產，亦可下令充公。不論收到甚麼（包括通知書），經營者應適時評估風險，考慮覆核客戶以斷定是否有可懷疑之處，並留意客戶可能是罪案的受害人。")
    return svg(W, H + 14, ''.join(b), aria, m, 860)


LEA_KEY = legend([('may', ("a power the court or law enforcement holds", "法院或執法機構持有的權力")),
                  ('must', ("a duty on you", "你的責任")), ('', ("what may follow for you (no duty stated)", "對你可能的影響（未訂明責任）"))])
