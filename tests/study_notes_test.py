"""Prevent regression to bank-generated notes and broken bilingual citations."""
import importlib.util
import html
import re
import sys
import unittest
from unittest.mock import patch
from pathlib import Path

STUDY = Path(__file__).resolve().parents[1] / 'revision' / 'study-notes'
sys.path.insert(0, str(STUDY))
spec = importlib.util.spec_from_file_location('study_notes_builder', STUDY / 'build.py')
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


class SourceFirstNotesTests(unittest.TestCase):
    def test_recall_aids_do_not_remove_explanations_or_qualifiers(self):
        for n, part in builder.PARTS.items():
            text = html.unescape(re.sub(r'<[^>]+>', '', builder.page(n)))
            for section in part['sections']:
                for block in section['blocks']:
                    for point in block['points']:
                        for language in ('tc', 'en'):
                            self.assertIn(point[language], text)

    def test_stage_names_are_visible_in_both_reading_languages(self):
        stage = builder.PANELS[1]['money-laundering'][0]
        self.assertEqual([s['term']['en'] for s in stage['steps']],
                         ['Placement', 'Layering', 'Integration'])
        for language in ('tc', 'en'):
            for name, step in zip(('Placement', 'Layering', 'Integration'), stage['steps']):
                self.assertIn(name, step['term'][language])
        self.assertIn('overlap', stage['note']['en'])
        self.assertEqual(stage['kind'], 'stages')

    def test_recall_tables_keep_boundaries_and_starting_events(self):
        panels = {p['id']: p for sections in builder.PANELS.values()
                  for group in sections.values() for p in group}
        money = str(panels['money-boundaries']).lower()
        self.assertIn('at least hk$120,000', money)
        self.assertIn('above hk$120,000', money)
        self.assertIn('more than hk$100,000', money)
        self.assertIn('exactly', money)
        review = next(s for s in builder.PARTS[2]['sections'] if s['id']=='review')
        self.assertIn('sent', str(review))
        self.assertIn('receipt', str(panels['assessment-clocks']).lower())
        retention = str(panels['retention-clocks']).lower()
        self.assertIn('when it ends', retention)
        self.assertIn('transaction completion', retention)
        for panel in panels.values():
            if panel['kind'] == 'table':
                self.assertTrue(all(len(row)==len(panel['headers']) for row in panel['rows']))
                self.assertTrue(all(row[-1]['tc'] and row[-1]['en'] for row in panel['rows']))

    def test_rendering_has_no_bank_or_quote_dependency(self):
        original = Path.read_text
        def guarded(path, *args, **kwargs):
            if path.name in ('questions.json', 'quotes.json'):
                raise AssertionError('Study content must not be generated from bank material')
            return original(path, *args, **kwargs)
        with patch.object(Path, 'read_text', guarded):
            builder.validate()
            for n in range(1, 8):
                page = builder.page(n)
                self.assertNotIn('which of the following', page.lower())
                self.assertNotIn('question-map', page.split('</style>')[1])

    def test_each_part_links_to_existing_sections_and_sources(self):
        from urllib.parse import unquote, urlsplit
        for n in range(1, 8):
            parser = builder.Inspector()
            parser.feed(builder.page(n))
            self.assertEqual(len(parser.ids), len(set(parser.ids)))
            for link in parser.links:
                if link.startswith('#'):
                    self.assertIn(link[1:], parser.ids)
                else:
                    self.assertTrue((STUDY / unquote(urlsplit(link).path)).resolve().is_file(), link)

    def test_english_only_source_is_labelled_in_chinese(self):
        refs = [r for s in builder.PARTS[6]['sections'] for b in s['blocks'] for r in b['refs'] if r['doc'] == '24']
        self.assertTrue(refs)
        rendered = builder.citations(refs[:1])
        self.assertIn('學習譯文', rendered)
        self.assertIn(builder.DOCS['24']['editions']['EN']['file'], rendered)
        self.assertNotIn('../../docs/TC/', rendered)


if __name__ == '__main__':
    unittest.main()
