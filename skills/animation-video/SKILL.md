---
name: animation-video
description: "Produce programmatic animation videos (explainers, diagram/math animations, motion graphics, 3D) with the local toolchain in ~/workspace/animation-studio: Remotion (React to MP4), Manim, Three.js/Babylon.js, Anime.js and other JS animation libraries, Blender and Godot."
---

# Animation Video Production

Installed 2026-11-15 at the user's request. Everything lives in `~/workspace/animation-studio/`.

## When to use

- The user wants an animated video made from instructions: explainers, title cards, charts/graphs in motion, math or diagram animations, product promos, map animations, 3D scenes.
- For AI-generated (photorealistic or illustrative) video clips, the built-in media pipeline is a better fit. This skill is for code-driven, precisely editable animation.

## Toolchain (all verified working on 2026-11-15)

- **Remotion** (npm: remotion, @remotion/cli, react) — main route. Write React compositions in `src/`, render MP4 with the bundled Chrome Headless Shell.
  - Render: `cd ~/workspace/animation-studio && npx remotion render src/index.ts <CompositionId> out/<name>.mp4`
  - Stills: `npx remotion still src/index.ts <CompositionId> out/frame.png --frame=<n>`
  - Official Remotion Agent Skills are vendored at `references/remotion-skills/skills/` inside the studio folder; read `remotion-best-practices/SKILL.md` and the topic REFERENCE.md files before non-trivial Remotion work.
- **Manim Community v0.22.1** — math/diagram animation. Python venv at `.venv`.
  - Render: `cd ~/workspace/animation-studio/manim && ../.venv/bin/manim render -ql <file>.py <SceneName>` (use `-qm`/`-qh` for final quality). Japanese text works with the system Noto CJK fonts.
- **JS animation libraries** (npm, in the studio project): animejs, motion, shifty, @tweenjs/tween.js (successor of CreateJS TweenJS), ola, two.js, konva, lottie-web, gifenc (GIF export), three, @babylonjs/core, lume, @motion-canvas/core + @motion-canvas/2d (diagram animations; needs its own Vite project scaffold), proton-engine (particles).
  - These run inside Remotion compositions, standalone HTML/canvas pages rendered via the headless browser, or Node scripts (e.g. gifenc for GIF output).
- **GSAP 3.15.1** (npm: gsap, added 2026-11-17; fully free incl. all plugins) — timeline-driven animation for HTML/canvas compositions and standalone pages. In Node, import as `const { gsap } = require('gsap')`. Timeline logic verified headlessly (easing values check out); drive Remotion frames from `tl.progress(frame/durationInFrames)` or use it in browser-rendered pages.
- **React Three Fiber stack** (npm, added 2026-11-17; versions matched to the project's React 19 — fiber must stay on v9): @react-three/fiber 9.8.2, @react-three/drei 10.7.9 (helpers/environments), @react-three/rapier 2.2.0 (3D physics), @react-three/postprocessing 3.2.2 (bloom/DOF effects). Use inside Remotion compositions for real 3D scenes rendered frame-by-frame. Verified at import level only — these need a browser/WebGL context, so smoke-test in an actual render before promising output.
- **three.quarks 0.18.0** (npm) — GPU particle systems for three.js (fire, sparks, smoke, bursts as secondary-motion layers). Import verified (`ParticleSystem`, `ParticleEmitter`, …).
- **tweakpane 4.0.5** (npm) — parameter-tuning UI for interactive figure/animation pages; handy when iterating on timing/easing values with the user watching.
- **librosa 1.0.1** (Python, in `~/workspace/sidebiz-toolkit/.venv-ml`) — beat/onset detection for music-synced cuts and motion: `librosa.beat.beat_track(y, sr)` returns tempo + beat frames (verified on a synthetic 120 BPM click track). Use it to place scene changes and hits on real beats. Subtitle/transcription route stays openai-whisper in the same venv; whisperx was attempted on 2026-11-17 but its dependency chain tried to replace the working torch 2.15 with torch 2.8 (888 MB), so it was aborted on purpose — do not force it into this venv.
- **Blender 4.5.3 LTS** — `tools/blender/blender` (headless: `blender -b <file.blend> -a`). Heavy 3D and character animation. CPU-only on this VM, so keep renders small.
- **Godot 4.5.1** — `tools/godot-bin/Godot_v4.5.1-stable_linux.x86_64` (headless capable) for game-style animation and interactive scenes.

## Reference packs (vendored 2026-11-17 under `~/workspace/animation-studio/references/`)

Read for technique; their bundled scripts were reviewed as text only and are NOT installed or run — rebuild any needed idea in our own toolchain.

- `motion-design-skill/` (LottieFiles) — `skills/motion-design/SKILL.md` + `director/` (Disney principles, choreography, emotion mapping) + `reference/timing-easing-tables.md`. The timing/easing source of truth below.
- `hairline/` (lucasmarkes) — `skills/hairline-create/` and `skills/hairline-adopt/`: isometric single-stroke line figures built from rounded solids that react to the pointer; an idea or an SVG becomes one self-contained HTML figure.
- `anatomy/` (wheresryan22) — `SKILL.md` + `references/craft.md` / `motion.md`: interactive isometric SVG figures that explain a technical idea as a real physical machine (many small parts, four-tone shading, painter's order, geometry audits, exploded views).
- `anatomy-reveal/` (annnguyentt) — `SKILL.md` + `references/shots.md`: product exploded-view reveal films built from a part-by-part model of a real object. The beat sheet in `shots.md` is the template for reveal videos.

## Motion design principles (distilled from the packs above)

- **Never linear for spatial movement.** Entrances decelerate (ease-out family), exits accelerate (ease-in), on-screen moves use ease-in-out. Signature curves: MD3 standard cubic-bezier(0.2,0,0,1), MD3 emphasized (0.05,0.7,0.1,1), Apple HIG (0.25,0.1,0.25,1), bounce-settle (0.175,0.885,0.32,1.275). Pick ONE signature easing + a 3-step duration palette (quick/standard/slow) per project and stay consistent.
- **Duration scales with element and distance.** Micro-feedback 80–180ms, cards 200–350ms, modals 300–400ms, page/context changes 400–600ms, dramatic reveals 600–1200ms. Entrances run 30–50% longer than exits; longer travel distance = longer duration (100px base, ×1.3 at 200px, ×1.6 at 400px). For video, scale these up proportionally but keep the ratios.
- **Three motion layers or it looks flat**: primary action, secondary richness (shadows, icons, follow-through), ambient life (subtle background motion). Add Disney basics: anticipation before the move, follow-through/overshoot after it, squash-and-stretch for playful personalities, arcs instead of straight lines.
- **Choreography**: hero enters first and biggest; everything enters from a consistent direction; stagger delays 20–100ms per element with the TOTAL stagger under 500ms; never more than 1/3 of elements in active motion at once, and no single move crosses more than 1/3 of the screen without a keyframe change.
- **One figure, one idea** (hairline): explain with geometry, not labels — if a label is needed, the concept isn't ready. The rest pose is the thumbnail: compose it like one. A guided tour is a sentence, not an inventory: ~3 stops that each show a different answer.
- **The object is the explanation** (anatomy): when explaining a system, invent a real physical machine whose mechanism IS the concept, built from many small true parts (screws, springs, rails, gauges), shaded in tones, painted back-to-front. Detail must be purposeful parts, never noise.
- **Exploded-view / reveal workflow** (anatomy + anatomy-reveal): model the object part-by-part from real dimensions first; explode along the real assembly axes with outer parts leading and staggered spring easing, hold the apart pose with a slow drift, then snap back. Film rhythm (10s default): tumble-in → whip (~0.24s, heavy motion blur) to a macro detail → hold while one feature actually works → more detail beats → pull out → explode (ease-out) → hold apart → implode → hero shot. When retiming, whips keep their length; holds stretch.

## Stock assets

- **Openverse API** (`https://api.openverse.org/v1/`) — keyless search for CC-licensed audio and images (verified 2026-11-17: `GET /v1/audio/?q=click` answers without a key and returns license/creator fields per result). Anonymous limits are tight: 20 requests/min burst, 200/day sustained — cache results, batch queries, and always record the license + creator for attribution. Good for sound effects (clicks, whooshes) to layer under motion.

## Workflow

1. Clarify only what changes the result: purpose, length, aspect (16:9 default; 9:16 for Shorts/Reels), text/language, deadline feel.
2. Pick the route: Remotion for most things, Manim for math/diagrams, Blender/Godot only when real 3D is needed.
3. Build the composition/scene, render a short preview or stills first when the design is uncertain, then the full render.
4. Deliver the MP4 as an attachment in chat. Keep sources in the studio folder so revisions are cheap: edit code, re-render.

## Limits

- VM has ~1.5 shared CPUs and limited RAM: 1080p Remotion renders of a few minutes are fine; long or 3D-heavy renders are slow. Prefer 720p drafts, confirm, then render final.
- First Remotion render in a fresh environment needs `npx remotion browser ensure` (downloads ~100 MB Chrome Headless Shell; the egress proxy occasionally stalls it — retry once).
- Do not claim a render finished from the command starting; verify the output file exists and probe its duration with ffprobe.
