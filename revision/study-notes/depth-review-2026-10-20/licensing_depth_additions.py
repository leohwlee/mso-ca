"""Source-first depth review of documents 01, 02, 05 and 06, 2026-10-20.

Part 4 changes are made in its manuscript. These Part 6 additions are kept
separate to avoid concurrent edits; they contain no question-bank input.
"""
from model import block, ref

ADDITIONS = {
    6: {
        'beneficial-owners': [
            block('理解：沒有持股也可有最終控制權', 'Understand: ultimate control without share ownership', [
                ('FAQ列的例子包括：透過與持股／表決權超過25%的擁有人之私人關連施加控制；或藉參與企業融資、密切家庭關係、歷史／合約聯繫，或公司違反某些付款約定而取得控制。這些是可能構成控制的例子，不是把所有親屬、債權人或合約對手自動當成實益擁有人。', 'FAQ examples include control through personal connections to owners of more than 25% of shares/votes, or through enterprise financing, close family relationships, historical/contractual associations or a company’s default on particular payments. These are possible routes to control, not automatic BO status for every relative, creditor or contracting party.'),
                ('即使控制權從未實際行使，也可能從使用、享受或得益於法人的資產等情況推定存在。相反，如CDD所得資料完全沒有顯示另有最終控制人，FAQ不要求積極尋找這樣一個人；這不免除已知擁有權、控制結構及其他BO分支的識別要求。', 'Control may be presumed even if never actually exercised, for example through using, enjoying or benefiting from the legal person’s assets. Conversely, where nothing obtained during CDD suggests another ultimate controller exists, the FAQ does not require actively identifying such a person. This does not waive identification under known ownership/control structures or other BO limbs.'),
            ], [ref('06', '打擊洗錢問答A10（比例按法例及指引統一為超過25%）', 'AML/CFT FAQ A10 (percentage follows the law/Guideline: more than 25%)', 'exerts control without ownership')], kind='list'),
        ],
        'representatives': [
            block('記憶：PPTA最低識別資料的四項與五項', 'Remember: four and five minimum PPTA identification items', [
                ('自然人PPTA至少四項：(1)全名；(2)出生日期；(3)國籍；(4)獨特識別號碼及文件類別。文件類別與號碼合列一項；不能只記姓名及證件號碼而省略出生日期／國籍。', 'For an individual PPTA obtain at least four items: (1) full name; (2) date of birth; (3) nationality; (4) unique identification number and document type. Number and type form one listed item; a name and ID number alone omit date of birth/nationality.'),
                ('法人PPTA至少五項：(1)全名；(2)註冊、成立或登記日期；(3)註冊、成立或登記地點，包括註冊辦事處地址；(4)獨特識別號碼及文件類別；(5)主要營業地點（如與註冊辦事處地址不同）。這是識別資料清單；合理核實身分及另外核實授權的責任仍須履行。', 'For a legal-person PPTA obtain at least five items: (1) full name; (2) date of incorporation, establishment or registration; (3) place of incorporation, establishment or registration, including registered-office address; (4) unique identification number and document type; (5) principal place of business if different from the registered office. These are identification data; reasonable identity verification and separate verification of authority remain required.'),
                ('法人透過面對面渠道開戶時，至少一名獲授權建立關係的自然人應現身；不用所有董事／BO到場。若代表法人開戶的人沒有親身在場接受識別，則須按非面對面風險處理，例如採額外CDD或使用關長認可且可靠獨立的數碼識別系統，不能因法人本身不可能現身就忽略代表的渠道風險。', 'For a legal person opening through a face-to-face channel, at least one natural person authorized to establish the relationship should be physically present; all directors/BOs need not attend. If the person acting for the legal person is not present for identification, mitigate the non-face-to-face risks, for example with additional CDD or a reliable independent digital identification system recognized by the CCE. A legal person’s inability to attend itself does not remove its representative’s channel risk.'),
            ], [ref('06', '打擊洗錢問答A9、A12', 'AML/CFT FAQ A9, A12', 'Natural person PPTA')], kind='list'),
        ],
        'enhanced': [
            block('財富來源：甚麼情況須深入了解', 'Source of wealth: when deeper understanding is required', [
                ('FAQ並不要求對每名客戶一律確立財富來源。列舉的高風險情況包括客戶／BO屬非香港政治人物、與香港／國際組織政治人物客戶或BO的高風險關係，以及適當時其他本質上高風險情況。政治人物所需全部措施仍按下節執行，不能用一般高風險措施的選項取代。', 'The FAQ does not expect source-of-wealth establishment for every customer. Its high-risk examples include a non-Hong Kong PEP customer/BO, a high-risk relationship with a Hong Kong/international-organisation PEP customer/BO and, where appropriate, other inherently high-risk situations. Apply the complete PEP measures in the next section; general high-risk alternatives do not replace them.'),
                ('非高風險客戶的職業／公司業務性質等已有資料，通常應足以理解客戶狀況，並監察戶口結餘、交易金額及交易量是否與預期財富／背景相符。高風險客戶亦不必全用同一套程序；風險不足以支持時，無須收集數十年前的證據。這是按風險決定查證程度，不是免除應做的財富來源審查。', 'For non-high-risk customers, existing occupation/business-nature information should often provide a basic profile against which to monitor account balances and transaction values/volumes. High-risk customers need not all undergo identical procedures; evidence from decades ago is not expected where the risk does not justify it. This sets a risk-sensitive depth, not an exemption from required source-of-wealth work.'),
            ], [ref('06', '打擊洗錢問答A16', 'AML/CFT FAQ A16', 'collect evidence dating back decades')], kind='list'),
        ],
        'remote': [
            block('核證作為補充措施的範圍', 'Scope of certification as a supplementary measure', [
                ('若選擇核證作為附表2第9條的補充措施，一般核證的是用作身分核實的文件，例如身分證、護照、公司註冊證書或職權證明書。無須把客戶交來的所有其他CDD資料或文件一律核證；如可與公開來源核對，也沒有一律核證的要求。', 'If certification is chosen as a supplementary measure under Schedule 2 section 9, it generally covers documents used for identity verification, such as ID cards, passports, incorporation certificates or certificates of incumbency. Certification is not expected for all other CDD information/documents or where the MSO can check the documents against public sources.'),
                ('中文FAQ說應盡量容許有意的客戶向職員出示正本；英文說應一直給予此機會。實際安排應讓客戶有機會出示正本，而不是堅持只能付費取得核證副本。採用核證仍須遵守本部分「身分文件與核證副本」的核證人及程序要求。', 'The Chinese FAQ says to allow willing customers to present originals as far as possible; the English says they should always be given that opportunity. Provide an opportunity to show originals instead of insisting only on paid certification. Certification still follows the certifier/procedure requirements in Identity documents and certified copies above.'),
            ], [ref('06', '打擊洗錢問答A27', 'AML/CFT FAQ A27', 'There is no expectation to require certification for all other')], kind='list'),
        ],
        'intermediaries': [
            block('持續監察可獲協助，但不能轉移責任', 'Ongoing monitoring: assistance without transferring responsibility', [
                ('依賴中介人的法定路徑只涵蓋附表2第2條CDD，不能依第18條把第5條持續CDD及交易監察交給中介人負責。不過，中介人可以協助收集更多文件、數據及資料，並提供或協調更新；MSO仍須確保自己保存的CDD紀錄現時有效及相關。', 'Statutory reliance on an intermediary covers Schedule 2 section 2 CDD; section 18 does not transfer section 5 ongoing CDD/transaction monitoring to the intermediary. It may nevertheless assist by collecting further documents, data and information and providing/coordinating updates. The MSO remains responsible for ensuring its own CDD records are up-to-date and relevant.'),
            ], [ref('06', '打擊洗錢問答A22', 'AML/CFT FAQ A22', 'provide or coordinate relevant updates')], kind='list'),
        ],
    },
}
