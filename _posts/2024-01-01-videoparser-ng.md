---
title:  videoparser-ng
excerpt: High-performance video bitstream parser for quality assessment
author: AVEQ GmbH, Werner Robitza, Jonatan Stenlund
license: LGPL-2.1
tags: macos linux c++ open-source
category: "Quality Analysis"
external_link: https://github.com/aveq-research/videoparser-ng
direct_download_link: https://github.com/aveq-research/videoparser-ng/releases
---

A command-line and API-based video bitstream parser for extracting detailed metrics from video files.

Supported codecs:

- H.264 / AVC
- H.265 / HEVC
- VP9
- AV1

Features:

- Up to 16x speedup over legacy parsers on HEVC, up to 70x on 4K videos
- Extracts QP values, motion vectors, and frame metadata
- Line-delimited JSON output format
- Both CLI and C++ API available

Requirements:

- Ubuntu 22.04+ or macOS 12.0+
- Docker images also available

Installation:

Pre-built binaries available on the releases page, or run via Docker:

    docker pull ghcr.io/aveq-research/videoparser-ng
