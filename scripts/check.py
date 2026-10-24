"""Run every repository check in order and stop at the first failure.

    python scripts/check.py          # what CI and the release workflow run
    python scripts/check.py --list   # print the commands without running them

The practice app is exported first because the Python link tests and the bundle
read dist/mso-ca.html; the bundle is built and checked last. Python commands run
with this interpreter and -X utf8, so the Chinese output also works on Windows.
"""
import subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PY = [sys.executable, '-X', 'utf8']
CHECKS = ['docs/build_catalog.py', 'bank/audit/active_scope.py', 'bank/audit/render_active_scope.py',
          'bank/audit/report.py', 'bank/audit/terms_report.py', 'bank/audit/p1_report.py',
          'bank/audit/remaining_report.py', 'revision/study-notes/build.py', 'revision/study-notes/gap_check.py']
COMMANDS = [
    ['go', 'run', '.', '-export-html', 'dist/mso-ca.html'],
    ['go', 'vet', './...'],
    ['go', 'test', './...'],
    ['node', '--test', *sorted(p.relative_to(ROOT).as_posix() for p in (ROOT / 'tests').glob('*.test.cjs'))],
    [*PY, '-m', 'unittest', 'discover', '-s', 'tests', '-p', '*_test.py'],
    *([*PY, script, '--check'] for script in CHECKS),
    [*PY, 'scripts/build_study_bundle.py'],
    [*PY, 'scripts/build_study_bundle.py', '--check'],
]

def main():
    run = '--list' not in sys.argv[1:]
    if run:
        (ROOT / 'dist').mkdir(exist_ok=True)
    for command in COMMANDS:
        print('$', *('python' if part == sys.executable else part for part in command), flush=True)
        if run and subprocess.run(command, cwd=ROOT).returncode:
            sys.exit(f'failed: {" ".join(command)}')
    if run:
        print(f'All {len(COMMANDS)} commands passed.')

if __name__ == '__main__':
    main()
