# 2026-11-14 absolute-qualifier wording repair (draft patch)

Wording revisions to six already-reviewed Part 1 items. The patch has been
checked but has not been applied, committed, or bound to a review of the
current final text.

`python3 bank/apply.py check bank/batches/2026-11-14-absolute-tell-fix/patch.json`
passed on 14 November 2026 (UTC+8) after the further English alignment of
m1-234 statement 3 below: `6 items, 0 with problems`. No length pad was
required.

The legal defect and the truth values, traps, stems, option sets, notes, quotes
and other statements are unchanged, except for the alignment edits recorded in
this file. The first pass removed absolute-qualifier tells from seven false
English statements (and the matching Traditional Chinese, where that text also
used a word in the Chinese absolute regex). Pre-existing items and the true
statement m1-233-1 are not edited. m1-235 was aligned after the first
independent review and was not edited in this further pass.

The pre-change archive of the live bank is
`bank/audit/history/2026-11-14-before-absolute-tell-fix.zip`. It is unchanged:
this further wording change is only in the unapplied patch, so no new snapshot
was taken.

Do not apply until an independent-context reviewer has judged the final text
without keys and the verdicts have been bound to the current `text_sha256`
values. For m1-234, that value is in `review-input-round3.json`, not in
`review-input.json` or `review-input-round2.json`. For m1-235, the current
value remains the one in `review-input-round2.json`.

## Language-alignment edits after the first independent review

An independent reviewer agreed the intended keys on all six items in
`answers-round1.json` (m1-229 T F T F T; m1-230 T T F T F; m1-231 T T T F F;
m1-233 T T T T T F; m1-234 T T F T T; m1-235 T T F F). That review cannot be
bound as-is: `check_review` in bank/audit/active_scope.py requires empty
`tc_mismatch` and a resolution for every non-empty doubt. Two alignment issues
were fixed in this patch instead of inventing resolutions for mismatched text.

1. m1-234 statement 3 (false). Removing “need only” had softened the English, so
   it was no longer clearly exclusive, while the Chinese still uses 「才」 and is
   exclusive. The reviewer marked both F, but recorded a doubt and a
   `tc_mismatch`. The English was first rewritten as a permission (`may defer`
   screening until the sanctions have already been implemented through Hong
   Kong legislation) so it would be clearly exclusive, without
   TestNoAbsoluteTell EN tokens (only, solely, exclusively, alone, always,
   never, at all, whatsoever, need not, not required, no requirement, nothing
   more, no more than, in every case, in all cases) and without new
   negation-regex words. The Chinese was left unchanged:
   `金錢服務經營者須在有關制裁已透過香港法例實施之後，才按所有新指定的名單篩查本身的客戶名單。`
   Truth stays false. That wording was superseded by the further edit below.

2. m1-235 statement 1 (true). The Chinese included the official parenthetical
   「（只備有英文版）」; the English statement and the English circular do not.
   The reviewer marked both true but recorded a `tc_mismatch`. The parenthetical
   was removed from the Chinese only (it was not added to the English, because
   the English circular does not say that). Both languages now state the same
   supported fact: the updated increased-monitoring statement exists and can be
   found on the FATF website. TC is now: `除呼籲各方對高風險司法管轄區採取行動的聲明外，特別組織亦已發布一份有關被加強監察的司法管轄區的最新聲明，該聲明可於其網站取覽。`
   English statement 1 and statements 2–4 are unchanged. Truth of statement 1
   stays true. This item was not edited again after the second review.

## Further English alignment after the second independent review

An independent reviewer agreed the intended keys on both remaining items in
`answers-round2.json` (m1-234 T T F T T; m1-235 T T F F). m1-235 is clean in
both languages: no doubts and no `tc_mismatch`. It was not edited after that
review.

That review still cannot be bound for m1-234: `check_review` requires empty
`tc_mismatch`. Statement 3 has a doubt and a `tc_mismatch` because the English
said MSOs *may defer* screening (a permission) while the Chinese says they
*must* screen only after implementation (`須……才……`, a mandatory delay). Both
were false against the source, but the claims were not the same.

The English of m1-234 statement 3 was rewritten so it states the same mandatory
delay as the unchanged Chinese, still without TestNoAbsoluteTell EN tokens
(only, solely, exclusively, alone, always, never, at all, whatsoever, need not,
not required, no requirement, nothing more, no more than, in every case, in all
cases) and without new negation-regex words. EN is now: `MSOs must wait until
the relevant sanctions have already been implemented through Hong Kong
legislation before screening all new designations against their client lists.`
The Chinese is unchanged:
`金錢服務經營者須在有關制裁已透過香港法例實施之後，才按所有新指定的名單篩查本身的客戶名單。`
Truth stays false. The defect stays: circular MSSB/SAN_01/2018 requires
screening as soon as practicable whenever lists are updated, including during
the gap before Hong Kong implementation — there is no permission or duty to
wait for implementation. No other statement or item was changed. No length pad
was required.

| ID | Statement | Defect unchanged |
|---|---|---|
| m1-229 | 2 (false) | s.18 continued detention is for CBNIs reasonably suspected to be crime proceeds under s.17(1)(a), not terrorist property under s.17(1)(b) |
| m1-230 | 5 (false) | s.18(7) interested person is broader than the person from whom the CBNI was seized |
| m1-231 | 5 (false) | s.19 covers proceedings instituted in Hong Kong or elsewhere |
| m1-233 | 6 (false) | s.18(2) conditions are cumulative; the investigation ground cannot replace the reasonable-grounds suspicion that the CBNIs are such crime proceeds |
| m1-234 | 3 (false) | Circular MSSB/SAN_01/2018 requires screening new designations against client lists as soon as practicable whenever lists are updated, including during the time gap before Hong Kong implementation — there is no permission or duty to wait for implementation |
| m1-235 | 3 (false) | Increased monitoring is not a FATF call for countermeasures. The Chinese already used 「單憑」, which is not in the Chinese absolute regex, and was left unchanged |
| m1-235 | 4 (false) | Myanmar is on the Call for Action list, not the sole jurisdiction under increased monitoring |

## Review packets

Round-1 keyless packets (bound to the pre-alignment text; leave them in place):

- `review-input.json` — from `python3 bank/review_packet.py`
- `packet.md` — from `python3 bank/blind.py packet`
- `answers-round1.json` — independent answers to that earlier text. They are
  stale for m1-234 and m1-235 after the alignment edits and must not be used to
  bind the current text.

Round-2 keyless packets for the items whose final text changed after the first
alignment (m1-234 and m1-235 only), generated with
`python3 bank/review_packet.py` and `python3 bank/blind.py packet`. Leave them
in place:

- `review-input-round2.json`
- `packet-round2.md`
- `answers-round2.json` — independent answers to that round-2 text. They are
  stale for m1-234 after the further English alignment and must not be used to
  bind the current m1-234 text. They remain the review of the current m1-235
  text. No answers-round3 has been written.

Round-3 keyless packets for the only item whose final text changed in this
further pass (m1-234 only), generated with `python3 bank/review_packet.py` and
`python3 bank/blind.py packet`:

- `review-input-round3.json`
- `packet-round3.md`

Current `text_sha256` values for the items whose text has changed since the
live bank:

- m1-234 (from `review-input-round3.json`): `2a0b677f14f5dc0520f5c6913e15fef84fb2d22bdb1f803b27a4ab4259034ef6`
- m1-235 (from `review-input-round2.json`, unchanged in this pass): `80721dc0bf1f7a2c91da3dbb9cf1b667a38e4cb5c8ed25ab91a03238f599e25d`

Earlier hashes: in `review-input.json`,
`ad132aee8e49b67651dd8a5707352bcd55e24eaeca9065386822c37c0c212adb` (m1-234) and
`c007427f0580591e91b5a35ac08af9da646ee353be119f92c8e049111cd9fc54` (m1-235); in
`review-input-round2.json`, m1-234 was
`862c5f5c7c7b791cc5c20d1350c0f3f1e49d67c1ee3e35b60df9ae4a1ca71399`.

Simulated after apply, without writing the bank: EN module 1 absolute-qualifier
matches would be 6 true / 8 total (75%), above the 45% floor; bank-wide EN
absolutes 102/153 (66.67%), above the 60% floor. EN module 1 negation remains
33/46 (71.74%). TC module 1 absolutes would improve from 13/25 (52%) to 13/19
(68.42%). These figures are unchanged by the alignment edits, which introduce
no TestNoAbsoluteTell tokens. They are not a claim that the live bank has been
updated; the live bank still has the old wording, and `go test` / `scripts/check.py`
have not been run as a success check.
