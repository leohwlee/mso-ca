# Development

[繁體中文版 →](DEVELOPMENT.zh-Hant.md)

## The mock exam

The repository holds the app's parts (`web/`) and a small Go program that folds
them into the single file. Building it requires Go ≥ 1.27 and nothing else.

```bash
go test ./...                          # question-bank checks + vet
go run . -export-html dist/mso-ca.html # build the single file
python -m http.server 8321 -d web      # or: serve web/ while developing
```

The bank is `web/questions.json`. `go test ./...` is more than a shape check: it
guards the faults that quietly ruin a question bank. Most of the checks were
added after a review found the fault in real questions.

| Check | What it stops |
|---|---|
| Per-module counts, 4 or 5 options, both languages, a citation | questions going missing or half-written |
| Option length balance, rank, spread and standout | "always pick the longest" — it once passed 64% of simulated papers |
| Citation has a locator | citing a document with no paragraph to turn to |
| Statutory Chinese terms | wording the official Chinese editions never use |
| Chinese 該 points back to something already named | "the customer" or "the MSO" rendered word for word as 該客戶 or 該經營者, with nothing before it to refer to |
| Guideline paragraphs are 段 in Chinese | a Guideline paragraph called 款, the Ordinance's word for a subsection |
| ML/TF pairing | dropping the terrorist-financing half in Chinese |
| No positional references | "option 2" in an explanation, when options are shuffled |
| No duplicate stems, no shared answer across modules | one question asked twice |
| Absolutes in combination statements | "always" and "never" marking the false statement |
| Even option punctuation | a stray semicolon marking the right answer |
| Combination format | the printed option block, verbatim, and a spread of answer letters |
| Stems state the provision; no number-only options | asking what a section number says, or which number a rule lives under |
| Every question stores its deciding quote, found word for word in a document it cites | a key the cited passage does not support; a document replaced without its text being extracted again |
| Circulars cited are current | a circular that a later document has overtaken coming back |
| Combination explanations name the false statements the key implies | an explanation arguing for a different answer from the key |
| The key is neither the option most like the others nor the one echoing the stem | "convergence" and "clang", two cues test-takers are taught to use |
| A guesser that sees only the options, trained on the bank itself | a new surface tell: it may pick at most 50% of four-option keys (chance 25%) and pass at most 0.5% of simulated papers |
| Each language's fields hold that language only | "the Chinese text says…", or an English abbreviation no Chinese source prints |

The quote check reads `docs/text/`, the extracted text of every document in
`docs/EN` and `docs/TC`, and `docs/quotes.json`, which holds one deciding quote
per question and language. After adding or replacing a document, run
`python docs/extract_text.py` (it needs PyMuPDF). The check then lists every
quote that the new edition no longer supports.

The method behind that table, and behind the revision pack, is written up as a
reusable skill: see [The skill](#the-skill) below.

Fonts: DM Sans and DM Mono are embedded under the SIL Open Font License; Chinese
text uses the operating system's fonts.

## The revision pack

The pack is generated from [`revision/`](revision/README.md) with Python 3's
standard library alone:

```bash
python revision/pack_build.py dist/mso-revision-pack.html
```

[`revision/README.md`](revision/README.md) covers its layout, the rules each page
follows, and the review tools.

## The skill

[`.claude/skills/exam-prep/SKILL.md`](.claude/skills/exam-prep/SKILL.md) is the
method behind both files, written for any exam. It covers choosing and checking
the sources, settling conflicts between them, and writing the study pack and the
question bank. It also covers verifying every answer blind, guarding the bank
with tests, and delivering the mock exam. The exam format is a spec the user
defines, so nothing in the skill is tied to this exam; this repository is its
reference implementation.

Its version is in the file's front matter (`metadata.version`). Each version is
tagged `skill-vX.Y.Z` on the commit that finished it. Those tags do not begin
with `v`, so they never trigger a release.

| Version | Date | First released in | What changed |
|---|---|---|---|
| 2.1.0 | 28 Sep 2026 | not yet released | Adds the options-only guesser to the guard catalogue, and what this repository measured once it had the new checks: stored deciding quotes, convergence and echo at chance, and the guesser's results. |
| 2.0.0 | 28 Sep 2026 | not yet released | Renamed `exam-prep`. Covers the study pack and the mock-exam app as well as the bank, and makes the exam format a spec the user defines. Adds the intake questions, the conflicts register, verification against the pack, the negation, echo and twin-statement tells, and briefs for subagents. |
| 1.2.1 | 28 Sep 2026 | v1.7.2 | A translated "the said X" may point back to an earlier statement, or to a kind of X. |
| 1.2.0 | 27 Sep 2026 | v1.7.0 | Prove that a guard can fail. A translated "the said X" must point back to something the item has named. |
| 1.1.0 | 21 Sep 2026 | v1.5.9 | Numbers as the unknown: ask about the rule, not the section number. |
| 1.0.0 | 7 Sep 2026 | v1.5.8 | First version, as `exam-question-bank`, covering the question bank only. |

## Releases

Releases are cut by tag. Pushing a tag beginning with `v` runs
[`release.yml`](.github/workflows/release.yml), which vets and tests the bank,
builds the file from that exact commit, and attaches it to a GitHub release
together with the revision pack built from `revision/`. The tests run before the
build, so a tag that fails never becomes a download.

Use an annotated tag: its message becomes the release notes, so say what
changed for a candidate. Keep `--cleanup=whitespace`, or git drops every line
that starts with `#`, Markdown headings included.

```bash
git tag -a v1.7.2 --cleanup=whitespace -F notes.md
git push origin v1.7.2
```
