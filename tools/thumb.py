#!/usr/bin/env python3
"""Designed thumbnail (1280x720): the exhibit in lamplight and a big engraved title. No caption box, no corner tag.
usage: python3 tools/thumb.py NN"""
import os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, ROOT)
import cairo
from engine import core, stone, museum, anc, plan
from engine.core import W, H, C

def make(n, out):
    num, title, short, period, art, label = plan.BY_EP[n]
    S = cairo.ImageSurface(cairo.FORMAT_ARGB32, 1280, 720); c = cairo.Context(S); c.scale(1280 / W, 720 / H)
    stone.bg_stone(c, 0.); stone.lamp(c, 1400, 520, 900, .55)
    c.save(); stone.lamp(c, 1420, 540, 600, .5)
    museum.draw_art(art, c, 1420, 520, 3.0, 1.); c.restore()
    def wrap_at(size):
        core.font(c, size, True, True); lines, cur = [], ''
        for w in title.split():
            t_ = (cur + ' ' + w).strip()
            if c.text_extents(t_).x_advance > 840 and cur: lines.append(cur); cur = w
            else: cur = t_
        lines.append(cur); return lines, max(c.text_extents(l).x_advance for l in lines)
    size = 128
    while size > 64:
        lines, wd = wrap_at(size)
        if len(lines) * size * 1.1 <= 470 and wd <= 840: break
        size -= 8
    lines, wd = wrap_at(size)
    y = 440 - (size * 1.1) * (len(lines) - 1) / 2 + size * .35
    for l in lines:
        stone.etext(c, l, 90, y, size, C['lime'], 1., 'l'); y += size * 1.1
    stone.etext(c, 'ANCIENT INDIA · EP %d' % n, 96, 110, 40, C['sandst'], 1., 'l')
    S.write_to_png(out)

if __name__ == '__main__':
    n = int(sys.argv[1]); os.makedirs(os.path.join(ROOT, 'output/youtube'), exist_ok=True)
    make(n, os.path.join(ROOT, f'output/youtube/Anc{n:02d}_thumb.png'))
