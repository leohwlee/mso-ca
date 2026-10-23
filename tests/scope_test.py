"""Mutation checks: source boundaries must fail before a patch reaches the bank."""
import copy
import importlib.util
import json
import pathlib
import sys
import unittest
import zipfile

ROOT=pathlib.Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('bank_apply',ROOT/'bank/apply.py')
authoring=importlib.util.module_from_spec(spec)
spec.loader.exec_module(authoring)
sys.path.insert(0,str(ROOT/'bank/audit'))
from active_scope import recover


class SourceScopeTests(unittest.TestCase):
    def setUp(self):
        bank=json.loads((ROOT/'web/questions.json').read_text(encoding='utf8'))
        quotes=json.loads((ROOT/'docs/quotes.json').read_text(encoding='utf8'))
        self.item=copy.deepcopy(next(q for q in bank if not q.get('official')))
        self.item['quotes']=copy.deepcopy(quotes[self.item['id']])

    def test_existing_approved_item_is_accepted(self):
        self.assertEqual(authoring.problems(self.item),[])

    def test_archived_source_cannot_enter_patch(self):
        self.item['quotes']['en'][0]['doc']='43'
        errors=authoring.problems(self.item)
        self.assertTrue(any('outside the approved' in e for e in errors))

    def test_language_override_cannot_hide_other_source_mismatch(self):
        self.item['quotes']['tc'][0]['language']='en'
        errors=authoring.problems(self.item)
        self.assertTrue(any('unsupported source-language override' in e for e in errors))

    def test_english_only_source_must_disclose_study_translation(self):
        self.item['quotes']['tc'][0].update(doc='24',language='en')
        errors=authoring.problems(self.item)
        self.assertTrue(any('label document 24 as a study translation' in e for e in errors))


class ReviewEvidenceTests(unittest.TestCase):
    def setUp(self):
        self.bank=json.loads((ROOT/'web/questions.json').read_text(encoding='utf8'))
        self.quotes=json.loads((ROOT/'docs/quotes.json').read_text(encoding='utf8'))

    def test_changed_reviewed_statement_invalidates_review(self):
        item=next(q for q in self.bank if q['id']=='m2-366')
        item['en']['statements'][0]+=' Changed after review.'
        with self.assertRaisesRegex(AssertionError,'Stale blind review'):
            recover(self.bank,self.quotes)

    def test_retained_explanation_cannot_change_without_evidence(self):
        item=self.bank[0]
        item['en']['notes'][0]+=' Unreviewed change.'
        with self.assertRaisesRegex(AssertionError,'Unreviewed old question edit'):
            recover(self.bank,self.quotes)

    def test_archived_source_rejected_even_if_quote_exists(self):
        self.quotes['m2-366']['en'][0]['doc']='43'
        with self.assertRaises(AssertionError):
            recover(self.bank,self.quotes)

    def test_changed_followup_statement_invalidates_review(self):
        item=next(q for q in self.bank if q['id']=='m6-497')
        item['tc']['statements'][0]+='（未經覆核）'
        with self.assertRaisesRegex(AssertionError,'Stale blind review'):
            recover(self.bank,self.quotes)

    def test_reviewer_doubt_needs_a_recorded_resolution(self):
        import active_scope
        followup=json.loads((ROOT/'bank/audit/active-followups/2026-10-23-gap-items.json').read_text(encoding='utf8'))
        review=next(r for r in followup['blind_review']['items'] if any(r['answer']['doubts']))
        q=next(q for q in self.bank if q['id']==review['answer']['id'])
        active_scope.check_review(review,q)
        review.pop('resolutions')
        with self.assertRaisesRegex(AssertionError,'Unresolved reviewer doubt'):
            active_scope.check_review(review,q)

    def test_revised_item_reverted_without_record_fails(self):
        followup=json.loads((ROOT/'bank/audit/active-followups/2026-10-23-gap-items.json').read_text(encoding='utf8'))
        with zipfile.ZipFile(ROOT/followup['archive']) as archive:
            old=next(q for q in json.loads(archive.read('web/questions.json')) if q['id']=='m6-480')
            old_quotes=json.loads(archive.read('docs/quotes.json'))['m6-480']
        index=next(i for i,q in enumerate(self.bank) if q['id']=='m6-480')
        self.bank[index]=old; self.quotes['m6-480']=old_quotes
        with self.assertRaisesRegex(AssertionError,'Revision changes nothing'):
            recover(self.bank,self.quotes)


if __name__=='__main__':unittest.main()
