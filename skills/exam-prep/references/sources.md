# Sources

Contents: [Archive](#archive) · [Extract and normalise](#extract-and-normalise) ·
[Find](#find) · [Currency](#currency) · [Conflicts](#conflicts) ·
[Terminology](#terminology) · [Language editions](#language-editions) ·
[Copy and informal material](#copy-and-informal-material) · [Before each release](#before-each-release)

## Archive

- Get the exact list from the owner, including every language edition, and
  archive it locally under stable numbered names (`01_…`, `02_…`). Use one number
  per document everywhere: file prefix, extracted-text name, quote `doc`,
  citation. A second identifier scheme drifts.
- Keep a manifest: number, title, edition or "as at" date, origin URL, date
  checked, SHA-256. `python scripts/sources.py manifest DIR` writes the hashes.
- Never guess an identifier or a URL. Read the real listing: in the reference
  project, translated editions sat at an unpredictable offset from the originals
  in 2 cases of 14.
- Look for the examinable material nobody archives: circulars, FAQs, amendment
  notices, errata, appendices, the syllabus's own sample questions. The reference
  project's README once said the examiner published no samples; it had published
  eight, all in a format the bank did not yet have.
- Downloads within the scope the owner set may proceed; a new source or a change
  of scope is the owner's decision. Some official sites block scripted downloads
  with a client check; a browser download works where a script does not.
- Copy into a public bundle only what the licence allows; otherwise link to the
  official source.

## Extract and normalise

`python scripts/sources.py extract FILE… --out text/` writes one text file per
document, with a `=== page N ===` marker per page, from PDF (PyMuPDF or pypdf),
DOCX, HTML, Markdown and plain text. It reports pages with little or no text:
read those as images (render the page and look), because a scan, a form or a
table may hold examinable content that text search will never find.

Normalise before comparing or searching, never in the stored text:

- Unicode NFKC, which also maps CJK compatibility ideographs (U+F900–U+FAFF; one
  extract stored 行 as U+FA08) to their unified forms;
- whitespace and line breaks removed inside CJK text, collapsed elsewhere;
- curly quotes, dashes and ligatures unified; soft hyphens removed;
- page headers and footers stripped, so a quote can run across a page break.

Manually transcribed labels from images keep their page, language and source
version, and a different reviewer checks them against the image.

## Find

`python scripts/sources.py find text/ "phrase" [--doc 03] [--context 200]`
prints each hit with its document, page and context, searching the normalised
text. Search for a distinctive 5–9 word phrase: anchoring on a section number
lands in the table of contents. Where one language's extract misplaces margin
numbers, trust the document's cross-references and the other edition's
numbering.

For a large corpus, segment each document into its citable units (section and
subsection, chapter and paragraph) with the page and text in each language. A
locator index lets the checks verify that a citation resolves.

## Currency

- Only current editions, unless the owner decides otherwise. A document a later
  one covers is superseded; of a series that replaces itself (watchlists,
  periodic statements), keep the latest.
- When a source is removed, re-cite its points to the current source, and list
  for the owner every point only it made. In the reference project, 49 items
  cited superseded circulars when this was first checked.
- Record "as at" dates for consolidated laws and living documents, and say when a
  live check could not be made rather than implying it was.

## Conflicts

Sweep for contradictions before writing. In the reference project, 95 surfaced
after the bank already held 1,500 items, and settling them cost two sweeps.

- **Look in four places**: between documents; within one document; between the
  language editions of one document; and apparent conflicts that are not.
- **Write each as a decision the owner can make in a minute**: the question in
  plain words; each side quoted with document, page and locator; a
  recommendation with the rule behind it (statute over guidance, later or more
  specific over earlier or general); the risk. Dense legal reasoning loses owners;
  plain words do not.
- **Classify the decision**: **one** answer everywhere; **own** (each language
  follows its own text, and no item may turn on the difference); **both** (both
  rules are true, and an item says which it tests, never presenting one as
  overriding the other); **none** (not a conflict, recorded so nobody raises it
  again).
- **Let the owner decide on one page** with one control per item, stored where you
  can read the picks back. Record every pick in the register with an id (B1,
  W3…), and teach it in both the notes and the bank.
- A conflict found later goes to the owner before either side is taught.

## Terminology

- Keep a terminology table per document and per language. Documents from one
  author do not share one vocabulary: two guidelines from one regulator used
  different words for "premises".
- Take each term from the document an item cites. Find-and-replace across a bank
  imposes one document's term on items citing another.
- Before banning a term, check how the source uses it: a long form defined once
  and a short form used throughout are both correct.
- Locator words follow the document (a statute's section, a guideline's
  paragraph; in Chinese 條 and 段).
- Paired terms keep both limbs (money laundering *and* terrorist financing).

## Language editions

- Archive every official edition, and decide with the owner what each language
  view follows where they differ (default: its own text).
- A document with no official edition in a language is cited in its original
  language; any translation is labelled a study translation, and its deciding
  quotes keep the original text and language.
- Compare editions with a word diff for spaced languages and a character diff for
  CJK, after normalisation.

## Copy and informal material

Marketing copy, product sheets, slide decks, transcripts and wikis need extra
care:

- **Separate fact from persuasion.** Testable: features, specifications,
  prices, eligibility, procedures, policies, claims with a stated basis. Not
  testable as fact: slogans, superlatives, tone, unqualified comparisons.
- **Flag unsupported claims** to the owner rather than keying them.
- **Versions move fast.** Date every source and record which version of the copy
  an item follows; a price change is a new version of every item that states it.
- **Transcripts and slides** cite by timestamp or slide number; spoken material
  often contradicts the handout, which is a conflict for the owner.
- **The organisation's voice** may be required in answers (what staff must say);
  record that as a decision, separately from what is true.

## Before each release

Download the sources again and diff them with footers stripped. Record what
matched, what changed and what could not be checked, and re-verify every item
citing a changed passage.
