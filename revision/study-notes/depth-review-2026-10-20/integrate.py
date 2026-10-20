"""Consolidate reviewed additions in the authoritative manuscripts."""
from pathlib import Path
exec(compile((Path(__file__).with_name('edit_guideline.py')).read_text(encoding='utf-8').split('\ndef ml(s):')[0],__file__,'exec'))
from licensing_depth_additions import ADDITIONS as A
from statutory_depth_additions import ADDITIONS as B
changes={}
for collection in (A,B):
    for n,sections in collection.items():
        for sid,blocks in sections.items():
            changes.setdefault(n,{}).setdefault(sid,[]).extend(blocks)
for n,sections in changes.items():
    write_sections(n,{sid:(lambda s, blocks=blocks:s['blocks'].extend(blocks)) for sid,blocks in sections.items()})
# Preserve the collaboration inputs as evidence, rather than adding runtime layers.
for name in ('licensing_depth_additions.py','statutory_depth_additions.py'):
    (HERE/name).rename(Path(__file__).with_name(name))
