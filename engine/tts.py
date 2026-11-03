import wave, json, re, io, sys
import numpy as np
from piper import PiperVoice
from piper.config import SynthesisConfig

def run(beats, voice_path):
    v = PiperVoice.load(voice_path)
    cfg = SynthesisConfig(length_scale=1.22, noise_scale=0.55, noise_w_scale=0.7)
    SR = v.config.sample_rate
    def synth(t):
        b = io.BytesIO()
        with wave.open(b, "wb") as w: v.synthesize_wav(t, w, syn_config=cfg)
        b.seek(0)
        with wave.open(b) as w: return np.frombuffer(w.readframes(w.getnframes()), np.int16)
    durs = {}; marks = {}
    for i, (k, txt) in enumerate(beats):
        out = []; mk = []; n = 0; pos = 0
        toks = re.split(r'(\[\[\d+(?:\.\d+)?\]\])', txt)       # [[3]] = 3 s of silence (countdowns)
        for tok in toks:
            m = re.fullmatch(r'\[\[(\d+(?:\.\d+)?)\]\]', tok)
            if m:
                out.append(np.zeros(int(SR * float(m.group(1))), np.int16)); n += int(SR * float(m.group(1))); pos += len(tok); continue
            for p in [p for p in re.split(r'(?<=[.?!:])\s+', tok) if p]:
                cs = txt.index(p, pos); pos = cs + len(p)
                a = synth(p)
                nz = np.where(np.abs(a) > 300)[0]
                if len(nz): a = a[max(0, nz[0]-800): nz[-1]+1600]
                ts = n / SR; out.append(a); n += len(a)
                mk.append([cs, ts, pos, n / SR])
                gap = np.zeros(int(SR*(0.55 if p.endswith(('.', '?', '!')) else 0.35)), np.int16)
                out.append(gap); n += len(gap)
        a = np.concatenate(out)
        with wave.open(f"vo/{i:02d}_{k}.wav", "wb") as w:
            w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(a.tobytes())
        durs[k] = len(a)/SR; marks[k] = mk
    json.dump(durs, open("vo/durs.json", "w"), indent=1); json.dump(marks, open("vo/marks.json", "w"))
    print(SR, round(sum(durs.values()), 1))
