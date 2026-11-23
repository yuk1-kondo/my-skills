---
name: mimo-narration
description: ゆうきちゃん専用のナレーション担当。Xiaomi MiMo V2.5 TTS API で音声を生成する。「いつもの声で読んで」「ナレーションを作って」と言われたらこのスキルの声レジストリと手順で生成する。声の追加・使い分けルールの更新もここを編集する。
---

# MiMo Narration — 専属ナレーション担当

Set up 2026-11-19 from @gagarot200's post: give the agent the tool, the reference
voices, and the rules for which voice to use when — as a skill, so narration is
one request away ("いつもの声で、この原稿を読んで").

## Tool

Xiaomi MiMo V2.5 TTS (official docs: mimo.mi.com, speech-synthesis-v2.5).
OpenAI-compatible API at `https://api.xiaomimimo.com/v1`. **Billing: 限时免费
(free for a limited time) as of 2026-11-19 — re-check the console billing page
before heavy use; the promotion can end.**

Helper: `bin/mimo_tts.py` (key injected from connection `custom.xiaomi-mimo`,
never stored in files).

| Mode | Model | How |
|---|---|---|
| Preset voice | `mimo-v2.5-tts` | `--voice <id>` |
| Voice design | `mimo-v2.5-tts-voicedesign` | `--design "声の説明文"` |
| Voice clone | `mimo-v2.5-tts-voiceclone` | `--clone-sample <mp3/wav>` (base64 ≤ 10 MB) |

Call rules (from the docs, easy to get wrong):
- Text to synthesize goes in the **assistant** message; style instruction or
  voice-design description goes in the **user** message. The helper does this.
- Style can also be steered inline with tags in the text, e.g. `(唱歌)`, emotion
  tags like `(慵懒)`, and `[音频标签]` insertions for breaths/pauses/laughs.
- Preset voices: Chinese — 冰糖 (F), 茉莉 (F), 苏打 (M), 白桦 (M); English —
  Mia (F), Chloe (F), Milo (M), Dean (M); `mimo_default`. **No Japanese preset
  voice exists.** Japanese text quality is unverified until the first real call
  — test with a short Japanese script before committing to a long narration.

## Voice registry （声の一覧と使い分け）

Fill this in as ゆうきちゃん provides voices. When he names a voice, resolve it
here first; when a scene matches a rule, pick that voice without asking.

| 呼び名 | 種別 | Voice ID / 参照音声 | 使い分け（どんな場面で） |
|---|---|---|---|
| （未登録） | | | ゆうきちゃんから参考音声と名前をもらったら追加する |

Preset defaults available immediately: mimo_default（既定）, plus the CN/EN
presets above — fine for tests, not "his" voices.

## Workflow

1. Resolve the voice from the registry (name or scene rule). If unspecified and
   a default voice is registered, use it; otherwise ask once.
2. Run `bin/mimo_tts.py --text "<原稿>" --out <path>.wav` with the mode flags
   for that voice. Long scripts: split by paragraph/scene and generate per
   chunk, then join with ffmpeg.
3. Verify the output (ffprobe duration; listen-check impossible — report the
   file and duration). Deliver the wav (and an mp3 copy for chat playback when
   useful: `ffmpeg -i out.wav out.mp3`).
4. New voice? Add a row to the registry: name, mode, voice id or sample path
   under `voices/`, and the usage rule in ゆうきちゃん's words.
