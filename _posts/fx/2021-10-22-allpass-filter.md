---
title: "Allpass Filter: All You Need To Know"
description: "Condensed knowledge on the digital allpass filter: all necessary definitions, diagrams, equations, and applications clearly explained."
date: 2021-10-22
author: Jan Wilczek
layout: post
images: assets/img/posts/fx/2021-10-22-allpass-filter
categories:
  - Audio FX
  - Digital Signal Processing
tags:
  - effects
  - filters
discussion_id: 2021-10-22-allpass-filter
---
What is an allpass filter? What is it used for?

An *allpass filter* is a filter with a **unity gain across all frequencies**. This means that no frequency passing through that filter will be boosted or attenuated. It introduces, however, a *frequency-dependent delay*. 

So although the output of an allpass filter doesn't sound different from the input, this simple structure used in conjunction with other elements has an incredible power which is present in almost all music software.

A digital allpass filter can be implemented as finite impulse response (FIR) filters or infinite impulse response (IIR) filters, typically of first or second order. It applications are manifold: it used to implement

* reverb
* basic filters (highpass, lowpass, notch),
* audio effects (e.g., phaser),
* phase equalization, and more.

In this article, we will discuss the digital allpass filter in detail, present its various forms, provide their characteristics, schematics, and implementation, and, finally, discuss how you can use it in your musical software like VST plugins.

<div class="card summary" style="width: 36rem;">
  <div class="card-body">
  <h5 class="card-title">In Short</h5>
  <h6 class="card-subtitle mb-2 text-muted">Allpass Filter</h6>
    <ul>
    <li>Allpass filter has gain equal to 1 at all frequencies.</li>
    <li>It delays all frequency components of the input, each with by its own phase shift.</li>
    <li>It comes in various forms, but the most popular are first- and second-order IIR form.</li>
    <li>It is a building block of a huge number of audio processing algorithms, like reverb or EQ.</li>
    </ul>
  </div>
</div>

{% katexmm %}
{% capture _ %}{% increment equationId20211022  %}{% endcapture %}
{% capture _ %}{% increment figureId20211022  %}{% endcapture %}

## Definition of an Allpass Filter

> An allpass filter is a filter which does not change the magnitude of any frequency component that passes through it [2].

Formally, if we denote the transfer function of the allpass filter by $H_\text{AP}(j\omega)$, we can write $|H_\text{AP}(j\omega)| = 1$.

But wait, since the magnitude does not change, what do we need allpass filters for? We need them, because they introduce a **frequency-dependent phase delay**. In other words, we are able to manipulate the phase of the frequency components without altering their magnitude.

*Note: A **transfer function** of a digital filter is a [Fourier transform]({% post_url 2021-03-18-convolution-in-popular-transforms %}#fourier-transform) or a [$z$-transform]({% post_url 2021-03-18-convolution-in-popular-transforms %}#z-transform) of its impulse response. We denote them by $H(j\omega)$ and $H(z)$ respectively.*

## Types of Allpass Systems

There are many types of systems that have the *allpass property*. They can be roughly divided into FIR and IIR categories.

### FIR Allpass System

The simplest allpass filter is the [delay]({% post_url 2021-04-01-identity-element-of-the-convolution %}#delay) [4]

$$H_\text{AP}(z) = e^{j \phi} z^{-K}, \quad ({% increment equationId20211022 %})$$

where the phase shift can take on one of two values, $\phi \in \{0, \pi\}$, and $K$ is an integer not smaller than 0, $K \geq 0$. Note that a unit delay $H_\text{AP}(z) = z^{-1}$ is also an allpass filter. Phase must be discretized, because we are operating in the real domain.

<!-- TODO: Add a block diagram of the above equation. -->

[A broader description of the properties of the delay can be found in my other article]({% post_url 2021-04-01-identity-element-of-the-convolution %}#delay).

### First-Order IIR Allpass

A first-order IIR allpass filter is given by the following transfer function [2,3,4]

$$H_\text{AP}(z) = \frac{a_1 + z^{-1}}{1 + a_1z^{-1}}, \quad ({% increment equationId20211022 %})$$

where $a \in \mathbb{R}$, because we consider real-valued filters only. The above equation corresponds to the following difference equation

$$y[n] = a_1 x[n] + \underbrace{x[n - 1] - a_1 y[n-1]}_{d[n-1]}, \quad ({% increment equationId20211022 %})$$

where $x[n]$ is the input signal, $y[n]$ is the output signal, and $d[n-1]$ can be stored in a buffer as an intermediate value.

<!-- TODO: Add a block diagram of the above equation. -->

Why is this system an allpass? Let's calculate its magnitude transfer function at the unit circle, i.e., its magnitude frequency response or $H_\text{AP}(z)$ for $z = e^{j\omega}$.

$$|H_\text{AP}(j\omega)| = |\frac{a_1 + e^{-j\omega}}{1 + a_1e^{-j\omega}}| = |e^{-j\omega} \frac{a_1e^{j\omega} + 1}{a_1e^{-j\omega} + 1}|
= |e^{-j\omega}| \frac{|\overline{a_1 e^{-j\omega} + 1|}}{|a_1 e^{-j\omega} + 1|} = 1,  \quad ({% increment equationId20211022 %})$$

where $\overline{z}$ denotes the complex conjugate of $z$. We used the facts that $|e^{-j\omega}| = 1$ and $|\frac{\overline{z}}{z}| = 1$.

#### $a_1$ Coefficient

What is the role of the $a_1$ (*allpass*) coefficient? It controls the *break frequency* of the allpass filter. What is the break frequency? It is the frequency at which the phase shift of the filter is exactly $-\frac{\pi}{2} \frac{\text{rad}}{\text{s}}$. To understand the break frequency we need to look at the phase frequency response of the allpass filter.

![]({{ page.images | absolute_url | append: "/allpass_phase_response.png" }})
_Figure {% increment figureId20211022 %}. ._

## Bibliography

[1] Alan V. Oppenheim, Alan S. Willsky, with S. Hamid *Signals and Systems*, 2nd Edition, Pearson 1997.

[2] Alan V Oppenheim, Ronald W. Schafer *Discrete-Time Signal Processing*, 3rd Edition, Pearson 2010.

[3] Zölzer, U. DAFX: Digital Audio Effects. 2nd ed. Helmut Schmidt University – University of the Federal Armed Forces, Hamburg, Germany: John Wiley & Sons Ltd, 2011.

[4] J. O. Smith, *Physical Audio Signal Processing*, [http://ccrma.stanford.edu/~jos/pasp/](http://ccrma.stanford.edu/~jos/pasp/), online
book, 2010 edition. Retrieved October 19, 2021.

{% endkatexmm %}
