#!/usr/bin/env python3
"""Layout/timing audit of every episode spec: text that overflows, items that overlap on the frieze, cue order, short scenes.
usage: python3 tools/audit.py [NN ...]"""
import os, sys, re, json
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, ROOT)
import cairo
from engine import core, anc, plan
from engine.core import font
S = cairo.ImageSurface(cairo.FORMAT_ARGB32, 10, 10); cx = cairo.Context(S)
def tw(s, size, bold=False, serif=False):
    font(cx, size, bold, serif); return cx.text_extents(s).x_advance
def lines(s, size, maxw, bold=False, serif=True): return len(anc.wrap_s(cx, s, size, maxw, bold, serif))
ART = dict(handaxe=55, polishedaxe=50, pot=120, seal=75, bead=105, palmleaf=110, tablet=70, coin=78, stupa=100, pillar=45, bullcap=96, wheel=85, lotus=70, footprints=90, bodhitree=90, throne=90, sword=44, plough=96, ship=100, elephant=90, temple=80, gopuram=75, fort=110, scales=100, lamp=100, crown=90, manuscript=96, sphere=118, helmet=82, chalice=60, gate=100, shelter=110, sickle=100, quern=110)
def frieze_issues(scenes):
    out = []
    for si, sc in enumerate(scenes):
        boxes = []
        for it in sc['items']:
            kind, dx, dy, s = it[0], it[1], it[2], it[3]; rest = it[4:]
            if kind == 'fig':
                lab = rest[0] if rest else None; w = 60 * s
                boxes.append((dx - 30 * s, dx + 30 * s, dy - 160 * s, dy, 'fig'))
                if lab: lw = tw(lab, 21, True) + 28; boxes.append((dx - lw / 2, dx + lw / 2, dy + 14, dy + 48, 'name:' + lab))
            elif kind.startswith('art:'):
                a = kind[4:]; hw = ART.get(a, 100) * s
                boxes.append((dx - hw, dx + hw, dy - 200 * s, dy, 'art:' + a))
                if rest and rest[0]: lw = tw(rest[0], 21, True) + 28; boxes.append((dx - lw / 2, dx + lw / 2, dy + 14, dy + 48, 'label:' + rest[0]))
            elif kind == 'text':
                size = rest[0] if rest else 30; w = tw(it[3], size, True, True); boxes.append((dx - w / 2, dx + w / 2, dy - size, dy, 'text:' + it[3][:20]))
            elif kind == 'house': boxes.append((dx - 86 * s, dx + 86 * s, dy - 130 * s, dy, 'house'))
            elif kind == 'wall': boxes.append((dx - 150 * s, dx + 150 * s, dy - 128 * s, dy, 'wall'))
            elif kind == 'tree': boxes.append((dx - 70 * s, dx + 70 * s, dy - 190 * s, dy, 'tree'))
        for b in boxes:
            if b[0] < -500 or b[1] > 500: out.append(f"scene {si+1} '{sc['title']}': {b[4]} outside panel ({b[0]:.0f}..{b[1]:.0f})")
        for i in range(len(boxes)):
            for j in range(i + 1, len(boxes)):
                a, b = boxes[i], boxes[j]
                if min(a[1], b[1]) - max(a[0], b[0]) > 6 and min(a[3], b[3]) - max(a[2], b[2]) > 6:
                    ta, tb = a[4].split(':')[0], b[4].split(':')[0]
                    if {ta, tb} <= {'tree', 'house', 'wall', 'art', 'fig'} and not ({ta, tb} & {'text', 'name', 'label'}) and False: continue
                    out.append(f"scene {si+1} '{sc['title']}': {a[4]} overlaps {b[4]}")
    return out
def audit(n):
    nn = f'{n:02d}'; d = os.path.join(ROOT, 'episodes', f'ep{nn}'); os.chdir(d)
    g = {}; src = open('ep.py').read()
    cap = {}
    import engine.epkit as ek; orig = ek.build
    def cb(S_, g_): cap['S'] = S_; orig(S_, g_)
    ek.build = cb
    exec(compile(src, 'ep.py', 'exec'), g); ek.build = orig
    S_ = cap['S']; iss = []
    for l in S_['tip']:
        w = tw(l, 54, True, True)
        if 1120 / w < .7: iss.append(f"inscription line too wide ({w:.0f}px): {l}")
    for f in S_.get('facts', []):
        if lines(f, 28, 650, False, True) > 2: iss.append(f"label fact wraps to >2 lines: {f}")
    pl = S_['plaque']
    if pl['kind'] == 'disagree':
        for t, b in (pl['a'], pl['b']):
            if lines(b, 30, 720) > 7: iss.append(f"plaque body >7 lines: {t}")
            if tw(t, 40, True, True) > 760: iss.append(f"plaque title too wide: {t}")
        if tw(pl.get('heading', ''), 56, True, True) > 1700: iss.append('plaque heading too wide')
    else:
        for lab in (pl['old'], pl['new']):
            if 600 / tw(lab, 54, True, True) < .65: iss.append(f"rename plaque label too wide ({tw(lab,54,True,True):.0f}): {lab}")
        if pl.get('sub') and tw(pl['sub'], 32, False, True) > 1700: iss.append('plaque sub too wide')
    if lines(S_['dig_q'], 52, 1500, True) > 2: iss.append('dig question >2 lines')
    for t in S_['tags']:
        if 332 / tw(t, 24, True) < .72: iss.append(f"dig tag too wide: {t}")
    for a, q, ans in S_['quiz']:
        if lines(ans[0].upper() + ans[1:], 44, 520, True) > 2: iss.append(f"quiz answer >2 lines: {ans}")
    if lines('One line: ' + S_['mains'], 40, 1380, True) > 3: iss.append('mains >3 lines')
    from engine import museum
    for a, q, ans in S_['quiz']:
        if a not in museum.ART: iss.append(f'quiz art not in ART (falls back to pot): {a}')
    if plan.BY_EP[n][4] not in museum.ART: iss.append('exhibit art missing: ' + plan.BY_EP[n][4])
    for sc_ in [x[1] for x in S_['scenes']]:
        for it in sc_['items']:
            if it[0].startswith('art:') and it[0][4:] not in museum.ART: iss.append(f'frieze art missing: {it[0]}')
    iss += frieze_issues([x[1] for x in S_['scenes']])
    # cue ordering
    B = {k: t for k, t, _ in g['BEATS']}
    pos = []
    for c in [x[0] for x in S_['scenes'][1:]]:
        i = B['frieze'].find(c)
        if i < 0: iss.append(f"frieze cue not found: {c}")
        pos.append(i)
    if pos != sorted(pos): iss.append(f"frieze cues out of narration order: {pos}")
    return iss
if __name__ == '__main__':
    eps = [int(a) for a in sys.argv[1:]] or [n for n in range(1, 45)]
    bad = 0
    for n in eps:
        try: r = audit(n)
        except Exception as e: r = [f'AUDIT ERROR {e!r}']
        if r: bad += 1; print(f'--- EP{n:02d}'); [print('  ', x) for x in r]
    print('episodes with issues:', bad)
