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
categories:
  - Digital Signal Processing
tags:
  - aliasing
  - sample rate
  - sampling
---
<figure class="wp-block-embed-youtube wp-block-embed is-type-video is-provider-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio">

<div class="wp-block-embed__wrapper">
  <div class="post-video">
  </div>
</div></figure> 



Aliasing is a very important phenomenon which highly influences the digital signal processing area. It is tightly coupled with the notion of sampling and sampling rate. Let&#8217;s discuss it in detail!

## Aliasing definition

**Aliasing** is the effect of overlapping frequency components resulting from unsufficiently large sample rate. In other words, it causes appearance of frequencies in the amplitude-frequency spectrum, that are not in the original signal. How does it come to life?

## Sampling theorem revisited

We should recall the sampling theorem:

<p class="ql-center-displayed-equation" style="line-height: 16px;">
  <span class="ql-right-eqno"> (1) </span><span class="ql-left-eqno"> &nbsp; </span><img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-3f7c5aae954cb3791e1fccfbcdf15c08_l3.png" height="16" width="85" class="ql-img-displayed-equation quicklatex-auto-format" alt="&#92;&#98;&#101;&#103;&#105;&#110;&#123;&#101;&#113;&#117;&#97;&#116;&#105;&#111;&#110;&#42;&#125;&#102;&#95;&#115;&#32;&#62;&#32;&#50;&#32;&#102;&#95;&#123;&#109;&#97;&#120;&#125;&#92;&#101;&#110;&#100;&#123;&#101;&#113;&#117;&#97;&#116;&#105;&#111;&#110;&#42;&#125;" title="Rendered by QuickLaTeX.com" />
</p>

where<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-e732ab7a055ad6a7a62754dbededbee5_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#102;&#95;&#115;" title="Rendered by QuickLaTeX.com" height="16" width="15" style="vertical-align: -4px;" /> is the sampling rate (how many samples of a continuous signal we take per second) and<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-71bb6069be79963fa181192fd4c18b4f_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#102;&#95;&#123;&#109;&#97;&#120;&#125;" title="Rendered by QuickLaTeX.com" height="16" width="36" style="vertical-align: -4px;" /> is the highest frequency in the observed signal. If we sample the signal holding on to the above inequality, we are able to perfectly reconstruct the signal:

<div class="wp-block-image is-style-default">
  <figure class="aligncenter size-full is-resized"><img src="https://thewolfsound.com/wp-content/uploads/2019/11/Sine100HzSampled9.png" alt="" class="wp-image-210" width="632" height="447" srcset="https://thewolfsound.com/wp-content/uploads/2019/11/Sine100HzSampled9.png 1780w, https://thewolfsound.com/wp-content/uploads/2019/11/Sine100HzSampled9-300x213.png 300w, https://thewolfsound.com/wp-content/uploads/2019/11/Sine100HzSampled9-1024x725.png 1024w, https://thewolfsound.com/wp-content/uploads/2019/11/Sine100HzSampled9-768x544.png 768w, https://thewolfsound.com/wp-content/uploads/2019/11/Sine100HzSampled9-1536x1088.png 1536w" sizes="(max-width: 632px) 100vw, 632px" /><figcaption>Accurately sampled signal.</figcaption></figure>
</div>

Clearly the samples preserve the original shape of the signal.

What happens if<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-a1030ace132c5af0d7161e4ca881ca37_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#102;&#95;&#115;&#32;&#61;&#32;&#50;&#32;&#102;&#95;&#123;&#109;&#97;&#120;&#125;" title="Rendered by QuickLaTeX.com" height="16" width="84" style="vertical-align: -4px;" /> ? Such a situation is depicted below:

<div class="wp-block-image">
  <figure class="aligncenter size-large is-resized"><img src="https://thewolfsound.com/wp-content/uploads/2019/11/Sine100HzSampled7-1024x725.png" alt="" class="wp-image-212" width="632" height="447" srcset="https://thewolfsound.com/wp-content/uploads/2019/11/Sine100HzSampled7-1024x725.png 1024w, https://thewolfsound.com/wp-content/uploads/2019/11/Sine100HzSampled7-300x213.png 300w, https://thewolfsound.com/wp-content/uploads/2019/11/Sine100HzSampled7-768x544.png 768w, https://thewolfsound.com/wp-content/uploads/2019/11/Sine100HzSampled7-1536x1088.png 1536w, https://thewolfsound.com/wp-content/uploads/2019/11/Sine100HzSampled7.png 1780w" sizes="(max-width: 632px) 100vw, 632px" /><figcaption>Signal sampled at the edge of reconstructibility.</figcaption></figure>
</div>

The sampled sinusoid is treated as a constant value; it can even become 0! So we clearly miss a part of the signal.

When we increase the maximum frequency<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-71bb6069be79963fa181192fd4c18b4f_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#102;&#95;&#123;&#109;&#97;&#120;&#125;" title="Rendered by QuickLaTeX.com" height="16" width="36" style="vertical-align: -4px;" /> (or equivalently: decrease the sampling rate<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-e732ab7a055ad6a7a62754dbededbee5_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#102;&#95;&#115;" title="Rendered by QuickLaTeX.com" height="16" width="15" style="vertical-align: -4px;" /> ) we can observe the following:

<div class="wp-block-image">
  <figure class="aligncenter size-large is-resized"><img src="https://thewolfsound.com/wp-content/uploads/2019/11/Sine100HzSampled5-1024x725.png" alt="" class="wp-image-213" width="632" height="448" srcset="https://thewolfsound.com/wp-content/uploads/2019/11/Sine100HzSampled5-1024x725.png 1024w, https://thewolfsound.com/wp-content/uploads/2019/11/Sine100HzSampled5-300x213.png 300w, https://thewolfsound.com/wp-content/uploads/2019/11/Sine100HzSampled5-768x544.png 768w, https://thewolfsound.com/wp-content/uploads/2019/11/Sine100HzSampled5-1536x1088.png 1536w, https://thewolfsound.com/wp-content/uploads/2019/11/Sine100HzSampled5.png 1780w" sizes="(max-width: 632px) 100vw, 632px" /><figcaption>Signal sampled at a too low rate to accurately reconstruct.</figcaption></figure>
</div>

The samples do not resemble the original signal and the information about it is lost. But we get **some** signal out of the sampling procedure. What is its frequency?

To learn the outcome of this operation we need to look at continuous and discrete signal spectra.

## Continuous vs discrete spectra

Having a continuous (analog) signal and being able to derive its continuous spectrum would enable us to see a situation similar as below:

<div class="wp-block-image">
  <figure class="aligncenter size-large is-resized"><img src="https://thewolfsound.com/wp-content/uploads/2019/11/AnalogSpectrum-1024x605.png" alt="" class="wp-image-237" width="632" srcset="https://thewolfsound.com/wp-content/uploads/2019/11/AnalogSpectrum-1024x605.png 1024w, https://thewolfsound.com/wp-content/uploads/2019/11/AnalogSpectrum-300x177.png 300w, https://thewolfsound.com/wp-content/uploads/2019/11/AnalogSpectrum-768x454.png 768w, https://thewolfsound.com/wp-content/uploads/2019/11/AnalogSpectrum.png 1070w" sizes="(max-width: 1024px) 100vw, 1024px" /><figcaption>Continuous spectrum of a continuous signal.</figcaption></figure>
</div>

The abscissa is equivalent to frequency<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-9c09a708375fde2676da319bcdfe8b24_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#102;" title="Rendered by QuickLaTeX.com" height="16" width="10" style="vertical-align: -4px;" /> and the ordinate to amplitude<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-7656074402dda0501352ee7b93f40c64_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#124;&#92;&#104;&#97;&#116;&#123;&#115;&#125;&#40;&#102;&#41;&#124;" title="Rendered by QuickLaTeX.com" height="18" width="39" style="vertical-align: -4px;" /> of particular frequency components. We can view a signal as a sum of its frequency components. The spectrum is even (<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-d8dc97a229e4d0a412e7218badef524e_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#92;&#104;&#97;&#116;&#123;&#115;&#125;&#40;&#102;&#41;&#32;&#61;&#32;&#92;&#104;&#97;&#116;&#123;&#115;&#125;&#40;&#45;&#102;&#41;" title="Rendered by QuickLaTeX.com" height="18" width="102" style="vertical-align: -4px;" />), because values of the original signal are real (<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-6b9aea0a486b9a1872ac97ed4da85002_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#115;&#40;&#116;&#41;&#32;&#92;&#105;&#110;&#32;&#92;&#109;&#97;&#116;&#104;&#98;&#98;&#123;&#82;&#125;" title="Rendered by QuickLaTeX.com" height="18" width="63" style="vertical-align: -4px;" />). We can clearly see, that there is some<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-71bb6069be79963fa181192fd4c18b4f_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#102;&#95;&#123;&#109;&#97;&#120;&#125;" title="Rendered by QuickLaTeX.com" height="16" width="36" style="vertical-align: -4px;" /> above which no frequency components are present.

_(Note: according to the Heisenberg&#8217;s uncertainty principle the signal corresponding to the above spectrum should be infinite in time domain since the spectrum is finite in the frequency domain.)_

_(Note: examples of continuous signals that are not finite in the frequency domain are white noise and Dirac&#8217;s delta)._

How does the spectrum of a sampled signal look? Well, it repeats itself every<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-e732ab7a055ad6a7a62754dbededbee5_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#102;&#95;&#115;" title="Rendered by QuickLaTeX.com" height="16" width="15" style="vertical-align: -4px;" /> :

<div class="wp-block-image">
  <figure class="aligncenter size-large is-resized"><img src="https://thewolfsound.com/wp-content/uploads/2019/11/DiscreteSpectrum-1024x680.png" alt="" class="wp-image-238" width="632" srcset="https://thewolfsound.com/wp-content/uploads/2019/11/DiscreteSpectrum-1024x680.png 1024w, https://thewolfsound.com/wp-content/uploads/2019/11/DiscreteSpectrum-300x199.png 300w, https://thewolfsound.com/wp-content/uploads/2019/11/DiscreteSpectrum-768x510.png 768w, https://thewolfsound.com/wp-content/uploads/2019/11/DiscreteSpectrum.png 1073w" sizes="(max-width: 1024px) 100vw, 1024px" /><figcaption>Discrete spectrum of a discrete signal. Although not visible here, the spectrum is quantized in frequency as well.</figcaption></figure>
</div>

Why is that? You can explain it intuitively that having a set of samples, you can always insert one or more periods of a sine between them and it would still get sampled the same way:

<div class="wp-block-image">
  <figure class="aligncenter size-large is-resized"><img src="https://thewolfsound.com/wp-content/uploads/2019/11/SpectraMultiplicity-2-1024x787.png" alt="" class="wp-image-234" width="632" srcset="https://thewolfsound.com/wp-content/uploads/2019/11/SpectraMultiplicity-2-1024x787.png 1024w, https://thewolfsound.com/wp-content/uploads/2019/11/SpectraMultiplicity-2-300x231.png 300w, https://thewolfsound.com/wp-content/uploads/2019/11/SpectraMultiplicity-2-768x590.png 768w, https://thewolfsound.com/wp-content/uploads/2019/11/SpectraMultiplicity-2-1536x1180.png 1536w, https://thewolfsound.com/wp-content/uploads/2019/11/SpectraMultiplicity-2.png 1641w" sizes="(max-width: 1024px) 100vw, 1024px" /><figcaption> Discrete nodes may be viewed as sampling a sine of frequency 0, <img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-e732ab7a055ad6a7a62754dbededbee5_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#102;&#95;&#115;" title="Rendered by QuickLaTeX.com" height="16" width="15" style="vertical-align: -4px;" />, <img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-d345868116bb4b9a432633e226f06660_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#50;&#32;&#102;&#95;&#115;" title="Rendered by QuickLaTeX.com" height="16" width="24" style="vertical-align: -4px;" />, etc. </figcaption></figure>
</div>

If we do not know anything about the signal that was sampled, we cannot say what frequencies it originally had. But we generally (not always) assume that the frequencies in the original signal were between 0 and<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-a593f0d1f67ebfe0ee1a026824cfe6df_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#92;&#102;&#114;&#97;&#99;&#123;&#102;&#95;&#115;&#125;&#123;&#50;&#125;" title="Rendered by QuickLaTeX.com" height="23" width="14" style="vertical-align: -6px;" /> (we ignore negative frequencies as they have no physical meaning). Thus, during reconstruction, we restrict ourselves to these frequencies only.

## Aliased spectra

Now with aliasing<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-c61b52833fc7c9ad8b949fbd484147fe_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#102;&#95;&#123;&#109;&#97;&#120;&#125;&#32;&#62;&#32;&#92;&#102;&#114;&#97;&#99;&#123;&#102;&#95;&#115;&#125;&#123;&#50;&#125;" title="Rendered by QuickLaTeX.com" height="23" width="76" style="vertical-align: -6px;" /> , so we could observe something like this:

<div class="wp-block-image">
  <figure class="aligncenter size-large is-resized"><img src="https://thewolfsound.com/wp-content/uploads/2019/11/AliasingSpectrum-1024x698.png" alt="" class="wp-image-236" width="632" srcset="https://thewolfsound.com/wp-content/uploads/2019/11/AliasingSpectrum-1024x698.png 1024w, https://thewolfsound.com/wp-content/uploads/2019/11/AliasingSpectrum-300x204.png 300w, https://thewolfsound.com/wp-content/uploads/2019/11/AliasingSpectrum-768x523.png 768w, https://thewolfsound.com/wp-content/uploads/2019/11/AliasingSpectrum-1536x1047.png 1536w, https://thewolfsound.com/wp-content/uploads/2019/11/AliasingSpectrum.png 1626w" sizes="(max-width: 1024px) 100vw, 1024px" /><figcaption>Aliasing: frequency components of multiplicated spectra overlap.</figcaption></figure>
</div>

The repeated spectra overlap and in the overlapping regions a permantent loss of signal information happens. That exactly is aliasing. Afterwards we cannot reconstruct the original signal anymore. Going back to our sine example: if the sampled sine had a frequency of<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-5a46bdd56a759dee4b24067302e5b5cb_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#51;&#56;&#32;&#92;&#116;&#101;&#120;&#116;&#123;&#107;&#72;&#122;&#125;" title="Rendered by QuickLaTeX.com" height="14" width="48" style="vertical-align: -1px;" /> and we sampled it with<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-b0af4b1889a10d2b80fc74752e1b89d6_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#102;&#95;&#115;&#32;&#61;&#52;&#56;&#32;&#92;&#116;&#101;&#120;&#116;&#123;&#107;&#72;&#122;&#125;" title="Rendered by QuickLaTeX.com" height="17" width="87" style="vertical-align: -4px;" /> , due to spectra duplication we would get a reflected component at<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-05c9e19a0b551754b622fd891944d404_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#102;&#32;&#61;&#32;&#45;&#49;&#48;&#32;&#92;&#116;&#101;&#120;&#116;&#123;&#107;&#72;&#122;&#125;" title="Rendered by QuickLaTeX.com" height="17" width="96" style="vertical-align: -4px;" /> and at<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-ec3e07a62130e71465534e6625f7d9ab_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#102;&#32;&#61;&#32;&#49;&#48;&#32;&#92;&#116;&#101;&#120;&#116;&#123;&#107;&#72;&#122;&#125;" title="Rendered by QuickLaTeX.com" height="17" width="82" style="vertical-align: -4px;" /> because the spectrum is even. It will be audible in the output and we shall demonstrate it below:

<div class="wp-block-image">
  <figure class="aligncenter size-large is-resized"><img src="https://thewolfsound.com/wp-content/uploads/2019/11/AliasedSpectrum-1024x807.png" alt="" class="wp-image-218" width="632" srcset="https://thewolfsound.com/wp-content/uploads/2019/11/AliasedSpectrum-1024x807.png 1024w, https://thewolfsound.com/wp-content/uploads/2019/11/AliasedSpectrum-300x237.png 300w, https://thewolfsound.com/wp-content/uploads/2019/11/AliasedSpectrum-768x606.png 768w, https://thewolfsound.com/wp-content/uploads/2019/11/AliasedSpectrum-1536x1211.png 1536w, https://thewolfsound.com/wp-content/uploads/2019/11/AliasedSpectrum.png 1697w" sizes="(max-width: 1024px) 100vw, 1024px" /><figcaption>Aliased frequency components: sine at 38 kHz appears at 10 kHz.</figcaption></figure>
</div>

## How to avoid aliasing?

To avoid aliasing we can:

  * ensure it is in the<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-0e988ec8a1e417ef90c1a17c68ae41ff_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#91;&#48;&#44;&#32;&#92;&#102;&#114;&#97;&#99;&#123;&#102;&#95;&#115;&#125;&#123;&#50;&#125;&#41;" title="Rendered by QuickLaTeX.com" height="23" width="43" style="vertical-align: -6px;" /> range (e.g. through low-pass filtering) or
  * increase the sample rate.

This implies that we should know what range our signal is in before we sample it.

Remember: after aliasing creeped into the sampled signal, it is impossible to eliminate.

## Summary

Aliasing is the effect of new frequencies appearing in the sampled signal after reconstruction, that were not present in the original signal. It is caused by too low sample rate for sampling a particular signal or too high frequencies present in the signal for a particular sample rate. We can avoid it by using sufficiently large sample rate or low-pass filtering the signal before sampling to ensure the<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-798751dbed6e08e60a07079a23b05606_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#102;&#95;&#123;&#109;&#97;&#120;&#125;&#32;&#60;&#32;&#92;&#102;&#114;&#97;&#99;&#123;&#102;&#95;&#115;&#125;&#123;&#50;&#125;" title="Rendered by QuickLaTeX.com" height="23" width="76" style="vertical-align: -6px;" /> condition.

## Sine aliasing code example

The following code plays out three consecutive sines: at 100, 1000, 10 000 and 38 000 Hz and displays their spectra. You can hear, that the 38 kHz sine sampled at 48 kHz sounds exactly like 10 kHz: an effect of aliasing.

<pre class="brush: python; title: ; notranslate" title="">#!/usr/bin/env python3
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

</pre>

Feel free to download and run it yourself! You should have numpy, matplotlib and sounddevice installed.

Reference:  
[1] Oppenheim, A. V. and Willsky, A. S. Signals & Systems. 2nd ed. Upper Sadle River, New Jersey: Prentice Hall, 1997. 

<!--themify-builder:block-->