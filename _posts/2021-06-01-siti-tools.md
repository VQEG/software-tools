---
title:  siti-tools
excerpt: Calculate spatial information (SI) and temporal information (TI) with Python
author: Werner Robitza, Lukas Krasula, Cosmin Stejerean
license: MIT
tags: windows macos linux python open-source
category: "Quality Analysis"
external_link: https://github.com/VQEG/siti-tools
direct_download_link: https://github.com/VQEG/siti-tools/archive/refs/heads/main.zip
---

A command-line-based tool to calculate spatial information (SI) and temporal information (TI) according to ITU-T P.910.

Developed under the Video Quality Expert Group (VQEG) No-Reference Metrics (NORM) working group.

Features:

- Supports 8-bit and higher bit-depth content (10-bit, 12-bit)
- Handles full and limited color ranges
- HDR support (HLG and HDR10)
- Available as both CLI and Python API
- Outputs JSON or CSV with per-frame values and aggregated statistics

Requirements:

- Python 3.10.1 or higher
- FFmpeg libraries (v5 or higher)

Install:

    pip3 install siti-tools
