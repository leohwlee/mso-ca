"""Exam traps from the owner's settled decisions in revision/CONFLICT-CALLS.md.

Only decisions with one answer in both reading languages appear here: between-document
(B), within-document (W), one-answer English/Chinese (E) and not-a-conflict (N) items.
Language-specific wording stays with each language view, as CONFLICT-CALLS requires,
so no note compares the two language versions.
"""


def t(ids, tc, en):
    return dict(ids=ids.split(), text=dict(tc=tc, en=en))


TRAPS = {1: {
    'legal-framework': [
        t('N1', '第03份第1.14段列六條「主要」法例：AMLO、DTROP、OSCO、UNATMO、UNSO及WMD(CPS)O。第629章及第34章另由通函列為打擊洗錢相關法例，兩者並不矛盾。', 'Document 03 ¶1.14 lists six “main” laws: AMLO, DTROP, OSCO, UNATMO, UNSO and WMD(CPS)O. Circulars also treat Cap.629 and Cap.34 as AML/CFT laws; the two do not conflict.'),
        t('E31', 'UNSO的制裁對象是人及中華人民共和國以外的地方，不只是地方。', 'UNSO sanctions target persons and places outside the People’s Republic of China, not places only.'),
        t('E34', '第526章：有合理理由相信或懷疑服務「可能」與擴散資金籌集有關，已足以觸發禁止。', 'Cap.526: a reasonable belief or suspicion that services “may be” connected to PF is enough for the prohibition.'),
    ],
    'international': [
        t('B18', 'FATF兩份名單現稱「呼籲各方對高風險司法管轄區採取行動」（舊稱「公開聲明」）及「被加強監察的司法管轄區」（舊稱「持續進程」）。', 'The two FATF lists are now “High-Risk Jurisdictions subject to a Call for Action” (formerly the “Public Statement”) and “Jurisdictions under Increased Monitoring” (formerly the “On-going Process”).'),
        t('B39', '「呼籲採取行動」名單：必須採取加強盡職審查。「加強監察」名單：屬風險因素，不自動要求加強盡職審查。', 'Call-for-action list: EDD is required. Increased-monitoring list: a risk factor, not automatic EDD.'),
    ],
    'sanctions': [
        t('E27', 'UNATMO第11L條（資助恐怖分子旅程）：有意圖「或」知悉，其一即可。', 'UNATMO s.11L (financing terrorist travel): intention or knowledge, either one is enough.'),
    ],
}, 2: {
    'statutory-map': [
        t('B21', 'JFIU全名是聯合財富情報組（Joint Financial Intelligence Unit），不是「調查」組。', 'JFIU is the Joint Financial Intelligence Unit, not an “Investigation” unit.'),
        t('B22', 'MSO的「有關當局」是海關關長（CCE）；海關（C&ED）是關長所領導的部門。', 'The “relevant authority” for MSOs is the Commissioner of Customs and Excise (CCE); the C&ED is the department the Commissioner heads.'),
        t('W7', '兩者都記：違反指引「本身」不會令人須負上司法或其他法律程序的責任；但可能因違反指引所闡釋的AMLO規定而被紀律處分或採取其他行動。', 'Learn both: a breach of the Guideline does not by itself make a person liable to judicial or other proceedings; disciplinary and other action can follow breaches of the AMLO requirements the Guideline explains.'),
    ],
    'licence-scope': [
        t('B2', '發牌豁免以現行第25條為準：政府及(a)至(h)項，包括新的保險名稱（持牌保險經紀公司、持牌個人保險代理）及穩定幣持牌人。', 'Learn the current s.25 exemptions: the Government plus (a)–(h), with the new insurance names (licensed insurance broker company, licensed individual insurance agent) and the stablecoin licensee.'),
        t('B26', '兩者都記：條例只豁除酒店為住客兌換；牌照指引另把附帶於主業的兌換（例如零售店收外幣）排除。', 'Learn both: the law excludes only a hotel changing money for its guests; the Licensing Guide also excludes exchange incidental to a main business, such as a shop accepting foreign currency in a sale.'),
        t('W5', '獲豁免人士申請牌照：海關「不會受理」（牌照指引第3.1段）。', 'An exempt person’s licence application: C&ED will not accept it (Licensing Guide ¶3.1).'),
    ],
    'grant-renewal': [
        t('B9 B10 B11', '適當人選的用語：個人經營者及合夥人須適合「經營金錢服務」；董事及最終擁有人須適合「與該業務有聯繫」。公司本身不是測試對象，但其紀錄可作為「其他事宜」考慮。', 'Fit-and-proper wording: the individual operator and partners must be fit “to operate a money service”; directors and ultimate owners must be fit “to be associated with the business”. A company is not itself tested, though its record can count as an “other matter”.'),
        t('B28', '任何受測試人士不符合適當人選準則，便不能獲批牌照：只有每名受測試人士均屬適當人選，關長才可批出或續期。', 'A failed fit-and-proper test means no licence: the CCE may grant or renew only if every tested person is fit and proper.'),
        t('B27', '兩者都記：有效的續牌申請待決時，牌照繼續有效；被視為無效的申請則不能延續，舊牌照屆滿即失效。', 'Learn both: a valid pending renewal keeps the licence in force until decided; an application treated as invalid does not, and the old licence lapses at expiry.'),
        t('E9', '續期牌照的2年（或較短期限）由續期生效日起計，即舊牌照屆滿翌日。', 'A renewed licence’s two years (or shorter period) run from the day the renewal takes effect: the day after the old licence expires.'),
    ],
    'discipline': [
        t('W6', '第43條的紀律行動只有三項：公開譴責、命令補救、罰款。撤銷或暫時吊銷牌照是第34條的另一權力。', 'Section 43 discipline has three actions only: public reprimand, an order to remedy and a pecuniary penalty. Revocation or suspension is a separate s.34 power.'),
    ],
    'enforcement': [
        t('B24', '申請遺漏資料：遺漏須令陳述屬虛假或具誤導性，而且當事人知道遺漏或罔顧是否遺漏，才構成第52(2)條罪行。', 'An omission in an application is a s.52(2) offence only if it makes the statement false or misleading and the person knows of, or is reckless as to, the omission.'),
    ],
}, 3: {
    'fees': [
        t('B6', '適當人選測試費：每名受測試人士HK$945，批牌及每次續牌都要繳付，不是一次性。', 'Fit-and-proper test fee: HK$945 for each person tested, paid at grant and again at each renewal; it is not one-off.'),
        t('B7', '法例要求申請須連同附表3費用提交；實務上海關以繳款通知書收取。', 'By law an application must be accompanied by the Schedule 3 fee; in practice C&ED collects it by demand note.'),
    ],
}, 4: {
    'premises': [
        t('B25 E40', '住宅處所的佔用人同意，是讓「獲授權人」進入作例行視察。', 'Occupants of domestic premises consent to entry by an “authorized person” for routine inspection.'),
        t('E10', '混合用途大廈：「須」取得每名佔用人的書面同意。', 'Mixed commercial-residential premises: the written consent of every occupant must be secured.'),
        t('W2 E1', '沒有維持本地紀錄存放地點或本地管理辦事處：「可」導致暫時吊銷及／或撤銷牌照。', 'Failing to maintain the local place of storage or the local management office “may” lead to suspension and/or revocation.'),
        t('W3', '兩者都記：申請欠本地管理辦事處或紀錄存放地點資料，屬無效申請，不獲處理；作為拒批理由時，則是關長「可」拒批。', 'Learn both: an application without LMO or storage-place details is invalid and not processed; as a refusal ground, the CCE “may” refuse.'),
    ],
    'application': [
        t('B42', '處所不適合，或住宅處所欠每名佔用人書面同意：不能獲批。兩項都符合，關長才可批牌。', 'Unsuitable premises, or domestic premises without every occupant’s written consent, mean no licence: the CCE may grant only if both are met.'),
    ],
    'fitness': [
        t('B3', '第30(4)條所列定罪及破產，是關長「必須考慮」的事宜，不會自動令人不合資格。', 'Section 30(4) convictions and bankruptcy are matters the CCE must weigh; they do not disqualify automatically.'),
        t('B12', '兩者都記：條例寫「持續地沒有遵守」；2018年指引補充任何不遵守亦可考慮。', 'Learn both: the law says “persistently failed to comply”; the 2018 Guideline adds that any failure can count.'),
        t('B13', '「關長認為有關的任何其他事宜」：記「必須考慮」。', '“Any other matter the CCE considers relevant”: learn “must have regard to”.'),
    ],
    'assessment': [
        t('W1', '至少一名高級管理人員須「通過」評核，不只是出席。', 'At least one senior manager must pass the Assessment, not merely attend it.'),
        t('B1 E2', '獲提名人缺席評核：續牌申請「會」被拒；新申請則「可能」被拒。', 'If the nominee misses the Assessment: a renewal “will” be rejected; a new application “may” be refused.'),
        t('B5', '續牌時，只有在已沒有通過評核的人時才須提名；須提名時，須在收到邀請後7日內提名。', 'At renewal, nominate only if no one who passed remains; when nomination is required, nominate within seven days of receiving the invitation.'),
        t('B23', '續牌評核：須在「收到」邀請信後30日內應考。', 'Renewal assessment: attend within 30 days of receiving the invitation letter.'),
        t('N2', '評核結果屬最終決定；但因未通過評核而被拒批牌照，仍可向覆核審裁處申請覆核。', 'The Assessment result is final; a licence refused for failing it can still go to the Review Tribunal.'),
    ],
    'licensing-actions': [
        t('E11', '續牌「須」在牌照屆滿前不少於45日申請。', 'Renewal must be applied for no later than 45 days before expiry.'),
        t('B8', '兩者都記：第34條只有兩項撤銷／暫時吊銷理由（不再屬適當人選；佔用人撤回或拒絕同意）；牌照指引的九項是可導致該結果的例子。', 'Learn both: s.34 has two grounds (no longer fit and proper; an occupant withdraws or refuses consent); the Guide’s nine items are examples that can lead there.'),
    ],
}, 5: {
    'institutional-assessment': [
        t('B38', '機構風險評估須一律考慮海關通知的較高風險。', 'Always take C&ED-notified higher risks into account in the institutional risk assessment.'),
    ],
    'group-controls': [
        t('B40', '海外分行及附屬公司的集團要求，適用於在香港成立為法團的MSO及遷冊到香港的公司。', 'Group requirements for overseas branches and subsidiaries cover MSOs incorporated in Hong Kong and companies re-domiciled to Hong Kong.'),
    ],
    'policy': [
        t('B41', '維持有效打擊洗錢程序的責任在AMLO「附表2」第19(3)條，不是主體條例第19條。', 'The duty to keep effective AML procedures is in Schedule 2 s.19(3) to the AMLO, not s.19 of the main Ordinance.'),
    ],
}, 6: {
    'identity': [
        t('E24', '核實信託時，核實的是規管及約束該信託本身的權力。', 'For a trust, verify the powers that regulate and bind the trust itself.'),
    ],
    'identity-evidence': [
        t('W4', '香港居民：以香港身份證（或簽證身分書）核實；旅行證件是給非居民用的。', 'Hong Kong residents: verify with the HKID card (or document of identity); a travel document is for non-residents.'),
        t('B4', '非居民在香港親身辦理：用有效旅行證件。國民身份證或駕駛執照適用於不在香港的非居民；題目沒說明地點時，三者都可。', 'A non-resident at the counter in Hong Kong: a valid travel document. A national ID card or driving licence is for a non-resident not in Hong Kong; if the location is unstated, all three count.'),
        t('B15', '澳門永久性居民身分證屬旅行證件（指引附錄A清單）；護照亦是。', 'The Macau Permanent Resident Identity Card is a travel document (Guideline Appendix A list); a passport is one too.'),
    ],
    'beneficial-owners': [
        t('B14', '實益擁有人通常是自然人；但客戶代其行事的「人」，以及信託的財產授予人、受託人、保護人或強制執行人，即使是公司亦屬實益擁有人。', 'A beneficial owner is usually an individual, but the person the customer acts for, and a trust’s settlor, trustee, protector or enforcer, count even if a company.'),
    ],
    'representatives': [
        t('B29', '兩者都記：一般按客戶的核實要求核實代表；低風險關係中，可用經客戶獨立部門確認的代表名單。', 'Learn both: normally verify a person acting for the customer like a customer; in a low-risk relationship, a list confirmed by an independent department of the customer can suffice.'),
    ],
    'timing': [
        t('B16', '非經常交易達門檻：必須在交易「前」完成CDD（包括核實）；延後核實只適用於業務關係。', 'A threshold occasional transaction: complete CDD, including verification, before carrying it out; deferred verification applies only to business relationships.'),
    ],
    'simplified': [
        t('B31', '兩者都記：條例下任何上市公司都可符合；指引補充須先確認其披露規定令擁有人透明。', 'Learn both: under the law any listed company may qualify; the Guideline adds a check that disclosure rules make its owners transparent.'),
        t('E22', '律師客戶帳戶：客戶的委託人的款項「或」證券混合存放，已符合。', 'Solicitor’s client account: clients’ money or securities pooled in it qualifies.'),
        t('E23', '停止簡化盡職審查：對資料的「真實或充分」有疑問。', 'SDD stops on doubts about the veracity or adequacy of information.'),
    ],
    'enhanced': [
        t('B17', '兩者都記：PEP須高級管理層批准、確立財富及資金來源、加強持續監察；其他高風險情況須高級管理層批准，加上確立財富及資金來源「或」其他額外措施。', 'Learn both. PEPs: senior approval, source of wealth and funds, enhanced monitoring. Other high-risk cases: senior approval plus source of wealth and funds or other additional measures.'),
    ],
    'peps': [
        t('B32', '前PEP停止加強措施：須有適當風險評估顯示已無高風險，「並且」獲高級管理層批准。', 'To stop EDD for a former PEP: an appropriate risk assessment showing no high risk and senior management approval.'),
        t('E21', '高風險關係中，客戶或實益擁有人是香港PEP「或」國際組織PEP其中一種，已須採取加強措施。', 'In a high-risk relationship, EDD applies if the customer or beneficial owner is either a Hong Kong PEP or an international organisation PEP.'),
    ],
    'remote': [
        t('E17', '非面對面：首次「付款」須經以客戶名義開立、受相類CDD標準規管的銀行帳戶進行。', 'Non-face-to-face: the first payment must go through an account in the customer’s own name with a bank subject to similar CDD standards.'),
    ],
    'intermediaries': [
        t('B30', '兩者都記：條例要求中介人有充分防洗錢程序；指引補充專業人士本身須就該客戶受附表2規管。', 'Learn both: the law requires adequate anti-ML/TF procedures; the Guideline adds that the professional must itself be under Schedule 2 for that customer.'),
        t('B33', '遷冊到香港的MSO，在關連境外金融機構規則下等同在香港成立為法團。', 'An MSO re-domiciled to Hong Kong is treated like one incorporated in Hong Kong for the related-foreign-FI route.'),
        t('B34', 'MSO不能依賴中介人進行持續監察。', 'An MSO cannot rely on an intermediary for ongoing monitoring.'),
        t('W8', '兩者都記：依賴前，須信納中介人會「不延誤」提供CDD副本；之後被要求時，須確保在「合理地切實可行範圍內盡快」提供。', 'Learn both: before relying, be satisfied copies will come “without delay”; afterwards, ensure they come “as soon as reasonably practicable” on request.'),
    ],
    'monitoring': [
        t('E6', '須查究的交易：(a) 與客戶資料不相符，「或」(b) 複雜／異常且無明顯目的，符合其一即須查究。', 'Look into a transaction that (a) does not fit what is known of the customer, or (b) is complex or unusual with no apparent purpose: either is enough.'),
        t('E41', '上述(b)本身是「並且」：複雜、款額異常大或模式異常，同時沒有明顯經濟或合法目的，才屬須以書面記錄審查結果的交易。', 'Within (b) it is “and”: a transaction that is complex, unusually large or unusually patterned and also has no apparent economic or lawful purpose falls under the written-examination duty.'),
        t('E33', '交易須與客戶、其業務、風險狀況「及」資金來源全部相符。', 'Transactions must fit all of: the customer, its business, risk profile and source of funds.'),
    ],
    'delivery': [
        t('N3', '第14份通函的定期覆核交付渠道及有懷疑時提交STR，都當作責任：指引第1.6段把「應」與「必須」同樣視為強制要求。', 'Treat circular 14’s regular channel reviews and suspicious-transaction reporting as duties: Guideline ¶1.6 treats “should” and “must” alike as mandatory.'),
    ],
    'wire-transfers': [
        t('B19', '電傳及匯款的門檻是「8,000元或以上」：恰好8,000元也包括。', 'The wire and remittance boundary is “HK$8,000 or more”: exactly HK$8,000 is caught.'),
    ],
    'wire-receiving': [
        t('B20', '兩者都記：條例下本地電傳只須補取欠缺的帳戶或參考號碼；指引要求補取所有欠缺的匯款人及收款人資料。', 'Learn both: the law requires a domestic transfer’s missing account or reference number; the Guideline asks for all missing originator and recipient information.'),
    ],
    'remittances': [
        t('B35', '8,000元或以上的非電傳匯款（附表2第13條）：只接受條例的四種識別文件——身分證、身分證明書、簽證身分書或旅行證件；駕駛執照不算。', 'Section 13 remittance check at HK$8,000 or more: only the law’s four identification documents count (identity card, certificate of identity, document of identity or travel document); a driving licence does not.'),
        t('B36', '第13條身分核實適用於電傳以外的匯款；官方樣題中「匯款達8,000元須核實匯款人身分」的陳述仍屬正確。', 'The s.13 identity check is for remittances other than wire transfers; the official sample statement that remittances of HK$8,000 or more require originator verification is still marked correct.'),
    ],
}, 7: {
    'reporting-duty': [
        t('W11', '首次產生懷疑後，須在合理地切實可行範圍內盡快提交STR；MLRO的評估也計在這段時間內，因此要迅速。', 'Report as soon as reasonably practicable after suspicion first arises; the MLRO’s review is part of that time, so it must be quick.'),
    ],
    'tipping-off': [
        t('W10', '通風報訊以第1.25段為準：知道或懷疑已作出報告，並披露相當可能損害調查的事宜；第7.6段只作例子。', 'Tipping off follows ¶1.25: knowing or suspecting a report has been made, then disclosing a matter likely to prejudice an investigation; use ¶7.6 for examples.'),
    ],
    'training': [
        t('B37', '培訓主題在指引第9.4及9.5段；第9.7段講培訓紀錄。', 'Training topics are in Guideline ¶9.4 and ¶9.5; ¶9.7 concerns training records.'),
    ],
    'law-enforcement': [
        t('W9', 'MLRO是與JFIU及執法機構聯絡的主要人員；就法庭命令另指定一名職員（可以是MLRO）作聯絡人。', 'The MLRO is the main contact with the JFIU and law enforcement; for court orders a named staff member (who can be the MLRO) is the contact.'),
    ],
    'periodic-return': [
        t('E3', '逾期提交定期申報表：「可」導致暫時吊銷及／或撤銷牌照。', 'A late periodic return “may” lead to suspension and/or revocation.'),
    ],
}}
