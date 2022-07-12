---
title: "Bandstop and Bandpass Filters: Real-Time Controllable Allpass-Based Design & Implementation"
description: "Learn how to design and implement easily controllable and efficient bandstop and bandpass filters."
date: 2022-07-12
author: Jan Wilczek
layout: post
images: /assets/img/posts/fx/2022-07-12-allpass-based-bandstop-and-bandpass-filters/
images_allpass: /assets/img/posts/fx/2021-10-22-allpass-filter
background: /assets/img/posts/fx/2022-07-12-allpass-based-bandstop-and-bandpass-filters/lowpass.svg
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

In one of the previous article, we discussed how to implement a simple lowpass and a highpass filter using the first-order allpass filter. That filter had a real-time cutoff frequency control.

Now, we can take it to the next level and design a bandpass and a bandstop filter with a second-order allpass filter. This design will allow us to control the center frequency and the bandwidth (or alternatively, the Q factor) in real time!

We'll discuss this design and its properties, listen to a few examples, and look at a sample Python implementation at the end.

## What Is a Bandstop Filter?

A **bandstop filter** is a filter that attenuates frequencies in a certain frequency range.

This frequency range is determined by a **center frequency** and a **bandwidth**.

// TODO: Bandstop amplitude response figure

The center frequency point to the frequency with the largest attenuation, the "dip" in the magnitude response of the filter.

The bandwidth determines how wide will the "dip" or "valley" be around the center frequency.

In order for the bandstop filter to sound equally wide in bandwidth at all center frequencies, we often use the **Q** or **quality factor** parameter. It is defined as

Q = BW * f_c,

where BW is the bandwidth in Hz and f_c is the center frequency in Hz.

"Constant-Q" filter allows for a narrower band in the low frequencies (where human hearing is more sensitive to frequency) and for a wider band in the high frequencies (where human hearing is less sensitive to frequency).

Note that we cannot control the amount of attenuation in the band-stop filter. That is possible only in a _peaking (band) filter_, which is not the topic of this article.

## What Is a Bandpass Filter?

A bandpass filter is a filter that attenuates all frequencies beside a specified range.

This range is defined in terms of the **center frequency** and the **bandwidth**, both expressed in Hz.

// TODO: Bandpass amplitude response figure

As in the case of the bandstop filter, we can specify the bandwidth using the **Q** or **quality factor** parameter. Constant-Q filters retain the same "perceptual width" of the passed-through frequency range. The relation between the center frequency, the bandwidth and Q is given by Equation 1.

## Recap: The Second-Order Allpass Filter

The main building block of the bandpass and the bandstop filters is the second-order allpass filter.

An allpass filter is a filter that does not attenuate any frequencies but it introduces a frequency-dependent phase shift.

Let's recap a few facts about this filter.

### Transfer Function

The transfer function of the second-order allpass filter is

H(z) = 

where

c = 

d = 

fb is the break frequency of the filter in Hz, BW is the bandiwidth of the transition band in Hz and fs is the sampling rate in Hz. The **break frequency** specifies the frequency at which the phase shift is -\pi.

### Phase Response

The phase response of the second-order allpass filter is visible in Figure 3.

// TODO: Second-order allpass filter phase response

As you can see, the phase shift is 0 at 0 Hz and gradually changes to -2\pi. The steepness of the phase response is determined by the bandwidth parameter expressed in Hz.

You can already guess that the bandwidth parameter of the second-order allpass filter translates to the bandwidth parameter of the bandpass and bandstop filters. Accordingly, the break frequency corresponds to the center frequency. How?

Thanks to the [phase cancellation effect], if we add two tones at the same frequency but with relative phase shift of \pi, they will cancel each other. A shift by \pi is equivalent to a multiplication of the tone by -1.

With this knowledge we can now employ the second-order allpass filter for bandpass or bandstop filtering.

## Allpass-Based Bandstop Filter

If we add the output of the second-order allpass filter to its input signal, at the break frequency we will obtain a phase cancellation. Why?

At the break frequency, the phase delay is -\pi. Adding two tones at the break frequency with the relative phase shift of \pi, we effectively eliminate them from the resulting signal. As the phase shift deviates from \pi, the cancellation is less and less effective.

### DSP Diagram

Here is the block diagram of the bandstop filter.

// TODO: Bandstop filter diagram

The output of the second-order allpass filter is added to the direct path.

### Magnitude Response

Here is a magnitude transfer function of the bandstop filter from Figure ??? with the center frequency at 250 Hz and Q equal to 0.3.

// TODO: Magnitude transfer function of the bandstop filter

At the center frequency, we get the biggest attenuation which decreases the further away we get from it. We can see how selective in frequency this filter is.

### Real-Time Control

As this filter requires quite easy computations to control the center frequency and the bandwidth, we can alter its parameters in real time.

As an example, here's a white noise signal filtered with the bandstop filter, whose center frequency varies from 50 to 16000 Hz over time.

// TODO: Audio file

To visualize what's happening here, take a look at the spectrogram of the audio file.

// TODO: Spectrogram

On the x-axis we have time, on the y-axis the log-scaled frequency, and the color indicates the amplitude level of the frequency at a specific time point in decibels full-scale (dBFS).

As you can see, the dip travels exponentially from low to high frequencies. Thus, we can hear the so-called "filter sweep".

### Implementation

You will find a sample implementation of the bandstop filter in Python at [the end of this article].

## Allpass-Based Bandpass Filter

The allpass-based bandpass filter differs from the bandstop filter only in the sign of the allpass filter output. In case of the bandpass, we invert the output of the allpass in phase so that the phase cancellation occurs at the 0 Hz frequency and the [Nyquist frequency]. Because the tone at the break frequency gets reversed twice, it is in phase with the input signal.

### DSP Diagram

In Figure ???, there's the block diagram of the presented bandpass filter.

// TODO DSP diagram

The multiplication by 1/2 is just to preserve the [-1, 1] amplitude range of the signal.

### Magnitude Response

In Figure ???, there's the magnitude response of the bandpass filter. 

// TODO: Magnitude response

As you can see, it actually passes through only the frequencies in the specified band.

The uneven slopes of the response result from the logarithmic scaling of the frequency axis; these slopes are identical on the linear scale.

### Real-Time Control

Exactly as the bandstop filter, the bandpass filter can be easily controlled in real time.

Here's an audio sample with a bandpass filtered white noise, where the center frequency varies from 50 Hz to 16000 Hz and Q is equal to 0.3.

// TODO: Audio file

You can observe the effect of the bandpass filter on the spectrogram of the above audio file (Figure ???).

// TODO: Spectrogram

Once again, the y-axis is a log-frequency axis, the x-axis is the time axis, and color intensity corresponds to the sound level in decibels full-scale (dBFS).

### Implementation

Here is a sample Python implementation of both filters: the bandpass and the bandstop. 

The code generates 5 seconds of white noise and then filters them with time-varying bandstop and bandpass filters respectively. The center frequency in both cases changes exponentially from 50 Hz to 16000 Hz (this code was used to generate the previous examples in this article).

The code is heavily commented so you should have no problems in understanding.


// TODO: Include code

## Applications

Apart from just filtering, bandpass and bandstop filters can be used in a variety of audio effects applications.

### Filter Sweep

Filter sweep is a very strong effect that can add a powerful character to the sound. 

### Hear band (in filters)

### Phaser

If we modulate the center frequency of the bandstop filter over time, for example, using a low-frequency oscillator (LFO), we can easily obtain the phaser effect.

The actual application of the phaser effect will be a topic of an another article, but you can already experiment with the attached implementation code!

## Summary

In this article, we learned how to implement efficient, real-time-controllable bandpass and bandstop filters using the second-order allpass filter.

Bandpass and bandstop filters are one of the basic effects in the audio programmer's arsenal. If you want to know which elements make up the audio plugin developer toolbox, check out my free [audio plugin developer checklist.]