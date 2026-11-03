"""Run one episode defined in ./ep.py (EP, TITLE, NAME, BEATS=[(id, narration, scene_fn)], CAPTIONS, EXTRA).
usage (inside episodes/epNN): python3 ../../engine/cli.py tts <voice.onnx> | tl | still <beat> <t> <out.png> | render <i,j,..> | audio | check"""
import importlib.util, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
HERE = os.getcwd()
spec = importlib.util.spec_from_file_location('ep', os.path.join(HERE, 'ep.py'))
ep = importlib.util.module_from_spec(spec); spec.loader.exec_module(ep)
from engine.runner import Episode
beats = [(k, n) for k, n, _ in ep.BEATS]
scenes = {k: f for k, _, f in ep.BEATS}
bg = {k: f.bg for k, _, f in ep.BEATS}
extra = dict(dig=1.5, quiz=4.0, gallery=3.0); extra.update(getattr(ep, 'EXTRA', {}))
E = Episode(ep.EP, HERE, beats, getattr(ep, 'CAPTIONS', {}), scenes, bg, extra, nocap=(), chunk_caps=True)
cmd = sys.argv[1]
if cmd == 'tts':
    from engine import tts; os.makedirs('vo', exist_ok=True); tts.run(beats, sys.argv[2])
elif cmd == 'audio':
    from engine.audiomix import build
    from engine import anc
    fx = []
    if 'inscription' in scenes:
        fx += [('chisel', 'inscription', x) for x in anc.chisel_times(ep.TIP_LINES)]
    if 'gallery' in scenes:
        fx += [('thud', 'gallery', getattr(ep, 'PLACE_AT', 1.5))]
    build(E.timeline(), fx, f'ep{ep.EP:02d}.srt')
elif cmd == 'check':
    import cairo
    from engine.core import W, H
    tl = E.timeline(); bad = 0
    surf = cairo.ImageSurface(cairo.FORMAT_ARGB32, W, H); ctx = cairo.Context(surf)
    for i, b in enumerate(tl):
        for tt in (2.0, b['D']/2, b['D']-1):
            try:
                E.frame(ctx, b, tt, bg[b['k']], bg[b['k']])
            except Exception as e:
                bad += 1; print('FAIL', b['k'], round(tt, 1), repr(e)); break
    print('check', 'FAILED' if bad else 'ok', len(tl), 'beats'); sys.exit(1 if bad else 0)
else:
    E.main([sys.argv[0]] + sys.argv[1:])
