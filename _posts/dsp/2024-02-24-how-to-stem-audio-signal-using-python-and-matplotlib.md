---
title: "How To Stem An Audio Signal Using Python And Matplotlib | Tutorial For Beginners"
description: "Need to plot some audio signals? This code snippet allows you to easily plot any audio signal as a continuous waveform (+ explainer video)."
description: "How to plot individual samples of an audio signal. Use the stem plot. This tutorial + explainer video shows you how to do it in Python"
date: 2024-02-24
author: Jan Wilczek
layout: post
background: /assets/img/posts/dsp/2024-02-24-how-to-stem-audio-signal-using-python-and-matplotlib/Thumbnail.webp
categories:
  - Digital Signal Processing
tags:
  - sound wave
  - python
  - waveform
discussion_id: 2024-02-24-how-to-stem-audio-signal-using-python-and-matplotlib
custom_js:
 - /assets/vendor/lazyload/lazyload.min.js
 - /assets/js/wolfsound/modules/load_lazyload.js
---
Display audio signal samples using Python!

## Code snippet to stem an audio signal in Python

<script src="https://gist.github.com/JanWilczek/8ad9f37b2a10a77785947374487047a0.js"></script>

{% render 'google-ad.liquid' %}

Explanation:

1. In the `main()` function, we generate a sine and pass the initial 40 samples into the "stem and save" function.
2. In the `stem_signal()` function, we mostly adjust figure's properties. We adjust the limits of the figure to include all samples. Lines starting with `ax` turn off the ugly frame of the plot.
3. In `save()` function, we create the output directory and then save the figure there with high quality and transparent background.

## Code explanation video

Watch how this code was written and why I included particular lines in this explainer video:

<!-- TODO -->

Want to know what knowledge from digital signal processing in needed for audio programming? Check out my [free Audio Plugin Developer Checklist]({% link collections.all, 'single-pages/checklist.html' %})!
