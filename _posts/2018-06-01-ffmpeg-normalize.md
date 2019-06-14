---
title:  ffmpeg-normalize
excerpt: Audio normalization script for Python/ffmpeg
author: Werner Robitza
license: MIT
tags: python windows macos linux audio open-source
category: "Helper Tools"
external_link: https://github.com/slhck/ffmpeg-normalize
---

This program normalizes media files to a certain LUFS level using the EBU R128 loudness normalization procedure. It can also perform RMS-based normalization (where the mean is lifted or attenuated), or peak normalization to a certain target level.

Batch processing of several input files is possible, including video files.

Install Python (2.7 or 3.x), then install the program with:

    pip install ffmpeg-normalize