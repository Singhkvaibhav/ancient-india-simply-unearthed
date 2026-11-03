# Ancient India, Simply Unearthed

44 five-minute animated explainers on UPSC Ancient Indian History: carved stone and terracotta relief in a lamp-lit museum.
See `CLAUDE.md` for the production rules, `scripts/episode_plan.md` for the plan, `engine/` for the renderer (stone look in `stone.py`, scenes in `anc.py`, exhibits in `museum.py`).

    bash setup.sh                 # once: pycairo, piper-tts, numpy, narrator voice
    bash tools/run_ep.sh 4        # tts, render, audio, mux, thumbnail, metadata -> output/
