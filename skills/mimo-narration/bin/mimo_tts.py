#!/usr/bin/env python3
"""MiMo TTS helper — synthesize narration with Xiaomi MiMo V2.5 TTS.

The API key is never stored here; it is injected at call time from the
registered connection `custom.xiaomi-mimo` via dynamic_credentials.

Usage:
  # preset voice
  mimo_tts.py --text "原稿テキスト" --out out.wav --voice mimo_default [--style "明るく元気に"]
  # designed voice (text description becomes the user message)
  mimo_tts.py --text "原稿テキスト" --out out.wav --design "落ち着いた低音の男性ナレーター"
  # cloned voice (reference sample: mp3/wav, base64 must stay <= 10 MB)
  mimo_tts.py --text "原稿テキスト" --out out.wav --clone-sample voices/sample.mp3 [--style "..."]

Rules from the official docs:
  - the text to synthesize goes in the `assistant` message
  - style instruction / voice design goes in the `user` message
  - output audio is base64 in choices[0].message.audio.data
"""
import argparse
import base64
import json
import sys
import urllib.request

sys.path.insert(0, "/opt/muse/skills/custom-connector-setup/bin")
from dynamic_credentials import add_surrogate_to_request, read_json_response

API_URL = "https://api.xiaomimimo.com/v1/chat/completions"
PROVIDER = "custom.xiaomi-mimo"


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args):
        raise RuntimeError("redirect refused, verify the endpoint")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--text", required=True, help="text to synthesize (assistant message)")
    ap.add_argument("--out", required=True, help="output wav path")
    ap.add_argument("--voice", default="mimo_default", help="preset voice id (preset mode)")
    ap.add_argument("--style", default="", help="natural-language style instruction")
    ap.add_argument("--design", default="", help="voice design description (voicedesign mode)")
    ap.add_argument("--clone-sample", default="", help="reference audio path (voiceclone mode)")
    args = ap.parse_args()

    if args.clone_sample:
        model = "mimo-v2.5-tts-voiceclone"
    elif args.design:
        model = "mimo-v2.5-tts-voicedesign"
    else:
        model = "mimo-v2.5-tts"

    user_content = args.design if args.design else args.style
    messages = [
        {"role": "user", "content": user_content},
        {"role": "assistant", "content": args.text},
    ]

    audio = {"format": "wav"}
    if model == "mimo-v2.5-tts":
        audio["voice"] = args.voice
    elif model == "mimo-v2.5-tts-voiceclone":
        with open(args.clone_sample, "rb") as f:
            raw = f.read()
        mime = "audio/mpeg" if args.clone_sample.lower().endswith(".mp3") else "audio/wav"
        audio["voice"] = "data:{};base64,{}".format(mime, base64.b64encode(raw).decode())

    body = {"model": model, "messages": messages, "audio": audio}
    request = urllib.request.Request(
        API_URL,
        data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    add_surrogate_to_request(request, PROVIDER, allowed_hosts=["api.xiaomimimo.com"])
    with urllib.request.build_opener(NoRedirect()).open(request, timeout=300) as response:
        payload = read_json_response(response)

    data = payload["choices"][0]["message"]["audio"]["data"]
    with open(args.out, "wb") as f:
        f.write(base64.b64decode(data))
    print(json.dumps({"ok": True, "model": model, "out": args.out}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
