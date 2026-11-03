#!/usr/bin/env python3
"""YouTube text for an episode: output/youtube/AncNN.txt (title, description with chapters, tags). usage: python3 tools/yt.py NN"""
import os, re, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, ROOT)
from engine import plan
LAB = dict(dig='The Dig', sources='How do we know?', frieze='The Frieze', plaque='The Plaque', inscription='Memory inscription', quiz='Dig Quiz', gallery='The Gallery')
def stamp(s): return f"{int(s//60)}:{int(s%60):02d}"
n = int(sys.argv[1]); nn = f'{n:02d}'; d = os.path.join(ROOT, 'episodes', f'ep{nn}')
out = subprocess.run(['python3', '../../engine/cli.py', 'tl'], cwd=d, capture_output=True, text=True).stdout
rows = [l.split() for l in out.splitlines() if re.match(r'^\d+ ', l)]
title = plan.BY_EP[n][1]
desc = [f"Episode {n} of Ancient India, Simply Unearthed: a calm five-minute animated explainer on {title} for UPSC aspirants (NCERT level).", "", "Chapters:"]
desc += [f"{stamp(0 if i == 0 else float(r[2]))} {LAB.get(r[1], r[1])}" for i, r in enumerate(rows)]
desc += ["", "Carved-stone relief in a lamp-lit museum. Dates are approximate (c.), BCE/CE.", "", "#UPSC #AncientIndia #IndianHistory #NCERT #CivilServices"]
os.makedirs(os.path.join(ROOT, 'output/youtube'), exist_ok=True)
open(os.path.join(ROOT, f'output/youtube/Anc{nn}.txt'), 'w').write(f"Title: Ancient India, Simply Unearthed · Episode {n}: {title}\n\n" + "\n".join(desc) + "\n")
