---
title:  PcapLossGenerator
excerpt: Generate packet loss in PCAP files
author: AGH University
license: unknown
tags: linux windows macos c++ open-source
categories: Streaming
direct_download_link: ftp://intecftp.intec.ugent.be/vqeg/jeg/tools/PcapLossGenerator.zip
---

Installation process:

You need to run cmake from build directory:

    PcapLossGenerator/build$ cmake ..

Then from the same directory, you should run:

    PcapLossGenerator/build$ make

and to install it globally:

    PcapLossGenerator/build$ sudo make install