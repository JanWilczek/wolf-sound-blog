---
title: "Allpass Filter: All You Need To Know"
description: "Condensed knowledge on the digital allpass filter: all necessary definitions, diagrams, equations, and applications clearly explained."
date: 2021-10-22
author: Jan Wilczek
layout: post
images: /assets/img/posts/fx/2021-10-22-allpass-filter
background: /assets/img/posts/fx/2021-10-22-allpass-filter/first_order_allpass_filter.webp
categories:
  - Audio FX
  - Digital Signal Processing
tags:
  - effects
  - filtering
discussion_id: 2021-10-22-allpass-filter
---
What is an allpass filter? What is it used for?

<iframe width="560" height="315" src="https://www.youtube.com/embed/AKMoKWYGe8I" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

An *allpass filter* is a filter with a **unity gain across all frequencies**. This means that no frequency passing through that filter will be boosted or attenuated. It introduces, however, a *frequency-dependent delay*. 

So although the output of an allpass filter doesn't sound different from the input, this simple structure used in conjunction with other elements has an incredible power, which is present in almost all music software.

A digital allpass filter can be implemented as a finite-impulse response (FIR) filter or an infinite-impulse response (IIR) filter, typically of the first or the second order. Its applications are manifold: it is used to implement

* artificial reverberation,
* filters (e.g., highpass, lowpass, notch),
* audio effects (e.g., phaser),
* phase equalization, and more.

In this article, we will discuss the digital allpass filter in detail, present its various forms, provide their characteristics, schematics, and implementation, and, finally, discuss how you can use the allpass filter in your musical software like VST or AAX plugins.

<div class="card summary">
  <div class="card-body">
  <h5 class="card-title">In Short</h5>
  <h6 class="card-subtitle mb-2 text-muted">Allpass Filter</h6>
    <ul>
    <li>An allpass filter has gain equal to 1 at all frequencies.</li>
    <li>It delays all frequency components of the input, each by its own phase shift.</li>
    <li>It comes in various forms, but the most popular are first- and second-order IIR forms.</li>
    <li>It is a building block of a huge number of audio processing algorithms, like reverbs or filters.</li>
    </ul>
  </div>
</div>

## Table of Contents

2. [Definition of an Allpass Filter](#definition-of-an-allpass-filter)
3. [Types of Allpass Systems](#types-of-allpass-systems)
   1. [FIR Allpass System](#fir-allpass-system)
   2. [First-Order IIR Allpass](#first-order-iir-allpass)
      1. [Implementation](#implementation)
      2. [Magnitude Response](#magnitude-response)
      3. [Phase Response](#phase-response)
      4. [Derive It Yourself?](#derive-it-yourself)
      5. [Properties of the First-Order Allpass Filter](#properties-of-the-first-order-allpass-filter)
      6. [Cascading Allpass Filters](#cascading-allpass-filters)
   3. [Second-Order IIR Allpass](#second-order-iir-allpass)
      1. [Phase Response](#phase-response-1)
      2. [Implementation](#implementation-1)
      3. [Properties of the Second-Order Allpass Filter](#properties-of-the-second-order-allpass-filter)
   4. [Higher-Order IIR Allpass Filter](#higher-order-iir-allpass-filter)
4. [Applications of Allpass Filters](#applications-of-allpass-filters)
   1. [Reverberation](#reverberation)
   2. [Parametric Equalizer](#parametric-equalizer)
   3. [Phaser](#phaser)
   4. [Phase Equalization](#phase-equalization)
5. [Example Allpass VST Plugin](#example-allpass-vst-plugin)
6. [Summary](#summary)
7. [Bibliography](#bibliography)


{% capture _ %}{% increment equationId20211022  %}{% endcapture %}
{% capture _ %}{% increment figureId20211022  %}{% endcapture %}

## Definition of an Allpass Filter

> An allpass filter is a filter which does not change the magnitude of any frequency component that passes through it [2].

Formally, if we denote the transfer function of an allpass filter by $H_\text{AP}(j\omega)$, we can write $|H_\text{AP}(j\omega)| = 1$. Here, $\omega = 2 \pi f / f_s$, where $f$ is a frequency in Hz and $f_s$ is the sampling rate in Hz.

But wait, since the magnitude does not change, what do we need allpass filters for? We need them, because they introduce a **frequency-dependent phase delay**. In other words, we are able to manipulate the phase of the frequency components without altering their magnitude.

*Note: A **transfer function** of a digital filter is a [Fourier transform]({% post_url collections.posts, '2021-03-18-convolution-in-popular-transforms' %}#fourier-transform) or a [$z$-transform]({% post_url collections.posts, '2021-03-18-convolution-in-popular-transforms' %}#z-transform) of its impulse response. We denote them by $H(j\omega)$ and $H(z)$ respectively.*


{% render 'google-ad.liquid' %}

## Types of Allpass Systems

There are many types of systems that have the *allpass property*. They can be roughly divided into FIR and IIR categories.

### FIR Allpass System

The simplest allpass filter is the [delay]({% post_url collections.posts, '2021-04-01-identity-element-of-the-convolution' %}#delay) [4]

$$H_\text{AP}(z) = \pm z^{-K}, \quad ({% increment equationId20211022 %})$$

where $K$ is an integer not smaller than 0, $K \geq 0$. Note that a unit delay $H_\text{AP}(z) = z^{-1}$ is also an allpass filter. Phase can be unaltered or inverted (multiplication by 1 or -1 respectively), because we are operating in the real domain.

![]({{ images | append: "/fir_allpass.webp" }}){: width="80%" alt="Block diagram of the FIR allpass filter."}
_Figure {% increment figureId20211022 %}. Block diagram of an FIR allpass filter._

[A broader description of the properties of the delay can be found in my article]({% post_url collections.posts, '2021-04-01-identity-element-of-the-convolution' %}#delay).

### First-Order IIR Allpass

A first-order IIR allpass filter is given by the following transfer function [2,3,4]

$$H_{\text{AP}_1}(z) = \frac{a_1 + z^{-1}}{1 + a_1z^{-1}}, \quad ({% increment equationId20211022 %})$$

where $a \in \mathbb{R}$, because we consider real-valued filters only. The above equation corresponds to the following difference equation

$$y[n] = a_1 x[n] + \underbrace{x[n - 1] - a_1 y[n-1]}_{d[n-1]}, \quad ({% increment equationId20211022 %})$$

where $x[n]$ is the input signal, $y[n]$ is the output signal, and $d[n-1]$ can be stored in a buffer as an intermediate value (a small implementation tip for you 😉).

#### Implementation

The difference equation 3 is equivalent to the following DSP diagram.

![]({{ images | append: "/first_order_allpass_filter.webp" }}){: alt="Block diagram of the first-order allpass filter."}
_Figure {% increment figureId20211022 %}. Block diagram of the first-order allpass filter._

How to see the equivalence? First, observe that we have here a combination of two comb filters: a feedback and a feedforward comb filter [4].

Feedback comb filter difference equation:

$$v[n] = x[n] - a_1 v[n-1]. \quad ({% increment equationId20211022 %})$$

Feedforward comb filter difference equation:

$$y[n] = a_1 v[n] + v[n-1]. \quad ({% increment equationId20211022 %})$$

Second, insert $v[n]$ from Eq. 4 into Eq. 5:

$$y[n] = a_1 x[n] - a_1^2 v[n-1] + v[n-1]. \quad ({% increment equationId20211022 %})$$

Finally, replace the first $v[n-1]$ with $\frac{y[n-1] - v[n-2]}{a_1}$ (from Eq. 5) and the second $v[n-1]$ with $x[n-1] - a_1 v[n-2]$ (from Eq. 4):

$$y[n] = a_1 x[n] - a_1^2 \frac{y[n-1] - v[n-2]}{a_1} + x[n-1] - a_1 v[n-2] 
\newline = a_1 x[n] - a_1 y[n-1] + x[n-1], \quad ({% increment equationId20211022 %})$$

which is equivalent to Eq. 3.

#### Magnitude Response

Why is this system allpass? Let's calculate its magnitude transfer function at the unit circle, i.e., its magnitude frequency response or $\Bigl\lvert H_{\text{AP}_1}(z) \Bigr\rvert$ for $z = e^{j\omega}$.

$$\Bigl\lvert H_{\text{AP}_1}(j\omega) \Bigr\rvert = \Bigl\lvert \frac{a_1 + e^{-j\omega}}{1 + a_1e^{-j\omega}} \Bigr\rvert = \Bigl\lvert e^{-j\omega} \frac{a_1e^{j\omega} + 1}{a_1e^{-j\omega} + 1} \Bigr\rvert
= \bigl\lvert e^{-j\omega} \bigr\rvert \Bigl\lvert \frac{\overline{a_1 e^{-j\omega} + 1}}{ a_1 e^{-j\omega} + 1} \Bigr\rvert = 1,  \quad ({% increment equationId20211022 %})$$

where $\overline{z}$ denotes the complex conjugate of $z$. We used the facts that $ \Bigl\lvert e^{-j\omega} \Bigr\rvert = 1$ and $ \Bigl\lvert \frac{\overline{z}}{z} \Bigr\rvert = 1$.

#### Phase Response

What is the role of the $a_1$ (*allpass*) coefficient? It controls the *break frequency* of the allpass filter. What is the break frequency? It is the frequency at which the phase shift of the first-order allpass filter is exactly $-\frac{\pi}{2}$ rad. To understand the break frequency we need to look at the phase frequency response of the allpass filter.

![]({{ images | append: "/first_order_allpass_phase_response.webp" }}){: width="80%" alt="Phase response of the first-order allpass filter."}
_Figure {% increment figureId20211022 %}. Phase response of a first-order allpass filter for different break frequencies $f_\text{b}$._

We here refer to the digital frequency, i.e., the ratio of the frequency $f$ in Hz to the sampling rate $f_s$ in Hz.

The blue dashed lines in the figure mark the break frequencies of particular curves. The red line marks the phase shift by $-\frac{\pi}{2}$ rad. If we want to set a desired break frequency $f_\text{b}$ in radians, we can use the following formula to compute the $a_1$ coefficient [3,4,5]

$$a_1 = \frac{\tan(\pi f_\text{b} / f_s) - 1}{\tan(\pi f_\text{b} / f_s) + 1}.  \quad ({% increment equationId20211022 %})$$

How are Equations 2 and 9 derived? They are the result of transforming an *analog allpass filter* to the digital domain via the *bilinear transform*. Explaining this process is beyond the scope of this article; if you are interested, check out [a great explanation in [4]](https://ccrma.stanford.edu/~jos/pasp/Classic_Virtual_Analog_Phase.html). After the derivations, we arrive exactly at the transfer function from Equation 2 with the coefficient $a_1$ given by Equation 9.

How are the plots in the above figure generated? They are derived from the [argument (in the complex numbers sense)](https://en.wikipedia.org/wiki/Argument_(complex_analysis)) of the allpass transfer function $H_{\text{AP}_1}(j\omega)$. It can be done in software using the `freqz` function of [Matlab](https://www.mathworks.com/help/signal/ref/freqz.html) or [`scipy.signal`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.freqz.html). Alternatively, you can use the following out-of-the-box formula [5]

$$\text{Phase shift}(f) = - 2 \pi f / f_s + 2 \arctan \left( \frac{a_1 \sin (2 \pi f / f_s)}{1 + a_1 \cos (2 \pi f / f_s)} \right).  \quad ({% increment equationId20211022 %})$$

#### Derive It Yourself?

Why am I saying that the formula in Equation 10 is out-of-the-box? I wasn't able to derive it myself. After manual calculations, however, I managed to obtain a formula which was equivalent in terms of the plots. Comparison against `freqz` also yielded an identical result.

Do you know how to derive Equation 10? If so, please, let me know in the comments!

#### Properties of the First-Order Allpass Filter

When you look at the figure with the phase response of the first-order allpass filter, you can read out interesting properties.

* The phase shift at DC ($f = 0$) is 0.
* The phase shift at the Nyquist frequency ($f / f_s = 0.5$) is $-\pi$ rad and is **always** the maximum phase delay.
* The phase shift at the break frequency $f_\text{b}$ is $-\frac{\pi}{2}$ rad.

#### Cascading Allpass Filters

Arranging allpass filters in a series results in the **summation of phase delays**. We can therefore obtain a phase delay of $-N \pi$ at $f / f_s = 0.5$ by cascading $N$ first-order allpass filters. This principle underlies the [phaser algorithm](#phaser).

### Second-Order IIR Allpass

The second-order IIR allpass filter has the following transfer function [3]:

$$H_{\text{AP}_2}(z) = \frac{-c + d(1-c) z^{-1} + z^{-2}}{1 + d(1-c) z^{-1} - c z^{-2}},  \quad ({% increment equationId20211022 %})$$

where the parameter $d$ controls the break (center, cutoff) frequency of the filter $f_\text{b}$ (at which the phase shift is $-\pi$) and the parameter $c$ is computed from the parameter $BW$ which determines the bandwidth (the steepness of the slope of the phase transition around the break frequency). The relations between these parameters are specified by the equations

$$c = \frac{\tan(\pi BW / f_s) - 1}{\tan(\pi BW / f_s) + 1},  \quad ({% increment equationId20211022 %})$$

$$d = - \cos(2\pi f_\text{b} / f_s),  \quad ({% increment equationId20211022 %})$$

where $f_s$ is the sampling rate. Parameters $BW$, $f_\text{b}$, and $f_s$ are given in Hz.

Note how $BW$ is coupled with $c$ but not with $d$ and $f_\text{b}$ is coupled with $d$ but not with $c$. This allows us to smoothly control our filter's properties.

#### Phase Response

The phase response of the second-order allpass filter with different break frequencies $f_\text{b}$ looks as follows:

![]({{ images | append: "/second_order_allpass_phase_response.webp" }}){: width="80%" alt="Phase response of the second-order allpass filter with constant bandwidth."}
_Figure {% increment figureId20211022 %}. Phase response of a second-order allpass filter for different break frequencies frequencies $f_\text{b}$ and bandwidth $BW / f_s = 0.022$._

As you can see above, the break frequency determines the point of the phase shift by $-\pi$. All slopes, however, have the same curvature.

If instead, we keep the break frequency constant and change the bandwidth parameter, we obtain the following phase responses:

![]({{ images | append: "/second_order_allpass_phase_response_break.webp" }}){: width="80%" alt="Phase response of the second-order allpass filter with constant break frequency."}
_Figure {% increment figureId20211022 %}. Phase response of a second-order allpass filter for different bandwidths $BW$ and break frequency $f_\text{b} / f_s = 1/8$._

The curvature of the slope gets milder with the increasing $BW$ parameter but the $-\pi$ shift point remains at the same frequency.

What do these plots really show? They show that **the second-order allpass filter is an incredibly flexible tool**. We can independently change meaningful parameters such as the break frequency or the bandwidth while ensuring the filter's stability. This property is crucial for implementing parametric filters (parametric equalizer, EQ), because we want to be able to change a filter's properties in an intuitive and safe manner.

#### Implementation

The difference equation of the second-order allpass is [3]

$$v[n] = x[n] - d(1 - c)v[n-1] + c v[n-2],  \quad ({% increment equationId20211022 %})$$
$$y[n] = -c v[n] + d (1-c) v[n-1] + v[n-2].  \quad ({% increment equationId20211022 %})$$

If that seems complicated, a diagram should make it clear 🙂

![]({{ images | append: "/second_order_allpass_filter.webp" }}){: alt="Block diagram of the second-order allpass filter."}
_Figure {% increment figureId20211022 %}. Block diagram of the second-order allpass filter._

#### Properties of the Second-Order Allpass Filter

The second-order allpass filter has the following properties:

* The phase shift at DC ($f = 0$) is 0.
* The phase shift at the Nyquist frequency ($f / f_s = 0.5$) is $-2 \pi$ rad and is **always** the maximum phase delay.
* The phase shift at the break frequency $f_\text{b}$ is $-\pi$ rad.
* We can control the break frequency $f_\text{b}$ and the bandwidth $BW$ independently. This is not possible with the first-order allpass: there, the higher the break frequency, the less steep the slope.

### Higher-Order IIR Allpass Filter

You may have noticed a kind of symmetry in Equations 2 and 11. Indeed, it turns out that every IIR allpass filter must have a transfer function of the form [4]

$$H_\text{AP} (z) = \pm z^{-K} \frac{\tilde{A}(z)}{A(z)},  \quad ({% increment equationId20211022 %})$$

where $K \in \mathbb{Z}$, $K \geq 0$, $A(z) = 1 + a_1 z^{-1} + a_2 z^{-2} + \dots + a_N z^{-N}$, and $\tilde{A}(z) = z^{-N} A(z^{-1})$. In other words, $\tilde{A}(z)$ is obtained by reversing the polynomial coefficients of $A(z)$. 

Note that we added here a possible phase inversion and an additional delay. Thus, this formulation is 100% general and can be applied to every real-valued case.

However, higher-order allpass filters are rarely used in practice of audio programming, because their usage requires complicated analysis and, in most cases, first- and second-order IIR allpass filters suffice.

## Applications of Allpass Filters

Although for the single-channel audio, we cannot hear the effect of the phase delay, allpass filters are incredibly useful in musical applications. Why?

* They are stable.
* They have a meaningful parameters-to-coefficients mapping (e.g., break frequency to the $d$ coefficient in the second-order allpass).
* They are computationally efficient.
* Their properties are well-examined.

How can we use them in audio processing? For example, what happens if we add two sines at the same frequency: one delayed by $-\pi$ with respect to the other? They cancel out (*destructive interference*) and the output is zero. 

Where can we use the properties of allpass filters? Below are some **selected** applications.

### Reverberation

Allpass filters are heavily used in artificial reverberation: an effect creating the impression of listening to music in some space (e.g., a room, a concert hall) [4]. Allpass filters are present in some established approaches to simulate reverberation.

The [**Schroeder reverberator**](https://ccrma.stanford.edu/~jos/pasp/Schroeder_Reverberators.html) consists of a series of allpass filters, a parallel bank of feedback comb filters, and a mixing matrix [4]. It was proposed as early as 1962!

The [**Freeverb**](https://ccrma.stanford.edu/~jos/pasp/Freeverb.html) algorithm uses a parallel bank of feedback comb filters and a series of allpass filters [4].

*Note: If you are interested in how to implement the Freeverb using Rust, check out [this video](https://www.youtube.com/watch?v=Yom9E-67bdI&ab_channel=JUCE) with Ian Hobson (ex-Ableton).*

### Parametric Equalizer

Have you ever wondered, how are highpass, lowpass, shelving, notch or bandpass filters implemented in digital audio workstation (DAW) plugins? Well, I bet most of them use the [RBJ Cookbook](https://webaudio.github.io/Audio-EQ-Cookbook/audio-eq-cookbook.html) as a foundation. The RBJ Cookbook is a set of recipes for stable, controllable, and efficient filters of any type. It turns out, that all these recipes use first- or second- order allpass filters underneath! More details on how to derive these formulae can be found in [3]... but I hope you will be able to read about them on WolfSound as well soon 🙂.

### Phaser

Do you know what's the effect applied to guitars on [Van Halen's Eruption](https://www.youtube.com/watch?v=M4Czx8EWXb0&ab_channel=VanHalen-Topic)? That's a *phaser*: an effect that sweeps notches through the spectrum of the input signal. One of the ways to implement a digital phaser is to use a chain of allpass filters, whose output is summed with the unfiltered input signal [3,4,5].

### Phase Equalization

Different microphones may introduce different frequency-dependent delays. Mixing their signals via summation could cause phase cancellation regardless of whether we invert the phase of one of the signals or not. We can prevent it only by selectively adjusting the phase delay of the frequency components of one of these signals. What is the system that can change the phase delay without changing the magnitude of a frequency component? I hope that you know the answer by now 🙂.

## Example Allpass VST Plugin

In [Reaper's ReaEQ VST plugin](https://www.reaper.fm/reaplugs/), there is an allpass filter available.

![]({{ images | append: "/ReaEQAllpass.webp" }}){: width="80%" alt="ReaEQ plugin window with the allpass filter selected."}
_Figure {% increment figureId20211022 %}. Allpass filter in the Reaper's ReaEQ VST plugin._

How to observe the frequency-dependent phase cancellation with a parallel allpass? Here's a quick tutorial:

![]({{ images | append: "/ReaEQAllpassAppliedMaster.webp" }}){: alt="Application of a parallel allpass filter with ReaEQ to create a notch."}
_Figure {% increment figureId20211022 %}. Application of a parallel allpass filter with ReaEQ to create a notch._

Steps to reproduce:

1. Load an audio track to Reaper and duplicate it.
1. Add [Reaper's ReaEQ VST plugin](https://www.reaper.fm/reaplugs/) to *one* of the tracks.
1. Open the plugin and remove all but 1 frequency bands.
1. Change the type of the remaining frequency band to "All Pass".
1. While listening to the master track, change the "Frequency [Hz]" parameter of the allpass. Can you hear the notch in the frequency spectrum?
1. You can also load ReaEQ on the master track and observe the notch there.

Have fun! 🎧

## Summary

In this article, we have discussed an allpass filter. Now, you understand

* what is an allpass filter,
* what types of musically useful allpass filters exist,
* how to implement them,
* how they are applied in various effects,
* how to use an allpass filter in a DAW.

Thank you for reading! If you enjoyed the article and want to learn even more, [sign up for my newsletter]({% link collections.all, 'newsletter.md' %})! You will become an expert in digital audio effects without the need to read thick books on DSP.

If you have any questions, don't hesitate to ask them below!

## Bibliography

[1] [Alan V. Oppenheim, Alan S. Willsky, with S. Hamid *Signals and Systems*, 2nd Edition, Pearson 1997.](https://amzn.to/3m2tZsd)

[2] [Alan V Oppenheim, Ronald W. Schafer, *Discrete-Time Signal Processing*, 3rd Edition, Pearson 2010.](https://amzn.to/3vygXGl)

[3] [Zölzer, U., *DAFX: Digital Audio Effects*, 2nd ed. Helmut Schmidt University – University of the Federal Armed Forces, Hamburg, Germany: John Wiley & Sons Ltd, 2011.](https://amzn.to/3aZIxT8)

[4] [J. O. Smith, *Physical Audio Signal Processing*, online book, 2010 edition. Retrieved October 19, 2021.](http://ccrma.stanford.edu/~jos/pasp/)

[5] [R. Kiiski, F. Esqueda, and V. Välimäki, *Time-Variant Gray-Box Modeling of a Phaser Pedal*, in Proceedings of the 19th International Conference on Digital Audio Effects (DAFx-16), Brno, Czech Republic, September 5–9, pp. 121–128, 2016.](https://www.dafx.de/paper-archive/2016/dafxpapers/05-DAFx-16_paper_42-PN.pdf)

{% include 'affiliate-disclaimer.html' %}


