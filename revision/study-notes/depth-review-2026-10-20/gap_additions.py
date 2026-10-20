"""Source-checked proposals after the authorised bank concept check.

Not imported by the builder; the main author decides placement and edits manuscripts.
No bank answers/explanations are used as prose sources.
"""

SUGGESTIONS = [
    dict(id='BG47-01', part=7, section='internal-report', action='append point',
         tc='MLRO真誠考慮所有可得資料後，若結論是沒有懷疑而決定不報JFIU，指引說一般不大可能因未報告而負刑責；這不是一律免責。仍須妥善記錄慎重考慮及行動，以顯示決定是合理作出。',
         en='Where the MLRO acts in good faith and concludes that there is no suspicion after considering all available information, the Guideline says criminal liability for not reporting is unlikely. This is not unconditional immunity. Proper records of deliberations and actions remain vital to demonstrate that the MLRO acted reasonably.',
         doc='03', tc_locator='第7.20段', en_locator='¶7.20', anchor='Providing an MLRO acts in good faith'),
    dict(id='BG47-02', part=7, section='after-report', action='append point',
         tc='JFIU會確認收到STR；如無需立即採取行動（例如向戶口發出限制令），一般會同意MSO運作該戶口。否則，MSO應採取適當行動，並在有需要時徵詢法律意見。確認收報與同意並非同一回事，亦不能取代下述持續風險覆核。',
         en='The JFIU acknowledges receipt of an STR. If no imminent action, such as a restraint order on the account, is needed, consent will usually be given for the MSO to operate it. Otherwise, the MSO should take appropriate action and seek legal advice where necessary. Acknowledgement and consent are different, and neither replaces the continuing risk review below.',
         doc='03', tc_locator='第7.24、7.26–7.27段', en_locator='¶7.24, 7.26–7.27', anchor='The JFIU will acknowledge receipt of an STR'),
    dict(id='BG47-03', part=7, section='evidence-records', action='expand business-correspondence clause',
         tc='業務通訊最低限度應包括與CDD措施或戶口運作重大改變有關的通訊；不要求每封電郵或每次日常問候都保存，但留下的通訊須足以顯示遵守AMLO。已作異常交易分析的結果仍應保存。',
         en='Business correspondence should at least cover material relating to CDD measures or significant changes in account operation. Every email or routine greeting need not be retained, but sufficient correspondence should remain to demonstrate AMLO compliance. Results of unusual-transaction analyses should still be kept.',
         doc='03', tc_locator='第8.3(d)–(e)段及註66', en_locator='¶8.3(d)–(e); footnote 66', anchor='correspondence material to CDD measures or significant changes'),
    dict(id='BG47-04', part=7, section='law-enforcement', action='expand restraint-order point',
         tc='限制令禁止在調查結果出來前處理指定款項／財產；MSO必須確保能扣留命令涵蓋的相關財產。命令未必涵蓋同一業務關係的全部財產，MSO應考慮按香港法律可動用哪些款項／財產（如有），不能把「未列入這份命令」直接當成必然可自由動用。',
         en='A restraint order prohibits dealing with specified funds/property pending the investigation’s outcome; the MSO must ensure that it can withhold the property covered. The order may not cover every asset in the relationship. The MSO should consider which funds/property, if any, may be used subject to Hong Kong law; absence from this order is not an automatic permission to deal freely.',
         doc='03', tc_locator='第7.33段', en_locator='¶7.33', anchor='must ensure that it is able to withhold'),
    dict(id='BG47-05', part=5, section='policy', action='merge into existing operational-content point',
         tc='渠道須交代面對面及非面對面交易所佔百分率；匯款的目標司法管轄區須分別說明匯入及匯出交易。',
         en='State the percentages of face-to-face and non-face-to-face transactions, and explain target jurisdictions separately for inward and outward remittances.',
         doc='21', tc_locator='第5、8項', en_locator='Items 5 and 8', anchor='Percentage of face-to-face and non-face-to-face transactions'),
    dict(id='BG47-06', part=6, section='trade-based-laundering', action='replace one-way comparison in existing point; Chinese is study translation',
         tc='登記進口貨值與相應付往境外的進口款項顯著不符；反過來，登記出口貨值與境外匯入款項顯著不符。進口看對外付款，出口看境外來款，不應只背一個方向。',
         en='Significant mismatches between registered import values and foreign transfers paying for imports, or between registered export values and incoming foreign transfers. Compare imports with outward payments and exports with inward receipts.',
         doc='24', tc_locator='英文原件第5頁：貿易單據及商品風險指標（中文為學習譯文）', en_locator='p.5, Trade documents and commodities risk indicators', anchor='Conversely, the value of registered exports'),
    dict(id='BG47-07', part=1, section='risk-assessment', action='2022 reference/understanding block near supervisory matrix; no historical counts',
         tc='2022年報告的評級更新資料包括定期風險狀況評估、業務計劃及AML/CFT政策、定期業務申報分析，以及實地面談意見；外展結果亦用來調整監督優次及風險為本監管策略。非實地監察配合實地視察，可常規查核非高風險MSO，或先收集資料作初步評估。獲選者須到海關辦事處面談，並在指定期限內交文件；「非實地」不是不用面談或只監察高風險機構。這是2022年報告所述做法。',
         en='In the 2022 report, rating updates draw on periodic risk profiles, business plans/AML policies, regular business-return analysis and feedback from on-site interviews. Outreach results also refine supervision priorities and risk-based strategies. Off-site monitoring complements on-site inspections: it may routinely review non-high-risk MSOs or collect advance information for preliminary assessment. Selected MSOs attend interviews at Customs offices and supply documents within a specified period. Off-site does not mean no interview or high-risk-only monitoring. These are practices described in the 2022 report.',
         doc='25', tc_locator='2022年版，第5.4.16、5.4.20段', en_locator='2022 edition, ¶5.4.16, 5.4.20', anchor='interviews in the C&ED’s office'),
    dict(id='BG47-XREF', part=7, section='reporting-duty', action='cross-reference only; Part1 already contains full definition',
         tc='舉報責任所指「任何財產」不限於現金或匯款，也包括動產及不動產，例如貨物及土地；完整定義見Part 1「洗錢」。',
         en='“Any property” for reporting is not limited to cash or remittances: it includes movable and immovable property, such as goods and land. See Part 1, Money laundering, for the full definition.',
         doc='03', tc_locator='第7.5段及註60', en_locator='¶7.5; footnote 60', anchor='Property includes both movable and immovable property'),
]
