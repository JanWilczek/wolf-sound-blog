---
title: "How to Design an Analog Prototype Filter?"
description: "PLACEHOLDER"
date: 2021-12-03
author: Jan Wilczek
layout: post
images: assets/img/posts/fx/2021-12-03-analog-prototype/
# background: /assets/img/posts/fx/2021-12-03-analog-prototype/
categories:
  - Audio FX
  - Digital Signal Processing
tags:
  - effects
  - filtering
discussion_id: 2021-12-03-analog-prototype
---
Design prototypes for stable, efficient, parametric IIR filters.

<!--  TODO: Add alt tags -->

{% katexmm %}
{% capture _ %}{% increment equationId20211203  %}{% endcapture %}
{% capture _ %}{% increment figureId20211203  %}{% endcapture %}

In the last article, [add link] I outlined the process of creating a parametric filter. The steps were

1. Decide on the filter type.
2. Design an analog prototype.
3. Digitize the analog prototype using the bilinear transform.
4. Implement the digital filter.

Here's how the process looks:

![]({{ page.images | absolute_url | append: "/PipelineUnmarked.png"}}){: alt="" }
_Figure {% increment figureId20211203 %}. ._

In this article, we'll discuss the second step of the process: **designing the analog prototype**.

![]({{ page.images | absolute_url | append: "/PipelineMarked.png"}}){: alt="" }
_Figure {% increment figureId20211203 %}. ._

## Recap

As you remember from the previous article [link], parametric filters must have [Valimaki]

* interpretable, real-time-adjustable controls and
* low processing delay.

This led us to choose infinite-impulse response (IIR) filters. To streamline the process of their design and to ensure that they remain stable, we said that the easiest way to come up with these filters is to design them in the analog domain and then digitize them.

Then, how to design them in the analog domain?

## Our Goal

Designing a filter in the analog domain is traditionally done by designing a low-pass filter with some of the desired characteristics and then transforming it to the desired filter type. This can be done with transformations like lowpass-to-bandpass transformation or lowpass-to-highpass transformation.

What is more, we can set the cutoff frequency of the low-pass filter to 1, because this frequency will eventually be altered by the bilinear transform.

**So our first goal is to design a low-pass filter with the cutoff frequency equal to 1.**

It's all downhill from there. 😉

## Analog Filters Design Methods

**Filter design in the analog or digital domain is the process of approximating the desired frequency response with a certain set of constraints.** [DigFiltDes]

As such, it may be considered a form of *constrained optimization*.

There are many methods to achieve this, as there are many optimization methods. There are, however, 4 basic filter approximations considered as standard. Each of them is optimal in a different sense [OppSchaf].

<div class="card summary">
  <div class="card-body">
  <h5 class="card-title">In Short</h5>
  <h6 class="card-subtitle mb-2 text-muted">Standard Analog Filter Design Methods</h6>
    <table class="table">
    <tr>
        <th>Method</th>    
        <th>What is optimal?</th>
    </tr>
    <tr>
        <td>Butterworth</td>
        <td>The amplitude response is maximally flat in the passband.</td>
    </tr>
    <tr>
        <td>Chebyshev type I</td>
        <td>The amplitude response is either equiripple in the passband and monotonic in the stopband.</td>
    </tr>
    <tr>
        <td>Chebyshev type II</td>
        <td>The amplitude response is monotonic in the passband and equiripple in the stopband.</td>
    </tr>
    <tr>
        <td>Elliptic functions</td>
        <td>The amplitude response has equiripple error in the passband and the stopband.</td>
    </tr>
    </table>
  </div>
</div>

But in equalizer filters mostly Butterworth responses are used, because the amplitude response is monotonic (without any ripples) and the higher the frequency above the cutoff frequency, the bigger the filter's attenuation [Zolzer05]. 

Additionally, it is easy to control the slope of the roll-off above the cutoff frequency with the filter order. If the filter order is $N$ its attenuation in the stopband is $N \cdot 6$ dB per octave (doubling of the frequency) [Zolzer05].

## Analog Prototype Butterworth Low-pass

We know that we want to design an analog prototype low-pass using the Butterworth approximation. What do we want to approximate exactly?

### Approximation Goal

The goal of the approximation is the *ideal low-pass filter*.

![]({{ page.images | absolute_url | append: "/IdealLowPass.png"}})
_Figure {% increment figureId20211203  %}. Amplitude response of the ideal low-pass filter._

Frequency $\omega_\text{a}$ is the analog cutoff frequency in radians per second. We assume that $\omega_\text{a} = 1$, i.e., the filter's transfer function is *normalized*.

Our only constraint is the filter order. According to [Zolzer05] the most commonly used orders are $N = 2$ and $N = 4$.

### Butterworth Low-pass Transfer Function

After necessary derivations, the low-pass transfer function of the second-order Butterworth low-pass is [Zolzer05]

$$H_2(s) = \frac{1}{s^2 + \sqrt{2} + 1}. \quad ({% increment equationId20211203 %})$$

The fourth-order Butterworth low-pass has the following transfer function

$$H_4(s) = \frac{1}{(s^2 + 1.848 s + 1)(s^2 + 0.765 s + 1)}. \quad ({% increment equationId20211203 %})$$

*Hint: To obtain an arbitrary analog cutoff frequency, simply replace $s$ with $s/\omega_\text{a}$ in the above transfer functions.*

### Visualization

To see, how much the Butterworth low-pass filter deviates from the ideal response from Figure 3, let's plot the amplitude responses of both filters against the ideal response.

<!-- TODO: Low-pass comparison. -->

## Summary

We did it! We obtained the transfer function of the ideal low-pass filter which we can now digitze with the bilinear transform and then transform to the desired form (high-pass, band-pass, etc.).

{% endkatexmm %}
