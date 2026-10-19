"""Post-reading wording refinements, documentation and isolated check setup."""
from pathlib import Path
import json
HERE=Path(__file__).resolve().parent
NOTES=HERE.parent
changes={
 'part1.py': [('定罪後可向原訟法庭或區域法院申請沒收。','定罪後可由原訟法庭或區域法院頒發沒收令。')],
 'part2.py': [
  ('客戶資產有獨立保障；牌照／批准、審計、介入及紀律制度均另有規定。','客戶資產保障的範圍及例外見下方第53ZRT條說明；牌照／批准、審計、介入及紀律制度均另有規定。'),
  ('Client assets have separate protection, alongside distinct approval, audit, intervention and disciplinary regimes.','See the section 53ZRT explanation below for client-asset protection and its exceptions; approval, audit, intervention and disciplinary regimes have separate provisions.'),
  ('規管／監督／調查指定金融服務','規管／監督／調查銀行、證券、保險、VA活動或其他金融服務'),
  ('regulates/supervises/investigates specified financial services','regulates/supervises/investigates banking, securities, insurance, VA activities or other financial services'),
  ('須盡快通知證監會、採可用的適當保密措施','須在合理地切實可行的範圍內盡快通知證監會、採可用的適當保密措施'),
  ('require prompt SFC notification','require SFC notification as soon as reasonably practicable'),
 ],
 'part6.py': [('通常所述居於香港的自然人成員','居於香港的自然人成員')],
}
for name,replacements in changes.items():
    target=NOTES/name;text=target.read_text(encoding='utf-8')
    for old,new in replacements:
        assert old in text,(name,old)
        text=text.replace(old,new)
    target.write_text(text,encoding='utf-8')

gap=NOTES/'gap_check.py'
gap.write_text(gap.read_text(encoding='utf-8').replace("HERE/'chinese-followup-2026-10-19'/'bank-source-routes.json'","HERE/'omissions-review-2026-10-19'/'bank-source-routes.json'"),encoding='utf-8')
builder=NOTES/'build.py'
text=builder.read_text(encoding='utf-8')
text=text.replace('See independent-audit-2026-10-19/REPORT.md for coverage and remaining limits.','See omissions-review-2026-10-19/REPORT.md for the latest omitted-content decisions and boundaries; earlier reports remain historical evidence.')
builder.write_text(text,encoding='utf-8')

readme=NOTES/'README.md';text=readme.read_text(encoding='utf-8')
start=text.index('The Chinese-source follow-up');end=text.index('Exact repository filenames')
text=text[:start]+'''The latest omitted-content review of documents 04/25 adds 12 source-backed groups
(32 bilingual point pairs), including predicate-offence proof, intelligence versus
prosecution, the significant controllers register, cross-sector laundering methods,
VA safeguards/offences/cooperation, and the non-Hong Kong DPMS cash-report contents.
The result has 75 topics, 529 bilingual point pairs, 18 tables and two diagrams.
These are size counts, not completeness measures.
See the [latest report](omissions-review-2026-10-19/REPORT.md),
[source-based inclusion decisions](omissions-review-2026-10-19/DISPOSITION.md),
and [findings with source locations](omissions-review-2026-10-19/FINDINGS.md).

第04／25份未納入內容的後續審核已落實12組補充，共32組雙語要點，
並重新生成七個Part。現有75個主題、529組雙語要點、18張表及2個示意圖；
數量不是覆蓋率。[最新報告](omissions-review-2026-10-19/REPORT.md)列出實際核對範圍、
取捨及驗證，並把需要理解的核心概念和其他行業參考分開。
歷史統計、其他行業行政費表／程序仍保留原文參考，不是因為未被引用便排除。
這不是所有條文逐字翻譯審校，也不保證涵蓋未知官方試題；官方出題來源不限於01–26。

Earlier evidence is preserved: [Chinese-source follow-up (17 findings)](chinese-followup-2026-10-19/REPORT.md),
[independent audit (36 findings)](independent-audit-2026-10-19/REPORT.md),
[official scope and original coverage map](independent-audit-2026-10-19/COVERAGE.md),
and [visual decisions](independent-audit-2026-10-19/VISUAL-REVIEW.md).
先前17項中文核對及36項獨立審核記錄原樣保留，不作本輪正確性的替代證據。

'''+text[end:]
text=text.replace('`chinese-followup-2026-10-19/bank-source-routes.json`','`omissions-review-2026-10-19/bank-source-routes.json`')
text=text.replace('[current checks](chinese-followup-2026-10-19/REPORT.md)','[current checks](omissions-review-2026-10-19/REPORT.md)')
readme.write_text(text,encoding='utf-8')

# Reuse checking mechanics only, with all evidence written to this new round.
browser=(NOTES/'chinese-followup-2026-10-19/verify_pages.cjs').read_text(encoding='utf-8')
browser=browser.replace("[[1,'#risk-assessment .concept-block:last-child','risk'],[2,'#other-sector-regimes','regimes'],[3,'#sector-specific .concept-block:last-child','schedules']]", "[[1,'#money-laundering .concept-block:last-child','predicate'],[2,'#other-sector-regimes .concept-block:nth-of-type(4)','assets'],[6,'#beneficial-owners .concept-block:last-child','scr'],[7,'#reporting-duty .concept-block:last-child','intelligence']]")
(HERE/'verify_pages.cjs').write_text(browser,encoding='utf-8')
print('Refined wording; current documentation/check outputs isolated from earlier evidence')
