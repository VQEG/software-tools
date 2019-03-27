---
title:  PSIAP-DL-YouTube-CC
excerpt: Download Creative Commons videos from a YouTube channel
author: MIT Lincoln Laboratory
license: BSD 2-Clause License
tags: python open-source youtube
category: "Helper Tools"
external_link: https://github.com/mit-ll/PSIAP-DL-YouTube-CC
direct_download_link: https://github.com/mit-ll/PSIAP-DL-YouTube-CC/archive/master.zip
---

This python script downloads all Creative Commons licensed videos for a given YouTube channel. Downloads are saved to `FILEPATH/{video_id}.{ext}`, where `{video_id}` is the YouTube id of the video, and `{ext}` is the filetype extension. The metadata is also stored in `FILEPATH/{video_id}.info.json` as a JSON file. An additional utility file at `FILEPATH/dl_status` keeps track of the download status, and an informational file about the channel is stored at `FILEPATH/channel_summary.json`.