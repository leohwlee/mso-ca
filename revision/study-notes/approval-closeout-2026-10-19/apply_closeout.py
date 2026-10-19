"""Apply owner-approved wording and one source-checked SCR omission; preserve earlier audits."""
from pathlib import Path

HERE = Path(__file__).resolve().parent
NOTES = HERE.parent
p = NOTES / 'part6.py'
s = p.read_text(encoding='utf-8')
changes = {
    '25%剛好本身不符合「超過25%」，但可能因管理控制等另一準則符合。': '超過25%包括25.1%及25.5%，不是到26%才符合。恰好25%不符合比例條件，但可能因管理控制等另一準則符合。',
    'Exactly 25% does not satisfy the percentage test alone, but another control test may apply.': 'More than 25% includes 25.1% and 25.5%; the threshold is not 26%. Exactly 25% does not satisfy the percentage test alone, but another control test may apply.',
    '直接／間接持有>25%已發行股份；直接／間接持有>25%表決權；': '直接／間接持有超過25%已發行股份；直接／間接持有超過25%表決權；',
    '。>25%包括25.1%，不包括恰好25%；': '。超過25%（>25%）包括25.1%，不包括恰好25%；',
    '公司須指定代表協助執法人員：': 'SCR須載有指定代表的姓名或名稱及聯絡資料。公司須指定代表協助執法人員：',
    'A company designates a representative to assist law enforcement:': 'The SCR must contain the designated representative’s name and contact details. A company designates a representative to assist law enforcement:',
}
for old, new in changes.items():
    assert s.count(old) == 1, old
    s = s.replace(old, new)
before = "        ('海關指引註27明確容許MSO參閱這類登記冊"
assert s.count(before) == 1
point = "        ('2022年報告第7.25段說明：公司須向實益擁有人或相關人士送達通知，以書面確認實益擁有人的個人資料，並在訂明期限內匯報變動。沒有備存準確及最新的SCR，或拒絕執法部門依法查閱，屬刑事罪行。該段沒有列出具體日數，不應套用MSO牌照變更通知期限。', 'Paragraph 7.25 of the 2022 report describes notices to beneficial owners or related parties, written confirmation of beneficial owners’ particulars and reporting changes within the prescribed timeframe. Failure to keep an accurate, up-to-date SCR or refusal of lawful law-enforcement inspection is a criminal offence. The paragraph does not specify the number of days; MSO licensing notification deadlines must not be substituted.'),\n"
s = s.replace(before, point + before)
p.write_text(s, encoding='utf-8')

p = NOTES / 'README.md'
s = p.read_text(encoding='utf-8')
s = s.replace('adds 14 source-backed groups\n(35 bilingual point pairs)', 'adds 15 source-backed groups\n(36 bilingual point pairs), including the owner-approved closeout')
s = s.replace('532', '533').replace('已落實14組補充，共35組雙語要點', '連同本次收尾已落實15組補充，共36組雙語要點')
s = s.replace('See the [latest report](omissions-review-2026-10-19/REPORT.md),', 'See the [approval and final closeout](approval-closeout-2026-10-19/REPORT.md),\nthe [preceding omission report](omissions-review-2026-10-19/REPORT.md),')
s = s.replace('[最新報告](omissions-review-2026-10-19/REPORT.md)', '[最新收尾報告](approval-closeout-2026-10-19/REPORT.md)')
s = s.replace('See [current checks](omissions-review-2026-10-19/REPORT.md)', 'See [current checks](approval-closeout-2026-10-19/REPORT.md)')
p.write_text(s, encoding='utf-8')

# New evidence has its own output path; never refresh the historical result file.
p = NOTES / 'gap_check.py'
s = p.read_text(encoding='utf-8').replace('omissions-review-2026-10-19', 'approval-closeout-2026-10-19')
p.write_text(s, encoding='utf-8')
p = NOTES / 'README.md'
s = p.read_text(encoding='utf-8').replace('omissions-review-2026-10-19/bank-source-routes.json', 'approval-closeout-2026-10-19/bank-source-routes.json')
p.write_text(s, encoding='utf-8')
p = NOTES / 'build.py'
s = p.read_text(encoding='utf-8').replace('omissions-review-2026-10-19/REPORT.md', 'approval-closeout-2026-10-19/REPORT.md')
p.write_text(s, encoding='utf-8')
print('Applied bilingual wording, SCR duty details and current-report links.')
