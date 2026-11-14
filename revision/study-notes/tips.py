#!/usr/bin/env python3
"""Hover/tap study tips for the official seven-part notes.

Tips are study aids only. Official short titles come from the source texts.
Ambiguous section numbers are left unwrapped unless context resolves them.
The builder calls apply_tips() on each generated page.
"""
from __future__ import annotations

import html
import json
import re

# Official short titles, then one-line study gloss. Not official commentary.
ORDINANCES = {
    '615': {
        'abbr': 'AMLO',
        'tc_name': '《打擊洗錢及恐怖分子資金籌集條例》（第615章）',
        'en_name': 'Anti-Money Laundering and Counter-Terrorist Financing Ordinance (Cap. 615)',
        'tc': '簡稱 AMLO。香港對金錢服務經營者做客戶盡職審查、備存紀錄，以及發牌監管的主要法律。',
        'en': 'Abbreviated AMLO. Hong Kong’s main law on CDD, record-keeping and the licensing and supervision of money service operators.',
    },
    '405': {
        'abbr': 'DTROP',
        'tc_name': '《販毒（追討得益）條例》（第405章）',
        'en_name': 'Drug Trafficking (Recovery of Proceeds) Ordinance (Cap. 405)',
        'tc': '簡稱 DTROP。處理與販毒得益有關的調查、限制、沒收，以及處理販毒得益的控罪。',
        'en': 'Abbreviated DTROP. Covers investigation, restraint and confiscation of drug-trafficking proceeds, and the offence of dealing with those proceeds.',
    },
    '455': {
        'abbr': 'OSCO',
        'tc_name': '《有組織及嚴重罪行條例》（第455章）',
        'en_name': 'Organized and Serious Crimes Ordinance (Cap. 455)',
        'tc': '簡稱 OSCO。覆蓋不限於販毒的有組織及嚴重罪行得益；處理犯罪得益的控罪及罰則與 DTROP 對應條文相同。',
        'en': 'Abbreviated OSCO. Covers proceeds of organized and serious crime, not limited to drugs. The corresponding dealing offence and penalties match DTROP.',
    },
    '575': {
        'abbr': 'UNATMO',
        'tc_name': '《聯合國（反恐怖主義措施）條例》（第575章）',
        'en_name': 'United Nations (Anti-Terrorism Measures) Ordinance (Cap. 575)',
        'tc': '簡稱 UNATMO。處理恐怖分子的指定、凍結財產和相關例外。行政長官在憲報刊登指定；例外牌照向保安局申請。',
        'en': 'Abbreviated UNATMO. Covers terrorist designations, freezing of terrorist property and related exceptions. The Chief Executive gazettes designations; exception licences are applied for from the Security Bureau.',
    },
    '537': {
        'abbr': 'UNSO',
        'tc_name': '《聯合國制裁條例》（第537章）',
        'en_name': 'United Nations Sanctions Ordinance (Cap. 537)',
        'tc': '簡稱 UNSO。把聯合國安全理事會制裁在香港落地。法定特許的書面申請交到商務及經濟發展局，由行政長官批出；不是保安局那條 UNATMO 牌照。',
        'en': 'Abbreviated UNSO. Implements UN Security Council sanctions in Hong Kong. Written applications for statutory licences go to the Commerce and Economic Development Bureau; the Chief Executive grants them. This is not the UNATMO licence handled by the Security Bureau.',
    },
    '526': {
        'abbr': 'WMD(CPS)O',
        'tc_name': '《大規模毀滅武器（提供服務的管制）條例》（第526章）',
        'en_name': 'Weapons of Mass Destruction (Control of Provision of Services) Ordinance (Cap. 526)',
        'tc': '簡稱 WMD(CPS)O。管制提供可能協助發展、生產或交付大規模毀滅武器或其投射工具的服務。',
        'en': 'Abbreviated WMD(CPS)O. Controls the provision of services that may assist the development, production or delivery of weapons of mass destruction or their means of delivery.',
    },
    '629': {
        'abbr': 'Cap. 629',
        'tc_name': '《實體貨幣及不記名可轉讓票據跨境流動條例》（第629章）',
        'en_name': 'Cross-boundary Movement of Physical Currency and Bearer Negotiable Instruments Ordinance (Cap. 629)',
        'tc': '就大量現金類物品（CBNI）進出香港設立申報及披露制度，並有扣留時限。',
        'en': 'Sets up the declaration and disclosure system for large quantities of currency and bearer negotiable instruments (CBNIs) moving in or out of Hong Kong, including detention time limits.',
    },
    '34': {
        'abbr': 'MCO',
        'tc_name': '《貨幣兌換商條例》（第34章）',
        'en_name': 'Money Changers Ordinance (Cap. 34)',
        'tc': '規管貨幣兌換交易，例如兌換單、匯率展示和相關罰則。不要把它和 AMLO 第34條（暫時吊銷／撤銷牌照的法定理由）混在一起；第34章是整條條例。',
        'en': 'Regulates money-changing transactions, including transaction notes, rate display and related penalties. Do not confuse it with AMLO section 34 (the statutory grounds for suspending or revoking a licence); Cap. 34 is the whole ordinance.',
    },
    '221': {
        'abbr': 'Cap. 221',
        'tc_name': '《刑事訴訟程序條例》（第221章）',
        'en_name': 'Criminal Procedure Ordinance (Cap. 221)',
        'tc': 'AMLO 等法例寫「第6級罰款」時，金額要對這條法例附表8：第1級2,000、第2級5,000、第3級10,000、第4級25,000、第5級50,000、第6級100,000港元。',
        'en': 'When AMLO and other ordinances say a “fine at level 6”, the amount comes from Schedule 8 to this Ordinance: level 1 HK$2,000; 2 HK$5,000; 3 HK$10,000; 4 HK$25,000; 5 HK$50,000; 6 HK$100,000.',
    },
    '32B': {
        'abbr': 'Cap. 32B',
        'tc_name': '《公司（表格）規例》（第32B章）',
        'en_name': 'Companies (Forms) Regulations (Cap. 32B)',
        'tc': '公司表格方面的附屬法例。申請文件有時要按它的第3條核證成立證明。不是打擊洗錢的主體條例。',
        'en': 'Subsidiary legislation about company forms. Application documents sometimes require a certificate of incorporation certified under its regulation 3. It is not one of the main AML/CFT ordinances.',
    },
}

# Terms that always map to one ordinance / institution.
# Each: list of regexes (applied to text nodes), plus tc/en tip fields.
# 'name' is used as a key; 'tc_name'/'en_name' are the bold first line.

def ord_tip(key):
    o = ORDINANCES[key]
    return o['tc_name'], o['tc'], o['en_name'], o['en']

ABBREV = []

def add_abbrev(patterns, tc_name, tc, en_name, en):
    ABBREV.append({'patterns': patterns, 'tc_name': tc_name, 'tc': tc, 'en_name': en_name, 'en': en})

for key, forms_en, forms_tc in [
    ('615', [r'AMLO'], [r'打擊洗錢條例', r'《打擊洗錢及恐怖分子資金籌集條例》']),
    ('405', [r'DTROP'], [r'《販毒（追討得益）條例》']),
    ('455', [r'OSCO'], [r'《有組織及嚴重罪行條例》']),
    ('575', [r'UNATMO'], [r'《聯合國（反恐怖主義措施）條例》']),
    ('537', [r'UNSO'], [r'《聯合國制裁條例》']),
    ('526', [r'WMD\(CPS\)O', r'WMD（CPS）O'], [r'《大規模毀滅武器（提供服務的管制）條例》']),
]:
    tn, t, en, e = ord_tip(key)
    add_abbrev(forms_en + forms_tc, tn, t, en, e)

add_abbrev([r'CBNI', r'現金類物品', r'不記名可轉讓票據'],
           'CBNI（現金類物品）',
           'Currency and Bearer Negotiable Instruments 的簡稱，即實體貨幣及不記名可轉讓票據。第629章的申報／披露門檻，是總價值超過12萬港元。',
           'CBNIs (currency and bearer negotiable instruments)',
           'Physical currency and bearer negotiable instruments. The Cap. 629 declaration/disclosure threshold is a total value of more than HK$120,000.')
add_abbrev([r'FATF', r'財務行動特別組織'],
           'FATF（財務行動特別組織）',
           'Financial Action Task Force。1989年成立的國際反洗錢及反恐融資標準制定組織；香港自1991年為成員。它的名單不能直接取代香港法律，要經過香港的法例或通函才對持牌人有本地法律效力。',
           'FATF (Financial Action Task Force)',
           'The international standard-setter for AML/CFT, established in 1989; Hong Kong has been a member since 1991. Its lists do not themselves replace Hong Kong law; local legal effect comes through Hong Kong legislation or circulars.')
add_abbrev([r'JFIU', r'聯合財富情報組'],
           'JFIU（聯合財富情報組）',
           'Joint Financial Investigation Unit。由警務處和海關組成，接收可疑交易報告（STR），並作情報處理。它不是法院，也不負責批出 UNATMO 或 UNSO 的牌照。',
           'JFIU (Joint Financial Investigation Unit)',
           'A unit formed by the Police and Customs. It receives suspicious transaction reports (STRs) and handles financial intelligence. It is not a court, and it does not grant UNATMO or UNSO licences.')
add_abbrev([r'C&ED', r'香港海關'],
           'C&ED（香港海關）',
           'Customs and Excise Department。負責監管金錢服務經營者的部門；日常監督工作由轄下的金錢服務監督科（MSSB）執行。',
           'C&ED (Customs and Excise Department)',
           'The department that supervises money service operators. Day-to-day supervision is carried out by its Money Service Supervision Bureau (MSSB).')
add_abbrev([r'\bCCE\b', r'關長'],
           'CCE（海關關長）',
           'Commissioner of Customs and Excise。AMLO 下的發牌及監管當局：批牌、訂條件、作紀律處分的是關長，不是 MSSB 這個內部科別本身。',
           'CCE (Commissioner of Customs and Excise)',
           'The licensing and supervisory authority under AMLO. The Commissioner grants licences, imposes conditions and takes disciplinary action; MSSB is the department’s internal bureau, not a separate statutory authority.')
add_abbrev([r'\bMSSB\b', r'金錢服務監督科'],
           'MSSB（金錢服務監督科）',
           'Money Service Supervision Bureau。香港海關內負責金錢服務監督的科別；對外作出法定決定的仍是關長（CCE）。',
           'MSSB (Money Service Supervision Bureau)',
           'The bureau inside C&ED that supervises money services. Statutory decisions are still made by the Commissioner (CCE).')
add_abbrev([r'\bCEDB\b', r'商務及經濟發展局'],
           'CEDB（商務及經濟發展局）',
           'Commerce and Economic Development Bureau。UNSO（第537章）法定特許的書面申請窗口；牌照由行政長官批出。它不辦理 UNATMO 的例外牌照。',
           'CEDB (Commerce and Economic Development Bureau)',
           'The office that receives written applications for UNSO (Cap. 537) statutory licences; the Chief Executive grants them. It does not handle UNATMO exception licences.')
add_abbrev([r'Security Bureau', r'保安局'],
           '保安局（Security Bureau）',
           'UNATMO（第575章）例外牌照的申請窗口，例如合理生活／法律開支。不要和 UNSO 那條向商務及經濟發展局申請、由行政長官批出的法定特許混淆。',
           'Security Bureau',
           'The office to which UNATMO (Cap. 575) exception licences are applied, for example reasonable living or legal expenses. Do not confuse this with a UNSO statutory licence, which is applied for to the Commerce and Economic Development Bureau and granted by the Chief Executive.')
add_abbrev([r'\bUNSC\b', r'聯合國安全理事會', r'安理會'],
           'UNSC（聯合國安全理事會）',
           'United Nations Security Council。可通過決議要求各國實施制裁，也可透過其委員會作出指定。這些指定要經過香港法律（例如 UNATMO 或 UNSO 規例）才在香港實施。',
           'UNSC (United Nations Security Council)',
           'It can adopt resolutions requiring sanctions, and its committees can make designations. Those designations take effect in Hong Kong only through Hong Kong law, such as UNATMO or regulations under UNSO.')
add_abbrev([r'\bUNSCR\b'],
           'UNSCR（聯合國安全理事會決議）',
           'United Nations Security Council Resolution。安理會通過的決議；在香港要由本地法例或根據 UNSO 訂立的規例實施。',
           'UNSCR (United Nations Security Council Resolution)',
           'A resolution of the UN Security Council. In Hong Kong it is implemented through local legislation or regulations made under UNSO.')
add_abbrev([r'\bCDD\b', r'客戶盡職審查', r'盡職審查'],
           'CDD（客戶盡職審查）',
           'Customer due diligence。識別和核實客戶及實益擁有人身分、了解業務關係目的等。AMLO 附表2規定何時必須做；風險較高時用 EDD，較低且符合條件時可用 SDD。',
           'CDD (customer due diligence)',
           'Identifying and verifying the customer and beneficial owner, and understanding the purpose of the business relationship. AMLO Schedule 2 sets out when it is required. Higher risk calls for EDD; SDD may be used only where the conditions for simplified measures are met.')
add_abbrev([r'\bEDD\b', r'加強盡職審查'],
           'EDD（加強盡職審查）',
           'Enhanced due diligence。在較高洗錢或恐怖分子資金籌集風險時，在一般 CDD 之上再採取的額外措施。',
           'EDD (enhanced due diligence)',
           'Additional measures on top of ordinary CDD when money-laundering or terrorist-financing risk is higher.')
add_abbrev([r'\bSDD\b', r'簡化盡職審查'],
           'SDD（簡化盡職審查）',
           'Simplified due diligence。只在法例和指引容許的較低風險情況使用，不能因為圖方便就用。',
           'SDD (simplified due diligence)',
           'May be used only in the lower-risk situations the law and the Guideline allow; it is not a shortcut of convenience.')
add_abbrev([r'\bPEP\b', r'政治人物'],
           'PEP（政治人物）',
           'Politically exposed person。擔任或曾擔任重要公職的人及其相關人士。對 PEP 通常要做 EDD，並取得高級管理層批准等額外措施。',
           'PEP (politically exposed person)',
           'A person who holds or has held a prominent public function, and certain connected persons. Dealing with a PEP usually requires EDD and extra steps such as senior-management approval.')
add_abbrev([r'\bMLRO\b', r'洗錢報告主任'],
           'MLRO（洗錢報告主任）',
           'Money Laundering Reporting Officer。接收內部報告、決定是否向 JFIU 提交可疑交易報告。前線員工在向 MLRO 匯報前，不應自行篩掉內部報告。',
           'MLRO (Money Laundering Reporting Officer)',
           'Receives internal reports and decides whether to file a suspicious transaction report with the JFIU. Front-line staff should not filter out an internal report before it reaches the MLRO.')
add_abbrev([r'\bSTR\b', r'可疑交易報告'],
           'STR（可疑交易報告）',
           'Suspicious transaction report。向 JFIU 提交的報告。知悉或懷疑時有法定披露責任；向無關人士透露已作出或將作出報告，可能構成通風報訊。',
           'STR (suspicious transaction report)',
           'A report made to the JFIU. There is a statutory duty to disclose when there is knowledge or suspicion. Telling an unauthorised person that a report has been or will be made may be tipping-off.')
add_abbrev([r'\bLMO\b', r'本地管理辦事處'],
           'LMO（本地管理辦事處）',
           'Local management office。沒有特定營業處所的持牌人，須在香港設一個可親身及電話聯絡的實體辦事處，作為與海關的聯絡點。不是每個已有特定處所的 MSO 都另外要設 LMO。',
           'LMO (local management office)',
           'A physical Hong Kong office, reachable in person and by phone, that an operator without particular business premises must maintain as the point of contact with C&ED. Not every MSO that already has particular premises needs a separate LMO.')
add_abbrev([r'\bLPS\b', r'本地紀錄儲存地方', r'本地儲存'],
           'LPS（本地紀錄儲存地方）',
           'Local place of storage。所有申請人都須在香港有實體地方，保存受持牌人控制的完整金錢服務交易帳目及紀錄。',
           'LPS (local place of storage)',
           'A physical place in Hong Kong, required of every applicant, for keeping the complete money-service books and records under the licensee’s control.')
add_abbrev([r'\bMSO\b', r'金錢服務經營者'],
           'MSO（金錢服務經營者）',
           'Money Service Operator。在香港經營貨幣兌換或匯款服務的人；除豁免情況外，須持有關長批出的牌照並遵守 AMLO。',
           'MSO (money service operator)',
           'A person who operates a money changing or remittance service in Hong Kong. Except where an exemption applies, the person must hold a licence granted by the CCE and comply with AMLO.')
add_abbrev([r'\bCO\b(?!\w)', r'合規主任'],
           'CO（合規主任）',
           'Compliance Officer。負責落實打擊洗錢制度的合規人員。與接收內部報告的洗錢報告主任（MLRO）角色不同，可以由同一人兼任，但職責不要混。',
           'CO (Compliance Officer)',
           'The officer responsible for giving effect to the AML/CFT systems. This is a different role from the MLRO, who receives internal reports. The same person may hold both roles, but the functions should not be blurred.')
add_abbrev([r'\bBO\b', r'實益擁有人'],
           '實益擁有人（beneficial owner）',
           '就法團、合夥或信託等，最終擁有或控制該客戶的人。AMLO 附表2對法團等用「超過25%」的百分比測試，還有控制權測試。不要把它和牌照第5部的「最終擁有人」（ultimate owner）完全當成同一個定義。',
           'Beneficial owner (BO)',
           'The person who ultimately owns or controls the customer, for example a corporation, partnership or trust. For corporations, AMLO Schedule 2 uses a “more than 25%” percentage test as well as a control test. This is not identical to “ultimate owner” in Part 5 of AMLO, which is about the licence.')
add_abbrev([r'最終擁有人', r'ultimate owner'],
           '最終擁有人（ultimate owner）',
           'AMLO 第5部（第24條）的發牌概念。對個人經營者，是最終擁有或控制該金錢服務業務的人；對合夥或法團，是超過25%的資本、利潤、已發行股本或表決權，或對管理有最終控制權的人。剛好25%且沒有最終管理控制權，不算最終擁有人。',
           'Ultimate owner',
           'A licensing concept in Part 5 of AMLO (section 24). For an individual operator, it is the person who ultimately owns or controls the money service. For a partnership or corporation, it is a person who has more than 25% of the capital, profits, issued share capital or voting rights, or who exercises ultimate control over management. Exactly 25%, without ultimate management control, is not an ultimate owner.')
add_abbrev([r'表格\s*6', r'Form\s*6'],
           '表格6（Form 6）',
           '在變更發生當日起計一個月內，通知關長申請資料有變。這是事後通知，不能代替第35至39條那些必須事先取得書面批准的情況。',
           'Form 6',
           'Used to notify the CCE of a change in particulars within one month beginning on the date the change takes place. This is after-the-fact notification. It does not replace prior written approval where sections 35 to 39 require it.')
add_abbrev([r'表格\s*4', r'Form\s*4'],
           '表格4（Form 4）',
           '用來申請事先書面批准：成為董事、最終擁有人或合夥人（AMLO 第35、36、37條）。要在任職或成為該人之前批出，不能事後用表格6代替。',
           'Form 4',
           'Used to apply for prior written approval to become a director, ultimate owner or partner (AMLO sections 35, 36 and 37). Approval is needed before the person takes that position. A later Form 6 notice does not replace it.')
add_abbrev([r'表格\s*5', r'Form\s*5'],
           '表格5（Form 5）',
           '用來申請事先書面批准：在牌照上新增營業處所（AMLO 第38、39條）。要在新處所開始經營之前批出。',
           'Form 5',
           'Used to apply for prior written approval to add business premises to a licence (AMLO sections 38 and 39). Approval is needed before operations start at the new premises.')
add_abbrev([r'表格\s*2', r'Form\s*2'],
           '表格2（Form 2）',
           '續牌申請表格。一般須在現有牌照屆滿前不少於45日提交。',
           'Form 2',
           'The licence-renewal application. It is generally to be submitted no later than 45 days before the current licence expires.')

# Fine levels under Cap. 221 Sch. 8
LEVELS = {
    '1': ('2,000', '2000'),
    '2': ('5,000', '5000'),
    '3': ('10,000', '10000'),
    '4': ('25,000', '25000'),
    '5': ('50,000', '50000'),
    '6': ('100,000', '100000'),
}

# Section tips keyed by (ordinance_key, section_id) where section_id is like '5', '5(9)', '25A'
SECTIONS = {}

def add_sec(ord_key, nums, tc, en):
    for n in nums:
        SECTIONS[(ord_key, n)] = (tc, en)

add_sec('615', ['5'],
        'AMLO 第5條：金錢服務經營者須遵守附表2的規定。有兩套控罪：明知違反，以及存心欺詐。罰則和適用的抗辯不一樣，不要混為一談。',
        'AMLO section 5: an MSO must comply with Schedule 2. There are two offence routes — knowing contravention, and intent to defraud — with different penalties and a defence that does not apply to both.')
add_sec('615', ['5(5)', '5(7)'],
        'AMLO 第5(5)/(7)條：明知而違反指明條文。機構或個人一經公訴程序定罪，最高罰款100萬港元及監禁2年；簡易程序是第6級罰款（100,000港元）及監禁6個月。',
        'AMLO section 5(5)/(7): knowing contravention of a specified provision. On indictment, the maximum is a HK$1 million fine and 2 years’ imprisonment; on summary conviction, a fine at level 6 (HK$100,000) and 6 months’ imprisonment.')
add_sec('615', ['5(6)', '5(8)'],
        'AMLO 第5(6)/(8)條：存心欺詐而違反。公訴最高罰款100萬港元及監禁7年；簡易程序是罰款500,000港元及監禁1年。這條簡易程序不是第6級罰款，不要和第5(7)條那檔搞混。',
        'AMLO section 5(6)/(8): contravention with intent to defraud. On indictment, the maximum is a HK$1 million fine and 7 years’ imprisonment; on summary conviction, a HK$500,000 fine and 1 year’s imprisonment. That summary fine is not a level 6 fine; do not confuse it with the section 5(7) tier.')
add_sec('615', ['5(9)'],
        'AMLO 第5(9)條：有限的員工抗辯。只適用於被控第5(7)條（明知違反）的僱員或受僱為機構工作的人，而且要證明已按機構的政策與程序行事。不適用於機構本身、第5(8)條（存心欺詐），或僅僅因為參與管理而被控的人。',
        'AMLO section 5(9): a limited employee defence. It applies only to an employee, or a person employed to work for the institution, who is charged under section 5(7) (knowing contravention), and who acted in accordance with the institution’s policies and procedures. It does not apply to the institution itself, to a section 5(8) (intent-to-defraud) charge, or to a person charged only because they took part in management.')
add_sec('615', ['5(11)'],
        'AMLO 第5(11)條：列明第5條所說的「指明的條文」有哪些，主要在附表2。',
        'AMLO section 5(11) sets out which “specified provisions” section 5 refers to, mainly in Schedule 2.')
add_sec('615', ['9'],
        'AMLO 第9條：獲授權人作例行視察，不是第12條那種正式調查。',
        'AMLO section 9: routine inspection by an authorized person, not a formal investigation under section 12.')
add_sec('615', ['9A'],
        'AMLO 第9A條：另一主管當局向某訂明人士索取「與任何客戶的事務有關」的資料或紀錄時，原則上對方沒有責任交出；除非該另一當局認為對第9條目的有需要，並以書面核證這個意見。這不是一項豁免權。',
        'AMLO section 9A: if another authority asks a prescribed person for information or records relating to the affairs of any of its customers, the person is not required to comply unless that other authority considers the disclosure necessary for section 9 purposes and certifies that opinion in writing. This is not an immunity.')
add_sec('615', ['10'],
        'AMLO 第10條：不遵從第9條視察要求的罰則。這是針對視察要求的條文，不要直接套用第5條那套明知／欺詐控罪和罰則。',
        'AMLO section 10: the penalty for failing to comply with a section 9 inspection requirement. It is not the same offence route or penalty ladder as section 5.')
add_sec('615', ['11'],
        'AMLO 第11條：關長可委任調查員，開展第12條的正式調查。',
        'AMLO section 11: the CCE may appoint an investigator to conduct a formal investigation under section 12.')
add_sec('615', ['12'],
        'AMLO 第12條：正式調查中調查員的權力，例如要求交出紀錄或回答問題。這和第9條的例行視察不同。',
        'AMLO section 12: the investigator’s powers in a formal investigation, such as requiring records or answers. This is not the same as a routine inspection under section 9.')
add_sec('615', ['12A'],
        'AMLO 第12A條：調查中向另一主管當局索取客戶事務資料的限制。須同時滿足兩項：調查員有合理因由相信該客戶能提供與調查有關的資料，以及該另一當局書面核證有需要交出。',
        'AMLO section 12A: limits on seeking customer-affairs information from another authority during an investigation. Both conditions must be met: the investigator has reasonable cause to believe the customer may provide investigation-relevant information, and the other authority certifies in writing that disclosure is necessary.')
add_sec('615', ['13'],
        'AMLO 第13條：不遵從第12條調查要求的罰則。和第10條一樣，不要直接套用第5條的罰則。',
        'AMLO section 13: the penalty for failing to comply with a section 12 investigation requirement. As with section 10, do not simply apply the section 5 penalties.')
add_sec('615', ['15'],
        'AMLO 第15條：在第12(2)或(3)條下被要求作出的回答、解釋或詳情，有舉證限制。調查員須先告知／提醒；若資料可能導致自己入罪，並在提供前申明，則該要求及有關答覆在刑事程序中一般不能用來針對該人，但第13條若干控罪或《刑事罪行條例》第V部等例外仍然適用。這不是一般拒絕權，也不讓已有文件自動獲得豁免。',
        'AMLO section 15: evidential limits on answers, explanations or particulars compelled under section 12(2) or (3). The investigator must first inform or remind the person. If the material might incriminate the person and the claim is made before it is provided, the requirement and the response are generally inadmissible against that person in criminal proceedings, subject to limited exceptions such as certain section 13 offences or Part V of the Crimes Ordinance. This is not a general right to refuse, and it is not blanket immunity for pre-existing documents.')
add_sec('615', ['24'],
        'AMLO 第24條：第5部「最終擁有人」的定義。對合夥或法團，百分比測試是超過25%（「25%以上」），剛好25%且沒有最終管理控制權，不算最終擁有人。',
        'AMLO section 24: the Part 5 definition of “ultimate owner”. For a partnership or corporation, the percentage test is more than 25%. Exactly 25%, without ultimate management control, is not an ultimate owner.')
add_sec('615', ['25'],
        'AMLO 第25條：發牌制度下的豁免情況（例如某些已受其他制度規管的人）。不要把它和 OSCO／DTROP 第25條（處理犯罪得益）混為一條。',
        'AMLO section 25: exemptions under the licensing regime (for example certain persons already regulated elsewhere). Do not confuse this with OSCO/DTROP section 25, which is the offence of dealing with proceeds.')
add_sec('615', ['30', '31'],
        'AMLO 第30、31條：申請金錢服務牌照時須向關長提供的資料。後來這些資料有變更，才會用到第40條在一個月內通知。',
        'AMLO sections 30 and 31: the information that must be given to the CCE when applying for a money service licence. Later changes to those particulars are what section 40 requires to be notified within one month.')
add_sec('615', ['34'],
        'AMLO 第34條：暫時吊銷或撤銷牌照的法定理由，法例本身只列兩項：有關人士不再是適當人選；以及商住處所的佔用人撤回或拒絕進入同意。指引還有其他可導致這個結果的例子，但法定理由就是這兩項。不要和《貨幣兌換商條例》（第34章）整條條例混淆。',
        'AMLO section 34: the statutory grounds for suspending or revoking a licence. The ordinance itself lists two: the person is no longer fit and proper; and an occupant of mixed premises withdraws or refuses entry consent. The Guideline gives further examples that can lead there, but those two are the statutory grounds. Do not confuse this with the Money Changers Ordinance (Cap. 34) as a whole.')
add_sec('615', ['35'],
        'AMLO 第35條：要成為董事，必須先得到關長書面批准，然後才能就任。沒有法定「須提前多少日申請」的日數，關鍵是就任前已經批出。無合理辯解而違反，屬第5級罰款（50,000港元）及監禁6個月。',
        'AMLO section 35: a person must have the CCE’s prior written approval before becoming a director. The law does not set a fixed number of days’ notice; what matters is that approval is already granted before the person takes office. Contravention without reasonable excuse is a level 5 fine (HK$50,000) and 6 months’ imprisonment.')
add_sec('615', ['36'],
        'AMLO 第36條：要成為最終擁有人，必須先得到關長書面批准。事後用表格6通知不能代替這項事先批准。',
        'AMLO section 36: prior written approval from the CCE is required before a person becomes an ultimate owner. A later Form 6 notification does not replace that prior approval.')
add_sec('615', ['37'],
        'AMLO 第37條：要成為合夥人，必須先得到關長書面批准。',
        'AMLO section 37: prior written approval from the CCE is required before a person becomes a partner.')
add_sec('615', ['38'],
        'AMLO 第38條：牌照已經指明營業處所，再要新增處所，必須先得到關長書面批准，才能在新處所經營。',
        'AMLO section 38: where the licence already specifies premises, adding further premises requires the CCE’s prior written approval before operations start there.')
add_sec('615', ['39'],
        'AMLO 第39條：牌照原先沒有規定須有特定處所，現在要加入某指定處所來經營，也須先得到關長書面批准。',
        'AMLO section 39: where the licence did not previously require particular premises, adding specified premises still requires the CCE’s prior written approval before operations start there.')
add_sec('615', ['40'],
        'AMLO 第40條：申請時向關長提供的詳情有變，須在變更發生當日起計一個月內通知（表格6）。這是事後通知；違反的罰則是第5級罰款（50,000港元），本條沒有訂監禁。它不能代替第35至39條的事先批准。',
        'AMLO section 40: a change in particulars provided in an application must be notified within one month beginning on the date the change takes place (Form 6). This is after-the-fact notification. The penalty is a level 5 fine (HK$50,000), with no imprisonment in this section. It does not replace prior approval under sections 35 to 39.')
add_sec('615', ['41'],
        'AMLO 第41條：停止經營須在停止日之前以書面通知關長（沒有規定須提前多少日），並在停止當日起計7日內交回牌照。',
        'AMLO section 41: notice of cessation must be given in writing before the date of cessation (no set number of days in advance), and the licence must be returned within 7 days beginning on that date.')

add_sec('405', ['25'],
        'DTROP 第25條：處理販毒得益的控罪。控方須證明有處理行為，以及知情或有合理理由相信該財產是販毒得益；不必證明上游販毒罪行確已實施，或該財產確實是販毒得益。最高可處監禁14年及罰款500萬港元。',
        'DTROP section 25: the offence of dealing with proceeds of drug trafficking. The prosecution must prove the dealing, and knowledge or reasonable grounds to believe that the property is such proceeds. It need not prove that the predicate trafficking was in fact carried out, or that the property was in fact such proceeds. The maximum is 14 years’ imprisonment and a HK$5 million fine.')
add_sec('455', ['25'],
        'OSCO 第25條：處理可公訴罪行得益的控罪，不限於販毒。證明要求及最高罰則與 DTROP 第25條相同：要證明處理行為及知情／有合理理由相信，不必證明上游罪確已實施。',
        'OSCO section 25: the offence of dealing with proceeds of an indictable offence, not limited to drugs. The proof required and the maximum penalty are the same as DTROP section 25: dealing plus knowledge or reasonable grounds to believe; the prosecution need not prove the predicate offence was in fact committed.')
add_sec('405', ['25A'],
        'DTROP 第25A條：知悉或懷疑某財產是販毒得益，或與販毒有關，須向 JFIU 作出披露。無合理辯解而不披露，即屬犯罪。',
        'DTROP section 25A: a person who knows or suspects that property is proceeds of drug trafficking, or is connected with drug trafficking, must disclose that to the JFIU. Failure to disclose without reasonable excuse is an offence.')
add_sec('455', ['25A'],
        'OSCO 第25A條：知悉或懷疑某財產是可公訴罪行得益，或與之有關，須向 JFIU 作出披露。與 DTROP 第25A條對應。',
        'OSCO section 25A: a person who knows or suspects that property is proceeds of an indictable offence, or is connected with it, must disclose that to the JFIU. It is the counterpart of DTROP section 25A.')
add_sec('575', ['4'],
        'UNATMO 第4條：行政長官可在憲報刊登指定，指明某人是恐怖分子或與恐怖分子有聯繫者。',
        'UNATMO section 4: the Chief Executive may gazette a designation specifying a person as a terrorist or a terrorist associate.')
add_sec('575', ['5'],
        'UNATMO 第5條：行政長官可向原訟法庭申請作出命令，指定某人是恐怖分子或與恐怖分子有聯繫者。',
        'UNATMO section 5: the Chief Executive may apply to the Court of First Instance for an order specifying a person as a terrorist or a terrorist associate.')
add_sec('575', ['6'],
        'UNATMO 第6條：凍結被指稱為恐怖分子財產的權力；這是保安局／UNATMO 這一套，不是 UNSO 的法定特許。',
        'UNATMO section 6: the power to freeze property specified as terrorist property. This belongs to the UNATMO / Security Bureau scheme, not to a UNSO statutory licence.')
add_sec('575', ['12'],
        'UNATMO 第12條：知悉或懷疑是恐怖分子財產時，須向 JFIU 披露。它和 DTROP／OSCO 第25A條是同一類披露責任，但對象是恐怖分子財產。',
        'UNATMO section 12: the duty to disclose to the JFIU knowledge or suspicion that property is terrorist property. It is the same family of disclosure duty as DTROP/OSCO section 25A, but the subject is terrorist property.')
add_sec('575', ['12(1)'],
        'UNATMO 第12(1)條：知悉或懷疑是恐怖分子財產時，向 JFIU 披露的法定責任。',
        'UNATMO section 12(1): the statutory duty to disclose to the JFIU knowledge or suspicion of terrorist property.')
add_sec('629', ['17'],
        '第629章第17條：初扣現金類物品一般不超過10個工作日。適用於懷疑是犯罪得益或恐怖分子財產的物品；繼續扣留還要看第18、19條。',
        'Cap. 629 section 17: initial detention of a CBNI is generally not more than 10 working days. It covers items suspected to be crime proceeds or terrorist property; any longer detention is subject to sections 18 and 19.')
add_sec('629', ['18'],
        '第629章第18條：只有懷疑是犯罪得益（不是恐怖分子財產）才可向法院申請繼續扣留。每次命令不超過3個月，一般合計不超過由該命令起計的2年。法院是原訟法庭或區域法院。',
        'Cap. 629 section 18: a court order continuing detention is available only for suspected crime proceeds, not for terrorist property. Each order lasts not more than 3 months, and the total is generally not more than 2 years from that order. The court is the Court of First Instance or the District Court.')
add_sec('629', ['19'],
        '第629章第19條：如果已有指明的法律程序（在香港或其他地方），物品可繼續扣留至該程序結束。',
        'Cap. 629 section 19: if specified legal proceedings (in Hong Kong or elsewhere) have begun, the item may remain detained until those proceedings are concluded.')

# Schedule 2 sections (AMLO)
SCH2 = {
    '12': (
        'AMLO 附表2第12條：電傳轉帳的特別規定，指引第10章有補充說明。達到8,000港元或等值時，須隨附並確保所需發款人和受款人資料準確。',
        'AMLO Schedule 2 section 12: special rules for wire transfers, supplemented by Chapter 10 of the Guideline. At HK$8,000 or more (or equivalent), the required originator and recipient information must accompany the transfer and be accurate.',
    ),
    '13': (
        'AMLO 附表2第13條：非電傳匯款交易的特別規定，指引第11章有補充說明。不要和電傳轉帳的第12條混用。',
        'AMLO Schedule 2 section 13: special rules for remittance transactions that are not wire transfers, supplemented by Chapter 11 of the Guideline. Do not apply the section 12 wire-transfer rules as if they were the same.',
    ),
}

GUIDE_CH = {
    '3': ('指引第3章講獨立審核等制度要求，不是某一條條例的「第3章」。',
          'Chapter 3 of the Guideline covers institutional requirements such as independent audit. It is not “Cap. 3” of an ordinance.'),
    '7': ('指引第7章講可疑交易舉報制度等。例如第7.7段列出三項要素；員工培訓和第3章的獨立審核是另外的要求，不要算進那三項裡。',
          'Chapter 7 of the Guideline covers the suspicious-transaction reporting system, among other things. Paragraph 7.7 lists three components; staff training and the independent audit in Chapter 3 are separate requirements, not part of those three.'),
    '9': ('指引第9章講員工培訓，不是某一條條例的「第9章」。',
          'Chapter 9 of the Guideline covers staff training. It is not “Cap. 9” of an ordinance.'),
    '10': ('指引第10章補充附表2第12條，講電傳轉帳。',
           'Chapter 10 of the Guideline supplements Schedule 2 section 12 on wire transfers.'),
    '11': ('指引第11章補充附表2第13條，講非電傳匯款。',
           'Chapter 11 of the Guideline supplements Schedule 2 section 13 on non-wire remittances.'),
}

# Marker patterns to detect ordinance context in surrounding text.
ORD_MARKERS = {
    '615': re.compile(r'AMLO|Cap\.?\s*615|第\s*615\s*章|打擊洗錢條例|打擊洗錢及恐怖分子', re.I),
    '405': re.compile(r'DTROP|Cap\.?\s*405|第\s*405\s*章|販毒（追討得益）|販毒\(追討得益\)', re.I),
    '455': re.compile(r'OSCO|Cap\.?\s*455|第\s*455\s*章|有組織及嚴重罪行', re.I),
    '575': re.compile(r'UNATMO|Cap\.?\s*575|第\s*575\s*章|反恐怖主義措施', re.I),
    '537': re.compile(r'UNSO|Cap\.?\s*537|第\s*537\s*章|聯合國制裁條例', re.I),
    '526': re.compile(r'WMD|Cap\.?\s*526|第\s*526\s*章|大規模毀滅武器', re.I),
    '629': re.compile(r'Cap\.?\s*629|第\s*629\s*章|現金類物品|CBNI|實體貨幣及不記名', re.I),
    '34': re.compile(r'Cap\.?\s*34\b|第\s*34\s*章|貨幣兌換商條例|Money Changers', re.I),
    '221': re.compile(r'Cap\.?\s*221|第\s*221\s*章|刑事訴訟程序條例|Criminal Procedure', re.I),
}
SCH2_MARK = re.compile(r'Schedule\s*2|附表\s*2|附表2', re.I)
GUIDE_MARK = re.compile(r'Guideline|指引|Licensing Guide|發牌指引|paragraph\s*[\d.]+|第[\d.]+段|¶', re.I)

SKIP_TAGS = {'script', 'style', 'noscript', 'a'}
SKIP_CLASSES = {'citations', 'source-citation', 'visual-links'}
VOID_TAGS = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}
ATTR_RE = re.compile(r'([^\s=<>/]+)(?:\s*=\s*(?:"([^"]*)"|\'([^\']*)\'|([^\s>]+)))?')


class Node:
    __slots__ = ('kind', 'raw', 'name', 'attrs', 'children', 'parent')

    def __init__(self, kind, raw='', name='', attrs=None):
        self.kind = kind
        self.raw = raw
        self.name = name
        self.attrs = attrs or {}
        self.children = []
        self.parent = None

    @property
    def classes(self):
        return (self.attrs.get('class') or '').split()

    @property
    def id(self):
        return self.attrs.get('id') or ''


def _add(parent, child):
    child.parent = parent
    parent.children.append(child)
    return child


def _tag_end(s, i):
    q = None
    j = i + 1
    while j < len(s):
        c = s[j]
        if q:
            if c == q:
                q = None
        elif c in '"\'':
            q = c
        elif c == '>':
            return j
        j += 1
    return len(s) - 1


def _parse_open(raw):
    inner = raw[1:-1].strip()
    if inner.endswith('/'):
        inner = inner[:-1].rstrip()
    parts = inner.split(None, 1)
    name = parts[0].lower()
    attrs = {}
    if len(parts) > 1:
        for m in ATTR_RE.finditer(parts[1]):
            key = m.group(1).lower()
            attrs[key] = m.group(2) if m.group(2) is not None else (m.group(3) if m.group(3) is not None else (m.group(4) or ''))
    return name, attrs


def parse_html(source):
    root = Node('root')
    stack = [root]
    i, n = 0, len(source)
    while i < n:
        if source[i] != '<':
            j = source.find('<', i)
            if j < 0:
                j = n
            _add(stack[-1], Node('text', source[i:j]))
            i = j
            continue
        if source.startswith('<!--', i):
            j = source.find('-->', i + 4)
            j = n if j < 0 else j + 3
            _add(stack[-1], Node('raw', source[i:j]))
            i = j
            continue
        if source.startswith('<!', i) or source.startswith('<?', i):
            j = _tag_end(source, i)
            _add(stack[-1], Node('raw', source[i:j + 1]))
            i = j + 1
            continue
        if source.startswith('</', i):
            j = _tag_end(source, i)
            name = source[i + 2:j].strip().split()[0].lower() if j > i + 2 else ''
            while len(stack) > 1 and stack[-1].name != name:
                stack.pop()
            if len(stack) > 1 and stack[-1].name == name:
                stack.pop()
            i = j + 1
            continue
        j = _tag_end(source, i)
        raw = source[i:j + 1]
        name, attrs = _parse_open(raw)
        node = _add(stack[-1], Node('tag', raw, name, attrs))
        i = j + 1
        if name in {'script', 'style', 'noscript'}:
            close = re.search(r'</' + re.escape(name) + r'\s*>', source[i:], re.I)
            if close:
                _add(node, Node('raw', source[i:i + close.start()]))
                i += close.end()
            continue
        if name not in VOID_TAGS and not raw.endswith('/>'):
            stack.append(node)
    return root


def get_text(node):
    if node.kind == 'text':
        return html.unescape(node.raw)
    if node.kind != 'tag':
        return ''
    if node.name in SKIP_TAGS:
        return ''
    return ''.join(get_text(c) for c in node.children)


def iter_text(node):
    if node.kind == 'text':
        yield node
        return
    if node.kind != 'tag' or node.name in {'script', 'style', 'noscript'}:
        return
    for child in list(node.children):
        yield from iter_text(child)


def iter_tags(node, name=None):
    if node.kind == 'tag' and (name is None or node.name == name):
        yield node
    if node.kind in {'root', 'tag'}:
        for child in node.children:
            yield from iter_tags(child, name)


def serialize(node):
    if node.kind in {'text', 'raw'}:
        return node.raw
    if node.kind == 'root':
        return ''.join(serialize(c) for c in node.children)
    inner = ''.join(serialize(c) for c in node.children)
    if node.name in VOID_TAGS:
        return node.raw
    if node.name in {'script', 'style', 'noscript'}:
        return node.raw + inner + f'</{node.name}>'
    return node.raw + inner + f'</{node.name}>'


def first_class(node, cls):
    for child in node.children:
        if child.kind == 'tag' and cls in child.classes:
            return child
        hit = first_class(child, cls) if child.kind == 'tag' else None
        if hit:
            return hit
    return None


# ---------- context helpers ----------

def detect_ords(text: str) -> set[str]:
    found = set()
    for key, pat in ORD_MARKERS.items():
        if pat.search(text):
            found.add(key)
    return found

def ancestor_context(node: Node) -> tuple[str, str, str]:
    """Return (surrounding_text, part_id, chapter_id)."""
    part = ''
    chapter = ''
    block = None
    el = node.parent
    while el is not None and el.kind != 'root':
        classes = el.classes
        el_id = el.id
        if not part and el.name == 'body':
            part = el.attrs.get('data-part') or ''
        if not part and el_id.endswith('-view') and el_id[:1] == 'p':
            part = el.attrs.get('data-part') or el_id
        if not part and el_id == 'amounts-view':
            part = 'amounts'
        if not chapter and 'chapter' in classes:
            chapter = el_id
        if block is None and ('concept-block' in classes or el.name in {'p', 'td', 'th', 'li', 'figure', 'article'}):
            block = el
        if el.name in {'section', 'article', 'figure'} and block is not None and part:
            break
        el = el.parent
    text = ''
    if block is not None:
        text = get_text(block)
    elif node.parent:
        text = get_text(node.parent)
    return text, str(part), chapter

def normalize_sec(num: str, sub: str | None) -> str:
    n = num.strip()
    if sub:
        return f'{n}({sub.strip().strip("()")})'
    return n

def tip_for_section(num: str, context: str, part: str, explicit_sch2=False, explicit_guide=False):
    """Return (tc_name, tc, en_name, en) or None if unsafe."""
    ords = detect_ords(context)
    is_sch2 = explicit_sch2 or bool(SCH2_MARK.search(context))
    is_guide = explicit_guide or bool(GUIDE_MARK.search(context) and not ords)

    # Schedule 2 first when clearly in that setting
    if is_sch2 and num in SCH2:
        tc, en = SCH2[num]
        return (f'AMLO 附表2第{num}條', tc, f'AMLO Schedule 2 section {num}', en)

    # Unique AMLO subsections
    if num.startswith('5(') or num in {'9A', '12A', '5(11)'}:
        key = ('615', num)
        if key in SECTIONS:
            tc, en = SECTIONS[key]
            return (f'AMLO 第{num}條', tc, f'AMLO section {num}', en)

    # If exactly one ordinance and we have a tip
    if len(ords) == 1:
        key = next(iter(ords))
        if (key, num) in SECTIONS:
            o = ORDINANCES[key]
            tc, en = SECTIONS[(key, num)]
            return (f'{o["abbr"]} 第{num}條', tc, f'{o["abbr"]} section {num}', en)
        # no tip written — do not invent
        return None

    # DTROP + OSCO together on s.25 / s.25A is a common, intentional pairing
    if ords <= {'405', '455'} and ords and num in {'25', '25A'}:
        if num == '25':
            return (
                'DTROP／OSCO 第25條',
                '兩條法例的第25條都是「處理犯罪得益」的控罪，罰則相同（最高監禁14年及罰款500萬港元）。分別只在於財產來源：DTROP 針對販毒得益，OSCO 針對可公訴罪行得益。控方須證明處理行為及知情／有合理理由相信，不必證明上游罪確已實施。',
                'DTROP/OSCO section 25',
                'Both section 25 offences are about dealing with proceeds, and the penalties are the same (maximum 14 years’ imprisonment and a HK$5 million fine). The difference is the source: DTROP covers drug-trafficking proceeds; OSCO covers proceeds of an indictable offence. The prosecution must prove dealing and knowledge or reasonable grounds to believe, not that the predicate offence was in fact committed.',
            )
        return (
            'DTROP／OSCO 第25A條',
            '兩條法例的第25A條都是知悉或懷疑時向 JFIU 披露的責任，罰則對應。UNATMO 第12條是同一類責任，但對象是恐怖分子財產。',
            'DTROP/OSCO section 25A',
            'Both section 25A provisions require disclosure to the JFIU on knowledge or suspicion, with corresponding penalties. UNATMO section 12 is the same family of duty, but the subject is terrorist property.',
        )

    # Part-level fallback only for clearly AMLO-heavy parts and known AMLO sections
    if part in {'2', '5'} and ('615', num) in SECTIONS and (not ords or ords == {'615'}):
        tc, en = SECTIONS[('615', num)]
        return (f'AMLO 第{num}條', tc, f'AMLO section {num}', en)
    if part == '3' and num in SCH2 and (is_sch2 or not ords):
        tc, en = SCH2[num]
        return (f'AMLO 附表2第{num}條', tc, f'AMLO Schedule 2 section {num}', en)

    # Known AMLO licensing sections are fairly unique even without a marker
    if num in {'9A', '12A', '35', '36', '37', '38', '39', '40', '41', '5(9)', '5(7)', '5(8)', '5(5)', '5(6)'} and (not ords or '615' in ords):
        if ('615', num) in SECTIONS:
            tc, en = SECTIONS[('615', num)]
            return (f'AMLO 第{num}條', tc, f'AMLO section {num}', en)

    # Cap 629 detention sections are fairly unique
    if num in {'17', '18', '19'} and ('629' in ords or part == '1'):
        if ('629', num) in SECTIONS and '615' not in ords:
            # section 17/18/19 could exist elsewhere; require 629 marker unless clearly detention context
            if '629' in ords or re.search(r'扣留|detention|工作日|working days', context, re.I):
                tc, en = SECTIONS[('629', num)]
                return (f'第629章第{num}條', tc, f'Cap. 629 section {num}', en)

    return None

# ---------- wrapping ----------

CAP_RE = re.compile(
    r'(?:Cap\.?\s*(?P<cap>32B|221|615|405|455|526|537|575|629|34)\b|'
    r'第\s*(?P<cap_tc>32B|221|615|405|455|526|537|575|629|34)\s*章)',
    re.I,
)

# More specific patterns first. Each match provides a kind.
SEC_EN_RE = re.compile(
    r'\b(?:sections?|ss\.|s\.)\s*(?P<n>\d+[A-Z]?)(?:\s*\(\s*(?P<sub>[0-9A-Za-z]+)\s*\))?',
    re.I,
)
SEC_TC_RE = re.compile(
    r'第\s*(?P<n>\d+[A-Z]?)(?:[（(](?P<sub>[0-9A-Za-z]+)[）)])?\s*條'
)
SEC_RANGE_RE = re.compile(
    r'(?:ss\.|sections?\s*)(?P<a>\d+)\s*[–\-至到and及]\s*(?P<b>\d+)|'
    r'第\s*(?P<a_tc>\d+)\s*[至到]\s*(?P<b_tc>\d+)\s*條',
    re.I,
)

SCH2_SEC_RE = re.compile(
    r'(?:Schedule\s*2\s*(?:s(?:ection)?s?\.?\s*)?(?P<n>\d+[A-Z]?)|附表\s*2第\s*(?P<n_tc>\d+[A-Z]?)條)',
    re.I,
)
GUIDE_CH_RE = re.compile(
    r'(?:指引第\s*(?P<n>\d+)\s*章|Chapter\s+(?P<n_en>\d+)\b)',
    re.I,
)
PARA_RE = re.compile(
    r'(?:指引\s*)?(?:paragraph|¶|第)\s*(?P<n>\d+\.\d+)\s*段?'
)
LEVEL_RE = re.compile(
    r'(?:fine\s+at\s+)?level\s+(?P<n>[1-6])\b|第\s*(?P<n_tc>[1-6])\s*級(?:罰款)?'
    ,
    re.I,
)

# Build abbreviation regexes (longer first within the list)
def compile_abbrev():
    items = []
    for rec in ABBREV:
        for pat in rec['patterns']:
            items.append((re.compile(pat), rec))
    # sort by pattern length desc so longer official titles match first
    items.sort(key=lambda x: len(x[0].pattern), reverse=True)
    return items

ABBREV_ITEMS = compile_abbrev()

TIP_REGISTRY = {}  # id -> {tc_name,tc,en_name,en}

def tip_id_for(tc_name, tc, en_name, en):
    key = (tc_name, tc, en_name, en)
    for existing, rec in TIP_REGISTRY.items():
        if (rec['tc_name'], rec['tc'], rec['en_name'], rec['en']) == key:
            return existing
    i = f't{len(TIP_REGISTRY)+1}'
    TIP_REGISTRY[i] = {'tc_name': tc_name, 'tc': tc, 'en_name': en_name, 'en': en}
    return i

def make_tip_tag(text, tc_name, tc, en_name, en):
    tid = tip_id_for(tc_name, tc, en_name, en)
    escaped = html.escape(text, quote=False)
    tag = Node('tag', f'<span class="cite-tip" tabindex="0" role="button" data-tip-id="{tid}">', 'span', {
        'class': 'cite-tip', 'tabindex': '0', 'role': 'button', 'data-tip-id': tid,
    })
    _add(tag, Node('text', escaped))
    return tag

def already_in_tip(node):
    el = node.parent
    while el is not None and el.kind != 'root':
        classes = el.classes
        if 'cite-tip' in classes or 'heading-tip' in classes or el.name in SKIP_TAGS:
            return True
        if any(c in SKIP_CLASSES for c in classes):
            return True
        if el.name in {'head', 'title'}:
            return True
        el = el.parent
    return False


HIGH_PARAS = {
    '1.14': (
        'C&ED《打擊洗錢指引》第1.14段列出六條「主要」法例：AMLO、DTROP、OSCO、UNATMO、UNSO 及 WMD(CPS)O。第629章和第34章由通函列為相關法例，並不矛盾。',
        'Paragraph 1.14 of the C&ED AML/CFT Guideline lists six “main” laws: AMLO, DTROP, OSCO, UNATMO, UNSO and WMD(CPS)O. Circulars treat Cap. 629 and Cap. 34 as relevant laws; that is not a conflict.',
    ),
    '7.7': (
        '指引第7.7段列出可疑交易報告制度的三項組成。員工培訓（第9章）和獨立審核（第3章）是另外的要求，不要算進這三項裡。',
        'Guideline paragraph 7.7 lists three components of the suspicious-transaction reporting system. Staff training (Chapter 9) and independent audit (Chapter 3) are separate requirements, not part of those three.',
    ),
    '7.8': (
        '指引第7.8段要求持續查核舉報制度是否符合規定並且行之有效；措施的類別和程度應與風險及業務規模相稱。',
        'Guideline paragraph 7.8 requires ongoing checks that the reporting system complies with the rules and actually works. The type and extent of those measures should be commensurate with the risk and the size of the business.',
    ),
    '5.10': (
        '《發牌指引》第5.10段列舉可拒絕發牌的情況。處所合適及所需佔用人同意是法例上的發牌前提，不能因為指引寫「可拒絕」就當作可以任意豁免。',
        'Licensing Guide paragraph 5.10 lists situations in which a licence may be refused. Suitable premises and any required occupant consent are statutory conditions for grant; the Guide’s “may refuse” wording does not make them freely waivable.',
    ),
    '11.1': (
        '《發牌指引》第11.1段列出持牌人責任，並且註明並非詳盡無遺。',
        'Licensing Guide paragraph 11.1 lists licensee obligations and says the list is not exhaustive.',
    ),
}

def find_matches(text, context, part):
    """Return list of (start, end, tc_name, tc, en_name, en) non-overlapping, first wins by priority."""
    candidates = []

    def add(m, tip):
        if tip is None:
            return
        candidates.append((m.start(), m.end(), tip))

    for m in CAP_RE.finditer(text):
        key = (m.group('cap') or m.group('cap_tc') or '').upper().replace('CAP', '')
        # normalize 32B / 34 etc - groups already have the number
        key = (m.group('cap') or m.group('cap_tc'))
        # canonical key in ORDINANCES
        key = next((k for k in ORDINANCES if k.lower() == key.lower()), None)
        if key:
            o = ORDINANCES[key]
            add(m, (o['tc_name'], o['tc'], o['en_name'], o['en']))

    for m in SCH2_SEC_RE.finditer(text):
        n = m.group('n') or m.group('n_tc')
        add(m, tip_for_section(n, context, part, explicit_sch2=True))

    for m in GUIDE_CH_RE.finditer(text):
        n = m.group('n') or m.group('n_en')
        # Avoid treating "Chapter 10" in "this chapter" English titles? Chapter + number is ok.
        # Skip if this is actually 第615章 style already handled? GUIDE_CH_RE is 指引第 or Chapter N
        # "Chapter 10" in English notes about Guideline - if Cap-like 第405章 doesn't use "Chapter"
        if n in GUIDE_CH and (m.group('n') or GUIDE_MARK.search(context) or 'Chapter' in m.group(0)):
            # If the English word Chapter appears without Guideline context and n is 1-11 of notes parts? 
            # Part titles are "Part 1" not "Chapter 1". OK.
            if m.group('n') or re.search(r'指引|Guideline|Wire transfer|電傳|匯款|培訓|審核', context, re.I):
                tc, en = GUIDE_CH[n]
                add(m, (f'指引第{n}章', tc, f'Guideline Chapter {n}', en))

    for m in SEC_EN_RE.finditer(text):
        num = normalize_sec(m.group('n'), m.group('sub'))
        add(m, tip_for_section(num, context, part))

    for m in SEC_TC_RE.finditer(text):
        num = normalize_sec(m.group('n'), m.group('sub'))
        add(m, tip_for_section(num, context, part))

    for m in SEC_RANGE_RE.finditer(text):
        a = m.group('a') or m.group('a_tc')
        b = m.group('b') or m.group('b_tc')
        if not a or not b:
            continue
        ia, ib = int(a), int(b)
        if ia >= 35 and ib <= 39 and ia < ib:
            add(m, (
                'AMLO 第35至39條',
                '新增董事、最終擁有人、合夥人或營業處所，都要先得到關長書面批准，才能就任或在新處所經營。事後用表格6通知不能代替。',
                'AMLO sections 35 to 39',
                'Prior written approval from the CCE is required before a person becomes a director, ultimate owner or partner, or before operations start at additional premises. A later Form 6 notification does not replace that approval.',
            ))
        elif ia == 35 and ib == 41:
            add(m, (
                'AMLO 第35至41條',
                '第35至39條是事先書面批准（董事、最終擁有人、合夥人或新增處所）；第40條是變更發生後一個月內通知（表格6）；第41條是停止經營前書面通知，並在停止日起7日內交回牌照。三套時間點不要混。',
                'AMLO sections 35 to 41',
                'Sections 35 to 39 require prior written approval (director, ultimate owner, partner or additional premises). Section 40 is notification within one month after a change in particulars (Form 6). Section 41 is written notice before cessation, and return of the licence within 7 days beginning on the cessation date. The three clocks are not interchangeable.',
            ))
        elif (ia, ib) == (10, 13):
            add(m, (
                'AMLO 第10條及第13條',
                '分別是不遵從第9條視察要求、以及不遵從第12條調查要求的罰則。不要直接套用第5條那套明知／欺詐控罪和罰則。',
                'AMLO sections 10 and 13',
                'These are the penalties for failing to comply with a section 9 inspection requirement and a section 12 investigation requirement. Do not simply apply the section 5 knowing / intent-to-defraud offence routes.',
            ))
        elif (ia, ib) == (17, 19) and ('629' in context or '扣留' in context or 'detention' in context.lower() or 'CBNI' in context):
            add(m, (
                '第629章第17至19條',
                '現金類物品的扣留時限：第17條初扣一般不超過10個工作日；第18條繼續扣留只適用於懷疑犯罪得益，每次不超過3個月，一般合計不超過2年；第19條處理已有法律程序的情況。',
                'Cap. 629 sections 17 to 19',
                'Detention clocks for CBNIs: section 17 initial detention is generally not more than 10 working days; section 18 continuation is only for suspected crime proceeds, each order not more than 3 months and generally not more than 2 years in total; section 19 covers cases where proceedings have already begun.',
            ))

    for m in LEVEL_RE.finditer(text):
        n = m.group('n') or m.group('n_tc')
        amt = LEVELS[n][0]
        add(m, (
            f'第{n}級罰款（{amt}港元）',
            f'金額來自《刑事訴訟程序條例》（第221章）附表8。法例條文通常只寫 fine at level {n}／第{n}級罰款，不會寫出金額，要自己對照。',
            f'Level {n} fine (HK${amt})',
            f'The amount comes from Schedule 8 to the Criminal Procedure Ordinance (Cap. 221). The provision usually only says “fine at level {n}” and does not state the figure; you need to look it up.',
        ))

    for pat, rec in ABBREV_ITEMS:
        for m in pat.finditer(text):
            add(m, (rec['tc_name'], rec['tc'], rec['en_name'], rec['en']))

    for m in PARA_RE.finditer(text):
        n = m.group('n')
        if n in HIGH_PARAS and ('paragraph' in m.group(0).lower() or '¶' in m.group(0) or m.group(0).endswith('段') or '指引' in (m.group(0)+context)):
            tc, en = HIGH_PARAS[n]
            add(m, (f'paragraph {n}', tc, f'paragraph {n}', en))

    # resolve overlaps: earlier start, then longer, then keep first (priority is implicit in arrival - we should sort by specificity)
    # Give Cap / official title / sch2 / section priority over generic abbrev and paragraph
    candidates.sort(key=lambda x: (x[0], -(x[1]-x[0])))
    taken = []
    used = [False] * (len(text) + 1)
    for start, end, tip in candidates:
        if any(used[i] for i in range(start, end)):
            continue
        # skip very short accidental matches of 1 char
        if end <= start:
            continue
        for i in range(start, end):
            used[i] = True
        taken.append((start, end, tip))
    taken.sort()
    return taken

def wrap_text_node(node, stats):
    if node.kind != 'text' or already_in_tip(node):
        return
    parent = node.parent
    if parent is None or parent.kind != 'tag' or parent.name in SKIP_TAGS:
        return
    text = html.unescape(node.raw)
    if not text or not text.strip():
        return
    context, part, _chapter = ancestor_context(parent)
    matches = find_matches(text, context, part)
    if not matches:
        return
    frag = []
    last = 0
    for start, end, tip in matches:
        if start > last:
            frag.append(Node('text', html.escape(text[last:start], quote=False)))
        tc_name, tc, en_name, en = tip
        frag.append(make_tip_tag(text[start:end], tc_name, tc, en_name, en))
        stats['wrapped'] += 1
        last = end
    if last < len(text):
        frag.append(Node('text', html.escape(text[last:], quote=False)))
    idx = parent.children.index(node)
    parent.children[idx:idx + 1] = frag
    for child in frag:
        child.parent = parent

_SANCTIONS_HEADING = (
    '這一節對照兩套制裁制度。UNATMO（第575章）負責指定和凍結恐怖分子財產，例外牌照向保安局申請；UNSO（第537章）是聯合國制裁在香港落地，書面申請交商務及經濟發展局，由行政長官批出法定特許。C&ED／JFIU 負責把名單納入篩查和接收可疑報告，本身不批這些牌照。',
    'This section contrasts two sanctions regimes. UNATMO (Cap. 575) covers designations and the freezing of terrorist property; exception licences are applied for from the Security Bureau. UNSO (Cap. 537) implements UN sanctions in Hong Kong: written applications go to the Commerce and Economic Development Bureau, and the Chief Executive grants the statutory licence. C&ED/JFIU put lists into screening and receive suspicious reports; they do not grant those licences.',
)
_LEGAL_HEADING = (
    '這一節整理香港相關法例的分工。第03份第1.14段列六條「主要」法例：AMLO、DTROP、OSCO、UNATMO、UNSO 及 WMD(CPS)O；通函另把第629章和第34章列為相關法例，兩者並不矛盾。',
    'This section sets out how Hong Kong’s relevant ordinances divide the work. Paragraph 1.14 of document 03 lists six “main” laws: AMLO, DTROP, OSCO, UNATMO, UNSO and WMD(CPS)O. Circulars also treat Cap. 629 and Cap. 34 as relevant laws; that is not a conflict.',
)
_CASH_HEADING = (
    '這一節講第629章：現金類物品（CBNI）進出香港的申報／披露，以及扣留時限。初扣第17條，繼續扣留第18條只適用於懷疑犯罪得益，第19條處理已有法律程序的情況。',
    'This section is about Cap. 629: declaration and disclosure of CBNIs moving in or out of Hong Kong, and the detention clocks. Section 17 is the initial detention; section 18 continuation applies only to suspected crime proceeds; section 19 covers cases where proceedings have already begun.',
)
HEADING_OVERRIDES = {
    'sanctions': _SANCTIONS_HEADING,
    'p1-sanctions': _SANCTIONS_HEADING,
    'legal-framework': _LEGAL_HEADING,
    'p1-legal-framework': _LEGAL_HEADING,
    'cross-boundary-cash': _CASH_HEADING,
    'p1-cross-boundary-cash': _CASH_HEADING,
}


def _lang_title(node):
    tc_el = first_class(node, 'tc')
    en_el = first_class(node, 'en')
    title_tc = get_text(tc_el).strip() if tc_el else get_text(node).strip()
    title_en = get_text(en_el).strip() if en_el else title_tc
    return title_tc, title_en


def _mark_heading(node, title_tc, tc, title_en, en, stats):
    if 'heading-tip' in node.classes:
        return
    tid = tip_id_for(title_tc, tc, title_en, en)
    classes = node.classes + ['heading-tip']
    node.attrs['class'] = ' '.join(classes)
    node.attrs.setdefault('tabindex', '0')
    node.attrs['data-tip-id'] = tid
    raw = node.raw
    if re.search(r'\bclass="', raw):
        raw = re.sub(r'\bclass="([^"]*)"', lambda m: f'class="{m.group(1)} heading-tip"', raw, count=1)
    else:
        raw = re.sub(r'^<(\w+)', r'<\1 class="heading-tip"', raw, count=1)
    extra = ''
    if 'tabindex=' not in raw:
        extra += ' tabindex="0"'
    if 'data-tip-id=' not in raw:
        extra += f' data-tip-id="{tid}"'
    if extra and raw.endswith('>'):
        raw = raw[:-1] + extra + '>'
    node.raw = raw
    stats['headings'] += 1


def _parent_chapter(node):
    el = node.parent
    while el is not None and el.kind != 'root':
        if el.name == 'section' and 'chapter' in el.classes:
            return el
        el = el.parent
    return None


def enhance_headings(root, stats):
    for heading in list(iter_tags(root)):
        if heading.name != 'div' or 'section-heading' not in heading.classes:
            continue
        if 'heading-tip' in heading.classes:
            continue
        host = _parent_chapter(heading) or heading
        host_id = host.id
        title_tc, title_en = _lang_title(heading)
        if host_id in HEADING_OVERRIDES:
            tc, en = HEADING_OVERRIDES[host_id]
        else:
            scope = host if host.name == 'section' else heading
            ctx = get_text(scope)
            ords = detect_ords(ctx)
            if not ords:
                continue
            names_tc = '、'.join(f'{ORDINANCES[k]["abbr"]}（{ORDINANCES[k]["tc_name"]}）' for k in sorted(ords, key=lambda x: (len(x), x)))
            names_en = '; '.join(f'{ORDINANCES[k]["abbr"]} ({ORDINANCES[k]["en_name"]})' for k in sorted(ords, key=lambda x: (len(x), x)))
            tc = f'這一節「{title_tc}」主要涉及：{names_tc}。把游標放到條文代號上，可以看到各條法在做甚麼。'
            en = f'This section, “{title_en}”, mainly involves: {names_en}. Hover over a citation mark to see what each instrument does.'
        _mark_heading(heading, title_tc, tc, title_en, en, stats)

    for fig in list(iter_tags(root, 'figure')):
        if 'memory-panel' not in fig.classes:
            continue
        fig_id = fig.id
        h3 = next((c for c in fig.children if c.kind == 'tag' and c.name == 'h3'), None)
        if not h3 or 'heading-tip' in h3.classes:
            continue
        if 'sanctions-actors' not in fig_id and not fig_id.endswith('sanctions-actors'):
            continue
        override = HEADING_OVERRIDES.get('sanctions') or HEADING_OVERRIDES.get('p1-sanctions')
        if not override:
            continue
        title_tc, title_en = _lang_title(h3)
        tc, en = override
        _mark_heading(h3, title_tc, tc, title_en, en, stats)

JS = r"""
(()=>{
const tip=document.createElement('div');
tip.id='cite-tooltip';
tip.setAttribute('role','tooltip');
document.body.appendChild(tip);
let current=null;
function lang(){return document.body.dataset.lang||'tc'}
function fill(el){
  const L=lang();
  const rec=(window.MSO_TIPS||{})[el.dataset.tipId]||{};
  const tcName=rec.tc_name||'';
  const enName=rec.en_name||'';
  const tc=rec.tc||'';
  const en=rec.en||'';
  const noteTc='學習提示，不是法例原文。';
  const noteEn='A study aid, not the official text of the law.';
  tip.innerHTML=
    '<div class="tip-tc-block"><div class="tip-name"></div><p class="tip-body"></p></div>'+
    '<div class="tip-en-block"><div class="tip-name"></div><p class="tip-body"></p></div>'+
    '<p class="tip-note"></p>';
  const blocks=tip.querySelectorAll('.tip-tc-block, .tip-en-block');
  blocks[0].querySelector('.tip-name').textContent=tcName;
  blocks[0].querySelector('.tip-body').textContent=tc;
  blocks[1].querySelector('.tip-name').textContent=enName;
  blocks[1].querySelector('.tip-body').textContent=en;
  tip.querySelector('.tip-note').textContent=(L==='en'?noteEn:noteTc);
}
function place(el){
  const r=el.getBoundingClientRect();
  const tw=tip.offsetWidth||Math.min(576,window.innerWidth-24);
  const th=tip.offsetHeight||120;
  let left=Math.min(Math.max(12,r.left), window.innerWidth-tw-12);
  let top=r.bottom+8;
  if(top+th>window.innerHeight-8) top=Math.max(8,r.top-th-8);
  tip.style.left=left+'px';
  tip.style.top=top+'px';
}
function show(el){
  if(current&&current!==el) current.classList.remove('is-open');
  current=el;
  fill(el);
  tip.classList.add('is-visible');
  el.classList.add('is-open');
  place(el);
}
function hide(){
  tip.classList.remove('is-visible');
  if(current) current.classList.remove('is-open');
  current=null;
}
function targetOf(e){return e.target.closest&&e.target.closest('.cite-tip,.heading-tip')}
document.addEventListener('pointerenter',e=>{
  const el=targetOf(e);
  if(!el) return;
  if(e.pointerType==='mouse'||e.pointerType==='pen') show(el);
},true);
document.addEventListener('mouseover',e=>{
  const el=targetOf(e);
  if(el) show(el);
});
document.addEventListener('mouseout',e=>{
  const el=targetOf(e);
  if(!el) return;
  const to=e.relatedTarget;
  if(to&&(el.contains(to)||tip.contains(to))) return;
  hide();
});
document.addEventListener('focusin',e=>{
  const el=targetOf(e);
  if(el) show(el);
});
document.addEventListener('focusout',e=>{
  const el=targetOf(e);
  if(el) hide();
});
document.addEventListener('click',e=>{
  const el=targetOf(e);
  if(el){e.preventDefault(); if(current===el) hide(); else show(el); return;}
  if(!tip.contains(e.target)) hide();
});
document.addEventListener('keydown',e=>{if(e.key==='Escape') hide()});
window.addEventListener('scroll',()=>{if(current) place(current)},true);
window.addEventListener('resize',()=>{if(current) place(current)});
const demo=new URLSearchParams(location.search).get('tip');
if(demo){
  const el=document.querySelector('#memory-sanctions-actors .cite-tip[data-tip-id="'+demo+'"]')||document.querySelector('[data-tip-id="'+demo+'"]');
  if(el){el.scrollIntoView({block:'center'});show(el);}
}
})();
"""

def _append_scripts(root):
    body = next((n for n in iter_tags(root, 'body')), None)
    if body is None:
        return
    data = json.dumps(TIP_REGISTRY, ensure_ascii=False).replace('<', '\\u003c')
    data_tag = Node('tag', '<script>', 'script', {})
    _add(data_tag, Node('raw', 'window.MSO_TIPS = ' + data + ';'))
    js_tag = Node('tag', '<script>', 'script', {})
    _add(js_tag, Node('raw', JS))
    _add(body, data_tag)
    _add(body, js_tag)


def apply_tips(source):
    """Wrap legislation codes and resolvable section numbers; return tipped HTML."""
    global TIP_REGISTRY
    TIP_REGISTRY = {}
    stats = {'wrapped': 0, 'headings': 0}
    root = parse_html(source)
    body = next((n for n in iter_tags(root, 'body')), root)
    for node in list(iter_text(body)):
        wrap_text_node(node, stats)
    enhance_headings(root, stats)
    _append_scripts(root)
    return serialize(root)
