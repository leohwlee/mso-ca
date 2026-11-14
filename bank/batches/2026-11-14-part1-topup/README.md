# 2026-11-14 Part 1 top-up (draft patch)

Phase B authoring patch only. It has not been applied, committed, or sent for
blind review.

`python3 bank/apply.py check bank/batches/2026-11-14-part1-topup/patch.json`
passed on 14 November 2026 (UTC+8): `8 items, 0 with problems`.

The patch revises one live item and adds seven new Part 1 items. Document
scope is 01–24 and 26 (sources used: 23, 19 and 26). Option sets are omitted;
`apply.py` generates them. The revision of m1-226 keeps the existing truth
`[T,T,F,T,F]` and traps `[null,null,period,null,actor]`, so apply will retain
its option sets.

| ID | Change | Truth | Topic |
|---|---|---|---|
| m1-226 | revise | T,T,F,T,F | Cap. 629 ss.17–18: 10 working days for crime proceeds or terrorist property; working-day definition; continued detention of items suspected to be crime proceeds (6 months vs 3; 2-year cap from the s.18(2) order; apply to a magistrate vs the Court) |
| m1-229 | new | T,F,T,F,T | s.18 scope and Court: application confined to s.17(1)(a), not terrorist property under s.17(1)(b); Court means CFI or District Court, not a magistrate or the Court of Appeal; 3-month period of an s.18(2) order |
| m1-230 | new | T,T,F,T,F | s.18(4)–(7): new-order 3-month period; 2-year cap from the s.18(2) order (not 5 years); return to an interested person on either application route; interested person is not only the person from whom the item was seized |
| m1-231 | new | T,T,T,F,F | s.19: further detention until listed proceedings (Hong Kong or elsewhere) are concluded, not a further 10 working days, and not Hong Kong proceedings only |
| m1-232 | new | T,T,F,T,T,F | Circular MSSB/FATF_02/2026: Call for Action buckets (DPRK/Iran countermeasures; Myanmar EDD; October 2026 “will consider countermeasures”); Bosnia and Herzegovina and Iraq added to increased monitoring, not Call for Action |
| m1-233 | new | T,T,T,T,T,F | s.18(2) conditions: OSCO s.25(1) proceeds ground and the s.18(2)(b) steps are cumulative; investigation, connected-offence proceedings, and forfeiture/confiscation proceedings; investigation alone is not enough |
| m1-234 | new | T,T,F,T,T | Circular MSSB/SAN_01/2018, from passages present in both EN and the truncated TC text: early alert circulars from time to time; screen new designations as soon as practicable whenever lists are updated (not only after Hong Kong implementation); time gap; existing AML/CFT offences remain relevant |
| m1-235 | new | T,T,F,F | Same circular, item (2): an updated increased-monitoring statement has been issued and can be found on the FATF website; FATF will closely monitor progress. Not, by that listing alone, a call for countermeasures, and not limited to Myanmar. The commitment-to-resolve wording is already tested in m1-161 and is not repeated as a standalone claim. Bosnia/Iraq is tested in m1-232 only. |

Quotes for Cap. 629 s.18(1) and s.19 stop at page breaks in `docs/text` (the
Chinese s.18(1) quote ends at 「財」; do not join it with 「產的現金類物品」).
Chinese for document 26 is truncated after the early pages; these items do not
rely on later-page Chinese that is missing from `docs/text/TC/26.txt`.
