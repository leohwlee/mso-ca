"""Source-authored bilingual manuscript; source-checked 2026-10-19. No bank input."""
from model import p, ref, block, section

PART = dict(title=p('金錢服務經營者的系統及管控措施（二）：打擊洗錢及恐怖分子資金籌集的管控範疇', 'MSO systems and controls (ii): AML/CFT control areas'),
intro=p('本部分按實際管控範疇整理：識別客戶及背後人士、判定審查程度、監察交易、篩查制裁，以及處理匯款和交付渠道。規定須連同觸發條件及例外一起記。', 'This part covers operational controls: identifying customers and the people behind them, setting due-diligence intensity, monitoring, sanctions screening, transfers and delivery channels. Learn each requirement with its trigger and exceptions.'), sections=[
section('cdd', '客戶盡職審查：定義及四項措施', 'Customer due diligence: definition and four measures', [
    block('四項基本措施', 'Four basic measures', [
        ('識別客戶，並以可靠及獨立來源的文件、數據或資料核實其身分。', 'Identify the customer and verify identity using documents, data or information from a reliable, independent source.'),
        ('有實益擁有人時，識別並採取合理措施核實其身分，使機構信納知道其為誰；法人及信託亦須了解擁有權及控制結構。', 'Identify any beneficial owner and take reasonable identity-verification measures so the MSO is satisfied it knows who that person is; understand ownership/control structures of legal persons and trusts.'),
        ('取得業務關係目的及擬具有的性質資料；若已顯而易見，毋須另行取得。客戶不是自然人時，亦須了解其業務性質。', 'Obtain information on the purpose and intended nature of the relationship unless obvious. Where the customer is not a natural person, also understand the nature of its business.'),
        ('有人代表客戶行事時，識別及採取合理措施核實代表的身分，並核實其授權。代表的身分及授權是兩件事，均須處理。', 'If someone acts for the customer, identify and take reasonable measures to verify the representative’s identity, and verify authority. Identity and authorisation are separate requirements.'),
    ], [
        ref('03', '第4.1.1–4.1.5、4.6.1段', '¶4.1.1–4.1.5, 4.6.1', 'The following are CDD measures applicable to an MSO'),
    ], kind='list'),
    block('客戶的界定', 'Who is the customer', [
        ('客戶通常是建立業務關係或由機構為其執行交易的一方，不通常包括交易第三方。例如對匯出機構而言，僅作收款且沒有其他關係的受款人不自動成為其客戶。', 'The customer is generally the party with whom the relationship is established or for whom the transaction is carried out, usually excluding third parties. A beneficiary of an outward transfer with no other relationship is not automatically the ordering MSO’s customer.'),
        ('與法人建立關係時須識別法人本身，不能只識別到櫃台辦理的個人而把代表當作法人客戶。', 'Identify the legal-person customer itself; identifying the individual at the counter does not substitute for identifying the represented company.'),
    ], [
        ref('03', '第4.1.4–4.1.5段', '¶4.1.4–4.1.5', 'generally excludes the third parties'),
        ref('07', '附錄第(3)部分，第5頁', 'Appendix (3), p.5', 'treated a PPTA as the customer'),
    ], kind='list'),
]),
section('triggers', 'CDD觸發條件、金額及相連交易', 'CDD triggers, thresholds and linked transactions', [
    block('必須執行的情況', 'When CDD is required', [
        ('建立業務關係之前須執行CDD，不以交易金額為前提。業務關係是具有持續性，或機構在首次接觸潛在客戶時預期具有持續性的業務、專業或商業關係。', 'Perform CDD before establishing a business relationship regardless of amount. A relationship has an element of duration, or is expected to have one when the potential customer first contacts the MSO.'),
        ('非經常交易是與沒有業務關係的客戶進行的交易。一般非經常交易達港幣120,000元或等值外幣，電傳轉帳達港幣8,000元，虛擬資產轉帳涉及價值不少於港幣8,000元，均在執行前觸發CDD。', 'An occasional transaction is with a customer without a business relationship. CDD is required before general occasional transactions of at least HK$120,000/equivalent, wire transfers of at least HK$8,000/equivalent, and virtual-asset transfers worth at least HK$8,000.'),
        ('單筆或機構認為看來相連的多筆交易都計算；同一受款人短時間收到一個或多個來源付款，或客戶經常向同一／多個目的地轉帳，均可構成相連線索。', 'Count single operations and operations that appear linked. Payments to the same recipient from one/more sources over a short period, or regular transfers to destinations, may indicate linkage.'),
        ('懷疑客戶／戶口涉及洗錢或恐怖分子資金籌集，或懷疑原有識別／核實資料的真實性或充分性時，亦須CDD；不受金額門檻限制。', 'Suspicion of ML/TF involving the customer/account, or doubts about the truth/adequacy of existing identification/verification information, also triggers CDD without a monetary threshold.'),
        ('另有非電傳匯款達港幣8,000元的發款人核實及紀錄要求，詳見本部分「匯款」；不可只記一般120,000元門檻。', 'Non-wire outward remittances of at least HK$8,000 have separate originator-verification and record requirements, explained under Remittances below; do not rely solely on the general HK$120,000 threshold.'),
    ], [
        ref('03', '第4.2.1–4.2.5、11.3段', '¶4.2.1–4.2.5, 11.3', 'whether the transaction is carried out in a single operation'),
    ], kind='list'),
    block('第三方現金交易', 'Third-party cash transactions', [
        ('非戶口授權名單人士代存現金達港幣120,000元時，機構應要求其身分文件並保留副本，以便持續監察；與客戶風險背景不符的大額現金須特別留意。', 'For a cash transaction of at least HK$120,000 by a person not on the account mandate, request and copy that person’s identity document for monitoring. Large cash amounts inconsistent with the customer profile require particular attention.'),
    ], [
        ref('03', '第4.2.6段', '¶4.2.6', 'whose name does not appear on the mandate'),
    ], kind='list'),
]),
section('identity', '身分資料：自然人、法人與信託', 'Identity information: individuals, legal persons and trusts', [
    block('收集與核實須分開', 'Distinguish collection from verification', [
        ('自然人至少收集全名、出生日期、國籍、獨特識別號碼及文件類別；核實全名、出生日期、號碼及文件類別。亦須取得居住地址資料，但不代表一律要另取地址證明。', 'For individuals collect at least full name, date of birth, nationality, unique ID number and document type; verify name, birth date, number and type. Obtain residential address information; this does not impose universal separate address-proof verification.'),
        ('法人至少收集全名、成立／註冊日期及地點（包括註冊辦事處地址）、識別號碼／文件類別，以及不同於註冊地址的主要營業地點。核實名稱、法律形式、當時仍然存在及規管／約束其權力。', 'For legal persons collect full name, incorporation/establishment/registration date and place (including registered office), ID number/type and principal business address if different. Verify name, legal form, current existence and governing/binding powers.'),
        ('法人核實可用註冊證明、獨立登記冊、存續或良好聲譽證明、合夥協議及章程等；通常成立證明只證名稱及法律形式，未必證明現時仍存在，可能要多於一份文件。', 'Verification sources include incorporation certificates, independent registries, incumbency/good-standing certificates, partnership agreements and constitutional documents. An incorporation certificate alone may not prove current existence, so multiple documents may be needed.'),
        ('信託／類似法律安排至少收集名稱、成立／設立日期、管限法律司法管轄區、官方識別號碼／文件類別（如有）及註冊辦事處地址（如適用）；核實名稱、形式、現時存在及約束權力，可用信託契據、適當登記冊或指定專業確認。', 'For trusts/similar arrangements collect name, establishment/settlement date, governing jurisdiction, official ID/type if any and registered office if applicable. Verify name, form, current existence and binding powers using a deed, suitable register or specified professional confirmation.'),
        ('信託受託人代表沒有獨立法人地位的信託建立關係／交易時，通常亦是客戶，須依其自然人或法人身分進行審查。', 'A trustee acting for a trust without separate legal personality is generally also the customer and must be checked under the relevant individual/legal-person requirements.'),
    ], [
        ref('03', '第4.3.2–4.3.13段及註18–20', '¶4.3.2–4.3.13; footnotes 18–20', 'cannot act as a proof of current existence'),
    ], kind='comparison'),
    block('文件可靠性及關連人士', 'Document reliability and connected parties', [
        ('核實資料須在提供／取得時仍有效，按風險採取防偽措施；在場客戶一般由職員查閱正本並保留副本，不能提供正本時須另確保可靠性。外文資料須採適當步驟確認其確能證明身分。', 'Verification information must be current when supplied/obtained, with risk-based anti-fraud measures. Generally sight originals and keep copies for physically present customers; ensure reliability where originals cannot be provided. Take suitable steps to understand foreign-language identity evidence.'),
        ('身分文件應有照片；確有例外且已妥善評估及緩減相關風險，才可接受沒有照片的文件。', 'Identity documents should contain a photograph; a non-photo document is acceptable only exceptionally with the associated risks properly assessed and mitigated.'),
        ('關連人士須取得姓名：公司董事、合夥人、信託受託人，其他情況為高級管理層或具執行權力的自然人。若該人同時是客戶、實益擁有人或代表，須另按較適用要求識別及核實，不能只記姓名。', 'Obtain connected-party names: directors, partners, trustees, or otherwise senior/executive natural persons. If someone is also customer, beneficial owner or representative, apply the corresponding identification/verification duties rather than collecting only a name.'),
    ], [
        ref('03', '第4.3.4、4.3.14–4.3.19段及註26', '¶4.3.4, 4.3.14–4.3.19; footnotes 26', 'identify all the connected parties'),
    ], kind='list'),
    block('常見文件情況', 'Common documentary situations', [
        ('旅行證件一般只須保留個人資料頁；姓名改變須核實新文件並與原有出生日期／識別號碼等核對。主要營業地址是實際主要營運地點，不一致須查詢。可靠獨立文件已有註冊地址且未知道已過期，可接受作地址資料。', 'Generally retain the travel-document biodata page. Verify a name change using new evidence and corroborate birth date/identifier. Principal business address means the actual main operating location; enquire into inconsistencies. A reliable independent document may evidence registered address unless known outdated.'),
        ('合夥可用登記紀錄、合夥協議／契據核實；非高風險可用適當摘錄／刪節版，但登記紀錄未必載有規管權力，可能須額外文件。具悠久歷史、良好聲譽及大量公開伙伴／控制人資料的知名機構，可按條件用專業／行業會員確認。', 'A partnership can be verified using registration or an agreement/deed; appropriate extracts/redactions may serve non-high-risk cases. Registration may not show governing powers, requiring another document. For well-known reputable organisations with long histories and substantial public partner/controller information, professional/trade membership confirmation may suffice under the stated conditions.'),
        ('了解擁有權結構是必須的，但不一定每次索取擁有權圖，亦不須例行核實每層中間公司的全部資料；按複雜性、風險及資料是否足以識別實益擁有人決定。', 'Understanding ownership/control is mandatory, but obtaining an ownership chart every time or routinely verifying all intermediate companies is not. Decide by complexity, risk and information sufficiency for BO identification.'),
        ('可靠來源的電子正本可以使用；客戶提供的列印本可須與登記冊等核對，機構直接從可靠來源下載者不必另作同一核對。翻譯須可靠適當，不一定必須由專業第三方提供。舊文件日後到期不自動要求重核，但仍須維持CDD資料更新。', 'Reliable electronic originals are usable. Customer-provided printouts may need registry corroboration, while direct downloads by the MSO from reliable sources need not repeat it. Translation must be appropriate/reliable, not necessarily by a professional third party. Later expiry alone does not automatically require re-verification; keep CDD current.'),
    ], [
        ref('06', '打擊洗錢問答A3–A8、A13–A15', 'AML/CFT FAQ A3–A8, A13–A15', 'biodata'),
    ], kind='list'),
    block('國籍核實、地址及更名的條件', 'Nationality verification, addresses and name-change conditions', [
        ('自然人的最低識別資料包括國籍；但第4.3.3段一般核實項目是姓名、出生日期、唯一識別號碼及證件類型，並非一律另行核實國籍。不能把「取得」和「核實」混為一談，也不能因此略去應取得的國籍資料。', 'Minimum identification information for an individual includes nationality, but the general verification set in paragraph 4.3.3 is name, birth date, unique identifier and document type. Nationality is not universally a separate verification item. Collection and verification are different tasks; nationality must still be obtained.'),
        ('須取得居住地址資料，不代表每個客戶一律交獨立地址證明。若客戶在建立關係前已更名，只需識別及核實現用姓名；關係建立後更名則核實新名並與既有出生日期／證件號碼核對，存疑可要求結婚證明或改名契。', 'Obtain residential-address information without imposing universal separate address proof. If a name changed before the relationship, identify/verify only the current name. For a later change, verify the new name and corroborate existing birth date/identifier, seeking a marriage certificate/deed poll if in doubt.'),
    ], [
        ref('03', '第4.3.2–4.3.5、4.3.13段及註17–18', '¶4.3.2–4.3.5, 4.3.13; footnotes 17–18', 'nationality'),
        ref('06', '打擊洗錢問答A4', 'AML/CFT FAQ A4', 'only the current name'),
    ], kind='list'),
    block('信託核實的五類來源與組織合法目的', 'Five trust-verification sources and legitimate organisational purpose', [
        ('信託的名稱、法律形式、現時是否存在及規管／約束權力，可參照：(1)信託契據或類似文書；(2)成立地的適當登記冊；(3)以專業身分行事的受託人書面確認；(4)已審閱有關文書的律師書面確認；(5)與MSO同一金融集團的信託公司書面確認，但須由該公司管理該信託。', 'To verify a trust’s name, legal form, current existence and regulating/binding powers, examples are (1) deed/similar instrument, (2) appropriate register in its establishment country, (3) professional trustee written confirmation, (4) written confirmation from a lawyer who reviewed the instrument, or (5) same-financial-group trust-company confirmation, only where that company manages the trust.'),
        ('特殊情況可保留遮蓋部分內容的契據副本；適當登記冊須有足夠透明度，並保持擁有／控制資料更新。專業受託人的業務包括信託管理／行政服務，並非任何自稱受託人的個人都符合這一項。', 'A redacted deed copy may exceptionally be retained. An appropriate register needs adequate transparency and current ownership/control information. A professional trustee provides trust administration/management services in a profession/business; not every self-described trustee qualifies for that alternative.'),
        ('協會、會所、社團、慈善團體、宗教組織、學會、互助／友愛社團、合作／公積社團等，另須信納其合法目的，例如查閱章程；核實註冊資料不能取代這項目的了解。', 'For associations, clubs, societies, charities, religious bodies, institutes, mutual/friendly societies and cooperative/provident societies, also satisfy yourself as to legitimate purpose, for example by sighting the constitution. Registration checks do not replace this purpose enquiry.'),
    ], [
        ref('03', '第4.3.9、4.3.12段及註23–25', '¶4.3.9, 4.3.12; footnotes 23–25', 'written confirmation from a trust company which is within the same financial group'),
    ], kind='list'),
]),
section('identity-evidence', '身分文件與核證副本', 'Identity documents and certified copies', [
    block('常用文件與例外', 'Documents and exceptions', [
        ('親身在香港的香港居民，使用香港身分證或簽證身分書；非居民使用有效旅行證件。沒有親身在香港的非居民，應使用有效護照／其他旅行證件、有照片的國民身分證或有效附照片國民駕駛執照。國際駕駛許可證／執照不獲接受。', 'For residents physically in Hong Kong use an HK identity card or document of identity; for non-residents use a valid travel document. For non-residents not physically in Hong Kong, a valid passport/travel document, photo national ID or valid photo national driving licence may be used. International driving permits/licences are not acceptable.'),
        ('旅行證件不只護照；指引亦列澳門永久性居民身分證、台灣居民來往大陸通行證、海員身分證、往來台灣通行證、澳門居民入境許可證、因公往來港澳通行證及往來港澳通行證。', 'Travel documents are not limited to passports: the list includes Macau permanent resident ID, Mainland Travel Permit for Taiwan Residents, Seaman’s Identity Document, Taiwan Travel Permit for Mainland Residents, permits for Macau residents, and official-purpose/ordinary exit-entry permits for Hong Kong and Macau.'),
        ('香港出生而沒有有效旅行證件或身分證的未成年人，可用香港出生證明核實；同時記錄及核實代表／陪同的父母或監護人身分。無國民身分證制度且客戶無有照片旅行證件／駕照的地區，可在例外及RBA下接受其他證據，盡量有照片。', 'For a Hong Kong-born minor without a valid travel document/ID, verify using the birth certificate and record/verify the representing/accompanying parent or guardian. In jurisdictions without national IDs, where the customer lacks a photo travel document/licence, other evidence may exceptionally be accepted under RBA, preferably with a photograph.'),
    ], [
        ref('03', '附錄A第1–6段及註72–73', 'Appendix A ¶1–6, footnotes 72–73', 'international drivers permits and licences are not acceptable'),
    ], kind='list'),
    block('核證程序及責任', 'Certification and responsibility', [
        ('核證者須獨立及適當，並親眼看過正本。例子包括合資格中介人、對等司法管轄區司法人員、證件發出國使領館人員、太平紳士，以及會計師、律師、公證人或特許秘書等專業人士。', 'The certifier must be independent and appropriate and have seen the original. Examples include eligible intermediaries, equivalent-jurisdiction judiciary, embassy/consulate officials of the issuing country, Justices of the Peace and professionals such as accountants, lawyers, notaries and chartered secretaries.'),
        ('副本須簽署及註明日期、清晰列出姓名及職銜／身分，並聲明與正本相符。一般客戶自行核證不足；法人客戶內受專業操守約束的專業人士以其專業身分核證，可屬例外。', 'The copy needs signature/date, clear name and position/capacity and a true-copy statement. Customer self-certification is generally insufficient, but a professional within a legal-person customer may qualify if bound by professional conduct rules and acting professionally.'),
        ('接受核證副本不會轉移CDD責任。來源地高風險、核證者不受規管，或對真偽／與客戶關係有疑問時，須採額外緩解措施。', 'Certified copies do not transfer CDD responsibility. Apply extra safeguards for higher-risk origins, unregulated certifiers or doubts about authenticity or whether the evidence relates to the customer.'),
    ], [
        ref('03', '附錄A第7–10段及註74–76', 'Appendix A ¶7–10, footnotes 74–76', 'the certifier will need to have seen the original'),
    ], kind='list'),
    block('查冊、核證與地址要求的補充', 'Company searches, certification and address requirements', [
        ('公司註冊證書本身不證明現時存在；採公司登記查冊時應取得完整公司查冊報告。核證人除簽署、日期、身分及原件真確副本聲明外，應在簽署下以大寫清晰列印姓名。', 'An incorporation certificate alone does not prove current existence; registry verification should obtain a full company search report. In addition to signature/date/capacity and true-copy statement, the certifier should clearly print the name in capitals below the signature.'),
        ('第03份附錄A的證件辨認說明包括香港居民年滿11歲須登記領取身分證，以及永久居民身分證出生日期下的A字標記。這是本版附錄的辨認細節，不把單一標記當成身分核實全套程序。', 'Document 03 Appendix A notes Hong Kong resident registration for an identity card from age 11 and the A marker beneath date of birth on permanent HKIDs. These are recognition details in this edition, not a substitute for complete identity verification.'),
        ('指引不一律要求核實居住地址；集團政策或其他本地／境外法律監管要求可能需要。若要求核實，應向客戶清楚解釋原因，不能把機構額外要求誤說成指引對所有客戶的統一要求。', 'The Guideline does not universally require residential-address verification; group policy or other local/overseas legal/regulatory requirements may. Clearly explain the reasons to the customer and distinguish additional institutional requirements from a universal Guideline requirement.'),
    ], [
        ref('03', '第4.3.5段及註18', '¶4.3.5; footnotes 18', 'communicate clearly to the customer the reasons'),
        ref('03', '附錄A第4–5、9段及註73、76', 'Appendix A ¶4–5, 9; footnotes 73, 76', 'obtaining a full company search'),
    ], kind='list'),
]),
section('beneficial-owners', '實益擁有人：擁有權、控制與代他人行事', 'Beneficial owners: ownership, control and acting for another', [
    block('定義及控制標準', 'Definitions and control tests', [
        ('實益擁有人是最終擁有／控制客戶，或交易為其進行的人。自然人客戶通常本身就是實益擁有人；有跡象顯示並非為自己行事時，須適當查詢。', 'A beneficial owner ultimately owns/controls the customer or is the person on whose behalf the transaction is conducted. An individual customer is normally its own beneficial owner, but contrary indications require enquiries.'),
        ('公司：直接／間接擁有或控制超過25%股本、可行使／控制超過25%表決權，或最終控制管理層的自然人；客戶代別人行事亦包括該人。超過25%包括25.1%及25.5%，不是到26%才符合。恰好25%不符合比例條件，但可能因管理控制等另一準則符合。', 'For corporations: individuals directly/indirectly owning/controlling more than 25% of capital or voting rights, or exercising ultimate management control; also the person for whom it acts. More than 25% includes 25.1% and 25.5%; the threshold is not 26%. Exactly 25% does not satisfy the percentage test alone, but another control test may apply.'),
        ('合夥：超過25%資本／利潤或表決權，或最終控制管理的自然人；非合夥的非法團組織：最終擁有或控制的自然人，及代其行事的其他人。', 'For partnerships: individuals with more than 25% of capital/profits/votes or ultimate management control; for other unincorporated bodies: ultimate owning/controlling individuals and persons for whom the body acts.'),
        ('信託：對信託財產有既得權益的受益人／受益人類別、財產授予人、受託人、保護人／執行人及最終控制的自然人。按特徵或類別指定受益人，須有足夠資料以便支付或行使既得權利時確定其身分。', 'For trusts: vested-interest beneficiaries/classes, settlor, trustee, protector/enforcer and individuals with ultimate control. For beneficiaries designated by characteristics/class, obtain enough information to establish identity at payout or exercise of vested rights.'),
        ('法人客戶沒有任何自然人符合實益擁有人定義時，須識別高級管理人員並採合理措施核實身分；不是只因沒有人持股超過25%便立即停止追查控制權。', 'If no natural person meets the beneficial-owner definition, identify and reasonably verify senior managing officials. Absence of a shareholder above 25% alone does not end the search for control.'),
    ], [
        ref('03', '第4.4.1–4.4.12段', '¶4.4.1–4.4.12', 'more than 25% of the issued share capital'),
    ], kind='comparison'),
    block('核實及特殊結構', 'Verification and special structures', [
        ('採合理措施核實實益擁有人，程度按客戶／關係風險；可交叉核對可靠公開資料、客戶提供的獨立文件及聲明。複雜架構須了解每層及其合理理由，不能只停在中間公司。', 'Take reasonable risk-sensitive verification measures, corroborating public information, independent documents and customer declarations. Understand intermediate layers and legitimate reasons for complex structures; do not stop at an intermediate company.'),
        ('不記名股票由合資格保管人持有時，取得獨立證據、保管人及權益人的身分，定期確認；否則在開戶前及其後每年取得各實益擁有人聲明，並要求即時通知持有權變更。代名股東亦須查出其代表的人及安排。', 'For bearer shares with an authorised/registered custodian, obtain independent evidence and identities of custodian/entitled persons, confirming periodically. Otherwise obtain owner declarations before opening and annually and require immediate change notification. Identify nominee shareholders and their principals/arrangements.'),
    ], [
        ref('03', '第4.4.3–4.4.4、4.4.13–4.4.18段', '¶4.4.3–4.4.4, 4.4.13–4.4.18', 'annually thereafter from each beneficial owner'),
    ], kind='list'),
    block('實益擁有人資料與極低風險核實', 'BO information and exceptionally-low-risk verification', [
        ('應盡量設法取得與自然人客戶相同的BO識別資料：姓名、出生日期、國籍、唯一識別號碼及證件類型。核實須合理及按風險，可參照公開紀錄、可靠獨立資料或核對客戶聲明；「盡量取得」不等於一律豁免核實。', 'Endeavour as far as possible to obtain the same BO identification information as for individuals: name, birth date, nationality, unique identifier and document type. Reasonable risk-sensitive verification can use public records, reliable independent evidence or corroborated customer declarations; endeavouring to obtain information is not a general verification waiver.'),
        ('極低風險情況，例如慈善信託，可能合理地以客戶（包括已核實身分的受託人）提供的資料，及確認其認識該BO來確認身分。必須有相應極低風險判斷，不是所有慈善組織自動豁免。', 'Exceptionally low risk, such as a charitable trust, may justify confirmation using information from the customer, including verified trustees, and confirmation that the BO is known to the customer. This needs the exceptionally-low-risk context, not an automatic charity exemption.'),
        ('不記名認股權證是實體證書持有人可憑以取得法人擁有權的可轉讓文書。對不記名股票的保管／聲明等管控，同樣適用於這類權證及其他沒有可追查性的類似文書。', 'A bearer-share warrant is a negotiable physical certificate entitling its holder to ownership in a legal person. Bearer-share custody/declaration controls also apply to those warrants and similar untraceable instruments.'),
    ], [
        ref('03', '第4.4.2–4.4.3、4.4.15–4.4.17段及註30', '¶4.4.2–4.4.3, 4.4.15–4.4.17; footnotes 30', 'The same controls should be applied to bearer share warrants'),
    ], kind='list'),
    block('自然人與「人」的界線', 'Individuals versus “persons”', [
        ('公司／合夥的擁有權及控制分支追查自然人；但交易為其進行的人，以及信託的財產授予人、受託人、保障人／執行人等，須按各自定義識別，不能一律排除法人。替代識別高級管理人員，也不是把該人自動重新定義為BO。', 'Ownership/control limbs for corporations and partnerships trace individuals. But the person for whom a transaction is conducted and trust roles such as settlor, trustee and protector/enforcer must be identified under their respective definitions; legal persons are not universally excluded. Identifying senior managing officials as a fallback does not automatically redefine them as BOs.'),
    ], [
        ref('04', '附表2第1條', 'Schedule 2 s.1', 'beneficial owner'),
        ref('03', '第4.4.6–4.4.12段', '¶4.4.6–4.4.12', 'senior managing official'),
    ], kind='list'),
    block('認識：重要控制人登記冊及CDD的關係', 'Recognise: the significant controllers register and CDD', [
        ('2022年報告介紹重要控制人登記冊（SCR，Significant Controllers Register）：香港成立的公司須識別並保存重要控制人資料，上市公司獲豁除並另受證券法的披露規定約束。SCR由公司在註冊辦事處或香港訂明地點備存及更新，供執法人員依法查閱／複印；它不是把所有實益擁有人資料公開放在公司註冊處查冊系統。', 'The 2022 report describes the Significant Controllers Register (SCR): Hong Kong-incorporated companies identify and maintain significant-controller information; listed companies are exempt and subject to separate securities-law disclosure requirements. The company keeps and updates its SCR at its registered office or a prescribed Hong Kong place, making it available for lawful law-enforcement inspection/copying. This does not put all beneficial-owner details on the public Companies Registry search system.'),
        ('第7.24段列五種擇一控制條件：直接／間接持有超過25%已發行股份；直接／間接持有超過25%表決權；直接／間接有權委任或罷免過半數董事；有權或實際對公司行使重大影響力／控制；或對非屬法人的信託／商號活動有上述重大影響力／控制，而其受託人／成員就該公司符合前四項任何一項。超過25%（>25%）包括25.1%，不包括恰好25%；恰好25%仍可能符合其他控制條件。', 'Paragraph 7.24 gives five alternative control conditions: directly/indirectly holding >25% of issued shares; directly/indirectly holding >25% of voting rights; directly/indirectly having the right to appoint/remove a majority of directors; having the right to exercise or actually exercising significant influence/control over the company; or such influence/control over a trust/firm that is not a legal person, whose trustees/members meet any of the first four conditions for the company. >25% includes 25.1%, but not exactly 25%; exactly 25% may still meet another control condition.'),
        ('重要控制人包括最終有重大控制權的須登記人士（自然人或指明實體），以及有重大控制權且為公司成員的須登記法律實體（可在香港或境外成立）。因此SCR內可列法人，不能把它直接等同MSO須追查的所有自然人實益擁有人名單。公司須識別、核實及記錄最終控制自然人和中間法律實體的資料。', 'Significant controllers include registrable persons (natural persons or specified entities with ultimate significant control) and registrable legal entities with significant control that are members of the company, whether incorporated in Hong Kong or elsewhere. An SCR can therefore contain legal entities; it is not simply identical to the natural-person beneficial owners an MSO must trace. Companies identify, verify and record ultimate controlling individuals and intermediate legal entities.'),
        ('SCR須載有指定代表的姓名或名稱及聯絡資料。公司須指定代表協助執法人員：可為居於香港的自然人成員／董事／僱員，或會計專業人士、法律專業人士、持牌TCSP。報告說明執法機構依法查閱SCR無須先取得法庭命令；這項執法權不等於MSO有相同查閱權。', 'The SCR must contain the designated representative’s name and contact details. A company designates a representative to assist law enforcement: a member/director/employee who is a natural person resident in Hong Kong, or an accounting professional, legal professional or licensed TCSP. The report states that law-enforcement access for lawful functions does not require a court order; this does not confer the same access power on an MSO.'),
        ('2022年報告第7.25段說明：公司須向實益擁有人或相關人士送達通知，以書面確認實益擁有人的個人資料，並在訂明期限內匯報變動。沒有備存準確及最新的SCR，或拒絕執法部門依法查閱，屬刑事罪行。該段沒有列出具體日數，不應套用MSO牌照變更通知期限。', 'Paragraph 7.25 of the 2022 report describes notices to beneficial owners or related parties, written confirmation of beneficial owners’ particulars and reporting changes within the prescribed timeframe. Failure to keep an accurate, up-to-date SCR or refusal of lawful law-enforcement inspection is a criminal offence. The paragraph does not specify the number of days; MSO licensing notification deadlines must not be substituted.'),
        ('海關指引註27明確容許MSO參閱這類登記冊以協助識別實益擁有人；如資料不公開，可直接向客戶索取紀錄。仍須按本節核實及了解擁有權／控制結構，不能把取得SCR當作完成全部CDD。', 'Customs Guideline note 27 expressly permits reference to such registers to assist identification of beneficial owners; where not public, the MSO may obtain the record directly from the customer. The verification and ownership/control analysis in this section still apply; obtaining an SCR is not completion of all CDD.'),
    ], [
        ref('25', '2022年版，第7.20、7.24–7.27段及註201', '2022 edition, ¶7.20, 7.24–7.27 and note 201', 'Significant controllers include'),
        ref('03', '第4.4.3–4.4.4段及註27', '¶4.4.3–4.4.4 and note 27', 'An MSO may refer to such registers'),
    ], kind='list'),
]),
section('representatives', '代表客戶行事者與授權', 'Persons acting for customers and authorisation', [
    block('PPTA的身分及權力', 'PPTA identity and authority', [
        ('按角色、獲授權活動及風險判定代表客戶行事的人（PPTA），包括代表建立關係或獲授權發指示的人。須有清晰政策並一致執行；法人客戶一般至少有一位代表建立關係的人。', 'Determine PPTAs by roles, authorised activities and risk, including persons establishing the relationship or giving instructions. Apply clear, consistent policies; a legal-person customer generally has at least one such relationship-establishing representative.'),
        ('按自然人或法人相應要求取得及核實PPTA身分；另以董事會決議或類似書面授權等適當文件核實每位代表的權力。只取名片或口頭表示獲授權，不能代替驗證授權。', 'Apply relevant individual/legal-person identification and verification requirements, and separately verify each representative’s authority using appropriate evidence such as a board resolution or equivalent written authorisation. A business card or mere assertion does not establish authority.'),
    ], [
        ref('03', '第4.5.1–4.5.4段', '¶4.5.1–4.5.4', 'verify the authority of each PPTA'),
        ref('07', '附錄第(3)部分', 'Appendix (3)', 'at least one PPTA'),
    ], kind='list'),
    block('獲授權代表及低風險核實', 'Authorized representatives and low-risk verification', [
        ('公司可由經核實授權的僱員親身建立關係，不要求每名董事或實益擁有人都親身到場。被列為授權簽署人，只有在實際代表客戶行事的範圍內才須按PPTA要求處理。', 'A properly authorized employee may establish a corporate relationship in person; every director/BO need not attend personally. Authorized signatories require PPTA treatment when they act for the customer.'),
        ('低風險關係可用代表人名單作合理核實，但名單內身分及授權須由客戶內獨立於該等代表人的部門／人士確認，例如合規、審核或人力資源。仍須取得每名PPTA適用的基本識別資料，不能只存未經確認的姓名表。', 'For low-risk relationships a representative list may support reasonable verification where identity and authority are confirmed by an independent department/person within the customer, such as compliance, audit or HR. Obtain applicable basic identity details for every PPTA; an unconfirmed name list is insufficient.'),
    ], [
        ref('06', '打擊洗錢問答A9、A11–A12', 'AML/CFT FAQ A9, A11–A12', 'appropriate measures which are commensurate with the ML/TF risks'),
    ], kind='list'),
]),
section('timing', '核實時間、延後條件及審查失敗', 'Verification timing, deferral and failed CDD', [
    block('一般規則與有限延後', 'General rule and limited deferral', [
        ('須在建立關係或達門檻非經常交易之前完成所需CDD；非經常交易不能套用「建立關係後延後核實」的例外。', 'Complete required CDD before establishing a relationship or carrying out a threshold occasional transaction. The post-establishment verification exception does not apply to occasional transactions.'),
        ('業務關係可例外延後身分核實，須同時：有效管理由延後帶來的風險、有必要避免妨礙正常業務，以及在合理切實可行範圍內盡快完成。', 'Identity verification may exceptionally follow relationship establishment only if the resulting risk is effectively managed, deferral is necessary not to interrupt normal business and verification is completed as soon as reasonably practicable.'),
        ('設合理完成期限及逾期跟進、限制交易數目／種類／金額、監察異常大額複雜交易，並定期向管理層報告未完成個案。一般不得向第三方付款。', 'Set a reasonable deadline and follow-up, transaction number/type/amount limits, monitoring of large/complex abnormal activity and periodic management reporting of pending cases. Generally do not pay third parties.'),
        ('延後核實期間第三方付款僅可例外：沒有懷疑、風險評為低、獲高級管理層按客戶業務性質批准，以及受款人不在恐怖分子／政治人物等監察名單。四條件須一併符合。', 'Third-party payment during deferred verification requires all four conditions: no suspicion, assessed low risk, senior approval considering the customer’s business and recipient names not matching watchlists such as terrorist/PEP lists.'),
    ], [
        ref('03', '第4.7.1–4.7.3段', '¶4.7.1–4.7.3', 'necessary not to interrupt the normal conduct'),
        ref('04', '附表2第3條', 'Schedule 2 s.3', 'before carrying out for the customer an occasional transaction'),
    ], kind='list'),
    block('不能完成CDD的後果', 'Consequences of inability to complete CDD', [
        ('不得建立關係或執行非經常交易；已建立者須在合理切實可行範圍內盡快終止。未能於合理核實期限完成時停止進一步交易，除盡可能按原形式退回資金／資產。', 'Do not establish a relationship or execute an occasional transaction; terminate an existing relationship as soon as reasonably practicable. On failed verification deadlines, stop further transactions except returning assets in original form as far as possible.'),
        ('評估失敗是否形成知悉或懷疑，適當時向JFIU舉報；尤其無合理理由要求轉至第三方或把現金轉換形式的情況。匿名／虛構姓名戶口不得開立或維持；編號戶口仍須完整CDD及可供授權人員取得真實身分。', 'Assess whether failure creates knowledge/suspicion and report as appropriate, especially unexplained third-party transfers or transformations of cash. Anonymous/fictitious-name accounts are prohibited; numbered accounts still require full CDD and real identity access for authorised staff.'),
    ], [
        ref('03', '第4.7.4、4.13.1–4.14.1段', '¶4.7.4, 4.13.1–4.14.1', 'must not open, or maintain any anonymous account'),
    ], kind='list'),
    block('號碼戶口仍須在付款訊息使用真名', 'Numbered accounts still use real names in payment messages', [
        ('號碼戶口不得規避完整CDD；合規、審核及其他獲授權員工須可取得資料，並須有足夠員工知道持有人身分。所有電傳／匯款訊息須反映戶口持有人的真實姓名，不能只填號碼來隱藏身分。', 'Numbered accounts do not avoid full CDD; compliance, audit and other authorized staff need access and sufficient staff must know the holder’s identity. All wire/remittance messages must reflect the real account-holder name, not conceal identity behind a number.'),
    ], [
        ref('03', '第4.14.1段及註50', '¶4.14.1; footnotes 50', 'must reflect the real name of the account holder'),
    ], kind='list'),
]),
section('simplified', '簡化盡職審查：可減甚麼、不能免甚麼', 'Simplified due diligence: permitted reductions and limits', [
    block('低風險簡化與法定實益擁有人例外', 'Low-risk simplification and beneficial-owner exceptions', [
        ('須有充分風險分析支持低風險判斷，簡化程度與風險相稱；可降低資料更新／交易監察頻率，或由交易／關係類型推斷目的及性質。仍須持續監察。', 'Support a low-risk finding with adequate analysis and apply proportionate simplification, such as less frequent updates/monitoring or inferring purpose from the transaction/relationship type. Ongoing monitoring remains required.'),
        ('風險升高不再屬低風險、出現洗錢／恐怖分子資金籌集懷疑，或對已有識別／核實資料真確性有疑問，即不可採用或繼續簡化。', 'Stop or do not apply SDD if risk is no longer low, ML/TF is suspected or identification/verification evidence is doubted.'),
        ('不識別／核實實益擁有人是附表2第4條的特定例外，不是「所有低風險客戶免查實益擁有人」。客戶本身、代表及其他仍適用的CDD措施須繼續履行。', 'Omitting beneficial-owner identification/verification is a specific Schedule 2 s.4 exception, not a general waiver for every low-risk customer. Customer/representative checks and other applicable CDD still remain.'),
    ], [
        ref('03', '第4.8.1–4.8.9段', '¶4.8.1–4.8.9', 'it is still required to continuously monitor'),
    ], kind='list'),
    block('可用實益擁有人簡化的客戶', 'Customers eligible for beneficial-owner simplification', [
        ('包括條例金融機構；在對等司法管轄區成立、從事類似業務、備有相類CDD／紀錄措施並受相類監管的機構；股票交易所上市公司；香港政府／公共機構及同等地區相類機構。上市客戶亦須評估披露要求能否提供足夠擁有權透明度。', 'Categories include AMLO FIs; comparable institutions established in equivalent jurisdictions with similar measures and supervision; listed corporations; Hong Kong government/public bodies and equivalent counterparts. Assess whether a listed customer’s disclosure requirements provide sufficient beneficial-ownership transparency.'),
        ('投資工具須能確定：負責對全部投資者實施相類CDD的人是合資格金融機構／受監管機構，並有可靠制度；若投資工具及獲委任機構均不合資格，須識別並合理核實擁有／控制超過25%權益的投資者及其他適用實益擁有人。', 'For investment vehicles, ascertain that a qualifying FI/supervised institution performs comparable CDD on all investors with reliable controls. If neither vehicle nor appointed institution qualifies, identify and reasonably verify investors owning/controlling more than 25% and other applicable beneficial owners.'),
        ('客戶擁有權鏈中有合資格實體，只可對該實體背後擁有人使用例外；與其無關的其他鏈條仍須追查。金融機構以代名公司持有基金或以服務提供者身分為投資工具開戶的特例，仍須有相應底層CDD及操作戶口的合約授權。', 'A qualifying entity within an ownership chain exempts only the owners behind that entity; unrelated chains still require tracing. Special FI nominee/fund-service accounts require the prescribed underlying CDD and contractual account authority.'),
    ], [
        ref('03', '第4.8.10–4.8.16段', '¶4.8.10–4.8.16', 'beneficial owners in the ownership chain that are not connected'),
    ], kind='list'),
    block('產品及律師客戶戶口例外', 'Product and solicitors’ client-account exceptions', [
        ('退休計劃須由僱用收入扣款供款，且規則不准轉讓成員權益；退休計劃保單須無退保條款且不可作抵押。人壽保單則須年保費不多於港幣8,000元或整付保費不多於港幣20,000元。', 'Retirement schemes require employment-income deductions and no assignment of member interests; retirement policies need no surrender clause and cannot be collateral. Life policies require annual premiums no more than HK$8,000 or a single premium no more than HK$20,000.'),
        ('律師／律師行的客戶戶口，須以律師／行名義持有、客戶款項或證券混合，並由律師作代理管理，才可免識別／核實背後實益擁有人。單一客戶戶口或各客戶分戶、不混合款項，仍須識別底層客戶。', 'A solicitor/firm client account qualifies only if in the solicitor’s name, holding mingled client money/securities and managed as clients’ agent. Single-client or segregated non-mingled subaccounts require identification of the underlying clients.'),
    ], [
        ref('03', '第4.8.17–4.8.20段', '¶4.8.17–4.8.20', 'moneys or securities of the customer'),
    ], kind='list'),
    block('投資工具及退休計劃例外的責任人', 'Responsible persons for investment-vehicle and retirement exceptions', [
        ('投資工具例外中，負責全體投資者相類CDD者，須為金融機構或香港／對等司法管轄區成立、具防洗錢措施且受相應監管的相類機構。法律容許時可委任經理、受託人、行政人、過戶代理、登記處或保管人執行，仍須可靠制度。', 'For the investment-vehicle exception, the person responsible for comparable CDD on all investors must be an FI or qualifying institution established in Hong Kong/an equivalent jurisdiction with AML measures and supervised compliance. Where law permits, a manager, trustee, administrator, transfer agent, registrar or custodian may be appointed, with reliable controls.'),
        ('若沒有符合資格者，可按風險考慮負責人按實際所知作書面陳述，列超過25%投資者的身分或確認沒有此人；接受理由須記錄、保存及定期覆核。這不免除合理核實及其他BO要求。', 'Where neither responsible/appointed person qualifies, a risk-based written representation of actual knowledge of over-25% investor identities or their absence may be considered. Document, retain and periodically review the basis of acceptance; reasonable verification and other BO duties remain.'),
        ('合資格退休計劃一般可把僱主視為客戶，選擇不識別／合理核實作為該計劃BO的僱員；與僱員另有獨立業務關係時，仍須完成該關係適用CDD。', 'For a qualifying retirement scheme the employer may generally be treated as customer and employee BO identification/verification waived. A separate business relationship with an employee still requires the applicable CDD.'),
    ], [
        ref('03', '第4.8.10(d)、4.8.14–4.8.18段', '¶4.8.10(d), 4.8.14–4.8.18', 'stating, to its actual knowledge'),
    ], kind='list'),
]),
section('enhanced', '加強盡職審查與資金／財富來源', 'Enhanced due diligence and sources of funds/wealth', [
    block('高風險的處理', 'Responding to high risk', [
        ('情況本質或關長書面通知顯示高風險，須採相稱EDD。建立／繼續高風險關係須取得高級管理層批准及加強持續監察；措施不足時再限制交易或戶口功能等減低剩餘風險。', 'Apply proportionate EDD where circumstances or a CCE written notice indicate high risk. Obtain senior approval to establish/continue high-risk relationships and enhance monitoring; impose additional limits/controls where residual risk remains.'),
        ('一般高風險情況，法例要求管理層批准，再確定財富及資金來源，或採其他額外緩解措施；特定政治人物情況則須完成全部指定措施，不能任選一項。', 'For general high-risk cases the law requires management approval plus establishing wealth/fund sources or other additional mitigation. Specified PEP cases require all prescribed measures rather than choosing one.'),
        ('可用EDD例子：補充職業／資產資料、更頻密更新、查明關係及交易原因、資金目的地，以及要求首筆付款經相類CDD銀行的客戶本人戶口。例子清單並非每宗都要全部做。', 'Examples include further occupation/asset information, more frequent updates, relationship/transaction reasons, fund destinations and first payment through the customer’s bank account subject to comparable CDD. The examples are not a mandatory all-items checklist for every case.'),
        ('高風險因素例子：不合理複雜架構、空殼／代名／不記名持股、現金密集業務、拆單規避門檻、無解釋第三方付款、無地理聯繫、代理制度不足，以及高貪污／制裁／恐怖活動地區。須綜合評估，不把單一線索當成已證犯罪。', 'Potential factors include unjustifiably complex/shell/nominee/bearer structures, cash-intensive businesses, structuring, unexplained third-party funding, absent geographical ties, weak agents and corruption/sanctions/terrorism risks. Assess holistically; a red flag is not proof of crime.'),
    ], [
        ref('03', '第4.9.1–4.9.6段及註36', '¶4.9.1–4.9.6; footnotes 36', 'no expectation for an MSO to conduct all the examples'),
        ref('04', '附表2第15條', 'Schedule 2 s.15', 'either'),
    ], kind='list'),
    block('財富來源與資金來源', 'Source of wealth versus source of funds', [
        ('財富來源（SOW）：整體資產如何累積，例如事業、投資、繼承等形成的總財富；重點是整個財富體系的來源。', 'Source of wealth (SOW): how the person’s overall body of assets was accumulated, such as business, investments or inheritance.'),
        ('資金來源（SOF）：本次關係或交易所涉特定資金／資產從何產生；不只記「從某銀行轉來」，還要了解產生資金的活動及取得資金的實質理由。', 'Source of funds (SOF): how the specific money/assets involved were generated. Naming the sending bank alone is insufficient; understand the generating activity and substantive provenance.'),
        ('措施按風險決定，可向客戶取得資料並以公開資產／收入申報等核對；並非所有官方財產申報都公開，拒交某一份非公開申報亦不自動證明不當。', 'Choose measures by risk, obtaining customer information and corroborating public asset/income declarations where available. Not every official declaration is public; absence of a particular non-public declaration alone is not proof of wrongdoing.'),
    ], [
        ref('03', '第4.9.24–4.9.26段', '¶4.9.24–4.9.26', 'the origin of an individual'),
    ], kind='comparison'),
    block('現有關係及非經常交易', 'Existing relationships and occasional transactions', [
        ('第15條下，繼續高風險關係時，除管理層批准及資金／財富來源或其他額外措施外，有實益擁有人者須合理核實其身分；高風險非經常交易須採額外緩解措施。不能把關係與單次交易的條件不加區分地互換。', 'Under section 15, continuing a high-risk relationship requires reasonable BO identity verification in addition to approval and SOF/SOW or other mitigation. High-risk occasional transactions require additional mitigation. Do not interchange relationship and one-off transaction conditions.'),
    ], [
        ref('04', '附表2第15(b)–(c)條', 'Schedule 2 s.15(b)–(c)', 'where an occasional transaction is to be carried out'),
    ], kind='list'),
    block('關長書面反制要求可獨立於FATF呼籲', 'CCE written countermeasure requirements can be independent of a FATF call', [
        ('FATF要求強制EDD／反制措施，或其他獨立於FATF呼籲但屬較高風險的情況，關長可書面通知要求遵從附表2第15條，或採取通知指定的反制措施；措施須與風險／缺失性質相稱。不能把所有反制義務只限於某一FATF名單。', 'Where FATF calls for mandatory EDD/countermeasures, or in other higher-risk circumstances independent of a FATF call, the CCE may by written notice impose compliance with Schedule 2 section 15 or specific countermeasures in the notice, proportionate to the risks/deficiencies. Countermeasure obligations are not limited to one FATF list.'),
    ], [
        ref('03', '第4.15.2段', '¶4.15.2', 'independent of any call by the FATF'),
    ], kind='list'),
]),
section('peps', '政治人物：類別、親屬及加強措施', 'Politically exposed persons: categories, associates and measures', [
    block('政治人物的範圍', 'Who is a PEP', [
        ('非香港政治人物指在香港以外獲委以重要公職的人，現任或曾任均包括；例如國家／政府首長、高級政界／政府／司法／軍方人員、國有企業高層及重要政黨官員，不包括中級或初級人員。', 'A non-Hong Kong PEP holds/has held a prominent public function outside Hong Kong, including heads of state/government, senior politicians/government/judiciary/military, state-enterprise executives and important party officials, excluding middle/junior ranks.'),
        ('香港政治人物為在香港獲委重要公職的人；國際組織政治人物包括董事、副董事、董事會成員等高級管理人員，不包括中級或初級人員。', 'Hong Kong PEPs hold/have held prominent public functions in Hong Kong. International-organisation PEPs include directors, deputies, board members and equivalent senior managers, excluding middle/junior officials.'),
        ('範圍亦包括配偶／伴侶、子女、父母、子女的配偶／伴侶，以及關係密切的人。密切聯繫包括緊密業務關係、共同實益擁有法人／信託，或實益擁有為政治人物利益設立的法人／信託。', 'The scope includes spouses/partners, children, parents, children’s spouses/partners and close associates: close business relations, joint beneficial ownership or beneficial ownership of an entity/trust set up for the PEP’s benefit.'),
    ], [
        ref('03', '第4.9.7–4.9.8、4.9.13–4.9.15段', '¶4.9.7–4.9.8, 4.9.13–4.9.15', 'a spouse or a partner of a child'),
    ], kind='list'),
    block('三類政治人物的措施', 'Measures by category', [
        ('客戶或實益擁有人屬非香港政治人物：建立關係前，或在既有關係中發現後繼續前，須獲高級管理層批准、合理確定財富及資金來源，並加強持續監察。', 'For a non-Hong Kong PEP customer/beneficial owner, before establishment or continuation after discovery, obtain senior approval, reasonably establish wealth and fund sources, and enhance ongoing monitoring.'),
        ('香港／國際組織政治人物：採合理措施識別；在建立高風險關係、既有關係變高風險，或高風險關係中發現其身分時，採上述全部EDD措施。不是每位本地政治人物一律自動高風險。', 'Take reasonable steps to identify Hong Kong/international-organisation PEPs. Apply all the above EDD for establishing a high-risk relationship, a relationship becoming high risk or discovery of PEP status within a high-risk relationship. Local PEP status is not an automatic universal high-risk classification.'),
        ('卸任不自動解除措施，也不設統一「過了若干年便免」期限。須評估殘餘影響力、原職位高低及前後職能聯繫，信納不再高風險並經管理層批准，才可不採用／停止指定EDD；保留評估紀錄。', 'Leaving office does not automatically end measures and there is no universal elapsed-time exemption. Assess residual influence, former seniority and links between former/current functions; cease prescribed EDD only with a documented finding of no continuing high risk and senior approval.'),
        ('商業資料庫只屬輔助工具，不能取代了解職業／僱主等正常CDD；須知道資料庫不完整、定義不一致及技術限制。親屬和密切聯繫亦須按風險調整EDD程度。', 'Commercial databases support rather than replace ordinary CDD such as occupation/employer enquiries. Understand incompleteness, definition and technical limitations. Tailor EDD intensity for family/associates according to risk.'),
    ], [
        ref('03', '第4.9.9–4.9.12、4.9.16–4.9.23段及註37–42', '¶4.9.9–4.9.12, 4.9.16–4.9.23; footnotes 37–42', 'not merely on prescribed time limits'),
    ], kind='comparison'),
    block('國際組織及批准人員的定義界線', 'International organisations and who can approve PEP relationships', [
        ('國際組織須由成員國正式政治協議設立，協議具國際條約地位，其存在獲成員國法律承認，並非所在地的居民機構單位；聯合國機構屬此類。不是所有名稱含「國際」的體育或民間組織都符合，但其職位仍可能影響客戶風險。', 'An international organisation is established by formal political agreements between member states having treaty status, legally recognized in member countries, and not a resident institutional unit of its host country. UN agencies qualify. An international sports/civil association does not qualify merely by its name, though its positions may still affect customer risk.'),
        ('PEP關係批准人須有足夠高級職權，並由MSO清楚記錄於政策。職銜及人數按組織規模、類型和機構風險而定；組織及風險管理安排適當時，可包括境外高級管理層，並非必須指定一個通用職銜。', 'PEP-relationship approvers need sufficient seniority and must be clearly documented in policy. Titles/numbers depend on size, type and institutional risk. Overseas senior personnel may qualify where consistent with organisational structure and risk management; no universal job title is prescribed.'),
    ], [
        ref('06', '打擊洗錢問答A18–A19、A21', 'AML/CFT FAQ A18–A19, A21', 'formal political agreements'),
    ], kind='list'),
]),
section('remote', '非親身識別：額外措施與數碼例外', 'Non-face-to-face identification: extra measures and digital exception', [
    block('至少一項額外措施', 'At least one additional measure', [
        ('客戶未親身在場接受識別，除獲承認數碼識別例外外，須至少採一項：使用未曾用於核實的獨立來源再核實；採補充措施驗證已取得資料；或確保首筆付款經客戶本人在認可機構／合資格同等地區機構的戶口進行。', 'If the customer was not physically present for identification, apply at least one additional measure unless the recognised-digital-ID exception applies: further verification using unused independent evidence; supplementary checks on obtained information; or first payment through the customer’s own account at an authorised/qualifying equivalent institution.'),
        ('合資格境外機構須在對等司法管轄區成立、從事相類銀行業務、有相類CDD／紀錄措施且受相類監管。首筆付款是「付款」，並非只有「存款」才計。', 'The overseas institution must be established in an equivalent jurisdiction, conduct comparable banking business, maintain similar measures and be comparably supervised. The requirement concerns a payment, not only a deposit.'),
        ('如已用關長承認、屬可靠獨立來源的數碼識別系統資料核實身分，可免上述額外措施；一般視像通話或自行選用的電子平台不自動等同獲承認系統。', 'The extra measures are waived where identity is verified using a reliable independent digital identification system recognised by the CCE. An ordinary video call or self-selected electronic platform is not automatically such a system.'),
        ('補充措施可包括合資格人士核證、可靠資料庫／登記冊或適當科技，須逐案確保足以防冒認。非自然人客戶由遠端代表建立關係，或只提供公司文件副本，也須緩減增加的風險。', 'Supplementary measures may use suitable certification, reliable databases/registers or technology, assessed case by case against impersonation risk. Also mitigate increased risk for non-individual customers onboarded through remote representatives or document copies.'),
    ], [
        ref('03', '第4.10.1–4.10.5段', '¶4.10.1–4.10.5', 'not required to carry out any additional measures'),
    ], kind='list'),
]),
section('intermediaries', '依賴中介人：條件與不可轉移責任', 'Reliance on intermediaries: conditions and retained responsibility', [
    block('依賴與外判的分別', 'Reliance versus outsourcing', [
        ('依賴中介人時，中介通常已有獨立客戶關係並按其自身程序做CDD；外判／代理按本機構程序並受其控制，不屬相同依賴安排。最終CDD責任始終由本機構承擔。', 'An intermediary normally has its own independent customer relationship and applies its own procedures. Outsourcing/agency applies the MSO’s procedures under its control and is a different arrangement. Ultimate CDD responsibility stays with the MSO.'),
        ('可依賴執行附表2第2條的部分或全部CDD，但不可依賴中介人代為履行第5條的持續監察責任。', 'Reliance may cover any part of s.2 CDD, but not the MSO’s s.5 ongoing-monitoring responsibility.'),
        ('須書面確認中介同意及承擔哪些措施，信納其可按要求不延誤提供文件。措施完成後立即取得其所收集的資料／資訊，毋須同一時間取得全部文件副本。', 'Obtain written confirmation of consent and agreed measures and be satisfied documents will be supplied on request without delay. Obtain collected data/information immediately after the measure; simultaneous copies of every underlying document are not required.'),
        ('取得保留底層CDD資料的承諾，涵蓋關係期間及關係完結後至少5年／關長較長指定期；抽查可否及時供應。終止依賴時立即取回全部資料；有疑問時覆核中介及補做CDD。', 'Obtain retention undertakings for the relationship and at least five years afterwards/longer CCE period, and sample-test timely retrieval. On termination obtain all information immediately; review doubts about reliability and perform necessary CDD.'),
    ], [
        ref('03', '第4.11.1–4.11.7段及註44', '¶4.11.1–4.11.7; footnotes 44', 'does not apply to outsourcing or agency relationships'),
    ], kind='list'),
    block('可依賴的類別', 'Eligible categories', [
        ('本地：認可機構、持牌法團、獲授權保險人及指定持牌保險中介；會計、地產及法律專業人士與TCSP持牌人，須備充分防洗錢程序，且就該客戶須遵守附表2相關要求。不是所有MSO均因此自動合資格。', 'Domestic: authorised institutions, licensed corporations, authorised insurers and specified licensed insurance intermediaries; accounting, estate-agency and legal professionals and TCSP licensees with adequate controls and applicable Schedule 2 duties for that customer. MSO status alone does not automatically qualify.'),
        ('境外：在對等司法管轄區經營的相類金融機構、律師／公證人、審計／會計／稅務顧問、TCSP、信託公司或相類地產代理，須受註冊／發牌／規管、有相類措施及受監督。', 'Overseas: equivalent-jurisdiction comparable FIs, lawyers/notaries, auditors/accountants/tax advisers, TCSPs, trust companies or comparable estate agents, subject to registration/licensing/regulation, similar measures and supervision.'),
        ('另有關連境外金融機構類別，須符合相同集團／分支關係、集團政策、相類措施及集團層面監管等條件。集團政策亦要適當減低機構所在地的較高國家風險，並受定期獨立覆核。', 'A separate related-foreign-FI route requires the prescribed group/branch relationship, group policy, comparable measures and group-level supervision. Group policy must address higher country risk and undergo regular independent review.'),
    ], [
        ref('03', '第4.11.8–4.11.14段', '¶4.11.8–4.11.14', 'an institution that carries on a business similar'),
    ], kind='list'),
    block('相關境外金融機構的三種關係', 'Three relationship routes for a related foreign FI', [
        ('該機構須在境外經營相類金融機構業務，並屬以下之一：(1)與MSO同一集團的公司；(2)香港成立或第04份所存版本所指經遷冊MSO的境外分行；(3)境外成立且並非經遷冊實體的MSO的總辦事處或該總辦事處分行。不能僅因有商業合作便當成「相關境外金融機構」。', 'The institution conducts similar FI business abroad and is (1) a same-group company, (2) an overseas branch of a Hong Kong-incorporated or qualifying re-domiciled MSO, or (3) the head office/a head-office branch of a foreign-incorporated MSO that is not a re-domiciled entity. Ordinary commercial cooperation does not establish this related-foreign-FI status.'),
        ('集團政策須適用於MSO及該機構，要求相類CDD、備存紀錄及打擊洗錢計劃；須符合有關當局或對等司法管轄區相類主管的集團層面監管條件。政策須緩解所在地較高國家風險，並定期獨立覆核持續遵從情況。', 'Group policy must apply to both, requiring similar CDD, records and AML programmes, with qualifying group-level supervision by a relevant authority or equivalent-jurisdiction counterpart. Address higher country risk and obtain regular independent review of ongoing compliance.'),
    ], [
        ref('03', '第4.11.12–4.11.14段', '¶4.11.12–4.11.14', 'it is a branch of the head office of the MSO'),
        ref('04', '附表2第18(7)條', 'Schedule 2 s.18(7)', 'related foreign financial institution'),
    ], kind='list'),
    block('本地中介人的保險及專業類別', 'Insurance and professional categories of domestic intermediary', [
        ('具體類別包括持牌個人保險代理、持牌保險代理機構、持牌保險經紀公司；會計類包括註冊會計師、執業法團及會計師事務所；地產類包括持牌地產代理及營業員；法律類包括香港律師及註冊外地律師，另有TCSP持牌人（包括法定當作持牌者）。仍須符合前文相應類別的附表2、該客戶及充分防洗錢程序條件，不能只憑職銜依賴。', 'Specific categories include licensed individual insurance agents, insurance agencies and insurance broker companies; accounting professionals include certified public accountants, corporate practices and firms; estate professionals include licensed estate agents and salespersons; legal professionals include Hong Kong solicitors and registered foreign lawyers, with TCSP licensees including statutory deemed licensees also eligible. The applicable Schedule 2, customer-specific and adequate-procedure conditions above still apply; a title alone is insufficient.'),
    ], [
        ref('03', '第4.11.8段', '¶4.11.8', 'a licensed individual insurance agent'),
    ], kind='list'),
]),
section('monitoring', '持續監察與原有客戶', 'Ongoing monitoring and pre-existing customers', [
    block('持續CDD及交易監察', 'Ongoing CDD and transaction monitoring', [
        ('持續CDD是不時更新客戶資料，保持相關及最新；不是每次覆核都重新核實已確認身分，除非對舊資料有疑問。高風險客戶至少每年覆核一次。休眠客戶的現有CDD紀錄不必定期覆核，但關係重新啟用時應覆核；政策及程序應清楚界定何謂休眠客戶。', 'Ongoing CDD keeps information relevant/current; it does not require routine re-verification of an already verified identity absent doubts. Review high-risk customers at least annually. Regular review of dormant customers’ existing CDD records is unnecessary, but review should occur upon relationship reactivation; policies/procedures should clearly define a dormant customer.'),
        ('交易監察一方面檢查交易與客戶業務、風險及資金來源是否一致，另一方面識別複雜、異常大額或異常模式且無明顯經濟／合法目的的交易，調查背景目的並書面記錄。', 'Monitoring checks consistency with customer business/risk/fund sources and identifies complex, unusually large or unusual-pattern transactions with no apparent economic/lawful purpose, examining their background/purpose and recording findings.'),
        ('監察宜採整體關係視角，跨戶口及關連客戶，而非只逐筆看。參數包括金額／頻率、相連系列、對手、資金來源／目的地及平常戶口活動，須定期覆核及獨立驗證。', 'Prefer a holistic relationship view across accounts/related customers rather than isolated transactions. Parameters include amount/frequency, series, counterparties, geographical origin/destination and normal activity, with regular review and independent validation.'),
        ('交易與客戶背景不符，或屬異常且無明顯目的，任一類情況都須適當查詢。解釋滿意可不再行動但應考慮更新風險；不能滿意解釋而形成懷疑則報JFIU，並記錄結果及理由。', 'Either profile inconsistency or unusual activity lacking an apparent purpose calls for appropriate enquiries. A satisfactory explanation may require no further action but may update risk; unresolved grounds leading to suspicion require JFIU reporting and documented findings/reasons.'),
    ], [
        ref('03', '第5.1–5.14段及註52–53', '¶5.1–5.14; footnotes 52–53', 'preferably the MSO adopts a relationship-based approach'),
    ], kind='list'),
    block('2012年4月1日前建立的關係', 'Relationships established before 1 April 2012', [
        ('原有客戶並非永久免CDD：異常／可疑或與已知背景、業務、風險／資金來源不符的交易，戶口運作重大改變、出現懷疑或質疑原資料時，須做CDD。休眠重新啟用或實益擁有人／控制權改變可屬觸發事件。持續監察一直適用。', 'Pre-existing customers are not permanently exempt. CDD is triggered by unusual/suspicious or profile-inconsistent transactions, material account changes, suspicion or doubts about old information. Reactivation or ownership/control changes may trigger review; ongoing monitoring always applies.'),
    ], [
        ref('03', '第4.12.1–4.12.3段', '¶4.12.1–4.12.3', 'before the AMLO came into effect on 1 April 2012'),
    ], kind='list'),
    block('監察制度設計與資料供應', 'Monitoring-system design and information access', [
        ('制度的設計、自動化及精密程度須按業務規模／複雜度、風險、現有系統及管控、其他業務監察程序，以及產品和交付方式而定，不是一律強制自動化。須及時向負責監察／調查的相關員工提供足夠資料，以識別及分析客戶交易。', 'System design, automation and sophistication depend on business size/complexity, risk, existing systems/controls, other business monitoring and products/delivery. Automation is not universally mandated. Relevant monitoring/investigation staff need timely sufficient information to identify/analyse customer transactions.'),
    ], [
        ref('03', '第5.4–5.5段', '¶5.4–5.5', 'timely and sufficient information required to identify, analyse and effectively monitor'),
    ], kind='list'),
    block('辨認：2022年報告列出的帳戶及轉移模式', 'Recognise: account and transfer patterns in the 2022 report', [
        ('第4.63段列出的七類觀察包括：(1)開戶後隨即更換公司董事／股東；(2)收到一筆或數筆騙款後便停用帳戶；(3)開戶後不久改變裝置識別碼／互聯網規約地址（IP address）；(4)可疑客戶共用裝置識別碼／IP地址。重點是實際使用者、控制權及活動是否與原有客戶資料相符。', 'The seven observations in paragraph 4.63 include: (1) changes of company directors/shareholders soon after account opening; (2) abandoning accounts after one/few fraudulent receipts; (3) changing device identity/Internet Protocol (IP) address soon after opening; (4) suspicious customers sharing device identity/IP addresses. Consider whether actual users, control and activity match the customer information.'),
        ('其餘三類是：(5)主要以轉數快（FPS，Faster Payment System）或其他網上支付平台轉移資金；(6)改用加密貨幣處置懷疑犯罪得益；(7)海外詐騙仍主要利用傳統銀行帳戶。這是2022年報告的犯罪模式觀察，不是說使用FPS、加密貨幣或傳統銀行本身便屬可疑或違法。', 'The other three are: (5) moving funds mainly via the Faster Payment System (FPS) or other online payment platforms; (6) using cryptocurrency to dispose of suspected proceeds; (7) continuing dominance of traditional bank accounts in overseas fraud cases. These are criminal-pattern observations in the 2022 report, not a claim that using FPS, cryptocurrency or traditional banks is itself suspicious or unlawful.'),
        ('第4.64段另列暫存款項、大額交易、交易與客戶背景不相稱、大額現金、非本地居民個人帳戶及無商業目的交易等舉報指標。須結合交易背景及解釋判斷，不能把報告的歷史舉報排序當成考試權重或機械化定罪規則。', 'Paragraph 4.64 also lists temporary holding of funds, large transactions, transactions inconsistent with customer background, large cash transactions, non-resident personal accounts and transactions without a business purpose as reported indicators. Assess context and explanations; the historical reporting order is neither exam weighting nor a mechanical conviction rule.'),
    ], [
        ref('25', '2022年版，第4.62–4.64段', '2022 edition, ¶4.62–4.64', 'Common Device identity'),
    ], kind='list'),
]),
section('screening', '制裁及恐怖分子篩查', 'Sanctions and terrorist screening', [
    block('資料庫、時間與處理', 'Database, timing and response', [
        ('建立及更新恐怖分子／受指定人士資料庫，涵蓋香港憲報、商經局及海關提示名單；可用第三方資料庫，但須抽查完整及準確。聯合國新名單應盡快加入，不等香港立法後才處理風險。', 'Maintain a database covering Gazette, CEDB and C&ED-notified designations. Third-party databases require completeness/accuracy checks. Add new UN lists promptly, without waiting for Hong Kong implementation before addressing risk.'),
        ('建立關係時篩查客戶及實益擁有人；名單新增／更新後盡快重查；執行跨境電傳／匯款前篩查全部相關人士。客戶風險低亦須篩查；關連人士及代表按RBA延伸處理。', 'Screen customers/beneficial owners on establishment and promptly after designation updates; screen all relevant cross-border wire/remittance parties before execution. Screening applies even to low-risk customers; extend it to connected parties/representatives on an RBA.'),
        ('相似姓名先加強核查確認是否真正命中，保存篩查及核查結果；有恐怖分子、擴散資金籌集或違反制裁懷疑時報JFIU。外判海外辦事處篩查／維護名單，最終責任仍在本機構。', 'Investigate potential name matches to determine genuine hits and keep screening/check results. Report TF/PF/sanctions suspicions to the JFIU. Overseas-office screening/database maintenance does not transfer ultimate responsibility.'),
        ('法律禁止交易與按風險採EDD是不同層次；不能因風險評為低便忽略適用制裁禁令。合法特許須按相應法例向保安局或商經局申請，詳見Part 1。', 'A legal prohibition differs from risk-based EDD: low risk does not override applicable sanctions. Licensing exceptions require the competent Security Bureau/CEDB process under the relevant law, explained in Part 1.'),
    ], [
        ref('03', '第6.6–6.8、6.12–6.19段及註58', '¶6.6–6.8, 6.12–6.19; footnotes 58', 'irrespective of the risk profile attributed to the customer'),
    ], kind='list'),
    block('匯款篩查的六組最低相關方', 'Six minimum groups of relevant payment parties for screening', [
        ('跨境電傳／匯款至少篩查：(1)匯款人；(2)收款人；(3)匯款機構；(4)中介機構；(5)收款機構；(6)付款訊息中列名的人士，例如個人、公司及銀行。篩查客戶及BO仍須完成，不能只查匯出銀行或收款人。', 'For a cross-border wire/remittance, at minimum screen (1) originator, (2) recipient, (3) ordering institution, (4) intermediary institution, (5) beneficiary institution and (6) named parties in the payment message, such as individuals, companies and banks. Customer/BO screening remains necessary; checking only the sending bank or recipient is insufficient.'),
    ], [
        ref('06', '打擊洗錢問答A24', 'AML/CFT FAQ A24', 'named parties'),
        ref('07', '附錄(2)第4頁', 'Appendix (2), p.4', 'irrespective of the risk profile'),
    ], kind='list'),
]),
section('third-party-payments', '第三方付款：例外接受與嚴格管控', 'Third-party payments: exceptional acceptance and strict controls', [
    block('接受條件及審查', 'Acceptance conditions and checks', [
        ('第三方指客戶以外的人。第三方付款可掩蓋真正實益擁有人或資金來源，應認真考慮拒絕；無足夠措施管理固有高風險並符合規定時，不應接受。', 'A third party is anyone other than the customer. Such funding can conceal ownership/fund sources. Seriously consider refusal; do not accept where adequate measures cannot manage inherent high risk and meet requirements.'),
        ('僅在例外、合法且合理符合客戶背景及正常商業做法時接受，依高級管理層批准的詳細政策及嚴格管理批准執行。明確列出可接受情況、判準、負責人、識別方法及加強監察。', 'Accept only exceptionally in legitimate circumstances reasonably consistent with the customer profile and normal commercial practice, under senior-approved detailed policies and stringent approval. Define criteria, owners, detection and enhanced monitoring.'),
        ('評估付款原因及必要性；按風險合理核實第三方身分及與客戶關係；由負責打擊洗錢的高級管理層批准，記錄查詢、佐證及批准。第三方也可能是真正實益擁有人。', 'Assess rationale/necessity, reasonably verify third-party identity and relationship on a risk-sensitive basis, obtain relevant AML senior-management approval and document enquiries, corroboration and approval. The payer may be the true beneficial owner.'),
        ('較低風險例子包括直系親屬、客戶實益擁有人／聯屬公司及受規管金融機構，並非自動豁免。較高風險須加強審查及確定相關資金來源；關係難核實、付款前無身分資料或一人替多名無關客戶收付尤其須小心。', 'Relatively lower-risk examples include immediate family, beneficial owners/affiliates and regulated FIs, not automatic exemptions. Enhance scrutiny and establish SOF for higher risk, especially unverifiable relationships, missing pre-payment identity or one payer for many unrelated customers.'),
        ('鼓勵客戶指定本人名下銀行戶口以辨識來源。加強持續監察及員工培訓、向客戶清楚說明拒收／例外政策及文件要求；形成懷疑時報JFIU。', 'Encourage designated customer-owned bank accounts to identify funding. Enhance monitoring/training, explain rejection/exception and evidence policies to customers and report suspicion to the JFIU.'),
    ], [
        ref('08', '第4–6頁，主要措施第1–12項及註6', 'pp.4–6, key controls 1–12; footnote 6', 'only under exceptional and legitimate circumstances'),
    ], kind='list'),
]),
section('delivery', '交付渠道、代理及境外對手風險', 'Delivery channels, agents and overseas counterpart risk', [
    block('加入渠道前與持續覆核', 'Before engagement and during the relationship', [
        ('使用海外代理／對手前先全面評估風險；建立或維持客戶、業務伙伴及對手關係時，評估整條交付渠道被濫用的程度，並定期重看地區監管及新風險。', 'Assess comprehensively before engaging overseas agents/counterparts. When establishing/maintaining customers, partners and counterpart relationships, assess vulnerability across the delivery channel and regularly review regulatory requirements and emerging risks.'),
        ('監察資金移動、代理結算及消費者資金不獲履約／被境外凍結的風險；渠道改變須反映在機構風險評估與內控制度，高風險客戶或交易須EDD。', 'Understand fund movements, agent settlement and risks of non-performance or overseas freezing of customer funds. Reflect channel changes in institutional assessment/controls and apply EDD to high-risk customers/transactions.'),
        ('境外行為若在香港發生會構成可公訴罪行，其得益可受香港洗錢罪涵蓋，不取決於當地是否同樣違法；有知悉／懷疑仍須報JFIU。', 'Proceeds of overseas conduct that would be an indictable offence in Hong Kong may fall within Hong Kong laundering law regardless of its local legal status; knowledge/suspicion still triggers JFIU reporting.'),
    ], [
        ref('14', '第1–2頁及註4', 'pp.1–2 and footnote 4', 'before engaging other parties in its business model'),
    ], kind='list'),
]),
section('wire-transfers', '電傳轉帳：定義及發出機構資料要求', 'Wire transfers: definition and ordering-institution information', [
    block('範圍與豁除', 'Scope and exclusions', [
        ('電傳轉帳是發出機構代表發款人，以電子方式令款項可供其本人或另一受款人在受益機構取得；可有中介機構，亦可在同一機構不同分行進行。按本機構在鏈中的角色履責。', 'A wire transfer electronically makes money available at a beneficiary institution for the originator/another recipient on instructions through an ordering institution. It can involve intermediaries or branches of the same institution. Duties depend on the role performed.'),
        ('機構本身是發款人或受款人時，不是以發出／中介／受益機構角色行事。雙方均為自身行事的MSO與金融機構／境外相類機構轉帳，屬第12條豁除。', 'An MSO acting as originator/recipient is not acting in an ordering/intermediary/beneficiary role. MSO–FI/comparable foreign-institution transfers where both act for themselves are excluded from s.12.'),
        ('卡交易豁除須同時：由信用／扣帳／預付卡交易產生、卡不作人對人轉帳付款系統，以及轉帳訊息附卡號或等同識別碼；不能把所有卡付款一律豁除。', 'The card exclusion requires a credit/debit/prepaid-card transaction, no person-to-person payment-system use and inclusion of the card number/equivalent identifier. It does not exclude every card-funded transfer.'),
    ], [
        ref('03', '第10.1–10.4段', '¶10.1–10.4', 'the card is not used as a payment system'),
    ], kind='list'),
    block('港幣8,000元的界線', 'The HK$8,000 boundary', [
        ('達8,000元：附發款人姓名、戶口／可追蹤編號，以及地址或客戶識別碼或證件號碼，或自然人的出生日期及地點；另附受款人姓名及戶口／受益機構編號。發款人資料須準確。', 'At least HK$8,000: carry originator name and account/traceable reference plus address or customer ID or identity-document number, or for an individual date/place of birth; also recipient name and account/beneficiary reference. Required originator information must be accurate.'),
        ('低於8,000元：仍附雙方姓名及各自戶口／參考編號；不是毋須任何資料。一般不必核實非經常交易發款人，但相連總額達門檻或有懷疑時仍須核實。', 'Below HK$8,000: still carry both names and account/reference numbers. An occasional originator generally need not be verified unless linked transactions reach the threshold or suspicion arises.'),
        ('同一發款人的批量跨境轉帳可在個別指示只附其戶口／編號，但批次檔須有準確、完整及可追蹤的所需雙方資料。本地電傳可將發款人資料簡化為可追蹤的發款人戶口號碼，如無戶口則用獨特參考號碼；所需受款人資料仍須隨附。應接收電傳指示的機構或關長要求，須在收到要求後3個營業日內提供完整發款人資料，應執法機構要求則立即提供。', 'Individual instructions in a same-originator cross-border batch may carry just the originator account/reference if the batch file contains required accurate, traceable information. Domestic wires may abbreviate originator data to a traceable originator account number, or a unique reference where no account exists; required recipient data still accompanies the transfer. Supply full originator data within three business days after receiving a request by the institution receiving the instructions or the CCE, and immediately on law-enforcement request.'),
    ], [
        ref('03', '第10.5–10.13段及註70–71', '¶10.5–10.13; footnotes 70–71', 'within 3 business days after the request is received'),
    ], kind='comparison'),
    block('匯款人資料的準確性與地址', 'Accuracy of originator information and usable addresses', [
        ('按AMLO及指引核實匯款人身分後，所需匯款人資料視為準確，通常毋須再次逐項核實；個案中仍可酌情進一步核查。隨附地址須足以識別所在位置，以供制裁篩查及監察；除沒有替代地址外，應避免只用郵政信箱。', 'Once originator identity is verified under AMLO/the Guideline, required originator information is deemed accurate and normally needs no further verification, though additional case-specific checks remain possible. An accompanying address should identify location for screening/monitoring; avoid a PO box unless no alternative exists.'),
    ], [
        ref('06', '打擊洗錢問答A25–A26', 'AML/CFT FAQ A25–A26', 'except where no alternative exists'),
    ], kind='list'),
    block('戶口號碼、客戶識別號碼、交易參考號碼', 'Account number, customer identifier and transaction reference', [
        ('有相關戶口時用戶口號碼；沒有該戶口，才用由相應匯款機構／收款機構編配、可追查交易的獨特參考號碼。這項先後條件適用於匯款人及收款人的所需資料，不是可任選一個方便的號碼。', 'Use the relevant account number when one exists; only without that account use the traceable unique reference assigned by the appropriate ordering/beneficiary institution. This applies to the required information on both originator and recipient, not a free choice of a convenient number.'),
        ('客戶識別號碼是機構用來唯一識別匯款人的號碼，須指向所存含至少一項以下資料的紀錄：地址、身分證明文件號碼，或出生日期及地點。獨特交易參考號碼用來追查該筆交易；兩者不是同一種號碼。', 'A customer identification number uniquely identifies the originator to the institution and points to a record containing at least one of address, identification-document number, or birth date and place. A unique transaction reference traces the transaction; the identifiers serve different purposes.'),
        ('直接撥付機制（cover payment，例如MT202COV付款）仍須遵守本章適用的電傳要求；這是付款機制名稱，不是「掩蓋付款」或洗錢的同義詞。匯款機構亦須有有效程序防止匯出不合規電傳：合理檢查本地／跨境轉帳的所需雙方資料缺漏、按風險處理缺漏轉帳，並及時修補管控缺失；可包括定期內控／審核測試。', 'Cover-payment mechanisms, such as MT202COV payments, remain subject to applicable Chapter 10 wire-transfer requirements. This names a payment mechanism, not concealment or money laundering. Ordering institutions need effective procedures to prevent non-compliant outgoing wires: reasonable checks for missing required information on both sides of domestic/cross-border transfers, risk-based handling and timely control repairs, including appropriate regular control/audit testing.'),
    ], [
        ref('03', '第10.3、10.5–10.7、10.13段及註70', '¶10.3, 10.5–10.7, 10.13; footnotes 70', 'is a different number from the unique transaction reference number'),
    ], kind='list'),
]),
section('wire-receiving', '電傳轉帳：中介及受益機構責任', 'Wire transfers: intermediary and beneficiary duties', [
    block('本地轉帳的範圍及兩層資料要求', 'Domestic scope and two levels of information requirements', [
        ('「本地」不只看發款人和受款人在哪裏：匯款機構、收款機構，以及每一間中介機構，都必須是位於香港、符合AMLO定義的金融機構。只要鏈中有境外中介機構，就不符合這項本地電傳定義。', '“Domestic” is not determined merely by the originator’s and recipient’s locations. The ordering institution, beneficiary institution and every intermediary must be financial institutions as defined by AMLO located in Hong Kong. An overseas intermediary takes the chain outside this domestic-wire definition.'),
        ('條例附表2第12(6)及(9)條：本地轉帳可隨附發款人戶口／獨特參考號碼；收款機構須追索缺漏的該號碼。第03份指引第10.11–10.12段只簡化發款人資料，並未免除所需受款人資料；第10.20段要求收款機構追索本地或跨境轉帳缺漏的所需雙方資料。兩層要求須分開認識，不能把較窄的法例文字當作可忽略指引的理由。', 'Schedule 2 sections 12(6) and (9) permit the originator account/unique reference number to accompany a domestic wire and require the beneficiary institution to obtain that number if missing. Document 03 paragraphs 10.11–10.12 simplify originator information, without exempting required recipient information; paragraph 10.20 requires the beneficiary institution to obtain missing required information on either side for domestic or cross-border wires. Recognise both levels: the narrower statutory wording does not justify ignoring the Guideline.'),
    ], [
        ref('04', '附表2第12(6)、(9)、(11)條', 'Schedule 2 s.12(6), (9), (11)', 'domestic wire transfer'),
        ref('03', '第10.11–10.12、10.20段及註71', '¶10.11–10.12, 10.20; footnote 71', 'Domestic wire transfer means'),
    ], kind='list'),
    block('資料傳遞、缺漏與核實', 'Pass-through, missing data and verification', [
        ('中介機構須保留並向下一站傳遞全部附隨發款人／受款人資料。若技術限制使跨境與相連本地轉帳間不能保留，須至少保存所收資料5年，反向情況亦適用。', 'Intermediaries retain and pass all accompanying originator/recipient information. If technical limitations prevent it remaining with a linked domestic/cross-border transfer, keep received information for at least five years, including the reverse direction.'),
        ('中介及受益機構須有風險為本程序識別缺漏，決定執行、拒絕、暫停及跟進；發現缺資料應盡快向上手機構索取，未能取得時考慮限制／終止對手機構關係，或採合理緩解措施。', 'Intermediaries/beneficiaries need risk-based missing-data detection and execute/reject/suspend/follow-up policies. Obtain missing information promptly from the preceding institution; if unavailable, consider restricting/ending that institutional relationship or reasonable mitigation.'),
        ('已知資料不完整或無意義，須盡快採合理措施減風險。受益機構收到達8,000元的轉帳，若此前未核實受款人，須核實其身分。', 'Known incomplete/meaningless data requires prompt reasonable mitigation. For transfers of at least HK$8,000, a beneficiary institution verifies a recipient not already verified.'),
    ], [
        ref('03', '第10.14–10.22段', '¶10.14–10.22', 'incomplete or meaningless'),
    ], kind='list'),
]),
section('remittances', '非電傳匯款：發款人與必備紀錄', 'Non-wire remittances: originator and required records', [
    block('匯款的特別要求', 'Special remittance requirements', [
        ('匯款交易是把錢送往／安排送往香港以外地方；電傳轉帳則按電子機構鏈定義，兩者不是同義詞。屬電傳者按第12條處理；非電傳外匯款按第13條。', 'A remittance sends/arranges money outside Hong Kong; a wire transfer is defined by the electronic institutional chain. The terms are not synonymous. Apply s.12 to wires and s.13 to non-wire outward remittances.'),
        ('非電傳外匯款達港幣8,000元或等值外幣，在執行前以身分文件識別及核實發款人；發款人是款項支付戶口的擁有人，沒有戶口時是發指示的人。', 'Before a non-wire outward remittance of at least HK$8,000/equivalent, identify/verify the originator using an identity document. The originator is the holder of the account funding it or, without an account, the person giving instructions.'),
        ('執行前記錄發款人姓名、證件號碼（旅行證件另記簽發地）、地址、幣種及金額；指示接收日期及時間、受款人姓名及地址，以及交付方式。資料須可供關長查閱。', 'Before execution record originator name, ID number (and travel-document issuing place), address, currency/amount, instruction date/time, recipient name/address and delivery method, available to the CCE.'),
    ], [
        ref('03', '第11.1–11.6段', '¶11.1–11.6', 'date and time of receipt of the instruction'),
    ], kind='list'),
    block('第13條的識別文件', 'Identification documents for section 13', [
        ('個人的法定「識別文件」包括身分證、身分證明書、簽證身分書及旅行證件；不可把一般非親身CDD可接受的國民駕駛執照，直接當成第13條的指定識別文件。', 'An individual’s statutory identification document includes an identity card, certificate of identity, document of identity or travel document. A national driving licence acceptable in some general remote-CDD cases is not thereby a section 13 identification document.'),
    ], [
        ref('04', '附表2第1、13條', 'Schedule 2 ss.1, 13', 'certificate of identity'),
    ], kind='list'),
    block('理解：跨境申報不等於證明資金合法', 'Understand: a cross-boundary declaration does not establish lawful funds', [
        ('2022年報告第4.55–4.56段指出，海關會從已申報及違規個案兩方面分析洗錢；報告中的不少申報違規並沒有被懷疑涉及洗錢。反過來，現金運送人即使按申報制度行事，多次把不清楚來源的現金帶到香港再經MSO兌換，仍有較高風險。申報是否合規、來源是否合理及是否需要STR，是不同問題。', 'Paragraphs 4.55–4.56 of the 2022 report describe Customs analysing both declarations and non-compliance cases for ML; many declaration breaches described were not suspected ML. Conversely, repeated cash carriage into Hong Kong for MSO exchange without full knowledge of its source remains a higher-risk pattern, even where declarations are made. Declaration compliance, a reasonable source explanation and the need for an STR are distinct questions.'),
    ], [
        ref('25', '2022年版，第4.55–4.56段', '2022 edition, ¶4.55–4.56', 'individual cash couriers repeatedly carry cash'),
    ], kind='list'),
]),
section('trade-based-laundering', '貿易洗錢：定義與四類風險指標', 'Trade-based money laundering: definition and four indicator groups', [
    block('概念及使用指標的方法', 'Concept and use of indicators', [
        ('貿易洗錢利用貿易交易掩飾犯罪得益或轉移價值，使非法來源合法化或資助非法活動，例如虛假貿易、錯報價格／數量／品質、重複單據或空殼公司。實際貨物、合約、單據與付款須能合理對應。', 'TBML disguises criminal proceeds and moves value through trade to legitimise illegal origins or finance illegal activities, including fictitious trade, misreported price/quantity/quality, duplicate documents and shells. Goods, contracts, documents and payments should have a reasonable relationship.'),
        ('風險指標只是警號，不單獨證明犯罪；清單非盡錄，機構亦未必能看到全部資料。須連同客戶、交易及可取得外部資料作整體判斷；多個指標同時出現應提高關注並及時呈報管理層。', 'Indicators are warning signs, not proof on their own. Lists are non-exhaustive and not all data are observable by an MSO. Assess the total customer/transaction context and available external data; multiple indicators warrant greater concern and timely management escalation.'),
    ], [
        ref('18', '第1–3頁', 'pp.1–3', 'trade-based money laundering'),
        ref('24', '第1–2頁（中文為學習譯文）', 'pp.1–2', 'By no means is this a conclusive list'),
    ], kind='list'),
    block('結構及業務活動指標', 'Structural and business-activity indicators', [
        ('結構：不合理複雜架構、空殼或缺乏人手／資產、地址不符業務、短期大量註冊、名義擁有人不了解業務、網站空泛／欠缺、名稱模仿知名企業、休眠後突然活躍，或與負面情報有關連。須同時考慮是否有合理解釋。', 'Structure: unjustifiably complex ownership, shells or minimal staff/assets, unsuitable addresses, mass recent registrations, nominees ignorant of business, generic/absent websites, imitation names, reactivated dormancy or adverse information. Consider reasonable explanations.'),
        ('活動：貨物／規模與業務不符、不必要中介人／迂迴航線、不合理低利潤或超過能力的交易、突然龐大融資、新設或重啟企業在高門檻行業突然巨額交易，以及不必要複雜貿易融資。', 'Activity: goods/scale inconsistent with business, unnecessary intermediaries/routes, implausibly low margins or beyond-capacity trade, sudden large funding, new/reactivated businesses trading heavily in high-entry-barrier sectors, or unnecessarily complex trade finance.'),
    ], [
        ref('24', '印刷第3–4頁', 'Printed pp.3–4', 'Structural risk indicators'),
    ], kind='list'),
    block('單據／貨物及帳戶／付款指標', 'Document/goods and account/payment indicators', [
        ('單據／貨物：合約、發票及付款的名稱不同；數量、品質或市場價格不符；描述過於籠統；單據偽造／遺失／不合理修改或被拒後重交；交易額與跨境資金不符；臨時進出口及路線不合理。', 'Documents/goods: inconsistent names across contracts/invoices/payments, mismatched quantity/quality/market value, vague descriptions, false/missing/unreasonably altered or resubmitted documents, trade values inconsistent with cross-border flows, and implausible temporary imports/exports or routes.'),
        ('帳戶／付款：臨時改收款人、日期或金額；營業額與背景不符；資金快速進出且餘額很低；不相干第三方付款；分拆避門檻；突然放量後休眠；不尋常整數及循環轉帳。', 'Accounts/payments: last-minute beneficiary/date/amount changes, turnover inconsistent with profile, rapid pass-through with little balance, unrelated third-party funding, threshold splitting, spikes followed by dormancy, unusual round amounts and circular flows.'),
    ], [
        ref('24', '印刷第5–6頁', 'Printed pp.5–6', 'Account and transaction activity'),
    ], kind='list'),
    block('發現風險後的措施', 'Response to identified risks', [
        ('按風險加強CDD、查詢交易目的及資金／財富來源，核對貨物、業務能力、單據及對手；不可以客戶隨便解釋便結束監察警報。無法合理解釋而形成懷疑時盡快報JFIU，包括嘗試及未完成交易，不受金額限制；覆核原有監控缺口。', 'Enhance risk-based CDD, purpose and SOF/SOW enquiries, checking goods, capacity, documents and counterparties. Do not close alerts on unsupported explanations. Promptly report suspicion to JFIU, including attempted/uncompleted activity irrespective of value, and review control gaps.'),
    ], [
        ref('18', '加強措施第1–4項', 'Enhancements 1–4', 'attempted transactions'),
    ], kind='list'),
    block('營運支出與所稱業務不符', 'Operating outgoings inconsistent with the claimed business', [
        ('與聲稱業務規模不符而缺少正常薪酬、營運開支或稅款交易，可屬結構風險線索。須連同整體背景及合理解釋評估，單一指標不等於洗錢證明。', 'An absence of ordinary payroll, operating-cost or tax transactions inconsistent with the claimed business can be a structural warning sign. Assess the full context and reasonable explanations; a single indicator is not proof of laundering.'),
    ], [
        ref('24', '印刷第3頁，結構風險指標', 'Printed p.3, Structural risk indicators', 'it lacks regular payroll transactions'),
    ], kind='list'),
    block('例子：貿易如何轉移價值', 'Examples: how trade moves value', [
        ('2022年風險報告列出的手法包括高報／低報發票價值、同一貨物重複開票、超額／不足付運及虛構付運。重點是貨物、價格、數量及付款的真實關係，不能只因有發票就視為合理。這些是手法例子，不是完整定罪清單。', 'The 2022 risk report describes over/under-invoicing, multiple invoicing, over/under-shipment and phantom shipment. Examine the real relationship among goods, prices, quantities and payments; an invoice alone does not establish legitimacy. These are typology examples, not an exhaustive criminal test.'),
        ('報告專題4.5：走私汽車的內地買款先進入主腦帳戶，再轉往香港MSO在內地的帳戶，主腦最後在香港取回主要為現金的款項。學習重點是兩地安排可轉移犯罪得益的價值，不必見到同一筆銀行匯款直接跨境；毋須背案例金額或人名。', 'Box 4.5 describes Mainland proceeds from smuggled cars moving through the mastermind’s account into a Hong Kong MSO’s Mainland account, followed by mainly cash collection in Hong Kong. The learning point is that coordinated arrangements can transfer value without a directly observed cross-border bank transfer of the same funds; names and case amounts are reference details.'),
    ], [
        ref('25', '2022年版，第4.44、4.57–4.59段及專題4.5', '2022 edition, ¶4.44, 4.57–4.59 and Box 4.5', 'Box 4.5'),
    ], kind='list'),
]),
section('suspicion-indicators', '其他可疑交易指標', 'Other suspicious-activity indicators', [
    block('由行為及背景識別異常', 'Detect anomalies through behaviour and context', [
        ('客戶拒絕提供正常資料、只願提供難核實資訊、過度關心申報門檻、顯得為不明第三方辦事，或交易與職業／財力不相稱。新客戶大額、頻密、分拆或無合理商業原因的現金／匯款均需留意。', 'Watch refusal of normal information, unverifiable details, excessive interest in reporting thresholds, apparent action for unknown third parties or transactions inconsistent with occupation/resources. Large/frequent/split new-customer cash/remittances without a sensible commercial purpose warrant attention.'),
        ('資金短時間在多個戶口／國家轉移、無關人士替同一受款人匯款、與高風險地區／犯罪情報有關、或資金來源與說法不符，須合併客戶及關連交易分析。單一警號不是定罪，但不得忽略。', 'Rapid movements across accounts/countries, unrelated payers funding one recipient, high-risk/crime links or sources inconsistent with explanations require combined customer/linked-transaction analysis. One warning sign is not a conviction but cannot be ignored.'),
    ], [
        ref('03', '第7.9–7.10段', '¶7.9–7.10', 'list of non-exhaustive red flag indicators'),
    ], kind='list'),
    block('化整為零、折返交易與其他警號', 'Structuring/Smurfing, U-turn transactions and other red flags', [
        ('化整為零／分拆（Structuring／Smurfing）：本可用一宗或幾宗大額交易，卻改用多宗小額。可用來避開CDD門檻，但辨識相連操作仍須合併考慮；不是每宗低於門檻就各自免審查。', 'Structuring/Smurfing means many lower-value transactions where one or a few larger ones could be used. It can seek to avoid CDD thresholds, but apparently linked operations still require aggregation; each below-threshold payment is not automatically a separate exemption.'),
        ('折返交易（U-turn）：境外某人／公司的來款，再匯回同一境外司法管轄區另一人／公司，或原匯款人在另一司法管轄區的戶口。另留意不必要多站轉款、多名匯款人集中付款予一人，以及不合理以大量小鈔換另一幣種大鈔。', 'A U-turn takes funds from a foreign person/company and remits them to another person/company in that same foreign jurisdiction or the sender’s account in another jurisdiction. Also watch unnecessary routing, multiple senders concentrating payments to one person and unusually large small-note exchanges for high-denomination notes in another currency.'),
        ('代理／對手拒交識別資料，同一客戶資料逐次改拼寫或局部改動，同日向多個代理分流；低調陪同或在外等候的人、催促先交易後補文件、不理會費率，以及向衝突區慈善團體捐款，均可為相關警號。', 'Agent/counterparty ID refusal, evolving spelling/partial identity details for the same customer, same-day routing through multiple agents, low-profile companions or people waiting outside, pressure to transact before documents, no concern for rates, and conflict-zone charity donations can be relevant warning signs.'),
        ('這是非盡列指標，單項不是定罪或一律必須交STR的充分條件；相關警號應促使進一步調查、初步資金來源查詢及支持文件。完成評估後仍有知悉／懷疑時，按既有法定及內部程序盡快報告。', 'These are non-exhaustive indicators, not automatic proof or an automatic STR requirement in every case. Relevant flags prompt further investigation, initial SOF enquiries and supporting evidence. Remaining knowledge/suspicion requires prompt reporting under statutory/internal procedures.'),
    ], [
        ref('03', '第7.10–7.11段', '¶7.10–7.11', '“Structuring” or “Smurfing”'),
    ], kind='list'),
]),
])
