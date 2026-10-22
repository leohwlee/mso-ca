"""Must-know quick sheet at the top of each part.

Each item restates a fact already in the linked section, which carries the citations.
`check` is English text that build.py requires in that section, so the sheet cannot
drift from the notes it summarises.
"""


def q(value_tc, value_en, tc, en, section, check):
    return dict(value=dict(tc=value_tc, en=value_en), text=dict(tc=tc, en=en), section=section, check=check)


QUICK = {
    1: [
        q('3', '3', '洗錢三個常見階段：存放、分層、整合；可重疊，不是固定步驟。', 'Three common ML stages: placement, layering, integration; they can overlap.', 'money-laundering', 'Placement'),
        q('6', '6', '六條核心法例：第615、405、455、575、537及526章。', 'Six core laws: Caps 615, 405, 455, 575, 537 and 526.', 'legal-framework', 'Cap.526'),
        q('14年 · 500萬', '14 yrs · HK$5m', 'DTROP／OSCO洗錢罪最高刑罰。', 'Maximum for the DTROP/OSCO laundering offence.', 'legal-framework', 'HK$5 million and 14 years'),
        q('3個月 · 5萬', '3 mths · HK$50,000', '不披露知悉或懷疑的最高刑罰。', 'Maximum for failing to disclose knowledge or suspicion.', 'legal-framework', 'HK$50,000 and three months'),
        q('3年', '3 yrs', '通風報訊最高監禁。', 'Maximum imprisonment for tipping off.', 'legal-framework', 'tipping-off up to three years'),
        q('2份名單', '2 FATF lists', '「呼籲採取行動」須加強盡職審查；「加強監察」納入風險評估。', 'Call for action requires EDD; increased monitoring feeds risk assessment.', 'international', 'call-for-action category requires enhanced due diligence'),
        q('> HK$120,000', '> HK$120,000', '跨境現金類物品須申報；恰好120,000元不用。', 'Cross-boundary CBNIs must be declared; exactly HK$120,000 need not.', 'cross-boundary-cash', 'must exceed HK$120,000'),
        q('50萬 · 2年', 'HK$500,000 · 2 yrs', '跨境申報違規或虛假申報的最高刑罰。', 'Maximum for non-compliant or false cross-boundary declarations.', 'cross-boundary-cash', 'HK$500,000 and two years'),
    ],
    2: [
        q('2年／7年', '2 / 7 yrs', '第5條：明知違反最高2年；意圖詐騙最高7年（均罰款100萬元）。', 'Section 5: knowing breach up to 2 years; intent to defraud up to 7 years (both HK$1m).', 'criminal-liability', 'HK$1 million and seven years'),
        q('100萬 · 2年', 'HK$1m · 2 yrs', '無牌經營（循公訴程序）的最高刑罰。', 'Maximum for operating without a licence (on indictment).', 'licence-scope', 'Operating without a licence carries, on indictment, up to HK$1 million and two years'),
        q('3種', '3 types', '匯款服務：匯出、收取、安排在香港以外收取。', 'Remittance: sending, receiving, arranging receipt outside Hong Kong.', 'licence-scope', 'arranging receipt outside Hong Kong'),
        q('2年', '2 yrs', '牌照有效期（或較短期限）；續期由舊牌照屆滿翌日起計。', 'Licence validity (or a shorter period); renewal runs from the day after expiry.', 'grant-renewal', 'Renewal is for two years'),
        q('≥ 45日', '≥ 45 days', '最少在屆滿前45日申請續牌。', 'Apply for renewal at least 45 days before expiry.', 'grant-renewal', 'at least 45 days before expiry'),
        q('1個月', '1 month', '資料改變起計1個月內書面通知，不是30日。', 'Notify changes in writing within one month, not 30 days.', 'changes', 'Do not substitute “30 days” for “one month”'),
        q('7日', '7 days', '停止營業當日起7日內交還牌照。', 'Return the licence within seven days beginning on cessation.', 'changes', 'within seven days beginning on the cessation date'),
        q('1,000萬或3倍', 'HK$10m or 3×', '第21條罰款上限，取較大者。', 'Section 21 penalty ceiling, whichever is greater.', 'discipline', 'greater of HK$10 million or three times'),
        q('100萬', 'HK$1m', '第43條牌照紀律罰款上限。', 'Section 43 licensing penalty ceiling.', 'discipline', 'Maximum = HK$1,000,000'),
        q('21日', '21 days', '通知「發出」後21日內申請覆核。', 'Apply for review within 21 days after the notice is sent.', 'review', 'within 21 days after notice is sent'),
    ],
    3: [
        q('4項', '4 measures', 'CDD四項措施。', 'The four CDD measures.', 'core-duties', 'The four CDD measures are'),
        q('5類', '5 sources', '核實客戶身分的法定來源，任何一類均可。', 'Statutory sources for verifying identity; any one may be used.', 'core-duties', 'five alternative sources'),
        q('≥ 120,000 · ≥ 8,000', '≥ HK$120,000 · ≥ HK$8,000', '一般非經常交易／電傳或虛擬資產轉帳的CDD門檻。', 'CDD thresholds: general occasional transactions / wire or VA transfers.', 'core-duties', 'at least HK$120,000'),
        q('> 25%', '> 25%', '實益擁有人：超過25%；恰好25%不算，另須看控制。', 'Beneficial owner: more than 25%; exactly 25% misses, and control is checked separately.', 'definitions', 'Exactly 25% alone misses'),
        q('5年', '5 yrs', 'CDD及交易紀錄最少保存5年。', 'Keep CDD and transaction records for at least five years.', 'ongoing-and-records', 'at least five years after termination'),
        q('3,810 · 945', 'HK$3,810 · HK$945', '批牌基本費；每名受測試人士的適當人選測試費。', 'Grant base fee; fit-and-proper fee per tested person.', 'fees', 'HK$3,810 base'),
        q('4項條件', '4 conditions', '空殼銀行：四項條件須全部成立。', 'Shell bank: all four conditions must hold.', 'special-cases', 'four shell-bank conditions'),
    ],
    4: [
        q('35題 · 75分鐘', '35 Qs · 75 min', '7個部分各5題，每題一個答案。', 'Seven Parts of five questions, one answer each.', 'assessment', '35 questions'),
        q('≥ 25 及 ≤ 2錯', '≥ 25 AND ≤ 2 wrong', '及格：總分最少25分，並且每部分最多錯2題。', 'Pass: at least 25 overall and no more than two wrong in any Part.', 'assessment', 'At least 25 / 35 overall'),
        q('7日 · 30日', '7 · 30 days', '續牌：收到邀請後7日內提名、30日內應考。', 'Renewal: nominate within 7 days, attend within 30 days of the invitation.', 'assessment', 'Nominate within seven days'),
        q('7日', '7 days', '成績通知發出後7日內書面要求覆檢。', 'Request rechecking in writing within seven days of the result issue.', 'assessment', 'Written request within seven days'),
        q('3個地方', '3 places', '特定處所、本地管理辦事處、本地紀錄存放地點。', 'Particular premises, local management office, local place of storage.', 'premises', 'Three places with different purposes'),
        q('14項', '14 changes', '表格6須通知的變更。', 'Changes to notify on Form 6.', 'licensing-actions', 'fourteen Form 6 changes'),
        q('9項', '9 examples', '撤銷或暫停牌照的例子（第7.1段）。', 'Examples of revocation or suspension grounds (¶7.1).', 'licensing-actions', 'nine examples'),
        q('> HK$100,000', '> HK$100,000', '第34章不適用；恰好100,000元仍適用。', 'Cap.34 does not apply; exactly HK$100,000 still does.', 'exchange-note', 'more than HK$100,000'),
        q('3日 · 12個月', '3 days · 12 mths', '違反第4條可於3日內撤銷交易；副本最少保存12個月。', 'Rescind within 3 days after a s.4 breach; keep duplicates at least 12 months.', 'exchange-note', 'at least 12 months'),
        q('17種', '17 currencies', '附表3須展示匯率的貨幣。', 'Schedule 3 currencies whose rates are displayed.', 'exchange-display', 'The 17 Schedule 3 currencies'),
    ],
    5: [
        q('3組', '3 groups', '客戶風險：客戶；國家；產品、服務、交易或交付渠道。', 'Customer risk: customer; country; product, service, transaction or delivery channel.', 'customer-assessment', 'three groups'),
        q('每2年', 'Every 2 yrs', '機構風險評估，另遇觸發事件須更新。', 'Institutional risk assessment, plus updates on trigger events.', 'institutional-assessment', 'every two years'),
        q('4項', '4 components', '制度組成：合規管理、獨立審計、員工甄選、持續培訓。', 'System components: compliance management, independent audit, employee screening, ongoing training.', 'control-framework', 'employee screening'),
        q('3項條件', '3 conditions', '簡化制度須三組條件全部符合；有懷疑時不可簡化。', 'All three groups of conditions to simplify systems; never where ML/TF is suspected.', 'control-framework', 'all three groups of conditions'),
        q('8項', '8 conditions', 'CO及MLRO的支援條件（第3.8段）。', 'Conditions enabling the CO and MLRO (¶3.8).', 'roles', 'eight conditions'),
        q('CO 4 · MLRO 3', 'CO 4 · MLRO 3', 'CO四項職能；MLRO三項主要職能。', 'CO: four functions; MLRO: three principal functions.', 'roles', 'three principal functions'),
        q('推出前', 'Before launch', '新產品、業務、渠道或技術：推出前先評估風險。', 'New products, practices, channels or technology: assess risk before launch.', 'new-business', 'Before launching'),
    ],
    6: [
        q('≥ 120,000 · ≥ 8,000', '≥ HK$120,000 · ≥ HK$8,000', 'CDD門檻：一般非經常交易／電傳或虛擬資產轉帳。', 'CDD thresholds: general occasional transactions / wire or VA transfers.', 'triggers', 'HK$120,000'),
        q('4 · 5 · 5', '4 · 5 · 5', '最低收集項目：自然人／法人／信託。', 'Minimum identification items: individual / legal person / trust.', 'identity', 'at least full name'),
        q('> 25%', '> 25%', '公司實益擁有人；另須看控制。', 'Corporate beneficial owner; control is checked separately.', 'beneficial-owners', 'more than 25%'),
        q('3組', '3 measures', 'PEP適用時須同時：高級管理層批准、財富及資金來源、加強持續監察。', 'PEPs, when applicable: senior approval, wealth and funds sources, enhanced monitoring.', 'peps', 'all three groups of measures'),
        q('≥ 1項', '≥ 1 measure', '非面對面：至少一項額外措施；認可數碼身分系統除外。', 'Non-face-to-face: at least one additional measure, unless a recognised digital ID is used.', 'remote', 'at least one additional measure'),
        q('6類', '6 parties', '跨境電傳或匯款最少須篩查的人士。', 'Minimum parties to screen in a cross-border wire or remittance.', 'screening', 'Six minimum groups'),
        q('8個', '8 red flags', '第三方付款警號（第08份）。', 'Third-party payment red flags (document 08).', 'third-party-payments', 'eight red flags'),
        q('43個 · 6組', '43 in 6 groups', '可疑交易警號（第7.10段），並非詳盡無遺。', 'Suspicious-transaction indicators (¶7.10), non-exhaustive.', 'suspicion-indicators', '43 non-exhaustive indicators'),
        q('2012年4月1日', '1 Apr 2012', '之前建立關係的是既有客戶，不是永久豁免。', 'Relationships before this date are pre-existing, not permanently exempt.', 'monitoring', '1 April 2012'),
        q('4種', '4 documents', '第13條匯款的識別文件：身分證、身分證明書、簽證身分書、旅行證件。', 'Section 13 remittance ID documents: identity card, certificate of identity, document of identity, travel document.', 'remittances', 'identity card, certificate of identity, document of identity or travel document'),
    ],
    7: [
        q('沒有下限', 'No minimum', 'STR沒有最低金額；嘗試或未完成的交易也可觸發。', 'No minimum STR amount; attempted or uncompleted transactions can trigger it.', 'reporting-duty', 'There is no minimum reporting amount'),
        q('3項', '3 components', 'STR制度：委任MLRO、清晰政策及程序、妥善紀錄。', 'STR system: appoint an MLRO, clear policies and procedures, proper records.', 'internal-report', 'three components'),
        q('3年', '3 yrs', '通風報訊最高監禁。', 'Maximum imprisonment for tipping off.', 'tipping-off', 'up to three years'),
        q('5年', '5 yrs', '關係結束或交易完成後最少保存。', 'Keep records at least five years after the relationship ends or the transaction completes.', 'retention', 'at least five years after it ends'),
        q('3年', '3 yrs', '培訓紀錄最少保存。', 'Keep training records for at least three years.', 'retention', 'Training records are retained for at least three years'),
        q('5項 · 5組', '5 topics · 5 groups', '培訓主題（第9.4段）及對象組別（第9.5段）。', 'Training topics (¶9.4) and staff groups (¶9.5).', 'training', 'five common topics'),
        q('半年 · 2星期', 'Half-yearly · 2 wks', '定期申報表每半年電子提交；期初2星期內提交。', 'Periodic returns half-yearly online; submit within 2 weeks of each half-year.', 'periodic-return', 'within 2 weeks'),
        q('4步', '4 steps', 'SAFE：篩查、提問、查找、評估。', 'SAFE: screen, ask, find, evaluate.', 'safe', 'The four SAFE steps'),
    ],
}
