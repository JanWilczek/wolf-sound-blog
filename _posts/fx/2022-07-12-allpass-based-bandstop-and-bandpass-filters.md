---
title: "Bandstop and Bandpass Filters: Allpass-Based Design & Implementation"
description: "Learn how to design and implement easily controllable and efficient bandstop and bandpass filters."
date: 2022-07-12
author: Jan Wilczek
layout: post
images: /assets/img/posts/fx/2022-07-12-allpass-based-bandstop-and-bandpass-filters/
images_parametric_eq: /assets/img/posts/fx/2021-11-26-parametric-eq-design/
images_allpass: /assets/img/posts/fx/2021-10-22-allpass-filter
background: /assets/img/posts/fx/2022-07-12-allpass-based-bandstop-and-bandpass-filters/bandpass.svg
categories:
  - Digital Signal Processing
  - Audio FX
tags:
  - filtering 
  - effects
  - Python
discussion_id: 2022-07-12-allpass-based-bandstop-and-bandpass-filters
---
With real-time center frequency and bandwidth control!

<iframe width="560" height="315" src="https://www.youtube.com/embed/wodumxEF9u0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

In [one of the previous articles]({% post_url fx/2022-05-08-allpass-based-lowpass-and-highpass-filters %}), we discussed how to implement a simple lowpass and a highpass filter using the first-order allpass filter. That filter had a real-time cutoff frequency control.

{% katexmm %}
{% capture _ %}{% increment equationId20220712  %}{% endcapture %}
{% capture _ %}{% increment figureId20220712  %}{% endcapture %}

Now, we can take it to the next level and design a bandpass and a bandstop filter with a second-order allpass filter. This design will allow us to control the center frequency and the bandwidth (or alternatively, the Q factor) in real time!

<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6611455743195468"
     crossorigin="anonymous"></script><ins class="adsbygoogle"
     style="display:block; text-align:center;"
     data-ad-layout="in-article"
     data-ad-format="fluid"
     data-ad-client="ca-pub-6611455743195468"
     data-ad-slot="7289385396"></ins><script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>

We'll discuss this design and its properties, listen to a few examples, and look at a [sample Python implementation](#implementation-1) at the end.

### Table of Contents

1. [What Is a Bandstop (Notch) Filter?](#what-is-a-bandstop-notch-filter)
2. [What Is a Bandpass Filter?](#what-is-a-bandpass-filter)
3. [Recap: The Second-Order Allpass Filter](#recap-the-second-order-allpass-filter)
   1. [Transfer Function](#transfer-function)
   2. [Phase Response](#phase-response)
4. [Allpass-Based Bandstop Filter](#allpass-based-bandstop-filter)
   1. [DSP Diagram](#dsp-diagram)
   2. [Magnitude Response](#magnitude-response)
   3. [Real-Time Control](#real-time-control)
   4. [Implementation](#implementation)
5. [Allpass-Based Bandpass Filter](#allpass-based-bandpass-filter)
   1. [DSP Diagram](#dsp-diagram-1)
   2. [Magnitude Response](#magnitude-response-1)
   3. [Real-Time Control](#real-time-control-1)
   4. [Implementation](#implementation-1)
6. [Applications](#applications)
   1. [Filter Sweep](#filter-sweep)
   2. [Hear band (in filters)](#hear-band-in-filters)
   3. [Phaser](#phaser)
7. [Summary](#summary)

## What Is a Bandstop (Notch) Filter?

A **bandstop filter** (also called a **notch filter**) is a filter that attenuates frequencies in a certain frequency range.

This frequency range is determined by a **center frequency** and a **bandwidth**.

![]({{ page.images_parametric_eq | absolute_url | append: "/Notch.webp"}}){: width="70%" alt="Bandstop filter amplitude response."}
_Figure {% increment figureId20220712  %}. Bandstop filter amplitude response._

The center frequency points to the frequency with the largest attenuation, the "dip" in the magnitude response of the filter.

The bandwidth determines how wide will the "dip" or "valley" be around the center frequency.

In order for the bandstop filter to sound equally wide in bandwidth at all center frequencies, we often use the **Q** or **quality factor** or **Q-factor** parameter. It is defined as

$$Q = \frac{f_c}{BW}, \quad ({% increment equationId20220712  %})$$

where $BW$ is the bandwidth in Hz and $f_c$ is the center frequency in Hz.

A "constant-Q" filter allows for a narrower band in the low frequencies (where human hearing is more sensitive to frequency) and for a wider band in the high frequencies (where human hearing is less sensitive to frequency).

Note that we cannot control the amount of attenuation in the bandstop filter. That is possible only in a _peaking (band) filter_, which is not the topic of this article.

## What Is a Bandpass Filter?

A bandpass filter is a filter that attenuates all frequencies apart from a specified range.

This range is defined in terms of the **center frequency** and the **bandwidth**, both expressed in Hz.

![]({{ page.images_parametric_eq | absolute_url | append: "/Bandpass.webp"}}){: width="70%" alt="Bandpass filter amplitude response."}
_Figure {% increment figureId20220712  %}. Bandpass filter amplitude response._

As in the case of the bandstop filter, we can specify the bandwidth using the **Q** (**quality factor**, **Q-factor**) parameter. Constant-Q filters retain the same "perceptual width" of the passed-through frequency range. The relation between the center frequency, the bandwidth, and Q is given by Equation 1.

## Recap: The Second-Order Allpass Filter

The main building block of bandpass and bandstop filters is the [second-order allpass filter]({% post_url fx/2021-10-22-allpass-filter %}#second-order-iir-allpass).

An allpass filter is a filter that does not attenuate any frequencies but it introduces a frequency-dependent phase shift.

Let's recap a few facts about this filter.

### Transfer Function

The transfer function of the second-order allpass filter is

$$H_{\text{AP}_2}(z) = \frac{-c + d(1-c) z^{-1} + z^{-2}}{1 + d(1-c) z^{-1} - c z^{-2}},  \quad ({% increment equationId20220712 %})$$

where

$$c = \frac{\tan(\pi BW / f_s) - 1}{\tan(\pi BW / f_s) + 1},  \quad ({% increment equationId20220712 %})$$

$$d = - \cos(2\pi f_\text{b} / f_s),  \quad ({% increment equationId20220712 %})$$

$BW$ is the bandwidth in Hz, $f_\text{b}$ is the break frequency in Hz, and $f_s$ is the sampling rate in Hz. The **break frequency** specifies the frequency at which the phase shift is $-\pi$. The **bandwidth** specifies the width of the transition band in which the phase shift goes from 0 to $-2\pi$.

### Phase Response

The phase response of the second-order allpass filter is visible in Figure 3.

![]({{ page.images_allpass | absolute_url | append: "/second_order_allpass_phase_response.webp" }}){: width="80%" alt="Phase response of the second-order allpass filter with constant bandwidth."}
_Figure {% increment figureId20220712 %}. Phase response of a second-order allpass filter for different break frequencies frequencies $f_\text{b}$ and bandwidth $BW / f_s = 0.022$._

As you can see, the phase shift is 0 at 0 Hz and gradually changes to $-2\pi$. The steepness of the phase response is determined by the bandwidth $BW$ parameter expressed in Hz.

You can already guess that the bandwidth parameter of the second-order allpass filter translates to the bandwidth parameter of bandpass and bandstop filters. Accordingly, the break frequency corresponds to the center frequency. How?

Thanks to the [phase cancellation effect]({% post_url fx/2022-05-08-allpass-based-lowpass-and-highpass-filters %}#phase-cancellation), if we add two tones at the same frequency but with relative phase shift of $\pi$, they will cancel each other. A shift by $\pi$ is equivalent to a multiplication of the tone by -1.

With this knowledge we can now employ the second-order allpass filter for bandpass or bandstop filtering.

## Allpass-Based Bandstop Filter

If we add the output of the second-order allpass filter to its input signal, at the break frequency we will obtain a phase cancellation. Why?

At the break frequency, the phase delay is $-\pi$. Adding two tones at the break frequency with the relative phase shift of $\pi$, we effectively eliminate them from the resulting signal. As the phase shift deviates from $\pi$ further away from the break frequency, the cancellation is less and less effective.

### DSP Diagram

Here is a block diagram of the bandstop filter.

![]({{ page.images | absolute_url | append: "/bandstop.svg"}}){: alt="DSP diagram of the allpass-based bandstop filter"}
_Figure {% increment figureId20220712  %}. DSP diagram of the allpass-based bandstop filter._

$\text{AP}_2(z)$ denotes the second-order allpass filter.

The output of the second-order allpass filter is added to the direct path. We multiply the result by $\frac{1}{2}$ to stay in the [-1, 1] range (input is in [-1, 1] range, allpass's output is in [-1, 1] range so their sum is in the [-2, 2] range; we want to scale that back down to [-1, 1], otherwise we'll possibly clip the signal).

### Magnitude Response

Here is a magnitude transfer function of the bandstop filter from Figure 4 with the center frequency at 250 Hz and $Q$ equal to 3.

![]({{ page.images | absolute_url | append: "/bandstop_amplitude_response.webp"}}){: width="70%" alt="Magnitude transfer function of the bandstop filter."}
_Figure {% increment figureId20220712  %}. Magnitude transfer function of the bandstop filter._

At the center frequency, we get the biggest attenuation which decreases the further away we get from the center frequency. We can see how selective in frequency this filter is.

### Real-Time Control

As this filter requires quite easy computations to control the center frequency and the bandwidth, we can alter its parameters in real time.

As an example, here's a white noise signal filtered with the bandstop filter, whose center frequency varies from 100 to 16000 Hz over time and Q is equal to 3.

{% include embed-audio.html src="/assets/wav/posts/fx/2022-07-12-allpass-based-bandstop-and-bandpass-filters/bandstop_filtered_noise.flac" %}

To visualize what's happening here, take a look at the spectrogram of the audio file.

![]({{ page.images | absolute_url | append: "/bandstop_example.webp"}}){: alt="Spectrogram of the bandstop filtering example."}
_Figure {% increment figureId20220712  %}. Spectrogram of the bandstop filtering example._

On the x-axis we have the time, on the y-axis we have the log-scaled frequency, and color indicates the amplitude level of the frequency at a specific time point in decibels full-scale (dBFS).

As you can see, the dip travels exponentially (mind the log scale!) from low to high frequencies. Thus, we can hear the so-called "filter sweep".

### Implementation

You will find a sample implementation of the bandstop filter in Python at [the end of this article](#implementation-1).

## Allpass-Based Bandpass Filter

The allpass-based bandpass filter differs from the bandstop filter only in the sign of the allpass filter output. In case of the bandpass, we invert the output of the allpass in phase so that the phase cancellation occurs at the 0 Hz frequency and the [Nyquist frequency]({% post_url 2019-11-19-how-to-represent-digital-sound-sampling-sampling-rate-quantization %}#the-sampling-theorem). Because the tone at the break frequency gets reversed twice, it is in phase with the input signal. Therefore, the summation results in doubling of the amplitude of the tone corresponding to the break frequency of the allpass.

### DSP Diagram

In Figure 7, there's a block diagram of the presented bandpass filter.

![]({{ page.images | absolute_url | append: "/bandpass.svg"}}){: alt="DSP diagram of the allpass-based bandpass filter"}
_Figure {% increment figureId20220712  %}. DSP diagram of the allpass-based bandpass filter._

$\text{AP}_2(z)$ denotes the second-order allpass filter.

The multiplication by $\frac{1}{2}$ is just to preserve the [-1, 1] amplitude range of the signal.

### Magnitude Response

In Figure 8, there's the magnitude response of the bandpass filter with center frequency set to 250 Hz and $Q$ set to 3.

![]({{ page.images | absolute_url | append: "/bandpass_amplitude_response.webp"}}){: width="70%" alt="Magnitude transfer function of the bandpass filter."}
_Figure {% increment figureId20220712  %}. Magnitude transfer function of the bandpass filter._

As you can see, it actually passes through only the frequencies in the specified band.

### Real-Time Control

Exactly as the bandstop filter, the bandpass filter can be easily controlled in real time.

Here's an audio sample with a bandpass-filtered white noise, where the center frequency varies from 100 Hz to 16000 Hz and Q is equal to 3.

{% include embed-audio.html src="/assets/wav/posts/fx/2022-07-12-allpass-based-bandstop-and-bandpass-filters/bandpass_filtered_noise.flac" %}

You can observe the effect of the bandpass filter on the spectrogram of the above audio file (Figure 9).

![]({{ page.images | absolute_url | append: "/bandpass_example.webp"}}){: alt="Spectrogram of the bandpass filtering example."}
_Figure {% increment figureId20220712  %}. Spectrogram of the bandpass filtering example._

Once again, the y-axis is a log-frequency axis, the x-axis is a time axis, and color intensity corresponds to the sound level in decibels full-scale (dBFS).

### Implementation

<iframe width="560" height="315" src="https://www.youtube.com/embed/boHWH_8ODv8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Here is a sample Python implementation of both filters: the bandpass and the bandstop.

The code generates 5 seconds of white noise and then filters it with time-varying bandstop and bandpass filters respectively. The center frequency in both cases changes exponentially from 100 Hz to 16000 Hz (this code was used to generate the previous examples in this article).

The code is heavily commented so you should have no problems in understanding.

_Listing 1. Allpass-based bandstop and bandpass filtering implementation & filter sweep application._
```python
{% include_relative _allpass_based_bandpass_bandstop.py %}
```

## Applications

Apart from just filtering, bandpass and bandstop filters can be used in a variety of audio effect applications.

### Filter Sweep

Filter sweep is a very strong effect that can add a powerful character to the sound. That's exactly the effect that you heard in the [bandstop-filtering example](#real-time-control).

### "Listen" to a Frequency Band (In Audio Plugins)

Audio plugins that use information from a frequency range to control their behavior often have a "listen" functionality that allows you to listen to the frequency band you specified and adjust it.

For example, [Tonmann Deesser plugin](https://www.tonmann.com/2015/07/18/free-tonmann-deesser-vst-plugin/) has the "listen" button to be able to hear the frequency range that is being compressed. With the "listen" functionality we can find the most audible range with the "s" consonant to compress and avoid compressing the desired signal.

![]({{ page.images | absolute_url | append: "/TonmannDeesserUI.webp"}}){: alt="Graphical user interface of the Tonmann Deesser plugin."}
_Figure {% increment figureId20220712  %}. Tonmann Deesser plugin has the "listen" functionality._

Alternatively, "listen" can be used to focus on just one part of the spectrum while making edits.

### Phaser

If we modulate the center frequency of the bandstop filter over time, for example, using a low-frequency oscillator (LFO), we can easily obtain the phaser effect.

Better yet, if we have a series of bandstop filters, the effect will be truly awesome! Think [Van Halen's Eruption](https://www.youtube.com/watch?v=M4Czx8EWXb0) level of awesome!

The actual application of the phaser effect will be a topic of an another article but you can already experiment with the attached implementation code!

## Summary

In this article, we learned how to implement efficient, real-time-controllable bandpass and bandstop filters using the second-order allpass filter.

Bandpass and bandstop filters are one of the basic effects in the audio programmer's arsenal. If you want to know which elements make up the audio plugin developer toolbox, check out my free [audio plugin developer checklist.]({% link single-pages/checklist.html %})

{% endkatexmm %}
