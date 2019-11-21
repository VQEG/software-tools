---
title: VQEGNumSubjTool
excerpt: Number of Subjects Calculations
author: Werner Robitza, Kjell Brunnström
license: MIT
tags: open-source
category: "Subjective Test Software"
external_link: https://github.com/VQEG/number-of-subjects
direct_download_link: https://slhck.shinyapps.io/number-of-subjects/
---

Scripts and data for estimating the required number of test subjects for typical Quality of Experience experiments.

The app can be used interactively here:

https://slhck.shinyapps.io/number-of-subjects/

The calculations are based on knowing:

- the number of statistical t-test comparisons to be performed
- the statistical significance level (alpha), typically 0.05
- the desired power of the test (1 - Type II error probability), typically 0.8
- the test conducted (paired or independent/two-sample), typically paired
- the expected effect size (expected MOS difference divided by standard deviation), which is automatically calculated

The result is the minimum number of subjects needed for the experiment in order to obtain enough data to perform statistical comparisons corrected for Type I errors.
