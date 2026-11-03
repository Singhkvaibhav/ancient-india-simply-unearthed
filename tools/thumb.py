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
    stone.bg_stone(c, 0.); stone.lamp(c, 1360, 520, 900, .55)
    c.save(); stone.lamp(c, 1360, 540, 600, .5)
    museum.draw_art(art, c, 1360, 540, 3.2, 1.); c.restore()
    words = title.split(); lines, cur = [], ''
    core.font(c, 128, True, True)
    for w in words:
        t = (cur + ' ' + w).strip()
        if c.text_extents(t).x_advance > 1000 and cur: lines.append(cur); cur = w
        else: cur = t
    lines.append(cur)
    y = 520 - 70 * (len(lines) - 1)
    for l in lines[:4]:
        stone.etext(c, l, 90, y, 128, C['lime'], 1., 'l'); y += 140
    stone.etext(c, 'ANCIENT INDIA · EP %d' % n, 96, 150, 40, C['sandst'], 1., 'l')
    S.write_to_png(out)

if __name__ == '__main__':
    n = int(sys.argv[1]); os.makedirs(os.path.join(ROOT, 'output/youtube'), exist_ok=True)
    make(n, os.path.join(ROOT, f'output/youtube/Anc{n:02d}_thumb.png'))
