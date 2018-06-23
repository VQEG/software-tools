---
title:  Modified JM H.264/AVC Codec
excerpt: Adjusted JM Reference software to generate traces
author: unknown
license: unknown
tags: c++ h264
category: Encoding
direct_download_link: ftp://intecftp.intec.ugent.be/vqeg/jeg/tools/jm_16.1_xmltrace_v1.5.zip
---

Version 16.1 of the JM Reference software has been adjusted in order to enable the generation of an XML-based trace file. This file contains detailed information concerning the encoded H.264 bit stream. The trace file is generated during the decoding process. Changes have been made to the following source files for enabling the trace file generation:

    ldecod/src/image.c
    ldecod/src/ldecod.c
    ldecod/src/macroblock.c
    ldecod/src/mbuffer.c
    ldecod/src/output.c
    ldecod/src/parset.c
    ldecod/inc/global.h
    ldecod/inc/mbuffer.h

Changes made for trace file generation are placed between a '/***** XML_TRACE_BEGIN ****/' and a '/****** XML_TRACE_END *****/' comment line. In addition, some new files are needed which simplify the creation of the XML trace file. These files are located in the ldecod/xmltracefile/src and the ldecod/xmltracefile/inc directories.

## Tracefile overview

Currently, the following information is extracted during the decoding process and stored in the trace file (version 1.5):

For every non-picture (NALU type >= 6)

* NAL unit information

NAL unit information:

* Num - NAL unit number according to position in the bit stream
* Type - NALU type as defined in Table 7-1 of ITU-Rec. H.264
* TypeString - String identifying NALU type (Redundant information)
* Length - Size of the NALU in bytes

In case of an SPS NALU (NALU type = 7), the following fields are literally outputted:

* `pic_width_in_mbs_minus1`
* `pic_height_in_map_units_minus1`
* `frame_mbs_only_flag`
* `frame_cropping parameters:`
* `frame_crop_left_offset`
* `frame_crop_right_offset`
* `frame_crop_top_offset`
* `frame_crop_bottom_offset`

* VUI parameters with timing information (if available):

* num_units_in_tick
* time_scale
* fixed_frame_rate_flag

For every picture:

* id
* poc - Picture Order Count
* GOPNr - GOP number to which this picture belongs
* SubPicture information (Represents frame or field data. In case of interlaced content, each picture contains two elements for the top and bottom field.)

For every subpicture:

* structure - integer indicating whether the subpicture contains frame or field data (0 = frame data, 1 = top field data, 2 = bottom field data)
* Slice information

For every slice:

* num
* Type - Slice type as defined in Table 7-6 of ITU-Rec. H.264
* TypeString - String identifying the slice type (Redundant information)
* NAL unit information - Note: this information can occur up to three times in case of data partitioning
* Macroblock information

For every macroblock:

* num
* QP_Y
* Type - Macroblock type as defined in tables 7-11, 7-12, 7-13 and 7-14 of ITU-Rec. H.264
* TypeString - String identifying the macroblock type (Redundant information)
* PredModeString - String identifying the macroblock prediction mode (I, SI, P or B)
* SkipFlag - true if the current macroblock is a P_SKIP or a B_SKIP
* Position - X and Y coordinate (in pixels) of the current macroblock
* MotionVector information or Submacroblock information (in case of B_8x8 or P_8x8 macroblock)
* Coefficients

For every submacroblock:

* num
* Type - Submacroblock type as defined in tables 7-17 and 7-18 of ITU-Rec. H.264
* TypeString - String identifying the submacroblock type (Redundant information)
* MotionVector information

For every motion vector:

* list - list 0 or list 1 prediction
* RefIdx - index in reference picture list of the reference picture to be used for prediction
* Difference - horizontal and vertical motion vector component difference
* Absolute - horizontal and vertical motion vector component

The structure of the XML trace file is also described in the XSD schema file `AVCTrace.xsd`.

When using a configuration file for decoding the video sequence (see below), it is possible to limit the XML
trace file generation depth by setting the XML trace log level variable. Possible values are:

    0 => trace up to Slice and NAL header
    1 => add Macroblock info
    2 => add SubMacroblock info
    3 => add MotionVector info
    4 => add Coefficients

## Usage

Command line interface:

```
ldecod.exe [-s] -i <input>.264 -o <output>.yuv [-r <orig>.yuv] [-xmltrace <tracefile>.xml]
-s silent decode    ommit unnecessary information during decoding (optional)
-i <input>.264  encoded bitstream to decode
-o <output>.yuv output filename for the decoded bitstream
-r <orig>.yuv   original decoded file (for PSNR computation) (optional)
-xmltrace <tracefile>.xml   filename for the XML tracefile (optional)
WARNING: this command line interface can only be used when no concealment must be performed
```

## Configuration file

Must be used in case error concealment must be performed

    ldecod.exe config.cfg

A sample configuration file is located in `ldecod/xmltracefile/doc/decod.cfg`

## Error concealment

In order for the error concealment to work correctly, two parameters need to be set in the config file: 'Err Concealment' (should be set to 1) and 'Reference POC gap' (2: IPP (Default), 4: IbP / IpP, ...) Currently, the error concealment only works in case of a fixed GOP size and structure.
It is also possible to conceal the corrupted stream based on the encoder log created during encoding with the JM reference software. This way, perfect error concealment can be achieved. The path to the encoder log must be specified at the end of the configuration file.
A sample configuration file is located in `ldecod/xmltracefile/doc/decod_with_enctrace.cfg`