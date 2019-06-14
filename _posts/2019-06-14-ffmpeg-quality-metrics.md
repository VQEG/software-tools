---
title:  ffmpeg-quality-metrics
excerpt: Calculate quality metrics with FFmpeg (SSIM, PSNR, VMAF)
author: Werner Robitza
license: MIT
tags: python windows macos linux video open-source
category: "Quality Analysis"
external_link: https://github.com/slhck/ffmpeg-quality-metrics
---

Simple script for calculating quality metrics with FFmpeg.

Currently supports PSNR, SSIM and VMAF.

Requirements:

- Python 3.6
- FFmpeg:
    - download a static build from [their website](http://ffmpeg.org/download.html))
    - put the `ffmpeg` executable in your `$PATH`

Optionally, you may install FFmpeg with `libvmaf` support to run VMAF score calculation:

- Install [Homebrew](https://brew.sh/)
- Install [this tap](https://github.com/varenc/homebrew-ffmpeg/)
- Run `brew install ffmpeg --with-libvmaf`.

Installation

    pip install ffmpeg_quality_metrics