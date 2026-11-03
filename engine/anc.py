"""Scene templates for Ancient India: DIG, SOURCES, FRIEZE, PLAQUE, INSCRIPTION, QUIZ, GALLERY + timeline ribbon.
Layers are f(ctx, t, D); scene() stacks them on a background. Time args accept seconds or a narration phrase."""
import math, random
from engine.core import *
from engine.stone import *
from engine.museum import *
from engine import plan as PL

BGS = {'stone': bg_stone, 'museum': bg_museum, 'trench': bg_trench}
PERIOD = (-2600, -1900)      # set by each ep.py:  anc.PERIOD = (a, b)
LIT = C['lime']

def scene(bg, *layers, ribbon_on=True):
    flat = []
    for L in layers: flat += getattr(L, 'layers', [L])
    def f(ctx, t, D):
        BGS[bg](ctx, t)
        for L in flat: L(ctx, t, D)
        if ribbon_on: ribbon(ctx, t)
        corner(ctx)
    f.bg = bg; f.layers = flat
    return f

def wrap_s(ctx, s, size, maxw, bold=False, serif=True):
    font(ctx, size, bold, serif)
    lines, cur = [], ''
    for w_ in s.split():
        tt = (cur + ' ' + w_).strip()
        if ctx.text_extents(tt).x_advance > maxw and cur: lines.append(cur); cur = w_
        else: cur = tt
    if cur: lines.append(cur)
    return lines

def fmt_year(y):
    if y == 0: return '1 CE'
    if y < 0:
        n = -y
        if n >= 1000000: return f'{n / 1e6:g} million BCE'
        return f'{n:,} BCE'
    return f'{y} CE'

# ---------------- TIMELINE RIBBON ----------------
def ribbon(ctx, t):
    lo, hi = PERIOD
    span = max(hi - lo, 1)
    pad = max(span * .6, 120)
    a, b = lo - pad, min(hi + pad, 1400)
    x0, x1, y0, h = 560., 1850., 26., 40.
    carve(ctx, lambda: rrect(ctx, x0, y0, x1 - x0, h, 8), darker(C['basalt'], .3), .95, bev=2, grain=.2)
    raw = (b - a) / 5.5
    mag = 10 ** math.floor(math.log10(raw)); step = min((1, 2, 5, 10), key=lambda m: abs(m * mag - raw)) * mag
    k = math.ceil(a / step)
    while k * step <= b:
        yr = k * step
        x = x0 + (yr - a) / (b - a) * (x1 - x0)
        if x0 + 40 < x < x1 - 40:
            rgba(ctx, C['lime'], .5); ctx.rectangle(x - 1, y0 + 4, 2, h - 8); ctx.fill()
            text(ctx, fmt_year(int(yr)), x, y0 + h + 24, 18, C['lime'], .75, False)
        k += 1
    mx0 = x0 + (lo - a) / (b - a) * (x1 - x0); mx1 = x0 + (hi - a) / (b - a) * (x1 - x0)
    mx1 = max(mx1, mx0 + 14)
    mid = (mx0 + mx1) / 2
    lamp(ctx, mid, y0 + h / 2, 90 + (mx1 - mx0) / 2, .7, t=t)
    carve(ctx, lambda: rrect(ctx, mx0, y0 + 5, mx1 - mx0, h - 10, 6), C['ochre'], 1., bev=2, grain=.05)

# ---------------- DIG ----------------
def dig(art, question, tags=(), t_start=1.2, per=1.15, q_at=None):
    bands = 4
    def f(ctx, t, D):
        cx, cy, s = 960, 540, 1.9
        sl = 330
        carve(ctx, lambda: rrect(ctx, cx - sl, cy - 250, 2 * sl, 500, 18), darker(C['clay'], .5), .85, bev=3)
        draw_art(art, ctx, cx, cy, s, ease(seg(t, .3, 1.2)))
        bh = 500 / bands
        rng = random.Random(4)
        for k in range(bands):
            pk = ease(seg(t, t_start + k * per, t_start + k * per + per * .92))
            y = cy - 250 + k * bh
            if pk < 1:
                fr = (cx - sl + 2 * sl * pk) if k % 2 == 0 else (cx + sl - 2 * sl * pk)
                xa, xb = (fr, cx + sl) if k % 2 == 0 else (cx - sl, fr)
                def band(xa=xa, xb=xb, y=y):
                    ctx.new_sub_path(); ctx.move_to(xa, y); ctx.line_to(xb, y)
                    n = 9
                    for j in range(n + 1):
                        ctx.line_to(xb + (j % 2) * (7 if xb > xa else -7) * (0 if (xb == cx + sl or xb == cx - sl) else 1), y + bh * j / n)
                    ctx.line_to(xa, y + bh); ctx.close_path()
                carve(ctx, band, [C['clay'], darker(C['clay'], .2), C['ochre'], darker(C['clay'], .3)][k % 4], 1., bev=2, grain=.3)
                bx = fr
                if 0 < pk < 1:
                    ang = .35 * math.sin(t * 14) + (.4 if k % 2 == 0 else -.4)
                    ctx.save(); ctx.translate(bx, y + bh / 2); ctx.rotate(ang)
                    carve(ctx, lambda: rrect(ctx, -10, -150, 20, 120, 8), C['clay'], 1., bev=2)
                    carve(ctx, lambda: rrect(ctx, -34, -34, 68, 40, 8), C['lime'], 1., bev=2)
                    ctx.restore()
                    for j in range(16):
                        px = bx + rng.uniform(-60, 60) + (j % 4) * 6 * (1 if k % 2 == 0 else -1)
                        py = y + bh / 2 + ((t * 120 + j * 37) % 120)
                        rgba(ctx, C['clay'], .7 * (1 - ((t * 120 + j * 37) % 120) / 120)); ctx.arc(px, py, 3 + j % 3, 0, 2 * math.pi); ctx.fill()
        qa = ease(seg(t, T(q_at) if q_at is not None else t_start + bands * per + .3, (T(q_at) if q_at is not None else t_start + bands * per + .3) + .8))
        if qa > 0:
            lines = wrap_s(ctx, question, 52, 1500, True)
            ty = 190
            ctx.new_path(); rrect(ctx, 960 - 800, ty - 66, 1600, 40 + 62 * len(lines), 18); rgba(ctx, C['soot'], .62 * qa); ctx.fill()
            for i, l in enumerate(lines): etext(ctx, l, 960, ty + i * 62, 52, C['lime'], qa)
        for i, tg in enumerate(tags):
            ta = ease(seg(t, 2.5 + i * .8, 3.3 + i * .8))
            xx = 340 if i == 0 else 1580
            lbl_w = 360
            carve(ctx, lambda xx=xx: rrect(ctx, xx - lbl_w / 2, 790 - 24 * (1 - ta), lbl_w, 52, 10), C['lime'], ta, bev=2, grain=.2)
            font(ctx, 24, True, False); fs = min(24, 24 * (lbl_w - 28) / ctx.text_extents(tg).x_advance)
            text(ctx, tg, xx, 825 - 24 * (1 - ta) - (24 - fs) * .3, fs, C['soot'], ta, True, 'c', False)
    f.bg = 'trench'
    return f

# ---------------- SOURCES ----------------
SRC = [('trowel', 'dug up'), ('leaf', 'texts'), ('stone', 'inscriptions'), ('coin', 'coins'), ('staff', "travellers' accounts")]

def _icon(ctx, kind, x, y, a):
    if kind == 'trowel':
        carve(ctx, lambda: poly(ctx, [(-34, -40), (34, -40), (10, 50), (-10, 50)], x, y, 1.), C['sandst'], a)
        carve(ctx, lambda: rrect(ctx, x - 7, y + 46, 14, 56, 5), C['clay'], a, bev=2)
    elif kind == 'leaf':
        art_palmleaf(ctx, x, y + 10, .8, a)
    elif kind == 'stone':
        art_tablet(ctx, x, y + 10, .6, a)
    elif kind == 'coin':
        art_coin(ctx, x, y + 10, .7, a)
    elif kind == 'staff':
        carve(ctx, lambda: rrect(ctx, x - 6, y - 80, 12, 190, 5), C['clay'], a)
        carve(ctx, lambda: ell(ctx, x, y - 84, 18, 14), C['ochre'], a, bev=2)
        carve(ctx, lambda: ell(ctx, x, y - 40, 20, 8), C['ochre'], a, bev=2)

def sources(lit, notes=None, cues=None):
    notes = notes or {}
    def f(ctx, t, D):
        n = len(lit)
        for i, (kind, name) in enumerate(SRC):
            x = 960 + (i - 2) * 350; y = 470
            on = name in lit
            if on:
                j = lit.index(name)
                ct = T(cues[j]) if cues else (1.2 + j * 1.8)
                p = ease(seg(t, ct, ct + .7))
            else:
                p = 0
            carve(ctx, lambda x=x, y=y: rrect(ctx, x - 140, y - 150, 280, 330, 20), darker(C['basalt'], .2), .9, bev=3, grain=.2)
            if p > 0: lamp(ctx, x, y, 240, p * .9, t=t)
            _icon(ctx, kind, x, y, .35 + .65 * p)
            etext(ctx, name, x, y + 160, 28, C['lime'] if on else darker(C['lime'], .4), .5 + .5 * p)
            if on and notes.get(name):
                for k, l in enumerate(wrap_s(ctx, notes[name], 26, 270)[:3]):
                    text(ctx, l, x, y + 235 + k * 30, 24, C['sandst'], p, False, 'c', False)
    f.bg = 'stone'
    return f

# ---------------- FRIEZE ----------------
GROUND = 700

def v_fig(ctx, x, y, s, label=None, crown=False, col='terra', seated=False, a=1.):
    bh = (70 if seated else 100) * s
    carve(ctx, lambda: poly(ctx, [(-30, 0), (-18, -bh / s), (18, -bh / s), (30, 0)], x, y, s), C[col], a)
    carve(ctx, lambda: ell(ctx, x, y - bh - 18 * s, 16 * s, 17 * s), C['sandst'], a, bev=2)
    if crown:
        carve(ctx, lambda: poly(ctx, [(-17, -2), (-13, -22), (-5, -10), (0, -26), (5, -10), (13, -22), (17, -2)], x, y - bh - 28 * s, s), C['ochre'], a, bev=1)
    else:
        carve(ctx, lambda: ell(ctx, x, y - bh - 28 * s, 16 * s, 8 * s), darker(C['clay'], .2), a, bev=1)
    carve(ctx, lambda: rrect(ctx, x + 14 * s, y - bh + 6 * s, 10 * s, 46 * s, 5), C['sandst'], a, bev=1)
    if label: nameplate(ctx, x, y + 14, label, a)

def nameplate(ctx, x, y, label, a=1., size=21):
    font(ctx, size, True, False)
    w = ctx.text_extents(label).x_advance + 28
    carve(ctx, lambda: rrect(ctx, x - w / 2, y, w, 34, 6), C['lime'], a, bev=2, grain=.2)
    text(ctx, label, x, y + 24, size, C['soot'], a, True, 'c', False)

def v_house(ctx, x, y, s, a=1.):
    carve(ctx, lambda: rrect(ctx, x - 70 * s, y - 80 * s, 140 * s, 80 * s, 3), C['sandst'], a)
    carve(ctx, lambda: poly(ctx, [(-86, 0), (86, 0), (50, -50), (-50, -50)], x, y - 80 * s, s), C['terra'], a)
    carve(ctx, lambda: rrect(ctx, x - 14 * s, y - 48 * s, 28 * s, 48 * s, 12 * s), C['soot'], a, bev=2)

def v_wall(ctx, x, y, s, a=1.):
    w = 300 * s
    carve(ctx, lambda: rrect(ctx, x - w / 2, y - 100 * s, w, 100 * s, 3), C['sandst'], a)
    for i in range(7):
        carve(ctx, lambda i=i: rrect(ctx, x - w / 2 + i * w / 7 + 4, y - 128 * s, w / 7 - 12, 28 * s, 2), C['sandst'], a, bev=2)
    groove(ctx, lambda: (ctx.move_to(x - w / 2, y - 50 * s), ctx.line_to(x + w / 2, y - 50 * s)), a)

def v_tree(ctx, x, y, s, a=1.):
    carve(ctx, lambda: rrect(ctx, x - 9 * s, y - 100 * s, 18 * s, 100 * s, 4), C['clay'], a)
    for dx, dy, r in ((-30, -120, 40), (0, -150, 48), (32, -118, 40)):
        carve(ctx, lambda dx=dx, dy=dy, r=r: ell(ctx, x + dx * s, y + dy * s, r * s, r * s * .82), darker(C['sandst'], .15), a, bev=2)

def v_hill(ctx, x, y, s, a=1.):
    carve(ctx, lambda: poly(ctx, [(-190, 0), (-60, -120), (0, -90), (80, -170), (200, 0)], x, y, s), C['clay'], a)

def v_sun(ctx, x, y, s, a=1.):
    for i in range(12):
        an = i * math.pi / 6
        groove(ctx, lambda an=an: (ctx.move_to(x + 56 * s * math.cos(an), y + 56 * s * math.sin(an)), ctx.line_to(x + 84 * s * math.cos(an), y + 84 * s * math.sin(an))), a, C['ochre'], 5)
    carve(ctx, lambda: ell(ctx, x, y, 44 * s, 44 * s), C['ochre'], a, bev=3)

def v_river(ctx, x, y, w, a=1.):
    for k in range(3):
        groove(ctx, lambda k=k: (ctx.new_sub_path(), ctx.move_to(x - w / 2, y + k * 22), [ctx.line_to(x - w / 2 + i * 20, y + k * 22 + 7 * math.sin(i * .9 + k)) for i in range(1, int(w / 20) + 1)]), a, C['verd'] if False else C['lime'], 4)

def v_text(ctx, x, y, s, size, a=1.):
    etext(ctx, s, x, y, size, C['lime'], a)

def v_ledge(ctx, x0, x1, a=1.):
    carve(ctx, lambda: rrect(ctx, x0, GROUND, x1 - x0, 22, 3), darker(C['sandst'], .3), a, bev=2, grain=.25)

def _item(ctx, cx, it, a):
    kind, dx, dy, s = it[0], it[1], it[2], it[3]
    x, y = cx + dx, GROUND + dy
    rest = it[4:]
    if kind == 'fig': v_fig(ctx, x, y, s, *(rest[:1] or [None]), **(rest[1] if len(rest) > 1 else {}), a=a)
    elif kind == 'house': v_house(ctx, x, y, s, a)
    elif kind == 'wall': v_wall(ctx, x, y, s, a)
    elif kind == 'tree': v_tree(ctx, x, y, s, a)
    elif kind == 'hill': v_hill(ctx, x, y, s, a)
    elif kind == 'sun': v_sun(ctx, x, y - 400 * s, s, a)
    elif kind == 'river': v_river(ctx, x, y + 40, s, a)
    elif kind == 'text': v_text(ctx, x, y, it[3], rest[0] if rest else 30, a)
    elif kind.startswith('art:'): draw_art(kind[4:], ctx, x, y - 100 * s, s, a)
    if kind.startswith('art:') and rest and rest[0]: nameplate(ctx, x, y + 14, rest[0], a)

def frieze(scenes, cues=None, width=1050):
    """scenes: list of dict(title=..., items=[(kind, dx, dy, scale, ...)]); cues: narration phrase (or seconds) at which the camera centres each scene"""
    n = len(scenes)
    def f(ctx, t, D):
        ts = [(.0 if i == 0 else T(cues[i])) for i in range(n)] if cues else [i * D / n for i in range(n)]
        cx = [width * (i + .5) + 200 for i in range(n)]
        cam = cx[0]
        for i in range(n - 1):
            cam = lerp(cx[i], cx[i + 1], ease(seg(t, ts[i + 1] - 1.6, ts[i + 1] - .2))) if t >= ts[i + 1] - 1.6 else cam
            if t < ts[i + 1] - 1.6: break
        else:
            cam = cx[-1]
        left, right = 200 - 120, 200 + n * width + 120
        ctx.save(); ctx.translate(W / 2 - cam, 0)
        # panel body
        carve(ctx, lambda: rrect(ctx, left, 140, right - left, 700, 14), darker(C['sandst'], .5), 1., bev=4, grain=.3)
        # borders: bead-and-reel (top) and lotus (bottom)
        x0 = max(left, cam - 1300); x1 = min(right, cam + 1300)
        for k in range(int((x1 - x0) / 46) + 1):
            xx = int(x0 // 46) * 46 + k * 46 + 23
            if left < xx < right:
                carve(ctx, lambda xx=xx: ell(ctx, xx, 166, 13, 13) if (xx // 46) % 2 == 0 else rrect(ctx, xx - 16, 158, 32, 16, 5), C['sandst'], 1., bev=2, grain=.1)
                carve(ctx, lambda xx=xx: poly(ctx, [(-14, 12), (0, -14), (14, 12)], xx, 812, 1.), C['sandst'] if (xx // 46) % 2 == 0 else C['ochre'], 1., bev=2, grain=.1)
        groove(ctx, lambda: (ctx.move_to(left + 10, 196), ctx.line_to(right - 10, 196)), 1., C['soot'], 3)
        groove(ctx, lambda: (ctx.move_to(left + 10, 782), ctx.line_to(right - 10, 782)), 1., C['soot'], 3)
        for i, sc in enumerate(scenes):
            sx = cx[i]
            if abs(sx - cam) > 1500: continue
            near = 1 - cl((abs(sx - cam) - 200) / 700)
            a = .55 + .45 * near
            v_ledge(ctx, sx - width / 2 + 20, sx + width / 2 - 20, a)
            for it in sc['items']: _item(ctx, sx, it, a)
            if sc.get('title'):
                etext(ctx, sc['title'], sx, 770, 24, C['soot'] if False else C['lime'], .55 + .45 * near, serif=False)
            if i < n - 1:
                rgba(ctx, C['soot'], .45); ctx.rectangle(sx + width / 2 - 2, 204, 4, 570); ctx.fill()
        ctx.restore()
        # lamp glow and vignette over the panel
        lamp(ctx, W / 2, 470, 900, .22, t=t)
    f.bg = 'stone'
    return f

# ---------------- PLAQUE ----------------
def plaque(old=None, new=None, a_txt=None, b_txt=None, heading=None, cue_a=None, cue_b=None, sub=None):
    def f(ctx, t, D):
        if old:   # old name -> new name
            p1 = ease(seg(t, .8, 1.6)); p2 = ease(seg(t, T(cue_b) if cue_b else 3.0, (T(cue_b) if cue_b else 3.0) + .8))
            etext(ctx, 'Old name, new name', 960, 250, 48, C['sandst'], ease(seg(t, .2, .9)))
            for xx, lab, p in ((520, old, p1), (1400, new, p2)):
                font(ctx, 54, True, True); fs = min(54, 54 * 600 / ctx.text_extents(lab).x_advance)
                carve(ctx, lambda xx=xx: rrect(ctx, xx - 330, 380, 660, 220, 16), C['lime'], p, bev=4, grain=.2)
                text(ctx, lab, xx, 510 + (54 - fs) * .35, fs, C['soot'], p, True, 'c', True)
            pa = ease(seg(t, T(cue_b) - .3 if cue_b else 2.6, (T(cue_b) if cue_b else 3.0) + .4))
            if pa > 0:
                ctx.save(); ctx.translate(960, 490)
                carve(ctx, lambda: poly(ctx, [(-90, -18), (20, -18), (20, -50), (90, 0), (20, 50), (20, 18), (-90, 18)], 0, 0, 1.), C['ochre'], pa, bev=3)
                ctx.restore()
            if sub:
                for i, l in enumerate(wrap_s(ctx, sub, 32, 1500)): text(ctx, l, 960, 700 + i * 44, 32, C['lime'], p2, False, 'c', True)
        else:     # two tablets: scholars disagree
            etext(ctx, heading or 'Scholars disagree', 960, 230, 56, C['sandst'], ease(seg(t, .2, .9)))
            for xx, (title, body), cu in ((520, a_txt, cue_a), (1400, b_txt, cue_b)):
                p = ease(seg(t, T(cu) if cu else .9, (T(cu) if cu else .9) + .8))
                carve(ctx, lambda xx=xx: rrect(ctx, xx - 400, 300, 800, 480, 18), C['lime'], p, bev=4, grain=.2)
                text(ctx, title, xx, 370, 40, C['terra'], p, True, 'c', True)
                for i, l in enumerate(wrap_s(ctx, body, 30, 720)[:7]): text(ctx, l, xx, 430 + i * 44, 30, C['soot'], p, False, 'c', True)
    f.bg = 'stone'
    return f

# ---------------- INSCRIPTION ----------------
TAP_START, TAP_RATE = 1.4, .12      # seconds, per letter

def inscription(lines, start=TAP_START):
    total = sum(len(l) for l in lines)
    def f(ctx, t, D):
        tab_w, tab_h = 1240, 130 + 100 * len(lines)
        x, y = 960 - tab_w / 2, 560 - tab_h / 2
        carve(ctx, lambda: rrect(ctx, x, y, tab_w, tab_h, 30), C['lime'], ease(seg(t, .2, .9)), bev=5, grain=.22)
        groove(ctx, lambda: rrect(ctx, x + 18, y + 18, tab_w - 36, tab_h - 36, 20), ease(seg(t, .2, .9)), C['clay'], 3)
        font(ctx, 54, True, True); fs = min(54, 54 * 1120 / max(ctx.text_extents(l).x_advance for l in lines))
        n = int((t - start) / TAP_RATE) if t > start else 0
        glow = ease(seg(t, start + total * TAP_RATE + .2, start + total * TAP_RATE + 1.6))
        used = 0; tip = None
        for i, l in enumerate(lines):
            k = max(0, min(len(l), n - used)); used += len(l)
            ly = y + 120 + i * 100
            font(ctx, fs, True, True)
            full_w = ctx.text_extents(l).x_advance
            if k > 0:
                part = l[:k]
                col = C['soot'] if glow <= 0 else mix(C['soot'], C['verd'], glow)
                text(ctx, part, 960 - full_w / 2, ly, fs, col, 1., True, 'l', True)
                if glow > 0:
                    text(ctx, part, 960 - full_w / 2, ly, fs, C['verd'], .0, True, 'l', True, glow=C['verd'])
                    ctx.save(); ctx.set_source_rgba(*C['verd'], .35 * glow)
                    font(ctx, fs, True, True); ctx.move_to(960 - full_w / 2, ly); ctx.text_path(part); ctx.set_line_width(10); ctx.stroke(); ctx.restore()
                if k < len(l): tip = (960 - full_w / 2 + ctx.text_extents(part).x_advance, ly)
        if tip and glow <= 0:
            ctx.save(); ctx.translate(tip[0] + 22, tip[1] - 28); ctx.rotate(-.6 + .08 * math.sin(t * 40))
            carve(ctx, lambda: rrect(ctx, -6, -110, 12, 90, 3), C['basalt'], 1., bev=2)
            carve(ctx, lambda: poly(ctx, [(-6, -22), (6, -22), (0, 12)], 0, 0, 1.), C['lime'], 1., bev=1)
            ctx.restore()
    f.bg = 'stone'
    return f

def chisel_times(lines, start=TAP_START):
    return [start + i * TAP_RATE for i in range(sum(len(l) for l in lines))]

# ---------------- QUIZ ----------------
def quiz_card(ctx, art, idx, t, q_t, a_t, answer, n_total=3, ring=3.0):
    p = ease(seg(t, q_t, q_t + .8))
    if p <= 0: return
    y = 580 + (1 - eoc(p)) * 340
    x0 = 960 - 520
    carve(ctx, lambda: rrect(ctx, x0, y - 330, 1040, 600, 22), C['lime'], p, bev=5, grain=.22)
    draw_art(art, ctx, 960 - 280, y - 40, 1.45, p)
    text(ctx, f'{idx + 1} of {n_total}', 960 + 330, y - 270, 24, C['clay'], p, True, 'c', False)
    text(ctx, 'Pause and name it', 960 + 220, y - 150, 40, C['terra'], p, True, 'c', True)
    if t < a_t and p > .9:
        rem = a_t - t
        rr = 74; cx, cy = 960 + 220, y - 20
        ctx.new_path(); ctx.arc(cx, cy, rr, 0, 2 * math.pi); rgba(ctx, C['clay'], .35); ctx.set_line_width(12); ctx.stroke()
        if rem < ring:
            ctx.new_path(); ctx.arc(cx, cy, rr, -math.pi / 2, -math.pi / 2 + 2 * math.pi * cl(rem / ring)); rgba(ctx, C['terra'], 1); ctx.set_line_width(12); ctx.stroke()
            text(ctx, str(max(1, math.ceil(rem))), cx, cy + 26, 76, C['soot'], 1., True, 'c', True)
    pa = ease(seg(t, a_t, a_t + .7))
    if pa > 0:
        for i, l in enumerate(wrap_s(ctx, answer, 44, 520, True)):
            etext(ctx, l, 960 + 220, y + 120 + i * 50, 44, C['soot'], pa)

def quiz(cards, mains, mains_at):
    """cards: [(art, q_phrase, a_phrase, answer)], mains: one line"""
    def f(ctx, t, D):
        ts = [(T(q), T(a)) for _, q, a, _ in cards]
        for i, (art, q, a, ans) in enumerate(cards):
            q_t, a_t = ts[i]
            end = ts[i + 1][0] - .2 if i + 1 < len(cards) else T(mains_at) - .3
            if q_t - .05 <= t < end:
                quiz_card(ctx, art, i, t, q_t, a_t, ans, len(cards))
        ma = ease(seg(t, T(mains_at), T(mains_at) + .8))
        if ma > 0:
            carve(ctx, lambda: rrect(ctx, 960 - 760, 330, 1520, 330, 22), C['sandst'], ma, bev=5, grain=.22)
            text(ctx, 'MAINS', 960, 410, 36, C['terra'], ma, True, 'c', True)
            for i, l in enumerate(wrap_s(ctx, mains, 40, 1380, True)): text(ctx, l, 960, 480 + i * 56, 40, C['soot'], ma, True, 'c', True)
    f.bg = 'stone'
    return f

# ---------------- GALLERY ----------------
def _slot(ep):
    return PL.BY_EP[ep]

def gallery(ep, title, facts, nxt, place_at=1.5, fact_cues=None, next_cue=None):
    """the exhibit is placed in its case with a thud; earlier exhibits stay in their cases along the back row"""
    def f(ctx, t, D):
        cur = _slot(ep)
        earlier = [e for e in range(max(1, ep - 11), ep)]
        # back row of earlier cases
        for k, e in enumerate(earlier):
            x = 140 + k * 165; y = 215
            case(ctx, x, y, 118, 150, .8, t)
            draw_art(_slot(e)[4], ctx, x, case_art_y(y, 150), .4, .9)
            text(ctx, str(e), x, y + 98, 20, C['lime'], .6, True, 'c', False)
        # current case, big
        cxs, cys = 560, 585
        case(ctx, cxs, cys, 440, 470, 1., t)
        land = place_at
        fall = 1 - eoc(seg(t, land - .9, land))
        bounce = 6 * math.sin(seg(t, land, land + .5) * math.pi * 3) * (1 - seg(t, land, land + .5)) if t > land else 0
        draw_art(cur[4], ctx, cxs, case_art_y(cys, 470) - 420 * fall - bounce, 1.55, ease(seg(t, land - 1.1, land - .6)))
        if t > land:
            lamp(ctx, cxs, case_art_y(cys, 470), 420, .35 * ease(seg(t, land, land + 1.2)), t=t)
        # label
        lp = ease(seg(t, land + .6, land + 1.4))
        lw = 760
        n = len(facts)
        lh = 150 + 74 * n + 62
        lx, ly = 1300 - lw / 2 + 40, 560 - lh / 2 + (1 - eoc(lp)) * 40
        carve(ctx, lambda: rrect(ctx, lx, ly, lw, lh, 14), C['lime'], lp, bev=4, grain=.2)
        groove(ctx, lambda: rrect(ctx, lx + 12, ly + 12, lw - 24, lh - 24, 8), lp, C['ochre'], 3)
        text(ctx, title, lx + lw / 2, ly + 80, 40, C['soot'], lp, True, 'c', True)
        for i, fa in enumerate(facts):
            ft = T(fact_cues[i]) if fact_cues else land + 1.4 + i * .9
            fp = ease(seg(t, ft, ft + .7))
            lines = wrap_s(ctx, fa, 28, lw - 110)
            for j, l in enumerate(lines[:2]):
                text(ctx, ('•  ' if j == 0 else '    ') + l, lx + 46, ly + 150 + i * 74 + j * 32, 28, C['soot'], fp, False, 'l', True)
        nt = T(next_cue) if next_cue else land + 1.4 + n * .9 + .3
        np_ = ease(seg(t, nt, nt + .7))
        if nxt:
            text(ctx, 'Next gallery: ' + nxt, lx + lw / 2, ly + lh - 34, 28, C['terra'], np_, True, 'c', True)
    f.bg = 'museum'
    return f

def final_walk(total=44):
    """slow walk past every case"""
    def f(ctx, t, D):
        sp = 420
        cam = lerp(260, 260 + (total - 1) * sp, ease(seg(t, 1.0, D - 3.0)))
        ctx.save(); ctx.translate(W / 2 - cam, 0)
        for e in range(1, total + 1):
            x = 260 + (e - 1) * sp
            if abs(x - cam) > 1200: continue
            case(ctx, x, 520, 300, 400, 1., t)
            draw_art(PL.BY_EP[e][4], ctx, x, case_art_y(520, 400), 1.0, 1.)
            text(ctx, f'{e}', x, 760, 28, C['lime'], .8, True, 'c', False)
            text(ctx, PL.BY_EP[e][5], x, 800, 24, C['sandst'], .9, False, 'c', False)
        ctx.restore()
    f.bg = 'museum'
    return f
