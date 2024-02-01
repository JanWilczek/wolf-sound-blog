---
title: "How To Plot An Audio Signal In Python Using Matplotlib | Tutorial For Beginners"
description: "Need to plot some audio signals? This code snippet allows you to easily plot any audio signal as a continuous waveform (+ explainer video)."
date: 2024-02-01
author: Jan Wilczek
layout: post
background: /assets/img/posts/dsp/2024-02-01-how-to-plot-audio-signal-in-python-with-matplotlib/Thumbnail.webp
categories:
  - Digital Signal Processing
tags:
  - sound wave
  - python
  - waveform
discussion_id: 2024-02-01-how-to-plot-audio-signal-in-python-with-matplotlib
custom_js:
 - /assets/vendor/lazyload/lazyload.min.js
 - /assets/js/wolfsound/modules/load_lazyload.js
---
Plot any audio signal using Python!

## Code snippet to plot an audio signal in Python

<script src="https://gist.github.com/JanWilczek/ccda1ea11a4288780548a4977b413d29.js"></script>

{% render 'google-ad.liquid' %}

Explanation:

1. Function `plot_signal()` plots the given signal using the passed-in time base (if given).
2. Function `plot_signal_and_save()` calls `plot_signal()` and then saves the figure to the disk while making sure that the `output_path` exists. You can show the figure with `plt.show()` but when you use it, you won't be able to save the figure as a file.
3. The `main()` function generates an example waveform (with time), plots it and saves to the disk using `plot_signal_and_save()`.

## Code explanation video

Watch how this code was written and why I included particular lines in this explainer video:



Want to know what knowledge from digital signal processing in needed for audio programming? Check out my [free Audio Plugin Developer Checklist]({% link collections.all, 'single-pages/checklist.html' %})!
