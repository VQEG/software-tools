---
title:  SubjectivePlayer
excerpt: A video player for Android, allowing Subjective Quality Assessment
author: Werner Robitza
license: GNU General Public License v3
tags: android open-source
category: "Subjective Test Software"
external_link: https://github.com/slhck/SubjectivePlayer
---

There are quite a few tools around that exist for traditional PCs, mostly Windows-based, which show videos or still images to test persons and ask them to rate the respective video or image quality. Such tools adhere to the ITU recommendations on subjective evaluation of audio and video and have been used for a long time. The hardware that should be used is described precisely, and so are the testing procedures.

Because the context of usage in mobile multimedia is totally different from the good old desktop PC at home, these ITU test recommendations do not really fit perfectly. We tried to come up with a simple and easy solution to present videos on an Android device and record the subjective opinion of viewers. Of course, when possible, ITU recommendations were followed or reinterpreted for mobile usage.

SubjectivePlayer for Android can:

* play videos encoded with H.264, H.265/HEVC, VP9, VP8, and AV1 codecs in MP4, WebM, MKV, and 3GP containers
* provide edge-to-edge playback, utilizing the full screen or avoiding display cutouts
* ask the user for their opinion using various methodologies:
  * 5-point ACR scale (Excellent/Good/Fair/Poor/Bad) following ITU-T standards
  * continuous slider-based ratings (0–100)
  * experimental DSIS impairment scale and real-time volume button ratings
* record a participant ID to identify the test person later
* support playlist-based video sequencing for different users
* include training sessions and break management
* log results to CSV files with timestamps
* support multiple languages (English and German)

Requirements: Android 7.0 (API level 24) or higher.