"""Create a keyless, text-bound bilingual review packet from a question patch.

python bank/review_packet.py patch.json packet.json
Reviewers read the packet and source files, never the patch or answer bank.
"""
import json
import pathlib
import sys
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent/'audit'))
from active_scope import review_text, text_hash

if __name__=='__main__':
    if len(sys.argv)!=3:
        raise SystemExit(__doc__)
    items=json.loads(pathlib.Path(sys.argv[1]).read_text(encoding='utf8'))
    packet={'instructions':'Independently judge every statement against the cited local source in each language. Do not read keys, notes, patches or the bank. Return id, verdicts, tc_verdicts (T/F arrays), quotes (one deciding source excerpt per statement), doubts and tc_mismatch (empty strings when none). A language=en quote for doc24 is an English original supporting a clearly labelled Chinese study translation.',
            'items':[review_text(q) for q in items],
            'text_sha256':{q['id']:text_hash(q) for q in items}}
    target=pathlib.Path(sys.argv[2]); target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(json.dumps(packet,ensure_ascii=False,indent=1)+'\n',encoding='utf8',newline='\n')
    print(f'{len(items)} keyless items -> {target}')
