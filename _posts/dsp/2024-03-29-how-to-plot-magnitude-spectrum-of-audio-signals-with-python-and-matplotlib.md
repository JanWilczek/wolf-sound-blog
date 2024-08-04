---
title: "How To Plot Magnitude Spectrum of Audio Signal with Python and Matplotlib | Tutorial for Beginners"
description: "Plot discrete Fourier transform (e.g., FFT) result. This tutorial + explainer video shows you how to do it in Python"
date: 2024-03-29
author: Jan Wilczek
layout: post
background: /assets/img/posts/dsp/2024-03-29-how-to-plot-magnitude-spectrum-of-audio-signals-with-python-and-matplotlib/Thumbnail.webp
categories:
  - Digital Signal Processing
tags:
  - fourier
  - python
  - transform
discussion_id: 2024-03-29-how-to-plot-magnitude-spectrum-of-audio-signals-with-python-and-matplotlib
custom_js:
 - /assets/vendor/lazyload/lazyload.min.js
 - /assets/js/wolfsound/modules/load_lazyload.js
---
Display the FFT result using Python!

In digital signal processing (DSP), we often compute the discrete Fourier transform (DFT) of an audio signal, for example, using the Fast Fourier Transform (FFT). This tutorial shows you how to easily display the magnitude of the DFT, the magnitude spectrum, using the Matplolib library in Python.

The script includes examples of how to include decibels full-scale (dBFS) scaling of the magnitude axis and a logarithmic frequency axis for a better interpretability of the graph.

Below there's the code snippet for it, further down are the explanations and finally, a video showing step-by-step how the script was created.

From the script you will learn:

* ✅ Which libraries to use
* ✅ How to effortlessly compute the FFT of an audio signal
* ✅ Step-by-step writing of the plot_magnitude_spectrum functions
* ✅ How to plot the magnitude in decibels full-scale (dBFS)
* ✅ How to plot the frequency axis logarithmically which corresponds to our perception of pitch
* ✅ How to mark the frequency axis using the ISO-standardized octave band marks
* ✅ How to adjust the figure to your needs (colors, labels, font size, markersize and more)
* ✅ How to export your figure to a .png file with transparent background effortlessly
* ✅ How to adjust the limits of the plot properly for optimal readability

## Code snippet to plot the magnitude spectrum of an audio signal in Python

<script src="https://gist.github.com/JanWilczek/c2103897d9a93fce0b02b690ca87d36d.js"></script>

{% render 'google-ad.liquid' %}

Explanation:

1. In the `main()` function, we read an example signal from the [LibriSpeech](https://www.openslr.org/12/) database. We then calculate its one-sided magnitude spectrum, i.e., including frequencies only up to the Nyquist frequency. We also compute the frequencies corresponding to the discrete Fourier transform bins. We then pass the frequencies and the magnitude spectrum to 3 plotting functions along with the path to save the plot to.
2. In the `plot_spectrum_and_save()` function, we plot the magnitude spectrum using linear frequency and magnitude scales. We then mostly adjust the figure's properties. Lines starting with `ax` turn off the ugly frame of the plot.
2. In the `plot_spectrum_db_and_save()` function, we do the same but the passed in magnitude spectrum must be in decibels. Before we compute the decibels with `librosa.amplitude_to_db` function, we normalize the magnitude spectrum to the highest value so that the maximum value is 1 the decibels are full scale (the highest value is 0 dBFS). In audio, we typically compare relative magnitudes rather than absolute because we're dealing with digital signals that are anyway in the [-1, 1] range (most often). In the function, we also display the grid so that reading from the plot is easier.
2. In the `plot_spectrum_plot_spectrum_db_in_octaves_and_saveand_save()` function, we do the same thing as in the previous function but we plot the frequency axis to be logarithmic, which corresponds more to our perception. We also set the ticks on the frequency axis to correspond to ISO octave bands.

Python libraries used:

* numpy
* matplotlib
* scipy
* pathlib
* librosa version 0.9.2

## Code explanation video

Watch how this code was written and why I included particular lines in this explainer video:

<iframe width="560" height="315" src="https://www.youtube.com/embed/nA778DSmZew?si=efXK2-SZFHHY9E_u" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen loading="lazy"></iframe>

Want to know what knowledge from digital signal processing in needed for audio programming? Check out my [free Audio Plugin Developer Checklist]({% link collections.all, 'single-pages/checklist.html' %})!
