"""Mutation checks: source boundaries must fail before a patch reaches the bank."""
import copy
import importlib.util
import json
import pathlib
import sys
import unittest

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


if __name__=='__main__':unittest.main()
