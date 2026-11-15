#!/usr/bin/env python3
"""Read-only release checks (standard library); not a phone or calibration test."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit
import ast
import hashlib
import io
import itertools
import json
import re
import xml.etree.ElementTree as ET
import zipfile

BASE = Path(__file__).resolve().parent.parent
SELECTIONS = ['acc', 'gyro', 'mag', 'temp', 'press', 'hum', 'heat', 'light', 'probe']
WIRE_ORDER = ['acc', 'gyro', 'mag', 'probe', 'temp', 'press', 'hum', 'heat', 'light']
CHANNELS = {'acc': ['ax', 'ay', 'az'], 'gyro': ['wx', 'wy', 'wz'], 'mag': ['bx', 'by', 'bz'],
            'probe': ['probe'], 'temp': ['temp'], 'press': ['press'], 'hum': ['humidity'],
            'heat': ['heat'], 'light': ['light']}
UNITS = dict(zip(SELECTIONS, ['m/s²', 'rad/s', 'µT', '°C', 'hPa', '%', '°C', 'lx', '°C']))
MASK_BITS = {'acc': 0x70, 'gyro': 0x380, 'mag': 0x1c00, 'probe': 0x20000,
             'temp': 0x40000, 'press': 0x80000, 'hum': 0x100000, 'heat': 0x800000, 'light': 0x4000000}


def formula_value(module, values):
    """Evaluate only arithmetic used by masks, ranks and sample positions."""
    inputs = module.findall('input')
    expression = re.sub(r'\[(\d+)\]', lambda m: repr(values[inputs[int(m[1])-1].text]), module.attrib['formula'])
    tree = ast.parse(expression, mode='eval')
    assert all(isinstance(n, (ast.Expression, ast.BinOp, ast.Constant, ast.Add,
                              ast.Sub, ast.Mult, ast.Div, ast.Load)) for n in ast.walk(tree))
    return eval(compile(tree, '<release-formula>', 'eval'), {'__builtins__': {}}, {})


def check_experiment(path):
    root = ET.parse(path).getroot()
    assert root.tag == 'phyphox' and root.attrib['locale'] == 'de', path
    assert 'v0.9.6' in root.findtext('title')
    containers = root.findall('./data-containers/container')
    names = [c.text for c in containers]
    assert len(names) == len(set(names)), 'Duplicate data containers'
    known = set(names)
    for element in root.findall('./analysis//input') + root.findall('./analysis//output') + root.findall('./views//input') + root.findall('./views//output'):
        if element.get('type', 'buffer') == 'buffer':
            assert element.text in known, (path, element.text)
    for element in root.findall('./views//*'):
        if 'visibility' in element.attrib:
            assert element.attrib['visibility'] in known
    toggles = [t.findtext('output') for t in root.findall('./views/view/toggle') if (t.findtext('output') or '').startswith('sel_')]
    assert len(toggles) == 9 and set(toggles) == {'sel_' + s for s in SELECTIONS}
    formulas = {f.findtext('output'): f for f in root.findall('./analysis/formula')}
    for bits in itertools.product((0, 1), repeat=9):
        enabled = dict(zip(SELECTIONS, bits))
        values = {'sel_' + s: enabled[s] for s in SELECTIONS}
        mask = sum(MASK_BITS[s] for s in SELECTIONS if enabled[s])
        for byte in range(1, 5):
            assert formula_value(formulas[f'mask_{byte}'], values) == (mask >> (8*(byte-1))) & 255
        count = sum(len(CHANNELS[s]) for s in SELECTIONS if enabled[s])
        values['num_channels'] = count
        assert formula_value(formulas['num_channels'], values) == count
        assert formula_value(formulas['expected_words'], values) == 3*count
        rank = 0
        for sensor in WIRE_ORDER:
            assert formula_value(formulas['rank_' + sensor], values) == rank
            values['rank_' + sensor] = rank
            if enabled[sensor]:
                for component, channel in enumerate(CHANNELS[sensor]):
                    for sample in range(3):
                        assert formula_value(formulas[f'pos_{channel}_{sample}'], values) == sample*count + rank + component
                rank += len(CHANNELS[sensor])
    init = {c.text: c.attrib.get('init') for c in containers}
    assert [int(init[f'stop_{i}']) for i in range(5)] == [110, 0, 0, 0, 0]
    assert int(init['mask_0']) == 110
    for sensor in SELECTIONS:
        graph = next(g for g in root.findall('./views/view/graph') if g.get('visibility') == 'sel_' + sensor)
        assert graph.get('unitY') == UNITS[sensor] and graph.get('unitX') == 's'
        assert graph.findall('input')[0].text == 't_' + sensor
    for c in CHANNELS['acc']:
        assert formulas[c].get('formula') == '9.80665*[1_]'
    for c in CHANNELS['gyro']:
        assert formulas[c].get('formula') == '0.017453292519943295*[1_]'
    assert formulas['pressure_hpa'].get('formula') == '[1_]/100'
    data = root.findall('./export/set/data')
    expected = {c for channels in CHANNELS.values() for c in channels} | {'t_' + s for s in SELECTIONS}
    assert len(data) == 24 and {d.text for d in data} == expected
    assert all(d.text in known for d in data)
    assert '(Pa)' in next(d.get('name') for d in data if d.text == 'press')
    assert '(°C)' in next(d.get('name') for d in data if d.text == 'probe')
    help_text = ' '.join(e.get('label', '') for e in root.findall('./views/view/info'))
    assert 'Referenztemperatur' in help_text and 'keine Kalibrierung' in help_text
    assert 'keine geräteinternen Zeitstempel' in root.findtext('description')
    return root


class SiteLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.refs, self.ids = [], set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.ids.add(attrs.get('id'))
        self.refs.extend(attrs[k] for k in ('href', 'src') if k in attrs)


def main():
    m = json.loads((BASE / 'release_manifest.json').read_text(encoding='utf-8'))
    assert m['version'] == 'v0.9.6' and m['offline_qr_count'] == 8
    for rel, expected in m['hashes'].items():
        dest = BASE / rel
        assert dest.is_file(), f'Missing file: {rel}'
        assert hashlib.sha256(dest.read_bytes()).hexdigest() == expected, f'SHA256 mismatch: {rel}'
        if dest.suffix == '.phyphox':
            assert ET.parse(dest).getroot().tag == 'phyphox'
    de, bilingual = [check_experiment(BASE / f'docs/experiments/Voyager2_v096_{lang}.phyphox') for lang in ('DE', 'DE_EN')]
    for tag in ('data-containers', 'input', 'output', 'analysis', 'views', 'export'):
        assert ET.tostring(de.find(tag)) == ET.tostring(bilingual.find(tag)), tag
    assert de.find('translations') is None
    assert bilingual.find('./translations/translation').get('locale') == 'en'
    translations = {s.get('original'): s.text for s in bilingual.findall('./translations/translation/string')}
    assert translations['Externe Temperatursonde'] == 'External Temperature Probe'
    with zipfile.ZipFile(BASE / 'docs/downloads/Voyager2_v096_Offline_QR_DE.zip') as z:
        assert z.testzip() is None
        assert len([n for n in z.namelist() if n.startswith('QR_') and n.endswith('.png')]) == 8
        for i in range(1, 9):
            name = m['offline_qr_pattern'].format(index=i)
            assert z.read(name) == (BASE / m['offline_qr_dir'] / name).read_bytes()
        experiment = (BASE / 'docs/experiments/Voyager2_v096_DE.phyphox').read_bytes()
        assert z.read('Voyager2_v096_DE.phyphox') == experiment
        with zipfile.ZipFile(io.BytesIO(z.read('Voyager2_v096_DE_offline.phyphox.zip'))) as inner:
            assert inner.testzip() is None
            assert inner.read('Voyager2_v096_DE.phyphox') == experiment
    html = (BASE / 'docs/index.html').read_text(encoding='utf-8')
    parser = SiteLinks()
    parser.feed(html)
    for ref in parser.refs:
        url = urlsplit(ref)
        if url.scheme or url.netloc:
            continue
        if url.path:
            assert (BASE / 'docs' / unquote(url.path)).is_file(), ref
        if url.fragment:
            assert url.fragment in parser.ids, ref
    for marker in ('Voyager2_v096_DE.phyphox', 'Voyager2_v096_DE_EN.phyphox', 'Voyager2_v096_Offline_QR_DE.zip', 'qr/online_v096.png', 'qr/offline/v096/QR_01_von_8.png', 'let i=1;const N=8;', '`qr/offline/v096/QR_${nr}_von_${N}.png`'):
        assert marker in html, marker
    readme = (BASE / 'README.md').read_text(encoding='utf-8')
    for ref in re.findall(r'\]\(([^)]+)\)', readme):
        if not urlsplit(ref).scheme:
            assert (BASE / unquote(ref)).is_file(), ref
    assert m['online_qr_url'] == m['intended_site'] + 'experiments/Voyager2_v096_DE_EN.phyphox'
    print(f"OK: {len(m['hashes'])} SHA256 checks, XML, 512 selections per language, 15 channels / 24 CSV columns, units, ZIPs and local links.")
    print('Not checked here: QR decoding, Android imports, live BLE behavior, long-duration stability and metrological accuracy.')


if __name__ == '__main__':
    main()
