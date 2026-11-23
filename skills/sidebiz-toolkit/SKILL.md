---
name: sidebiz-toolkit
description: "Local toolkit in ~/workspace/sidebiz-toolkit for content production workflows (research → write → video → voice → publish): yt-dlp, MarkItDown, Marp slides, Crawl4AI, Whisper, F5-TTS, MoneyPrinterTurbo, ComfyUI code, plus vendored Agent Skill packs (anthropics/skills, obra/superpowers, wshobson/agents)."
---

# Side-Business Content Toolkit

Installed 2026-11-15 from the user's request (a 14-tool list post; grok_x_search and Remotion Skills from the same list live in their own skills). Everything lives in `~/workspace/sidebiz-toolkit/`.

## Verified working

- **yt-dlp** 2026.10.26 — `.venv/bin/yt-dlp`. Download video/audio from supported sites. Respect site terms and copyright; download only what the user is entitled to.
- **MarkItDown** 0.1.9 — `.venv/bin/markitdown <file>` or the Python API. Converts PDF/Word/Excel/PowerPoint/HTML/images to Markdown. Conversion test passed.
- **Marp CLI** v4.5.1 — `npx marp` in the toolkit folder (or `node_modules/.bin/marp`). Markdown → slides (HTML/PDF/PPTX). PDF/PPTX export uses the bundled Chromium.
- **MoneyPrinterTurbo** — code at `apps/MoneyPrinterTurbo/`, deps installed in its own `.venv` (streamlit, moviepy, edge-tts, faster-whisper verified importable). Generates short videos from a topic, but **needs API keys to run** (an LLM key and a stock-footage key such as Pexels, set in its config.toml). Do not start it until the user provides keys via Secure Vault.

## Vendored reference packs (read, don't execute blindly)

- `packs/skills/` — anthropics/skills: official Agent Skills (docx, pdf, pptx, xlsx, frontend-design, skill-creator, webapp-testing, etc.). Consult the relevant SKILL.md when doing document/design work.
- `packs/superpowers/` — obra/superpowers: working-method skills (brainstorming, writing-plans, systematic-debugging, TDD, verification-before-completion...). Consult when planning or debugging substantial work.
- `packs/agents/` — wshobson/agents: large agent/skill collection. Reference only.

## ML tools (`.venv-ml`, installed 2026-11-15)

- **Whisper (openai-whisper 20250625)** — `.venv-ml/bin/whisper`. End-to-end verified: tiny model transcribed the JFK test speech perfectly. CPU-only: tiny/base/small are usable, large models are slow.
- **F5-TTS 1.1.22** — `.venv-ml/bin/f5-tts_infer-cli` (help verified). Voice-cloning TTS; model weights download from Hugging Face on first run. Short clips only on CPU. Source code also at `apps/F5-TTS/`.
- **Crawl4AI 0.9.5** — `.venv-ml/bin/crawl4ai` (import verified). Playwright browsers (chromium-1255 + headless shell + ffmpeg) were placed manually in `~/.cache/ms-playwright` via curl because the node downloader stalls through the egress proxy. BUT live crawling from this VM does not work: the egress proxy rejects Chromium's CONNECT tunnels (`ERR_TUNNEL_CONNECTION_FAILED`) even with proxy auth, while curl works fine. Use Muse's built-in browser tools for scraping; Crawl4AI becomes usable if the network policy changes or on another host (e.g. Simular Box).
- torch in `.venv-ml` is 2.15.0+cu132 (pulled in by f5-tts) but runs CPU-only here; whisper works with it.
- Install lesson: this VM's `/tmp` is a 512MB tmpfs — big pip installs die with Errno 28 while unpacking large wheels (e.g. triton). Always run pip with `TMPDIR=~/workspace/sidebiz-toolkit/.tmp`. Large wheels download more reliably with curl than through pip's proxy path.

## Pending / limited

- **ComfyUI** — code only at `apps/ComfyUI/` (master branch). Runtime deps and model checkpoints (multiple GB) are NOT installed; CPU-only generation on this VM is impractically slow. Install on demand only if the user accepts that.
- **Firecrawl** — not installed: it is a hosted API service (self-hosting needs a Docker stack). If the user wants it, get an API key via Secure Vault and call the API directly. The browser tools already cover most scraping needs.

## Related skills

- `animation-video` (~/workspace/animation-studio) for Remotion/Manim video production.
- `grok_x_search` for X search via Grok (sign-in may still be pending on Simular Box).
