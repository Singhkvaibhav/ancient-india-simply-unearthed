"""Build an episode from a compact spec. ep.py = `from engine.epkit import *` + SPEC dict + `build(SPEC, globals())`.
Narration for the quiz, inscription and gallery beats is generated from the data so cue phrases always match."""
import sys, os
sys.path.insert(0, os.path.abspath('../..'))
from engine import anc, plan

# ---- shorthand for frieze items ----
def fg(dx, name=None, crown=0, col='terra', s=1.0, dy=0): return ('fig', dx, dy, s, name, {'crown': bool(crown), 'col': col})
def ar(dx, art, label=None, s=1.3, dy=0): return ('art:' + art, dx, dy, s, label)
def hs(dx, s=1.0): return ('house', dx, 0, s)
def wl(dx, s=.9): return ('wall', dx, 0, s)
def tr(dx, s=1.0): return ('tree', dx, 0, s)
def hl(dx, s=1.0): return ('hill', dx, 0, s)
def sn(dx, s=.9): return ('sun', dx, 0, s)
def rv(w=760, dy=-60): return ('river', 0, dy, w)
def tx(dy, s, size=34, dx=0): return ('text', dx, dy, s, size)
def sc(cue, title, *items): return (cue, dict(title=title, items=list(items)))

def build(S, g):
    n = S['ep']; p = plan.BY_EP[n]; art = p[4]
    nxt = plan.BY_EP[n + 1][1] if n < 44 else None
    anc.PERIOD = tuple(S.get('period', p[3]))
    scenes = [x[1] for x in S['scenes']]; fcues = [0] + [x[0] for x in S['scenes'][1:]]
    tip = S['tip']; tip_say = ' '.join(l.rstrip('.,') + '.' for l in tip)
    q = S['quiz']; N = {}
    N['dig'] = S['dig']; N['sources'] = S['sources']; N['frieze'] = S['frieze']; N['plaque'] = S['plaque_say']
    N['inscription'] = f"Carve this tip into memory. {tip_say} {S['tip_close']}"
    qs = 'Dig Quiz. Pause and name it. [[1]] '
    for i, (a, qq, ans) in enumerate(q):
        qs += f"Number {['one', 'two', 'three'][i]}. {qq} [[3]] The answer: {ans}. [[1]] "
    qs += f"Now one line for Mains. {S['mains']}"
    N['quiz'] = qs
    facts = S['facts']
    N['gallery'] = f"{S['exhibit_say']} Three facts to take away. " + ' '.join(f.rstrip('.') + '.' for f in facts) + (f" Next gallery: {nxt}." if nxt else '')
    pl = S['plaque']
    if pl['kind'] == 'rename':
        plaque = anc.plaque(old=pl['old'], new=pl['new'], cue_b=pl['cue_b'], sub=pl.get('sub'))
    else:
        plaque = anc.plaque(a_txt=pl['a'], b_txt=pl['b'], heading=pl.get('heading'), cue_a=pl.get('cue_a'), cue_b=pl['cue_b'])
    S_ = anc.scene
    quiz_cards = [(a, f"Number {['one', 'two', 'three'][i]}", f"The answer: {ans}", ans[0].upper() + ans[1:]) for i, (a, qq, ans) in enumerate(q)]
    BEATS = [
        ('dig', N['dig'], S_('trench', anc.dig(art, S['dig_q'], S['tags'], q_at=S['q_at']))),
        ('sources', N['sources'], S_('stone', anc.sources(S['lit'], S.get('notes', {}), S['lit_cues']))),
        ('frieze', N['frieze'], S_('stone', anc.frieze(scenes, fcues))),
        ('plaque', N['plaque'], S_('stone', plaque)),
        ('inscription', N['inscription'], S_('stone', anc.inscription(tip))),
        ('quiz', N['quiz'], S_('stone', anc.quiz(quiz_cards, 'One line: ' + S['mains'], 'Now one line for Mains'))),
        ('gallery', N['gallery'], S_('museum', anc.gallery(n, p[5], facts, nxt, 1.5, [f.rstrip('.')[:22] for f in facts], ('Next gallery' if nxt else None)))),
    ]
    g.update(EP=n, TITLE=p[1], NAME=p[2], TIP_LINES=tip, PLACE_AT=1.5, BEATS=BEATS, CAPTIONS={}, EXTRA=S.get('extra', {}))
