# 2026-10-23 number, period, name and actor traps

These files are the reviewed inputs for the second 23 October 2026 change, not a
second runtime question bank. The app reads `web/questions.json`; deciding
quotations live in `docs/quotes.json`.

- `patch.json`: the final authoring patch, 2 revised items (m5-08, m3-324) followed by 36 new items
  (m1-224–228, m2-388–393, m3-348–352, m4-416–421, m5-140–142, m6-513–519, m7-221–224). Every false
  statement changes one number, period, name or actor in an otherwise faithful sentence.
- `review-input-1.json`, `review-input-2.json`: round 1 keyless bilingual packets (19 items each).
- `review-round1-1.json`, `review-round1-2.json`: round 1 blind answers as given, with deciding
  source excerpts, doubts and language notes.
- `review-round2-input-1.json`, `review-round2-input-2.json`, `review-round2-1.json`,
  `review-round2-2.json`: round 2 packets and answers for the 29 items whose wording changed after
  round 1 (language notes, doubts, the Go style rules on stems and source terms, and m7-221, which
  had repeated m7-179 and was rewritten around the Risk Assessment Report's account of the JFIU).
- `review-round3-input.json`, `review-round3.json`: round 3 packet and answers for the 9 items
  changed again after round 2.
- `review-round4-input.json`, `review-round4.json`: round 4 packet and answers for the last 3 items.
- `resolutions.json`: the author's recorded resolution of each reviewer doubt that stands beside a
  final answer (m3-324, m1-227, m3-350, m3-352, m4-416, m6-513).

Every verdict in all four rounds, in both languages, matched the key for the item as it stood
when reviewed (189, 145, 45 and 15 statements). Each item's final answer is the one given on its
final text, bound by a text hash. Language notes were cleared by rewording until none remained;
the five remaining doubts are kept with the author's resolutions.

Reviewers were Claude subagents (claude-fable-5-1, the model that wrote the items) working in
fresh contexts. They read only their packet, `bank/FORMAT.md`, `revision/CONFLICT-CALLS.md` and
`docs/text`, searching with `bank/find.py`. This is independent-context review, not a
different-model panel.

The consolidated, enforced record is
[`../../audit/active-followups/2026-10-23-number-traps.json`](../../audit/active-followups/2026-10-23-number-traps.json).

本批為2026年10月23日第二次改動（新增36題、修訂2題）的已覆核輸入檔，並非第二套題庫。每道新題的
錯誤陳述都只改動原文句子中的一個數字、期限、名稱或主體。四輪盲審（189、145、45及15句）的中英文
判斷全部與受審當時的答案一致；語言差異均以改寫消除，餘下五項疑問連同作者的處理說明記錄在案。
盲審由同一模型的子代理在獨立語境中進行，只閱讀題目包、題目規格、來源衝突決定及原文文字檔；
不屬不同模型的覆核。
