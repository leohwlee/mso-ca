"""Archived files remain evidence only while their exact bytes are verified."""
import hashlib
import json
import pathlib
import sys
import tempfile
import unittest
from unittest.mock import patch
import zipfile

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'bank/audit'))
import state


class ArchiveEvidenceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = pathlib.Path(self.temp.name)
        self.audit = self.root / 'bank/audit'
        (self.audit / 'maintenance').mkdir(parents=True)
        self.original = b'Original reviewed source\n'
        self.source_hash = hashlib.sha256(self.original).hexdigest()
        with zipfile.ZipFile(self.root / 'history.zip', 'w') as archive:
            archive.writestr('revision/ci.py', self.original)
        self.record = {
            'status': 'verified', 'archive': 'history.zip',
            'archive_sha256': hashlib.sha256((self.root / 'history.zip').read_bytes()).hexdigest(),
            'archive_preserved': {'revision/ci.py': {'sha256': self.source_hash}},
            'documentation_updates': {},
        }

    def verify(self):
        (self.audit / 'maintenance/record.json').write_text(json.dumps(self.record), encoding='utf8')
        with patch.object(state, 'ROOT', self.root), patch.object(state, 'HERE', self.audit):
            return state.maintenance_followups()

    def test_verified_archive_proves_removed_source(self):
        self.assertIn(('revision/ci.py', self.source_hash), self.verify())
        self.assertFalse((self.root / 'revision/ci.py').exists())

    def test_changed_archive_is_rejected(self):
        with zipfile.ZipFile(self.root / 'history.zip', 'w') as archive:
            archive.writestr('revision/ci.py', b'Changed after review\n')
        with self.assertRaisesRegex(AssertionError, 'Snapshot changed'):
            self.verify()

    def test_even_rehashed_archive_cannot_prove_wrong_original(self):
        with zipfile.ZipFile(self.root / 'history.zip', 'w') as archive:
            archive.writestr('revision/ci.py', b'Changed after review\n')
        self.record['archive_sha256'] = hashlib.sha256((self.root / 'history.zip').read_bytes()).hexdigest()
        with self.assertRaisesRegex(AssertionError, 'revision/ci.py'):
            self.verify()


if __name__ == '__main__':
    unittest.main()
