---
name: colab-gpu
description: Borrow a cloud GPU through Google Colab (operated in the browser) for heavy work Muse's own VM cannot do — Blender/Cycles rendering, image/video generation models, fine-tuning, large transcription. Uses the user's Google AI plan Colab compute units when available, or the free tier (T4) otherwise.
---

# Colab GPU (borrowed compute via Google Colab)

Prepared 2026-11-18 from @tetumemo's post (Muse operating Colab to render 750 frames on an A100).

## When to use

- Blender Cycles rendering beyond a few frames (local Blender 4.5.3 in `~/workspace/animation-studio` is CPU-only here; this VM has no GPU).
- GPU model work: image/video generation (ComfyUI etc.), Whisper large, fine-tuning, embeddings at scale.

## Facts (verified 2026-11-18 against Google's plan pages and third-party measurements)

- Since 2026-09-22, paid Google AI plans include monthly Colab compute units (CCU): Plus 50, **Pro 200**, **Ultra 1,000 / 2,000** (5x / 20x). Ultra also gets Premium GPU access and background execution. Benefits apply automatically to the same Google account; check balance in Colab: Settings -> Subscription.
- **Free trials are excluded** from the CCU benefit. A ¥0 trial of Ultra does NOT come with units. The free Colab tier (T4, dynamic limits) still works for anyone signed in.
- Burn rates are per connected hour and vary; third-party measurements: T4 ~1.15 CCU/h, L4 ~1.94, A100 ~8.88 (so Pro's 200 CCU ≈ 22 h of A100). A100 allocation is not guaranteed, especially on Pro; it depends on capacity.
- Runtimes disconnect when idle and have max lifetimes; units burn while connected — always disconnect when done. Results left only in `/content` are lost when the runtime dies: save outputs to Drive.

## MCP route (preferred — added 2026-11-19, from @gota_bara's post + Google's official announcement)

Google announced the Colab API + hosted MCP endpoint on 2026-11-16/17. This replaces browser driving for most work:

- Endpoint: `https://colaboratory.googleapis.com/mcp` (verified live 2026-11-19: unauthenticated `tools/list` answers; tools include create_runtime / list_runtimes / list_runtime_specs / get_subscription / create_session / execute_code).
- Auth: every tool call needs an OAuth access token with scope `https://www.googleapis.com/auth/colaboratory`. Practical route: the official **Colab CLI** (`pip install google-colab-cli`) — `colab --auth oauth2 …` runs a public InstalledAppFlow login in the browser and saves a refreshable token at `~/.config/colab-cli/token.json`.
- A **quota project** is also required: a Google Cloud project the user owns with the Colaboratory API enabled, sent as the `x-goog-user-project` header. His existing Gemini/AI Studio project may serve; otherwise create a free project.
- Prepared state (2026-11-19): Colab CLI installed on the MacBook Pro at `~/colab-mcp/.venv` (Python 3.14 venv — the MBP's default python3 is 3.9 and cannot install the package). Token stays on the MBP; drive the MCP client over SSH so credentials never move to this VM.
- Remaining user steps: (1) run the CLI login once on the MBP and approve in the browser as yukilab.m@gmail.com; (2) enable the Colaboratory API in a GCP project he owns.
- The trial exclusion still applies: his Ultra trial ended 2026-11-18, so expect free-tier runtimes (T4-class, availability permitting) unless he holds a paid AI plan.

## Operating procedure (browser, fallback)

1. Use `browser.browse` on `https://colab.research.google.com`. The user signs in with their Google account themselves (login agent / secure entry) — never ask for or handle their password or codes beyond the standard sign-in flow.
2. Upload or open the notebook (starter: `~/workspace/colab-gpu/blender_render_test.ipynb`). To upload: Colab welcome screen -> Upload tab -> the notebook file (pass it via the browser task's `files`).
3. Runtime -> Change runtime type -> GPU (pick the strongest available the task justifies; A100 only when the job is big).
4. Run cells in order; watch for errors (missing libs, OOM) and adapt: reduce tile/sample/resolution, or switch GPU type.
5. Get results out: mount Drive in the notebook and copy outputs to `MyDrive/ColabOutput/`, then pull them with the Google Drive connector; or download through the browser if small.
6. Runtime -> Disconnect and delete runtime to stop unit burn. Report units/time used when visible.

## Blender on Colab recipe

- Install: `apt-get install libxrender1 libxi6 libxkbcommon0 libgl1 libsm6`, then the official `blender-4.5.3-linux-x64.tar.xz` from download.blender.org, extract under `/content`.
- Run headless: `blender -b --python scene.py`.
- In the script, enable GPU before rendering: cycles preferences `compute_device_type = 'CUDA'` (works on T4/L4/A100), `get_devices()`, set every device `use = True`, `scene.cycles.device = 'GPU'`.
- The starter notebook in `~/workspace/colab-gpu/` implements all of this for a 1-frame test; extend it for real scenes/animations (frame range + zip frames to Drive).

## Limits and care

- One browser window = one Colab session; long renders need the session kept alive (Ultra's background execution relaxes this when available).
- Do not burn the user's units on exploratory runs without saying so first; a 1-frame or few-second test render comes before any full-length job, with an estimate.
- Respect Colab's acceptable-use rules (no crypto mining, no deepfakes, etc.).
