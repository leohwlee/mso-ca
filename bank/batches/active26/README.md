# 01–26 expansion review material

The v1.10.1 study-note update does not change these reviewed question patches. Current reading-material review is recorded [separately](../../../revision/study-notes/README.md).

v1.10.1只更新溫習材料及說明，未改本批題目；筆記審核另見上方連結，不用本批題目審核替代。

These three authoring patches add 171 questions to the 354 retained questions.
They are the reviewed inputs, not a second runtime question bank. The app reads
`web/questions.json`; deciding quotations live in `docs/quotes.json`.

- `p1-p4.json`, `p2-p3.json`, `p5-p7.json`: final authoring patches.
- `*-coverage.json`: topic and application mapping prepared during authoring.
- `review-input-*.json`: keyless bilingual review packets.
- `review-*.json`: independent judgments with deciding source excerpts.
- `review-*-binding.json`: hashes of the exact final text approved by each reviewer.

The P1/P4 author reviewed P2/P3 and P5; the P2/P3 author reviewed P1/P4 and P6.
The coordinating agent reviewed P7 from the keyless packet and originals before
comparing against the author answers. All agents inherited the same model.
This records independent context reviews, not a different-model-family panel.

Final re-review resolved a six-month minimum ambiguity, incomplete statutory
locators, Chinese terminology and missing CFT wording, should/must drift,
the distinction between not requiring and prohibiting repeated verification,
and a trade-risk indicator's named staff roles. False statements were also
reworded where absolute qualifiers made answers predictable; final meanings
were checked again against the same sources.

The consolidated, enforced record is
[`../../audit/active26-implementation.json`](../../audit/active26-implementation.json).
Run the checks in the repository's `DEVELOPMENT.md`. Future substantive changes
need new source review and a new verified follow-up; do not overwrite historical
evidence or refresh hashes merely to make a check pass.
