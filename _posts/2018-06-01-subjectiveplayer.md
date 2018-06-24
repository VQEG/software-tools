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

* play an indefinitely long list of MPEG-4 AVC (H.264) coded videos, either in .mp4 or .3gpp format
* after each video ask the user for their opinion using a certain methodology
* record a user ID so as to identify the test person later
* log the user opinion to text files