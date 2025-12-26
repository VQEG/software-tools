---
title:  ffmpeg-debug-qp
excerpt: Extract QP values from video files on a per-frame, per-macroblock basis
author: Werner Robitza, Steve Göring, Pierre Lebreton, Nathan Trevivian, Valerio Triolo
license: MIT
tags: python macos linux video open-source
category: "Quality Analysis"
external_link: https://github.com/slhck/ffmpeg-debug-qp
direct_download_link: https://github.com/slhck/ffmpeg-debug-qp/releases
---

Extracts quantization parameter (QP) values from video files on a per-frame, per-macroblock basis.

Supported codecs:

- MPEG-2
- MPEG-4 Part 2
- H.264 / AVC

Features:

- Multiple output formats (JSON, line-delimited JSON, CSV)
- Optional macroblock-level metadata extraction
- Static binary builds with embedded FFmpeg available

Requirements:

- Python 3.9+
- FFmpeg 8.x or higher libraries

Installation:

    pip3 install ffmpeg-debug-qp

Pre-built static binaries for Linux and macOS (x86_64, ARM64) are available on the releases page.
