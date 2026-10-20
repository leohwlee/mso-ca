# Final visual assessment A

Reviewer: `/root/visual_refinement_a`  
Date: 2026-10-20  
Method: read-only review in a fresh isolated Chromium context, using the current rebuilt local pages and A's own saved baseline. No shipping files were edited. No detector findings were used to judge visual quality.

## Verdict

**No remaining material visual or diagram-logic problem found in this scoped final review.** The principal CDD interpretation risk is resolved, nested conditions are visibly contained, peer comparisons now have equal emphasis, and the changed layouts remain readable at phone, middle and desktop widths. Preserve the current B visual direction.

The longest combined-language figures still require scrolling because they retain substantive conditions and both languages. This is a remaining reading trade-off, not a release-blocking regression or a reason to hide content.

## Current evidence

- New captures cover all 33 panels at **390 × 844**, **900 × 1000**, and **1440 × 1000**: 99 panel viewport captures in `assessment-a-evidence-after/`.
- Visually checked all 33 current panels at 900px, where the retained sidebar reduces the usable figure width. Compared changed families in complete 1440px desktop and 390px phone captures, with additional phone viewport checks. Reviewed the complete CDD case map, nested logic groups and comparison matrix.
- `assessment-a-evidence-after/observations.json` records the capture-time source hashes, rendered text, dimensions and initial anchor checks.
- `assessment-a-evidence-after/final-hashes-and-anchor-switches.json` contains the **final source/HTML hashes**, after the final anchor/language-switch patch. The earlier figure captures have the same visual wording/CSS; the later patch changed only anchor/language-switch position handling. Table accessibility labelling was already present in the first refinement.
- Use `assessment-a-evidence-after/final-stable-anchor-switches.json` for the valid final position check. It records actual pointer clicks at the visible language button centres after the page settles.
- The early click measurements inside `final-hashes-and-anchor-switches.json` are **not valid user-visible defect evidence**: Playwright's locator click scrolled the sticky controls' document position before clicking. The separate actual-pointer reproduction passed and supersedes those measurements.
- Browser contexts were closed. No server or persistent process was created.

## Resolution of the five original findings

| Finding | Final assessment | Evidence |
|---|---|---|
| P1 CDD triggers looked mutually exclusive | **Resolved.** The cross-cutting suspicion/doubt requirement is distinct from new relationship, existing relationship and occasional-transaction cases. There is no NO-only continuation spine or stop-on-YES signal. Threshold, aggregation, deferred-verification, STR and tipping-off qualifications remain visible. | `p6-memory-cdd-trigger-tree-tc-desktop-full.png`, `p6-memory-cdd-trigger-tree-both-middle-viewport.png`, `anchor-390-both.png` |
| P2 bilingual phone comparisons demanded excess recall | **Improved sufficiently for this refinement.** Metadata labels share a compact bilingual line, event/requirement blocks sit closer, and substantive text remains readable. The longer figures retain their conditions and source captions. | `p4-memory-assessment-clocks-both-mobile-viewport.png`, `p3-memory-money-boundaries-both-mobile-viewport.png`, `p7-memory-retention-clocks-both-mobile-viewport.png` |
| P2 inspection/investigation peer imbalance | **Resolved.** Peer columns have equal widths and normal body weight; mobile/middle stacking preserves the same dimension labels without treating one alternative as a subordinate exception. | `p2-memory-inspection-versus-investigation-tc-desktop-full.png`, `p2-memory-inspection-versus-investigation-both-mobile-viewport.png` |
| P2 nested AND scope was buried in prose | **Resolved.** Shell-bank affiliation criteria are nested inside the negated parent condition; date and place of birth form one outer OR option; SOW and SOF form one visibly cumulative subgroup. | `p3-memory-shell-bank-and-tc-desktop-full.png`, `p6-memory-transfer-information-both-mobile-full.png`, `p6-memory-pep-common-and-both-mobile-full.png` |
| P2 anchored title could be covered | **Resolved in the focused check.** Direct hashes and EN/Both/TC switches at the destination leave the title approximately 24–25px below the toolbar at all three reviewed widths. | `final-stable-anchor-switches.json`, `final-real-click-anchor-390.png`, `final-real-click-anchor-900.png`, `final-real-click-anchor-1440.png` |

## Measured phone improvement

Rendered full-figure heights at 390px in combined language mode, including visible source captions:

| Panel | Baseline | Final | Reduction |
|---|---:|---:|---:|
| `memory-assessment-clocks` | 5,808px | 4,814px | 17% |
| `memory-money-boundaries` | 4,955px | 4,451px | 10% |
| `memory-licence-clocks` | 3,413px | 2,977px | 13% |
| `memory-retention-clocks` | 3,248px | 2,905px | 11% |
| `memory-cdd-trigger-tree` | 3,658px | 3,106px | 15% |

These are layout measurements, not claims of faster learning. The nested-logic figures deliberately use more room to make logical scope clearer.

## All-panel final check

The 33 current panels remain present. No material visual regression was found in the checked figure families:

| Part | Panels checked | Outcome |
|---|---|---|
| 1 | three-stages, ml-tf-pf, risk-lists, cross-sector-mechanisms, cash-scope | Mechanisms remain independent; examples and date context stay explicit; thresholds and route qualifications remain visible. |
| 2 | inspection-versus-investigation, licence-clocks, penalty-ceilings, review-commencement | Equal peers, independent clocks, clearer grouped formula and genuine sequential branches remain distinguishable. |
| 3 | ownership-boundary, money-boundaries, shell-bank-and, fee-components | Regimes and operators remain distinct; nested negative affiliation scope is legible; fee column labels are now specific. |
| 4 | three-places, assessment-pass, assessment-clocks, exchange-rights | Place labels are specific; the pass-rule AND remains visible; clock groups and conditional exchange rights retain their meaning. |
| 5 | risk-levels, review-frequency, control-responsibilities | Relationships and periodic/event-triggered duties remain separate; no artificial checklist sequence was introduced. |
| 6 | cdd-trigger-tree, party-roles, cdd-extent-tree, sow-sof, pep-categories, pep-common-and, reliance-outsourcing, transfer-information, wire-responsibilities, trade-value-paths | Case map, genuine decisions, relations, comparisons, nested groups, packet and payment-chain forms each preserve their intended distinction. |
| 7 | reporting-route, after-report-parallel, retention-clocks | Reporting alternatives remain labelled, post-report responsibilities remain concurrent, and retention starts remain independent. |

At 900px, the figures correctly respond to their available content width rather than retaining cramped multi-column layouts merely because the overall browser is wider than a phone. This is the most useful responsive improvement in the final build.

## Limits and remaining work

- This is a scoped visual/semantic-presentation review, not a new legal-source audit or proof of complete syllabus coverage.
- The parent agent owns the broader 7 Parts × 3 languages × 5 viewport automated checks and interaction verification. This report does not substitute for those results.
- No further visual change is requested from this assessment. Do not expand this pass into a new design direction or remove visible conditions to reduce scrolling.

Questions skipped: the existing authorization covers this refinement and verification.
