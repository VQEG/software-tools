---
title:  ffmpeg-black-split
excerpt: Split videos based on black frame detection
author: Werner Robitza
license: MIT
tags: python windows macos linux open-source
category: "Helper Tools"
external_link: https://github.com/slhck/ffmpeg-black-split
---

Split videos based on black frame detection using FFmpeg's blackdetect filter.

Features:

- Detects black periods in videos
- Cuts videos into segments at black frame boundaries
- JSON output with black and content period timestamps
- Customizable detection thresholds
- Stream-copy mode (fast, no re-encoding) or re-encoding options
- CLI and Python API available

Requirements:

- Python 3.9+
- FFmpeg in system PATH

Installation:

    pip3 install ffmpeg-black-split
