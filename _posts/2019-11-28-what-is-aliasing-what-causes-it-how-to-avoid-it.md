---
id: 197
title: What is aliasing? What causes it? How to avoid it?
date: 2019-11-28T16:21:16+00:00
author: Jan Wilczek
layout: post
guid: https://thewolfsound.com/?p=197
permalink: /what-is-aliasing-what-causes-it-how-to-avoid-it/
content_width:
  - default_width
hide_post_title:
  - default
unlink_post_title:
  - default
hide_post_date:
  - default
hide_post_image:
  - default
unlink_post_image:
  - default
header_wrap:
  - solid
background_repeat:
  - fullcover
themify_used_global_styles:
  - 'a:1:{i:0;s:0:"";}'
tbp_custom_css:
  - ""
image: /wp-content/uploads/2019/11/thumbnail.png
background: /wp-content/uploads/2019/11/thumbnail.png
categories:
  - Digital Signal Processing
tags:
  - aliasing
  - sample rate
  - sampling (A/C conversion)
discussion_id: 2019-11-28-what-is-aliasing-what-causes-it-how-to-avoid-it
---
<iframe width="560" height="315" src="https://www.youtube.com/embed/npeMd5U-5QI" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

{% katexmm %}

Aliasing is a very important phenomenon which highly influences the digital signal processing area. It is tightly coupled with the notion of sampling and sampling rate. Let&#8217;s discuss it in detail!

## Aliasing definition

**Aliasing** is the effect of overlapping frequency components resulting from unsufficiently large sample rate. In other words, it causes appearance of frequencies in the amplitude-frequency spectrum, that are not in the original signal. How does it come to life?

## Sampling theorem revisited

We should recall the sampling theorem:

$$f_s > 2 f_{max}$$

where $f_s$ is the sampling rate (how many samples of a continuous signal we take per second) and $f_{max}$ is the highest frequency in the observed signal. If we sample the signal holding on to the above inequality, we are able to perfectly reconstruct the signal:

![](https://thewolfsound.com/wp-content/uploads/2019/11/Sine100HzSampled9.png)
*Accurately sampled signal.*

Clearly the samples preserve the original shape of the signal.

What happens if $f_s = 2 f_{max}$? Such a situation is depicted below:

![](https://thewolfsound.com/wp-content/uploads/2019/11/Sine100HzSampled7-1024x725.png)
*Signal sampled at the edge of reconstructibility.*

The sampled sinusoid is treated as a constant value; it can even become 0! So we clearly miss a part of the signal.

When we increase the maximum frequency $f_{max}$ (or equivalently: decrease the sampling rate $f_s$) we can observe the following:

![](https://thewolfsound.com/wp-content/uploads/2019/11/Sine100HzSampled5-1024x725.png)
*Signal sampled at a too low rate to accurately reconstruct.*

The samples do not resemble the original signal and the information about it is lost. But we get **some** signal out of the sampling procedure. What is its frequency?

To learn the outcome of this operation we need to look at continuous and discrete signal spectra.

## Continuous vs discrete spectra

Having a continuous (analog) signal and being able to derive its continuous spectrum would enable us to see a situation similar as below:

![](https://thewolfsound.com/wp-content/uploads/2019/11/AnalogSpectrum-1024x605.png)
*Continuous spectrum of a continuous signal.*

The abscissa is equivalent to frequency $f$ and the ordinate to amplitude $|\hat{s}(f)|$ of particular frequency components. We can view a signal as a sum of its frequency components. The spectrum is even ($\hat{s}(f) = \hat{s}(-f)$), because values of the original signal are real ($s(t) \in \mathbb{R}$). We can clearly see, that there is some $f_{max}$ above which no frequency components are present.

_(Note: according to the Heisenberg&#8217;s uncertainty principle the signal corresponding to the above spectrum should be infinite in time domain since the spectrum is finite in the frequency domain.)_

_(Note: examples of continuous signals that are not finite in the frequency domain are white noise and Dirac&#8217;s delta)._

How does the spectrum of a sampled signal look? Well, it repeats itself every $f_s$:

![](https://thewolfsound.com/wp-content/uploads/2019/11/DiscreteSpectrum-1024x680.png)
*Discrete spectrum of a discrete signal. Although not visible here, the spectrum is quantized in frequency as well.*

Why is that? You can explain it intuitively that having a set of samples, you can always insert one or more periods of a sine between them and it would still get sampled the same way:

![](https://thewolfsound.com/wp-content/uploads/2019/11/SpectraMultiplicity-2-1024x787.png)
*Discrete nodes may be viewed as sampling a sine of frequency 0, $f_s$, $2f_s$, etc.*

If we do not know anything about the signal that was sampled, we cannot say what frequencies it originally had. But we generally (not always) assume that the frequencies in the original signal were between 0 and $\frac{f_s}{2}$ (we ignore negative frequencies as they have no physical meaning). Thus, during reconstruction, we restrict ourselves to these frequencies only.

## Aliased spectra

Now with aliasing $f_{max} > \frac{f_s}{2}$, so we could observe something like this:

![](https://thewolfsound.com/wp-content/uploads/2019/11/AliasingSpectrum-1024x698.png)
*Aliasing: frequency components of multiplicated spectra overlap.*

The repeated spectra overlap and in the overlapping regions a permantent loss of signal information happens. That exactly is aliasing. Afterwards we cannot reconstruct the original signal anymore. Going back to our sine example: if the sampled sine had a frequency of $38 \text{ kHz}$ and we sampled it with $f_s =48 \text{kHz}$, due to spectra duplication we would get a reflected component at $ f = -10 \text{ kHz}$ and at  $ f = 10 \text{ kHz}$ because the spectrum is even. It will be audible in the output and we shall demonstrate it below:

![](https://thewolfsound.com/wp-content/uploads/2019/11/AliasedSpectrum-1024x807.png)
*Aliased frequency components: sine at 38 kHz appears at 10 kHz.*

## How to avoid aliasing?

To avoid aliasing we can:

  * ensure it is in the $[0, \frac{f_s}{2})$ range (e.g. through low-pass filtering) or
  * increase the sample rate.

This implies that we should know what range our signal is in before we sample it.

Remember: after aliasing creeped into the sampled signal, it is impossible to eliminate.

## Summary

Aliasing is the effect of new frequencies appearing in the sampled signal after reconstruction, that were not present in the original signal. It is caused by too low sample rate for sampling a particular signal or too high frequencies present in the signal for a particular sample rate. We can avoid it by using sufficiently large sample rate or low-pass filtering the signal before sampling to ensure the $f_{max} < \frac{f_s}{2}$ condition.

## Sine aliasing code example

The following code plays out three consecutive sines: at 100, 1000, 10 000 and 38 000 Hz and displays their spectra. You can hear, that the 38 kHz sine sampled at 48 kHz sounds exactly like 10 kHz: an effect of aliasing.

```python
#!/usr/bin/env python3
"""Example of sine sampling"""
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
__author__  = "Jan Wilczek"
__license__ = "GPL"
__version__ = "1.0.0"

# Plotting parameters
plt.rcParams.update({'font.size': 15})
xlim = [-15, 15]
stem_params = {'linefmt': 'C0-', 'markerfmt': 'C0o', 'basefmt': ' '}


def signal(A, f, t, phi=0.0):
    """
    :param A: amplitude
    :param f: frequency in Hz
    :param t: time in s
    :param phi: phase offset
    :return: sine with amplitude A at frequency f over time t
    """
    return A * np.sin(2 * np.pi * f * t + phi)

def normalized_dft(signal, n_fft, fs):
    """
    :param signal: signal to calculate DFT of
    :param n_fft: number of samples for Fast Fourier Transform
    :param fs: sample rate
    :return: discrete Fourier spectrum of the given signal normalized to the highest amplitude of frequency components
    """
    dft = np.abs(np.fft.fft(signal[:n_fft]))
    dft /= np.amax(dft)
    frequencies = np.fft.fftfreq(len(dft), d=1 / fs)

    amplitude_threshold = 0.01
    nonzero_frequencies = [frequency for i, frequency in enumerate(frequencies) if dft[i] &gt; amplitude_threshold]
    nonzero_dft = [amplitude for amplitude in dft if amplitude &gt; amplitude_threshold]

    return np.array(nonzero_dft), np.array(nonzero_frequencies)


if __name__ == '__main__':
    # Signal parameters
    fs = 48000                  # sample rate, Hz
    time_start = 0              # s
    signal_duration = 1         # s
    n_fft = int(0.01 * fs)      # number of samples for DFT
    t = np.arange(time_start, signal_duration, step=1/fs)

    # Hz to kHz conversion
    divisor = 1000.0
    fs_plot = fs / divisor

    frequencies = [100, 1000, 10000, 38000]
    for f in frequencies:
        # Generation
        s_t = signal(1.0, f, t)

        # Discrete Fourier transform
        dft, frequencies = normalized_dft(s_t, n_fft, fs)

        # Scaling
        frequencies_plot = frequencies / divisor

        # Playing
        attenuation = 0.3
        sd.play(attenuation * s_t, samplerate=fs)

        # Plotting
        plt.figure()
        plt.stem(frequencies_plot, dft, **stem_params)
        plt.hlines(xmin=xlim[0], xmax=xlim[1], y=0, colors='black')
        plt.vlines(0, 0, 1.0)
        plt.yticks([0, 1])
        plt.ylabel('Relative amplitude')
        plt.xlabel('f [kHz]')
        plt.show()
```

Feel free to download and run it yourself! You should have numpy, matplotlib and sounddevice installed.

Reference:  
[1] Oppenheim, A. V. and Willsky, A. S. Signals & Systems. 2nd ed. Upper Sadle River, New Jersey: Prentice Hall, 1997. 

{% endkatexmm %}