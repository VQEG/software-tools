---
title:  ffmpeg-debug-qp
excerpt: FFmpeg Debug Script for QP Values
author: Werner Robitza, Steve Göring, Pierre Lebreton
license: MIT
tags: python windows macos linux video open-source
category: "Quality Analysis"
external_link: https://github.com/slhck/ffmpeg-debug-qp
---

Prints QP values of input sequence on a per-frame basis.

Supported input:

- MPEG-2
- MPEG-4 Part 2
- H.264 / MPEG-4 Part 10 (AVC)

Supported formats:

- MPEG-4 Part 14
- H.264 Annex B bytestreams

To run the tool:

    ./ffmpeg_debug_qp test.mp4

The output will be as follows:

    ...
    [h264 @ 0x7fcf61813e00] nal_unit_type: X, nal_ref_idc: X
    [h264 @ 0x7fcf61813e00] New frame, type: X
    [h264 @ 0x7fcf61813e00] AABBCCDD...

Where in the above, AA is the QP value of the first macroblock, BB of the second, etc.
For every macroblock row, there will be another row printed per frame.

You can parse the values with the `parse-qp-output.py` script, e.g.

    $ ./ffmpeg-debug-qp test.mp4 2> qp-values.txt
    $ ./parse-qp-output.py qp-values.txt qp-values.ldjson

This produces a newline-delimited JSON file that is easier to parse. Each line contains one frame.
