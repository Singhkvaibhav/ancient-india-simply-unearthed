"""The gallery and its exhibits. Each exhibit is its own small function art_<name>(ctx, cx, cy, s, a); ART maps names to them.
Figures of revered persons are never drawn: the Buddha, Mahavira and deities are shown by symbols only."""
import math
from engine.core import *
from engine.stone import *

def ell(ctx, x, y, rx, ry):
    ctx.save(); ctx.translate(x, y); ctx.scale(rx, ry); ctx.new_sub_path(); ctx.arc(0, 0, 1, 0, 2 * math.pi); ctx.restore()

def poly(ctx, pts, cx=0, cy=0, s=1):
    ctx.new_sub_path(); ctx.move_to(cx + pts[0][0] * s, cy + pts[0][1] * s)
    for x, y in pts[1:]: ctx.line_to(cx + x * s, cy + y * s)
    ctx.close_path()

def C_(k): return C[k]

# ---- exhibits (drawn about 200 px wide at s=1) ----
def art_handaxe(ctx, cx, cy, s=1., a=1.):
    carve(ctx, lambda: poly(ctx, [(0, -90), (45, -20), (55, 40), (20, 85), (-25, 85), (-55, 35), (-40, -25)], cx, cy, s), C['clay'], a)
    groove(ctx, lambda: poly(ctx, [(0, -60), (28, -10), (34, 40), (0, 62), (-30, 40), (-26, -10)], cx, cy, s), a)

def art_polishedaxe(ctx, cx, cy, s=1., a=1.):
    carve(ctx, lambda: poly(ctx, [(-30, -85), (30, -85), (50, 70), (0, 90), (-50, 70)], cx, cy, s), C['basalt'], a, grain=.2)
    groove(ctx, lambda: poly(ctx, [(-50, 70), (0, 90), (50, 70)], cx, cy, s), a, C['lime'], 2)

def art_pot(ctx, cx, cy, s=1., a=1.):
    def body():
        ctx.new_sub_path(); ctx.move_to(cx - 40 * s, cy - 80 * s); ctx.curve_to(cx - 120 * s, cy - 40 * s, cx - 110 * s, cy + 70 * s, cx - 50 * s, cy + 90 * s)
        ctx.line_to(cx + 50 * s, cy + 90 * s); ctx.curve_to(cx + 110 * s, cy + 70 * s, cx + 120 * s, cy - 40 * s, cx + 40 * s, cy - 80 * s); ctx.close_path()
    carve(ctx, body, C['terra'], a)
    for i in range(3):
        groove(ctx, lambda i=i: (ctx.new_sub_path(), ctx.move_to(cx - 98 * s + i * 4, cy - 10 * s + i * 22 * s), ctx.curve_to(cx - 30 * s, cy + 14 * s + i * 22 * s, cx + 30 * s, cy + 14 * s + i * 22 * s, cx + 98 * s - i * 4, cy - 10 * s + i * 22 * s)), a, C['soot'], 4)
    carve(ctx, lambda: ell(ctx, cx, cy - 82 * s, 48 * s, 12 * s), darker(C['terra'], .3), a)

def art_seal(ctx, cx, cy, s=1., a=1.):
    carve(ctx, lambda: rrect(ctx, cx - 75 * s, cy - 75 * s, 150 * s, 150 * s, 10 * s), C['sandst'], a)
    # a bull in profile, schematic
    carve(ctx, lambda: poly(ctx, [(-45, 10), (-40, -20), (-15, -30), (20, -30), (45, -20), (50, 0), (40, 38), (28, 38), (24, 14), (-20, 14), (-24, 38), (-38, 38)], cx, cy, s), darker(C['sandst'], .3), a, bev=2)
    carve(ctx, lambda: poly(ctx, [(-45, -20), (-60, -34), (-50, -36), (-36, -28)], cx, cy, s), darker(C['sandst'], .3), a, bev=2)
    for i in range(5):
        carve(ctx, lambda i=i: rrect(ctx, cx - 56 * s + i * 22 * s, cy - 62 * s, 14 * s, 14 * s, 3), darker(C['sandst'], .4), a, bev=1)

def art_bead(ctx, cx, cy, s=1., a=1.):
    for i in range(7):
        x = cx + (i - 3) * 30 * s
        carve(ctx, lambda x=x: ell(ctx, x, cy + 28 * s * math.cos((i - 3) * .35) - 20 * s, 15 * s, 22 * s), [C['terra'], C['ochre'], C['lime']][i % 3], a, bev=2)

def art_palmleaf(ctx, cx, cy, s=1., a=1.):
    carve(ctx, lambda: rrect(ctx, cx - 110 * s, cy - 36 * s, 220 * s, 72 * s, 8 * s), C['ochre'], a)
    for i in range(4):
        groove(ctx, lambda i=i: (ctx.move_to(cx - 92 * s, cy - 20 * s + i * 13 * s), ctx.line_to(cx + 92 * s, cy - 20 * s + i * 13 * s)), a, C['soot'], 3)
    for x in (-70, 70):
        carve(ctx, lambda x=x: ell(ctx, cx + x * s, cy, 6 * s, 6 * s), C['soot'], a, bev=1)

def art_tablet(ctx, cx, cy, s=1., a=1.):
    carve(ctx, lambda: rrect(ctx, cx - 70 * s, cy - 95 * s, 140 * s, 190 * s, 40 * s), C['lime'], a, grain=.18)
    for i in range(6):
        groove(ctx, lambda i=i: (ctx.move_to(cx - 42 * s, cy - 40 * s + i * 22 * s), ctx.line_to(cx + 42 * s - (i % 2) * 20 * s, cy - 40 * s + i * 22 * s)), a, C['soot'], 4)

def art_coin(ctx, cx, cy, s=1., a=1.):
    carve(ctx, lambda: ell(ctx, cx, cy, 78 * s, 78 * s), C['ochre'], a, bev=4)
    groove(ctx, lambda: ell(ctx, cx, cy, 62 * s, 62 * s), a, C['soot'], 3)
    carve(ctx, lambda: poly(ctx, [(0, -40), (10, -10), (40, -10), (16, 8), (24, 38), (0, 20), (-24, 38), (-16, 8), (-40, -10), (-10, -10)], cx, cy, s), darker(C['ochre'], .35), a, bev=2)

def art_stupa(ctx, cx, cy, s=1., a=1.):
    carve(ctx, lambda: rrect(ctx, cx - 100 * s, cy + 50 * s, 200 * s, 34 * s, 4), C['sandst'], a)
    carve(ctx, lambda: (ctx.new_sub_path(), ctx.arc(cx, cy + 50 * s, 82 * s, math.pi, 2 * math.pi), ctx.close_path()), C['lime'], a)
    carve(ctx, lambda: rrect(ctx, cx - 26 * s, cy - 50 * s, 52 * s, 20 * s, 3), C['sandst'], a)
    carve(ctx, lambda: rrect(ctx, cx - 5 * s, cy - 100 * s, 10 * s, 52 * s, 3), C['clay'], a)
    for i in range(3):
        carve(ctx, lambda i=i: rrect(ctx, cx - (36 - i * 9) * s, cy - (92 - i * 14) * s, (72 - i * 18) * s, 8 * s, 3), C['sandst'], a, bev=2)

def art_pillar(ctx, cx, cy, s=1., a=1.):
    carve(ctx, lambda: poly(ctx, [(-26, 95), (-20, -50), (20, -50), (26, 95)], cx, cy, s), C['sandst'], a, grain=.2)
    carve(ctx, lambda: rrect(ctx, cx - 44 * s, cy - 78 * s, 88 * s, 28 * s, 6), C['lime'], a)
    carve(ctx, lambda: ell(ctx, cx, cy - 98 * s, 44 * s, 18 * s), C['sandst'], a)

def art_bullcap(ctx, cx, cy, s=1., a=1.):
    """Rampurva bull capital: a bull standing on an abacus above a lotus bell"""
    carve(ctx, lambda: poly(ctx, [(-46, 95), (-60, 42), (-20, 20), (20, 20), (60, 42), (46, 95)], cx, cy, s), C['sandst'], a)   # bell
    carve(ctx, lambda: rrect(ctx, cx - 76 * s, cy + 6 * s, 152 * s, 18 * s, 4), C['lime'], a)
    carve(ctx, lambda: poly(ctx, [(-62, 4), (-58, -44), (-20, -60), (32, -58), (60, -44), (66, -10), (56, 4), (44, 4), (42, -16), (-34, -16), (-36, 4)], cx, cy, s), C['sandst'], a)
    carve(ctx, lambda: poly(ctx, [(-58, -42), (-86, -58), (-96, -48), (-72, -30), (-60, -22)], cx, cy, s), C['sandst'], a)
    carve(ctx, lambda: poly(ctx, [(-82, -58), (-92, -80), (-82, -76), (-74, -56)], cx, cy, s), C['lime'], a, bev=2)

def art_wheel(ctx, cx, cy, s=1., a=1.):
    carve(ctx, lambda: ell(ctx, cx, cy, 85 * s, 85 * s), C['ochre'], a, bev=4)
    carve(ctx, lambda: ell(ctx, cx, cy, 66 * s, 66 * s), C['soot'], a, bev=2, grain=.1)
    for i in range(24):
        an = i * math.pi / 12
        groove(ctx, lambda an=an: (ctx.move_to(cx + 14 * s * math.cos(an), cy + 14 * s * math.sin(an)), ctx.line_to(cx + 66 * s * math.cos(an), cy + 66 * s * math.sin(an))), a, C['ochre'], 3)
    carve(ctx, lambda: ell(ctx, cx, cy, 16 * s, 16 * s), C['ochre'], a, bev=2)

def art_lotus(ctx, cx, cy, s=1., a=1.):
    for k, ang in enumerate((-70, -35, 0, 35, 70)):
        r = math.radians(ang)
        def petal(r=r):
            ctx.save(); ctx.translate(cx, cy + 50 * s); ctx.rotate(r); ctx.new_sub_path(); ctx.move_to(0, 0)
            ctx.curve_to(-34 * s, -40 * s, -26 * s, -90 * s, 0, -118 * s); ctx.curve_to(26 * s, -90 * s, 34 * s, -40 * s, 0, 0); ctx.close_path(); ctx.restore()
        carve(ctx, petal, C['lime'] if k % 2 == 0 else C['sandst'], a, bev=2)
    carve(ctx, lambda: ell(ctx, cx, cy + 56 * s, 62 * s, 14 * s), C['clay'], a)

def art_footprints(ctx, cx, cy, s=1., a=1.):
    for dx in (-52, 52):
        carve(ctx, lambda dx=dx: ell(ctx, cx + dx * s, cy, 38 * s, 78 * s), C['sandst'], a)
        groove(ctx, lambda dx=dx: ell(ctx, cx + dx * s, cy + 8 * s, 22 * s, 48 * s), a, C['soot'], 3)
        for j in range(5):
            carve(ctx, lambda dx=dx, j=j: ell(ctx, cx + (dx + (j - 2) * 14) * s, cy - 78 * s - abs(j - 2) * -4 * s, 7 * s, 9 * s), C['lime'], a, bev=1)

def art_bodhitree(ctx, cx, cy, s=1., a=1.):
    carve(ctx, lambda: poly(ctx, [(-14, 95), (-10, 10), (-40, -20), (-26, -22), (0, 0), (26, -22), (40, -20), (10, 10), (14, 95)], cx, cy, s), C['clay'], a)
    for x, y, r in ((-50, -48, 42), (0, -78, 52), (52, -46, 42), (-12, -30, 38)):
        carve(ctx, lambda x=x, y=y, r=r: ell(ctx, cx + x * s, cy + y * s, r * s, r * s * .85), C['verd'] if False else darker(C['sandst'], .12), a, bev=2)

def art_throne(ctx, cx, cy, s=1., a=1.):
    """empty throne: a seat with high back and nothing on it"""
    carve(ctx, lambda: rrect(ctx, cx - 70 * s, cy - 90 * s, 140 * s, 110 * s, 12 * s), C['ochre'], a)
    carve(ctx, lambda: rrect(ctx, cx - 90 * s, cy + 20 * s, 180 * s, 36 * s, 6 * s), C['sandst'], a)
    carve(ctx, lambda: rrect(ctx, cx - 78 * s, cy + 56 * s, 28 * s, 44 * s, 4 * s), C['clay'], a)
    carve(ctx, lambda: rrect(ctx, cx + 50 * s, cy + 56 * s, 28 * s, 44 * s, 4 * s), C['clay'], a)

def art_sword(ctx, cx, cy, s=1., a=1.):
    carve(ctx, lambda: poly(ctx, [(-8, -100), (8, -100), (12, 50), (0, 62), (-12, 50)], cx, cy, s), C['basalt'], a, grain=.1)
    carve(ctx, lambda: rrect(ctx, cx - 44 * s, cy + 50 * s, 88 * s, 14 * s, 4), C['ochre'], a)
    carve(ctx, lambda: rrect(ctx, cx - 7 * s, cy + 62 * s, 14 * s, 36 * s, 4), C['clay'], a)

def art_plough(ctx, cx, cy, s=1., a=1.):
    carve(ctx, lambda: poly(ctx, [(-90, -20), (30, 40), (80, 38), (84, 60), (20, 62), (-96, 0)], cx, cy, s), C['clay'], a)
    carve(ctx, lambda: poly(ctx, [(34, 36), (96, 44), (60, 90)], cx, cy, s), C['basalt'], a, grain=.1)

def art_ship(ctx, cx, cy, s=1., a=1.):
    carve(ctx, lambda: poly(ctx, [(-100, 20), (100, 20), (70, 70), (-70, 70)], cx, cy, s), C['clay'], a)
    carve(ctx, lambda: rrect(ctx, cx - 4 * s, cy - 90 * s, 8 * s, 110 * s, 2), C['sandst'], a, bev=2)
    carve(ctx, lambda: poly(ctx, [(6, -86), (70, -10), (6, 8)], cx, cy, s), C['lime'], a)

def art_elephant(ctx, cx, cy, s=1., a=1.):
    carve(ctx, lambda: poly(ctx, [(-90, 30), (-86, -30), (-40, -64), (20, -62), (62, -40), (74, 0), (70, 40), (84, 80), (66, 82), (56, 50), (40, 50), (40, 82), (20, 82), (16, 50), (-40, 50), (-44, 82), (-64, 82), (-70, 50)], cx, cy, s), C['basalt'], a, grain=.2)
    carve(ctx, lambda: poly(ctx, [(68, 8), (84, 38), (74, 40)], cx, cy, s), C['lime'], a, bev=1)

def art_temple(ctx, cx, cy, s=1., a=1.):
    carve(ctx, lambda: rrect(ctx, cx - 78 * s, cy + 30 * s, 156 * s, 60 * s, 4), C['sandst'], a)
    carve(ctx, lambda: poly(ctx, [(-56, 30), (-40, -30), (-24, -70), (0, -104), (24, -70), (40, -30), (56, 30)], cx, cy, s), C['ochre'], a)
    for i in range(4):
        groove(ctx, lambda i=i: (ctx.move_to(cx - (50 - i * 8) * s, cy + (20 - i * 30) * s), ctx.line_to(cx + (50 - i * 8) * s, cy + (20 - i * 30) * s)), a, C['soot'], 3)
    carve(ctx, lambda: rrect(ctx, cx - 16 * s, cy + 46 * s, 32 * s, 44 * s, 14), C['soot'], a, bev=2)

def art_gopuram(ctx, cx, cy, s=1., a=1.):
    for i in range(5):
        w = (150 - i * 22) * s
        carve(ctx, lambda i=i, w=w: rrect(ctx, cx - w / 2, cy + (60 - i * 30) * s, w, 28 * s, 3), [C['terra'], C['ochre'], C['sandst']][i % 3], a, bev=2)
    carve(ctx, lambda: ell(ctx, cx, cy - 98 * s, 20 * s, 10 * s), C['ochre'], a, bev=2)

def art_fort(ctx, cx, cy, s=1., a=1.):
    carve(ctx, lambda: rrect(ctx, cx - 110 * s, cy - 30 * s, 220 * s, 120 * s, 4), C['sandst'], a)
    for i in range(6):
        carve(ctx, lambda i=i: rrect(ctx, cx - 110 * s + i * 40 * s, cy - 56 * s, 28 * s, 28 * s, 2), C['sandst'], a, bev=2)
    carve(ctx, lambda: rrect(ctx, cx - 28 * s, cy + 30 * s, 56 * s, 60 * s, 26), C['soot'], a, bev=2)

def art_scales(ctx, cx, cy, s=1., a=1.):
    carve(ctx, lambda: rrect(ctx, cx - 100 * s, cy - 70 * s, 200 * s, 10 * s, 3), C['ochre'], a)
    carve(ctx, lambda: rrect(ctx, cx - 5 * s, cy - 70 * s, 10 * s, 150 * s, 3), C['ochre'], a)
    for sx in (-90, 90):
        carve(ctx, lambda sx=sx: (ctx.new_sub_path(), ctx.arc(cx + sx * s, cy - 8 * s, 44 * s, 0, math.pi), ctx.close_path()), C['ochre'], a, bev=2)
        groove(ctx, lambda sx=sx: poly(ctx, [(sx, -60), (sx - 40, -8), (sx + 40, -8)], cx, cy, s), a, C['lime'], 2)

def art_lamp(ctx, cx, cy, s=1., a=1.):
    carve(ctx, lambda: poly(ctx, [(-80, 10), (-40, -10), (50, -10), (96, -30), (96, -12), (60, 40), (-50, 50)], cx, cy, s), C['ochre'], a)
    carve(ctx, lambda: ell(ctx, cx + 100 * s, cy - 36 * s, 10 * s, 14 * s), C['lime'], a, bev=2)

def art_crown(ctx, cx, cy, s=1., a=1.):
    carve(ctx, lambda: poly(ctx, [(-80, 50), (-90, -50), (-45, -10), (0, -70), (45, -10), (90, -50), (80, 50)], cx, cy, s), C['ochre'], a)
    for x in (-45, 0, 45):
        carve(ctx, lambda x=x: ell(ctx, cx + x * s, cy + 10 * s, 9 * s, 9 * s), C['terra'], a, bev=1)

def art_manuscript(ctx, cx, cy, s=1., a=1.):
    carve(ctx, lambda: rrect(ctx, cx - 96 * s, cy - 56 * s, 192 * s, 112 * s, 6 * s), C['clay'], a)
    carve(ctx, lambda: rrect(ctx, cx - 86 * s, cy - 46 * s, 82 * s, 92 * s, 4 * s), C['lime'], a, bev=2)
    carve(ctx, lambda: rrect(ctx, cx + 4 * s, cy - 46 * s, 82 * s, 92 * s, 4 * s), C['lime'], a, bev=2)
    for i in range(5):
        groove(ctx, lambda i=i: (ctx.move_to(cx - 74 * s, cy - 28 * s + i * 16 * s), ctx.line_to(cx - 16 * s, cy - 28 * s + i * 16 * s), ctx.move_to(cx + 16 * s, cy - 28 * s + i * 16 * s), ctx.line_to(cx + 74 * s, cy - 28 * s + i * 16 * s)), a, C['soot'], 3)

def art_sphere(ctx, cx, cy, s=1., a=1.):
    carve(ctx, lambda: ell(ctx, cx, cy, 80 * s, 80 * s), C['sandst'], a, bev=4)
    groove(ctx, lambda: ell(ctx, cx, cy, 80 * s, 28 * s), a, C['soot'], 3)
    groove(ctx, lambda: ell(ctx, cx, cy, 28 * s, 80 * s), a, C['soot'], 3)
    carve(ctx, lambda: ell(ctx, cx + 100 * s, cy + 70 * s, 18 * s, 18 * s), C['ochre'], a, bev=2)

def art_kudo(ctx, cx, cy, s=1.1, a=1.):
    art_pot(ctx, cx, cy, s * .9, a)

def art_helmet(ctx, cx, cy, s=1., a=1.):
    carve(ctx, lambda: (ctx.new_sub_path(), ctx.arc(cx, cy + 20 * s, 74 * s, math.pi, 2 * math.pi), ctx.close_path()), C['basalt'], a, grain=.1)
    carve(ctx, lambda: rrect(ctx, cx - 82 * s, cy + 16 * s, 164 * s, 16 * s, 4), C['ochre'], a)
    carve(ctx, lambda: rrect(ctx, cx - 5 * s, cy - 82 * s, 10 * s, 24 * s, 3), C['terra'], a, bev=2)

def art_chalice(ctx, cx, cy, s=1., a=1.):
    carve(ctx, lambda: poly(ctx, [(-60, -50), (60, -50), (40, 20), (-40, 20)], cx, cy, s), C['ochre'], a)
    carve(ctx, lambda: rrect(ctx, cx - 8 * s, cy + 18 * s, 16 * s, 44 * s, 2), C['ochre'], a, bev=2)
    carve(ctx, lambda: rrect(ctx, cx - 44 * s, cy + 60 * s, 88 * s, 14 * s, 4), C['ochre'], a)

def art_gate(ctx, cx, cy, s=1., a=1.):
    carve(ctx, lambda: rrect(ctx, cx - 80 * s, cy - 20 * s, 28 * s, 110 * s, 3), C['sandst'], a)
    carve(ctx, lambda: rrect(ctx, cx + 52 * s, cy - 20 * s, 28 * s, 110 * s, 3), C['sandst'], a)
    for k, w in enumerate((200, 180, 160)):
        carve(ctx, lambda k=k, w=w: rrect(ctx, cx - w / 2 * s, cy - (24 + k * 30) * s, w * s, 18 * s, 6 * s), C['sandst'], a, bev=2)

ART = {k[4:]: v for k, v in list(globals().items()) if k.startswith('art_')}

def draw_art(name, ctx, cx, cy, s=1., a=1.):
    ART.get(name, art_pot)(ctx, cx, cy, s, a)

# ---- glass case and the hall ----
def case(ctx, x, y, w, h, a=1., t=0.):
    """glass case (y = centre of the whole case) with plinth; art centre is case_art_y(y, h)"""
    gh = h * .78; top = y - h / 2
    carve(ctx, lambda: rrect(ctx, x - w / 2, top + gh, w, h - gh, 3), C['basalt'], a, bev=2)
    ctx.new_path(); rrect(ctx, x - w / 2, top, w, gh, 6); rgba(ctx, C['lime'], .06 * a); ctx.fill_preserve()
    rgba(ctx, C['lime'], .42 * a); ctx.set_line_width(3); ctx.stroke()
    ctx.move_to(x - w / 2 + 12, top + 10); ctx.line_to(x - w / 2 + 12 + w * .18, top + 10)
    rgba(ctx, (1, 1, 1), .35 * a); ctx.set_line_width(3); ctx.stroke()

def case_art_y(y, h): return y - h / 2 + h * .39

def art_shelter(ctx, cx, cy, s=1., a=1.):
    carve(ctx, lambda: poly(ctx, [(-110, 90), (-110, -10), (-70, -70), (0, -96), (70, -70), (110, -10), (110, 90), (60, 90), (60, 20), (-60, 20), (-60, 90)], cx, cy, s), C['basalt'], a, grain=.25)
    carve(ctx, lambda: poly(ctx, [(-40, 10), (-34, -22), (-8, -34), (24, -34), (38, -18), (34, 8)], cx, cy, s), C['terra'], a, bev=2)

def art_sickle(ctx, cx, cy, s=1., a=1.):
    def blade():
        ctx.new_sub_path(); ctx.move_to(cx - 70 * s, cy + 70 * s); ctx.curve_to(cx - 100 * s, cy - 60 * s, cx + 40 * s, cy - 100 * s, cx + 90 * s, cy - 20 * s)
        ctx.curve_to(cx + 20 * s, cy - 60 * s, cx - 40 * s, cy - 40 * s, cx - 50 * s, cy + 70 * s); ctx.close_path()
    carve(ctx, blade, C['basalt'], a, grain=.15)
    carve(ctx, lambda: rrect(ctx, cx - 76 * s, cy + 56 * s, 36 * s, 46 * s, 6), C['clay'], a, bev=2)

def art_quern(ctx, cx, cy, s=1., a=1.):
    carve(ctx, lambda: poly(ctx, [(-110, 30), (110, 30), (90, 74), (-90, 74)], cx, cy, s), C['basalt'], a, grain=.25)
    carve(ctx, lambda: ell(ctx, cx, cy + 20 * s, 54 * s, 24 * s), C['sandst'], a, bev=2)
    carve(ctx, lambda: ell(ctx, cx + 20 * s, cy - 14 * s, 40 * s, 22 * s), C['clay'], a, bev=2)

ART = {k[4:]: v for k, v in list(globals().items()) if k.startswith('art_')}
