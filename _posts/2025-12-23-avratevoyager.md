---
title:  AVrate Voyager
excerpt: Web-based Framework for Crowdsourced Quality Assessment
author: Technische Universität Ilmenau
license: GNU General Public License v3
tags: python web docker open-source
category: "Subjective Test Software"
external_link: https://github.com/Telecommunication-Telemedia-Assessment/AVrateVoyager
direct_download_link: https://github.com/Telecommunication-Telemedia-Assessment/AVrateVoyager/archive/master.zip
---

AVrate Voyager is an online-based framework for conducting image, video, and audio quality assessment testing through web browsers. Participants rate stimuli presented in a browser interface while responses are stored in a database.

Key features include web-based stimulus presentation and rating collection, configurable questionnaires for participant background information, support for training phases before actual testing, multiple rating templates (ACR scale, multi-slider), and a basic statistics dashboard for test monitoring. The framework uses Docker-based deployment and includes development tools for video/audio preprocessing.

AVrate Voyager is built upon avrateNG for rating functionality and bottle_docker_kit for containerization. The framework requires specific video encoding (H.264, 4:2:0 8-bit) for browser compatibility.
