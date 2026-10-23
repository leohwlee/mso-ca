"""Ruling marks: where the notes apply a source-conflict ruling (owner request, 23 Oct 2026).

Numbers are the decisions in revision/CONFLICT-CALLS.md: B (between documents), W (within
one document), E (English and Chinese texts), N (checked, not a conflict) and D26, the
owner decision of 20 October 2026. U notes are language differences the text handles
without a CONFLICT-CALLS entry, so they can be checked too.

An anchor is part of the English text of exactly one point in its section, or
'panel:<id>' for a whole figure. build.py checks every anchor and number, marks the point
and lists each ruling, with its recorded entry, at the end of the Part. A check note can flag
text that may not match its ruling until the owner settles it; the v1.12.0 notes on B6, B13
and E23 were settled on 23 Oct 2026 by correcting the text.
"""
from model import p


def m(ids, anchor, check=None):
    return dict(ids=ids.split(), anchor=anchor, check=check)


MARKS = {1: {
    'terrorist-financing': [m('E34', 'panel:ml-tf-pf')],
    'legal-framework': [
        m('N1', 'Cap.615 AMLO establishes'),
        m('E34', 'Cap.575 UNATMO addresses'),
    ],
    'international': [
        m('B18 B39', 'The call-for-action category requires'),
        m('B39', 'panel:risk-lists'),
    ],
    'sanctions': [
        m('E27', 'UNATMO section 8A prohibits'),
        m('E31', 'Applicable UNSO prohibitions extend'),
    ],
}, 2: {
    'statutory-map': [
        m('W7 N3', 'Section 7 guidelines are not subsidiary legislation'),
        m('B22', 'C&ED is the Customs and Excise Department'),
        m('B21', 'JFIU means Joint Financial Intelligence Unit'),
    ],
    'licence-scope': [
        m('B26', 'The hotel exception requires'),
        m('B2', 'Section 25 excludes the Government'),
        m('B26 W5', 'The Licensing Guide also excludes exchange incidental'),
    ],
    'grant-renewal': [
        m('B9 B10 B11 B28', 'The proprietor and partners must be fit and proper'),
        m('B42', 'Where an application concerns particular business premises'),
        m('E11 B7 E9 B27', 'Apply for renewal in the specified form'),
        m('B27', 'Invalid/late applications cannot be treated'),
        m('B27 E9', 'If a section 31 renewal application is validly made'),
    ],
    'changes': [m('E11 B27', 'panel:licence-clocks')],
    'discipline': [
        m('W6', 'Section 43 licensing discipline permits'),
        m('B8 W6', 'Loss of fitness/propriety, or withdrawal/refusal'),
    ],
    'enforcement': [m('B24', 'Section 52 covers knowingly/recklessly')],
}, 3: {
    'definitions': [
        m('B14', 'Both also include another “person”'),
        m('B14', 'Trust BOs include a beneficiary'),
        m('B35', 'Schedule 2 statutory identification documents'),
    ],
    'core-duties': [
        m('B16 B19', 'CDD precedes a business relationship'),
        m('B19 B36', 'Section 13 separately imposes'),
        m('B16', 'Delayed verification requires necessity'),
        m('B19 B35 B36', 'panel:money-boundaries'),
    ],
    'simplification': [
        m('B31', 'Qualifying categories: financial institutions'),
        m('E22', 'For solicitor/firm accounts'),
    ],
    'special-cases': [
        m('E17', 'Non-face-to-face identification requires'),
        m('B17 B32', 'Non-Hong Kong PEP relationships require'),
        m('B17', 'For section 15 other high-risk cases'),
    ],
    'ongoing-and-records': [
        m('E33 E41', 'Review customer information, scrutinize'),
        m('W8 B34', 'A qualifying intermediary consents in writing'),
        m('B40', 'Hong Kong-incorporated or re-domiciled financial institutions'),
    ],
    'fees': [
        m('B6', 'Grant application: HK$3,810 base'),
        m('B6', 'HK$945 is payable for each person subject to the fit-and-proper test'),
        m('B6', 'panel:fee-components'),
    ],
}, 4: {
    'premises': [
        m('E13', 'the Chinese text says “only” using such devices'),
        m('E10 B25 E40', 'Mixed commercial/residential premises need every occupant'),
        m('W3 W2 E1', 'All applicants need a physical Hong Kong LPS'),
        m('E10 B25', 'panel:three-places'),
    ],
    'application': [
        m('B42 B28 W3', 'Paragraph 5.10 lists fitness-test failure'),
        m('W1 W5', 'Further examples are a business plan'),
    ],
    'fitness': [
        m('B3 B12 B13', 'Consider statutory Hong Kong/overseas offences'),
        m('B12', 'Document 10 adds AMLO/licence/regulatory compliance'),
        m('B3 B12 B13', 'Foreign convictions include conduct'),
    ],
    'assessment': [
        m('W1', 'At least one senior manager overseeing AML policies'),
        m('B23 B5', 'renewal applicants requiring assessment attend within 30 days'),
        m('U1', 'Following failure, a further opportunity'),
        m('E8', 'Under the guide’s weather arrangements'),
        m('B5', 'The guide permits one nomination'),
        m('B5 B23 B27', 'Where assessment is required for renewal, nominate'),
        m('B5', 'Nomination is made once'),
        m('B5 B23 B27 U1', 'panel:assessment-clocks'),
    ],
    'licensing-actions': [
        m('E11 B27', 'Use Form 2 at least 45 days'),
        m('W1 B25', 'Paragraph 11.1 lists licensee obligations'),
        m('E11 B5 B27', 'Paragraph 6.4 gives three alternative invalidity grounds'),
        m('B27', 'An invalid application cannot be processed'),
        m('B8 W2 E1', 'The non-exhaustive paragraph 7.1 examples'),
        m('B8 E3 W6', 'Also (f) late periodic returns'),
    ],
}, 5: {
    'institutional-assessment': [m('B38', 'Include higher risks notified by the CCE')],
    'roles': [
        m('W9', 'The MLRO is the central suspicious-reporting point'),
        m('E29 E28', 'Timely, complete, understandable'),
    ],
    'group-controls': [
        m('B40', 'A Hong Kong-incorporated MSO applies group-wide controls'),
        m('B40', 'Schedule 2 section 22 in the consolidated Ordinance'),
    ],
}, 6: {
    'triggers': [
        m('B19 B16', 'CDD is required before general occasional transactions'),
        m('B19 B36', 'Non-wire outward remittances of at least HK$8,000 have'),
        m('B16 B19', 'panel:cdd-trigger-tree'),
    ],
    'identity': [
        m('E24', 'For trusts/similar arrangements collect'),
        m('E4', 'Generally sight originals and keep copies'),
        m('E24', 'To verify a trust’s name'),
        m('E24', 'panel:identity-data'),
    ],
    'identity-evidence': [
        m('W4 E18 B4', 'Appendix A paragraph 1 first addresses'),
        m('B4 E16 B35', 'For non-residents not physically present'),
        m('B15', 'Travel documents are not limited to passports'),
        m('E19', 'For a Hong Kong-born minor'),
    ],
    'beneficial-owners': [
        m('B14', 'A beneficial owner ultimately owns/controls'),
        m('B14', 'also the person for whom it acts'),
        m('B14 E20', 'For trusts: vested-interest beneficiaries'),
        m('B14', 'Ownership/control limbs for corporations'),
    ],
    'representatives': [
        m('B29', 'Apply relevant individual/legal-person identification'),
        m('B29', 'For low-risk relationships a representative list'),
    ],
    'timing': [
        m('B16', 'Complete required CDD before establishing'),
        m('B16', 'Identity verification may exceptionally follow'),
    ],
    'simplified': [
        m('E23', 'Stop or do not apply SDD'),
        m('B31', 'Categories include AMLO FIs'),
        m('E22', 'A solicitor/firm client account qualifies'),
    ],
    'enhanced': [
        m('B17', 'For general high-risk cases the law requires'),
        m('B17', 'Under section 15, continuing a high-risk relationship'),
        m('U3', 'The four country factors are'),
        m('B17 E21', 'The FAQ does not expect source-of-wealth'),
    ],
    'peps': [
        m('B17', 'For a non-Hong Kong PEP customer/beneficial owner'),
        m('B17 E21', 'Take reasonable steps to identify Hong Kong'),
        m('B32', 'Leaving office does not automatically end'),
        m('E21 B32', 'panel:pep-categories'),
        m('B17', 'panel:pep-common-and'),
    ],
    'remote': [
        m('E17', 'If the customer was not physically present'),
        m('E17', 'The requirement concerns a payment, not only a deposit'),
        m('E7', 'The Chinese FAQ says to allow'),
    ],
    'intermediaries': [
        m('B34', 'Reliance may cover any part'),
        m('W8', 'Obtain written confirmation of consent'),
        m('B30', 'Domestic: authorised institutions'),
        m('B33', 'an overseas branch of a Hong Kong-incorporated or qualifying re-domiciled MSO'),
        m('B34', 'Statutory reliance on an intermediary covers'),
        m('W8 B34', 'panel:reliance-outsourcing'),
    ],
    'monitoring': [
        m('E33 E41', 'Monitoring checks consistency'),
        m('E6', 'Either profile inconsistency'),
    ],
    'screening': [
        m('D26', 'Page 2 of document 26'),
        m('D26', 'Both versions require screening'),
    ],
    'delivery': [m('N3', 'Assess comprehensively before engaging')],
    'wire-transfers': [m('B19', 'At least HK$8,000: carry originator')],
    'wire-receiving': [
        m('B20', 'Recognise both levels'),
        m('U2', 'Intermediaries use reasonable measures consistent with straight-through'),
        m('B19', 'For transfers of at least HK$8,000'),
    ],
    'remittances': [
        m('B19 B36 B35', 'Before a non-wire outward remittance'),
        m('B35', 'A national driving licence acceptable'),
    ],
    'trade-based-laundering': [m('E32', 'TBML disguises criminal proceeds')],
}, 7: {
    'reporting-duty': [m('W11', 'panel:str-route')],
    'internal-report': [
        m('U4', 'the Chinese uses 必須'),
        m('W11', 'Balance information gathering with prompt reporting'),
        m('E30', 'An MSO controlling both sides'),
    ],
    'tipping-off': [m('W10', 'Revealing information likely to prejudice')],
    'retention': [m('W8', 'The MSO remains responsible when intermediaries')],
    'independent-audit': [m('E36', 'awareness of staff with AML responsibilities')],
    'training': [
        m('E26', 'MSOs are encouraged to consider a mix'),
        m('B37', 'Paragraph 9.5 gives areas'),
    ],
    'law-enforcement': [m('W9', 'Use clear procedures, a contact person')],
    'periodic-return': [m('E3', 'late submission may lead to suspension/revocation')],
}}

# The question each ruling settles, in the reader's language.
ISSUES = {
    'B1': p('續牌：獲提名人缺席評核，申請「會」還是「可能」被拒', 'Renewal: the nominee misses the Assessment — “will” or “may” it be rejected'),
    'B2': p('發牌豁免：牌照指引的名單，還是現行第25條', 'Licensing exemptions: the Guide’s list, or s.25 as it stands'),
    'B3': p('第30(4)條的定罪及破產：自動不合資格，還是須考慮的事宜', 'Section 30(4) convictions and bankruptcy: an automatic bar, or matters to weigh'),
    'B4': p('非居民在港親身辦理：只用旅行證件，還是國民身分證／駕照亦可', 'Non-resident at the counter in Hong Kong: travel document only, or ID card / driving licence too'),
    'B5': p('續牌：每名持牌人都須提名應考，還是只限已沒有合格人士者', 'Renewal: must every licensee nominate, or only one with no passer left'),
    'B6': p('適當人選測試費：一次性，還是每人每次批牌及續牌HK$945', 'Fit-and-proper test fee: one-off, or HK$945 per person at each grant and renewal'),
    'B7': p('牌照費：隨申請繳付，還是其後按繳款通知書繳付', 'Licence fee: paid with the application, or later on a demand note'),
    'B8': p('撤銷／暫時吊銷理由：牌照指引的九項，還是條例的兩項', 'Grounds to revoke or suspend: the Guide’s nine, or the law’s two'),
    'B9': p('個人／合夥申請人的最終擁有人：適合「經營」還是「與業務有聯繫」', 'Ultimate owner of an individual or partnership: fit “to operate” or “to be associated”'),
    'B10': p('獨資經營者及合夥人：適合「與業務有聯繫」還是「經營金錢服務」', 'Sole proprietor and partners: fit “to be associated” or “to operate a money service”'),
    'B11': p('公司申請人：公司本身是否接受適當人選測試', 'Company applicant: is the company itself tested as fit and proper'),
    'B12': p('不遵從作為考慮因素：只限「持續地」，還是任何不遵從', 'Failure to comply as a fitness matter: only “persistently”, or any failure'),
    'B13': p('「關長認為有關的任何其他事宜」：必須考慮還是可考慮', '“Any other matter the CCE considers relevant”: must or may'),
    'B14': p('實益擁有人是否一定是自然人', 'Is a beneficial owner always a natural person'),
    'B15': p('澳門永久性居民身分證是否旅行證件', 'Is the Macau Permanent Resident Identity Card a travel document'),
    'B16': p('非經常交易：交易前核實，還是「之前或期間」', 'Occasional transaction: verify before it, or “before or during”'),
    'B17': p('高風險情況：必須確立財富及資金來源，還是可改用其他措施', 'High risk: must the MSO establish source of wealth and funds, or may it take other measures'),
    'B18': p('FATF兩份名單的名稱：舊稱還是現稱', 'Names of the two FATF lists: old titles or today’s'),
    'B19': p('電傳及匯款的8,000元：「超過」還是「等於或以上」', 'HK$8,000 for wires and remittances: “over” or “equal to or above”'),
    'B20': p('本地電傳欠缺資料：收款機構須補取甚麼', 'Domestic wire with details missing: what the receiving institution must obtain'),
    'B21': p('JFIU全名：情報組還是調查組', 'JFIU: Intelligence or Investigation'),
    'B22': p('MSO的「有關當局」：海關還是海關關長', 'The “relevant authority” for MSOs: the C&ED or the CCE'),
    'B23': p('續牌評核的30日：由信件發出還是收到起計', 'Renewal Assessment within 30 days: from the letter’s issue or its receipt'),
    'B24': p('申請遺漏資料：怎樣才構成罪行', 'Leaving a fact out of an application: what makes it an offence'),
    'B25': p('住宅處所佔用人同意：讓「獲授權人員」還是「獲授權人」進入', 'Occupant’s consent: entry by an “authorized officer” or an “authorized person”'),
    'B26': p('貨幣兌換服務：只豁除酒店，還是亦豁除附帶於主業的兌換', 'Money changing: only the hotel exception, or incidental exchange too'),
    'B27': p('續牌未於屆滿前決定：牌照繼續有效還是失效', 'Renewal undecided at expiry: does the licence stay in force or lapse'),
    'B28': p('受測試人士不合格：關長「可」拒批，還是「只在」全部合格時才可批', 'A tested person fails: the CCE “may” refuse, or may grant “only if” everyone passes'),
    'B29': p('代表客戶行事的人：按客戶要求核實，還是可憑名單', 'Person acting for the customer: verified like a customer, or from a list'),
    'B30': p('依賴香港專業中介人：有充分程序是否已足夠', 'Relying on a Hong Kong professional: are adequate procedures enough'),
    'B31': p('上市公司客戶：任何上市公司都可略過實益擁有人，還是須有披露規定', 'Listed company customer: any listed company, or only one under disclosure rules'),
    'B32': p('前PEP：風險評估是否足以停止加強措施，還是另須高級管理層批准', 'Former PEP: is a risk assessment enough to stop EDD, or is senior approval also needed'),
    'B33': p('關連境外金融機構：遷冊到香港的MSO如何處理', 'Related foreign FI as intermediary: an MSO re-domiciled to Hong Kong'),
    'B34': p('不可依賴中介人持續監察：FAQ引註33，規則在註44', 'No reliance for ongoing monitoring: the FAQ cites footnote 33; the rule is footnote 44'),
    'B35': p('8,000元或以上非電傳匯款：非居民駕照是否足夠', 'Non-wire remittance of HK$8,000 or more: is a non-resident’s driving licence enough'),
    'B36': p('8,000元身分核實：所有匯款，還是只限電傳以外的匯款', 'The HK$8,000 identity check: every remittance, or only non-wire remittances'),
    'B37': p('額外培訓主題：指引第9.7段還是第9.5段', 'Extra training topics: Guideline ¶9.7 or ¶9.5'),
    'B38': p('海關通知的較高風險：必須納入，還是「可包括」', 'C&ED-notified higher risks in the risk assessment: required, or “may include”'),
    'B39': p('「FATF識別的國家」的加強盡職審查：所有名單，還是只限呼籲採取行動名單', 'EDD for “countries identified by the FATF”: every list, or only call for action'),
    'B40': p('海外分行及附屬公司：只限在香港成立的MSO，還是包括遷冊公司', 'Overseas branches and subsidiaries: Hong Kong-incorporated only, or re-domiciled too'),
    'B41': p('維持有效程序的責任：AMLO第19(3)條還是附表2第19(3)條', 'Duty to keep effective procedures: AMLO s.19(3) or Schedule 2 s.19(3)'),
    'B42': p('處所不適合或欠佔用人同意：關長「可」拒批，還是兩項符合才可批', 'Unsuitable premises or missing consent: “may” refuse, or grant only if both are met'),
    'W1': p('高級管理人員須「通過」評核，還是只須「應考」', 'Must a senior manager pass the Assessment, or only attend it'),
    'W2': p('沒有維持本地紀錄存放地點：「將」還是「可」導致暫時吊銷／撤銷', 'No local place of storage: “will” or “may” it lead to suspension or revocation'),
    'W3': p('欠管理辦事處／存放地點資料：無效申請，還是「可」拒批', 'No management-office or storage details: invalid application, or “may” refuse'),
    'W4': p('香港居民在港辦理：一律用香港身分證，還是護照亦可', 'Hong Kong resident at the counter: always the HKID card, or a passport too'),
    'W5': p('獲豁免人士申請牌照：不受理還是可拒批', 'Exempt person applies for a licence: not accepted, or may be refused'),
    'W6': p('暫時吊銷及撤銷是否「紀律行動」', 'Are suspension and revocation “disciplinary actions”'),
    'W7': p('違反指引本身會否招致行動', 'Can breaking the Guideline itself lead to action'),
    'W8': p('中介人提供CDD副本：「不延誤」還是「合理切實可行範圍內盡快」', 'Intermediary’s CDD copies: “without delay” or “as soon as reasonably practicable”'),
    'W9': p('與執法機構的主要聯絡人：MLRO，還是就法庭命令指定的職員', 'Main contact with law enforcement: the MLRO, or a staff member named for court orders'),
    'W10': p('通風報訊罪行的準確內容', 'Tipping off: what exactly is the offence'),
    'W11': p('提交STR的時限：由首次懷疑起計，還是MLRO評估後', 'Time to file an STR: from first suspicion, or after the MLRO’s review'),
    'E1': p('沒有維持本地管理辦事處：「將」還是「可」導致暫時吊銷／撤銷', 'No local management office: “will” or “may” it lead to suspension or revocation'),
    'E2': p('新牌：獲提名人缺席評核，申請「會」還是「可能」被拒', 'New licence: the nominee misses the Assessment — “will” or “may” it be refused'),
    'E3': p('逾期提交定期申報表：「將」還是「可」導致暫時吊銷／撤銷', 'Late periodic return: “will” or “may” it lead to suspension or revocation'),
    'E4': p('親身在場客戶：「一般應」查閱正本並保留副本，還是「通常可」', 'Customer present: “should generally” see the original and keep a copy, or 通常可'),
    'E6': p('何時須查究交易：任一警號，還是兩者同時出現', 'When to look into a transaction: either warning sign, or both'),
    'E7': p('讓客戶出示正本：「always」還是「盡量」', 'Letting customers show originals: “always” or 盡量'),
    'E8': p('早上8時八號風球或黑雨：評核暫停還是改期', 'No.8 signal or black rainstorm at 8 a.m.: Assessment suspended or 改期'),
    'E9': p('續期牌照的兩年由何時起計', 'When a renewed licence’s two years start'),
    'E10': p('混合用途大廈每名佔用人的書面同意：「should」還是「須」', 'Every occupant’s written consent: “should” or 須'),
    'E11': p('屆滿前不少於45日續牌：「should」還是「須」', 'Renewal no later than 45 days before expiry: “should” or 須'),
    'E13': p('無特定處所：「使用」還是「只使用」流動電子設備', 'Not operating at particular premises: “with the use of” or 只使用 mobile devices'),
    'E16': p('不在港的非居民：「may」還是「應」使用所列文件', 'Non-resident not in Hong Kong: MSOs “may” or 應 use the listed documents'),
    'E17': p('非面對面：首次「付款」還是「存款」須經客戶名下帳戶', 'Customer not present: the first “payment” or 存款 through an account in the customer’s name'),
    'E18': p('香港居民身分：「always」還是「經常」以香港身分證核實', 'Hong Kong resident: “always” or 經常 verified by HKID card'),
    'E19': p('香港出生的未成年人：出生證明「should」還是「可」', 'Hong Kong-born minor: birth certificate “should” or 可'),
    'E20': p('按類別指定的信託受益人：「may」還是「應」列明類別範圍', 'Trust beneficiaries named by class: the MSO “may” or 應 name the class'),
    'E21': p('高風險關係：香港PEP「或」還是「及」國際組織PEP', 'High-risk relationship: a Hong Kong PEP “or” 及 an international-organisation PEP'),
    'E22': p('律師客戶帳戶：委託人款項「或」還是「及」證券', 'Solicitor’s client account: clients’ money “or” 及 securities'),
    'E23': p('停止簡化盡職審查：「真實或準確」還是「真實或充分」', 'Simplified CDD ends on doubts about “veracity or accuracy” or 真實或充分'),
    'E24': p('核實信託：約束「該信託」還是「該法人」的權力', 'Verifying a trust: powers that bind “the trust” or 該法人'),
    'E26': p('混合培訓方法：「encouraged」還是「應考慮」', 'Mix of training methods: “encouraged” or 應…考慮'),
    'E27': p('UNATMO第11L條：意圖「或」還是「及」知悉', 'UNATMO s.11L: intention “or” 及 knowledge'),
    'E28': p('副CO及MLRO：「如切實可行」修飾甚麼', 'Deputy CO and MLRO: what “where practicable” qualifies'),
    'E29': p('洗錢／恐怖分子資金籌集風險管理資料的接收者', 'Who receives management information on ML/TF risks'),
    'E30': p('兩端均受控制的可疑電傳：資料交哪個情報單位', 'Suspicious wire controlled at both ends: which intelligence unit gets the information'),
    'E31': p('聯合國制裁（UNSO）：針對人及地方，還是只針對地方', 'UN sanctions (UNSO): against persons and places, or places only'),
    'E32': p('貿易洗錢：掩飾得益「及」轉移價值，還是「或」', 'Trade-based laundering: disguising proceeds “and” moving value, or 或'),
    'E33': p('交易須相符：客戶、業務、風險狀況「及」資金來源，還是「或」', 'Transactions must fit customer, business, risk profile “and” source of funds, or 或'),
    'E34': p('第526章：服務「可能」與擴散資金籌集有關，還是「有關」', 'Cap.526: services that “may be” connected to PF, or 有關'),
    'E36': p('審計覆核：負有職責員工的認知，還是員工對職責的認知', 'Audit review: awareness of staff with AML/CFT duties, or staff’s awareness of the duty'),
    'E40': p('住宅處所同意：「C&ED的獲授權人」還是「海關人員」進入', 'Domestic premises consent: “any authorized person of C&ED” or 海關人員'),
    'E41': p('須書面審查的交易：複雜／異常「並且」無明顯目的，還是兩組', 'Transactions to examine in writing: complex or unusual “and” without purpose, or two groups'),
    'N1': p('第03份的「主要」法例沒有第629章及第34章', 'Document 03’s “main” laws leave out Cap.629 and Cap.34'),
    'N2': p('評核決定屬最終，但拒批牌照可申請覆核', 'Assessment decisions are final, yet a refused licence can be reviewed'),
    'N3': p('第14份通函：英文「should」、中文「須」', 'Circular 14: English “should”, Chinese 須'),
    'D26': p('2018年制裁通函：列入名單「可能構成」還是「已足以構成」懷疑理由', '2018 sanctions circular: inclusion “may constitute” or 已足以構成 grounds for suspicion'),
    'U1': p('重考的30日：由「成績通知」還是「成績通知發出」起計', 'Retake after 30 days: from “notification of result” or 成績通知發出'),
    'U2': p('收款機構取不到欠缺資料：「should consider」還是「須考慮」', 'Beneficiary institution cannot get missing data: “should consider” or 須考慮'),
    'U3': p('國家風險因素(iv)：英文「or」、中文「以及」', 'Country risk factor (iv): English “or”, Chinese 以及'),
    'U4': p('MLRO確認收妥內部報告：「should」還是「必須」', 'MLRO acknowledges an internal report: “should” or 必須'),
}

# Decisions not restated by a single-number exam trap. The others reuse the trap's text.
DECISIONS = {
    'B1': p('續牌記「會」：獲提名人缺席評核，續牌申請會被拒。新申請則記「可能」（E2）。', 'For a renewal, learn “will”: missing the session gets the renewal rejected. For a new licence, learn “may” (E2).'),
    'B9': p('依法例：個人／合夥申請人的最終擁有人須適合「與經營金錢服務的業務有聯繫」；只有個人經營者及合夥人須適合「經營金錢服務」。', 'Learn the law: ultimate owners of an individual or partnership are tested “to be associated with the business”; only the individual and the partners are tested “to operate a money service”.'),
    'B10': p('依法例：獨資經營者及每名合夥人須適合「經營金錢服務」；董事及最終擁有人須適合「與該業務有聯繫」。', 'Learn the law: the sole proprietor and partners are tested “to operate a money service”; directors and ultimate owners “to be associated with the business”.'),
    'B11': p('依法例：公司申請人由每名董事及每名最終擁有人接受適當人選測試；公司本身的紀錄仍可作「其他事宜」考慮。', 'Learn the law: for a company, each director and each ultimate owner must be fit and proper. The company’s own record can still count as an “other matter”.'),
    'B25': p('記「獲授權人」：佔用人同意讓獲授權人進入作例行視察。', 'Learn “authorized person” (獲授權人): the occupant consents to entry by an authorized person for routine inspection.'),
    'W2': p('記「可」：沒有維持本地紀錄存放地點，「可」導致暫時吊銷及／或撤銷牌照。', 'Learn “may”: failing to keep the local place of storage may lead to suspension and/or revocation.'),
    'E1': p('兩語同一答案，記「可」：沒有維持本地管理辦事處，「可」導致暫時吊銷及／或撤銷牌照。', 'One answer in both languages, “may”: failing to keep the local management office may lead to suspension and/or revocation.'),
    'E2': p('兩語同一答案，記「可能」：新申請的獲提名人缺席評核，申請可能被拒。中文如照錄第5.4段的「會導致」，不因此判錯。', 'One answer in both languages, “may”: a new application may be refused if the nominee misses the Assessment. In Chinese, a statement copying ¶5.4’s 會導致 is not wrong for that word alone.'),
    'E40': p('兩語同一答案，記「獲授權人」：同意是讓獲授權人進入。', 'One answer in both languages, “authorized person” (獲授權人): the consent lets an authorized person enter.'),
    'E4': p('各按本身語文學習：英文should generally、中文「通常可」。實務按英文：查閱正本並保留副本。', 'Learn the word in your exam language: English “should generally”, Chinese 通常可. In practice, do what the English says: see the original and keep a copy.'),
    'E7': p('各按本身語文學習：英文always、中文「盡量」。實務上每次都讓客戶有機會出示正本，兩者均符合。', 'Learn the word in your exam language: English “always”, Chinese 盡量. In practice, offer the chance every time; that meets both.'),
    'E8': p('各按本身語文學習：英文suspended（暫停）、中文「改期」。兩者都表示當日不舉行評核。', 'Learn the word in your exam language: English “suspended”, Chinese 改期. Either way, the Assessment does not go ahead that day.'),
    'E13': p('各按本身語文學習：英文with the use of、中文「只使用」。中文較穩妥：店舖兼用手機仍屬在處所經營。', 'Learn the item in your exam language: English “with the use of”, Chinese 只使用. The Chinese “only” is the safer reading: a shop that also uses phones still operates at premises.'),
    'E16': p('各按本身語文學習：英文may、中文「應」。兩者都接受所列三類文件。', 'Learn the word in your exam language: English “may”, Chinese 應. Either way, the three listed documents are acceptable.'),
    'E18': p('各按本身語文學習：英文always、中文「經常」。實務取always：香港居民以香港身分證或簽證身分書核實。', 'Learn the word in your exam language: English “always”, Chinese 經常. In practice, take “always”: use the HKID card or document of identity for a Hong Kong resident.'),
    'E19': p('各按本身語文學習：英文should、中文「可」。兩者所用文件都是香港出生證明。', 'Learn the word in your exam language: English “should”, Chinese 可. Either way, the document is the Hong Kong birth certificate.'),
    'E20': p('記第4.4.12段的責任：取得足夠資料，以便支付時確定受益人身分；列明類別範圍只是其中一種方法。', 'Learn the duty in ¶4.4.12: get enough information to identify the beneficiary at payout. Naming the class is one way.'),
    'E26': p('各按本身語文學習：英文為「鼓勵」考慮，中文為「應」考慮。兩者都不是規定必須混合使用。', 'English: a mix is encouraged. Chinese: you 應 (should) consider a mix. Neither text makes you use one.'),
    'E28': p('各按本身語文學習：英文的「如切實可行」修飾「相同地位」，中文的修飾「設副手」。實務上委任與正職地位相同的副CO及副MLRO，兩者均符合。', 'Learn your exam language’s version: in English “where practicable” qualifies the same status; in Chinese it qualifies having a deputy. In practice, appoint a deputy CO and MLRO with the same status; that meets both.'),
    'E29': p('各按本身語文學習：英文為董事會（或其委員會）及高級管理層，中文為高級管理層。實務上兩者都送交。', 'English: the board (or its committee) and senior management. Chinese: senior management. In practice, send it to both.'),
    'E30': p('各按本身語文學習：英文為在每個受影響地方提交並通知當地情報單位，中文為財富情報組。實務上兩者都通知。', 'English: file in every affected place and inform that place’s intelligence unit. Chinese: the JFIU. In practice, tell both.'),
    'E32': p('各按本身語文學習：英文and、中文「或」。兩者都描述利用貿易掩飾及轉移犯罪資金。', 'Learn your exam language’s wording: English “and”, Chinese 或. Both describe using trade to hide and move criminal money.'),
    'E36': p('各按本身語文學習。實務上，審計檢查負有打擊洗錢職責的員工對其職責的理解。', 'Learn your exam language’s wording. In practice, the audit checks how well staff with AML/CFT duties understand them.'),
    'D26': p('保留兩語的強度差異，不擅自統一：英文may constitute grounds；中文「已足以構成知悉或懷疑的理由」，條文「隨即適用」。兩語共同要求不變：聯合國公布後盡快篩查，不論香港是否已實施；履行知悉／懷疑舉報責任。單純同名不等於確認命中。', 'Keep the difference in strength; do not harmonise it. English: “may constitute grounds”. Chinese: inclusion is already sufficient grounds and the provisions apply at once. The common requirements stay: screen promptly after UN promulgation regardless of Hong Kong implementation, and meet knowledge/suspicion reporting duties. A merely similar name is not a confirmed match.'),
    'U1': p('筆記做法：兩語各保留本身的起算事件（英文notification of result，中文「成績通知發出當日」），並互相註明。兩語共同：30日「後」重考，不是30日內；續牌重考須在屆滿前。', 'The notes keep each language’s starting event (English “notification of result”, Chinese 成績通知發出當日) and point to the other. Common to both: retake after, not within, 30 days; renewal retakes before expiry.'),
    'U2': p('筆記做法：中文保留中介機構「應考慮」、收款機構「須考慮」；英文寫should consider，並註明中文為「須考慮」。', 'The Chinese keeps the split (intermediary 應考慮, beneficiary institution 須考慮); the English says “should consider” and notes the Chinese 須考慮.'),
    'U3': p('筆記做法：中文保留「以及」，並註明英文連詞為or；英文要點沒有加註。', 'The Chinese keeps 以及 and notes that the English conjunction is “or”; the English point carries no note.'),
    'U4': p('筆記做法：兩語各保留本身的情態詞（英文should，中文「必須」），並互相註明。', 'The notes keep each language’s modal verb (English “should”, Chinese 必須) and point to the other.'),
}

# Entries that are not rows of the CONFLICT-CALLS tables, quoted from their records.
RECORDS = {
    'D26': dict(
        record=p('revision/CONFLICT-CALLS.md，〈Additional owner decision — 20 October 2026〉', 'revision/CONFLICT-CALLS.md, “Additional owner decision — 20 October 2026”'),
        sources=[
            ('26', 'EN', '26_Medium-Selected_Circular - United Nations Sanctions - Principles and Early Alerts (7 Feb 2018).pdf, p.2, paragraph after (d): inclusion “may constitute grounds for knowledge or suspicion”'),
            ('26', 'TC', '26_中選讀_通函_聯合國制裁_原則及預警機制（2018年2月7日）.pdf, p.2, the corresponding paragraph: “已足以構成知悉或懷疑的理由”; the statutory duties/offence provisions “隨即適用”'),
        ],
        decision='Owner decision in this review: 保留两语措辞差异. Study notes must explicitly retain the difference, without silently harmonising the strength. Preserve the common requirements for prompt screening after UN promulgation regardless of Hong Kong implementation, and applicable knowledge/suspicion reporting obligations. This does not decide that a merely similar name is a confirmed match.'),
    'U1': dict(
        record=p('未列入CONFLICT-CALLS；2026年10月19日獨立審核F27加入筆記', 'Not in CONFLICT-CALLS; added to the notes by the 19 Oct 2026 independent audit, finding F27'),
        sources=[
            ('01', 'EN', 'Guidance Notes (01) ¶4.5, ¶4.6 and ¶8.2: re-take the Assessment “after 30 days upon (the) notification of result”'),
            ('01', 'TC', 'Guidance Notes (01) (Chinese) ¶4.5, ¶4.6 and ¶8.2: 於成績通知發出當日起計30日後再次應考'),
        ],
        decision=None),
    'U2': dict(
        record=p('未列入CONFLICT-CALLS；2026年10月20日深度審核加入筆記', 'Not in CONFLICT-CALLS; added to the notes by the 20 Oct 2026 depth review'),
        sources=[
            ('03', 'EN', 'AML/CFT Guideline (03) ¶10.17 and ¶10.20: the intermediary and the beneficiary institution “should either consider restricting or …”'),
            ('03', 'TC', 'AML/CFT Guideline (03) (Chinese) ¶10.17: 中介機構應考慮限制或結束…; ¶10.20: 收款機構須考慮限制或結束…'),
        ],
        decision=None),
    'U3': dict(
        record=p('未列入CONFLICT-CALLS；2026年10月20日深度審核加入筆記', 'Not in CONFLICT-CALLS; added to the notes by the 20 Oct 2026 depth review'),
        sources=[
            ('03', 'EN', 'AML/CFT Guideline (03) ¶4.9.5(c)(iv): “providing funding or support for terrorist activities, or that have designated terrorist organisations operation”'),
            ('03', 'TC', 'AML/CFT Guideline (03) (Chinese) ¶4.9.5(c)(iv): 向恐怖分子提供資金或支持恐怖活動，以及有指定恐怖主義組織在其境內運作'),
        ],
        decision=None),
    'U4': dict(
        record=p('未列入CONFLICT-CALLS；2026年10月20日深度審核加入筆記', 'Not in CONFLICT-CALLS; added to the notes by the 20 Oct 2026 depth review'),
        sources=[
            ('03', 'EN', 'AML/CFT Guideline (03) ¶7.16: “The MLRO should acknowledge receipt of an internal report”'),
            ('03', 'TC', 'AML/CFT Guideline (03) (Chinese) ¶7.16: 洗錢報告主任必須確認收到內部報告'),
        ],
        decision=None),
}
