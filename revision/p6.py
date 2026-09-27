# AMLO Part 6: the Review Tribunal, ss.54-76, read from the licensee's side.
from ui import *
from bl_figs import lines_down


def dash(a, b):
    return f'<polyline class="e e-dash" points="{a[0]:.0f},{a[1]:.0f} {b[0]:.0f},{b[1]:.0f}"/>'


def split_label(x, y, en, tc, below=24):
    """Edge label for a horizontal line: one language sits above it; in the bilingual view the Chinese sits just below."""
    out = []
    for v, parts in (('en', [(en, y)]), ('tc', [(tc, y)]), ('both', [(en, y), (tc, y + below)])):
        g = [f'<text class="lbl s-{v}" text-anchor="middle">']
        for t, ty in parts:
            g.append(f'<tspan x="{x:.1f}" y="{ty:.1f}">{esc(t)}</tspan>')
        g.append('</text>')
        out.append(''.join(g))
    return ''.join(out)


def fig_route():
    W = 1000
    D0 = Card(115, 480, ("The Commissioner makes a specified decision about you", "關長就你作出指明決定"),
              ("A written notice gives the reasons and says you may apply to the Review Tribunal", "書面通知載明理由，並說明你可向覆核審裁處申請覆核"), cite="s.54 · s.30(9) · s.44(3)")
    Q1 = Node(115, 480, ("Aggrieved? Apply in writing, stating your grounds, within 21 days after the notice was sent",
                         "感到受屈？須在通知送出後21日內，以書面申請並述明理由"), "s.59(1), (4)", shape='hex')
    X1 = Card(665, 325, ("Out of time?", "已逾期？"),
              ("The Tribunal may extend the time, but only after both sides have had a chance to be heard, and for good cause", "審裁處可延展限期，但須先給予雙方陳詞機會，並信納有良好因由"), 'may', "s.59(2)–(3)", answer=True)
    T = Card(115, 480, ("The Tribunal reviews", "審裁處進行覆核"),
             ("A chairperson and 2 other members. Both parties are heard, and facts are found on the balance of probabilities",
              "由主席及另外2名成員組成。審裁處覆核時須給予雙方合理的陳詞機會；事實在相對可能性的衡量下確立"), cite="s.56 · s.60(3)–(4)")
    S1 = Card(665, 325, ("Applying is not a stay", "申請覆核不等於暫緩執行"),
              ("If the decision is already in effect, only a stay order pauses it, and the Tribunal must hear your application as soon as reasonably practicable",
               "如決定已經生效，只有暫緩執行命令才可暫停。審裁處須盡快聆訊你的暫緩執行申請"), 'may', "s.69", answer=True)
    DET = Card(115, 480, ("The determination", "裁定"),
               ("Confirm; vary, or set aside and substitute any decision the Commissioner could have made, heavier or lighter; or send it back with directions",
                "確認或更改原決定，或推翻原決定並以關長本可作出的任何決定取代，可較嚴苛或較寬鬆；或連同指示發還關長"), 'must', "s.60(1)–(2)", answer=True)
    Q2 = Node(175, 360, ("Dissatisfied with the determination?", "不滿意裁定？"), "s.71(1)", shape='hex')
    FIN = Card(10, 250, ("No appeal: the determination is final", "不上訴：裁定屬終局"),
               ("Subject only to this appeal and to section 50 of the High Court Ordinance", "只受本項上訴及《高等法院條例》第50條規限"), 'must', "s.74", answer=True)
    CA = Card(455, 300, ("Appeal to the Court of Appeal, with its leave", "經上訴法庭許可後上訴"),
              ("On law, fact, or mixed law and fact. Leave needs a reasonable prospect of success, or another reason in the interests of justice",
               "你可就法律、事實或法律兼事實問題上訴。批予許可須符合其一：有合理的機會得直；或有其他有利於秉行公正的理由"), 'ok', "s.71", answer=True)
    S2 = Card(780, 210, ("Appealing is not a stay", "上訴不等於暫緩執行"),
              ("The determination keeps its effect. Ask the Tribunal or the Court of Appeal for a stay", "裁定照常有效。可向審裁處或上訴法庭申請暫緩執行"), 'may', "s.70 · s.73", answer=True)
    CAR = Card(455, 300, ("The Court of Appeal decides", "上訴法庭作出決定"),
               ("Allow, dismiss, vary or set aside and substitute, or remit to the Tribunal or to the Commissioner", "判上訴得直、駁回上訴、更改或推翻並取代裁定，或發還審裁處或關長處理"), 'must', "s.72", answer=True)
    H = place([([D0], 34), ([Q1, X1], 40), ([T, S1], 34), ([DET], 40), ([Q2], 46), ([FIN, CA, S2], 34), ([CAR], 0)])
    b = [n.render() for n in (D0, Q1, X1, T, S1, DET, Q2, FIN, CA, S2, CAR)]
    m = 'p6r'
    b.append(edge([D0.bottom, Q1.top], mid=m))
    b.append(edge([Q1.bottom, T.top], ("yes, in time", "是，並在限期內"), Q1.cx + 10, (Q1.bottom[1] + T.top[1]) / 2 + 4, 'start', mid=m))
    b.append(dash(Q1.right, X1.left))
    b.append(split_label((Q1.x + Q1.w + X1.x) / 2, Q1.cy - 7, "late", "逾期"))
    b.append(edge([T.bottom, DET.top], mid=m))
    b.append(dash(T.right, S1.left))
    b.append(edge([DET.bottom, Q2.top], mid=m))
    b.append(edge([Q2.left, (FIN.cx, Q2.cy), FIN.top], ("no", "否"), FIN.cx - 10, (Q2.cy + FIN.y) / 2 + 5, 'end', mid=m))
    b.append(edge([Q2.right, (CA.cx, Q2.cy), CA.top], ("yes", "是"), CA.cx + 10, (Q2.cy + CA.y) / 2 + 5, 'start', mid=m))
    b.append(dash(CA.right, S2.left))
    b.append(edge([CA.bottom, CAR.top], mid=m))
    aria = ("The review route. The Commissioner's specified decision comes with a written notice. An aggrieved person applies in writing with grounds within 21 days after the notice was sent; the Tribunal may extend the time after hearing both sides and finding good cause. The Tribunal of a chairperson and two members hears both parties and determines the review by confirming, varying, substituting or remitting. Applying does not stay the decision. A party dissatisfied with the determination may appeal to the Court of Appeal on law, fact or both, but only with leave; otherwise the determination is final. Appealing does not stay the determination either.",
            "覆核途徑。關長的指明決定附有書面通知。感到受屈的人須在通知送出後21日內以書面申請並述明理由；審裁處在聽取雙方陳詞並信納有良好因由後可延展限期。由主席及兩名成員組成的審裁處聽取雙方陳詞，以確認、更改、取代或發還的方式作出裁定。申請覆核不會令決定暫緩執行。不滿意裁定的一方可經許可就法律、事實或兩者向上訴法庭上訴；否則裁定屬終局。上訴亦不會令裁定暫緩執行。")
    return svg(W, H + 14, ''.join(b), aria, m, 860)


ROUTE_KEY = legend([('hex', ("a question you answer", "你須回答的問題")), ('', ("a step", "步驟")),
                    ('may', ("a discretion the Tribunal or court holds", "審裁處或法院的酌情權")),
                    ('must', ("a binding result: the Tribunal's determination, or the Court of Appeal's decision", "具約束力的結果：審裁處的裁定或上訴法庭的決定")), ('ok', ("a route open to you", "你可循的途徑"))])

A = sec('route', [("Part 6", "第6部"), "s.54–s.76", ("the review", "覆核")],
        ("From a decision to the Court of Appeal", "由決定到上訴法庭"),
    P("Follow the centre column from the top: it is the path of a review. The boxes to the right, joined by dashed lines, are the side-applications you can make on the way. The first hexagon holds the only deadline in the Part.",
      "由頂部沿中間一欄往下看：這是覆核的路徑。右邊以虛線連接的方格，是途中可提出的附帶申請。第一個六邊形載有本部唯一的限期。")
    + fig(fig_route, ("A review is a full second look, not a one-way ratchet: the Tribunal can substitute any decision the Commissioner had power to make, even a heavier one, and it can reach for a different section to do it.",
                        "覆核是全面重新審視，並非只可減輕：審裁處可以關長本有權作出的任何決定取代原決定，即使較嚴苛亦可，而且可以根據另一條文作出。"), ROUTE_KEY)
    + traps(
        trap(("21 days after the notice is sent, not received", "是通知送出後21日，不是收到後"),
             ("The clock starts when the notice goes out. Put that beside Part 7: a notice left at, or posted to, any premises named in your licence counts as duly given. A letter sitting unread at a closed branch is still running down your time.",
              "限期由通知送出時開始計算。再配合第7部：通知留在或郵寄往牌照所指明的任何處所，即視為已妥為發出。即使信件擱在已關門的分店無人拆閱，限期仍在流逝。"),
             "s.59(1) · s.80(1)"),
        trap(("A review can make it worse, and so can an appeal", "覆核可以令結果更重，上訴亦然"),
             ("Varying or substituting a decision can produce anything the Commissioner could have decided about you, whether more or less onerous, and under any provision. The Court of Appeal has the same reach one level up: a determination it varies or substitutes can be anything the Tribunal had power to make in that review, heavier or lighter, under the same provision or another.",
              "更改或取代決定時，結果可以是關長本可就你作出的任何決定，不論較嚴苛或較寬鬆，亦不限於同一條文。上訴法庭在上一層亦有同樣的權力：它更改或取代的裁定，可以是審裁處本有權就該覆核作出的任何裁定，不論較嚴苛或較寬鬆，亦不論是否根據同一條文。"),
             "s.60(2) · s.72(2)"),
    ))

# ---------------------------------------------------------------- B. what you can challenge
B_ = sec('decisions', [("s.54, 'specified decision' (d)", "第54條「指明決定」(d)段"), "s.59(1)"],
         ("What you can take to the Tribunal", "可向審裁處申請覆核的決定"),
    P("Only a <b>specified decision</b> can be reviewed, and the list is closed. For a money service operator it is the Commissioner's licensing and disciplinary decisions. Find the area on the left.",
      "只有<b>指明決定</b>才可申請覆核，而且清單是封閉的。就金錢服務經營者而言，即關長的發牌及紀律決定。在左邊找出範疇。")
    + table([th("Area", "範疇"), th("Reviewable: a specified decision", "可覆核：屬指明決定"), th("Not on the list", "不在清單之內")], [
        tr(rh("Your licence", "你的牌照"),
           td("Refusing to grant or to renew it; imposing a condition when granting; amending or imposing a condition on renewal or mid-term; revoking or suspending it.",
              "拒絕批給或續期；批給時施加條件；續期時或有效期內修改或施加條件；撤銷或暫時吊銷牌照。", "s.30 · s.31 · s.32 · s.34"),
           td("The licence ending by itself on death, dissolution or the start of winding up, and your own decision to cease business. Neither is a decision of the Commissioner.",
              "牌照因去世、解散或開始清盤而不再有效，以及你自行決定停業。兩者都不是關長的決定。", "s.42 · s.41")),
        tr(rh("People and premises", "人員及處所"),
           td("Refusing approval for a new director, ultimate owner or partner; refusing to add new premises; refusing to let you operate at particular premises.",
              "拒絕批准新董事、最終擁有人或合夥人；拒絕加入新處所；拒絕讓你在特定處所經營。", "s.35 · s.36 · s.37 · s.38 · s.39"),
           td("—", "—")),
        tr(rh("Discipline", "紀律行動"),
           td("Any power under section 21 (Part 4), for breach of a Schedule 2 specified provision, and any power under section 43 (Part 5), for breach of a licence condition, a s.51 regulation or a licensee duty in ss.35–41: public reprimand, order to take remedial action, pecuniary penalty.",
              "第21條（第4部）下的任何權力（就違反附表2的指明的條文），以及第43條（第5部）下的任何權力（就違反牌照條件、根據第51條訂立的規例，或第35至41條下持牌人的責任）：公開譴責、命令採取糾正行動、罰款。", "s.21 · s.43(1)–(2)", post=flag()),
           td("—", "—")),
        tr(rh("Supervision and prosecution", "監管及檢控"),
           td("None of these.", "全部不屬指明決定。"),
           td("A routine inspection or an investigation requirement, a magistrate's warrant, a decision to prosecute, and a notice to keep records for longer than five years.",
              "例行視察或調查要求、裁判官手令、檢控決定，以及要求把紀錄備存超過五年的通知。", "Part 3 · s.79 · s.20(4) Sch. 2", post=flag())),
    ], minw=780)
    + traps(
        trap(("Aggrieved, and about you", "感到受屈，而且關乎你"),
             ("The right belongs to a person aggrieved by a specified decision made in relation to that person. It is not a general right for anyone who dislikes the Commissioner's decision about somebody else.",
              "覆核權屬於因就其作出的指明決定而感到受屈的人，並非任何不滿關長對他人所作決定的人都享有的一般權利。"),
             "s.59(1)"),
    ))

# ---------------------------------------------------------------- C. the clock
def fig_clock6():
    W = 1000
    # The axis is drawn to scale: 21 days, then 30 days (51 in all) between x0 and x51.
    x0, x51 = 110, 900
    x21 = x0 + (x51 - x0) * 21 / 51
    WIN = Node(x0, x21 - x0 - 5, ("21 days to apply for review, counted from when the notice was sent", "申請覆核的限期：通知送出後的21日"), "s.59(1)", 'ok', size=12)
    PAY = Node(x21 + 5, x51 - x21 - 5, ("30 days to pay a pecuniary penalty from when the decision takes effect, unless the notice allows longer",
                          "繳付罰款的限期：決定生效後30日，除非通知容許較長期間"), "s.21(3) · s.43(3)", 'must', size=12)
    WIN.h = PAY.h = max(WIN.h, PAY.h)
    H = place([([WIN, PAY], 0)], y0=14)
    ay = H + 26
    b = [WIN.render(), PAY.render()]
    # Coloured bands on the axis tie each box to the stretch of time it describes.
    # The axis is drawn in two pieces that stop at the bands, so nothing shows through them.
    b.append(f'<line class="e" x1="60" y1="{ay}" x2="{x0}" y2="{ay}"/>')
    b.append(f'<line class="e" x1="{x51}" y1="{ay}" x2="980" y2="{ay}" marker-end="url(#{mref("p6c")})"/>')
    b.append(f'<rect x="{x0}" y="{ay-5}" width="{x21-x0:.0f}" height="10" rx="2" style="fill:var(--green);fill-opacity:.7;stroke:none"/>')
    b.append(f'<rect x="{x21:.0f}" y="{ay-5}" width="{x51-x21:.0f}" height="10" rx="2" style="fill:var(--red);fill-opacity:.7;stroke:none"/>')
    for x in (x0, x21, x51):
        b.append(f'<line class="e" x1="{x:.0f}" y1="{ay-11}" x2="{x:.0f}" y2="{ay+11}"/>')
    ends = (["30 days after it", "takes effect:", "the penalty is due"], ["生效後30日：", "罰款到期"])
    b.append(lines_down(x0, ay + 14, ["the notice is sent"], ["通知送出"], 't', size=11.5))
    b.append(lines_down(x21, ay + 14, ["day 21: if you did nothing,", "the decision takes effect"], ["第21日：如你沒有任何行動，", "決定即生效"], 't', size=11.5))
    b.append(lines_down(x51, ay + 14, *ends, 't', size=11.5))
    n = {'en': 3, 'tc': 2, 'both': 5}[lay()]
    aria = ("The default clock, drawn to scale: the notice is sent, you have 21 days from then to apply for review, the decision takes effect when those days end if you did nothing, and a pecuniary penalty is then due within 30 days unless the notice allows longer.",
            "預設時限（按比例繪畫）：通知送出後，你有21日申請覆核；如你沒有任何行動，決定在限期屆滿時生效；其後罰款須在30日內繳付，除非通知容許較長期間。")
    return svg(W, ay + 14 + n * 11.5 * FS * 1.3 + 14, ''.join(b), aria, 'p6c', 720)


C_ = sec('clock', ["s.59", "s.75", ("with s.30–34", "另及第30至34條")],
         ("The 21-day clock, and when a decision bites", "21日的限期，以及決定何時生效"),
    P("The line is the default path when nothing unusual happens. The table below it covers every other way the decision can take effect, including the decisions that never wait for the 21 days at all.",
      "時間線顯示在沒有特別情況下的預設路徑。下表列出決定生效的所有其他方式，包括完全不必等待21日的決定。")
    + fig(fig_clock6, ("The two periods run end to end, and the axis is drawn to scale: the 30 days to pay start only when the decision takes effect, which by default is the end of the 21 days.",
                         "兩個期間首尾相接，時間軸按比例繪畫：30日的繳款期要到決定生效時才開始，而決定預設在21日屆滿時生效。"),
          legend([('ok', ("time you are given", "給予你的時間")), ('must', ("time you must meet", "你必須遵守的時限"))]))
    + table([th("What happened", "發生了甚麼"), th("The decision takes effect", "決定何時生效")], [
        tr(td("Before the 21 days run out, you tell the Commissioner in writing that you will not apply", "在21日屆滿前，你以書面通知關長你不會申請覆核", "s.75(1)(a)"),
           td("At the moment you tell him", "在你通知他之時")),
        tr(td("You neither tell him nor apply within the 21 days", "你在21日內既沒有通知他，也沒有申請覆核", "s.75(1)(b)"),
           td("When the 21 days expire", "在21日屆滿時")),
        tr(td("You apply, and the Tribunal confirms the decision", "你申請覆核，而審裁處確認決定", "s.75(1)(c)(i)"),
           td("When it is confirmed", "在獲確認時")),
        tr(td("You apply, and the Tribunal varies it or substitutes another", "你申請覆核，而審裁處更改決定或以另一決定取代", "s.75(1)(c)(ii)"),
           td("When varied or substituted, on the terms of the variation", "在被更改或取代時，按更改或取代的條款生效")),
        tr(td("You apply, then withdraw", "你申請覆核後撤回申請", "s.75(1)(c)(iii)"),
           td("When the application is withdrawn", "在申請被撤回時")),
        tr(td("The Commissioner considers it appropriate in the public interest", "關長認為為維護公眾利益而屬適當", "s.75(2)"),
           td("At whatever other time he specifies in the notice", "在通知內指明的另一時間")),
        '<tr class="divhead"><td colspan="2">' + B("Decisions with their own clock: the Ordinance provides otherwise", "有自己時限的決定：條例另有規定") + '</td></tr>',
        tr(td("A licence condition imposed at grant, amended or imposed on renewal, or amended or imposed mid-term", "批給時施加的牌照條件，或在續期時或有效期內修改或施加的條件", "s.30(7) · s.31(7) · s.32(4)"),
           td("When you receive the notice, or at the time it specifies, <b>whichever is later</b>", "在你收到通知時，或在通知指明的時間，<b>以較遲者為準</b>", post=flag())),
        tr(td("Revocation or suspension of your licence", "撤銷或暫時吊銷你的牌照", "s.34(6)"),
           td("At the time specified in the notice", "在通知指明的時間", post=flag())),
        tr(td("A refusal to renew, when you applied in time and the licence expired while the Commissioner was deciding", "你已按時申請續期，而牌照在關長作出決定前期滿，其後續期被拒", "s.31(10)"),
           td("Your licence stays in force until the refusal takes effect under the ordinary rules above, unless you withdraw the renewal application or the licence is revoked or suspended under s.34", "除非續期申請被撤回，或牌照根據第34條被撤銷或暫時吊銷，否則你的牌照仍然有效，直至拒絕續期的決定按上述一般規則生效")),
    ], minw=720)
    + numreq([
        (("21 days", "21日"),
         ("Apply to the Tribunal in writing, stating the grounds", "以書面向審裁處申請覆核，並述明理由"),
         ("Counted from when the notice of the decision was sent", "自告知決定的通知送出後起計"),
         ("The decision takes effect when the period ends, and a late application needs an extension, granted only for good cause after both sides are heard", "限期屆滿時決定即生效；逾期申請須獲延展，而延展只在雙方均獲陳詞機會並有良好因由時才批給"),
         "s.59(1)–(4) · s.75(1)(b)"),
        (("30 days", "30日"),
         ("Pay a pecuniary penalty imposed under Part 4 or Part 5", "繳付根據第4部或第5部施加的罰款"),
         ("From when the order takes effect as a specified decision, unless the notice allows longer", "自命令作為指明決定生效時起計，除非通知容許較長期間"),
         ("If unpaid, the Commissioner may apply to the Court of First Instance to register the order. Once registered, it is treated as an order of that Court for the payment of money, made within its civil jurisdiction", "如未繳付，關長可向原訟法庭申請登記該罰款命令；命令一經登記，即視為原訟法庭在其民事司法管轄權範圍內作出的繳付款項命令"),
         "s.21(3), (5)–(6) · s.43(3), (5)–(6)"),
        (("as soon as reasonably practicable", "在合理地切實可行範圍內盡快"),
         ("The Tribunal sends your application to the Commissioner, hears any stay application, and delivers its determination with reasons", "審裁處把你的申請送交關長、聆訊暫緩執行的申請，並宣告其裁定及理由"),
         ("Each step of a review; these are duties on the Tribunal, not on you", "覆核的每個步驟；這些是審裁處而非你的責任"),
         ("No fixed consequence is written in; they are standards of promptness", "條文並無訂明固定後果；屬迅速處理的標準"),
         "s.59(5) · s.69(3) · s.66(1)"),
    ])
    + traps(
        trap(("Not every decision waits for the 21 days", "並非每項決定都等待21日"), None, "s.30(7) · s.34(6) · s.75",
             vs=[(("Waits", "等待"), ("Penalties, reprimands, orders to take remedial action, refusals: the ordinary rules apply, so an application for review keeps them from taking effect until it is decided or withdrawn, unless the notice set another time in the public interest.", "罰款、譴責、命令採取糾正行動、拒絕：適用一般規則，故申請覆核後，決定要待覆核有結果或申請撤回時才生效，除非通知為公眾利益另定時間。")),
                 (("Does not wait", "不等待"), ("Licence conditions bite on receipt of the notice or later; revocation and suspension bite at the time the notice specifies.", "牌照條件在收到通知時或其後生效；撤銷及暫時吊銷在通知指明的時間生效。"))]),
        trap(("Applying is not the same as a stay", "申請覆核不等於暫緩執行"),
             ("An application for review does not by itself operate as a stay of execution. Where the decision is already biting, only an order of the Tribunal, on your application, can pause it.",
              "覆核申請本身並不具有暫緩執行決定的效力。若決定已經生效，只有審裁處應你的申請作出命令，才可暫停執行。"),
             "s.69(1)–(2)"),
    ))

# ---------------------------------------------------------------- D. powers
D_ = sec('powers', ["s.61–s.68", ("powers and offences", "權力與罪行")],
         ("What the Tribunal can make people do", "審裁處可要求別人做甚麼"),
    P("The Tribunal runs like a court but is freer with evidence. The first table is what it can do; the second is what it costs anyone who gets in its way.",
      "審裁處的運作與法院相似，但在證據方面較寬鬆。第一個表是它可以做甚麼；第二個表是妨礙它的代價。")
    + table([th("Power", "權力"), th("What it lets the Tribunal do", "審裁處可以做甚麼")], [
        tr(rh("Evidence", "證據", "s.61(1)(a)–(b)"), td("Receive and consider any material, oral, written or documentary, <b>whether or not a court would admit it</b>, and decide how it is received.", "收取及考慮任何以口述、書面或文件形式提供的材料，<b>不論法院是否接納</b>，並決定收取方式。", post=flag())),
        tr(rh("Witnesses", "證人", "s.61(1)(c)–(f)"), td("By a notice signed by the chairperson, require a person to attend, give evidence and produce anything relevant; administer oaths; examine on oath or otherwise and require truthful answers; order evidence by affidavit.", "藉主席簽署的書面通知，要求任何人出席、提供證據及交出相關物品；監誓；訊問已宣誓或未經宣誓的人並要求據實回答；命令以誓章提供證據。")),
        tr(rh("Secrecy", "保密", "s.61(1)(g)–(h) · s.66(2)"), td("Order that material it receives is not published, prohibit publication of anything from a private sitting, and, after a private sitting, ban publication or disclosure of all or part of its determination, a costs order, or the reasons for either.", "命令不得發表其收取的材料、禁止發表閉門聆訊中的任何內容；閉門聆訊後，亦可禁止發表或披露裁定、訟費命令或其理由的全部或任何部分。")),
        tr(rh("Procedure", "程序", "s.61(1)(i)–(j)"), td("Stay the proceedings on terms in the interests of justice, and decide its own procedure.", "在顧及公正原則後按條款擱置程序，並自行決定程序。")),
        tr(rh("Contempt", "藐視罪", "s.63"), td("Punish for contempt with the same powers, and the same standard of proof, as the Court of First Instance.", "以與原訟法庭相同的權力及舉證準則懲罰藐視罪。")),
        tr(rh("Costs", "訟費", "s.65"), td("Award costs to a party, or to anyone whose attendance was needed, payable by the other party or a party it chooses and recoverable as a civil debt.", "向覆核的一方或須出席的人判給訟費，由另一方或審裁處選定的一方支付，並可作為民事債項追討。")),
        tr(rh("Enforcement", "強制執行", "s.67–s.68"), td("Its orders are recorded in writing and signed by the chairperson; a document purporting to be one is, in the absence of evidence to the contrary, presumed to be an order duly made and signed. An order can be registered in the Court of First Instance, after which it counts as that court's order.", "其命令須以書面記錄並由主席簽署；在沒有相反證據的情況下，看來是由主席簽署的命令，須被推定為妥為作出並簽署的審裁處命令。命令並可在原訟法庭登記，登記後即視為該法庭的命令。")),
    ], minw=700)
    + table([th("What someone did, without reasonable excuse", "某人在無合理辯解下的行為"), th("On indictment", "循公訴程序定罪"), th("Summarily", "循簡易程序定罪")], [
        tr(td("Ignored an order, notice, prohibition or requirement of the Tribunal; disrupted or misbehaved at a sitting; left without permission after being required to attend", "不遵從審裁處的命令、通知、禁令或要求；干擾聆訊或行為不檢；被要求出席後未經准許而離開", "s.61(2)(a)–(c)"),
           td("$1,000,000 + 2 years", "罰款$1,000,000及監禁2年", cls='pen'), td("level 6 + 6 months", "第6級罰款及監禁6個月", cls='pen')),
        tr(td("Hindered or deterred a witness, or threatened, insulted or caused loss to a witness or to a member of the Tribunal because of their role", "阻礙或阻嚇證人，或因證人或審裁處成員的角色而威脅、侮辱他們或令他們蒙受損失", "s.61(2)(d)–(f)"),
           td("$1,000,000 + 2 years", "罰款$1,000,000及監禁2年", cls='pen'), td("level 6 + 6 months", "第6級罰款及監禁6個月", cls='pen')),
        tr(td("Broke a ban, made after a private sitting, on publishing or disclosing the determination, a costs order, or the reasons for either", "違反在閉門聆訊後禁止發表或披露裁定、訟費命令或其理由的命令", "s.66(2)–(4)"),
           td("$1,000,000 + 2 years", "罰款$1,000,000及監禁2年", cls='pen'), td("level 6 + 6 months", "第6級罰款及監禁6個月", cls='pen')),
    ], note=B("The same conduct cannot be punished twice. If criminal proceedings under section 61(2) have been brought and are still pending, or cannot lawfully be brought again, the Tribunal cannot deal with the conduct as contempt. The reverse also applies: if the contempt power has been used and those proceedings are still pending, or the power cannot lawfully be used again, no prosecution under section 61(2) can follow.",
             "同一行為不可受兩次懲處：如已根據第61(2)條提起刑事法律程序，而該程序仍待決或不得再合法提起，審裁處即不可再以藐視罪處理；反之，如已行使藐視罪懲罰權力，而有關程序仍待決或該權力不得再合法行使，亦不可再根據第61(2)條提出檢控。") + ' ' + cite_html("s.63(4)"), minw=700)
    + traps(
        trap(("Incriminating evidence: protected automatically before the Tribunal, only if claimed first in an investigation", "會導致入罪的證據：在審裁處席前毋須聲稱，調查時須先聲稱"), None, "s.61(4) · s.62 · s.15",
             vs=[(("Before the Tribunal", "在審裁處席前"), ("You cannot refuse because an answer might incriminate you, but the answer and the requirement are inadmissible against you in criminal proceedings without any claim, except where you are charged, in respect of that evidence, with failing to comply with the Tribunal under s.61(2)(a) or with an offence under Part V of the Crimes Ordinance (Cap. 200).", "你不可因答案可能令你入罪而拒絕回答；但毋須任何聲稱，該答案及要求即不得在刑事法律程序中用作針對你的證據，惟你就該證據被控犯第61(2)(a)條（不遵從審裁處）或《刑事罪行條例》（第200章）第V部所訂罪行者除外。")),
                 (("Before a Part 3 investigator", "在第3部調查員面前"), ("The same shield exists only if you claim it before you answer.", "只有在回答之前作出聲稱，才享有同樣的保障。"))]),
        trap(("Your bank's other customers stay private", "你銀行的其他客戶資料受保密"),
             ("If an authorized institution acts as banker or financial adviser to the person applying for review, neither Part 6 nor Schedule 4 makes it disclose the affairs of any of its other customers.",
              "如認可機構擔任覆核申請人的銀行或財務顧問，第6部及附表4均不規定它披露其他客戶的事務資料。"),
             "s.64"),
    ))

# ---------------------------------------------------------------- E. appeal
E_ = sec('appeal', ["s.70–s.74", ("appeal", "上訴")],
         ("Appeals, stays and finality", "上訴、暫緩執行與終局"),
    P("Once the Tribunal has spoken there is exactly one way out, and it needs permission. Read the table by row: each row compares the Tribunal stage with the appeal stage on the same question.",
      "審裁處作出裁定後，只有一條出路，而且須經許可。按行閱讀：每一行就同一問題比較審裁處階段與上訴階段。")
    + table([th("", ""), th("At the Tribunal", "在審裁處"), th("At the Court of Appeal", "在上訴法庭")], [
        tr(rh("How you get there", "如何進入"), td("Apply within 21 days after the notice was sent; late only with an extension", "在通知送出後21日內申請；逾期須獲延展", "s.59"),
           td("Only with the Court of Appeal's <b>leave</b>, which may be limited to particular issues and made subject to conditions", "必須獲上訴法庭批予<b>許可</b>；許可可限於特定爭論點，並可附加條件", "s.71(2)–(3)")),
        tr(rh("What can be argued", "可爭議甚麼"), td("Everything: the whole decision is reviewed", "全部：整個決定均受覆核", "s.60(1)"),
           td("A question of <b>law, of fact, or of mixed law and fact</b>", "<b>法律問題、事實問題，或法律兼事實問題</b>", "s.71(1)", post=flag())),
        tr(rh("The test to get in", "進入的門檻"), td("Being aggrieved by a specified decision about you", "因就你作出的指明決定而感到受屈", "s.59(1)"),
           td("A reasonable prospect of success, or some other reason in the interests of justice", "上訴有合理機會得直，或有其他有利於秉行公正的理由", "s.71(4)")),
        tr(rh("What can come out", "可能的結果"), td("Confirm, vary, set aside and substitute, or remit to the Commissioner", "確認、更改、推翻並取代，或發還關長", "s.60(1)"),
           td("Allow, dismiss, vary or set aside and substitute, or remit to the Tribunal or to the Commissioner. A varied or substituted determination can be anything the Tribunal had power to make, heavier or lighter", "判上訴得直、駁回、更改或推翻並取代，或發還審裁處或關長。經更改或取代的裁定，可以是審裁處本有權作出的任何裁定，不論較嚴苛或較寬鬆", "s.72(1)–(2)", post=flag())),
        tr(rh("Is applying a stay?", "申請本身是否暫緩執行？"), td("No: an application for review is not by itself a stay. Ask the Tribunal for one", "否：覆核申請本身並不具暫緩執行的效力。須向審裁處申請", "s.69"),
           td("No: lodging an appeal is not by itself a stay. Ask the Tribunal or the Court of Appeal", "否：提出上訴本身並不具暫緩執行的效力。須向審裁處或上訴法庭申請", "s.70 · s.73")),
        tr(rh("When you can ask for a stay", "何時可申請暫緩執行"), td("Of the Commissioner's decision: at any time before the Tribunal determines the review, or your application for more time. Of the Tribunal's own determination: any party, at any time after it is made", "暫緩執行關長的決定：在審裁處就覆核或你的延展限期申請作出裁定前，隨時可申請。暫緩執行審裁處的裁定：覆核的任何一方在裁定作出後隨時可申請", "s.69(2) · s.70(1)", post=flag()),
           td("Once an appeal is lodged, any party to the review may apply", "上訴一經提出，覆核的任何一方均可申請", "s.73(2)")),
        tr(rh("Conditions on a stay", "暫緩執行的條件"), td("The Tribunal may grant it subject to conditions as to costs, payment of money into the Tribunal, or other matters it considers appropriate", "審裁處可在訟費、繳存款項於審裁處或其他事宜方面定出它認為適當的條件，暫緩執行須受該等條件規限", "s.69(4) · s.70(2)"),
           td("Any condition the Court of Appeal considers appropriate, including conditions as to costs and payment of money into the Tribunal", "上訴法庭認為適當的任何條件，包括關於訟費及繳存款項於審裁處的條件", "s.73(3)")),
        tr(rh("Costs", "訟費"), td("The Tribunal may award them, under the High Court's rules on costs", "審裁處可判給，並適用高等法院的訟費規則", "s.65"),
           td("The Court of Appeal may make any order it considers appropriate", "上訴法庭可作出其認為適當的命令", "s.72(3)")),
    ], cls='cmp', note=B("Beyond this appeal the determination is final and not subject to appeal, subject only to section 50 of the High Court Ordinance.", "除本項上訴外，審裁處的裁定屬終局決定，不可上訴，只受《高等法院條例》第50條規限。") + ' ' + cite_html("s.74"), minw=760)
    + traps(
        trap(("Appeal on the facts too", "亦可就事實上訴"),
             ("Many appeals from tribunals are limited to points of law. This one is not: a question of fact, or of mixed law and fact, can go up, provided the Court of Appeal gives leave.",
              "不少針對審裁處的上訴只限於法律問題，但本項上訴並非如此：只要上訴法庭批予許可，事實問題或法律兼事實問題亦可上訴。"),
             "s.71(1)–(2)"),
    ))

P6_NAV = [('route', 'The route to review', '覆核途徑'), ('decisions', 'What you can challenge', '可覆核的決定'),
          ('clock', 'When a decision bites', '決定何時生效'), ('powers', 'Tribunal powers', '審裁處的權力'),
          ('appeal', 'Appeals and stays', '上訴與暫緩執行')]
P6_BODY = A + B_ + C_ + D_ + E_
