## Guard catalogue

These are candidate checks, run per language and per section; N is the option count.
Enforce deterministic correctness checks. Treat style thresholds as diagnostics
until calibrated, unless the project already requires them as hard guards.
Never change a legally material qualifier merely to improve a style statistic. The
reference suite is [`questions_test.go`](https://github.com/leohwlee/mso-ca/blob/main/questions_test.go).

| Guard | Default | Stops |
|---|---|---|
| Section counts reach `bank_min`; every item has every language, its format's fields and a valid key | — | items going missing or half-written |
| Every citation has a locator and resolves in the locator index | — | a document with no paragraph to turn to; drift (one chapter's citations sat two paragraphs high) |
| The deciding quote is found in the cited unit, in each language, and shares the key's deciding words more than any distractor does | normalise (NFKC, spaces, quote marks); exact substring, else a fuzzy partial match ≥ 95 | a missing or stale quote; semantic support still needs source-context review |
| No citation of a removed document | the manifest | superseded sources creeping back |
| Key is the longest option | ≤ 45% | "pick the longest" |
| No length rank above chance plus 15 points | ≤ 40% when N = 4 | the same tell moved to second-longest |
| Longest minus shortest within an item | ≤ 40% of the mean; floor 20 Latin / 8 CJK characters | one option carrying visibly more |
| No option more than 15% clear of its nearest neighbour, at either end | floor 8 Latin / 3 CJK characters | the comparison a reader actually makes |
| Punctuation all or none within an item | semicolons, and any mark that correlates | a semicolon marking the fuller answer |
| The key is the option sharing most with the other options no more often than chance | share of items ≤ 1/N + 2 standard errors | convergence: distractors made by varying the key |
| The key is the option sharing most words with the stem no more often than chance | the same test; stop-list the terms every item must use | the key echoing the stem |
| A guesser learnt from the bank's own options, never shown the stem or the source, stays bounded | cross-validated; e.g. ≤ 50% of four-option keys, ≤ 0.5% of simulated papers passed | a new tell that no single guard names |
| Statements carrying absolutes are true at a healthy rate | ≥ 60% bank-wide, ≥ 45% per section | "mark the absolutes false" |
| No positional references in any field | case-fold the keyword only | "option 2" after a shuffle |
| All/none uses the format's defined semantics, pinning and remapping | spec, including statement-shuffle formats | an option made meaningless by a shuffle |
| A negative stem marks its negation | NOT, EXCEPT; 不, 並非, 除…外 in bold | a negation read past |
| Numeric options in order, and ranges never overlapping | — | two defensible answers; an order that points to the key |
| Fixed blocks verbatim; answer letters and false-statement positions spread | ≤ 40% for any letter | a drifting printed format; "the second is usually false" |
| Fixed-block explanations re-derive the key | — | an explanation arguing for another answer |
| Statements independent | no "statement N", "the above", 上述 | statements leaning on each other |
| A stem citing a fine-grained provision keeps ≥ 4 substantive words; no number-as-object questions; no number-only key; no pair of number-only options | — | clause-number recall |
| No duplicate stems | exact across the bank; within a section, word 4-shingles or CJK character 4-grams, ≥ 0.75 | one question asked twice |
| No key shared across sections (within a section it is often legitimate: several offences carry one penalty) | no length floor | one question in two sections |
| Each language uses its own edition's terms, in every field including citations | banned rendering → the source's term | wording the source never uses |
| Paired terms keep both limbs | e.g. ML/TF | half the concept dropped in translation |
| Script purity; no other-language words the source does not print; no language tags | e.g. simplified characters in Traditional text | a slip from a fixer's draft |
| Locator words match the document | e.g. Chinese 條 for a statute section, 段 for a guideline paragraph | a paragraph cited with the statute's word |
| A translated "the said X" points back to something already met in the item | stem, then statements in order | a determiner referring to nothing |
| Each language version of an item is the other's nearest neighbour | cross-lingual embeddings, calibrated on a hand-labelled sample | two languages drifting into two questions |

**Writing guards.**

- Case-fold the keyword only: `(?i:option|answer)\s+[A-E]`. A whole-pattern
  `(?i)` makes "answer a question" fail the build.
- Put no length floor in a duplicate check that already keys on the cited
  passage. An 11-character shared answer hid behind a 12-character floor.
- Guard correlations statistically, not per item.
- Tune each pattern on the bank until the only hits are items you mean to fix.

---

## The catalogue of tells

The tells are ordered by how much they leaked. Every one was measured, and the
direction differed between languages, so measure rather than assume.

1. **Length, in four rules. Only the last matters to a reader.**
   - *Key-is-longest.* 1,241 of 1,510 keys were the longest option, by a
     median 55 characters, and "pick the longest" passed 64% of simulated
     papers.
   - *Rank.* Trimming keys moved them to second-longest in half the bank, so
     cap every rank.
   - *Spread.* Rank ignores size: 40/41/42/130 ranks like 40/41/42/43.
   - *Standout.* Readers compare an option with its nearest neighbour. With the
     first three rules met, an English option more than 25% longer than its
     nearest rival was the key 1 time in 55 (a reverse tell). One more than 25%
     shorter was the key 47% of the time. In Chinese, standing out long meant
     the key 37% of the time.
   - *The rank-shift trap.* Padding one distractor past the key moves the key to
     rank 2. Pad two, each clearing the key by 2 characters or more, because
     ties sort to the better rank. Better still, trim the bloated option. Rank
     skew left on options differing by a character or two (dates, names) is
     unreadable, so say so instead of chasing it.
2. **Hedges mark true statements.** Drafting hedges what is true: "reasonable"
   or "appropriate" marked the key 71% of the time in English and 62% in
   Chinese. In the mirror image, an option alone saying "only" or "solely" was
   the key 6.5% of the time, and one alone carrying a currency figure 6%. Hedge
   distractors in the same register.
3. **Absolutes mark false statements.** A statement carrying "only", "always",
   "never" or "need not" was true 32% of the time, against a 76% base rate.
   Marking absolutes false scored 66–71% where the rule discriminated, against
   20% for chance, because overstating a true rule is the easiest way to
   falsify it. Make the statement wrong on substance instead, delete incidental
   absolutes, and put accurate absolutes on true statements. Don't dodge the
   regex: "where X, so Y falls short" keeps the exclusivity for a reader.
4. **Negation marks false statements.** After the absolutes repair, statements
   containing a negation were true 59% of the time against a 76% base rate, and
   23–40% in two sections. Negate true statements too.
5. **Punctuation.** A semicolon made an option the key 45% of the time (chance
   25%), and a parenthesis 38–43%. Don't balance the correlation, remove the
   discrimination: every option has the mark, or none does. Most recasts become
   ", and" or ", while", and about 10% need rewriting by hand.
6. **Echo and convergence.** The key alone repeats the stem's words or its
   deciding facts; blind reviewers flagged several. When distractors are made by
   varying the key, the key is also the option sharing most with all the others,
   and test-takers are known to use that (the NBME guide names both cues).
   In the reference bank both sat at chance: the key was the most convergent
   option in 22–24% of items and the most stem-echoing in 23–25%, against 25%.
   That is what a bank whose distractors come from the source looks like.
   Measure yours.
7. **Twins and leaning statements.** 77 pairs of near-identical statements were
   found, 19 of them with one true and one false; such a pair tells the
   candidate which statement to doubt. A statement that refers to another (28
   found) exposes their relationship.
8. **Position and grammar.** Positional references break under shuffling, and
   "all of the above" means something only in a fixed block. Answer letters and
   false-statement positions must spread. Agreement with the stem (singular,
   plural, article) marks the option written first. In a fixed block, one
   statement known to be false eliminates every option containing it. Reproduce
   the examiner's block anyway, and put the difficulty in the statements.

**State the ceiling with every percentage.** The strongest lexical guesser
averaged 11.7 of 35 over 4,000 simulated papers, against a pass mark of 25 with
section floors: a 0.00% pass rate. It still got a free elimination on about one
question in eight. Say both.

---

## Languages

- **Options and statements align index for index** across languages, because
  the renderer pairs `options[i]`. Tell every packet, since length tuning tempts
  reordering.
- **When a check in one language drives an edit, re-check the other.** Rewriting
  only the flagged side split 29 questions into two exams: one told English
  candidates a document is acceptable, and Chinese candidates that it never is.
  Align to the side that was not rewritten, keeping its claim and dropping only
  the offending word.
- **A question whose key, or a statement's truth, depends on wording that
  differs between the editions is invalid in a bilingual bank.** Rework it onto
  what both texts share.
- **Terms come from each language's own edition of the cited document**, never
  from translating the other language's term.
- **CJK specifics.**
  - Count characters, not bytes.
  - Compare with character 4-grams, because word shingles collapse a Chinese
    stem into one token.
  - Normalise compatibility ideographs.
  - Model estimates of CJK length run 1–3 characters short, so overshoot by 3–4
    and `check` first.
- **Thresholds and floats.** `207 > 180*1.15` is true in Python.

---
