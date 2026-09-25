# Sections 5–8: SDD vs EDD, PEPs, not present, intermediaries (bilingual).
from bl_core import *
from bl_figs2 import fig4, fig8
from bl_sec1 import td, th
import ui as U


def row(h, sdd, edd):
    return '<tr>' + th(*h) + td(*sdd) + td(*edd) + '</tr>'


def ans_td(en, tc, cite, post=''):
    """A table cell whose text blurs in recall mode; post goes after the text (e.g. a flag)."""
    return td(en, tc, cite, '<span class="answer">').replace(cite_html(cite) + '</td>', post + '</span>' + cite_html(cite) + '</td>')


S5 = sec('sdd-edd', ["¶2.13, 4.1.2", "¶4.8–4.9", "¶4.15–4.16", "s.4, 10, 15 Sch. 2", ("Circular 3 Jul 2026", "2026年7月3日通函")], ("Simplified or enhanced: the two ends of the risk-based approach", "簡化還是更嚴格：風險為本方法的兩端"),
    P("SDD is a <b>may</b>: the MSO decides, on an adequate analysis, that the risk is low. EDD is a <b>must</b>: high risk obliges enhanced measures, and the CCE can add situations by written notice. Neither removes the duty to monitor.",
      "簡化盡職審查是<b>可以</b>：金錢服務經營者經充分分析，斷定風險屬低。更嚴格的盡職審查是<b>必須</b>：高風險即須執行更嚴格措施，關長亦可藉書面通知指明情況。兩者都不免除持續監察的責任。")
    + P("Assessing risk helps you differentiate between the risks of individual customers and business relationships, and apply appropriate and proportionate CDD and risk-mitigating measures (¶2.13). You should apply a risk-based approach when conducting CDD, and the extent of CDD should be commensurate with the ML/TF risks of the business relationship (¶4.1.2). For countries it identifies as high-risk, the FATF calls for enhanced due diligence, and in the most serious cases countermeasures, to protect the international financial system from the money laundering, terrorist financing and proliferation financing risks emanating from those countries (Circular 3 Jul 2026).",
        "評估風險有助金錢服務經營者分辨個別客戶與業務關係所涉的風險，並採取適當及相稱的盡職審查及減低風險措施（第2.13段）。執行盡職審查措施時應採用風險為本的方法，而盡職審查措施的程度應與業務關係所涉及的洗錢／恐怖分子資金籌集風險相稱（第4.1.2段）。就被識別為高風險的國家而言，特別組織要求採取更嚴格的盡職審查，及在最嚴重的情況下採取針對措施，以免國際金融體系因這些國家出現洗錢、恐怖分子資金籌集和擴散資金籌集的風險而受損（2026年7月3日通函）。")
    + '<div class="tbl"><table><thead><tr><th></th><th>' + B("Simplified due diligence", "簡化盡職審查") + ' <span class="chip may">' + B("may", "可以", True) + '</span></th><th>' + B("Enhanced due diligence", "更嚴格的盡職審查") + ' <span class="chip must">' + B("must", "必須", True) + '</span></th></tr></thead><tbody>'
    + row(("When", "何時", ""),
          ("The MSO determines, taking its risk assessment into account, that the relationship or transaction presents a <b>low</b> ML/TF risk, supported by an adequate analysis.", "金錢服務經營者經考慮風險評估結果後，斷定業務關係或交易的風險屬於<b>低</b>，並有充分分析支持。", "¶4.8.2, 4.8.4"),
          ("A situation that by its nature may present <b>high</b> ML/TF risk, or a situation the CCE specifies in a written notice; also non-Hong Kong PEPs, and jurisdictions for which the FATF calls for EDD. Where the FATF calls for EDD or countermeasures, or in other higher-risk cases, the CCE may by written notice impose the s.15 duty on MSOs generally, or require specific countermeasures.",
           "以性質而論可能造成<b>高度</b>風險的情況，或關長藉書面通知指明的情況；亦適用於非香港政治人物，以及特別組織呼籲執行更嚴格盡職審查的司法管轄區。如特別組織呼籲執行更嚴格的盡職審查或採取針對措施，或在其他被視為屬較高風險的情況下，關長可藉書面通知，對金錢服務經營者施加遵守附表2第15條的一般責任，或要求採取特定針對措施。", "¶4.9.1, 4.9.10, 4.15.1–4.15.2"))
    + '<tr>' + th("Risk factors the Guideline lists", "指引所列的風險因素", "")
    + ans_td("Customer: Hong Kong or equivalent-jurisdiction government or public body; listed corporation with BO transparency; FI in the AMLO sense or an equivalent supervised FI; authorised collective investment scheme. Product: provident or pension schemes funded by payroll deduction with no assignment; insurance for such a scheme with no surrender clause that cannot be used as collateral; life policy with annual premium up to HK$8,000 or single premium up to HK$20,000. Country: credible sources show effective AML/CFT systems or low corruption.",
             "客戶：香港或對等司法管轄區的政府機構或公共機構；實益擁有權具透明度的上市法團；條例所界定的金融機構或對等司法管轄區受監管的金融機構；獲授權向公眾發售的集體投資計劃。產品：從入息扣減供款且不准轉讓的公積金或退休金計劃；為該等計劃而設、不載有退回條款及不可用作抵押品的保險單；每年保費不多於8,000元或整付保費不多於20,000元的人壽保險單。國家：可靠消息來源顯示制度有效或貪污較少。", "¶4.8.7")
    + ans_td("Customer: unusual circumstances such as unexplained geographic distance or groups transacting across locations; shell vehicles with no clear purpose; nominee shareholders, nominee directors or bearer shares; cash-intensive business; unusually complex ownership; reluctance to disclose the counterparty; PEPs. Product or channel: anonymous transactions (which may involve cash); structuring to stay under thresholds; many-to-one or one-to-many transfers without explanation; frequent payments received from unknown or un-associated third parties; no tie to the destination jurisdiction; agent volumes out of pattern; agents with sub-standard compliance. Country: ineffective AML/CFT, significant corruption, sanctions or embargoes, terrorist funding or activity.",
             "客戶：業務關係異乎尋常（例如距離遙遠而原因不明、特定組別在多個地點交易）；無明確合法商業目的的空殼公司；有代名人股東、代名人董事、持票人股份或認股權證；現金密集型業務；擁有權結構異常繁複；不願披露收款人／匯款人詳情；政治人物。產品或渠道：匿名交易（或涉及現金）；拆分款項以規避門檻；不同人轉帳至同一人或同一人轉帳至不同人而無合理解釋；經常接收來歷不明或無聯繫的第三方支付的款項；與目的地／來源地無明顯關連；代理人交易量異常；代理人合規計劃未達標準。國家：制度欠缺效能、貪污嚴重、受制裁或禁運、資助恐怖主義。", "¶4.9.5") + '</tr>'
    + '<tr>' + th("Example measures", "措施例子", "")
    + ans_td("Accept other evidence such as proof of licence or listed status; the beneficial-owner exemptions below; less frequent updates of identification information; reduced ongoing monitoring and scrutiny of transactions based on a reasonable monetary threshold; infer the purpose of the relationship instead of asking.",
             "接納其他證明（例如牌照或上市地位證明）；下文有關實益擁有人的豁免；下調更新識別資料的頻密程度；下調持續監察和審查合理的金額門檻下的交易的程度；按交易類別推斷目的而不另行收集。", "¶4.8.8")
    + ans_td("More information on the customer such as occupation, assets and public sources, and more frequent updates; more on the intended nature of the relationship; source of funds and source of wealth; reasons for the transactions; evaluate the stated destination and reason; first payment through an account in the customer's name at a bank with similar CDD standards. Where EDD cannot fully mitigate the risk, add transaction limits or restrict functions. These are examples: you are not expected to apply them all to every high-risk relationship.",
             "就客戶索取額外資料（職業、資產、公開資料）並更頻密更新；就業務關係擬具有的性質索取額外資料；查明資金來源及財富來源；查明交易理由；評估資金目的地及交易原因；規定第一次付款經由客戶名下、在盡職審查標準相若的銀行開設的戶口進行。如未能完全減低風險，設交易限額或限制戶口功能。以上僅為例子：毋須就每項高風險業務關係執行全部措施。", "¶4.9.2, 4.9.6 fn 36", U.flag()) + '</tr>'
    + row(("Senior management", "高級管理層", ""), ("No approval requirement stated for SDD itself.", "簡化盡職審查本身沒有訂明批准規定。"),
          ("Approval to <b>establish</b> a high-risk relationship, or to <b>continue</b> one that becomes high risk.", "<b>建立</b>高風險業務關係，或<b>維持</b>其後被評為高風險的關係，均須批准。", "¶4.9.3 · s.15 Sch. 2"))
    + row(("Ongoing monitoring", "持續監察", ""), ("Still required under s.5 of Schedule 2 (the duty never falls away), although its degree may be reduced as an SDD measure.", "仍須按附表2第5條持續監察（責任不會免除），但可作為簡化盡職審查措施下調其程度。", "¶4.8.6, 4.8.8(d)"),
          ("<b>Enhanced</b>: more controls, better timing, patterns selected for examination; high-risk records reviewed at least annually.", "<b>更嚴格</b>：增加管控措施的次數及時間，篩選須進一步查驗的交易模式；高風險客戶的紀錄最少每年覆核一次。", "¶4.9.4 · 5.3"))
    + row(("When it ends", "何時終止", ""), ("SDD must stop when the risk assessment changes and the risk is no longer low; ML/TF is suspected; or documents or information already obtained are doubted.", "簡化盡職審查須停止的情況：風險評估有變而不再屬低；懷疑有洗錢／恐怖分子資金籌集；或對已取得的文件或資料存疑。", "¶4.8.3"),
          ("It follows the risk: EDD applies while the situation is high risk, and the customer's risk assessment is reviewed and updated over time. Exception: for a current non-Hong Kong PEP the measures apply whatever the risk rating; they can stop only once the person is a former PEP. For a former PEP (non-Hong Kong, Hong Kong or international organisation), the PEP measures may stop only with <b>senior management approval</b>, on an appropriate risk assessment, kept on record, showing the PEP no longer presents a high ML/TF risk.",
           "視乎風險：情況屬高風險期間即須執行更嚴格措施，客戶的風險評估亦須不時覆核和更新。例外：對現任非香港政治人物，不論風險評級均須執行；只有在其成為前政治人物後方可停止。對前政治人物（非香港、香港或國際組織政治人物），須經<b>高級管理層批准</b>，並以適當的風險評估（須保存紀錄）證明該政治人物不再構成高度洗錢／恐怖分子資金籌集風險，方可不再執行政治人物的更嚴格措施。", "¶2.14, 4.9.1, 4.9.10, 4.9.12, 4.9.18 · s.10(3) Sch. 2"))
    + '</tbody></table></div>'
    + '<h3>' + B("Beneficial owners you may choose not to identify or verify", "可選擇不識別或核實實益擁有人的情況") + '</h3>'
    + U.table([U.th("The case", "情況"), U.th("What you may skip, and the limit", "可省略甚麼，以及限制")], [
        U.tr(U.rh("The customer itself is one of these", "客戶本身屬以下類別", "¶4.8.10 · s.4(3) Sch. 2"), U.td("A financial institution under the Ordinance; an institution in an equivalent jurisdiction, in a similar business, with similar measures and supervised for them; a corporation listed on any stock exchange, after checking its disclosure requirements; an investment vehicle whose investors' CDD is done by a supervised institution; or the Hong Kong Government or a public body, or their equivalent in an equivalent jurisdiction. You may skip identifying and verifying its beneficial owners",
                                                                                                             "條例所界定的金融機構；在對等司法管轄區成立、業務相類似、設有相類似措施並受監管的機構；在任何證券市場上市的法團（須先評估其披露規定）；由受監管機構為所有投資者執行盡職審查的投資公司；或香港政府或公共機構，或對等司法管轄區的同等機構。可省略識別及核實其實益擁有人")),
        U.tr(U.rh("Such an entity sits in the customer's ownership chain", "客戶的擁有權鏈中有此類實體", "¶4.8.11 · s.4(2) Sch. 2"), U.td("You need not look through <b>that</b> entity, but beneficial owners elsewhere in the chain must still be identified and verified", "毋須穿透<b>該</b>實體，但鏈中其他部分的實益擁有人仍須識別及核實", post=U.flag())),
        U.tr(U.rh("The product is one of these", "產品屬以下類別", "¶4.8.17–4.8.18 · s.4(4)–(5) Sch. 2"), U.td("A provident, pension or retirement scheme funded by payroll deduction that forbids assignment; insurance for such a scheme with no surrender clause that cannot be used as collateral; or a life policy with an annual premium up to <b>$8,000</b> or a single premium up to <b>$20,000</b>",
                                                                                                                 "從入息扣減供款且不准轉讓的公積金、退休金或退休計劃；為該等計劃而設、不載有退回條款及不可用作抵押品的保險單；或每年保費不多於<b>$8,000</b>或整付保費不多於<b>$20,000</b>的人壽保險單")),
        U.tr(U.rh("A solicitor's client account", "律師的當事人戶口", "¶4.8.19–4.8.20 · s.4(6) Sch. 2"), U.td("Only if it is in the solicitor's name, clients' money is <b>mingled</b>, and the solicitor manages it as the clients' agent. A single-client account, or unmingled sub-accounts, means identifying the underlying client",
                                                                                                           "只限戶口以律師名義開設、當事人的款項<b>混合</b>存放，且由律師以當事人代理人的身分管理。單一當事人戶口或未混合的分戶口，須識別有關當事人")),
    ], minw=700)
    + U.traps(
        U.trap(("$8,000 again, doing a different job", "又是$8,000，但作用不同"), None, "s.4(1), 4(5)(c), 3(1A) Sch. 2",
               vs=[(("A life policy premium", "人壽保險單保費"), ("Up to $8,000 a year, or $20,000 single: a product for which simplified measures are allowed.", "每年不多於$8,000，或整付不多於$20,000：可採用簡化措施的產品。")),
                   (("A wire transfer", "電傳轉帳"), ("$8,000 or more: the amount at which CDD must be carried out before an occasional wire transfer (simplified CDD under s.4 of Schedule 2 can still apply to a qualifying customer).", "$8,000或以上：進行非經常電傳轉帳前必須執行客戶盡職審查的款額（如客戶符合資格，仍可按附表2第4條採用簡化客戶盡職審查）。"))]),
        U.trap(("High-risk EDD is a menu; the PEP measures are all three", "高風險的更嚴格措施可選取；政治人物的措施須全部執行"), None, "¶4.9.2, 4.9.6 fn 36 · ¶4.9.10, 4.9.23",
               vs=[(("High risk in general", "一般高風險情況"), ("The listed EDD measures are examples. Choose measures proportionate to the risk that you can justify to the CCE; you are not expected to apply them all.", "所列的更嚴格盡職審查措施只是例子。按風險選擇合乎比例、能向關長提供理據的措施，毋須全部執行。")),
                   (("A PEP the rule catches", "受規定涵蓋的政治人物"), ("All three measures, every time: senior management approval, source of wealth and source of funds, enhanced ongoing monitoring. Only their depth is scaled to the risk.", "每次均須執行全部三項：高級管理層批准、財富來源及資金來源、更嚴格的持續監察。只有措施的深度按風險調整。"))]),
        U.trap(("\"Equivalent jurisdiction\" is not just a FATF member", "「對等司法管轄區」不限於特別組織成員"),
               ("It means (a) a FATF member other than Hong Kong, or (b) a jurisdiction that imposes requirements similar to Schedule 2. For (b) you may have to judge for yourself; document the assessment, drawing for example on FATF-style regional body membership and mutual evaluations, FATF findings of strategic deficiencies and C&amp;ED advisory circulars; review it regularly or on trigger events. The term decides the SDD customers above, the payment route for a customer not present, and which overseas intermediaries you may rely on.",
                "指(a)特別組織成員的司法管轄區（香港除外），或(b)施加類似附表2規定的司法管轄區。就(b)項或須自行評估，並應將評估記錄在案，例如參考是否與特別組織相類似職能的地區組織成員及其相互評估報告、是否被特別組織識別為在打擊洗錢／恐怖分子資金籌集策略上有缺失，以及關長發出的忠告通函；並須定期及／或遇有觸發事件時覆核。這個詞決定上文可簡化的客戶、客戶沒有現身時的付款途徑，以及可依賴哪些海外中介人。"),
               "s.1 Sch. 2 · ¶4.16.1–4.16.3"),
    )
    + numreq([
        (("HK$8,000 / HK$20,000", "8,000元／20,000元"),
         ("You may choose not to identify or verify the customer's beneficial owners", "可選擇不識別或核實客戶的實益擁有人"),
         ("A life policy with an annual premium at or under $8,000, or a single premium at or under $20,000", "每年保費不多於8,000元，或整付保費不多於20,000元的人壽保險單"),
         ("Above these amounts the policy is not a listed lower-risk product: identify and verify the customer's beneficial owners as usual", "超過此等款額，保單不屬所列較低風險產品：須照常識別及核實客戶的實益擁有人"),
         "¶4.8.7(b)(iii), 4.8.9(b), 4.8.17(c)"),
        (("every 2 years", "每兩年一次"),
         ("Redo the institutional ML/TF risk assessment, and review it on trigger events as well", "重做機構層面的洗錢／恐怖分子資金籌集風險評估；發生觸發事件時亦須覆核"),
         ("Always. Trigger events include a significant breach, a new customer segment or a new delivery channel", "任何時候。觸發事件包括嚴重違規、新客戶類別或新交付渠道"),
         ("Every customer risk rating rests on this assessment, so a stale one undermines the whole risk-based approach", "所有客戶風險評級均以此評估為基礎；評估過時即動搖整個風險為本方法"),
         "¶2.9"),
    ]))

PEP_KEY = U.legend([('hex', ("a question you answer", "你須回答的問題")), ('', ("a fact or step", "事實或步驟")),
                    ('must', ("the rules say must", "規定：必須")), ('ok', ("standard CDD applies", "按標準盡職審查")),
                    ('may', ("risk-based: may be relaxed with approval", "按風險：經批准可放寬"))])

S6 = sec('pep', ["¶4.9.7–4.9.26", "s.1, 5, 10, 15, 19 Sch. 2"], ("Politically exposed persons: three kinds, two rules", "政治人物：三種類別，兩條規則"),
    P("Screening covers the customer <b>and every beneficial owner</b>. The rule then splits by geography: a non-Hong Kong PEP triggers the EDD package without any risk assessment; a Hong Kong or international-organisation PEP triggers it only when the relationship is high risk.",
      "篩查範圍涵蓋客戶<b>及每名實益擁有人</b>。規則按地域分開：非香港政治人物毋須風險評估即觸發更嚴格措施；香港或國際組織政治人物只在業務關係屬高風險時才觸發。")
    + U.fig(fig4, ("The same three measures appear in every mandatory branch. What changes is whether risk is assessed first. Note the trap in ¶4.9.10: for a non-Hong Kong PEP the trigger is knowing the status, not the risk rating.", "每個「必須」分支都是同樣三項措施，分別只在於是否先評估風險。留意第4.9.10段的陷阱：對非香港政治人物，觸發點是知悉其身分，而非風險評級。"), PEP_KEY)
    + U.table([U.th("Question", "問題"), U.th("Answer", "答案")], [
        U.tr(U.rh("Who is a PEP?", "誰是政治人物？", "¶4.9.7, 4.9.13–4.9.14"), U.td("Someone who <b>is or has been</b> entrusted with a <b>prominent public function</b>. Non-Hong Kong: a head of state or government, a senior politician, a senior government, judicial or military official, a senior executive of a <b>state-owned</b> corporation, or an important political party official. Hong Kong: a head of government, a senior politician, a senior government or judicial official, a senior executive of a <b>government-owned</b> corporation, or an important political party official; there is no head of state and no military official in this list. International organisation: directors, deputy directors, board members or equivalent functions. Middle-ranking and more junior officials are not included",
                                                                                         "<b>擔任或曾擔任重要公職</b>的人。非香港：國家元首、政府首長、資深從政者、高級政府、司法或軍事官員、<b>國有企業</b>高級行政人員及重要政黨幹事。香港：政府首長、資深從政者、高級政府或司法官員、<b>政府持有公司</b>的高級行政人員及重要政黨幹事；此列沒有國家元首，亦沒有軍事官員。國際組織：總監、副總監及理事會成員或同等職能。中級或更低級官員不包括在內", post=U.flag())),
        U.tr(U.rh("What is an international organisation?", "何謂國際組織？", "¶4.9.15"), U.td("A body set up by formal political agreements between member States that have the status of international treaties, whose existence is recognised by law in its member countries, and which is not treated as a resident institutional unit of the country where it is located. Examples: the United Nations and affiliates such as the International Maritime Organization; the Council of Europe, EU institutions, the OSCE and the Organization of American States; NATO; the WTO and ASEAN",
                                                                                              "由成員國根據具有國際條約地位的正式政治協議成立的實體；其地位獲成員國的法律認可；以及不會被視作所處國家的常駐機構單位。例子：聯合國及附屬國際組織（例如國際海事組織）；歐洲理事會、歐洲聯盟機構、歐洲安全與合作組織及美洲國家組織；北大西洋公約組織；世界貿易組織及東南亞國家協會")),
        U.tr(U.rh("Who else counts?", "還有誰計算在內？", "¶4.9.7–4.9.8 · s.1(2)–(3) Sch. 2"), U.td("<b>Family</b>: a spouse, a partner treated as a spouse where they live, a child, a parent, or a child's spouse or partner. <b>Close associates</b>: close business relations, including co-owning a legal person or trust with the PEP, or owning a vehicle set up for the PEP's benefit",
                                                                                                "<b>家庭成員</b>：配偶、當地法律視為等同配偶的伴侶、子女、父母，或子女的配偶或伴侶。<b>關係密切的人</b>：有密切業務關係，包括與政治人物同為某法人或信託的實益擁有人，或為政治人物利益而成立的法人或信託的實益擁有人")),
        U.tr(U.rh("Who is a former PEP?", "誰是前政治人物？", "¶4.9.11, 4.9.18 · s.1 Sch. 2"), U.td("For non-Hong Kong PEPs, Schedule 2 defines it: someone who has been, but is not currently, entrusted with a prominent public function outside Hong Kong, <b>and</b> that person's family members and close associates. For Hong Kong and international-organisation PEPs, ¶4.9.18 covers a PEP who is no longer entrusted with the function",
                                                                                              "就非香港政治人物，附表2有所界定：曾在香港以外地方擔任、但目前沒有擔任重要公職的人，<b>以及</b>其家庭成員及關係密切的人。就香港及國際組織政治人物，第4.9.18段適用於不再擔任有關職位的政治人物")),
        U.tr(U.rh("How do you find them?", "如何識別？", "¶4.9.9, 4.9.16, 4.9.19–4.9.21 · s.19(1) Sch. 2"), U.td("For non-Hong Kong PEPs, <b>effective procedures</b> are a statutory must; for Hong Kong and international-organisation PEPs, you should take <b>reasonable measures</b>. Commercial databases support that work but never replace knowing a customer's occupation and employer. Under-classifying raises ML risk; over-classifying wastes compliance effort",
                                                                                                                  "就非香港政治人物，設有<b>有效程序</b>是法定要求；就香港政治人物及國際組織政治人物，應採取<b>合理措施</b>。商業數據庫只是支援工具，不能取代了解客戶的職業及僱主。分類不足會提高洗錢風險；分類過度則造成不必要的合規負擔", post=U.flag())),
        U.tr(U.rh("How much EDD?", "更嚴格措施做到多深？", "¶4.9.22–4.9.23"), U.td("Scaled to the function held, the jurisdiction, the product and delivery channel, and for a former PEP the ¶4.9.12 and ¶4.9.18 factors. The risk posed by family members and close associates varies, to some extent, with the social-economic and cultural structure of the PEP's jurisdiction",
                                                                              "按所擔任的公職、司法管轄區、產品及交付渠道，以及（前政治人物）第4.9.12及4.9.18段的因素調整。家庭成員及關係密切的人的風險，某程度上視乎政治人物所屬司法管轄區的社會、經濟及文化結構而定")),
    ], minw=700)
    + U.traps(
        U.trap(("Source of wealth is not source of funds", "財富來源不等於資金來源"), None, "¶4.9.24–4.9.26 · s.10 Sch. 2",
               vs=[(("Source of wealth", "財富來源"), ("Where the person's whole body of assets came from, and how they were acquired.", "該人全部財富的源頭，以及如何取得。")),
                   (("Source of funds", "資金來源"), ("Where the particular money in this relationship came from, including the activity that generated it.", "本業務關係所涉特定資金的源頭，包括衍生資金的活動。"))]),
        U.trap(("The statute's PEP is a non-Hong Kong PEP", "條例中的政治人物是非香港政治人物"),
               ("Schedule 2 defines a politically exposed person by a prominent public function in a place outside Hong Kong, and its mandatory measures attach to that definition. The Hong Kong and international-organisation categories are defined in the Guideline, which applies the enhanced measures to them on risk.",
                "附表2以在香港以外地方擔任重要公職界定政治人物，其強制措施亦附於此定義。香港政治人物及國際組織政治人物兩類，則由指引界定，並按風險適用更嚴格措施。"),
               "s.1, 10 Sch. 2 · ¶4.9.13–4.9.17"),
        U.trap(("A former PEP: a recorded risk assessment, not merely a time limit", "前政治人物：須有紀錄在案的風險評估，不能僅看時限"),
               ("How long ago the person left office does not settle it: the handling rests on an assessment of risk, not merely on prescribed time limits. Drop the enhanced measures without an appropriate risk assessment and the Commissioner treats it as a breach, so keep the assessment as proof.",
                "卸任多久並不能決定處理方法：應依據風險評估而定，不應僅訂明時限。未經適當的風險評估便不執行更嚴格措施，關長會視之為違規，因此應保存評估紀錄作為證明。"),
               ("¶4.9.12 fn 37–38 · ¶4.9.18 fn 41–42", "第4.9.12段註37至38 · 第4.9.18段註41至42"),
               vs=[(("Former non-Hong Kong PEP", "前非香港政治人物"), ("A breach of section 10(1) or 10(2) of Schedule 2; the record proves compliance with section 10(3).", "違反附表2第10(1)或10(2)條；紀錄證明已符合第10(3)條。")),
                   (("Former Hong Kong or international-organisation PEP", "前香港或國際組織政治人物"), ("A breach of section 15(a) or 15(b) of Schedule 2; the record proves compliance with section 15(a) or 15(b).", "違反附表2第15(a)或15(b)條；紀錄證明已符合第15(a)或15(b)條。"))]),
    ))


def opt(n, en, tc, cite):
    return f'<div class="card must" data-n="{n}"><span class="answer">{P(en, tc)}</span>{cite_html(cite)}</div>'


S7 = sec('nfp', ["¶4.10", "s.9 Sch. 2"], ("Customer not physically present: pick at least one", "客戶沒有現身：最少執行一項"),
    P("The Ordinance allows non-face-to-face onboarding but names the risk, impersonation, and demands at least one extra measure. Which one, and how many, follows the product and the assessed risk.",
      "條例容許非面對面建立業務關係，但點明假冒風險，並要求最少一項額外措施。選哪一項、做多少項，視乎產品及評估所得的風險。")
    + '<div class="pick">'
    + opt("(a)", "Further verify identity using documents, data or information from a s.2(1)(a) source <b>not previously used</b> for this customer.", "以附表2第2(1)(a)條提述、但<b>不曾用於</b>核實該客戶身分的文件、數據或資料，進一步核實身分。", "¶4.10.1(a)")
    + opt("(b)", "Take <b>supplementary measures</b> to verify what you already hold: an independent, appropriate certifier of the documents; checks against reliable databases or registries; appropriate technology. You must be able to show the CCE it guards against impersonation.", "採取<b>增補措施</b>核實已取得的資料：由獨立的合適人選認證文件；根據可靠的數據庫或登記冊核對；使用合適的科技。須能向關長證明措施足以應對假冒風險。", "¶4.10.1(b), 4.10.4 · Appendix A")
    + opt("(c)", "Ensure the payment, or the <b>first</b> of several, comes through an account in the customer's name at an <b>authorized institution</b>, or an equivalent-jurisdiction institution doing similar business, with similar measures, supervised by an HKMA-like authority.", "確保付款（如多於一次，則指<b>第一次</b>）經由以客戶名義在<b>認可機構</b>開設的戶口進行，或在對等司法管轄區經營相類似業務、設有相類似措施並受金管局同類主管當局監管的機構。", "¶4.10.1(c)")
    + '</div><div class="cards">'
    + card(("No extra measure needed", "毋須額外措施"), "¶4.10.2 · s.9(2) Sch. 2", P("When identity was verified through a <b>digital identification system</b> that is a reliable and independent source recognised by the CCE.", "如已根據關長認可、屬可靠及獨立來源的<b>數碼識別系統</b>核實客戶身分。"), 'ok')
    + card(("Customers that are not natural persons too", "非自然人客戶亦然"), "¶4.10.5", P("The additional measures generally apply to natural persons, but mitigate any increased risk when a customer that is <b>not a natural person</b> onboards non-face-to-face (for example, the natural person acting for it is not physically present for identification), or when you receive only <b>copies</b> of a legal person customer's identification documents.",
                                                                                            "額外措施一般適用於屬自然人的客戶，但如<b>並非自然人</b>的客戶透過非面對面的渠道建立業務關係（例如代表客戶的自然人不曾為身分識別的目的而現身），或僅獲法人客戶文件的<b>複本</b>用作識別及核實身分時，仍應減低任何增加的風險。"))
    + '</div>')

RELY_KEY = U.legend([('must', ("you, the MSO: the duties and the ultimate responsibility are yours", "金錢服務經營者：責任及最終責任在你")),
                     ('', ("the other parties", "其他各方"))])

S8 = sec('rely', ["¶4.11", "s.18 Sch. 2"], ("Relying on an intermediary's CDD", "依賴中介人執行客戶盡職審查"),
    P("In reliance, a third party, which <b>usually</b> has its own existing relationship with the customer, performs some of the measures under its own procedures. That is different from outsourcing or an agent applying your procedures under your control, which is not reliance at all.",
      "依賴是指<b>通常</b>已與客戶建立既有業務關係的第三方，按其本身程序執行部分措施。這與外判或代理按你的程序、受你管控而執行措施不同，後者根本不算依賴。")
    + P("Read the figure from top to bottom: the numbered arrows are what must pass between the intermediary and you, in order.",
        "由上而下閱讀下圖：編號箭咀是中介人與你之間須傳遞的事項，按先後排列。")
    + U.fig(fig8, ("Ongoing monitoring under s.5 can never be relied on (fn 44). Doubts about the intermediary mean reviewing it, and if needed redoing the CDD yourself (¶4.11.7).", "附表2第5條的持續監察永不可依賴中介人執行（註44）。對中介人有疑慮時須覆核其能力，必要時自行重新執行盡職審查（第4.11.7段）。"), RELY_KEY)
    + U.table([U.th("The intermediary", "中介人"), U.th("Conditions", "條件")], [
        U.tr(U.rh("A Hong Kong financial institution", "香港的金融機構", "¶4.11.8 · s.18(3)(b) Sch. 2"), U.td("An authorized institution, licensed corporation, authorized insurer, or licensed insurance agent, agency or broker company", "認可機構、持牌法團、獲授權保險人，或持牌保險代理、代理機構或經紀公司")),
        U.tr(U.rh("A Hong Kong professional", "香港的專業人士", "¶4.11.8–4.11.9 · s.18(3)(a) Sch. 2"), U.td("An accounting professional, estate agent, legal professional or TCSP licensee that satisfies you it (1) has adequate procedures to prevent money laundering and terrorist financing and (2) is required to comply with Schedule 2 for that customer. It is so required (condition (2)) only when it, by way of business, prepares for or carries out for the customer a transaction specified in s.5A of the Ordinance (fn 45); otherwise condition (2) is not met",
                                                                                                          "能令你信納其(1)有充分程序防止洗錢及恐怖分子資金籌集，及(2)須就有關客戶遵從附表2所載相關規定的會計專業人士、地產代理、法律專業人士或信託或公司服務持牌人。該專業人士只在以業務方式為該客戶擬備或進行打擊洗錢條例第5A條指明的交易時，才須就該客戶遵從附表2（即第(2)項）；否則不符合第(2)項（註45）", post=U.flag())),
        U.tr(U.rh("An overseas intermediary", "海外中介人", "¶4.11.10–4.11.11 · s.18(3)(c) Sch. 2"), U.td("In an equivalent jurisdiction: a lawyer, notary, auditor, accountant, trust or company service provider, tax adviser, trust company, estate-agent-like business, or an institution like an intermediary financial institution; required to be registered, licensed or regulated there; with measures similar to Schedule 2, and supervised for them",
                                                                                                           "在對等司法管轄區：律師、公證人、核數師、專業會計師、信託或公司服務提供者、稅務顧問、信託公司、與地產代理相類似的業務，或與中介人金融機構相類似的機構；須在當地註冊、領牌或受規管；設有與附表2相類似的措施，並就此受監管")),
        U.tr(U.rh("A related foreign financial institution", "相關外地金融機構", "¶4.11.12–4.11.14 · s.18(3)(d), (3A) Sch. 2"), U.td("In the same group, or a branch or head office; required by group policy to have measures like Schedule 2 and AML/CFT programmes; supervised at group level by a relevant authority or an equivalent-jurisdiction authority; and group policy must also mitigate any higher country risk",
                                                                                                                         "屬同一集團，或分行或總行關係；集團政策規定設有與附表2相類似的措施，並針對洗錢及恐怖分子資金籌集實施計劃；在集團層面受有關當局或對等司法管轄區主管當局監管；集團政策亦須足以減低較高的國家風險")),
    ], minw=700)
    + U.traps(
        U.trap(("Relying is not using an agent, but you stay liable either way", "依賴不等於使用代理人，但兩者你都須負責"), None, "s.18(2), (6) Sch. 2 · ¶4.11.1–4.11.2",
               vs=[(("Relying on an intermediary", "依賴中介人"), ("A third party, usually one with its own customer relationship, carries out a measure under its own procedures.", "通常與客戶已有本身業務關係的第三方，按其本身程序執行某項措施。")),
                   (("Using an agent", "使用代理人"), ("Someone carries out the measure for you, under your procedures and your control.", "由他人按你的程序、在你管控下代你執行措施。"))]),
    )
    + numreq([
        (("at least 5 years", "至少5年"),
         ("The intermediary's undertaking to keep all the underlying CDD information, and to supply copies when you ask", "中介人承諾備存所有相關盡職審查資料，並在你要求時提供複本"),
         ("Throughout your relationship with the customer and for at least 5 years from the day it ends, or until a time the CCE specifies", "在你與客戶的業務關係持續期間，及由業務關係終止日期起計至少5年，或直至關長指明的時間"),
         ("Reliance is no defence: you remain liable under the Ordinance for any failure to carry out the measure", "依賴中介人不是免責理由：未有執行有關措施，你仍須按條例負責"),
         "¶4.11.5 · s.18(2), (4)(b) Sch. 2"),
    ]))
