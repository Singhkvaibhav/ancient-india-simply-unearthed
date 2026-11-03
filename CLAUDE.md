# Ancient India, Simply Unearthed: video production

This repo makes 44 five-minute animated explainers covering UPSC Ancient Indian History, from the Stone Age to the Rajput kingdoms. It's for the same channel as "Indian Polity, Simply Drawn", "Geography, Simply Mapped" and "Modern History, Simply Told" (each in its own repo).

**This series has a different look from the other three.** They are bright paper cut-outs. This one is **carved stone and terracotta relief in a lamp-lit museum**. Keep the channel's calm pace, narrator and caption style, but don't reuse the paper look, the paper town, or any other series' signatures.

- Episode list, exhibits and status: `scripts/episode_plan.md`
- Format sample (the approved style): `scripts/sample_ep04.md`
- Scripts: `scripts/unitN_scripts.md`
- Episode code: `episodes/epNN/ep.py`
- Finished files: `output/`

## Rules that matter most
1. **Never render a unit before the user approves its scripts.** Write the unit's script file, commit and push it, tell the user it's ready, and **stop and wait** for a message saying it's approved. The only exception is Episode 4, the format sample, which you render as the test episode when the user asks.
2. **Approved narration is used word for word.** If you spot a factual problem in an approved script, flag it; don't silently change it.
3. **Religious founders and revered figures** (the Buddha, Mahavira, the Tirthankaras, deities) are **never shown as faces or figures**. Show them through symbols, as early Indian art did: footprints, an empty throne, the Bodhi tree, a dharma wheel, a stupa, a lotus. Rulers and other people are simple carved figures with nameplates, with no real likenesses.
4. **Don't draw the State Emblem** (the Sarnath lion capital), because its use is restricted by law. The Ashoka episode uses the Rampurva bull capital.
5. **Maps:** never draw national or state boundaries, an outline of India, or ancient kingdoms as shaded territories. Show capitals and sites as labelled pins on a schematic physical board (rivers, coasts, ranges). Every map carries "Schematic · not to scale · boundaries not shown".
6. **Sensitive debates** (the Aryan question, the origins of caste, conflicts between religious traditions, the feudalism debate): present the main scholarly views neutrally on the "Scholars disagree" plaque, giving each equal space. Don't take sides.
7. **Dates:** use "about" or "c." for uncertain dates, BCE/CE throughout, and the most common textbook date where sources differ, with a "Fact check:" note.
8. **Commit only code and finished output.** Run `git status` before every commit. Never commit `vo/`, `parts/`, `.wav`, stills, logs or `*.part.mp4`.
9. **Be economical.** The user is on a usage budget. Check 3–4 stills per episode, render with two background workers, wait with a single `until` loop, and don't narrate progress.

## The engine (already built, from the Polity series)
- `engine/core.py`: palette `C`, easing, `text`, `label`, `caption`, timeline helpers, and the paper drawing helpers (`paper`, backgrounds, props). `SERIES` and `SERIES_TITLE` at the top are already set to Ancient India.
- `engine/templates.py`: `scene(bg, *layers)`, `TL`, `GRID`, `LIST`, `TIPS`, `MAINS`, `HOOK`, `END`, `FIG`, and other layouts
- `engine/runner.py`: `Episode` (timeline, caption chunks, render loop); `engine/cli.py`: the per-episode command line
- `engine/audiomix.py`: the mix (voice, pad, sound effects, SRT); `engine/tts.py`: narration
- `engine/town.py` and `engine/units.py` are the Polity town. Don't use them.
- `tools/`: helpers from earlier series (`run_ep.sh`, `render_ep.sh`, `sheet.sh`, `qa.py`, `youtube_meta.py`). Adapt them first: output names `AncNN_<Title>.mp4` and `AncNN.srt`, episode range 1–44, series name and hashtags for Ancient India.

An episode is one `ep.py` file with `EP`, `TITLE`, `NAME`, `BEATS=[(id, narration, scene)]`, `CAPTIONS` and optional `EXTRA`, run from inside `episodes/epNN/` with `python3 ../../engine/cli.py tts|tl|still|render|audio|check`. `reference/polity_example_ep59.py` shows a complete episode in this format. Keep that structure, the timeline, the captions and the render loop.

## First task: build the new look
Put everything new in `engine/stone.py` (drawing style and backgrounds), `engine/anc.py` (scene templates) and `engine/museum.py` (the gallery and exhibits). Don't change the paper helpers other series depend on.

1. **`carve(ctx, path, col)`**, the relief equivalent of `paper()`. Fill the shape, then clip to it and draw a light bevel (lighter tint, about 3 px) along the top-left edges and a dark bevel along the bottom-right, so the shape looks carved. Add a subtle stone-grain texture: a pre-generated noise tile at low opacity, generated once and cached, never per frame. No drop shadows.
2. **Backgrounds:** `bg_stone` (a dark basalt wall with soft grain and a warm pool of lamplight, and an off-centre vignette), `bg_museum` (a gallery hall: dark walls, a floor line, lamp glows, glass cases), and `bg_trench` (a soil cross-section with layered strata).
3. **Palette** (add to `C`): limestone `EFE7DA`, sandstone `E0C49A`, terracotta `A8492A`, ochre `C9973A`, river clay `8B6B4A`, basalt `3A3A3F`, soot `2B2622`. **Verdigris `4FA39A` is used only for the inscription tip.** Text on dark backgrounds is limestone; captions keep the channel's light caption box for readability.
4. **Fonts:** headings in DejaVu Serif Bold (like engraved lettering), body and captions in Inter.
5. **Sound:** in `audiomix.py`, add a soft drone (a low, slowly breathing tone on one root note with its fifth, like a tanpura bed) used in place of the piano pad, plus a `chisel` effect (short, bright taps) for the inscription and a soft `thud` when the exhibit is placed. Keep everything well below the narration.
6. **Check:** render 3 stills (one each on stone, museum and trench backgrounds) and look at them before building any episode.

## Episode format (exactly 300 s)
| Time | Segment | Template |
| --- | --- | --- |
| 0:00–0:20 | The Dig: a lamp-lit soil trench; a brush reveals the episode's artefact; one question | DIG |
| 0:20–0:35 | How do we know?: source tags for the evidence this topic rests on | SOURCES |
| 0:35–2:20 | The Frieze: the story as one long carved relief panel that pans slowly sideways, scene by scene | FRIEZE |
| 2:20–2:50 | The Plaque: "Old name, new name" or "Scholars disagree" | PLAQUE |
| 2:50–3:20 | Inscription: the memory tip | INSCRIPTION |
| 3:20–4:30 | Dig Quiz: three artefacts, "Pause and name it", 3-2-1, answer; then one Mains line | QUIZ |
| 4:30–5:00 | The Gallery: the exhibit placed in its case; museum label with three facts and "Next gallery: …" | GALLERY |

Narration is about 480–600 words per episode (the sample has about 490), so everything fits in 300 s with calm pauses. A thin **timeline ribbon** runs along the top of every scene except the title: a BCE/CE line with a marker for the period being discussed (pass the period per episode, for example `(-2600, -1900)`).

## Scene templates (in `engine/anc.py` and `engine/museum.py`)
- **DIG:** `bg_trench`. A brush sweeps across in a few strokes, and soil particles fade to reveal the artefact, carved in relief. Optional small tags (site, year of discovery).
- **SOURCES:** five carved icons in a row: trowel ("dug up"), palm leaf ("texts"), inscribed stone ("inscriptions"), coin ("coins"), traveller's staff ("travellers' accounts"). The ones relevant to the episode light up with a warm glow, and the rest stay dim. Optional one-line note under an icon.
- **FRIEZE:** one long horizontal relief panel, about 4–6 screen widths long, built from that episode's scenes left to right. The camera pans so each scene is centred while its narration plays, with an ease between scenes. Scenes are simple carved vignettes: buildings, figures with nameplates, objects, rivers, labels carved into the stone border. The panel's top and bottom borders carry a repeating carved motif (lotus or bead-and-reel).
- **PLAQUE:** either one plaque with two names joined by an arrow ("Pataliputra → Patna"), or two carved tablets under "Scholars disagree" with one interpretation each, always the same size and level.
- **INSCRIPTION:** a stone tablet; a chisel taps the tip in letter by letter (with chisel sounds), then the grooves fill with verdigris green and glow softly. Up to three short lines.
- **QUIZ:** a carved artefact card rises with "Pause and name it" and a 3-2-1 countdown ring, then the answer is carved in beneath. Three cards per episode, then a small Mains card with one line.
- **GALLERY:** `bg_museum`. The episode's exhibit is placed in a glass case with a soft thud, and exhibits from earlier episodes stay in their cases along the hall, so the museum fills across the series. A museum label (cream card, serif heading) shows three facts, then "Next gallery: …". Each exhibit is its own small function in `museum.py`. The final episode is a slow walk past every case.
- **TIMELINE RIBBON:** a thin carved band at the top; years labelled at sensible intervals; a small lamp-glow marker at the episode's period.

## Writing scripts for a unit
1. Write `scripts/unitN_scripts.md` in exactly the format of `sample_ep04.md`. That means a header line (Inscription tip · Sources lit · Timeline ribbon · Plaque · Exhibit · Label facts), then a Time | Segment | Visual | Narration table following the seven segments.
2. Every episode has a memory tip in the Inscription row, a plaque (old name, new name, or scholars disagree), and three real, unambiguous answers in the Dig Quiz.
3. Stick to standard textbook facts (NCERT level). Where textbooks differ on a date or figure, use the most common version and add a "Fact check:" note under the episode.
4. Commit and push the script file, tell the user, and **stop** (rule 1). They may approve only some episodes. Update the Status column in `episode_plan.md` as you go.

## Delivering each episode
- `output/AncNN_<Short_Title>.mp4` and `output/AncNN.srt`
- `output/youtube/AncNN.txt` (title, description, chapters) and `AncNN_thumb.png`: a designed thumbnail with the exhibit in lamplight and a big engraved title, **without** the caption box or corner tag
- 1920×1080, 30 fps, `libx264 -preset veryfast -crf 20`, yuv420p, AAC 192k, `-movflags +faststart`
- Commit and push each finished episode as soon as it's ready. If you work on a branch, keep one open pull request and tell the user the branch name.

## Setup notes
- Run `bash setup.sh` once. It installs pycairo, piper-tts and numpy, and downloads the narrator voice from **GitHub releases** to `voice/`. Hugging Face is usually blocked, so don't try it.
- The voice model is 16 kHz; the audio mix resamples it to 44.1 kHz.
- Use the same narrator voice as the other series, so the channel sounds consistent.
- Lessons from earlier test episodes: keep labels clear of pins and markers, make the recurring world (here, the museum) a main visual and not a small inset, make sure on-screen numbers match the narration exactly, and make thumbnails as designed images, not video frames.
