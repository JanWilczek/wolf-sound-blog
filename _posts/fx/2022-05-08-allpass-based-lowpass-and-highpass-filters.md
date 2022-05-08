---
title: "Allpass-Based Lowpass and Highpass Filters"
description: "Learn how to design and implement easily controllable and efficient lowpass and highpass filters."
date: 2022-05-08
author: Jan Wilczek
layout: post
images: /assets/img/posts/fx/2022-05-08-allpass-based-lowpass-and-highpass-filters/
images_parametric_eq: /assets/img/posts/fx/2021-11-26-parametric-eq-design/
# background: /assets/img/posts/fx/2022-05-08-allpass-based-lowpass-and-highpass-filters/Thumbnail.webp
categories:
  - Digital Signal Processing
  - Audio FX
tags:
  - filtering 
  - effects
  - Python
discussion_id: 2022-05-08-allpass-based-lowpass-and-highpass-filters
---
Control the cutoff with just one coefficient!

{% katexmm %}
{% capture _ %}{% increment equationId20211126  %}{% endcapture %}
{% capture _ %}{% increment figureId20211126  %}{% endcapture %}

You have probably seen it: a low-pass filter digital audio workstation (DAW) plugin.

It could have had a roll-off and a resonance control knob or slider.

But it definitely had the **cutoff frequency control**.

If you learned a little bit about digital signal processing (DSP), you may have come across formulas for different types of filters. However, these formulas typically require to have all their coefficients recalculated as soon as the cutoff frequency changes. That means that their real-time control is inefficient, computationally speaking.

*How to design and implement a lowpass or a highpass filter, where adjusting the cutoff frequency requires a recalculation of just one parameter?*

That is the topic of this article 🙂

<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6611455743195468"
     crossorigin="anonymous"></script><ins class="adsbygoogle"
     style="display:block; text-align:center;"
     data-ad-layout="in-article"
     data-ad-format="fluid"
     data-ad-client="ca-pub-6611455743195468"
     data-ad-slot="7289385396"></ins><script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>

Let's start with the basics.

## Lowpass Filter

For the purpose of this article, we'll define a lowpass filter as a filter that attenuates frequencies above a certain frequency, called the *cutoff frequency*.

The cutoff frequency is typically defined as the frequency at which the attenuation is already 3 dB.

The frequencies below the cutoff frequency aren't affected by it.

The amplitude response (how each frequency is attenuated at the output of the filter) of a lowpass filter is shown in Figure 1.

![]({{ page.images_parametric_eq | absolute_url | append: "/LowPass.webp"}}){: width="70%" alt="Low-pass filter amplitude response."}
_Figure {% increment figureId20211126  %}. Low-pass filter amplitude response._

## Highpass Filter

Contrary to a lowpass filter, a highpass filter attenuates all frequencies below the cutoff frequency.

The amplitude response of a highpass filter is shown in Figure 2.

![]({{ page.images_parametric_eq | absolute_url | append: "/HighPass.webp"}}){: width="70%" alt="High-pass filter amplitude response."}
_Figure {% increment figureId20211126  %}. High-pass filter amplitude response._

## The Need for a Simple Control-to-Coefficients Mapping

Let's recap a "traditional" method of designing an IIR lowpass filter:

1. Design the analog prototype.
2. Digitize it with the bilinear transform.

For example, in the [bilinear transform tutorial]({% post_url fx/2022-01-15-bilinear-transform %}), we digitized the Butterworth lowpass of order 2. The resulting transfer function formula was

$$H_2(z) = \frac{W^2 + 2W^2 z^{-1} + W^2z^{-2}}{1 + W \sqrt{2} + W^2 + 2(W^2 - 1)z^{-1} + (W^2 - W\sqrt{2} + 1)z^{-2}}, \quad ({% increment equationId20220115 %})$$

where $W = \tan(\omega_\text{c} T / 2)$ and $\omega_\text{c}$ is the desired cutoff frequency of the digital filter in radians per second.

Note that if we change the cutoff frequency $\omega_\text{c}$, we need to calculate 6 filter coefficients!

(A reminder: a filter coefficient is a scalar at each power of the $z$ variable in the numerator and the denominator.)

If we wanted to control the cutoff freqency in real time, for example, during a live performance, or using an amplitude envelope, the computational overhead could be troublesome.

Can we have a simple mapping: 1 filter control change requires 1 coefficient change?

That is the promise of allpass-based parametric filters.

To understand them, we first need to recap a few facts about the allpass filter.

## Allpass Filter Revisited

An *allpass filter* is a filter that does not attenuate or boost any frequencies but introduces a frequency-dependent delay.

That means that a single allpass filter won't introduce any audible change in a signal. Only when we use this filter in some context, can we hear or see its true power.

What is a "frequency-dependent delay"? Well, the higher the frequency, the later it will appear at the filter's output.

<!-- TODO: Amplitude & phase response of an allpass filter figure -->

If this delay was large and we put a signal with a flat spectrum at the input, we could hear a tone rising in frequency at the output; the lowest frequency would appear immediately at the output, whereas the highest would appear last, because it has the largest delay.

In practice, this delay is too small to be audible, we can, however, observe its effect on the waveform in the time domain.

<!-- TODO: An example waveform; a few aligned sines at the input and their misaligment at the output -->

## Phase Cancellation

The *break frequency* of an allpass filter is the frequency at which the phase shift is exactly $-\frac{\pi}{2}$.

We can control the break frequency of an allpass filter of any order with a single coefficient that appears in the simple formulas for the final filter coefficients.

<!-- TODO: Insert allpass filter transfer function formula -->

If you don't understand it now, don't worry; all you need to know is that the break frequency is easily controllable.

<!-- TODO: Insert link to the sampling article -->

Now, at the Nyquist frequency (half of the sampling rate), the phase shift is exactly $-\pi$ so the tone corresponding to that frequency is exactly *inverted in phase*.

(Phase inversion is sometimes marked as $\phi$ in DAWs.)

If we add a signal and its phase-inverted version, a *phase cancellation* will occur; we will obtain an all-zero signal, i.e., silence.

<!-- TODO: Example of sines with phase cancellation figure -->

Phase cancellation means perfect attenuation, right? Could we possibly use this property in a lowpass or highpass filter?

## Allpass-Based Lowpass Filter

What will happen if we add the output of the first-order allpass filter to the original input signal (the so-called *direct path*)? (see Figure ???).

* block diagram
  
Since the phase shift at the Nyquist frequency is $=\pi$, we'll obtain phase cancellation at this frequency.

At the direct current (DC) (frequency of 0 Hz), the output signal is not shifted with respect to the input (the signals are said to be *in-phase*). If we add two sines that have the same frequency and are in phase, we effectively obtain a sine at the same frequency which has the amplitude equal to the sum of amplitudes of the original sines.

In the case of the discussed structure, the DC component at the input and at the output are identical. Therefore, the amplitude of the input DC component will double.

Ok, we know that at the output of the structure from Figure ???, the 0 Hz component will be doubled in amplitude and the Nyquist frequency component will vanish (have amplitude equal to 0). What will happen between these frequencies?

Between these frequencies, the amplitude of sines will be gradually attenuated as the input signal and the output of the allpass filter gradually move out of phase with increasing frequency.

The resulting magnitude transfer function can be seen in Figure ???. We obtained a lowpass filter!

* transfer function

### Cutoff Frequency Control

As I promised, the cutoff frequency of this lowpass filter is very easy to control. We just need to set the $a_1$ coefficient of the allpass filter according to Equation ???, which controls the frequency at which the phase shift of the allpass is exactly $-\frac{\pi}{2}$. The $a_1$ coefficient can then be used as a regular filter coefficient.

We, thus, obtained a one-to-one control to coefficient mapping!

## Allpass-Based Highpass Filter

What if instead of adding the output of the allpass to the input signal, we subtracted it?

The corresponding structure is shown in Figure ???

<!-- TODO: Highpass filter structure -->

By mutliplying the output of the allpass by $-1$ we invert all the components in phase.

Therefore, the frequency component at the Nyquist frequency, which was inverted in phase by the allpass filter, gets inverted again and is back in phase with the corresponding component of the input signal.

So the Nyquist frequency component at the output of the structure in Figure ??? is doubled in amplitude.

Conversely, the DC component, which was previously in phase, is now inverted in phase. Therefore, the DC component is missing in the output signal of the structure from Figure ???.

In between these two frequencies, we get a slow increase in the magnitude of the transfer function with increasing frequency.

The magnitude transfer function can be seen in Figure ???.

* transfer function

We, thus, obtained a high-pass filter!

Its cutoff frequency can again be controlled with just one coefficient as in the lowpass case (because we merely introduced the multiplication by $-1$).

Great, we have just designed easily controllable lowpass and highpass filters! How can we implement them in code?

## Python Implementation

Listing 1 shows the implementation of the allpass-based lowpass/highpass and includes extensive comments.

_Listing 1. Allpass-based lowpass/highpass filter.
```python
#!/usr/bin/python3
from scipy import signal
import numpy as np
import soundfile as sf
from pathlib import Path


def generate_white_noise(duration_in_seconds, sampling_rate):
    duration_in_samples = int(duration_in_seconds * sampling_rate)
    return np.random.default_rng().uniform(-1, 1, duration_in_samples)


def a1_coefficient(break_frequency, sampling_rate):
    tan = np.tan(np.pi * break_frequency / sampling_rate)
    return (tan - 1) / (tan + 1)


def allpass_filter(input_signal, break_frequency, sampling_rate):
    # Initialize the output array
    allpass_output = np.zeros_like(input_signal)

    # Initialize the inner 1-sample buffer
    dn_1 = 0

    for n in range(input_signal.shape[0]):
        # The allpass coefficient is computed for each sample
        # to show its adaptability
        a1 = a1_coefficient(break_frequency[n], sampling_rate)

        # The allpass difference equation
        allpass_output[n] = a1 * input_signal[n] + dn_1

        # Store a value in the inner buffer for the 
        # next iteration
        dn_1 = input_signal[n] - a1 * allpass_output[n]
    return allpass_output


def allpass_based_filter(input_signal, cutoff_frequency, \
    sampling_rate, highpass=False, amplitude=1.0):
    # Perform allpass filtering
    allpass_output = allpass_filter(input_signal, \
        cutoff_frequency, sampling_rate)

    # If we want a highpass, we need to invert 
    # the allpass output in phase
    if highpass:
        allpass_output *= -1

    filter_output = input_signal + allpass_output
    filter_output *= 0.5
    filter_output *= amplitude

    return filter_output


def white_noise_filtering_example():
    sampling_rate = 44100
    duration_in_seconds = 5

    # Generate 5 seconds of white noise
    white_noise = generate_white_noise(duration_in_seconds, sampling_rate)
    input_signal = white_noise

    # Make the cutoff frequency decay with time ("real-time control")
    cutoff_frequency = np.geomspace(20000, 20, input_signal.shape[0])

    # Actual filtering
    filter_output = allpass_based_filter(input_signal, \
        cutoff_frequency, sampling_rate, highpass=False, amplitude=0.1)

    # Store the result in a file
    output_dir = Path('assets', 'wav', 'posts', 'fx', \
        '2022-05-08-allpass-based-lowpass-and-highpass-filters')
    output_dir.mkdir(parents=True, exist_ok=True)
    filename = 'filtered_white_noise.flac'
    sf.write(output_dir / filename, filter_output, sampling_rate)


def main():
    white_noise_filtering_example()


if __name__ == '__main__':
    main()
```

The resulting audio file should sound similar to the following:

<audio controls>
    <source src="/assets/wav/posts/fx/2022-05-08-allpass-based-lowpass-and-highpass-filters/filtered_white_noise.flac"  type="audio/flac">
    Your browser does not support the audio tag.
</audio>

Can you notice how the cutoff frequency lowers over time? We achieved this easily thanks to the one-to-one control-to-coefficient mapping.

## Summary

In this article, we discussed an easy and popular method of obtaining a lowpass or a highpass filter; by combining an allpass filter and a direct path.

The allpass filter delays the input frequency components. The phase delay increases with frequency.

At DC, the phase shift is 0. At the Nyquist frequency the phase shift is $-\pi$.

Adding (subtracting) the allpass output to/from the direct path creates phase cancellation at the Nyquist frequency (DC component). We, thus, obtain a lowpass (highpass) filter.

The real power of this structure can be seen in a real-time implementation... So that's what we'll do next!

{% endkatexmm %}

## Bibliography

[DAFX]