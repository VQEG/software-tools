---
title:  MATLAB Code for Subject Screening
excerpt: Popular subject screening techniques implemented in MATLAB
author: Austin Mivshek, Margaret Pinson, Institute for Telecommunication Sciences, NTIA
license: For any purpose
tags: matlab
category: "Subjective Test Software"
external_link: https://www.its.bldrdoc.gov/resources/video-quality-research/guides-and-tutorials/subject-screening-overview.aspx
direct_download_link: https://www.its.bldrdoc.gov/resources/video-quality-research/guides-and-tutorials/subject-screening-code.aspx
---

Following is a list of popular subject screening techniques. MATLAB code for the automated techniques is made available. This code may be used for any purpose, commercial or non-commercial.

## ITU-R Rec. BT.500 Annex 2 Clause 2.3.1

ITU-R Rec. BT.500 Annex 2 Clause 2.3.1 recommends a technique for screening Double

Stimulus Impairment Scale (DSIS) and Double Stimulus Continuous Quality Scale (DSCQS) data. However, this technique has been applied to tests conducted with other methods. This technique discards subjects whose ratings disagree frequently with other subjects. This technique can only be used with scores that have a normal distribution. Note that because the BT.500 technique analyzes agreement, it might discard a subjects who scores consistently higher or lower than other subjects, despite agreeing on the ranking of sequences by quality.

ITU-R Rec. BT.500 Annex 2 Clause 2.3.2 recommends a technique for Single Stimulus Continuous Quality Evaluation (SSCQE), however this algorithm is not implemented in the above code.

## ITU-R BT.1788 (SAMVIQ) Annex 2 Clauses 3.2, 3.3 And 3.4 In Series

ITU-R BT.1788, also known as SAMVIQ, demands that subjects have a stable and coherent method to vote degradations of quality. The rejection criteria uses both Pearson correlation and Spearman rank correlation. This technique rejects subject who do not associate with other subjects (i.e., rank impairments differently).

## VQEG HDTV Test Plan, Annex I

The Video Quality Experts Group (VQEG) HDTV Phase I Test Plan includes a method for screening subjects in Annex I (page 37). The rejection criteria tests consistency of scores using Pearson correlation on a per-clip basis. This technique rejects subject who do not associate with other subjects (e.g., rank impairments differently). The thresholds were chosen to be appropriate for Absolute Category Rating (ACR) tests.

Note that if the threshould were to be adjusted to be very low (e.g., 0.30), then the VQEG HDTV test plan rejection criteria would probably only eliminate subjects who did not understand the task.

## VQEG MM Test Plan, Annex VI

The Video Quality Experts Group (VQEG) Multimedia Phase I Test Plan includes a method for screening subjects in Annex VI (page 57). The rejection criteria tests consistency of scores using Pearson correlation on both a per-clip basis and averaging scores across all scenes associated with one impairment (i.e., per-HRC or Hypothetical Reference Circuit). This technique rejects subject who do not associate with other subjects (e.g., rank impairments differently). The thresholds were chosen to be appropriate for ACR tests.