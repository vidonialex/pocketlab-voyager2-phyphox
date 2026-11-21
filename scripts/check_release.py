#!/usr/bin/env python3
"""Read-only release checks (standard library); not a phone or calibration test."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit
from copy import deepcopy
import zlib
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


def check_experiment(path, version='v0.9.6', ir=False):
    selections = SELECTIONS + (['ir'] if ir else [])
    order = WIRE_ORDER[:-1] + ['ir', 'light'] if ir else WIRE_ORDER
    channels = dict(CHANNELS, ir=['ir']) if ir else CHANNELS
    units = dict(UNITS, ir='m') if ir else UNITS
    masks = dict(MASK_BITS, ir=0x1000000) if ir else MASK_BITS
    root = ET.parse(path).getroot()
    assert root.tag == 'phyphox' and root.attrib['locale'] == 'de', path
    assert version in root.findtext('title')
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
    assert len(toggles) == len(selections) and set(toggles) == {'sel_' + s for s in selections}
    formulas = {f.findtext('output'): f for f in root.findall('./analysis/formula')}
    for bits in itertools.product((0, 1), repeat=len(selections)):
        enabled = dict(zip(selections, bits))
        values = {'sel_' + s: enabled[s] for s in selections}
        mask = sum(masks[s] for s in selections if enabled[s])
        for byte in range(1, 5):
            assert formula_value(formulas[f'mask_{byte}'], values) == (mask >> (8*(byte-1))) & 255
        count = sum(len(channels[s]) for s in selections if enabled[s])
        values['num_channels'] = count
        assert formula_value(formulas['num_channels'], values) == count
        assert formula_value(formulas['expected_words'], values) == 3*count
        rank = 0
        for sensor in order:
            assert formula_value(formulas['rank_' + sensor], values) == rank
            values['rank_' + sensor] = rank
            if enabled[sensor]:
                for component, channel in enumerate(channels[sensor]):
                    for sample in range(3):
                        assert formula_value(formulas[f'pos_{channel}_{sample}'], values) == sample*count + rank + component
                rank += len(channels[sensor])
    init = {c.text: c.attrib.get('init') for c in containers}
    assert [int(init[f'stop_{i}']) for i in range(5)] == [110, 0, 0, 0, 0]
    assert int(init['mask_0']) == 110
    for sensor in selections:
        graph = next(g for g in root.findall('./views/view/graph') if g.get('visibility') == 'sel_' + sensor)
        assert graph.get('unitY') == units[sensor] and graph.get('unitX') == 's'
        assert graph.findall('input')[0].text == 't_' + sensor
    for c in channels['acc']:
        assert formulas[c].get('formula') == '9.80665*[1_]'
    for c in channels['gyro']:
        assert formulas[c].get('formula') == '0.017453292519943295*[1_]'
    assert formulas['pressure_hpa'].get('formula') == '[1_]/100'
    data = root.findall('./export/set/data')
    expected = {c for components in channels.values() for c in components} | {'t_' + s for s in selections}
    assert len(data) == (26 if ir else 24) and {d.text for d in data} == expected
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


def canonical(element):
    element = deepcopy(element)
    for node in element.iter():
        if node.text and not node.text.strip(): node.text = None
        if node.tail and not node.tail.strip(): node.tail = None
    return ET.tostring(element)


def check_candidate(root, source):
    # Metadata, information labels and export set title may change; all
    # measurement logic, graph settings and CSV data definitions must match.
    for tag in ('data-containers', 'input', 'output', 'analysis'):
        assert canonical(root.find(tag)) == canonical(source.find(tag)), tag
    views = [deepcopy(r.find('views')) for r in (root, source)]
    for view in views:
        for group in view.findall('view'):
            for info in group.findall('info'): group.remove(info)
    assert canonical(views[0]) == canonical(views[1])
    assert [canonical(e) for e in root.findall('./export/set/data')] == [canonical(e) for e in source.findall('./export/set/data')]
    rx = root.find('./input/bluetooth')
    assert rx.get('name') == 'PL Voyager 2' and rx.get('mode') == 'notification' and rx.get('mtu') == '247'
    write_uuid = '152fdea5-28a1-11ed-a261-0242ac120002'
    notify_uuid = '152fdea6-28a1-11ed-a261-0242ac120002'
    assert [e.text for e in rx.findall('config')] == ['23', '60 01', '78 03', '7C 00', '70 96 00 03 00', '6E 00 00 00 00']
    assert all(e.get('char') == write_uuid for e in rx.findall('config'))
    assert all(e.get('char') == notify_uuid for e in rx.findall('output'))
    floating = rx.find("output[@conversion='float32LittleEndian']")
    assert floating.text == 'rx_words' and floating.get('offset') == '6' and floating.get('repeating') == '4'
    for i in range(6):
        h = rx.find(f"output[@offset='{i}']")
        assert h.get('conversion') == 'uInt8' and h.get('length') == '1' and h.text == f'rx_h{i}'
    for trigger, prefix in [('apply_selection', 'mask'), ('all_stop', 'stop')]:
        outputs = root.findall(f"./output/bluetooth/input[@triggerId='{trigger}']")
        assert len(outputs) == 5
        assert [(e.get('char'), e.get('conversion'), e.get('offset'), e.text) for e in outputs] == [(write_uuid, 'uInt8', str(i), f'{prefix}_{i}') for i in range(5)]
    graph = root.find("./views/view/graph[@visibility='sel_ir']")
    assert {k: graph.get(k) for k in ['unitY','scaleMinY','scaleMaxY','minY','maxY']} == dict(unitY='m',scaleMinY='fixed',scaleMaxY='fixed',minY='0',maxY='6')
    assert [e.text for e in graph.findall('input')] == ['t_ir', 'ir']
    assert [e.text for e in root.findall('./export/set/data')[-2:]] == ['t_ir', 'ir']
    snapshots = [e for e in root.findall('./analysis/subrange') if any(i.text == 'rx_words' for i in e.findall('input'))]
    assert len(snapshots) == 1 and len(snapshots[0].findall('output')) == 8
    assert all(i.get('keep') == 'false' for i in snapshots[0].findall("input[@as='in']"))
    assert len([e for e in root.findall('./analysis/count') if any(i.text == 'packet_words' and i.get('keep', 'false') == 'false' for i in e.findall('input'))]) == 8


def check_zip(version, count, pattern, directory, manifest=None):
    experiment = (BASE / f'docs/experiments/Voyager2_{version}_DE.phyphox').read_bytes()
    with zipfile.ZipFile(BASE / f'docs/downloads/Voyager2_{version}_Offline_QR_DE.zip') as z:
        assert z.testzip() is None
        assert len([n for n in z.namelist() if n.startswith('QR_') and n.endswith('.png')]) == count
        for i in range(1, count+1):
            name = pattern.format(index=i)
            assert z.read(name) == (BASE / directory / name).read_bytes()
        assert z.read(f'Voyager2_{version}_DE.phyphox') == experiment
        payload = z.read(f'Voyager2_{version}_DE_offline.phyphox.zip')
        if manifest:
            size = manifest['offline_segment_payload_bytes_max']
            assert size > 0 and (len(payload) + size - 1) // size == count
            assert f'{zlib.crc32(payload):08x}' == manifest['offline_payload_crc32']
            assert hashlib.sha256(payload).hexdigest() == manifest['offline_payload_sha256']
        with zipfile.ZipFile(io.BytesIO(payload)) as inner:
            assert inner.testzip() is None
            assert inner.read(f'Voyager2_{version}_DE.phyphox') == experiment


def main():
    m = json.loads((BASE / 'release_manifest.json').read_text(encoding='utf-8'))
    assert m['version'] == 'v0.9.7' and m['status'] == 'unpublished-release-candidate'
    count = m['offline_qr_count']
    assert 1 <= count <= 255
    for rel, expected in m['hashes'].items():
        dest = BASE / rel
        assert dest.is_file(), f'Missing file: {rel}'
        assert hashlib.sha256(dest.read_bytes()).hexdigest() == expected, f'SHA256 mismatch: {rel}'
        if dest.suffix == '.phyphox': assert ET.parse(dest).getroot().tag == 'phyphox'
    # Retain the existing complete nine-sensor checks for the frozen release.
    for lang in ('DE', 'DE_EN'):
        check_experiment(BASE / f'docs/experiments/Voyager2_v096_{lang}.phyphox')
    roots = [check_experiment(BASE / f'docs/experiments/Voyager2_v097_{lang}.phyphox', 'v0.9.7', True) for lang in ('DE','DE_EN')]
    for root, lang in zip(roots, ('DE','DE_EN')):
        source = ET.parse(BASE / f'docs/experiments/tests/Voyager2_Sensorwahl_10_IR_057_Test_{lang}.phyphox').getroot()
        check_candidate(root, source)
        guidance = root.findtext('description') + ' '.join(e.get('label', '') for e in root.findall('./views/view/info'))
        assert 'empfohlen' in guidance.lower() and 'vor ▶' in guidance
        selection_hint = root.find("./views/view[@label='Sensorauswahl']/info").get('label')
        assert selection_hint == 'Empfohlen: Sensoren wählen → Aufzeichnung mit ▶ (oben rechts) starten → „Messdaten STARTEN“.'
        assert '\n' not in selection_hint and 'nach dem Pausieren und Wiederaufnehmen jedoch nicht zuverlässig' in guidance
        assert not any(text in guidance for text in ('setzt eine laufende phyphox-Aufzeichnung voraus', 'nur bei laufender phyphox-Aufzeichnung', 'benötigt eine laufende phyphox-Aufzeichnung', 'Erst bei laufender phyphox-Aufzeichnung'))
    for tag in ('data-containers','input','output','analysis','views','export'):
        assert canonical(roots[0].find(tag)) == canonical(roots[1].find(tag)), tag
    assert roots[0].find('translations') is None
    english = roots[1].find('./translations/translation')
    assert english.get('locale') == 'en' and english.findtext('title') and english.findtext('description')
    strings = english.findall('string')
    translations = {e.get('original'): e.text for e in strings}
    assert len(strings) == len(translations), 'Duplicate translation key'
    for info in roots[1].findall('./views/view/info'):
        assert translations.get(info.get('label')), info.get('label')
    for node in roots[1].findall('./views/view') + roots[1].findall('./views/view/toggle') + roots[1].findall('./views/view/button') + roots[1].findall('./views/view/graph') + roots[1].findall('./export/set/data'):
        label = node.get('label') or node.get('name')
        assert translations.get(label), label
    assert translations['IR-Entfernung'] == 'IR Rangefinder'
    assert translations[roots[1].find('./export/set').get('name')]
    english_guidance = english.findtext('description') + ' '.join(translations.values())
    assert 'before ▶' in english_guidance and 'recommend' in english_guidance.lower()
    hint_translation = translations[roots[1].find("./views/view[@label='Sensorauswahl']/info").get('label')]
    assert hint_translation == 'Recommended: Select sensors → Start recording with ▶ (top right) → START DATA.'
    assert '\n' not in hint_translation and translations['Messdaten STARTEN'] in hint_translation
    assert 'was not reliable after pausing and resuming' in english_guidance
    assert not any(text in english_guidance for text in ('requires an active phyphox recording', 'requires recording in phyphox', 'requires phyphox recording', 'only while phyphox recording is running', 'Only when phyphox recording is running'))
    check_zip('v096', 8, 'QR_{index:02d}_von_8.png', 'docs/qr/offline/v096')
    check_zip('v097', count, m['offline_qr_pattern'], m['offline_qr_dir'], m)
    html = (BASE / 'docs/index.html').read_text(encoding='utf-8')
    parser = SiteLinks(); parser.feed(html)
    for ref in parser.refs:
        url = urlsplit(ref)
        if url.scheme or url.netloc: continue
        if url.path: assert (BASE / 'docs' / unquote(url.path)).is_file(), ref
        if url.fragment: assert url.fragment in parser.ids, ref
    for marker in ('Voyager2_v097_DE.phyphox','Voyager2_v097_DE_EN.phyphox','Voyager2_v097_Offline_QR_DE.zip','qr/online_v097.png',f'qr/offline/v097/QR_01_von_{count}.png',f'let i=1;const N={count};','`qr/offline/v097/QR_${nr}_von_${N}.png`','Voyager2_v095_DE.phyphox','Voyager2_v096_DE.phyphox'):
        assert marker in html, marker
    for md in [BASE/'README.md', *sorted((BASE/'docs').glob('*.md'))]:
        for ref in re.findall(r'\]\(([^)]+)\)', md.read_text(encoding='utf-8')):
            url = urlsplit(ref)
            if not url.scheme and url.path: assert (md.parent / unquote(url.path)).is_file(), (md, ref)
    assert m['online_qr_url'] == m['intended_site'] + 'experiments/Voyager2_v097_DE_EN.phyphox'
    print(f"OK: {len(m['hashes'])} SHA256 checks; frozen v0.9.6 (512 selections/language); v0.9.7 (1024 selections/language), 16 channels / 26 CSV columns; unchanged measurement XML; BLE, translations, axes, ZIP CRC32 and local links.")
    print('QR decoding and synthetic batch/regression checks are separate checks. Previous candidate passed Android approval tests on 2026-11-21; re-import of text-corrected files/new QR codes remains pending, as do online QR scan and systematic long-duration/metrological tests.')


if __name__ == '__main__':
    main()
