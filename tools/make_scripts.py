#!/usr/bin/env python3
"""Write scripts/unitN_scripts.md from the episode specs: header line + Time | Segment | Visual | Narration table per episode."""
import os, re, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, ROOT)
from engine import plan
UNITS = [(1, 6, 'Prehistory and the Indus'), (7, 9, 'The Vedic age'), (10, 15, 'Religions and the Mahajanapadas'), (16, 21, 'The Mauryas'), (22, 27, 'After the Mauryas'), (28, 33, 'The Guptas'), (34, 38, 'Harsha and the South'), (39, 44, 'Early medieval India')]
VIS = dict(dig='DIG: brush reveals the artefact', sources='SOURCES: evidence tags light up', frieze='FRIEZE: carved panel pans scene by scene', plaque='PLAQUE', inscription='INSCRIPTION: tip chiselled in', quiz='QUIZ: three artefact cards, then Mains', gallery='GALLERY: exhibit placed, label', walk='GALLERY: slow walk past every case')
SEG = dict(dig='The Dig', sources='How do we know?', frieze='The Frieze', plaque='The Plaque', inscription='Inscription', quiz='Dig Quiz', gallery='The Gallery', walk='The Gallery')
def load(n):
    nn = f'{n:02d}'; d = os.path.join(ROOT, 'episodes', f'ep{nn}')
    code = ("import sys,json;sys.path.insert(0,'../..');sys.argv=['x'];exec(open('ep.py').read());"
            "print(json.dumps(dict(tip=SPEC['tip'],lit=SPEC['lit'],plaque=SPEC['plaque'],facts=SPEC.get('facts',[]),beats=[(k,t) for k,t,_ in BEATS],period=list(__import__('engine.anc',fromlist=['x']).PERIOD))))")
    import json
    return json.loads(subprocess.run(['python3', '-c', code], cwd=d, capture_output=True, text=True).stdout)
for i, (a, b, name) in enumerate(UNITS, 1):
    out = [f'# Unit {i}: {name} (Episodes {a} to {b})\n', 'Dates: "about" or "c.", BCE/CE, most common textbook date. Fact check notes follow each episode.\n']
    for n in range(a, b + 1):
        p = plan.BY_EP[n]
        try: e = load(n)
        except Exception as ex: out.append(f'## Episode {n}: {p[1]}\n(missing)\n'); continue
        pl = e['plaque']; plq = (f"Old name, new name: {pl['old']} → {pl['new']}" if pl['kind'] == 'rename' else 'Scholars disagree: ' + pl['a'][0] + ' / ' + pl['b'][0])
        out.append(f"## Episode {n}: {p[1]}\n")
        out.append(f"**Inscription tip:** {' '.join(e['tip'])} · **Sources lit:** {', '.join(e['lit'])} · **Timeline ribbon:** {tuple(e['period'])} · **Plaque:** {plq} · **Exhibit:** {p[5]} · **Label facts:** {'; '.join(e['facts']) or 'the whole gallery'}\n")
        out.append('| Segment | Visual | Narration |\n| --- | --- | --- |')
        for k, t in e['beats']:
            out.append(f"| {SEG[k]} | {VIS[k]} | {re.sub(r'\[\[[0-9.]+\]\]\s*', '', t).replace('|', '/')} |")
        out.append('\nFact check: dates are the most common textbook versions; where sources differ the narration says "about", "c." or names the alternative.\n')
    open(os.path.join(ROOT, 'scripts', f'unit{i}_scripts.md'), 'w').write('\n'.join(out) + '\n')
print('ok')
