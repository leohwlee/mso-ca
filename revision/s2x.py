# Schedule 2 sections added when the CDD page became the Schedule 2 page:
# thresholds by service, ongoing monitoring, transfers, record keeping, and the
# procedures, prohibitions and branch duties.
from ui import *
from bl_figs import lines_down


def same_h(*cards):
    """Give a row of cards one height (the tallest), so tops and bottoms line up."""
    h = max(c.h for c in cards)
    for c in cards:
        c.h = h


def stack_lbl(cx, y_bottom, en, tc, anchor='middle', pitch=17):
    """A bold edge label; the combined view stacks English over Chinese, bottom line at y_bottom."""
    out = []
    for v, ls in (('en', [en]), ('tc', [tc]), ('both', [en, tc])):
        g = [f'<text class="lbl s-{v}" text-anchor="{anchor}">']
        for i, l in enumerate(ls):
            g.append(f'<tspan x="{cx}" y="{y_bottom - (len(ls) - 1 - i) * pitch:.1f}">{esc(l)}</tspan>')
        g.append('</text>')
        out.append(''.join(g))
    return ''.join(out)


def small_down(x, y_top, en, tc, anchor='start', size=11):
    """Muted tick text hanging below a point; the combined view stacks English over Chinese."""
    size = size * FS
    out = []
    for v, ls in (('en', [en]), ('tc', [tc]), ('both', [en, tc])):
        g = [f'<text class="c-sans s-{v}" font-size="{size}" text-anchor="{anchor}">']
        for i, l in enumerate(ls):
            g.append(f'<tspan x="{x}" y="{y_top + size + i * size * 1.3:.1f}">{esc(l)}</tspan>')
        g.append('</text>')
        out.append(''.join(g))
    return ''.join(out)


PART4 = ("Proceeding without CDD breaches a specified provision: Part 4 discipline, including a pecuniary penalty of up to $10,000,000 or 3 times the profit gained or costs avoided, whichever is greater; and an offence if done knowingly",
         "未執行盡職審查即進行，屬違反指明的條文：可受第4部紀律處分，包括罰款最高為$10,000,000或因該項違反而獲取的利潤或避免的開支的金額的3倍（以金額較大者為準）；明知而違反即屬犯罪")

GL_STD_EN = "not following the Guideline can lead to disciplinary and other action under the AMLO, and the Commissioner must have regard to it when deciding whether Schedule 2 was breached"
GL_STD_TC = "不遵從指引或會招致根據打擊洗錢條例採取的紀律行動及其他行動，而關長在考慮有否違反附表2時須顧及指引"


# ---------------------------------------------------------------- thresholds
def mc(kind, en, tc, cite=None):
    return f'<td class="m-{kind}">{B(en, tc)}{cite_html(cite)}</td>'


MX_KEY = legend([('must', ("full CDD: all four measures, before the transaction", "全面盡職審查：交易前執行全部四項措施")),
                 ('rec', ("a record or identification duty short of full CDD", "未達全面盡職審查的紀錄或身分識別責任")),
                 ('', ("no CDD trigger from the amount alone", "單憑款額不觸發盡職審查"))])

MATRIX = (MX_KEY + '<div class="tbl mx"><table style="min-width:860px"><thead><tr>'
          + th("The service, for a customer with no business relationship", "服務（沒有業務關係的客戶）")
          + th("Under $8,000", "$8,000以下") + th("$8,000 to under $120,000", "$8,000至$120,000以下") + th("$120,000 or more", "$120,000或以上")
          + '</tr></thead><tbody>'
          + tr(rh("Money changing", "貨幣兌換"),
               mc('none', "No trigger from the amount", "款額本身不觸發"),
               mc('none', "No trigger from the amount. There is no $8,000 threshold for money changing", "款額本身不觸發。貨幣兌換並無$8,000門檻"),
               mc('cdd', "Full CDD", "全面盡職審查", "s.3(1)(b) Sch. 2"))
          + tr(rh("A remittance that is not a wire transfer", "並非電傳轉帳的匯款", "s.13 Sch. 2"),
               mc('none', "No trigger from the amount", "款額本身不觸發"),
               mc('rec', "Before the remittance: identify the originator, verify against the identification document, and record the details listed below", "進行匯款前：識別匯款人、根據其識別文件核實身分，並記錄下文所列資料", "s.13(2) Sch. 2 · ¶11.3, 11.6"),
               mc('cdd', "Full CDD, and the remittance record as well", "全面盡職審查，並須備存匯款紀錄", "s.3(1)(b), 13 Sch. 2"))
          + tr(rh("A wire transfer, with you as ordering institution", "電傳轉帳（你是匯款機構）", "s.12 Sch. 2"),
               mc('rec', "No CDD trigger, but record and send the originator's and recipient's names and account or reference numbers", "不觸發盡職審查，但須記錄及附上匯款人及收款人的姓名及戶口號碼或參考編號", "s.12(3), (3A), (5)(b) Sch. 2"),
               mc('cdd', "Full CDD, and the fuller originator information: address, customer or ID document number, or date and place of birth", "全面盡職審查，並附上較完整的匯款人資料：地址、客戶識別號碼或識別文件號碼，或出生日期及地點", "s.3(1A)(a), 12(5)(a) Sch. 2"),
               mc('cdd', "The same as from $8,000", "與$8,000起的規定相同"))
          + tr(rh("A virtual asset transfer, as ordering institution", "虛擬資產轉帳（你是匯款機構）", "s.13A Sch. 2"),
               mc('rec', "No CDD trigger, but obtain, record and submit the same short set of information", "不觸發盡職審查，但須取得、記錄及提交同一組簡略資料", "s.13A(2)–(4) Sch. 2"),
               mc('cdd', "Full CDD, and the full information", "全面盡職審查，並提交完整資料", "s.3(1A)(b), 13A(4)(a) Sch. 2"),
               mc('cdd', "The same as from $8,000", "與$8,000起的規定相同"))
          + tr(rh("Any other occasional transaction, such as buying a cashier order or gift cheque", "任何其他非經常交易，例如購買銀行本票或禮券", "fn 13"),
               mc('none', "No trigger from the amount", "款額本身不觸發"),
               mc('none', "No trigger from the amount", "款額本身不觸發"),
               mc('cdd', "Full CDD", "全面盡職審查", "s.3(1)(b) Sch. 2"))
          + '<tr class="note"><td colspan="4">' + B("<b>At any amount, for any service:</b> suspicion of ML/TF, or doubt about identity information obtained earlier, requires CDD; so does establishing a business relationship.",
                                                     "<b>任何款額、任何服務：</b>懷疑涉及洗錢或恐怖分子資金籌集，或懷疑過往取得的身分資料時，均須執行盡職審查；建立業務關係時亦然。")
          + ' ' + cite_html("s.3(1)(a), (d)–(e) Sch. 2") + ' '
          + B("<b>Linked operations are added together.</b> The link lies in the transactions themselves: for example several payments to the same recipient from one or more sources over a short period, or a customer who regularly transfers funds to one or more destinations. Weigh these factors against the timeframe of the transactions.",
              "<b>有關連的操作須合併計算。</b>關連取決於交易本身的特徵，例如在一段短時間內從同一個或多個來源支付數筆款項給同一收款人，或客戶定期將款項轉帳至一個或多個目的地。決定交易是否有關連時，應將這些因素與進行交易的時間一併考慮。")
          + ' ' + cite_html("s.3(1)(b), (1A) Sch. 2 · ¶4.2.4–4.2.5") + '</td></tr>'
          + '</tbody></table></div>')

THR = sec('thresholds', ["s.3(1), (1A) Sch. 2", "s.12, 13, 13A Sch. 2", ("occasional customers", "非經常客戶")],
          ("Which threshold applies to which service", "哪個門檻適用於哪種服務"),
    P("Every figure in this table is about a customer you have no business relationship with. Find your service on the left and read across to the amount. The key sits above the table because the cell colours carry the answer.",
      "表內每個數字都關乎與你沒有業務關係的客戶。在左邊找出你的服務，再橫向找到款額。圖例置於表上，因為格子的顏色就是答案。")
    + MATRIX
    + table([th("What a remittance record must hold", "匯款紀錄須載有的資料"), th("Compared with a wire transfer record", "與電傳轉帳紀錄比較")], [
        tr(td("The originator's name, identification document number, and the place of issue if that document is a travel document", "匯款人姓名、識別文件號碼；如識別文件是旅行證件，另加發出地方", "s.13(2)(c)(i)–(ii) Sch. 2"),
           td("A wire transfer uses the originator's account or reference number instead, and the ID number is only one option", "電傳轉帳改用匯款人戶口號碼或參考編號，識別號碼只是選項之一")),
        tr(td("The originator's address", "匯款人地址", "s.13(2)(c)(iii) Sch. 2"),
           td("Compulsory in every remittance record, and section 13 itself starts at $8,000. A wire transfer also needs it only from $8,000, and there it is just one of several options", "每份匯款紀錄都必須載有，而第13條本身由$8,000起適用。電傳轉帳亦只在$8,000或以上才須記錄，而且只屬若干選項之一", post=flag())),
        tr(td("The currency and amount", "貨幣及款額", "s.13(2)(c)(iv) Sch. 2"), td("Not a listed item for a wire transfer", "並非電傳轉帳的指定記錄項目")),
        tr(td("The date and time the instructions were received, the recipient's name and address, and the method of delivery", "接獲指示的日期及時間、收款人姓名及地址，以及送遞方式", "s.13(2)(c)(v) Sch. 2"),
           td("A wire transfer records the recipient's name and account or reference number, not the address", "電傳轉帳記錄收款人姓名及戶口號碼或參考編號，而非地址", post=flag())),
    ], minw=760)
    + numreq([
        (("HK$8,000", "8,000元"),
         ("Full CDD before the transaction, plus the full originator information in the message", "在交易前執行全面盡職審查，並在信息內附上完整的匯款人資料"),
         ("An occasional wire transfer or virtual asset transfer, in one operation or several that appear linked", "非經常的電傳轉帳或虛擬資產轉帳，不論以單一次或看來有關連的若干次操作進行"),
         PART4,
         "s.3(1A), 12(5)(a) Sch. 2 · s.5(5), 21 · ¶4.2.1(b)(ii)–(iii)"),
        (("HK$8,000", "8,000元"),
         ("Before carrying out the remittance: identify the originator, verify against the identification document, and record the listed details", "在進行匯款前：識別匯款人、根據其識別文件核實身分，並記錄指定資料"),
         ("A remittance transaction that is not a wire transfer, carried out by a licensed money service operator", "持牌金錢服務經營者進行並非電傳轉帳的匯款交易"),
         ("The duty is itself a specified provision, with the same Part 4 and criminal exposure", "此責任本身即屬指明的條文，同樣可引致第4部紀律處分及刑事責任"),
         "s.13 Sch. 2 · ¶11.3–11.6"),
        (("HK$120,000", "120,000元"),
         ("Full CDD before the transaction", "在交易前執行全面盡職審查"),
         ("Any other occasional transaction, money changing and non-wire remittances included, in one operation or several that appear linked", "任何其他非經常交易（包括貨幣兌換及並非電傳轉帳的匯款），不論以單一次或看來有關連的若干次操作進行"),
         ("The same exposure. Aggregating linked transactions is your duty, not the customer's", "後果相同。合併計算有關連的交易是你的責任，不是客戶的責任"),
         "s.3(1)(b) Sch. 2 · ¶4.2.1(b)(i), 4.2.4"),
        (("HK$120,000", "120,000元"),
         ("Ask for the payer's identity document and keep a copy, to support your ongoing monitoring", "要求付款人提供身分證明文件並將副本存檔，以便持續監察"),
         ("A cash transaction made by a third party whose name is not on the account mandate", "由姓名不在帳戶委託書上的第三方進行的現金交易"),
         ("A Guideline standard, not a specified provision: " + GL_STD_EN, "屬指引的標準，而非指明的條文：" + GL_STD_TC),
         "¶4.2.6 · ¶1.3, 1.8"),
        (("no threshold", "不設門檻"),
         ("Carry out CDD whatever the amount", "不論款額，一律執行盡職審查"),
         ("You suspect ML/TF, or you doubt the truth or adequacy of identity information obtained earlier", "你懷疑涉及洗錢或恐怖分子資金籌集，或懷疑過往取得的身分資料是否真實或充分"),
         ("The thresholds are no defence here, and the suspicion also calls for a report to the JFIU", "門檻在此不能作為辯解；有關懷疑亦須向財富情報組報告"),
         "s.3(1)(d)–(e) Sch. 2 · ¶4.2.1(c)–(d) · fn 15"),
    ])
    + traps(
        trap(("$8,000 means two different things", "$8,000有兩種不同意思"), None, "s.3(1A), 13 Sch. 2 · ¶4.2.4, 8.4",
             vs=[(("A wire transfer", "電傳轉帳"), ("$8,000 triggers full CDD: all four measures.", "$8,000即觸發全面盡職審查：全部四項措施。")),
                 (("A remittance that is not a wire transfer", "並非電傳轉帳的匯款"), ("$8,000 triggers the remittance duty: identify, verify by ID document, record. Full CDD waits for $120,000.", "$8,000觸發匯款責任：識別、以識別文件核實、記錄。全面盡職審查要到$120,000才觸發。"))]),
        trap(("Exactly $8,000 is caught", "剛好$8,000亦包括在內"),
             ("Schedule 2 and the Guideline say 'equal to or above $8,000', so a wire transfer or remittance of exactly $8,000 is caught.",
              "附表2及指引均寫明「相等於$8,000或以上」，因此剛好$8,000的電傳轉帳或匯款亦包括在內。"),
             "s.12(5)(a), 13(1) Sch. 2 · ¶10.5"),
        trap(("A wire transfer's record duty has no floor", "電傳轉帳的紀錄責任不設下限"),
             ("Below $8,000 you still record and send four items. The threshold only adds the fifth: address, customer or ID document number, or date and place of birth.",
              "即使在$8,000以下，你仍須記錄及附上四項資料。門檻只是加上第五項：地址、客戶識別號碼或識別文件號碼，或出生日期及地點。"),
             "s.12(3), (3A) Sch. 2"),
    ))


# ---------------------------------------------------------------- monitoring
def fig_monitor():
    W = 1000
    M1 = Card(20, 222, ("Review the file", "覆核資料"), ("Keep your documents, data and information up to date and relevant", "不時覆核文件、數據及資料，確保反映現況及仍屬相關"), cite="s.5(1)(a) Sch. 2")
    M2 = Card(268, 222, ("Scrutinise transactions", "審查交易"), ("Against what you know of the customer, its business, risk profile and source of funds", "對照你對客戶、其業務及風險狀況，以及資金來源的認知"), cite="s.5(1)(b) Sch. 2")
    M3 = Card(516, 222, ("Spot the unusual", "識辨異常交易"), ("Complex, unusually large or unusually patterned, with no apparent economic or lawful purpose", "複雜、款額或模式異乎尋常，而且並無明顯經濟或合法目的"), cite="s.5(1)(c) Sch. 2")
    M4 = Card(764, 222, ("If found: examine and record", "如發現：審查並以書面記錄"), ("Examine its background and purpose, and set out the findings in writing", "審查其背景及目的，並藉書面列明審查所得"), 'must', "s.5(1)(c) Sch. 2", answer=True)
    same_h(M1, M2, M3, M4)
    H = place([([M1, M2, M3, M4], 0)], y0=16)
    b = [n.render() for n in (M1, M2, M3, M4)]
    m = 's2m'
    for a, c in ((M1, M2), (M2, M3), (M3, M4)):
        b.append(edge([a.right, c.left], mid=m))
    ly = H + 24
    b.append(edge([M4.bottom, (M4.cx, ly), (M1.cx, ly), M1.bottom], mid=m))
    b.append(label((M1.cx + M4.cx) / 2, ly + 20, ("and again: the duty is continuous", "周而復始：責任是持續的")))
    aria = ("Continuous monitoring as a loop: review the customer file to keep it up to date and relevant, scrutinise transactions against what you know of the customer, spot complex, unusually large or unusually patterned transactions with no apparent purpose, examine them and set out the findings in writing, and start again.",
            "持續監察的循環：覆核客戶資料以確保反映現況及仍屬相關，對照你對客戶的認知審查交易，識辨複雜、款額異常或模式異常而並無明顯目的的交易，審查並藉書面列明審查所得，然後周而復始。")
    return svg(W, ly + 32, ''.join(b), aria, m, 820)


MON = sec('monitoring', ["s.5–6 Sch. 2", "Ch. 5", "¶4.12"],
          ("Ongoing monitoring, and customers from before 2012", "持續監察，以及2012年前的客戶"),
    P("Read the loop left to right, then back along the bottom: monitoring never finishes. The tables below cover when it must go further, and how customers who predate the Ordinance are caught.",
      "由左至右閱讀循環，再沿底部返回：監察永不終止。下列表格說明何時須加強監察，以及條例生效前已有的客戶如何受規管。")
    + fig(fig_monitor, ("Keeping CDD information up to date does not mean verifying a verified identity again, unless doubts arise about it. A dormant customer's file needs no periodic review, but it does need one when the relationship reactivates.",
                          "確保盡職審查資料反映現況，並不表示須再次核實已核實的身分，除非對其有所懷疑。不動客戶的盡職審查資料毋須定期覆核，但當該關係重新活躍起來時便應進行覆核。"),
          legend([('', ("a step in the loop", "循環中的步驟")), ('must', ("the step that must leave a written record", "必須留下書面紀錄的步驟"))]))
    + table([th("When monitoring must go further", "何時須加強監察"), th("What you must add", "須加上甚麼"), th("Unless", "除非")], [
        tr(rh("The customer was not physically present for identification", "客戶沒有為身分識別的目的而現身", "s.5(3)(a) Sch. 2"),
           td("Additional measures to compensate for the risk this creates", "採取額外措施，以應對由此引致的風險"),
           td("You identified and verified the customer through a recognized digital identification system", "你以認可數碼識別系統識別及核實了客戶身分", "s.5(4) Sch. 2")),
        tr(rh("The customer or a beneficial owner is known to be a PEP", "已知客戶或實益擁有人屬政治人物", "s.5(3)(b) Sch. 2"),
           td("The same additional measures", "同樣的額外措施"),
           td("It is a former PEP who, on an appropriate risk assessment, does not present a high risk", "屬前政治人物，而基於適當風險評估，不會造成高度風險", "s.5(5) Sch. 2", post=flag())),
        tr(rh("The customer or a beneficial owner is in a high-risk situation under section 15", "客戶或實益擁有人涉及第15條所指的高風險情況", "s.5(3)(c) Sch. 2"),
           td("The same additional measures", "同樣的額外措施"), td("No exception", "沒有例外")),
    ], minw=760)
    + table([th("A pre-existing customer: one whose relationship began before 1 April 2012", "先前客戶：在2012年4月1日前已建立業務關係的客戶"), th("What you must do", "須做甚麼")], [
        tr(td("A transaction that is unusual or suspicious because of its amount or nature", "因款額或性質而屬異乎尋常或可疑的交易", "s.6(1)(a)(i) Sch. 2"), td("Carry out CDD", "執行盡職審查")),
        tr(td("A transaction inconsistent with what you know of the customer, its business or risk profile, or its source of funds", "與你對客戶、其業務或風險狀況，或其資金來源的認知不符的交易", "s.6(1)(a)(ii) Sch. 2"), td("Carry out CDD", "執行盡職審查")),
        tr(td("A material change in the way the account is operated", "戶口的操作模式出現相當程度的轉變", "s.6(1)(b) Sch. 2"), td("Carry out CDD", "執行盡職審查")),
        tr(td("Suspicion of ML/TF, or doubt about earlier identity information, as for any customer", "懷疑涉及洗錢或恐怖分子資金籌集，或懷疑過往的身分資料，與任何客戶相同", "s.3(1)(d)–(e) Sch. 2"), td("Carry out CDD", "執行盡職審查")),
        tr(td("Trigger events the Guideline gives as examples: a dormant account is re-activated, or the account's beneficial ownership or control changes. You must also consider trigger events specific to your own customers and business", "指引列舉的觸發事件例子：把不動戶口重新活躍起來，或戶口的實益擁有權或控制權有變。你亦須考慮本身客戶及業務特有的其他觸發事件", "¶4.12.2"),
           td("Treat them as trigger events for CDD. Not the same as the file review a reactivated dormant customer gets under ongoing monitoring", "視為須執行盡職審查的觸發事件。這有別於不動客戶恢復活躍時在持續監察下進行的資料覆核", post=flag())),
        tr(td("You cannot complete CDD in any of these cases", "在上述任何情況下未能完成盡職審查", "s.6(2) Sch. 2"), td("End the relationship as soon as reasonably practicable", "在合理地切實可行範圍內盡快終止業務關係")),
    ], note=B("Before a pre-existing customer's first CDD under the Schedule, reviewing the file means reviewing only what you hold at the time of the review.", "在按附表首次就先前客戶執行盡職審查之前，覆核資料只須覆核你在覆核時持有的資料。") + ' ' + cite_html("s.5(2) Sch. 2"), minw=720)
    + numreq([
        (("at least yearly", "最少每年一次"),
         ("Review the customer's CDD records to confirm they are up to date and still relevant", "覆核該客戶的盡職審查紀錄，確認資料反映現況及仍屬相關"),
         ("The customer presents high ML/TF risk; review more often if you judge it necessary. Schedule 2 itself says only 'from time to time'", "客戶構成高洗錢或恐怖分子資金籌集風險；如認為有需要應更頻密覆核。附表2本身只規定「不時」覆核"),
         ("Falls short of the Guideline's minimum. Not following the Guideline can lead to disciplinary and other action under the AMLO, and may also reflect adversely on the fitness and properness of the sole proprietor, partners, directors and ultimate owner",
          "未達指引的最低要求。不遵從指引或會招致根據打擊洗錢條例採取的紀律行動及其他行動，亦將對獨資經營者、合夥人、董事和最終擁有人作為適當人選帶有負面影響"),
         "¶5.3 · s.5(1)(a) Sch. 2 · ¶1.3"),
        (("1 April 2012", "2012年4月1日"),
         ("The cut-off date that makes a customer pre-existing", "界定先前客戶的分界日期"),
         ("Relationships a money service operator established before that date", "金錢服務經營者在該日期前建立的業務關係"),
         ("A trigger event then requires CDD, and failing that the relationship must end", "其後如出現觸發事件即須執行盡職審查，未能完成則須終止關係"),
         "s.1, 6 Sch. 2"),
    ])
    + traps(
        trap(("Simplified or enhanced, monitoring never switches off", "不論簡化或更嚴格，監察從不停止"),
             ("Simplified due diligence lightens the four measures, but the duty to monitor never falls away: you must still continuously monitor every business relationship (ongoing CDD and transaction monitoring). What changes with the risk is the extent: you may reduce it in low-risk situations, for example by reducing the monitoring and scrutiny of transactions under a reasonable monetary threshold, and you should enhance it where the risk is high.",
              "簡化盡職審查減輕四項措施，但監察責任並不因此消失：你仍須持續監察每段業務關係（即持續進行盡職審查及監察交易）。隨風險改變的是監察程度：在低風險的情況下可下調監察的程度，例如下調持續監察和審查合理的金額門檻下的交易的程度；風險屬於高度時則應更嚴格執行交易監察。"),
             "s.4–5 Sch. 2 · ¶4.8.6, 4.8.8(d) · ¶5.9"),
    ))


# ---------------------------------------------------------------- transfers
def fig_wire():
    W = 1000
    LX, LW = 20, 250          # the chain, top to bottom
    RX, RW = 320, 660         # each institution's duty, beside it
    ORIG = Card(LX, LW, ("Originator", "匯款人"), ("Whose account pays; with no account, whoever gives the instruction", "付款戶口的持有人；如沒有戶口，則指發出指示的人"), cite="s.12(11) Sch. 2")
    ORD = Card(LX, LW, ("Ordering institution", "匯款機構"), ("Usually you, sending the transfer", "通常是你，負責發出轉帳"))
    INT = Card(LX, LW, ("Intermediary institution", "中介機構"), ("Any institution in between, if there is one", "其間的任何機構（如有）"))
    BEN = Card(LX, LW, ("Beneficiary institution", "收款機構"), ("Makes the money available to the recipient", "向收款人提供款項"))
    REC = Card(LX, LW, ("Recipient", "收款人"), None)
    DORD = Card(RX, RW, ("Before sending: record, then include in the message", "發出前：記錄，並附於信息內"),
                ("Always the originator's name and account or reference number, and the recipient's name and account or reference number. From $8,000, also the originator's address, customer or ID document number, or date and place of birth, and the originator information must be accurate",
                 "一律附上匯款人及收款人各自的姓名及戶口號碼或參考編號。由$8,000起，另須附上匯款人地址、客戶識別號碼或識別文件號碼，或出生日期及地點，而所附匯款人資料必須準確"),
                'must', "s.12(3), (3A), (5) Sch. 2 · ¶10.8", answer=True)
    DINT = Card(RX, RW, ("Pass everything on", "全部傳遞"),
                ("All the information received with the transfer goes to the next institution. In a transfer that is not domestic, also chase anything missing, as the beneficiary institution does",
                 "收到的所有資料須傳遞予下一間機構；非本地電傳轉帳亦須像收款機構一樣追補遺漏資料"),
                'must', "s.12(8), (10) Sch. 2", answer=True)
    DBEN = Card(RX, RW, ("Chase what is missing", "追補遺漏資料"),
                ("Obtain it from the institution that sent the transfer, as soon as reasonably practicable: in a domestic transfer, a missing originator account or reference number; in any other, any missing required information. If it cannot be obtained, consider restricting or ending the relationship with that institution, or take reasonable measures to mitigate the risk",
                 "在合理地切實可行範圍內盡快向發出轉帳指示的機構取得：本地電傳轉帳為遺漏的匯款人戶口號碼或參考編號；其他轉帳為任何遺漏的所需資料。如未能取得，考慮限制或結束與該機構的業務關係，或採取合理措施減低風險"),
                'must', "s.12(9)–(10) Sch. 2", answer=True)

    DOM = Card(20, 360, ("Domestic transfer shortcut", "本地轉帳的簡便安排"),
               ("When every institution is a financial institution in Hong Kong, the message may carry only the originator's account or reference number, if it permits traceability. Supply the rest of the originator information you recorded within 3 business days of a request from the next institution or the Commissioner",
                "如所有機構均為位於香港的金融機構，信息可只附匯款人的戶口號碼或參考編號，但須可用作追蹤轉帳。如下一間機構或關長提出要求，須在3個營業日內提供其餘已記錄的匯款人資料"),
               'may', "s.12(6) Sch. 2 · ¶10.11–10.12")
    BAT = Card(410, 270, ("Batch file shortcut", "群組檔案的簡便安排"),
               ("Several transfers from one originator to recipients outside Hong Kong: each carries the originator's account or reference number, and the batch file carries all the recorded information",
                "同一匯款人發給香港以外收款人的多項轉帳：每項轉帳只附匯款人戶口號碼或參考編號，全部已記錄資料則載於群組檔案"),
               'may', "s.12(7) Sch. 2")
    EXE = Card(710, 270, ("Outside section 12 altogether", "完全不受第12條規管"),
               ("Transfers between two financial institutions, or with a foreign institution, each acting for itself; card payments that are not person-to-person and carry the card number",
                "兩間金融機構之間或與外地機構之間、各自只代表本身進行的轉帳；並非人對人並附有咭號的咭類付款"),
               'ok', "s.12(2) Sch. 2")
    same_h(DOM, BAT, EXE)
    GAP = 30
    H = place([([ORIG], GAP), ([ORD, DORD], GAP), ([INT, DINT], GAP), ([BEN, DBEN], GAP), ([REC], 56), ([DOM, BAT, EXE], 0)])
    b = [n.render() for n in (ORIG, ORD, INT, BEN, REC, DORD, DINT, DBEN, DOM, BAT, EXE)]
    m = 's2w'
    for a, c in ((ORIG, ORD), (ORD, INT), (INT, BEN), (BEN, REC)):
        b.append(edge([a.bottom, c.top], mid=m))
    for a, c in ((ORD, DORD), (INT, DINT), (BEN, DBEN)):
        b.append(edge([a.right, c.left], mid=m))
    sy = REC.y + REC.h + 28   # a rule sets the options band apart from the chain
    b.append(f'<line class="e" x1="20" y1="{sy:.0f}" x2="{W - 20}" y2="{sy:.0f}" stroke-dasharray="5 5"/>')
    aria = ("A wire transfer runs from the originator to the ordering institution, through any intermediary institutions, to the beneficiary institution and the recipient. The ordering institution records and includes the originator's and recipient's names and account or reference numbers, adding the originator's address or identity number or date and place of birth from $8,000, when the originator information must also be accurate. An intermediary passes everything on and, in a transfer that is not domestic, chases missing information. A beneficiary institution chases missing information from the sending institution and, failing that, considers restricting or terminating the relationship with that institution, or takes reasonable measures to mitigate the risk. Below the chain: the ordering institution's two shortcuts, a domestic transfer carrying only the originator's account or reference number with the rest supplied within three business days of a request, and a batch file; and the transfers outside section 12.",
            "電傳轉帳由匯款人經匯款機構、任何中介機構，到達收款機構及收款人。匯款機構記錄並附上匯款人及收款人的姓名及戶口號碼或參考編號，$8,000起另加匯款人地址、識別號碼或出生日期及地點，而所附匯款人資料必須準確。中介機構須傳遞全部資料，如屬非本地電傳轉帳亦須追補遺漏資料。收款機構須向發出轉帳指示的機構追補遺漏資料；如未能取得，須考慮限制或結束與該機構的業務關係，或採取合理措施減低風險。鏈下方為匯款機構的兩項簡便安排：本地轉帳可只附匯款人戶口號碼或參考編號，其餘資料在接獲要求後三個營業日內提供；以及群組檔案；另有不受第12條規管的轉帳。")
    return svg(W, H + 14, ''.join(b), aria, m, 860)


TRN = sec('transfers', ["s.12, 13, 13A Sch. 2", "Ch. 10–11", "¶10.2"],
          ("Wire transfers, remittances and virtual asset transfers", "電傳轉帳、匯款及虛擬資產轉帳"),
    P("Read the left column top to bottom: it is the path of a wire transfer. The red box beside each institution is its duty. Below the dashed line are the ordering institution's two shortcuts and the transfers outside section 12. When you pay your own supplier or receive money for yourself, you are the originator or recipient, not an institution in the chain, and none of this applies.",
      "由上至下閱讀左欄：這是電傳轉帳的路徑。每間機構旁邊的紅色方格是其責任。虛線以下是匯款機構的兩項簡便安排，以及不受第12條規管的轉帳。當你為自己付款予供應商或自行收款時，你是匯款人或收款人，並非鏈中的機構，上述規定一概不適用。")
    + fig(fig_wire, ("The chain works only if every link does its part: the information you attach as ordering institution is what the next institution checks, and what it must chase if it is missing.",
                       "每一環節須各盡其責：你作為匯款機構所附的資料，正是下一間機構要核對、如有遺漏便須追補的資料。"),
          legend([('', ("a party in the chain", "鏈中的一方")), ('must', ("a duty on that institution", "該機構的責任")),
                  ('may', ("an option the ordering institution may use", "匯款機構可採用的安排")), ('ok', ("outside the section", "不受本條規管"))]))
    + table([th("Your role in the transfer", "你在轉帳中的角色"), th("Procedures to spot transfers lacking information", "識辨欠缺資料的轉帳的程序"),
             th("When the information is missing, incomplete or meaningless", "資料遺漏、不完整或不具意義時"), th("Also", "另須")], [
        tr(rh("Ordering institution: you send it", "匯款機構：由你發出", "s.19(2) Sch. 2"),
           td("Safeguards against sending a non-compliant transfer: reasonable measures, such as regular review or testing by internal control or audit, to spot domestic or cross-border transfers lacking required information; risk-based policies for handling them; and timely fixes for control deficiencies", "設有防止發出不合規轉帳的保障措施：採取合理措施（例如定期覆核或藉內部管控或審計職能進行測試），識辨欠缺所需資料的本地或跨境電傳轉帳；設有處理這些轉帳的風險為本政策；並適時糾正管控不足之處", "¶10.13"),
           td("Do not let it go out without the required information", "不讓欠缺所需資料的轉帳發出", "s.12(5) Sch. 2 · ¶10.13"),
           td("From $8,000 the originator information must be accurate, and an occasional originator's identity verified. On the domestic shortcut, law enforcement agencies should get the full originator information immediately on request", "$8,000起所附匯款人資料必須準確，並須核實非經常客戶匯款人的身分。採用本地轉帳簡便安排時，應按執法機構要求立即提供全部匯款人資料", "¶10.8–10.9, 10.12")),
        tr(rh("Intermediary institution", "中介機構", "s.19(2) Sch. 2"),
           td("Reasonable measures, consistent with straight-through processing, to spot cross-border transfers lacking required information; risk-based policies on when to execute, reject or suspend such a transfer, and on the follow-up", "採取與直通式處理程序一致的合理措施，識辨欠缺所需資料的跨境電傳轉帳；設有風險為本政策，以斷定何時執行、拒絕或暫停這類轉帳，以及適當的跟進行動", "¶10.16"),
           td("Only in a transfer that is not domestic: obtain what is missing from the sending institution as soon as reasonably practicable; failing that, consider restricting or ending that relationship, or mitigate; and if the information is incomplete or meaningless, mitigate", "只限非本地電傳轉帳：在合理地切實可行範圍內盡快向發出轉帳指示的機構取得遺漏資料；如未能取得，考慮限制或結束與該機構的業務關係，或減低風險；如資料不完整或不具意義，亦須減低風險", "s.12(10) Sch. 2 · ¶10.17–10.18", post=flag()),
           td("Pass on everything received. If technical limits stop the information travelling between a cross-border transfer and a related domestic one, you should keep a record of all the information received for at least 5 years", "傳遞收到的全部資料。如因技術限制而未能在跨境轉帳與相關本地轉帳之間保留資料，應把收到的所有資料存檔至少5年", "s.12(8) Sch. 2 · ¶10.14–10.15")),
        tr(rh("Beneficiary institution", "收款機構", "s.19(2) Sch. 2"),
           td("Reasonable measures, such as post-event monitoring, to spot domestic or cross-border transfers lacking required information; risk-based policies on when to execute, reject or suspend such a transfer, and on the follow-up", "採取合理措施（例如事後監察），識辨欠缺所需資料的本地或跨境電傳轉帳；設有風險為本政策，以斷定何時執行、拒絕或暫停這類轉帳，以及適當的跟進行動", "¶10.19"),
           td("Obtain what is missing from the sending institution as soon as reasonably practicable; failing that, consider restricting or ending that relationship, or mitigate. For a domestic transfer the statute names only the originator's account or reference number; ¶10.20 words the duty for any required information, domestic or cross-border. Incomplete or meaningless information: mitigate", "在合理地切實可行範圍內盡快向發出轉帳指示的機構取得遺漏資料；如未能取得，考慮限制或結束與該機構的業務關係，或減低風險。就本地電傳轉帳，條例只指明匯款人戶口號碼或參考編號；第10.20段則把責任寫成涵蓋本地或跨境轉帳的任何所需資料。資料不完整或不具意義：減低風險", "s.12(9)–(10) Sch. 2 · ¶10.20–10.21", post=flag()),
           td("From $8,000, verify the recipient's identity if it has not been verified before", "就$8,000或以上的轉帳，如未曾核實收款人的身分，便應加以核實", "¶10.22")),
    ], note=B("Follow these requirements in every jurisdiction where you operate, directly or through agents, according to your role in the transfer.", "你應就在電傳轉帳中擔當的角色，在直接營運或通過代理人營運的每個司法管轄區遵從這些規定。") + ' ' + cite_html("¶10.1"), minw=980)
    + table([th("", ""), th("Wire transfer", "電傳轉帳"), th("Remittance transaction, not a wire transfer", "匯款交易（並非電傳轉帳）"), th("Virtual asset transfer", "虛擬資產轉帳")], [
        tr(rh("What it is", "是甚麼"),
           td("An institution, by electronic means, makes money available at an institution", "機構藉電子方式，將款項轉往某機構提供予收款人", "s.1(4) Sch. 2"),
           td("Sending, or arranging to send, money to a place outside Hong Kong", "將金錢或安排將金錢送往香港以外地方", "s.13(3) Sch. 2"),
           td("An institution transfers virtual assets to make them available at an institution", "機構轉出虛擬資產，以供在某機構提供予收款人", "s.13A(1) Sch. 2")),
        tr(rh("Who it binds", "約束誰"),
           td("Any financial institution acting as ordering, intermediary or beneficiary institution", "任何以匯款、中介或收款機構身分行事的金融機構"),
           td("A licensed money service operator, and only from $8,000", "持牌金錢服務經營者，而且只在$8,000或以上適用", post=flag()),
           td("Any financial institution acting in the chain", "任何在鏈中行事的金融機構")),
        tr(rh("The identity check", "身分核實"),
           td("Full CDD from $8,000 for an occasional customer", "非經常客戶由$8,000起須執行全面盡職審查", "s.3(1A)(a) Sch. 2"),
           td("Before the remittance: identify the originator and verify against the identification document", "進行匯款前：識別匯款人，並根據其識別文件核實身分", "s.13(2)(a)–(b) Sch. 2"),
           td("Full CDD from $8,000 for an occasional customer", "非經常客戶由$8,000起須執行全面盡職審查", "s.3(1A)(b) Sch. 2")),
        tr(rh("Does the information travel?", "資料是否隨轉帳傳遞？"),
           td("Yes: in the message or payment form accompanying the transfer", "是：附於隨轉帳的信息或付款表格內"),
           td("No: it is a record you keep", "否：屬你備存的紀錄"),
           td("Yes: submitted to the beneficiary institution under published codes and guidelines", "是：按已公布的守則及指引提交予收款機構")),
        tr(rh("Procedures you must have", "須設立的程序"),
           td("For identifying and handling transfers that lack the required information", "識辨及處理欠缺所需資料的轉帳", "s.19(2) Sch. 2"),
           td("No specific procedures duty in section 19: section 19(3) covers only the duties under sections 3, 4, 5, 9, 10 and 15, and section 13 is not among them", "第19條並無針對匯款交易的特定程序規定：第19(3)條只涵蓋第3、4、5、9、10及15條所指的責任，並不包括第13條", "s.19(3) Sch. 2", post=flag()),
           td("For identifying and handling transfers that lack the required information", "識辨及處理欠缺所需資料的轉帳", "s.19(2A) Sch. 2")),
    ], minw=860, cls='cmp')
    + numreq([
        (("3 business days", "3個營業日"),
         ("Supply the originator information a domestic wire transfer left out: the name and, from $8,000, the address, customer or ID document number, or date and place of birth. Law enforcement agencies should get it immediately on request", "提供本地電傳轉帳所略去的匯款人資料：姓名，以及$8,000起的地址、客戶識別號碼或識別文件號碼，或出生日期及地點。如執法機構要求，應立即提供"),
         ("You used the domestic shortcut, and the next institution or the Commissioner asks", "你採用了本地轉帳的簡便安排，而下一間機構或關長提出要求"),
         ("A breach of a specified provision. Business days exclude public holidays and gale or black rainstorm warning days", "屬違反指明的條文。營業日不包括公眾假日，以及烈風或黑色暴雨警告日"),
         "s.12(3A), (6) Sch. 2 · Sch. 1 Pt 2 · ¶10.12"),
        (("as soon as reasonably practicable", "在合理地切實可行範圍內盡快"),
         ("Obtain missing information from the sending institution, or mitigate information that is incomplete or meaningless", "向發出轉帳指示的機構取得遺漏資料，或就不完整或不具意義的資料減低風險"),
         ("You are the beneficiary institution in a domestic transfer and the originator's account or reference number is missing; or the beneficiary or an intermediary institution in a transfer that is not domestic and any required information is missing", "你是本地電傳轉帳中的收款機構，而匯款人戶口號碼或參考編號遺漏；或是非本地電傳轉帳中的收款機構或中介機構，而任何所需資料遺漏"),
         ("A breach of a specified provision. If the information still cannot be obtained, consider restricting or ending the relationship with the sending institution, or take reasonable measures to mitigate the risk", "屬違反指明的條文。如仍未能取得資料，須考慮限制或結束與發出轉帳指示機構的業務關係，或採取合理措施減低風險"),
         "s.12(9)–(10) Sch. 2"),
    ])
    + traps(
        trap(("Who must chase: the intermediary only across borders", "誰須追補：中介機構只限跨境轉帳"), None, "s.12(9)–(10) Sch. 2 · ¶10.16–10.20",
             vs=[(("Intermediary institution", "中介機構"), ("Chases missing information only in a transfer that is not domestic, and spots such transfers with measures consistent with straight-through processing.", "只在非本地電傳轉帳中追補遺漏資料，並以與直通式處理程序一致的措施識辨這類轉帳。")),
                 (("Beneficiary institution", "收款機構"), ("Chases in domestic and cross-border transfers alike, and may spot the gaps after the event, by post-event monitoring.", "本地及跨境轉帳均須追補，並可藉事後監察識辨遺漏。"))]),
        trap(("The same originator, two definitions that match", "同一匯款人，兩項相同的定義"),
             ("For both a wire transfer and a remittance, the originator is the person whose account with you pays for it or, with no account, the person who instructs you. The recipient is not your customer unless you have some other relationship with them.",
              "不論是電傳轉帳或匯款，匯款人都是在你處開立戶口並以該戶口付款的人；如沒有戶口，則為向你發出指示的人。收款人除非與你另有關係，否則並非你的客戶。"),
             "s.12(11), 13(3) Sch. 2 · ¶4.1.5"),
    ))


# ---------------------------------------------------------------- records
def fig_records():
    W = 1000
    L1 = Card(20, 320, ("Each transaction", "每項交易"), ("Documents, data and information obtained in connection with it, kept even if the relationship ends", "與每項交易有關而取得的文件、數據及資料；即使業務關係在期間終止，仍須備存"), cite="s.20(1)(a), (2) Sch. 2")
    L2 = Card(20, 320, ("Customers in a relationship", "業務關係中的客戶"), ("Identity and verification records for the customer and any beneficial owner; account files; business correspondence", "客戶及任何實益擁有人的身分識別及核實紀錄；戶口檔案；業務通訊"), cite="s.20(1)(b), (3) Sch. 2")
    L3 = Card(20, 320, ("Occasional customers", "非經常客戶"), ("Customer records, when an occasional transaction reaches a CDD threshold", "非經常交易達盡職審查門檻時的客戶紀錄"), cite="s.20(3A) Sch. 2")
    same_h(L1, L2, L3)
    H = place([([L1], 22), ([L2], 22), ([L3], 0)], y0=16)
    b = [n.render() for n in (L1, L2, L3)]
    m = 's2r'
    X0, X1, L = 400, 655, 285     # trigger, end of relationship, and one length for every 5-year bar

    def bar(x1, x2, y, cls):
        return f'<rect class="{cls}" x="{x1}" y="{y - 7}" width="{x2 - x1}" height="14" rx="3"/>'

    def tick(x, y, en, tc):
        return (f'<line class="e" x1="{x}" y1="{y - 13}" x2="{x}" y2="{y + 13}"/>'
                + small_down(x - 2, y + 12, en, tc))

    def five(x, y, en, tc):
        # the red minimum period, with an arrow past its end: "at least"
        return (bar(x, x + L, y, 'bar') + edge([(x + L, y), (x + L + 26, y)], mid=m)
                + stack_lbl(x + L / 2, y - 14, en, tc))

    y1, y2, y3 = L1.cy, L2.cy, L3.cy
    b += [five(X0, y1, "at least 5 years from completion", "自交易完成起最少5年"),
          tick(X0, y1, "transaction completed", "交易完成")]
    b += [bar(X0, X1, y2, 'bar-soft'), stack_lbl((X0 + X1) / 2, y2 - 14, "kept throughout", "在關係存續期間備存"),
          five(X1, y2, "at least 5 years after it ends", "關係終止後最少5年"),
          tick(X0, y2, "relationship begins", "業務關係開始"), tick(X1, y2, "relationship ends", "業務關係終止")]
    b += [five(X0, y3, "at least 5 years from completion", "自交易完成起最少5年"),
          tick(X0, y3, "transaction completed", "交易完成")]
    aria = ("Three retention clocks, each red bar the same five years. Records of each transaction: at least five years from completion, even if the relationship ends meanwhile. Customer records in a business relationship: kept throughout the relationship and for at least five years after it ends, so they run longest. Customer records for an occasional transaction at a CDD threshold: at least five years from completion.",
            "三個備存時限，每條紅色橫條都代表同樣的五年。每項交易的紀錄：自交易完成起最少五年，即使業務關係在期間終止。業務關係中的客戶紀錄：在關係存續期間備存，並在關係終止後最少五年，因此備存最久。達盡職審查門檻的非經常交易的客戶紀錄：自交易完成起最少五年。")
    return svg(W, H + 20, ''.join(b), aria, m, 820)


REC = sec('records', ["s.20–21 Sch. 2", "Ch. 8", ("with ¶9.7", "另及第9.7段")],
          ("Record keeping: what, how long, and in what form", "備存紀錄：甚麼、多久、以甚麼形式"),
    P("Each lane is one kind of record, and every red bar is the same five years. What to learn is where it starts: from the transaction for transaction records, and for customer records from the end of the relationship, or from completion for an occasional customer's records. The arrow at the end of each bar means at least.",
      "每一行是一類紀錄，每條紅色橫條都是同樣的五年。要記的是它從何時開始計算：交易紀錄由交易起計；客戶紀錄由業務關係終止起計，非經常客戶的紀錄則由交易完成起計。橫條末端的箭頭表示「最少」。")
    + fig(fig_records, ("A written notice from the Commissioner can require any of these records to be kept for longer, where they are relevant to an ongoing investigation or to another purpose the notice states; keeping them for that period is then itself a specified provision.",
                          "關長可藉書面通知，要求把與正在進行的調查或通知所述其他目的相關的紀錄保存較長時間；遵從該期間本身即屬指明的條文。"),
          legend([('must', ("the minimum period after the trigger", "觸發事件後的最短期間")), ('', ("kept while the relationship lasts", "在關係存續期間備存"))]))
    + table([th("If the record is", "如紀錄是"), th("Keep it as", "須以下列形式備存")], [
        tr(td("A document", "文件", "s.21(a) Sch. 2"), td("The <b>original</b>; or a <b>copy on microfilm or in a computer database</b>", "<b>正本</b>；或<b>以微縮影片或電腦數據庫備存的複本</b>", post=flag())),
        tr(td("Data or information", "數據或資料", "s.21(b) Sch. 2"), td("A record of it on microfilm or in a computer database", "以微縮影片或電腦數據庫備存的紀錄")),
    ], note=B("You should also ensure that all CDD information and transaction records are available swiftly to the Commissioner, other authorities and auditors upon appropriate authority. The Licensing Guide requires every applicant to have a local place for storage of books and records in Hong Kong: a physical place, under the licensee's control, for keeping the full set of books and records of its money service transactions.", "你亦應確保迅速地為有適當授權的關長、其他機構及核數師提供所有盡職審查資料及交易紀錄。《牌照指引》規定所有申請人必須有香港的本地儲存帳目及紀錄地點，即由持牌人控制、用作儲存完整金錢服務交易帳目及紀錄的實體地點。") + ' ' + cite_html(("¶8.2(b) · Licensing Guide ¶4.10–4.11", "第8.2(b)段 · 《牌照指引》第4.10至4.11段")), minw=620)
    + numreq([
        (("at least 5 years", "最少5年"),
         ("Keep the transaction records", "備存交易紀錄"),
         ("From the date the transaction is completed, whether or not the relationship ends in that time", "自交易完成之日起計，不論業務關係是否在該段期間內終止"),
         ("Record keeping is a specified provision, so a gap carries Part 4 discipline and, if knowing, an offence", "備存紀錄屬指明的條文，出現缺口可引致第4部紀律處分；明知而為即屬犯罪"),
         "s.20(1)(a), (2) Sch. 2 · ¶8.5–8.6"),
        (("at least 5 years", "最少5年"),
         ("Keep the customer records: identity and verification, account files, business correspondence", "備存客戶紀錄：身分識別及核實、戶口檔案、業務通訊"),
         ("Throughout the relationship, then from the date it ends. For an occasional transaction at a CDD threshold ($8,000 for wire and virtual asset transfers, $120,000 for any other), from the date it is completed", "在業務關係存續期間，其後自關係終止之日起計。如屬達盡職審查門檻的非經常交易（電傳轉帳及虛擬資產轉帳為$8,000，其他交易為$120,000），則自交易完成之日起計"),
         ("The same exposure, and an intermediary you relied on must be able to hand copies over within the same period", "後果相同；你所依賴的中介人亦須能在同一期間內交出複本"),
         "s.20(1)(b), (3), (3A), 18(4)(b) Sch. 2 · ¶8.4"),
        (("longer, by notice", "按通知延長"),
         ("Keep the specified records for the period the notice sets", "按通知所訂期間備存指明紀錄"),
         ("The Commissioner gives written notice because the records bear on an investigation or another stated purpose", "關長因該等紀錄與調查或其他所述目的相關而發出書面通知"),
         ("Breaching the notice is itself a breach of a specified provision", "違反通知本身即屬違反指明的條文"),
         "s.20(4)–(5) Sch. 2 · ¶8.8"),
        (("at least 3 years", "最少3年"),
         ("Keep training records: who was trained, when, and in what", "備存培訓紀錄：誰接受了培訓、何時，以及培訓類別"),
         ("For all AML/CFT training, whatever the method", "所有打擊洗錢培訓，不論以何種方式進行"),
         ("You cannot demonstrate the training duty was met; this period comes from the Guideline, not Schedule 2", "無法證明已履行培訓責任；此期間出自指引，而非附表2"),
         "¶9.7"),
    ])
    + traps(
        trap(("A paper photocopy is not one of the two forms", "紙本影印本並非兩種形式之一"),
             ("For a document, Schedule 2 allows the original, or a copy kept on microfilm or in a computer database. A copy kept only on paper fits neither.",
              "就文件而言，附表2准許備存正本，或以微縮影片或電腦數據庫備存的複本。只以紙本備存的複本兩者皆不符合。"),
             "s.21 Sch. 2"),
        trap(("Two different starting points for five years", "五年有兩個不同的起算點"), None, "s.20(2)–(3A) Sch. 2",
             vs=[(("Transaction records", "交易紀錄"), ("Five years from the transaction, even if the customer leaves the next day.", "由交易起計五年，即使客戶翌日便終止關係。")),
                 (("Customer records", "客戶紀錄"), ("In a business relationship: five years from the end of the relationship, however long it lasted. For an occasional transaction at a CDD threshold: five years from its completion.", "業務關係中的客戶紀錄：由業務關係終止起計五年，不論關係維持了多久。如屬達盡職審查門檻的非經常交易：自交易完成起計五年。"))]),
        trap(("Which occasional transactions carry the completion clock", "哪些非經常交易適用「自交易完成起計」"), None,
             "s.20(3A), 3(1)(b), (1A) Sch. 2 · ¶8.4",
             vs=[(("Wire transfers and virtual asset transfers", "電傳轉帳及虛擬資產轉帳"), ("An occasional transaction of $8,000 or more: keep the customer records for at least five years from the date it is completed.", "總值相等於或超過$8,000的非經常交易：客戶紀錄須由交易完成當日起計備存至少5年。")),
                 (("Any other type, money changing included", "其他類別的交易（包括貨幣兌換）"), ("The CDD threshold, and so the completion clock, is $120,000, not $8,000.", "盡職審查門檻，亦即適用「自交易完成起計」的門檻，是$120,000，而非$8,000。"))]),
    ))


# ---------------------------------------------------------------- procedures, prohibitions, branches
SYS = sec('systems', ["s.15–17 Sch. 2", "s.19, 22, 23 Sch. 2", "¶4.14–4.15"],
          ("High-risk situations, prohibitions, procedures and branches", "高風險情況、禁止事項、程序及分行"),
    P("The first table is the one rule here that changes with the situation. The second collects the standing duties of Schedule 2's closing sections.",
      "第一個表是本節唯一隨情況而變的規則；第二個表匯集附表2最後幾條的常設責任。")
    + table([th("In a high-risk situation, including one the Commissioner specifies by written notice", "在高風險情況下（包括關長藉書面通知指明的情況）"), th("What you must do", "須做甚麼")], [
        tr(rh("A business relationship is about to be established", "即將建立業務關係", "s.15(a) Sch. 2"),
           td("Obtain senior management approval to establish it; <b>and either</b> take reasonable measures to establish source of wealth and source of funds, <b>or</b> take additional measures to mitigate the risk", "取得高級管理層批准建立關係；<b>並且</b>採取合理措施確立財富來源及資金來源，<b>或</b>採取額外措施減低風險")),
        tr(rh("A business relationship already exists", "業務關係已經存在", "s.15(b) Sch. 2"),
           td("Obtain senior management approval to <b>continue</b> it; take reasonable measures to verify any beneficial owner's identity; <b>and either</b> source of wealth and funds, <b>or</b> additional measures", "取得高級管理層批准以<b>繼續</b>該業務關係；採取合理措施核實任何實益擁有人的身分；<b>並且</b>確立財富來源及資金來源，<b>或</b>採取額外措施")),
        tr(rh("An occasional transaction is about to be carried out", "即將進行非經常交易", "s.15(c) Sch. 2"),
           td("Take additional measures to mitigate the risk", "採取額外措施減低風險")),
    ], note=B("Where the FATF calls for enhanced due diligence or countermeasures, or in another case considered higher risk, the Commissioner may by written notice either impose a general obligation to comply with section 15, or require the specific countermeasures the notice describes, in proportion to the risks.",
              "如特別組織呼籲執行更嚴格的盡職審查或採取針對措施，或在其他被視為屬較高風險的情況下，關長可透過書面通知，對經營者施加遵守第15條的一般責任，或要求採取通知內所述的特定針對措施，措施與風險相稱。") + ' ' + cite_html("¶4.15.2"), minw=720)
    + table([th("The standing duty", "常設責任"), th("What it requires", "規定甚麼")], [
        tr(rh("No anonymous accounts", "不得有匿名戶口", "s.16 Sch. 2"),
           td("Never open or maintain an anonymous account, or one in a fictitious name, for any customer. A confidential numbered account should not work as one: it should get exactly the same CDD and controls, the customer's identity must be verified and known to enough staff, and transfers and remittances from it must show the account holder's real name. Every customer's CDD record must be available to the Commissioner, other competent authorities, the compliance officer, auditors and other staff with appropriate authority",
              "不得為任何客戶開立或維持匿名戶口，或以虛構姓名或名稱開立或維持戶口。設有保密號碼的戶口不應作為匿名戶口：應遵從一模一樣的盡職審查及管控措施，客戶身分須經核實並讓相當數目的職員知悉，而該戶口的電傳轉帳和匯款須顯示戶口持有人的真實姓名。所有客戶的盡職審查紀錄必須可向關長、其他主管當局、合規主任、核數師及其他獲適當授權的人員提供",
              ("¶4.14.1 · fn 49–50", "第4.14.1段 · 註49至50"))),
        tr(rh("Effective procedures", "有效的程序", "s.19 Sch. 2"), td("For deciding whether a customer or beneficial owner is a PEP; for handling wire and virtual asset transfers that lack the required information; and, for each kind of customer, relationship, product and transaction, for carrying out the duties on CDD, simplified CDD, monitoring, customers not present, PEPs and high-risk situations", "用以斷定客戶或實益擁有人是否政治人物；處理欠缺所需資料的電傳轉帳及虛擬資產轉帳；以及就每種客戶、業務關係、產品及交易，履行盡職審查、簡化盡職審查、持續監察、客戶沒有現身、政治人物及高風險情況的責任")),
        tr(rh("Branches and subsidiaries outside Hong Kong", "香港以外的分行及附屬企業", "s.22 Sch. 2"), td("If you are incorporated in Hong Kong or re-domiciled here, make sure overseas branches, and subsidiaries in the same business, follow requirements similar to Schedule 2 Parts 2 and 3 as far as local law allows. Where local law forbids it, inform the Commissioner and take additional measures", "如你在香港成立為法團或屬經遷冊實體，須確保海外分行及經營相同業務的附屬企業，在當地法律准許的範圍內遵從與附表2第2及3部相類似的規定。如當地法律不准許，須通知關長並採取額外措施")),
        tr(rh("Safeguards", "預防措施", "s.23 Sch. 2"), td("Take all reasonable measures to ensure proper safeguards exist against contravening Parts 2 and 3 of the Schedule, and to mitigate ML/TF risks", "採取所有合理措施，確保有適當的預防措施防止違反附表第2或3部，並減低洗錢及恐怖分子資金籌集風險")),
        tr(rh("Correspondent banking and shell banks", "代理銀行服務及空殼銀行", "s.14, 17 Sch. 2"), td("Duties on authorized institutions only; they do not bind a money service operator", "只屬認可機構的責任，並不約束金錢服務經營者")),
    ], minw=720)
    + traps(
        trap(("A PEP needs both; another high-risk relationship needs one of two", "政治人物兩者皆須；其他高風險業務關係二擇其一"), None, "s.10, 15 Sch. 2",
             vs=[(("A politically exposed person", "政治人物"), ("Senior management approval <b>and</b> reasonable measures to establish source of wealth and source of funds.", "高級管理層批准，<b>以及</b>採取合理措施確立財富來源及資金來源。")),
                 (("Any other high-risk business relationship", "其他高風險業務關係"), ("Senior management approval too, then <b>either</b> source of wealth and funds <b>or</b> additional measures to mitigate. A high-risk occasional transaction needs additional measures only.", "同樣須取得高級管理層批准，然後<b>二擇其一</b>：確立財富來源及資金來源，<b>或</b>採取額外措施減低風險。高風險非經常交易只須採取額外措施。"))]),
    ))
