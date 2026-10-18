# Authoring and reviewing MSO questions

This guide is for humans and any coding agent. Start with [AGENTS.md](../../../AGENTS.md).
The authoritative [format](../../../bank/FORMAT.md) defines the seven parts,
combination items, scoring, bilingual fields and distractor rules. Do not duplicate
those rules in another skill or invent a new format.

## Scope and source decisions

- Only documents **01–26** may decide active questions. Resolve editions through
  `docs/catalog.json`; document number, filename prefix and quote ID are identical.
- Read [source maintenance](../../SOURCE-MAINTENANCE.md) before changing sources.
  External links, archived publications and the old revision pack do not extend scope.
- Use each official language edition. Document 24 has English only: label Chinese
  items as study translations and retain English quotes. Document 25 findings refer to 2022.
- Follow the existing [source-conflict decisions](../../../revision/CONFLICT-CALLS.md).
  If an unresolved conflict changes the correct answer, identify the exact passages
  and ask the owner to resolve it. Reuse settled decisions and authorization.

## Write from a deciding passage

1. Identify a rule or a distinct application missing from the current bank; consult
   [source accounting](../../QUESTION-SOURCES.md). Do not count cosmetic rewrites as coverage.
2. Read the whole relevant passage, including conditions, exceptions, headings and
   footnotes. Inspect the original page when extracted text loses a table or diagram.
3. Write a patch using the [question schema](../../../bank/FORMAT.md). Every statement
   needs its deciding quotation and an explanation in both languages. False statements
   should change a specific actor, condition, threshold, deadline or exception;
   explain that difference. Preserve modal strength such as must, should and may.
4. Use the cited edition's official terminology. Guideline paragraphs are 段;
   Ordinance sections and subsections follow their official labels. Cite a locator
   such as `¶7.13` / `第7.13段`, not just a document title. Do not introduce English
   wording into Chinese explanations. Official sample abbreviations allowed by the
   format and tests remain allowed.
5. Generate options with `bank/apply.py`; never hand-write an option block or reuse
   retired IDs. Explanations must survive reordered statements without referring to
   an old statement number or option letter.

## Review without seeing the key

Give an independent reviewer the keyless bilingual packet from
`bank/review_packet.py`, the approved sources and the strict-reading rule.
The reviewer must judge every statement in each language and record the deciding
passage, not merely agree with an answer. Resolve every discrepancy against source
context. After any wording change, repeat review of the final text and bind its hash.
Record the actual reviewer and model; multiple agents using one model are not
cross-model verification. Do not fabricate independent review or semantic certainty.

Quote matching checks that text exists; it does not establish that the passage
supports the entire claim. Human or independent semantic review remains necessary.
Do not weaken a qualifier just to satisfy a length or style test.

## Apply, verify and preserve evidence

```bash
python bank/find.py EN 03 "target market"
python bank/apply.py next 3 15
python bank/apply.py check patch.json
python bank/review_packet.py patch.json review-input.json
python bank/apply.py apply patch.json
python bank/show.py m3-322
```

Keep the final patch, coverage mapping and reviewed-text bindings. Preserve
existing question IDs and completed scores. A changed bank needs an explicit
review record; do not replace earlier evidence or hashes to make checks pass.
Use [Development](../../../DEVELOPMENT.md) for the single complete check and build
list. Tests catch source, answer, translation, duplicate and guessing-pattern defects;
they do not replace source review. Check affected app behaviour and the offline HTML.

The former general-purpose guide and its optional guard/tool catalogues are retained
in the [cleanup archive](../../../bank/audit/history/2026-10-18-before-repository-cleanup.zip).
They are historical background, not extra setup or current project requirements.
