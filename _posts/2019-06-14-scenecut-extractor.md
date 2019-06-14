---
title:  scenecut-extractor
excerpt: Extract scenecuts from video files using ffmpeg
author: Werner Robitza
license: MIT
tags: python windows macos linux video open-source
category: "Helper Tools"
external_link: https://github.com/slhck/scenecut-extractor
---

This tool uses the [`select` filter](http://ffmpeg.org/ffmpeg-filters.html#select_002c-aselect) from ffmpeg to determine the scene cut probability of adjacent frames, and allows users to determine which frames (or at which timestamps) the scene cuts happen.

Requirements

- Python 2.7 or 3.x
- FFmpeg:
    - download a static build from [their website](http://ffmpeg.org/download.html))
    - put the `ffmpeg` executable in your `$PATH`

Installation

    pip install scenecut_extractor