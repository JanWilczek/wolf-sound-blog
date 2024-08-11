---
title: "How To Plot Audio Spectrogram For Machine Learning In Python Using Librosa & Matplotlib | Tutorial for Beginners"
description: "Plot magnitude of a short-time Fourier transform (STFT). Ready-to-go code snippet & explainer video show you how to do it in Python"
date: 2024-06-05
author: Jan Wilczek
layout: post
permalink: /how-to-plot-audio-spectrogram-for-machine-learning-magnitude-stft-of-audio-signal-with-python-librosa-and-matplotlib/
background: /assets/img/posts/dsp/2024-06-05-how-to-plot-audio-spectrogram-magnitude-stft-of-audio-signal-with-python-librosa-and-matplotlib/Thumbnail.webp
categories:
  - Digital Signal Processing
tags:
  - fourier
  - python
  - transform
discussion_id: 2024-06-05-how-to-plot-audio-spectrogram-magnitude-stft-of-audio-signal-with-python-librosa-and-matplotlib
custom_js:
 - /assets/vendor/lazyload/lazyload.min.js
 - /assets/js/wolfsound/modules/load_lazyload.js
---
Visualize a sound file using Python!

In digital signal processing (DSP), machine learning, and deep learning we often need a representation of an audio signal in an image form.

The closest we can get is via using a **spectrogram**: the magnitude of a short-time Fourier transform (STFT).

In the below code snippet and linked YouTube tutorial, I'm showing you how to calculate the spectrogram, plot it, and save it.

## What is a short-time Fourier transform (STFT)?

A short-time Fourier transform (STFT) is the effect of

1. windowing a signal and
2. calculating its discrete Fourier transform (DFT)

every few samples.

To calculate the STFT:

1. Window a part of the signal of length $W$ with a window, for example, [the Hann window](https://en.wikipedia.org/wiki/Hann_function).
2. If the given DFT size $N_\text{DFT}$ is larger than $W$ pad the windowed signal with zeros so that it is of length $N_\text{DFT}$.
3. Calculate the DFT of the windowed and zero-padded signal.
4. Advance by $H$ samples and go to step 1. Repeat until the whole signal has been processed.

Following parameters of the STFT are important:

* Window length or window size $W$,
* Hop length or hop size $H$,
* DFT size (often called FFT size or FFT length) $N_\text{DFT}$.

These parameters are given in samples and they influence the time and frequency resolution of the STFT.

## What is a spectrogram?

Spectrogram is the magnitude of the STFT.

Each STFT coefficient is a complex number. By taking their magnitude, we obtain a real-valued spectrogram.

## How to calculate the spectrogram in Python?

Below there's the code snippet for it, further down are the explanations and finally, a video showing step-by-step how the script was created.

From the video, you will learn:

* ✅ Which libraries to use
* ✅ How to effortlessly compute the STFT of an audio signal
* ✅ Step-by-step writing of the `plot_spectrogram_and_save()` function
* ✅ How to plot the spectrogram in decibels full-scale (dBFS)
* ✅ How to mark the frequency axis using the ISO-standardized octave band marks
* ✅ How to adjust the figure to your needs (colors, labels, font size, and more)
* ✅ How to export your figure to a .png file effortlessly

### Code snippet to plot the magnitude spectrum of an audio signal in Python

<script src="https://gist.github.com/JanWilczek/680c63a2f3710e1ad833d7c8aa8a7250.js"></script>

{% render 'google-ad.liquid' %}

Explanation:

1. `plot_spectrogram_and_save()`
    1.  calculates the short-time Fourier transform (the STFT),
    1.  computes its magnitude (i.e., the spectrogram),
    1.  converts it to decibels full scale (normalized to the highest value),
    1.  plots the spectrogram with beautiful formatting,
    1.  saves it to a file.
1.  Example `main()` function
    1.  reads an audio file from a specified location,
    1.  passes it to the plotting function.

Example speech comes from [the LibriSpeech database](https://www.openslr.org/12/).

Feel free to copy & paste & modify the snippet according to your needs!

Python libraries used:

* numpy
* matplotlib
* pathlib
* librosa version 0.9.2
* soundfile (only for reading the example audio file, not needed for the spectrogram per se)

### Code explanation video

Watch how this code was written and why I included particular lines in this explainer video:

{% include 'youtube-video', video_id: '6nLx1Zqmkuw' %}

Want to know what knowledge from digital signal processing in needed for audio programming? Check out my [free Audio Plugin Developer Checklist]({% link collections.all, 'single-pages/checklist.html' %})!
