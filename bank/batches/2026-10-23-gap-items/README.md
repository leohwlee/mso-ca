# 2026-10-23 gap items and corrections

These files are the reviewed inputs for the 23 October 2026 change, not a second
runtime question bank. The app reads `web/questions.json`; deciding quotations
live in `docs/quotes.json`.

- `patch.json`: the final authoring patch, 12 revised items followed by 27 new items.
- `review-input-1.json`, `review-input-2.json`: round 1 keyless bilingual packets (34 items).
- `review-round1-1.json`, `review-round1-2.json`: round 1 blind answers as given,
  with deciding source excerpts, doubts and language notes.
- `review-round2-input-1.json`, `review-round2-input-2.json`: round 2 packets, the final
  text of the 22 items whose wording was corrected or questioned in round 1.
- `review-round2-1.json`, `review-round2-2.json`: round 2 blind answers as given.
- `review-round3-input.json`, `review-round3.json`: round 3 packet and answers for the
  five items with no true statement that the owner asked for afterwards.

Every verdict in all three rounds, in both languages, matched the key (161, 104 and
23 statements). Rounds 2 and 3 limited doubts to cases where a careful candidate could
reasonably reach the opposite verdict. The one remaining doubt, on how the Chinese
texts write the more-than-25% threshold (m6-480), is kept in the record with the
author's resolution, and the Chinese explanation now teaches that drafting convention.

Reviewers were Claude subagents (claude-opus-5-5, the model that wrote the items)
working in fresh contexts. They read only their packet, `bank/FORMAT.md`,
`revision/CONFLICT-CALLS.md` and `docs/text`. This is independent-context review,
not a different-model panel.

The consolidated, enforced record is
[`../../audit/active-followups/2026-10-23-gap-items.json`](../../audit/active-followups/2026-10-23-gap-items.json).

本批為2026年10月23日新增27題及修訂12題的已覆核輸入檔，並非第二套題庫。三輪盲審的中英文判斷
全部與答案一致；唯一保留的疑問（m6-480中文「25%以上」是否包括本數）連同處理說明記錄在案，
中文解釋亦已說明「以上」與「或以上」的分別。盲審由同一模型的子代理在獨立語境中進行，
只閱讀題目包、題目規格、來源衝突決定及原文文字檔；不屬不同模型的覆核。
