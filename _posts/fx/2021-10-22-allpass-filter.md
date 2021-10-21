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

$$H_\text{AP}(z) = \pm z^{-K}, \quad ({% increment equationId20211022 %})$$

where $K$ is an integer not smaller than 0, $K \geq 0$. Note that a unit delay $H_\text{AP}(z) = z^{-1}$ is also an allpass filter. Phase can be unaltered or inverted (multiplication by 1 and $-1$ respectively), because we are operating in the real domain.

![]({{ page.images | absolute_url | append: "/fir_allpass.png" }}){: width="80%" alt="Block diagram of the FIR allpass filter."}
_Figure {% increment figureId20211022 %}. Block diagram of the FIR allpass filter._

[A broader description of the properties of the delay can be found in my article]({% post_url 2021-04-01-identity-element-of-the-convolution %}#delay).

### First-Order IIR Allpass

A first-order IIR allpass filter is given by the following transfer function [2,3,4]

$$H_\text{AP}(z) = \frac{a_1 + z^{-1}}{1 + a_1z^{-1}}, \quad ({% increment equationId20211022 %})$$

where $a \in \mathbb{R}$, because we consider real-valued filters only. The above equation corresponds to the following difference equation

$$y[n] = a_1 x[n] + \underbrace{x[n - 1] - a_1 y[n-1]}_{d[n-1]}, \quad ({% increment equationId20211022 %})$$

where $x[n]$ is the input signal, $y[n]$ is the output signal, and $d[n-1]$ can be stored in a buffer as an intermediate value.

#### Implementation

The difference equation 3 is equivalent to the following DSP diagram.

![]({{ page.images | absolute_url | append: "/first_order_allpass_filter.png" }}){: alt="Block diagram of the first-order allpass filter."}
_Figure {% increment figureId20211022 %}. Block diagram of the first-order allpass filter._

How to see the equivalence? First, observe that we have here a combination of two comb filters: a feedback and a feedforward comb filter [4].

Feedback comb filter difference equation:

$$v[n] = x[n] - a_1 v[n-1]. \quad ({% increment equationId20211022 %})$$

Feedforward comb filter difference equation:

$$y[n] = a_1 v[n] + v[n-1]. \quad ({% increment equationId20211022 %})$$

Insert $v[n]$ from Eq. 4 into Eq. 5:

$$y[n] = a_1 x[n] - a_1^2 v[n-1] + v[n-1]. \quad ({% increment equationId20211022 %})$$

Substitute first $v[n-1]$ by $\frac{y[n-1] - v[n-2]}{a_1}$ (from Eq. 5) and second $v[n-1]$ by $x[n-1] - a_1 v[n-2]$ (from Eq. 4):

$$y[n] = a_1 x[n] - a_1^2 \frac{y[n-1] - v[n-2]}{a_1} + x[n-1] - a_1 v[n-2] 
\\= a_1 x[n] - a_1 y[n-1] + x[n-1], \quad ({% increment equationId20211022 %})$$

which is equivalent to Eq. 3.

#### Magnitude Response

Why is this system an allpass? Let's calculate its magnitude transfer function at the unit circle, i.e., its magnitude frequency response or $H_\text{AP}(z)$ for $z = e^{j\omega}$.

$$\Bigl\lvert H_\text{AP}(j\omega) \Bigr\rvert = \Bigl\lvert \frac{a_1 + e^{-j\omega}}{1 + a_1e^{-j\omega}} \Bigr\rvert = \Bigl\lvert e^{-j\omega} \frac{a_1e^{j\omega} + 1}{a_1e^{-j\omega} + 1} \Bigr\rvert
= \bigl\lvert e^{-j\omega} \bigr\rvert \frac{\bigl\lvert \overline{a_1 e^{-j\omega} + 1\bigr\rvert}}{\bigl\lvert a_1 e^{-j\omega} + 1\bigr\rvert} = 1,  \quad ({% increment equationId20211022 %})$$

where $\overline{z}$ denotes the complex conjugate of $z$. We used the facts that $|e^{-j\omega}| = 1$ and $|\frac{\overline{z}}{z}| = 1$.

#### Phase Response

What is the role of the $a_1$ (*allpass*) coefficient? It controls the *break frequency* of the allpass filter. What is the break frequency? It is the frequency at which the phase shift of the filter is exactly $-\frac{\pi}{2}$ rad. To understand the break frequency we need to look at the phase frequency response of the allpass filter.

![]({{ page.images | absolute_url | append: "/allpass_phase_response.png" }}){: width="80%" alt="Phase response of the first-order allpass filter."}
_Figure {% increment figureId20211022 %}. Phase response of a first-order allpass filter for different break frequencies $\omega_\text{b}$._

We here refer to digital frequency given in radians, where $\omega = 0$ is corresponds to 0 Hz and $\omega = \pi$ corresponds to the Nyquist frequency $\frac{f_s}{2}$ ($f_s$ is the sampling rate in Hz). Digital frequency $\omega$ in radians can be computed out of frequency $f$ in Hz using the following formula:

$$\omega = 2 \pi f / f_s.  \quad ({% increment equationId20211022 %})$$

The blue lines in the figure mark the break frequencies of particular curves. The red line marks the phase shift by $-\frac{\pi}{2}$ rad. If we want to set a desired break frequency $\omega_\text{b}$ in radians, we can use the following formula to compute the $a_1$ coefficient [3,4,5]

$$a_1 = \frac{\tan(\omega_\text{b} / 2) - 1}{\tan(\omega_\text{b} / 2) + 1}.  \quad ({% increment equationId20211022 %})$$

How is the above formula found? It is the result of transforming an *analog allpass filter* to the digital domain via the *bilinear transform*. Explaining this process is beyond the scope of this article; if you are interested, check out [the great explanation in [4]](https://ccrma.stanford.edu/~jos/pasp/Classic_Virtual_Analog_Phase.html). After the derivations, we arrive exactly at the transfer function from Equation 2.

How are the plots in the above figure generated? They are derived from calculating the [argument (in the complex numbers sense)](https://en.wikipedia.org/wiki/Argument_(complex_analysis)) of the allpass transfer function $H_\text{AP}(j\omega)$. It can be done in software using the `freqz` function of [Matlab](https://www.mathworks.com/help/signal/ref/freqz.html) or [`scipy.signal`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.freqz.html). Alternatively, you can use the following out-of-the-box formula [5]

$$\theta (\omega) = - \omega + 2 \arctan \left( \frac{a_1 \sin \omega}{1 + a_1 \cos \omega} \right),  \quad ({% increment equationId20211022 %})$$

where $\omega$ is the digital frequency in radians.

#### Derive It Yourself?

Why am I saying that the formula in Equation 7 is out-of-the-box? I wasn't able to derive it myself. After manual calculations, however, I managed to obtain a formula which was equivalent in terms of the plots. Comparison against `freqz` yielded identical result. I wasn't able to find the derivation of this formula either. Do you know how to derive it? If so, please, let me know in the comments!

#### Properties of the First-Order Allpass Filter

When you look at the figure with the phase response of the first-order allpass filter, you can read out interesting properties.

* The phase shift at DC ($\omega = 0$) is 0.
* The phase shift at the Nyquist frequency ($\omega = \pi$) is $-\pi$ rad and is **always** the maximum possible phase delay.
* The phase shift at the break frequency $\omega_\text{b}$ is $-\frac{pi}{2}$ rad.

#### Cascading Allpass Filters

Arranging allpass filters in a series results in the **summation of phase delays**. We can therefore obtain a phase delay of $-N \pi$ at $\omega = \pi$ by cascading $N$ first-order allpass filters.

### Second-Order IIR Allpass

The second-order IIR allpass filter has the following transfer function [3]:

$$H_{\text{AP}_2}(z) = \frac{-c + d(1-c) z^{-1} + z^{-2}}{1 + d(1-c) z^{-1} - c z^{-2}},  \quad ({% increment equationId20211022 %})$$

where the parameter $d$ controls the center (cutoff) frequency of the filter $f_\text{c}$ (at which the phase shift is $-\pi$) and the parameter $c$ is computed from parameter $f_\text{b}$ which determines the bandwidth (the steepness of the slope of the phase transition around the cutoff frequency). The relations between these parameters are specified by these equations:

$$c = \frac{\tan(\pi f_\text{b} / f_s) - 1}{\tan(\pi f_\text{b} / f_s) + 1},  \quad ({% increment equationId20211022 %})$$

$$d = - \cos(2\pi f_\text{c} / f_s),  \quad ({% increment equationId20211022 %})$$

where $f_s$ is the sampling rate. Parameters $f_\text{b}$, $f_\text{c}$, and $f_s$ are given in Hz.

Note how $f_\text{b}$ is coupled with $c$ but not with $d$ and $f_\text{c}$ is coupled with $d$ but not with $c$. This allows us to smoothly control our filter's properties.

#### Phase Response



#### Implementation

The difference equation of the second-order allpass is

$$v[n] = x[n] - d(1 - c)v[n-1] + c v[n-2],  \quad ({% increment equationId20211022 %})$$
$$y[n] = -c v[n] + d (1-c) v[n-1] + v[n-2].  \quad ({% increment equationId20211022 %})$$

If that seems complicated, a diagram should make it clear 🙂

![]({{ page.images | absolute_url | append: "/second_order_allpass_filter.png" }}){: alt="Block diagram of the second-order allpass filter."}
_Figure {% increment figureId20211022 %}. Block diagram of the second-order allpass filter._



## Bibliography

[1] Alan V. Oppenheim, Alan S. Willsky, with S. Hamid *Signals and Systems*, 2nd Edition, Pearson 1997.

[2] Alan V Oppenheim, Ronald W. Schafer *Discrete-Time Signal Processing*, 3rd Edition, Pearson 2010.

[3] Zölzer, U. DAFX: Digital Audio Effects. 2nd ed. Helmut Schmidt University – University of the Federal Armed Forces, Hamburg, Germany: John Wiley & Sons Ltd, 2011.

[4] J. O. Smith, *Physical Audio Signal Processing*, [http://ccrma.stanford.edu/~jos/pasp/](http://ccrma.stanford.edu/~jos/pasp/), online
book, 2010 edition. Retrieved October 19, 2021.

[5] R. Kiiski, F. Esqueda, and V. Välimäki, *Time-Variant Gray-Box Modeling of a Phaser Pedal*, in
Proceedings of the 19th International Conference on Digital Audio Effects (DAFx-16), Brno, Czech
Republic, September 5–9, pp. 121–128, 2016.


{% endkatexmm %}
