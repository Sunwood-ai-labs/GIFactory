---
title: GIFactory
emoji: 🏢
colorFrom: red
colorTo: gray
sdk: docker
pinned: false
license: mit
---

<p align="center">
<img src="https://media.githubusercontent.com/media/Sunwood-ai-labs/GIFactory/main/docs/icon/icon3.gif" width="100%">
<br>
<h1 align="center">GIFactory</h1>
<h2 align="center">
  ～Where GIFs come to life～

[![GIFactory - Sunwood-ai-labs](https://img.shields.io/static/v1?label=GIFactory&message=Sunwood-ai-labs&color=blue&logo=github)](https://github.com/GIFactory/Sunwood-ai-labs "Go to GitHub repo")
[![stars - Sunwood-ai-labs](https://img.shields.io/github/stars/GIFactory/Sunwood-ai-labs?style=social)](https://github.com/GIFactory/Sunwood-ai-labs)
[![forks - Sunwood-ai-labs](https://img.shields.io/github/forks/GIFactory/Sunwood-ai-labs?style=social)](https://github.com/GIFactory/Sunwood-ai-labs)
[![GitHub Last Commit](https://img.shields.io/github/last-commit/Sunwood-ai-labs/GIFactory)](https://github.com/Sunwood-ai-labs/GIFactory)
[![GitHub Top Language](https://img.shields.io/github/languages/top/Sunwood-ai-labs/GIFactory)](https://github.com/Sunwood-ai-labs/GIFactory)
[![GitHub Release](https://img.shields.io/github/v/release/Sunwood-ai-labs/GIFactory?sort=date&color=red)](https://github.com/Sunwood-ai-labs/GIFactory)
[![GitHub Tag](https://img.shields.io/github/v/tag/Sunwood-ai-labs/GIFactory?color=orange)](https://github.com/Sunwood-ai-labs/GIFactory)



  <br>

</h2>

</p>

>[!IMPORTANT]
>このリポジトリは[SourceSage](https://github.com/Sunwood-ai-labs/SourceSage)を活用しており、リリースノートやREADME、コミットメッセージの9割は[SourceSage](https://github.com/Sunwood-ai-labs/SourceSage) ＋ [claude.ai](https://claude.ai/)で生成しています。



## 🎥 Introduction

GIFactoryは、動画ファイルからハイクオリティなGIFアニメーションを作成するためのシンプルで効率的なPythonプロジェクトです。MoviePyライブラリを活用し、動画の一部をGIFに変換する機能を提供します。簡単なインストールと直感的な使い方で、ユーザーはすぐにGIF作成を開始できます。

## 🎬 Demo

プロジェクトのデモ動画や作成したGIFサンプルを近日公開予定です。お楽しみに！

## 🚀 Getting Started

### Installation

1. リポジトリをクローンします：`git clone https://github.com/Sunwood-ai-labs/GIFactory.git`
2. 必要なライブラリをインストールします：`pip install -r requirements.txt`

### Usage

1. `example`フォルダに変換したい動画ファイルを配置します。
2. `gif_converter.py`を実行し、入力ファイル名と出力ファイル名を指定します。
   ```python
   python gif_converter.py example/input.mp4 example/output.gif
   ```
3. `example`フォルダにGIFファイルが生成されます。

### Customization

`gif_converter.py`の関数引数を変更することで、GIF作成の設定をカスタマイズできます：

- `fps`：GIFのフレームレート（デフォルト：10）
- `program`：使用するプログラム（'ImageMagick'または'ffmpeg'）（デフォルト：'ImageMagick'）
- `opt`：最適化オプション（ImageMagick: 'optimizeplus'または'OptimizeTransparency'）（デフォルト：'OptimizeTransparency'）
- `fuzz`：ImageMagickのfuzzオプションの値（デフォルト：5）

## 📈 Updates

- v1.0.0 (2023-04-22)：初回リリース。基本的なGIF変換機能を実装。

## 🤝 Contributing

GIFactoryプロジェクトへの貢献を歓迎します！バグ報告、機能要求、プルリクエストを通じて貢献いただけます。詳細は[CONTRIBUTING.md](CONTRIBUTING.md)をご覧ください。

## 📄 License

このプロジェクトは[MIT License](LICENSE)の下でライセンスされています。

## 🙏 Acknowledgements

GIFactoryの開発にあたり、以下のプロジェクトとライブラリに感謝します：

- [MoviePy](https://zulko.github.io/moviepy/)
- [ImageMagick](https://imagemagick.org/)
- [ffmpeg](https://ffmpeg.org/)