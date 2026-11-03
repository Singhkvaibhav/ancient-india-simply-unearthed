"""Carved-stone drawing style and backgrounds for Ancient India, Simply Unearthed.
carve() is the relief equivalent of paper(): fill, clip, light bevel top-left, dark bevel bottom-right, cached grain."""
import math, random
import cairo
import numpy as np
from engine.core import *

_GRAIN = None
_BGC = {}

def mix(a, b, x): return tuple(a[i] + (b[i] - a[i]) * x for i in range(3))
def lighter(c, x=.35): return mix(c, (1, 1, 1), x)
def darker(c, x=.45): return mix(c, (0, 0, 0), x)

def grain_pattern():
    """noise tile generated once, never per frame"""
    global _GRAIN
    if _GRAIN is None:
        rng = np.random.default_rng(11)
        n = rng.random((256, 256)).astype(np.float32)
        n = (n + np.roll(n, 1, 0) + np.roll(n, 1, 1)) / 3
        g = (np.clip((n - .5) * 3.2 + .5, 0, 1) * 255).astype(np.uint8)
        buf = np.zeros((256, 256, 4), np.uint8)
        buf[..., 0] = g; buf[..., 1] = g; buf[..., 2] = g; buf[..., 3] = 255
        surf = cairo.ImageSurface.create_for_data(bytearray(buf.tobytes()), cairo.FORMAT_ARGB32, 256, 256)
        pat = cairo.SurfacePattern(surf); pat.set_extend(cairo.EXTEND_REPEAT)
        _GRAIN = (pat, surf)
    return _GRAIN[0]

def carve(ctx, path, col, a=1., bev=3, grain=.13):
    """fill the shape, clip to it, grain + light bevel on the top-left + dark bevel on the bottom-right. No drop shadow."""
    if a <= 0: return
    ctx.save()
    ctx.new_path(); path(); rgba(ctx, col, a); ctx.fill_preserve()
    ctx.clip()
    ctx.set_source(grain_pattern()); ctx.paint_with_alpha(grain * .5 * a)
    for d, c, al in ((bev, lighter(col), .85), (-bev, darker(col), .8)):
        ctx.save(); ctx.translate(d, d); ctx.new_path()
        ctx.rectangle(-60, -60, W + 120, H + 120); path()
        ctx.set_fill_rule(cairo.FILL_RULE_EVEN_ODD); rgba(ctx, c, al * a); ctx.fill(); ctx.restore()
    ctx.restore()

def groove(ctx, path, a=1., col=None, w=3):
    """a thin incised line"""
    if a <= 0: return
    ctx.new_path(); path(); ctx.set_line_width(w); rgba(ctx, col or C['soot'], .55 * a); ctx.stroke()

def etext(ctx, s, x, y, size, col, a=1., align='c', bold=True, serif=True):
    """engraved lettering: dark below-right, light above-left"""
    if a <= 0: return
    text(ctx, s, x + 2, y + 2, size, darker(col, .7), .5 * a, bold, align, serif)
    text(ctx, s, x, y, size, col, a, bold, align, serif)

def lamp(ctx, x, y, r, a=1., col=(1., .72, .38), t=0.):
    fl = 1 + .05 * math.sin(t * 7.3 + x) + .03 * math.sin(t * 11.1)
    g = cairo.RadialGradient(x, y, 4, x, y, r * fl)
    g.add_color_stop_rgba(0, *col, .55 * a); g.add_color_stop_rgba(.4, *col, .18 * a); g.add_color_stop_rgba(1, *col, 0)
    ctx.set_source(g); ctx.arc(x, y, r * fl, 0, 2 * math.pi); ctx.fill()

def _vignette(ctx, cx=W * .46, cy=H * .5, a=.62):
    g = cairo.RadialGradient(cx, cy, 380, cx, cy, 1250)
    g.add_color_stop_rgba(0, 0, 0, 0, 0); g.add_color_stop_rgba(1, .02, .01, 0, a)
    ctx.set_source(g); ctx.paint()

def _cached(name, build):
    if name not in _BGC:
        s = cairo.ImageSurface(cairo.FORMAT_ARGB32, W, H); c = cairo.Context(s); build(c); _BGC[name] = s
    return _BGC[name]

def _blit(ctx, surf):
    ctx.set_source_surface(surf, 0, 0); ctx.paint()

def _grad(c, top, bot):
    g = cairo.LinearGradient(0, 0, 0, H); g.add_color_stop_rgb(0, *top); g.add_color_stop_rgb(1, *bot)
    c.set_source(g); c.paint()

def _stone_base(c):
    _grad(c, darker(C['basalt'], .25), darker(C['basalt'], .55))
    rng = random.Random(5)
    for _ in range(26):           # faint dressed-block joints
        y = rng.randrange(0, H, 120)
    for y in range(0, H, 150):
        rgba(c, C['soot'], .35); c.rectangle(0, y, W, 3); c.fill()
        off = 0 if (y // 150) % 2 == 0 else 180
        for x in range(-off, W, 360):
            c.rectangle(x, y, 3, 150); c.fill()
    c.set_source(grain_pattern()); c.paint_with_alpha(.16)

def bg_stone(ctx, t=0.):
    """dark basalt wall, warm pool of lamplight, off-centre vignette"""
    def build(c):
        _stone_base(c)
        g = cairo.RadialGradient(W * .42, H * .38, 20, W * .42, H * .38, 900)
        g.add_color_stop_rgba(0, 1, .68, .34, .30); g.add_color_stop_rgba(.5, 1, .62, .3, .10); g.add_color_stop_rgba(1, 1, .6, .3, 0)
        c.set_source(g); c.paint(); _vignette(c)
    _blit(ctx, _cached('stone', build))
    lamp(ctx, W * .42, H * .38, 640, .22, t=t)

def bg_museum(ctx, t=0.):
    """gallery hall: dark walls, floor line, lamp glows, glass cases behind"""
    def build(c):
        _grad(c, darker(C['soot'], .3), C['basalt'])
        c.set_source(grain_pattern()); c.paint_with_alpha(.10)
        for x in range(120, W, 330):         # wall panels
            rgba(c, C['soot'], .45); c.rectangle(x, 120, 6, 640); c.fill()
        fy = 800
        g = cairo.LinearGradient(0, fy, 0, H); g.add_color_stop_rgb(0, *darker(C['clay'], .55)); g.add_color_stop_rgb(1, *darker(C['clay'], .8))
        c.set_source(g); c.rectangle(0, fy, W, H - fy); c.fill()
        rgba(c, C['ochre'], .5); c.rectangle(0, fy, W, 3); c.fill()
        for x in range(-100, W + 200, 240):  # floor planks in perspective
            rgba(c, C['soot'], .4); c.move_to(x, fy); c.line_to(x - (x - W / 2) * .5, H); c.set_line_width(2); c.stroke()
        _vignette(c, W / 2, 420, .55)
    _blit(ctx, _cached('museum', build))
    for x in (330, 960, 1590):
        lamp(ctx, x, 150, 520, .30, t=t)

def bg_trench(ctx, t=0.):
    """soil cross-section with layered strata"""
    def build(c):
        _grad(c, darker(C['clay'], .55), darker(C['soot'], .1))
        cols = [C['clay'], C['sandst'], C['ochre'], C['terra'], C['clay'], C['basalt'], C['sandst']]
        y = 150
        for i, col in enumerate(cols):
            hgt = 120 + (i % 3) * 40
            c.move_to(0, H)
            c.line_to(0, y)
            for x in range(0, W + 41, 40):
                c.line_to(x, y + 14 * math.sin(x * .007 + i * 1.7) + 7 * math.sin(x * .021 + i))
            c.line_to(W, H); c.close_path()
            rgba(c, darker(col, .32 + .04 * i), 1); c.fill()
            rgba(c, lighter(col, .2), .25); c.set_line_width(3)
            c.move_to(0, y)
            for x in range(0, W + 41, 40):
                c.line_to(x, y + 14 * math.sin(x * .007 + i * 1.7) + 7 * math.sin(x * .021 + i))
            c.stroke()
            y += hgt
        rng = random.Random(9)
        for _ in range(180):                  # pebbles and sherds
            x, yy = rng.uniform(0, W), rng.uniform(170, H)
            rgba(c, lighter(C['clay'], rng.uniform(0, .5)), .35)
            c.save(); c.translate(x, yy); c.scale(rng.uniform(4, 13), rng.uniform(3, 8)); c.arc(0, 0, 1, 0, 2 * math.pi); c.restore(); c.fill()
        rgba(c, darker(C['soot'], .3), 1); c.rectangle(0, 0, W, 150); c.fill()          # dark sky above the trench
        rgba(c, C['clay'], .9); c.rectangle(0, 140, W, 14); c.fill()
        c.set_source(grain_pattern()); c.paint_with_alpha(.18)
        g = cairo.RadialGradient(W / 2, 560, 20, W / 2, 560, 760)
        g.add_color_stop_rgba(0, 1, .7, .35, .32); g.add_color_stop_rgba(1, 1, .6, .3, 0)
        c.set_source(g); c.paint(); _vignette(c, W / 2, 560, .66)
    _blit(ctx, _cached('trench', build))
    lamp(ctx, W / 2, 560, 560, .18, t=t)
