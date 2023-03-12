---
title: "Group Delay vs Phase Delay: What's the Difference?"
description: "The last part of the Android synthesizer app tutorial, where we implement the wavetable synthesis algorithm in C++."
date: 2023-03-12
author: Jan Wilczek
layout: post
images: /assets/img/posts/dsp/2023-03-12-group-delay-vs-phase-delay-whats-the-difference/
# background: /assets/img/posts/synthesis/android-wavetable-synthesizer/Thumbnail.webp
categories:
  - Digital Signal Processing
tags:
  - waveform
  - filtering
discussion_id: 2023-03-12-group-delay-vs-phase-delay-whats-the-difference
custom_js:
 - /assets/vendor/lazyload/lazyload.min.js
 - /assets/js/wolfsound/modules/load_lazyload.js
---
I don’t know about you but I have always been confused about the group delay, phase delay, and sample delay in digital signal processing… Let’s clear this all up once and for all!

1. [What is a sample delay?](#what-is-a-sample-delay)
2. [What is a phase delay?](#what-is-a-phase-delay)
   1. [How to Calculate the Phase Shift from the Transfer Function?](#how-to-calculate-the-phase-shift-from-the-transfer-function)
3. [What is a group delay?](#what-is-a-group-delay)
   1. [How to Calculate Group Delay from the Phase Delay?](#how-to-calculate-group-delay-from-the-phase-delay)
   2. [Example 1](#example-1)
   3. [Example 2](#example-2)
   4. [Where Does the Term “Group Delay” Come From?](#where-does-the-term-group-delay-come-from)
4. [Why Is Constant Group Delay or Linear Phase Important?](#why-is-constant-group-delay-or-linear-phase-important)
5. [Summary](#summary)
6. [Bibliography](#bibliography)

<script defer src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6611455743195468"
     crossorigin="anonymous"></script><ins class="adsbygoogle"
     style="display:block; text-align:center;"
     data-ad-layout="in-article"
     data-ad-format="fluid"
     data-ad-client="ca-pub-6611455743195468"
     data-ad-slot="7289385396"></ins><script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>

{% katexmm %}
{% capture _ %}{% increment equationId20230312  %}{% endcapture %}
{% capture _ %}{% increment figureId20230312  %}{% endcapture %}

## What is a sample delay?

The first one to start off is the sample delay.

A system that delays the input by a constant number of samples introduces a delay to the signal.

Whenever you see the $z^{-1}$ delay block in a DSP diagram or in a difference equation, it delays the signal by 1 sample.

Let’s look at an example.

Here, we have a signal $x[n]$.

![two_sines_signal.png](Article%2034787530836545b7926d763403eda854/two_sines_signal.png)

What happens to it if we delay it by 4 samples?

![delayed_two_sines_signal.png](Article%2034787530836545b7926d763403eda854/delayed_two_sines_signal.png)

As you can see, at the output of the delay, the signal is simply delayed by 4 samples.

Remember that by the sample delay of a system, we refer to the delay of the whole signal by some number of samples between the output and the input. However, there may not be any other change in the signal for this to hold. Thus, only pure delays can introduce a delay in samples.

## What is a phase delay?

Let’s consider once again the output of the system delayed by 4 samples.

![delayed_two_sines_signal.png](Article%2034787530836545b7926d763403eda854/delayed_two_sines_signal%201.png)

This signal consists of 2 sines: one of them has its period equal to 16 samples and the other one has its period equal to 8 samples.

![sine1_signal.png](Article%2034787530836545b7926d763403eda854/sine1_signal.png)

![sine2_signal.png](Article%2034787530836545b7926d763403eda854/sine2_signal.png)

If you don’t know what the period of a signal is, it’s the smallest positive number of samples after which the signal starts repeating itself. For example, the period of the “2-sine” signal is 16 samples.

Both sines inside the signals were delayed by the same number of samples. But how did their phase advance?

The **phase** of a sine is a value in the $[0, 2\pi)$ range. The period of a sine is equal to $2\pi$. So its phase tells us at which point in the period we are.

For the sine, whose period is 8 samples, 4 samples are half of its period. Therefore, 4 samples correspond to a shift of its argument (phase) by $\pi$ (half of the $2\pi$ period). Thus, the phase delay (or phase shift) of this sine is $\pi$.

However, for the sine, whose period is 16 samples, 4 samples are just one quarter of its period. Therefore, 4 samples correspond to a phase delay of $\frac{1}{4} \cdot 2\pi = \frac{\pi}{2}$.

See? A delay in samples means different phase delays for different sines. To calculate the phase shift of a sine given its sample delay or vice versa, we need to know the period or the frequency of the sine.

### How to Calculate the Phase Shift from the Transfer Function?

If we have the transfer function of a digital system or its frequency response $H(e^{j\omega})$, we can easily calculate its phase response as

$$
\begin{equation}\arg H\left(e^{j\omega}\right),\quad
\end{equation}
$$

where $\arg$ returns the principal argument of the given complex number in radians. The principal argument is always in the $(-\pi, \pi]$ range. Therefore, this phase is also called the **wrapped phase** because it is wrapped to the $(-\pi, \pi]$ range.

Here is an example phase response plot. It is the phase response of the second-order Butterworth IIR lowpass filter with the cutoff frequency set to $\frac{1}{4}$ of the Nyquist frequency.

![butterworth_lp2_phase_response.png](Article%2034787530836545b7926d763403eda854/butterworth_lp2_phase_response.png)

As you can see, this phase response is clearly nonlinear; in fact, all IIR filters have nonlinear phase.

Ok, we know what is the sample delay and the phase delay. Then, what is the group delay?

## What is a group delay?

“Group delay” is probably the most misleading term in the history of DSP but I admit, it does make sense.

To understand the group delay let’s look at an example.

In a pure delay system, all frequency components at the input are delayed by a constant number of samples.

What if each frequency was delayed by a different number of samples?

To use our “2-sine” signal again, let’s say that we delay the sine with the period equal to 8 samples by 4 samples and the sine with the period equal to 16 samples by 8 samples.

Here you can see the output of the described frequency-dependent delaying system.

![phase_delayed_two_sines_signal.png](Article%2034787530836545b7926d763403eda854/phase_delayed_two_sines_signal.png)

Looking at the sines separately, at the output of this system the delayed sines look as follows.

![delayed_sine1_signal.png](Article%2034787530836545b7926d763403eda854/delayed_sine1_signal.png)

![delayed_sine2_signal.png](Article%2034787530836545b7926d763403eda854/delayed_sine2_signal.png)

What is interesting, now both sines have the same phase delay, $\pi$. However, you can see that the output looks different visually from the input although these are still those two sines; if you’re unsure, check the first nonzero samples of the delayed signal. The relative position of the sines changed and, thus, the waveform changed.

As you might guess at this point, the **group delay** is exactly the number of samples by which a single frequency component is delayed.

In our example, the group delay of the frequency corresponding to period 8 is 4 and the group delay of the frequency corresponding to period 16 is 8.

In the previous example, where the whole input was delayed by 4 samples, you saw that if the group delay is constant for all frequencies, the system does not alter the waveform visually, it simply delays it; we get a delay system from the definition of the sample delay.

### How to Calculate Group Delay from the Phase Delay?

Group delay can be easily calculated from the phase delay of the system

$$
\begin{equation}
\text{grd}\left[ H(e^{j\omega})\right] = - \frac{d}{d\omega}\{\arg H\left(e^{j\omega}\right)\},
\end{equation}
$$

where

- $H(e^{j\omega})$ is the complex frequency response of the system,
- $\arg H(e^{j\omega})$ is its phase response, and
- $\frac{d}{d\omega}$ denotes the derivative with respect to the angular frequency $\omega$ in radians per sample ($\omega = 2\pi f / f_s$, where $f$ is a frequency in Hz and $f_s$ is the sampling rate).

### Example 1

Let’s look at an example of a constant-group delay filter.

Here is the phase response of our delay by 4 samples.

![delay_by_4_phase_response.png](Article%2034787530836545b7926d763403eda854/delay_by_4_phase_response.png)

You can see that the phase is wrapped: when it reaches $-\pi$ it jumps up to $\pi$.

If we unwrap the phase, the phase response looks as follows.

![delay_by_4_unwrapped_phase_response.png](Article%2034787530836545b7926d763403eda854/delay_by_4_unwrapped_phase_response.png)

By the way, these plots were obtained using [scipy.signal.freqz](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.freqz.html), [numpy.angle](https://numpy.org/doc/stable/reference/generated/numpy.angle.html), [numpy.unwrap](https://numpy.org/doc/stable/reference/generated/numpy.unwrap.html), and the [matplotlib](https://matplotlib.org/stable/index.html) library 🙂

The derivative of the phase response with respect to the frequency is simply the tilt coefficient of this linear function. In this case, the derivative is constant at each frequency $\omega$ (because the phase is linear) and can be calculated from the grid. Therefore, the group delay of this filter (negated derivative) is equal to $-\frac{-4\pi}{\pi} = -(-4) = 4$. We obtained the group delay at each frequency: it is constant and equal to 4. Therefore, this system is a delay of 4 samples. And indeed it has linear phase.

*Note: You can also calculate the group delay from the analytical form of the phase response. In the case of a pure delay of 4, the frequency response is $e^{-j4\omega}$ so the phase response is $-4\omega$. Thus, the negated derivative is 4.*

### Example 2

Here is the plot of the gourp delay of the second-order Butterworth IIR lowpass filter with the cutoff frequency set to $\frac{1}{4}$ of the Nyquist frequency whose phase response you’ve seen in Figure ???.

![butterworth_lp2_group_delay.png](Article%2034787530836545b7926d763403eda854/butterworth_lp2_group_delay.png)

This group delay was calculated with the [scipy.signal.group_delay](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.group_delay.html) function.

As you can see, a nonlinear phase response resulted in a non-constant group delay.

### Where Does the Term “Group Delay” Come From?

The group delay takes its name from the continuous frequency domain. Mathematically speaking, group delay describes the time delay of an infinitesimally small range of frequencies around some particular frequency $\omega$. This range of frequencies can also be called a “group” of frequencies, hence the name group delay. Clever, I know 😉

## Why Is Constant Group Delay or Linear Phase Important?

If a system has **linear phase**, it means that its phase response is a linear function of angular frequency, typically of the form $-\omega t_0$.

If a system has linear phase, it has constant group delay $t_0$, which can be easily calculated by inserting $\arg H\left(e^{j\omega}\right) =-\omega t_0$ into Equation 2.

Well, if a system has constant group delay, then it means that it does not alter the input waveform visually; its behavior can be represented as a frequency-dependent amplitude scaling and a frequency-independent delay. The output of such a system will be very similar to its input.

Why is it important? Well, as you could for the 2 sines example, the change in the outlook of the signal can be drastic. Also such drastic changes make the outcome less predictable when we start mixing multiple signals together. If the group delay is not constant we may run into phase cancellation issues.

That’s why everyone prefers linear phase (=constant group delay) systems.

Unfortunately, only finite impulse response (FIR) filters can have linear phase… But that’s a topic for another article 😎

## Summary

In this article, you learned what is sample delay, phase delay, and group delay. You now know what is the difference between these three.

You also learned that systems (filters) with linear phase have constant group delay so their effect on the system can be described by a frequency-dependent gain and a frequency-independent delay in samples. Systems with linear phase are more predictable and, thus, more desirable.

With this knowledge you won’t be confused again when you stumble upon one of these “delay” terms!

If you want to know which other bits and pieces of knowledge are necessary for writing software that processes sound, check out my [free Audio Plugin Developer Checklist](https://thewolfsound.com/checklist/)!

## Bibliography

[OppenheimSchafer10] [Alan V Oppenheim, Ronald W. Schafer, *Discrete-Time Signal Processing*, 3rd Edition, Pearson 2010.](https://amzn.to/3vygXGl)

{% endkatexmm %}
