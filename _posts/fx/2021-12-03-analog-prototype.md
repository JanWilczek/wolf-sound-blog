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

### Butterworth Filter Derivation

**WARNING: This part is Math-heavy. It is intended for those who want to fully understand the derivation of analog prototypes. If you don't want to get that deep, just use tabularized, ready-made formulas. You can [skip to their examples here](#butterworth-low-pass-transfer-function).**

*Note: This part is based on a great explanation in [Parks and Burrus].*
<!-- Variables??? -->

The Butterworth amplitude response $F(\omega) = |H_\text{a}(j \omega)|$ is a *Taylor series approximation* of the ideal amplitude response around $\omega=0$.

#### Taylor Series

Taylor series around $\omega=0$ is 

$$F(j\omega) = K_0 + K_1 \omega + K_2 \omega^2 + \dots = \sum_{k=0}^{\infty} K_k \omega^k, \quad ({% increment equationId20211203 %})$$

where

$$K_k = \frac{1}{k!} \frac{d^k F(\omega)}{d\omega^k} \Bigr\rvert_{\omega=0}, \quad ({% increment equationId20211203 %})$$

with $K_0 = F(0)$.

#### General Squared Magnitude Response

Function $F(j\omega)$ is the magnitude of the analog frequency response. Let'd denote by $\mathcal{\omega}$ the squared magnitude response of the approximation we seek, i.e.,

$$\mathcal{F}(j\omega) = F^2(j\omega) = |H_\text{a}(j\omega)|^2. \quad ({% increment equationId20211203 %})$$

This squared magnitude response is an *even* function (symmetric with respect to the value axis) so it may be written in a general form as a function of $\omega^2$, i.e., neglecting the odd powers of $\omega$ because they are odd functions. The general form reads

$$\mathcal{F}(k\omega) = \frac{d_0 + d_2 \omega^2 + d_4 \omega^4 + \dots + d_{2M} \omega^{2M}}{c_0 + c_2 \omega^2 + c_4 \omega^4 + \dots + c_{2N} \omega^{2N}}. \quad ({% increment equationId20211203 %})$$

The following observations can already be made with regard to Equation 4.

* We require that $\mathcal{F}(0) = 1$ so we can readily set $c_0 = d_0$.
* We require that $\mathcal{F}(j\infty) = 0$ which leads to the conclusion that the denominator must have a greater order than the numerator, i.e., $N > M$ and $c_{2N} \neq 0$.

#### Error Formulation

We can write $\mathcal{F}(j\omega)$ in terms of the sum of the desired value at $0$ and approximation error $E(\omega)$

$$\mathcal{F}(j\omega) = 1 + E(\omega). \quad ({% increment equationId20211203 %})$$

We can insert Equation 5 into Equation 4 and obtain

$$d_0 + d_2 \omega^2 + \dots + d_{2M} \omega^{2M} = c_0 + c_2 \omega^2 + \dots + c_{2N} \omega^{2N} \\+ E(\omega) [c_0 + c_2 \omega^2 + \dots + c_{2N} \omega^{2N}]. \quad ({% increment equationId20211203 %})$$

#### Error Minimization

To achieve the closest Taylor approximation possible (minimize error $E(\omega)$), we want to eliminate as many low order terms as possible so we set

$$c_0 = d_0 \text{(as before)}, \quad ({% increment equationId20211203 %})$$

$$c_2 = d_2, \quad ({% increment equationId20211203 %})$$

$$\vdots$$

$$c_{2M} = d_{2M}, \quad ({% increment equationId20211203 %})$$

$$c_{2M+2} = 0, \quad ({% increment equationId20211203 %})$$

$$\vdots$$

$$c_{2N - 2} = 0, \quad ({% increment equationId20211203 %})$$

$$c_{2N} \neq 0. \quad ({% increment equationId20211203 %})$$

Equations 7-12 tell us that the numerator of $\mathcal{F}(j\omega)$ from Equation 4 can be arbitrary, because any setting of parameters $d_0, \dots, d_{2M}$ and subsequent setting of parameters $c_0, \dots, c_{2M}$ will yield equally good Taylor approximation.

That allows us to pick the numerator as we wish. In order to have $\mathcal{F}(j \omega) = 0$, we set $c_0 = d_0 = 1$ and $d_2 = d_4 = \dots = d_{2M} = 0$.

We, thus, obtain

$$\mathcal{F}(j \omega) = \frac{1}{1 + c_{2N} \omega^{2N}}. \quad ({% increment equationId20211203 %})$$

#### Determining the Cutoff Frequency

Parameter $c_{2N}$ determines the analog cutoff frequency $\omega_\text{a}$ so that $\mathcal{F}(\omega_\text{a}) = \frac{1}{2}$ (-3 dB point).

We have already decided that for us $\omega_\text{a} = 1$ so we need to set

$$c_{2N} = 1. \quad ({% increment equationId20211203 %})$$

#### Final Squared Magnitude Response

We obtained the final formula for the analog Butterworth low-pass filter of the $N$-th order

$$\mathcal{F}(j\omega) = \frac{1}{1 + \omega^{2N}}. \quad ({% increment equationId20211203 %})$$

Equation 15 is the Taylor approximation of the ideal low-pass filter squared magnitude response at $\omega = 0$. This means that $\mathcal{F}(j\omega)$ is maximally flat at $\omega = 0$.

It turns out that Equation 15 is at the same time the Taylor approximation at $\omega = \infty$! So $\mathcal{F}(j\omega)$ is maximally flat at both ends: $\omega=0$ and $\omega = \infty$. That is why, Butterworth filter is said to have *maximally flat amplitude response* at the endpoints [SmithDigFilt].

#### Transfer Function Derivation

You may wonder,

**Since Equation 15 is the squared magnitude response, how do we obtain the transfer function over the $s$-domain?**

<!-- To this end, we can use a property of the complex numbers -->
<!-- TODO: Add commentary -->

$$\mathcal{F}(s) = F(s) F(-s) = \frac{1}{1 + (-s^2)^N}, \quad ({% increment equationId20211203 %})$$

because if we substitute $s = j\omega$, we arrive back at Equation 15.

The fractional on the right side of Equation 16 has exactly $2N$ poles. What are they?

$$(-s^2)^N + 1 = 0, \quad ({% increment equationId20211203 %})$$

$$(-s^2)^N = -1, \quad ({% increment equationId20211203 %})$$

$$(-1)^N s^{2N} = -1, \quad ({% increment equationId20211203 %})$$

$$s^{2N} = (-1)^{N+1}, \quad ({% increment equationId20211203 %})$$

$$s^{2N} = \begin{cases} -1, \quad \text{if } N \text{ is even},\\ 1, \quad \text{if } N \text{ is odd}.\end{cases} \quad ({% increment equationId20211203 %})$$

$$s_k = \begin{cases} e^{i(\pi + 2k\pi)/2N}, \quad \text{if } N \text{ is even},\\ e^{i2k\pi/2N}, \quad \text{if } N \text{ is odd.}\end{cases}, \\ \quad k=-(N-1), -(N-2), \dots, 0, 1, 2, \dots , N-1, N. \quad ({% increment equationId20211203 %})$$

*Note: This indexing of $k$ is chosen so as to simplify further derivations. Another but equivalent indexing is $k=0,1,2,\dots,2N-1$.

So $\mathcal{F}(s)$ has $2N$ poles. As their number is even, they are symmetrically placed on the unit circle: $N$ on the left half-plane, $N$ on the right half-plane. 

Since we want just $F(s)$, we need to factorize $\mathcal{F}(s)$ into $F(s)$ and $F(-s)$.

For $F(s)$ to be stable, we need all of its poles to lie on the left half-plane of the $s$-plane, i.e., have negative real parts.

We can obtain it by finding the poles of $F(-s)$ (which lie on the right half-plane) and negating their real parts (because the poles are symmetrical with respect to the imaginary axis).

Poles of $F(-s)$ are $s_k$ from Equation 22 for $k=0,\pm 1,\pm 2,\dots,\pm (N-1)/2$ if $N$ is odd, and for $k=0, \pm 1, \pm 2, \dots, \pm (N/2 -1)$ if $N$ is even. After negating the real part of these $s_k$, we obtain the pole locations of $F(s)$

$$s_k^{F(s)} = \begin{cases} -e^{-i(\pi + 2k\pi)/2N},k=0, \pm 1, \pm 2, \dots, \pm (N/2 -1) \quad \text{if } N \text{ is even},\\ -e^{-i2k\pi/2N}, k=0,\pm 1,\pm 2,\dots,\pm (N-1)/2 \quad \text{if } N \text{ is odd.}\end{cases} \quad ({% increment equationId20211203 %})$$

*Note: Negating the real part of a complex number is equivalent to negating its complex conjugate.*

Knowing all the poles, we can write out $F(s)$ in the factorized version. Let's consider $N$ odd first (so $k=0,\pm 1,\pm 2,\dots,\pm (N-1)/2$).

$$F(s) = \prod \limits_k \frac{1}{s - s_k} = \prod \limits_k \frac{1}{s + e^{-i 2 k \pi / 2N}}. \quad ({% increment equationId20211203 %})$$

We did it! Now let's just polish this formula.

#### Tidying Up the Product

The polynomial in the denominator of Equation 16 has real coefficients. Therefore, all roots occur in complex conjugate pairs apart from $s_0$, which is a real number.

Since the complex conjugate lies on the same half-plane, we can combine combine the roots with their conjugates to create a neat-looking real polynomial in the denominator.

$$F(s) = \frac{1}{s+1} \prod \limits_k \frac{1}{(s + e^{-i 2 k \pi / 2N})(s + e^{i 2 k \pi / 2N})} \\= \frac{1}{s+1} \prod \limits_k \frac{1}{s^2 + 2 \cos (2 k \pi / 2N) s + 1}, \quad ({% increment equationId20211203 %})$$

with $k=1, 2,\dots, (N-1)/2$ (note the lack of nonpositive integers).

For $N$ even, we obtain analogously (without any real roots),

$$F(s) = \prod \limits_k \frac{1}{s^2 + 2 \cos ((\pi + 2 k \pi) / 2N) s + 1}, \quad ({% increment equationId20211203 %})$$

where $k=0, \pm 1, \pm 2, \dots, \pm (N/2 -1)$.
 
According to [ParksBurrus], Equations 25 and 26 are very convenient forms.

We did it! We obtained our analog prototype!

Now, let's analyze it a little bit. 😉

### Butterworth Low-pass Transfer Function

As an example, the low-pass transfer function of the second-order Butterworth low-pass is [Zolzer05]

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
