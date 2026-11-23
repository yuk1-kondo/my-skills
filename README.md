# my-skills

個人用の Agent Skills 集。SKILL.md のオープン仕様（Agent Skills）で書き、Devin / Codex / Claude Code / Muse など対応エージェントで共通利用する。正本はこのリポジトリ。

## スキル一覧

| スキル | 概要 | 前提・移植性 |
|---|---|---|
| animation-video | Remotion / Manim / Blender 等でプログラム的に動画を作る | Muse VM の `~/workspace/animation-studio` 前提 |
| colab-gpu | Google Colab の GPU を借りて重い処理を回す | ブラウザ操作部は Muse 前提。Colab CLI 部は MBP でも可 |
| grok-x-search | Grok Build CLI の x_search で X の投稿を検索 | Grok Build CLI とサインインが必要 |
| mimo-narration | Xiaomi MiMo TTS でナレーション音声を生成 | MiMo API キーが必要（Muse ではコネクタ経由） |
| multi-machine-device-work | 複数マシン・実機が絡む作業の前に場所と接続先を確認する | 汎用、そのまま使える |
| sidebiz-toolkit | コンテンツ制作ローカルツールキットの使い方 | Muse VM の `~/workspace/sidebiz-toolkit` 前提 |
| verify-checkable-claims | 確認可能な事実は一次情報で確かめてから述べる | 汎用、そのまま使える |
| x-reddit-research | X は Weir、Reddit は Arctic Shift で読む | Arctic Shift は認証不要で汎用。Weir は API キーが必要 |

## 導入

まとめて入れる（グローバル）:

```
npx skills add yuk1-kondo/my-skills -a codex -a devin -a claude-code -g
```

Devin にはプラグインとしても入る:

```
devin plugins install yuk1-kondo/my-skills
```

## 更新の流れ

1. このリポジトリで編集して commit / push
2. 各エージェント側で `npx skills update`（Devin プラグインなら `devin plugins update my-skills`）。symlink で導入した分は clone の pull で反映される

## ルール

- API キーなどの秘密情報はスキル内に書かない
- frontmatter は `name` / `description` の最小構成を保つ（エージェント固有フィールドは解釈が割れるので避ける）
- 常時効かせたい指示は Skills ではなく AGENTS.md に書く
- Muse の `~/workspace/custom-skills` はこのリポジトリの同期コピー。`skill.yaml` は Muse 側でのみ管理し、このリポジトリには含めない
