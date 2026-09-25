# Sections 1–4: map, four measures, beneficial owner, timing (bilingual).
from bl_core import *
from bl_figs import fig1, fig3, fig5
import ui as U


def legend():
    items = [('hex', ("a question you answer", "你須回答的問題")), ('', ("a fact or step", "事實或步驟")), ('must', ("a duty you must meet", "你必須履行的責任")),
             ('may', ("a permission you may use", "你可以選用的做法")), ('ok', ("you may proceed", "可以進行")), ('stop', ("you must stop", "必須停止"))]
    return '<div class="legend">' + ''.join(f'<span><i class="{c}"></i>{B(en, tc, True)}</span>' for c, (en, tc) in items) + '</div>'


S1 = sec('map', ["¶4.1–4.2", "¶4.8–4.9, 4.13", "s.2–3 Sch. 2", "¶1.6"], ("Do I owe CDD, and how much?", "我須否執行盡職審查？程度多深？"),
    P("Start at the top with the person in front of you. Hexagons are questions you answer. Every path that reaches the grey CDD box then meets the same risk question, which decides whether CDD is simplified, standard or enhanced. Box colours follow the key under the chart.",
      "由頂部眼前的人開始。六角形是你須回答的問題。凡到達灰色盡職審查方格的路徑，都會接著面對同一條風險問題，由它決定執行簡化、標準或更嚴格的盡職審查。方格顏色見圖下的圖例。")
    + U.fig(fig1, ("Occasional transactions include, for example, wire transfers, virtual asset transfers, remittance service, currency exchange and buying cashier orders or gift cheques (fn 13). Suspicion or doubt overrides every threshold (¶4.2.1(c)–(d), fn 15). Whether CDD is simplified, standard or enhanced, ongoing monitoring under s.5 of Schedule 2 is never switched off (¶4.8.6). The HK$120,000 third-party cash rule is in <a href=\"#s2-thresholds\">Thresholds</a>; the separate statutory exemption from beneficial-owner checks for the specified kinds of customer in s.4(3) of Schedule 2 is in <a href=\"#s2-sdd-edd\">SDD vs EDD</a>.",
                   "非經常交易可包括電傳轉帳、虛擬資產轉帳、匯款服務、貨幣兌換、購買銀行本票或禮券（註13）。有懷疑或存疑時，門檻一概不適用（第4.2.1(c)至(d)段、註15）。不論盡職審查是簡化、標準或更嚴格，附表2第5條的持續監察從不豁免（第4.8.6段）。第三方現金交易120,000元的規定見<a href=\"#s2-thresholds\">門檻</a>；附表2第4(3)條就指明類別客戶毋須核查實益擁有人的另一項法定規則，見<a href=\"#s2-sdd-edd\">簡化與更嚴格</a>。"), legend())
    + U.traps(
        U.trap(("A Guideline \"should\" is not optional", "指引的「應」並非可有可無"),
               ("Where the Guideline uses \"must\" or \"should\" for an action, consideration or measure, it says that is a mandatory requirement. Do not read a \"should\" on this page as a mere recommendation.",
                "指引訂明，凡提及行動、考慮或措施時採用「須／必須」或「應／應該」，即表示該項屬強制規定。本頁的「應」不可視作單純建議。"),
               "¶1.6"),
        U.trap(("What makes occasional transactions linked", "非經常交易怎樣才算有關連"),
               ("The link lies in the transactions themselves: for example, several payments to the same recipient from one or more sources over a short period, or a customer who regularly transfers funds to one or more destinations. Weigh these factors against the timeframe of the transactions. Once linked transactions meet a threshold, CDD should be carried out.",
                "關連取決於交易本身的特徵，例如在一段短時間內，把來自同一個或多個來源的數筆款項支付予同一收款人，或客戶定期將款項轉帳至一個或多個目的地。應將此等因素與進行交易的時間一併考慮。有關連的交易一旦達至門檻，便應執行盡職審查措施。"),
               "¶4.2.4–4.2.5"),
    ))


def td(en, tc, cite=None, extra=''):
    return f'<td>{extra}{B(en, tc)}{cite_html(cite)}</td>'


def th(en, tc, cite):
    return f'<th class="rowh">{B(en, tc)}{cite_html(cite)}</th>'


chip_verify = '<span class="chip ink">' + B("verify", "核實", True) + '</span> '
chip_reas = '<span class="chip">' + B("reasonable measures", "合理措施", True) + '</span> '
chip_und = '<span class="chip">' + B("understand", "了解", True) + '</span> '
chip_auth = '<span class="chip ink">' + B("verify authority", "核實授權", True) + '</span> '

S2 = sec('measures', ["¶4.1.3", "¶4.3–4.6", "s.2(1) Sch. 2"], ("The four measures, and how hard each one verifies", "四項措施，以及各自核實的嚴格程度"),
    P("The Ordinance uses two different verbs, and the paper likes the difference. A customer's identity is <b>verified</b>. A beneficial owner's identity gets <b>reasonable measures</b> to verify it, scaled to risk. A person acting for the customer gets reasonable measures on identity plus a hard <b>verification of authority</b>.",
      "條例用了兩個不同的動詞，試卷很喜歡考這個分別。客戶的身分須<b>核實</b>；實益擁有人的身分則採取<b>合理措施</b>核實，程度按風險而定；看似代表客戶行事的人，身分採取合理措施核實，其<b>授權</b>則須確實核實。")
    + '<div class="tbl"><table><thead><tr><th>' + B("Measure", "措施") + '</th><th>' + B("Identify: collect at least", "識別：最低限度收集") + '</th><th>' + B("Verify", "核實") + '</th><th>' + B("Acceptable sources", "可接納的來源") + '</th></tr></thead><tbody>'
    + '<tr>' + th("(a) The customer", "(a) 客戶", "s.2(1)(a) · ¶4.3")
    + '<td>' + B("<b>Natural person:</b> full name, date of birth, nationality, unique ID number and document type. Also obtain the residential address: collect it, but you need not verify it.", "<b>自然人：</b>全名、出生日期、國籍、獨特識別號碼及文件類別。另應索取住址資料：須收集，但毋須核實。") + '' + cite_html("¶4.3.2, 4.3.5 fn 18") + ''
    + B("<b>Legal person:</b> name, date and place of incorporation including registered office, ID number and document type, principal place of business if different.", "<b>法人：</b>全名、註冊或成立的日期及地點（包括註冊辦事處地址）、獨特識別號碼及文件類別、主要營業地點（如不同）。") + '' + cite_html("¶4.3.6") + ''
    + B("<b>Trust:</b> name, date of settlement, governing law, any official ID number, registered office.", "<b>信託：</b>名稱、成立或設立日期、規管法律的司法管轄區、官方識別號碼（如有）、註冊辦事處。") + '' + cite_html("¶4.3.11") + '</td>'
    + td("Natural person: name, date of birth, ID number and document type against documents, data or information from a reliable and independent source, for example an identity card, a valid travel document such as an unexpired passport, or a document issued by a government body; the document should carry a photograph, though in exceptional circumstances one without a photograph may be accepted if the risks have been properly assessed and mitigated. Legal person: name, legal form, current existence and binding powers, which often takes more than one document.",
         "自然人：根據可靠及獨立來源所提供的文件、數據或資料，核實姓名、出生日期、識別號碼及文件類別，例如身份證、有效的旅遊證件（例如未過期的護照）或政府機構發出的文件；文件應載有照片，但如情況特殊，經妥善評估和減低所涉及的風險後，可接納沒有照片的身分證明文件。法人：核實名稱、法定形式、現時仍然存在及規管和約束該法人的權力，往往須多於一份文件。", "¶4.3.3–4.3.4, 4.3.7, 4.3.12 · fn 20", '<span class="answer">' + chip_verify + '</span>')
    + td("Reliable and independent: a governmental body; the CCE or another relevant authority; an equivalent overseas authority; a CCE-recognised digital identification system; any other CCE-recognised source.",
         "可靠及獨立來源：政府機構；關長或其他有關主管當局；香港以外職能相類似的主管當局；關長認可的數碼識別系統；關長認可的其他來源。", "¶4.3.1 · Appendix A") + '</tr>'
    + '<tr>' + th("(b) Beneficial owner", "(b) 實益擁有人", "s.2(1)(b) · ¶4.4")
    + td("The same fields as a natural person, as far as possible. Understand the ownership and control structure, including intermediate layers.", "盡量收集與自然人相同的資料。了解擁有權及控制權結構，包括任何中介層。", "¶4.4.2, 4.4.13")
    + td("Scaled to the risk of the customer and relationship: records of the beneficial owner in the public domain, documents or information from a reliable and independent source obtained through the customer, or the customer's declaration corroborated with public information. Registers such as the significant controllers register may assist in identifying. In an exceptionally low-risk case such as a charitable trust, information from the customer (including verified trustees), with confirmation that the beneficial owners are known to the customer, may be reasonable.",
         "按客戶及業務關係的風險而定：使用在公共領域的實益擁有人紀錄、要求客戶提供根據可靠及獨立來源取得的文件或資料，或使用公開資料核對客戶的承諾或聲明。重要控制人登記冊一類登記冊可協助識別。在風險極低的情況下（例如慈善信託），根據客戶（包括已核實身分的受託人）提供的資料，並確認有關人士為客戶所知悉，亦可能是合理做法。", "¶4.4.1, 4.4.3 fn 27", '<span class="answer">' + chip_reas + '</span>')
    + '<td>' + B("Not the customer's list: the Ordinance sets a different, risk-based verification standard for a beneficial owner (see Verify).", "並非客戶的來源清單：打擊洗錢條例對實益擁有人的身分核實規定與客戶不同，按風險而定（見「核實」一欄）。") + U.flag() + cite_html("¶4.4.3") + '</td>' + '</tr>'
    + '<tr>' + th("(c) Purpose and intended nature", "(c) 目的及擬具有的性質", "s.2(1)(c) · ¶4.6")
    + td("Obtain information on the purpose and intended nature of the business relationship, unless it is obvious. For a customer that is not a natural person, also understand the nature of its business.", "取得業務關係的目的及擬具有的性質的資料，除非顯而易見。客戶並非自然人時，亦須了解其業務性質。", "¶4.1.3(c), 4.6.1")
    + td("Commensurate with the customer's risk profile and the nature of the relationship. Under SDD the purpose may be inferred from the type of transaction.", "與客戶的風險狀況及業務關係的性質相稱。簡化盡職審查下，可按交易類別推斷目的。", "¶4.6.1, 4.8.8(e)", '<span class="answer">' + chip_und + '</span>')
    + '<td>—</td></tr>'
    + '<tr>' + th("(d) Person purporting to act (PPTA)", "(d) 看似代表客戶行事的人", "s.2(1)(d) · ¶4.5")
    + td("Decide who counts as a PPTA by their role, the activities they are authorised to conduct, and the risk. Identify them like a natural or legal person.", "按其角色、獲授權進行的活動及所涉風險，判斷誰屬看似代表客戶行事的人。按自然人或法人的規定識別。", "¶4.5.1, 4.5.3")
    + td("to verify identity, and with documentary evidence such as a board resolution or similar written authorisation.", "核實身分；並以文件證據（例如董事會決議案或類似書面授權）核實授權。", "¶4.5.2, 4.5.4", '<span class="answer">' + chip_reas + chip_auth + '</span>')
    + td("Governmental body, CCE or RA, equivalent overseas authority, other CCE-recognised source.", "政府機構、關長或有關主管當局、香港以外職能相類似的主管當局、關長認可的其他來源。", "¶4.5.2(a)") + '</tr>'
    + '<tr class="note"><td colspan="4">' + B("<b>Connected parties</b> of a customer that is a legal person or trust are its directors (corporation), partners (partnership), trustees or equivalent (trust or similar arrangement), or in other cases a natural person holding a senior management position or having executive authority in the customer. Obtain their <b>names</b> only, unless one also counts as the customer, a beneficial owner or a PPTA: then identify and verify them under that requirement.", "屬法人、信託或其他類似法律安排的客戶的<b>有關連者</b>，即董事（法團）、合夥人（合夥）、受託人或同等身分的人（信託或其他類似法律安排），或在其他情況下為客戶擔任高級管理職位或掌握執行權力的自然人。只須收集其<b>姓名</b>；但如同時符合客戶、實益擁有人或看似代表客戶行事的人的定義，則須按相關規定識別和核實其身分。") + ' ' + cite_html("¶4.3.18–4.3.19 fn 26") + '</td></tr>'
    + '<tr class="note"><td colspan="4">' + B("<b>Documents</b> should be current when obtained; when a natural-person customer, or someone representing a legal person, trust or similar arrangement, is physically present for CDD to establish a business relationship, you should generally have your staff sight the original identification document and keep a copy. Where no original can be produced, for example an electronic document, take appropriate measures to ensure reliability; take steps to be satisfied with foreign-language documents; consider applying anti-fraud procedures commensurate with the risk profile of the person being verified. You need not prove every collected field.", "<b>文件</b>在取得時應反映現況；屬自然人的客戶或代表法人、信託或其他類似法律安排建立業務關係的人為盡職審查程序而現身時，通常可由職員查看識別文件的正本，並保存該文件的複本。如未能出示正本，例如文件為電子版本，應採取適當措施確保文件可靠；外語文件應採取適當步驟確認；應考慮採取防止詐騙的程序，其程度與正接受身分核實的人的風險狀況相稱。收集的每項資料毋須逐一證實。") + ' ' + cite_html("¶4.3.13–4.3.17") + '</td></tr>'
    + '<tr class="note"><td colspan="4">' + B("<b>Who is the customer?</b> The party you establish a relationship with or transact for. The beneficiary of an outward wire transfer, with no other relationship, is not. A trustee that enters the relationship for a trust without legal personality is also your customer.", "<b>誰是客戶？</b>與你建立業務關係或由你為其進行交易的一方。付款電傳轉帳的收款人（與你沒有其他關係）並非客戶。代表沒有獨立法律人格的信託建立業務關係的受託人，亦是你的客戶。") + ' ' + cite_html("¶4.1.4–4.1.5, 4.3.10") + '</td></tr>'
    + '</tbody></table></div>'
    + U.traps(
        U.trap(("Residential address: collect it, no need to verify it", "住址：須收集，毋須核實"), None, "¶4.3.3, 4.3.5 fn 18",
               vs=[(("Collect", "收集"), ("You should obtain the residential address of a customer who is a natural person.", "你應向屬自然人的客戶索取住址資料。")),
                   (("Verify", "核實"), ("Not part of the check: you verify name, date of birth, ID number and document type. If you ask for address proof for another reason, such as a group or overseas rule, tell the customer clearly why.", "不屬核實範圍：須核實的是姓名、出生日期、識別號碼及文件類別。如因其他目的（例如集團或外地規定）要求住址證明，應向客戶清楚說明理由。"))]),
    ))

S3 = sec('bo', ["¶4.4", "s.1–2 Sch. 2"], ("Beneficial owner: follow the chain to a natural person", "實益擁有人：沿擁有權鏈追蹤至自然人"),
    P("For a corporation the test is owning or controlling, directly or indirectly, <b>more than 25%</b> of the shares or voting rights, or <b>ultimate control over management</b>, or being the person the corporation acts for. Indirect holdings count, so follow the chain of ownership through each intermediate layer to the natural persons behind it. In the chart, multiplying 50% × 60% is only a way to work out each person's indirect share; control of an intermediate layer also counts.",
      "就法團而言，準則是直接或間接擁有或控制<b>25%以上</b>的股本或投票權，或對管理行使<b>最終控制權</b>，或法團代其行事的人。間接持有亦計算在內，因此須沿擁有權鏈狀架構穿透每個中介層，追蹤至背後的自然人。圖中把50% × 60%相乘，只是計算間接持股的方法；控制中介層亦須計算。")
    + U.fig(fig3, ("Peak Holdings is a shareholder but not a beneficial owner: a beneficial owner is a natural person, so look through it. Mr Wong and Ms Ho each hold 30% of the customer indirectly (half of Peak's 60%), so both are beneficial owners alongside Ms Chan. Mr Lee at 10% is a director, so a connected party whose name you record, and a beneficial owner only under the control limb.",
                   "峰匯控股是股東但非實益擁有人：實益擁有人是自然人，須穿透該公司。王先生及何女士各間接持有客戶30%（峰匯所持60%的一半），故與陳女士同屬實益擁有人。李先生持有10%並任董事，屬有關連者（記錄姓名），只有在控制權一項下才屬實益擁有人。"),
            U.legend([('ok', ("a beneficial owner", "實益擁有人")), ('faint', ("a company in the chain: look through it", "擁有權鏈中的公司：須穿透")),
                      ('', ("the customer, or a person who is not a beneficial owner by ownership", "客戶，或以擁有權計並非實益擁有人的人"))]))
    + U.table([U.th("If the customer is", "如客戶是"), U.th("Its beneficial owner is", "其實益擁有人是")], [
        U.tr(U.rh("A corporation", "法團", "¶4.4.6 · s.1 Sch. 2"), U.td("An individual who owns or controls, directly or indirectly, including through a trust or bearer shares, <b>more than 25%</b> of the issued share capital; or is entitled to exercise or control <b>more than 25%</b> of the voting rights at general meetings; or exercises <b>ultimate control</b> over the management. If the corporation acts for another person, that person",
                                                                                  "直接或間接（包括透過信託或持票人股份）擁有或控制已發行股本<b>25%以上</b>的個人；或有權行使或支配成員大會上<b>25%以上</b>投票權的個人；或對管理行使<b>最終控制權</b>的個人。如法團代另一人行事，即該另一人")),
        U.tr(U.rh("A partnership", "合夥", "¶4.4.7 · s.1 Sch. 2"), U.td("An individual entitled to or controlling <b>more than 25%</b> of the capital or profits, or <b>more than 25%</b> of the voting rights, or exercising ultimate control over the management; or the person the partnership acts for",
                                                                             "有權攤分或控制資本或利潤<b>25%以上</b>、或<b>25%以上</b>投票權的個人，或對管理行使最終控制權的個人；或合夥代其行事的人")),
        U.tr(U.rh("A trust", "信託", "¶4.4.10–4.4.12 · s.1 Sch. 2"), U.td("The settlor; the trustee; any protector or enforcer; beneficiaries, or a class of them, entitled to a vested interest in the trust property; and any individual with ultimate control, including through a chain. For a class of beneficiaries, obtain enough to identify them at payout or when they exercise their rights",
                                                                                     "財產授予人；受託人；保護人或執行人（如有）；有權享有信託財產的既得權益的受益人或某類別受益人；以及擁有最終控制權的個人（包括透過控制或擁有權鏈）。按類別指定的受益人，須取得足夠資料，以便在付款或行使權利時確定其身分")),
        U.tr(U.rh("Any other body, such as an unincorporated association", "其他團體，例如非法團團體", "¶4.4.8 · s.1 Sch. 2"), U.td("An individual who ultimately owns or controls it, or the person it acts for", "最終擁有或控制該團體的個人，或該團體代其行事的人")),
        U.tr(U.rh("A natural person", "自然人", "¶4.4.5"), U.td("The customer is the beneficial owner. There is no proactive search, but enquire where the transactions or other circumstances suggest they act for someone else", "客戶本人就是實益擁有人。毋須主動追尋，但如交易特徵或其他情況顯示客戶代他人行事，則須查詢")),
        U.tr(U.rh("Nobody meets the definition", "無人符合定義", "¶4.4.9"), U.td("Identify the <b>senior managing official</b> instead, and take reasonable measures to verify their identity", "改為識別擔任<b>高級管理人員</b>的相關自然人，並採取合理措施核實其身分")),
        '<tr class="divhead"><td colspan="2">' + B("Structures that need extra steps", "須採取額外步驟的架構") + '</td></tr>',
        U.tr(U.rh("Bearer shares", "持票人股份", "¶4.4.15–4.4.17"), U.td("Deposited with an authorised/registered custodian: independent confirmation, re-confirmed at each periodic review. Not deposited: declarations from each beneficial owner before account opening and <b>every year</b> after, with immediate notice of any change",
                                                                                 "存放於認可╱註冊保管人：取得獨立確認，並在每次定期覆核時再確認。並非存放：開戶前及其後<b>每年</b>向每名實益擁有人索取聲明，擁有權變動須即時知會")),
        U.tr(U.rh("Nominee shareholders", "代名人股東", "¶4.4.18"), U.td("Satisfactory evidence of who the nominees are, who they act for, and the arrangement between them", "取得令你信納的證據，證明代名人、其所代表的人及有關安排的詳情")),
        U.tr(U.rh("A complex structure", "繁複的架構", "¶4.4.4, 4.4.14"), U.td("Find who has ultimate ownership or control over the customer, or who constitutes its controlling mind and management, and obtain enough to be satisfied the structure has a legitimate reason", "找出誰是最終擁有或控制客戶的人，或誰是控制及管理客戶的主腦；並取得足夠資料，信納採用該架構有合法理由")),
    ], minw=700)
    + U.traps(
        U.trap(("More than 25%, not 25% or more", "是25%以上，不是25%或以上"),
               ("Someone holding exactly 25% is not a beneficial owner by ownership. The test is strictly more than 25%, for shares, voting rights, and a partnership's capital or profits alike. Trust beneficiaries have no percentage test at all.",
                "持有剛好25%的人，並不因擁有權而成為實益擁有人。準則是嚴格的「25%以上」，股本、投票權，以及合夥的資本或利潤皆然。信託受益人則完全不設百分比門檻。"),
               "s.1 Sch. 2"),
        U.trap(("A holding company in the chain is not the beneficial owner", "擁有權鏈中的控股公司並非實益擁有人"),
               ("A beneficial owner is the natural person who ultimately owns or controls the customer, or on whose behalf a transaction or activity is being conducted. A holding company is not a natural person, so it is not a beneficial owner itself: follow the chain of ownership through every intermediate layer to the individuals who own or control it.",
                "實益擁有人是指最終擁有、控制客戶或由客戶代其進行交易或活動的自然人。控股公司並非自然人，本身不是實益擁有人：須沿擁有權鏈狀架構穿透每個中介層，追蹤至擁有或控制該公司的個人。"),
               "¶4.4.1, 4.4.13"),
        U.trap(("A trust beneficiary has no 25% threshold", "信託受益人不設25%門檻"),
               ("Every beneficiary, or class of beneficiaries, entitled to a vested interest in the trust property is a beneficial owner, whether the interest is in possession or in remainder or reversion and whether it is defeasible or not. Unlike the tests for a corporation or a partnership, the definition for a trust sets no percentage.",
                "凡有權享有信託財產的既得權益的受益人或某類別受益人，均屬實益擁有人，不論該受益人是享有該權益的管有權、剩餘權或復歸權，亦不論該權益是否可予廢除。與法團或合夥的準則不同，信託的定義不設任何百分比。"),
               "s.1 Sch. 2 · ¶4.4.10"),
    )
    + numreq([
        (("more than 25%", "25%以上"),
         ("Identify the person, and take reasonable measures to verify their identity", "識別該人，並採取合理措施核實其身分"),
         ("Shares, voting rights, or capital or profits, held directly or indirectly", "直接或間接持有的股本、投票權，或資本或利潤"),
         ("Missing a beneficial owner breaches a specified provision, and leaves your PEP and sanctions screening incomplete", "遺漏實益擁有人即違反指明的條文，並令政治人物及制裁篩查不完整"),
         "¶4.4.6–4.4.7 · s.2(1)(b) Sch. 2"),
        (("nobody over 25%", "無人超過25%"),
         ("Identify the senior managing official instead, and verify by reasonable measures", "改為識別高級管理人員，並採取合理措施核實"),
         ("No natural person meets any limb of the beneficial owner definition", "沒有自然人符合實益擁有人定義的任何一項"),
         ("Stopping at the corporate shareholder leaves the customer with no identified beneficial owner at all", "若止步於法團股東，該客戶便完全沒有已識別的實益擁有人"),
         "¶4.4.9"),
        (("every year", "每年一次"),
         ("Obtain a declaration from each beneficial owner of the shares", "向每名該等股份的實益擁有人索取聲明"),
         ("The customer has bearer shares that are not deposited with an authorised/registered custodian", "客戶持有並非存放於認可╱註冊保管人的持票人股份"),
         ("Ownership cannot be established, so the higher risk the Guideline attaches to bearer shares stays unmitigated", "無法確立擁有權，指引就持票人股份所指的較高風險因而未獲緩減"),
         "¶4.4.17"),
    ]))

S4 = sec('timing', ["¶4.7", "s.3(1)–(4) Sch. 2"], ("Timing: verify before or during, only exceptionally after", "核實的時間：之前或過程中；例外情況才可其後"),
    U.fig(fig5, ("Delayed verification is a managed exception for a business relationship, not a convenience, and it does not exist for an occasional transaction. The three conditions in the amber box are cumulative; the red box is what follows if the timeframe passes.",
                 "延遲核實是業務關係的受管控例外，不是便利；非經常交易則沒有此例外。琥珀色方格內三項條件須同時符合；紅色方格是時限屆滿後應採取的行動。"),
          U.legend([('ok', ("verify here: the normal case", "一般情況：在此核實")), ('may', ("the exception you may use", "你可以選用的例外")), ('must', ("what you should do once the timeframe passes", "時限屆滿後應採取的行動")), ('stop', ("not allowed", "不容許"))]))
    + U.table([U.th("While verification is pending", "核實尚未完成期間"), U.th("What applies", "適用規定")], [
        U.tr(U.rh("Your policies should include", "政策及程序應包括", "¶4.7.3"), U.td("(a) a reasonable <b>timeframe</b> to finish, and what happens when it is exceeded, such as suspending or ending the relationship; (b) <b>limits</b> on the number, types and amount of transactions; (c) <b>monitoring</b> of large and complex transactions outside the norm for that relationship; (d) <b>senior management</b> kept periodically informed of pending cases; (e) <b>no payment to third parties</b>, except as in the next row",
                                                                                 "(a) 完成核實的合理<b>時限</b>，以及逾時的跟進行動（例如暫停或終止業務關係）；(b) 對交易的次數、類別及款額設<b>限額</b>；(c) <b>監察</b>與這類業務預期常規有異的大額及複雜交易；(d) 定期向<b>高級管理層</b>報告尚未完成的個案；(e) <b>不向第三者付款</b>，下一行所述情況除外")),
        U.tr(U.rh("Paying a third party before verification", "核實前向第三者付款", "¶4.7.3(e)"), U.td("Only if <b>all four</b> hold: no suspicion of ML/TF; the risk is assessed as low; senior management approves, having regard to the customer's business; and the recipients' names do not match watch lists such as terrorist and PEP lists",
                                                                                                  "只有在<b>四項條件全部</b>符合時方可：沒有洗錢或恐怖分子資金籌集的懷疑；風險評估為低；高級管理層顧及客戶的業務性質後批准；以及收款人姓名與恐怖分子及政治人物等監察名單不符")),
        U.tr(U.rh("If the timeframe passes", "如時限屆滿", "¶4.7.4 · 4.13.1"), U.td("End the relationship as soon as reasonably practicable; carry out no further transactions except to <b>return funds or other assets in their original form as far as possible</b>; and consider whether the failure itself gives grounds for suspicion and a report, especially if the customer, without a justifiable reason, asks for funds to go to a third party or be transformed, for example cash into a cashier order",
                                                                                          "在合理地切實可行的範圍內盡快終止業務關係；除<b>在可行情況下將資金或其他資產以原狀退回</b>外，不再進行交易；並評估未能完成核實是否構成懷疑理據，並考慮應否舉報，尤其當客戶在無充分理由下要求將資金轉移給第三者或「轉變」資金（例如把現金轉為銀行本票）")),
        U.tr(U.rh("The Guideline's own examples", "指引所舉的例子", "¶4.7.2"), U.td("Securities transactions that must execute at market speed; and life insurance, where the beneficiary may be verified after the policyholder, but at or before payout or the exercise of vested rights",
                                                                                          "須按市況迅速執行的證券交易；以及人壽保險：受益人可在保單持有人之後核實，但須在付款或行使既得權利時或之前完成")),
    ], minw=680)
    + numreq([
        (("before or during", "之前或過程中"),
         ("Verify the identity of the customer and of any beneficial owner", "核實客戶及任何實益擁有人的身分"),
         ("Establishing a business relationship, or carrying out an occasional transaction", "建立業務關係或執行非經常交易時"),
         ("Verifying after an occasional transaction, or after starting a business relationship without meeting all three exception conditions, breaches a specified provision (the exception covers business relationships only)", "在執行非經常交易後才核實，或未符合三項例外條件而在建立業務關係後才核實，即違反指明的條文（例外只適用於業務關係）"),
         "¶4.7.1 · s.3(1), (1A), (2) Sch. 2"),
        (("a reasonable timeframe", "合理時限"),
         ("Finish the delayed verification. You set the period yourself, in your risk management policies", "完成延後的核實。期限由你在風險管理政策中自行訂定"),
         ("You allowed the relationship to start before verification, under the exception", "你按例外情況，在核實前已容許業務關係開始"),
         ("Terminate as soon as reasonably practicable, return funds or other assets in their original form as far as possible, and consider a report to the JFIU", "在合理地切實可行範圍內盡快終止關係，在可行情況下以原狀退回資金或其他資產，並考慮向財富情報組報告"),
         "¶4.7.3(a), 4.7.4"),
    ]))
