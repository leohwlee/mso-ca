## Environment traps

- Force UTF-8 on tool output (`PYTHONIOENCODING=utf-8`), or non-Latin text comes
  back garbled and cannot be edited.
- Write patch files with the file-writing tool, not heredocs; long JSON heredocs
  break.
- `\\` in a shell command can reach the program as `\`. Build backslashes from
  codes (`chr(92)`) or use the file-editing tool, then verify the bytes.
- Keep the bank's line endings (a CRLF checkout is written back CRLF), or no
  apply round-trips byte for byte.
- Delete temporary browser profiles after rendering checks. One project left 200
  of them behind, 2.5 GB.

---

## Prior art

Checked in September 2026. None of these handles fixed option blocks, locators a
reader can turn to, languages kept aligned, or bank-level tells as tests; those
parts of this skill have no ready-made equivalent. Borrow ideas freely, but check
a repository's licence before copying code, because several carry none.

| Project | What to borrow |
|---|---|
| [huggingface/yourbench](https://github.com/huggingface/yourbench) | Citations as data: each question stores verbatim quotes and their source, and export fails when a source does not resolve. Its citation score is fuzzy word overlap, not a check of correctness. |
| [ZeKaiNie/universal-examprep-skill](https://github.com/ZeKaiNie/universal-examprep-skill) | The nearest existing skill. Quizzes are drawn from a bank by a script, not by the model. Every graded item says where its question and answer came from. A missing source reads "source unknown", never an invented page. Failing transcripts are kept as tests of the skill. It is a tutor for one learner, with no rules on distractors or guessability. |
| [1EdTech QTI](https://www.1edtech.org/standards/qti/index) (2.1 and 3.0), used by TAO and OpenOLAT | The test vocabulary (selection, ordering, time limits, item session control), and `fixed` on single options, the one standard way to pin a fixed block. |
| Moodle XML, GIFT, [gpoore/text2qti](https://github.com/gpoore/text2qti), [R/exams](https://www.r-exams.org/) | Export targets. R/exams can draw N options from a larger pool, which stops candidates memorising option shapes; every subset it can draw must still pass the length guards. |
| [kerrickstaley/genanki](https://github.com/kerrickstaley/genanki) | Anki decks from code, with stable note ids. |
| [nbalepur/mcqa-artifacts](https://github.com/nbalepur/mcqa-artifacts) | The options-only audit (Balepur, Ravichander and Rudinger, ACL 2024). |
| [MadryLab/platinum-benchmarks](https://github.com/MadryLab/platinum-benchmarks), [aryopg/mmlu-redux](https://github.com/aryopg/mmlu-redux) | Triage by a panel of models, and a fixed set of error codes for items. |
| [NBME Item-Writing Guide, 6th ed.](https://www.nbme.org/sites/default/files/2021-02/NBME_Item%20Writing%20Guide_R_6.pdf); Haladyna, Downing and Rodriguez (2002) | The standard lists of item-writing flaws, including convergence, clang, grammatical cues and the wording of true-false statements. Moore et al. (EC-TEL 2023) turned 19 of them into rules. |
| [ekzhu/datasketch](https://github.com/ekzhu/datasketch); LaBSE or [BGE-M3](https://github.com/FlagOpen/FlagEmbedding) | MinHash for duplicate sweeps at scale; cross-lingual embeddings for paraphrased duplicates and language alignment. |
| [ShinyItemAnalysis](https://github.com/patriciamar/ShinyItemAnalysis), mirt, [py-irt](https://github.com/nd-ball/py-irt) | Item analysis once there are responses; Tarrant, Ware and Mohammed (2009) for distractor thresholds. |
| [stanford-oval/storm](https://github.com/stanford-oval/storm), [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook), [Cinnamon/kotaemon](https://github.com/Cinnamon/kotaemon) | For study material: an outline first, then sections written with their citations; kinds of material defined as data; a citation that opens the highlighted source passage. |
| [open-spaced-repetition/ts-fsrs](https://github.com/open-spaced-repetition/ts-fsrs) | A spaced-repetition scheduler for the wrong-answer queue, small enough for a static app. |
