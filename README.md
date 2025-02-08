# God Is Saying

プロジェクト「God Is Saying」へようこそ。

[English version below](#english)

## 概要

この Python アプリケーションは、指定された動画や音声からメッセージを抽出・解析するためのツールです。

## インストール方法

```bash
git clone https://github.com/your-username/god-is-saying.git
cd god-is-saying
pip install -e .
```

## 使用方法

```bash
python -m god-is-saying-lol
```

## プロジェクト構造

```
god-is-saying/
├── god-is-saying-lol/     # メインパッケージ
│   ├── __init__.py
│   └── __main__.py
├── tests/                 # テストスイート
├── video/                 # 入力動画ファイル用ディレクトリ
├── output/               # 出力ファイル用ディレクトリ
└── build/                # ビルド成果物
```

## 開発

テストの実行:

```bash
python -m pytest tests/
```

---

<a name="english"></a>

# God Is Saying

Welcome to the God Is Saying project.

## Overview

This Python application is a tool for extracting and analyzing messages from specified video and audio content.

## Installation

```bash
git clone https://github.com/your-username/god-is-saying.git
cd god-is-saying
pip install -e .
```

## Usage

```bash
python -m god-is-saying-lol
```

## Project Structure

```
god-is-saying/
├── god-is-saying-lol/     # Main package
│   ├── __init__.py
│   └── __main__.py
├── tests/                 # Test suite
├── video/                 # Directory for input video files
├── output/               # Directory for output files
└── build/                # Build artifacts
```

## Development

To run tests:

```bash
python -m pytest tests/
```
