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


class StudyTipTests(unittest.TestCase):
    def setUp(self):
        sys.path.insert(0, str(STUDY))
        import tips as study_tips
        self.tips = study_tips

    def test_amlo_section_25_is_licensing_exemption(self):
        tip = self.tips.tip_for_section('25', 'AMLO Cap. 615 licensing', '2')
        self.assertIsNotNone(tip)
        self.assertEqual(tip[2], 'AMLO section 25')
        self.assertIn('exemptions under the licensing regime', tip[3])
        self.assertNotEqual(tip[2], 'DTROP/OSCO section 25')

    def test_dtrop_osco_section_25_combined_when_both_in_scope(self):
        tip = self.tips.tip_for_section('25', 'DTROP Cap. 405 and OSCO Cap. 455 dealing', '1')
        self.assertIsNotNone(tip)
        self.assertEqual(tip[2], 'DTROP/OSCO section 25')
        self.assertIn('Both section 25 offences are about dealing with proceeds', tip[3])

    def test_ambiguous_section_25_is_left_unwrapped(self):
        tip = self.tips.tip_for_section('25', 'AMLO Cap. 615 together with OSCO Cap. 455', '1')
        self.assertIsNone(tip)
        tip = self.tips.tip_for_section('25', 'a bare section number with no ordinance', '1')
        self.assertIsNone(tip)

    def test_skip_wrapping_inside_citation_and_visual_links(self):
        html = (
            '<body data-part="2" data-lang="tc">'
            '<div class="concept-block"><p>AMLO section 25 exemptions.</p></div>'
            '<div class="citations"><div class="source-citation">'
            '<a href="../../docs/EN/04.pdf">Cap. 615</a></div></div>'
            '<nav class="visual-links"><a href="part-2.html">AMLO</a></nav>'
            '</body>'
        )
        out = self.tips.apply_tips(html)
        self.assertIn('class="cite-tip"', out)
        self.assertIn('<a href="../../docs/EN/04.pdf">Cap. 615</a>', out)
        self.assertIn('<a href="part-2.html">AMLO</a>', out)
        self.assertNotIn('cite-tip" tabindex="0" role="button" data-tip-id="t',
                         out[out.find('class="citations"'):out.find('class="visual-links"')])
        visual = out[out.find('class="visual-links"'):]
        visual = visual[:visual.find('</nav>')]
        self.assertNotIn('cite-tip', visual)

    def test_generated_pages_keep_source_links_plain(self):
        from html.parser import HTMLParser

        class Guard(HTMLParser):
            def __init__(self):
                super().__init__()
                self.stack = []
                self.bad = []

            def handle_starttag(self, tag, attrs):
                data = dict(attrs)
                classes = (data.get('class') or '').split()
                self.stack.append((tag, classes))
                if 'cite-tip' in classes:
                    for name, cls in self.stack[:-1]:
                        if name in {'a', 'script', 'style', 'noscript'} or any(
                            item in cls for item in ('citations', 'source-citation', 'visual-links')
                        ):
                            self.bad.append((name, cls))
                            break

            def handle_endtag(self, tag):
                for i in range(len(self.stack) - 1, -1, -1):
                    if self.stack[i][0] == tag:
                        self.stack = self.stack[:i]
                        break

        pages = [builder.page(n) for n in range(1, 8)] + [builder.amounts_page()]
        for page in pages:
            self.assertIn('class="cite-tip"', page)
            self.assertIn('window.MSO_TIPS', page)
            self.assertIn('學習提示，不是法例原文。', page)
            guard = Guard()
            guard.feed(page)
            self.assertEqual(guard.bad, [])

    def test_generated_pages_disambiguate_section_25(self):
        import json
        def registry(page):
            marker = 'window.MSO_TIPS = '
            start = page.index(marker) + len(marker)
            return json.loads(page[start:page.index('</script>', start)].rstrip().rstrip(';'))

        part1 = registry(builder.page(1))
        combined = [rec for rec in part1.values() if rec['en_name'] == 'DTROP/OSCO section 25']
        self.assertTrue(combined)
        self.assertIn('dealing with proceeds', combined[0]['en'])

        part2 = registry(builder.page(2))
        amlo = [rec for rec in part2.values() if rec['en_name'] == 'AMLO section 25']
        self.assertTrue(amlo)
        self.assertIn('exemptions under the licensing regime', amlo[0]['en'])
        self.assertNotEqual(amlo[0]['en_name'], 'DTROP/OSCO section 25')


if __name__ == '__main__':
    unittest.main()
