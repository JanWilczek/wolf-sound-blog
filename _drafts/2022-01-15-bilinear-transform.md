---
title: "How To Digitize an Analog Filter with the Bilinear Transform"
description: "Learn how to derive and use the bilinear transform to convert analog systems into digital ones."
date: 2022-01-15
author: Jan Wilczek
layout: post
images: assets/img/posts/fx/2022-01-15-bilinear-transform/
# background: /assets/img/posts/fx/2022-01-15-bilinear-transform/Thumbnail.webp
categories:
  - Audio FX
  - Digital Signal Processing
tags:
  - effects
  - filtering
discussion_id: 2022-01-15-bilinear-transform
---
Learn how to derive and use the bilinear transform to convert analog systems into digital ones.

{% katexmm %}
{% capture _ %}{% increment equationId20220115 %}{% endcapture %}
{% capture _ %}{% increment figureId20220115 %}{% endcapture %}

To design and implement a parametric filter, [4 steps are needed]({% post_url fx/2021-11-26-parametric-eq-design %}):

1.	[Decide on the filter type you want to implement.]({% post_url fx/2021-11-26-parametric-eq-design %}#step-1-decide-on-the-filter-type)
2.	[Design an analog prototype.]({% post_url fx/2021-12-03-analog-prototype %})
3.	**Digitize the analog prototype using the bilinear transform.**
4.	Implement the digital filter in code.

In this article, we'll explain the second step of that process: how to go from an analog prototype to a digital form of the parametric filter.

## System Digitization Methods

There are many methods of digitalization (discretization) of analog (continuous) systems. The most popular ones are [OppenheimSchafer10]:

* *impulse-invariant transformation (IIT)*: sampling the impulse response of the continuous system,
* *bilinear transformation (BT)*: mapping the transfer function of the continuous system from the $s$-plane to the $z$-plane.

Because the impulse-invariant transformation may introduce aliasing, in the music domain, we usually use the bilinear transform. So how is it defined?

## The Bilinear Transform

> The bilinear transform is a change of variables, mapping the $j \omega$ frequency axis of the $s$-plane to the unit circle of the $z$-plane.

Given an analog transfer function $H_\text{a}(s)$ in the $s$-domain, we obtain the discrete transfer function $H_\text{d}(z)$ in the $z$-domain by substituting

$$s = \frac{2}{T} \frac{1 - z^{-1}}{1 + z^{-1}}, \quad ({% increment equationId20220115 %})$$

where $T = 1 / f_s$ is the sampling interval of the discrete system with $f_s$ being the sampling rate. Therefore,

$$H_\text{d}(z) = H_\text{a}\left(\frac{2}{T} \frac{1 - z^{-1}}{1 + z^{-1}}\right). \quad ({% increment equationId20220115 %})$$

We can go back from the discrete transfer function to the analog transfer function by substituting

$$z = \frac{1-sT/2}{1+sT/2}, \quad ({% increment equationId20220115 %})$$

what can be directly derived from Equation 1.

The bilinear transform formulas are summarized on Figure 1 (with $c=2/T$).

![]({{ "assets/img/posts/fx/2021-11-26-parametric-eq-design/" | absolute_url | append: "/BilinearTransform.webp"}}){: width="70%" alt="Bilinear transform formulas."}
_Figure {% increment figureId20220115  %}. Bilinear transform formulas._

## Derivation of the Bilinear Transform

How is the bilinear transform derived? How to come up with the mapping in Equation 1?

Below I give you a simple, intuitive explanation. If you are not interested in it, you can [skip to the properties of the bilinear transform](#properties-of-the-bilinear-transform).

<!--  Something about the allpass filter? -->

The $s \rightarrow z$ mapping of the bilinear transform may be explained as a derivation of a digital representation of an integrator.

An integrator is a system at whose output the integral of the input signal may be observed

$$y(t) = \int \limits_0^t x(\tau) d\tau, \quad ({% increment equationId20220115 %})$$

where $x(t)$ is the input signal over continuous time $t$ and $y(t)$ is the output signal of the integrator.

The Laplace transform of Equation 4 yields

$$Y(s) = \frac{1}{s}X(s), \quad ({% increment equationId20220115 %})$$

where $s \in \mathbb{C}$. Therefore, the integrator can be shown on the diagram as in Figure 2.

<!-- TODO: Integrator diagram -->

We want to obtain a discrete system described by a discrete transfer function $G(z)$ that behaves like $\frac{1}{s}$. To this end, we observe the output of the continuous system at discrete time points $t = kT$, where $k \in \mathbb{Z}$ and $T$ is the sampling interval.

$$y(kT) = \int \limits_{0}^{kT} x(\tau) d\tau = \int \limits_{0}^{(k-1)T} x(\tau) d \tau + \int \limits_{(k-1)T}^{kT} x(\tau) d \tau 
\\= y((k-1)T) + \int \limits_{(k-1)T}^{kT} x(\tau) d \tau. \quad ({% increment equationId20220115 %})$$

We can now approximate the last integral in Equation 6 via the [trapezoidal rule](https://en.wikipedia.org/wiki/Trapezoidal_rule)

$$\int \limits_{(k-1)T}^{kT} x(\tau) d \tau \approx (x((k-1)T) + x(kT))T / 2. \quad ({% increment equationId20220115 %})$$

Inserting Equation 7 into Equation 6 yields

$$y(kT) = y((k-1)T) + (x((k-1)T) + x(kT))T / 2. \quad ({% increment equationId20220115 %})$$

We now transform Equation 8 with the $z$-transformation

$$Y(z) = z^{-1} Y(z) + (z^{-1} X(z) + X(z))T / 2. \quad ({% increment equationId20220115 %})$$

After rearranging Equation 9 we obtain the transfer function formulation

$$Y(z) = \frac{T}{2}\frac{1 + z^{-1}}{1 - z^{-1}} X(z) = G(z) X(z). \quad ({% increment equationId20220115 %})$$

Since $G(z)$ was meant to approximate $\frac{1}{s}$, we can write

$$\frac{1}{s} = G(z) = \frac{T}{2}\frac{1 + z^{-1}}{1 - z^{-1}}. \quad ({% increment equationId20220115 %})$$

which after inversion gives Equation 1, i.e., the bilinear transform. $\Box$

The bilinear transform can also be derived by representing a signal as a series of impulses, calculating its Laplace transform and $z$-transform, equating the two and approximating the resulting $s$-to-$z$ mapping with a series expansion. But the integrator derivation seems more intuitive to me, especially the origin of the $\frac{2}{T}$ constant. What do you think? Let me know in the comments below the article. 😉

## Properties of the Bilinear Transform

The bilinear transform has a number of useful properties [1`2Burrus87].

First of all, it is called *bilinear* because **the numerator and the denominator are linear in $z$.**

Second of all, the bilinear transform maps the left halfplane of the $s$-plane into the interior of of the unit circle in the $z$-plane. This is shown on Figure 3.

<!-- TODO: Figure with bending the j omega axis -->

As a consequence, the poles from the left half-plane of the $s$-plane are mapped to the poles within the unit circle of the $z$-plane. That means that stable analog filters are transformed into stable digital filters, what is a very desirable property in the context of musically useful parametric filters.


<!-- phase is made nonlinear [OppenheimSchafer10] -->

<!-- same filter order of the prototype and digital filter -->
<!-- optimality is preserved -->
<!-- cascade of a transformed sections is equivalent to a transform of a cascade of sections -->
## Frequency Warping

<!-- Add a visualization of the frequency warping with marks -->



## Example: Digitization of the Butterworth Low-Pass

{% endkatexmm %}

## Bibiliography

[OppenheimSchafer10] Alan V Oppenheim, Ronald W. Schafer *Discrete-Time Signal Processing*, 3rd Edition, Pearson 2010.

[ParksBurrus87]  [T. W. Parks, C. S. Burrus, *Digital Filter Design*, John Wiley & Sons, Inc., 1987.](https://amzn.to/3DyoXJE)
