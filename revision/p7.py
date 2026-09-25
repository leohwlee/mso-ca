# AMLO Part 7: miscellaneous provisions, ss.77-82.
from ui import *


def fig_prosecute():
    W = 1000
    TOP = Card(190, 620, ("Someone is to be prosecuted for an offence under the Ordinance", "有人須就本條例所訂罪行被檢控"), None)
    L1 = Card(24, 440, ("The Secretary for Justice prosecutes", "律政司司長提出檢控"),
              ("The ordinary route. Section 79 does not derogate from the Secretary's powers, so both penalty tiers written into the offence section stay available",
               "一般途徑。第79條並不減損律政司司長的權力，故罪行條文所訂的兩級罰則均可適用"), cite="s.79(3)")
    R1 = Card(536, 440, ("The Commissioner prosecutes in his own name", "關長以本身名義提出檢控"),
              ("Allowed for any offence under the Ordinance, and for conspiracy to commit one", "適用於本條例所訂的任何罪行，以及串謀犯該等罪行"), 'may', "s.79(1)", answer=True)
    R2 = Card(536, 440, ("Tried summarily, before a magistrate", "由裁判官以簡易程序審訊"),
              ("So the summary penalty is the ceiling: level 6 and 6 months, say, instead of $1,000,000 and 2 years", "故上限為簡易程序罰則：例如第6級罰款及監禁6個月，而非罰款$1,000,000及監禁2年"), 'must', "s.79(1)", answer=True)
    R3 = Card(536, 440, ("His own staff may run the case", "其僱員或員工可處理案件"),
              ("An employee or staff member who is not a barrister or solicitor may appear and plead before the magistrate, with a lawyer's other rights for that prosecution",
               "並非大律師或律師的僱員或員工，可在裁判官席前出席及陳詞，並就該項檢控享有律師的所有其他權利"), 'may', "s.79(2)")
    # the two routes are alternatives: give them the same top and height so both drops are equal
    L1.h = R1.h = max(L1.h, R1.h)
    H = place([([TOP], 50), ([L1, R1], 44), ([R2], 44), ([R3], 0)])
    b = [n.render() for n in (TOP, L1, R1, R2, R3)]
    m = 'p7p'
    jy = TOP.bottom[1] + 24
    b.append(edge([TOP.bottom, (TOP.cx, jy), (L1.cx, jy), L1.top], mid=m))
    b.append(edge([TOP.bottom, (TOP.cx, jy), (R1.cx, jy), R1.top], mid=m))
    b.append(edge([R1.bottom, R2.top], ("must be", "必須"), R1.cx + 10, (R1.bottom[1] + R2.top[1]) / 2 + 5, 'start', mid=m))
    b.append(edge([R2.bottom, R3.top], ("in that prosecution", "就該項檢控"), R2.cx + 10, (R2.bottom[1] + R3.top[1]) / 2 + 5, 'start', mid=m))
    aria = ("Two ways an offence under the Ordinance reaches court. The Secretary for Justice can prosecute in the ordinary way, including on indictment. The Commissioner can prosecute in his own name, but the case must then be tried summarily before a magistrate, so the summary penalty is the ceiling, and in that prosecution his non-lawyer staff may appear and plead. Section 79 does not reduce the Secretary for Justice's powers.",
            "本條例所訂罪行進入法院的兩條途徑。律政司司長可按一般方式檢控，包括循公訴程序。關長可以本身名義檢控，但案件必須由裁判官以簡易程序審訊，故上限為簡易程序的罰則；就該項檢控，其非律師員工可出席及陳詞。第79條並不減損律政司司長的權力。")
    return svg(W, H + 14, ''.join(b), aria, m, 860)


# ---------------------------------------------------------------- A. standard of proof
A = sec('proof', [("Part 7", "第7部"), "s.78", ("with s.60, s.63", "另及第60、63條")],
        ("How sure a regulator has to be", "監管機構須證明到甚麼程度"),
    P("One question, four answers, depending on who is deciding. Find the decision-maker on the left.",
      "同一問題，四種答案，視乎由誰作決定。在左邊找出決策者。")
    + table([th("Who is deciding", "由誰決定"), th("What they must establish", "須證明甚麼"), th("The standard", "舉證準則")], [
        tr(rh("The Commissioner, for any purpose other than a criminal one", "關長（刑事以外的任何目的）", "s.78"),
           td("That you contravened any Ordinance, a notice or requirement, a licence condition or any other condition; or were responsible for, assisted, were concerned in, attempted or conspired in such a thing; or that it might occur",
              "你違反任何條例、通知或要求、牌照條件或其他條件；或曾對此負責、協助、牽涉其中、企圖或串謀；或此等事宜可能發生"),
           td("The <b>civil standard</b>, as in civil proceedings in a court", "<b>民事舉證準則</b>，與法院的民事法律程序相同", post=flag())),
        tr(rh("The Review Tribunal, on the facts of a review", "覆核審裁處（覆核中的事實）", "s.60(4)"),
           td("Any matter of fact in the review", "覆核中的任何事實事宜"),
           td("The <b>balance of probabilities</b>", "<b>相對可能性的衡量</b>")),
        tr(rh("The Review Tribunal, punishing contempt", "覆核審裁處（懲罰藐視罪）", "s.63(3)"),
           td("That someone is guilty of contempt", "某人犯藐視罪"),
           td("The <b>same standard as the Court of First Instance</b> uses for contempt", "<b>與原訟法庭</b>懲罰藐視罪時採用的準則<b>相同</b>")),
        tr(rh("A criminal court, trying an offence", "刑事法院（審理罪行）", "s.78"),
           td("That you committed an offence under the Ordinance", "你干犯本條例所訂罪行"),
           td("Section 78 does not apply: it expressly excludes provisions relating to criminal proceedings or to an offence", "第78條不適用：該條明文豁除關乎刑事法律程序或罪行的條文")),
    ], minw=760)
    + traps(
        trap(("Why discipline is easier to prove than a crime", "為何紀律行動比刑事罪行容易證明"),
             ("The same conduct can lead to Part 4 discipline and to a prosecution. For the discipline, the Commissioner needs only the civil standard and no proof of knowledge; the prosecution must prove the offence, including that the institution acted knowingly.",
              "同一行為可同時引致第4部紀律行動及刑事檢控。紀律行動只需民事舉證準則，亦毋須證明明知；刑事檢控則須證明罪行成立，包括機構明知而為。"),
             "s.78 · s.21(1) · s.5(5)"),
    ))

# ---------------------------------------------------------------- B. who prosecutes
B_ = sec('prosecute', ["s.79", ("with s.53", "另及第53條")],
         ("Who prosecutes, and what that caps", "由誰檢控，以及刑罰上限為何"),
    P("Two routes lead into court. Take the right-hand one and follow it down: the Commissioner may prosecute without the Department of Justice, but only in a magistrate's court.",
      "有兩條途徑進入法院。沿右邊一條往下看：關長可不經律政司自行檢控，但只能在裁判法院進行。")
    + fig(fig_prosecute, ("The practical result: when the Commissioner prosecutes in his own name, the ceiling is the summary penalty written into the offence section.",
                            "實際結果是：關長以本身名義提出檢控時，上限是罪行條文所訂的簡易程序罰則。"),
          legend([('', ("a step or a fact", "步驟或事實")), ('may', ("a power or permission on the Commissioner's side", "關長一方持有的權力或准許")),
                  ('must', ("a limit that follows", "隨之而來的限制"))]))
    + numreq([
        (("12 months", "12個月"),
         ("The window for prosecuting a Part 5 offence that is not indictable", "檢控第5部非可公訴罪行的期限"),
         ("Counted from when the offence is discovered by, or comes to the notice of, the Commissioner, not from when it was committed", "自關長發現或知悉該罪行時起計，而非自罪行發生時起計"),
         ("Proceedings for that offence can no longer be instituted", "即不可再就該罪行提起法律程序"),
         "s.53"),
    ])
    + traps(
        trap(("The 12-month rule belongs to Part 5 only", "12個月的規定只屬第5部"),
             ("It overrides the Magistrates Ordinance time limit for non-indictable offences under Part 5, such as failing to display the licence or to notify a change. It says nothing about offences elsewhere in the Ordinance.",
              "它就第5部的非可公訴罪行（例如沒有展示牌照或沒有具報改變）取代《裁判官條例》的時限；對條例其他部分的罪行並無規定。"),
             "s.53"),
    ))

# ---------------------------------------------------------------- C. notices
C_ = sec('notices', ["s.80", ("with s.59", "另及第59條")],
         ("How a notice reaches you", "通知如何送達你"),
    P("For a licensee, s.80(1) sets the deemed-service rule: a notice from the Commissioner counts as duly given if it is left at or posted to a premises named in the licence. Other senders have other rules. Find the sender on the left.",
      "就持牌人而言，第80(1)條訂明視為妥為發出的規則：關長的通知如留在或郵寄往牌照指明的任何處所，即須視為已妥為發出。其他發件人另有規則。在左邊找出發件人。")
    + table([th("The sender", "發件人"), th("It counts as duly given if", "在以下情況視為妥為發出")], [
        tr(rh("The Commissioner, writing to you as a licensee", "關長致你（持牌人）", "s.80(1)"),
           td("It is <b>left at, or sent by post to,</b> the premises, or any of the premises, specified in your licence as premises where you may operate a money service",
              "通知<b>留在或郵寄往</b>你所持牌照指明你可經營金錢服務的處所，或其中任何處所", post=flag())),
        tr(rh("The Registrar of Companies, or the Commissioner under the precious metals and stones regime", "公司註冊處處長，或關長根據貴金屬及寶石制度", "s.80(1A)–(1B)"),
           td("Left at or posted to a last known business, residential or correspondence address, a registered office, or <b>sent to the last known email address</b>",
              "留在或郵寄往最後為人所知的營業地址、住址或通訊地址、註冊辦事處，或<b>以電子方式傳送往最後為人所知的電郵地址</b>")),
        tr(rh("The Insurance Authority, the Monetary Authority or the Securities and Futures Commission", "保監局、金融管理專員或證監會", "s.80(2)–(5)"),
           td("The service rules of their own Ordinances apply, with necessary modifications", "各自條例的送達規則經必要變通後適用")),
    ], minw=700)
    + traps(
        trap(("Deemed service to a licensee: premises only, no email", "向持牌人視為妥為發出：只限處所，不包括電郵"), None, "s.80(1), (1B)(e) · s.59(1) · s.38 · s.40 · s.41",
             vs=[(("Commissioner to a licensee", "關長致持牌人"), ("Left at or posted to your licensed premises. Email is not in the subsection.", "留在或郵寄往你的持牌處所。該款並無提及電郵。")),
                 (("Why it matters", "為何重要"), ("A decision notice posted to a branch still named in your licence starts the 21 days for review. Keep the premises in your licence current: a change in premises particulars must be notified within one month (s.40); a new premises can be used only after the Commissioner, on your application, has added it to the licence (s.38); ceasing at a premises must be notified in writing before the date of cessation, and the licence returned for amendment within 7 days beginning on the date of cessation (s.41).", "郵寄往牌照上仍列明的分店的決定通知，同樣開始計算21日的覆核限期。須保持牌照上的處所資料準確：處所詳情有改變，須在一個月內向關長具報（第40條）；新的營業處所須先由你申請、關長加入牌照後方可使用（第38條）；停止在某處所經營，須在停業日期前以書面具報，並在自停業日期起計的7日內交回牌照以作修訂（第41條）。"))]),
    ))

# ---------------------------------------------------------------- D. what you can hold back
D_ = sec('privilege', ["s.81", ("with s.9A, s.12A, s.64", "另及第9A、12A、64條")],
         ("What you can hold back", "可保留不披露的資料"),
    P("The Ordinance compels a great deal, but three kinds of information keep some protection. The right-hand column is the limit on each.",
      "條例可強制取得大量資料，但有三類資料仍保留若干保障。右欄是各自的限制。")
    + table([th("Protected", "受保障的資料"), th("The protection", "保障內容"), th("The limit", "限制")], [
        tr(rh("Legal professional privilege", "法律專業保密權", "s.81"),
           td("The Ordinance does not affect any claim, right or entitlement arising from legal professional privilege.", "本條例不影響基於法律專業保密權而產生的任何聲稱、權利或享有權。"),
           td("A requirement to disclose the <b>name and address of a lawyer's client</b> still has to be met, whether or not the lawyer is qualified in Hong Kong.", "披露<b>法律執業者的客戶的姓名或名稱及地址</b>的要求仍須遵從，不論該執業者是否在香港取得資格。", post=flag())),
        tr(rh("Your customers' affairs, when another regulator's officer asks", "由其他監管當局的人員查詢你客戶的事務時", "s.9A · s.12A"),
           td("You need not disclose a customer's affairs to an officer sent by a regulator that is not your own.", "你毋須向並非你的有關當局的其他監管當局所派的人員披露客戶事務。"),
           td("Unless that regulator is of the opinion, and certifies in writing, that disclosure is necessary; in an investigation, the investigator must also have reasonable cause to believe the customer may be able to give information relevant to the investigation.", "除非該監管當局認為（並藉書面證明它認為）披露屬必要；在調查中，調查員另須有合理因由相信該客戶是可能有能力提供與該項調查相關的資料的人。")),
        tr(rh("A bank's other customers, at the Review Tribunal", "在覆核審裁處：銀行的其他客戶", "s.64"),
           td("An authorized institution acting as banker or financial adviser to the applicant need not disclose the affairs of its other customers.", "擔任申請人的銀行或財務顧問的認可機構，毋須披露其其他客戶的事務。"),
           td("It covers customers other than the applicant only.", "只涵蓋申請人以外的客戶。")),
    ], minw=760))

# ---------------------------------------------------------------- E. regulations and the transition
E_ = sec('regs', ["s.77", "s.82", ("with s.51, s.24", "另及第51、24條")],
         ("Regulations, and the move from the old register", "規例，以及由舊紀錄冊過渡"),
    P("Two housekeeping sections. The first says who writes the detailed rules; the second explains how the money changers and remittance agents already registered under the old regime became licensees when the Ordinance began.",
      "兩條處理行政事宜的條文。第一條說明由誰訂立詳細規則；第二條解釋在本條例生效時，已根據舊制度登記的貨幣兌換商及匯款代理人如何成為持牌人。")
    + table([th("", ""), th("What it provides", "規定甚麼")], [
        tr(rh("Regulations", "規例", "s.77 · s.51"),
           td("The Chief Executive in Council may make regulations for the whole Ordinance <b>except Parts 5, 5A, 5B and 5C</b>. Regulations for Part 5 are the Commissioner's, and that power cannot be delegated.",
              "行政長官會同行政會議可為整條條例訂立規例，<b>但第5、5A、5B及5C部除外</b>。第5部的規例由關長訂立，而該權力不可轉授。", "s.26(2)", post=flag())),
        tr(rh("Who was deemed licensed", "誰被當作已獲發牌", "s.82(1)–(2)"),
           td("Anyone on the register kept under the old Organized and Serious Crimes Ordinance as a money changer or remittance agent immediately before commencement, for all premises entered on that register.",
              "緊接本條例生效前，名列於舊《有組織及嚴重罪行條例》所備存紀錄冊的貨幣兌換商或匯款代理人，就該紀錄冊所列的所有處所而言。")),
        tr(rh("How long the deemed licence lasted", "當作牌照的有效期", "s.82(3)"),
           td("60 days from commencement. If the person applied for a licence within those 60 days, until the earliest of: the licence being granted, the refusal taking effect, or the application being withdrawn.",
              "自生效日期起計60日。如該人在該60日內申請牌照，則有效至以下最早發生者：牌照獲批給、拒絕批給的決定生效，或申請被撤回。")),
    ], note=B("Part 5 counts a licence deemed granted under section 82 as a licence, so everything in Part 5 applied to those operators from the first day.",
             "第5部把根據第82條當作已批給的牌照視為牌照，故第5部的一切規定由第一天起已適用於該等經營者。") + ' ' + cite_html("s.24"), minw=720)
    + numreq([
        (("60 days", "60日"),
         ("Apply for a licence under section 30 to keep the deemed licence alive", "根據第30條申請牌照，以延續當作牌照的效力"),
         ("A money changer or remittance agent already on the old register when the Ordinance commenced", "本條例生效時已名列舊紀錄冊的貨幣兌換商或匯款代理人"),
         ("The deemed licence expired at the end of the 60 days, so continuing to operate meant operating without a licence", "當作牌照在60日屆滿時失效，其後繼續經營即屬無牌經營"),
         "s.82(3) · s.29"),
    ]))

P7_NAV = [('proof', 'Standard of proof', '舉證準則'), ('prosecute', 'Who prosecutes', '由誰檢控'),
          ('notices', 'How notices reach you', '通知如何送達'), ('privilege', 'What you can hold back', '可保留的資料'),
          ('regs', 'Regulations and transition', '規例與過渡安排')]
P7_BODY = A + B_ + C_ + D_ + E_
