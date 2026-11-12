#!/usr/bin/env python3
"""Check release integrity without changing any file (standard library only)."""
from pathlib import Path
from zipfile import ZipFile
import hashlib, json, xml.etree.ElementTree as ET
base=Path(__file__).resolve().parent.parent
m=json.loads((base/'release_manifest.json').read_text(encoding='utf-8'))
for rel, expected in m['hashes'].items():
    p=base/rel
    actual=hashlib.sha256(p.read_bytes()).hexdigest()
    assert actual==expected, f'Changed file: {rel}'
    if p.suffix=='.phyphox':
        tree=ET.parse(p)
        assert tree.getroot().tag.endswith('phyphox')
with ZipFile(base/'docs/downloads/Voyager2_v095_Offline_QR_DE.zip') as z:
    assert z.testzip() is None
for i in range(1,8):
    assert (base/f'docs/qr/offline/QR_{i:02d}_von_7.png').exists()
html=(base/'docs/index.html').read_text(encoding='utf-8')
assert 'experiments/Voyager2_v095_DE_EN.phyphox' in html
assert 'experiments/Voyager2_v095_DE.phyphox' in html
assert (base/'docs/qr/online.png').exists()
print('OK: v0.9.5 release files, hashes, XML, ZIP and website paths verified.')
print('Note: This is not a live GitHub Pages/phone QR scan test.')
