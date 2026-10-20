# Final Assessment B — accessibility and navigation verification

20 October 2026. Independent verification of the regenerated `part-1.html` through `part-7.html`. No shipping source was edited by this reviewer.

**Result: passed for the requested checks.** The two confirmed issues from the initial B assessment are resolved. The CDD trigger map now presents coexisting requirements, and the measured navigation cases keep their destination headings below the actual toolbar.

## Verified results

| Check | Evidence | Result |
|---|---|---|
| Accessible column headings | 63 page states: seven Parts × TC/EN/Both × 390/900/1440px. The complete set of 52 headings is exposed in every language/width combination. Accessible names match the visible heading wording. | Pass |
| Accessible table titles | 15 tables × nine modes = 135 table instances. Every table has a nonempty accessible name matching its own figure or subgroup heading. | Pass |
| Operator + amount wrapping | 216 visible numeric units were measured. Every unit occupies one text line and stays inside the viewport. | Pass |
| Memory-figure hash destinations | 33 figures × nine modes = 297 visits. All headings are below the measured sticky toolbar; minimum clearance 23.61px. | Pass |
| Cross-Part figure links | Both cross-Part links exercised in all nine modes = 18 activations. Language is retained and destination headings are below the toolbar; minimum clearance 23.92px. | Pass |
| Language changes at a figure destination | All six TC/EN/Both switching directions × seven Parts × three widths = 126 transitions. All retain the intended figure heading below the toolbar; minimum clearance 23.64px. | Pass |
| Language changes after reading onward | Three width cases, with the reader deliberately scrolled away from the old hash. Switching language does not force the reader back to the old destination. | Pass |
| CDD trigger structure | Nine modes checked. Four cases, one explicitly cross-cutting suspicion/identification-doubt case, zero decision-tree nodes and zero NO-only continuation nodes. | Pass |

The mobile headers now remain in Chromium's accessibility tree while visually hidden; the visible cell labels can remain decorative duplicates without losing column meaning. The amount units are kept together and comparison tables stack according to the figure's available width. The CDD introduction explicitly says that requirements may coexist, with the any-amount requirement shown separately from relationship/transaction cases.

The current CDD figure was also visually inspected at 900px in Both mode. Its heading clears the toolbar, the cross-cutting requirement is clearly separated, and the former numbered YES/NO chain is absent. Screenshot: `previews-b/final-cdd-trigger-both-900.png`.

The browser matrix also recorded no document-width overflow, page errors or remote requests. Browser use was offline, in new temporary Chromium contexts; all browser processes were closed by the scripts.

## Test-harness correction

The first language-switch failure report is **withdrawn**. A pointer-event trace proved that Playwright's `locator.click()` automatically scrolled the sticky language control's original document position into view before delivering the click. In the traced case, the figure was correctly positioned at 143.66px before the action, but scrollY changed from 485 to 0 before `pointerdown`. This changed the state the test intended to exercise.

The final language verification therefore uses a coordinate click at the center of the observed, visible language button. All 126 transitions pass. The 19 `language-anchor` entries retained in `final-assessment-b-browser.json` are invalid harness results, not unresolved product defects. They are superseded by `final-assessment-b-language.json`. `final-assessment-b-summary.json` explicitly records this distinction and contains the reconciled final result.

A separate first-run locator timeout used newline-containing bilingual text to find a cross-Part link. That test was corrected to use the link's observed exact href. The final 18 activations passed. No product issue is inferred from that timeout.

## Final detector reconciliation

The final Impeccable CLI scan covered the same seven current generated HTML files after the last language-script rebuild. Exit code 2, **159 findings**: 5 `cramped-padding`, 77 `design-system-color`, 7 `design-system-font`, and 70 `design-system-font-size`. Per-file totals remain Part 1 = 27, Parts 2–7 = 22 each.

These are the same categories and totals as the initial B scan:

- The five padding warnings concern Part 1's intentional open rules/wrappers. The rendered stage figure did not show clipped or boundary-touching text in the initial review; no new padding defect is established.
- Color and size findings repeat the shared embedded stylesheet in seven generated files. They include legacy/overridden rules and values documented in the prose design specification rather than the detector's frontmatter ramp. They remain documentation/cleanup observations, not evidence of 147 independent rendering failures.
- The seven font findings misparse the declared `Study Sans` family; the shipped font stack agrees with DESIGN.md.

No rules were suppressed, no ignore file was added, and no design requirement was weakened to make the detector clean. The initial scan of this refinement preceded the parent's final language-script adjustment; the saved final detector artifact was refreshed once after that rebuild so it describes the final generated files.

## Evidence files and limits

- `final-assessment-b-summary.json`: reconciled pass result and precise counts.
- `final-assessment-b-browser.json`: table/accessibility, numeric-unit, hash, cross-Part and trigger measurements; exact SHA-256 fingerprints for the seven HTML files and relevant sources.
- `final-assessment-b-language.json`: authoritative coordinate-click language tests and old-hash checks.
- `final-assessment-b-click-trace.json`: evidence of the locator auto-scroll artifact.
- `final-assessment-b-detector.json`: complete unsuppressed final CLI findings.
- `final-assessment-b-check.cjs`, `final-assessment-b-language.cjs`, `final-assessment-b-click-trace.cjs`: reproduction scripts.

This is Chromium layout/accessibility-tree evidence, not an NVDA/VoiceOver speech test, cross-browser certification, legal review or learner-outcome study. No reliable user-visible detector overlay was available or claimed. No additional shipping change is recommended by this final B verification.
