# Official source documents

[繁體中文版 →](README.zh-Hant.md)

The 23 documents the question bank and the revision pack are written from, in
English (`EN/`) and Traditional Chinese (`TC/`). The same number denotes the
same document in both languages. All were downloaded from the official sources
listed below (the C&ED Money Service Operators Licensing System portal, and Hong
Kong e-Legislation for the Ordinance), and were checked as a full set against the portal
on 24 September 2026 (the Ordinance on 28 September 2026).

On 17 October 2026, the EN and TC PDFs for 02–09 and 19–21 were
re-downloaded and matched the archives byte for byte; substantive FAQ passages
also matched the official page. Other documents retain their original check
dates. The current Ordinance page was blocked by a client-configuration check,
so this update continues to use the archived consolidated text above.

On 18 October 2026, all 42 language editions of the 21 PDF sources other
than Ordinance 10 were re-downloaded and matched the archives byte for byte.
The substantive FAQ text also matched. Sources 01 and 23 were checked via the
current licensing/capacity-building pages, distinguishing the sample paper from
its announcement. The Ordinance page remains blocked by the client check; its
latest version was not verified. Image-only fields in source 16 were manually
transcribed, independently checked and bound to the PDF version in
`transcripts/16.json`; extraction adds them to their own pages.

Documents 01–09 are the Guidance Notes and the guidelines, 10 is the
Ordinance, 11–21 are the circulars still in force, oldest first, 22 is the FAQ
page and 23 is the official sample paper. The Guidance Notes ¶6.1 name five
reference sources for the assessment and item (5) is "Circulars issued by C&ED
to MSOs", so the circulars are examinable.

Only current documents belong here: a circular whose content a later official
document now covers is superseded, and is removed. The FATF-statement circulars
replace one another after each FATF plenary, so only the latest, 20, is kept.
The UN-sanctions notices are left out: each announces one change to a sanctions
list, and the examinable rules on screening are in 02 ch. 6. The numbers 01–23
date from 24 September 2026; earlier commits number the documents differently.

| # | Document (`EN/`) | Version | Source |
|---|---|---|---|
| 01 | Guidance Notes on the Competence Assessment | Dec 2022 | MSOS portal, licensing downloads |
| 02 | Guideline on AML/CFT for Money Service Operators | Jun 2023 | MSOS portal, guidelines |
| 03 | Licensing Guide | May 2026 | MSOS portal, guidelines |
| 04 | Guideline on Criteria for Determining Fitness and Propriety | Apr 2018 | MSOS portal, guidelines |
| 05 | Supplementary Guideline on Fitness and Propriety | Jan 2020 | MSOS portal, guidelines |
| 06 | Guidelines for Submission of Business Plan | Ver 12-2019 | MSOS portal, guidelines |
| 07 | Guidelines for Submission of AML/CFT Policy | Ver 12-2019 | MSOS portal, guidelines |
| 08 | Disciplinary Action Guideline on Pecuniary Penalty | Apr 2018 | MSOS portal, guidelines |
| 09 | Disciplinary Fining Guideline | May 2018 | MSOS portal, guidelines |
| 10 | Anti-Money Laundering and Counter-Terrorist Financing Ordinance, Cap. 615 (consolidated) | as at 24 Sep 2026 | e-Legislation, verified copy |
| 11 | Circular: Cross-boundary Movement of Currency Ordinance, Cap. 629 (MSSB/MIS_06/2018) | 31 Jul 2018 | MSOS portal, circulars |
| 12 | Circular: ML/TF Risks of Delivery Channels (MSSB/MIS_05/2021) | 13 Dec 2021 | MSOS portal, circulars |
| 13 | Circular: Supervisory Findings on Customer Due Diligence (MSSB/MIS_03/2023) | 22 Nov 2023 | MSOS portal, circulars |
| 14 | Circular: ML/TF Risks of Third Party Payments (MSSB/MIS_01/2024) | 17 Sep 2024 | MSOS portal, circulars |
| 15 | Circular: Fraudulent Websites and Social Media Platforms related to MSOs (MSSB/MIS_01/2025) | 24 Apr 2025 | MSOS portal, circulars |
| 16 | Circular: E-submission of the Periodic Return (MSSB/MIS_02/2025) | 30 May 2025 | MSOS portal, circulars |
| 17 | Circular: E-form Submission for Passenger Information (Currency and Bearer Negotiable Instruments) (MSSB/MIS_03/2025) | 23 Jun 2025 | MSOS portal, circulars |
| 18 | Circular: Amendments to the Money Changers Ordinance, Cap. 34 (MSSB/MIS_04/2025) | 17 Nov 2025 | MSOS portal, circulars |
| 19 | Circular: Trade-based Money Laundering Guidance (MSSB/MIS_01/2026) | 20 Jan 2026 | MSOS portal, circulars |
| 20 | Circular: Statements issued by the FATF (MSSB/FATF_02/2026) — the latest FATF statement | 3 Jul 2026 | MSOS portal, circulars |
| 21 | Circular: FATF public consultation on guidance to increase payment transparency (MSSB/FATF_03/2026) | 16 Jul 2026 | MSOS portal, circulars |
| 22 | FAQ applicable to all MSOs — the portal page itself (`.md`, not a PDF) | as at 8 Dec 2022 | MSOS portal, FAQs page |
| 23 | Competence Assessment — Sample Questions (MSSB/CA_01/2021) | 12 May 2021 | MSOS portal, circulars |

The Traditional Chinese editions in `TC/` carry the same numbers.

`text/` holds the text of every document in both languages, extracted by
[`extract_text.py`](extract_text.py). `quotes.json` holds, for every statement in
the bank and each language, the passage of a cited document that decides its
truth, copied word for word from that text. The tests check each quote against
the text, and the text against the documents here, so after adding or replacing
a document run `python docs/extract_text.py` (it needs PyMuPDF).

## Which documents each module is examined from

Guidance Notes ¶5.2 name the seven modules; ¶6.1 names five categories of
reference material, but neither says which category feeds which module. The
mapping below is derived from the bank itself — every citation in
[`web/questions.json`](../web/questions.json) resolved to the document it names,
by the numbers used in the table above. A question may cite two documents, so
the per-document figures can sum above the module total.

| Module | Source documents (questions citing each) | Questions |
|---|---|---|
| **1** General knowledge on AML/CFT and counter-proliferation financing | **01** (1) · **02** (23) · **10** (2) · **11** (2) · **14** (2) · **15** (1) · **17** (1) · **18** (1) · **19** (2) · **20** (2) · **21** (1) · **22** (1) | 32 |
| **2** Parts 1–7 of the AMLO | **10** (53) · **22** (1) · **23** (1) | 53 |
| **3** Schedules to the AMLO | **02** (2) · **10** (43) · **23** (1) | 43 |
| **4** Guidelines promulgated by the C&ED | **01** (10) · **03** (29) · **04** (1) · **05** (5) · **06** (5) · **07** (4) · **08** (4) · **09** (5) · **10** (2) · **16** (3) · **22** (1) · **23** (1) | 59 |
| **5** Systems and controls (i): institutional governance and strategy | **02** (55) · **07** (1) · **10** (1) · **12** (1) · **23** (1) | 56 |
| **6** Systems and controls (ii): AML/CFT control areas | **02** (62) · **10** (5) · **12** (2) · **13** (5) · **14** (7) · **22** (26) · **23** (1) | 74 |
| **7** Systems and controls (iii): demonstrating and monitoring compliance | **02** (40) · **22** (1) · **23** (2) | 40 |

The current bank includes all seven samples from **23**, plus the sample in
**01** ¶7.1. **22**, the FAQ, is cited by 30 questions: 1 in module 1, 1 in module 2, 1 in module 4, 26 in module 6, 1 in module 7. The figures above describe the active bank, excluding
retired questions preserved in Git history.

Two of these are worth singling out. **23** is the only set of sample questions
C&ED has ever published, and it settles what the paper looks like: seven items,
each a stem with four numbered statements and the five fixed options `a) 1, 2
and 3 b) 1, 2 and 4 c) 2, 3 and 4 d) 1, 3 and 4 e) All of the above`. Guidance
Notes ¶7.1 carries an eighth in the same family, with five statements and a
different fixed block. **22** is not a PDF: the FAQ exists only as a page on the
portal, so the page itself is archived as Markdown. It holds two series — “FAQ
applicable to all Money Service Operators”, 28 questions on the AML/CFT
Guideline, each answer closing with a Key Reference naming the paragraph it
elaborates, and “FAQ in Application for an MSO Licence”, 15 on licence
application, which carry no such reference. Both series serve as question material; the licensing FAQ also supports
questions on exemptions, related persons and procedural roles.

Live pages to re-check for newer editions, for the next FATF statement (which
replaces 20), and for the UN-sanctions notices (deliberately not archived here):

- FAQs: <https://eservices.customs.gov.hk/MSOS/common/faqs>
- Guidelines: <https://eservices.customs.gov.hk/MSOS/common/guidelines>
- Circulars: <https://eservices.customs.gov.hk/MSOS/common/circulars>
- The Ordinance: <https://www.elegislation.gov.hk/hk/cap615>

These documents are publications of the Government of the Hong Kong Special
Administrative Region and are reproduced here for study reference only.

They are **not covered by the licences that apply to the rest of this
repository** — see [LICENSE-CONTENT.md](../LICENSE-CONTENT.md). The MIT licence
on the rest of the repository grants no rights in them, because they are not the
author's to grant. If you redistribute this repository
or reuse the bank commercially, satisfy yourself about the terms on which these
documents may be copied; every one is available from the official sources listed
above.
