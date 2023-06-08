---
title: "How to Design an Analog Prototype Filter? Butterworth Filter Derivation"
description: "A thorough, step-by-step tutorial on the derivation of the transfer function of the Butterworth analog low-pass filter."
date: 2021-12-03
author: Jan Wilczek
layout: post
images: assets/img/posts/fx/2021-12-03-analog-prototype/
background: /assets/img/posts/fx/2021-12-03-analog-prototype/Thumbnail.webp
categories:
  - Audio FX
  - Digital Signal Processing
tags:
  - effects
  - filtering
discussion_id: 2021-12-03-analog-prototype
---
Design prototypes for stable, efficient, parametric IIR filters.

<iframe width="560" height="315" src="https://www.youtube.com/embed/rrMRkPpRQAs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


{% capture _ %}{% increment equationId20211203  %}{% endcapture %}
{% capture _ %}{% increment figureId20211203  %}{% endcapture %}

In the [last article]({% post_url collections.posts, 'fx/2021-11-26-parametric-eq-design' %}), I outlined the process of creating a parametric filter. The steps are

1. Decide on the filter type.
2. Design an analog prototype.
3. Digitize the analog prototype using the bilinear transform.
4. Implement the digital filter.

Here's how the process looks:

![]({{ page.images | absolute_url | append: "/PipelineUnmarked.webp"}}){: alt="Parametric filter design workflow." }
_Figure {% increment figureId20211203 %}. Parametric filter design workflow._

In this article, we'll discuss the second step of the process: **designing the analog prototype**.

![]({{ page.images | absolute_url | append: "/PipelineMarked.webp"}}){: alt="Parametric filter design workflow with marked second step." }
_Figure {% increment figureId20211203 %}. In this article, we discuss analog prototype design._

## Recap

As you remember from the [previous article]({% post_url collections.posts, 'fx/2021-11-26-parametric-eq-design' %}), parametric filters must have [VälimäkiReiss16]

* interpretable, real-time-adjustable controls and
* low processing delay.

This led us to choose infinite-impulse response (IIR) filters. To streamline the process of their design and to ensure that they remain stable, we said that the easiest way to come up with these filters is to design them in the analog domain and then digitize them.

How to design them in the analog domain, then?

## Our Goal

Designing a filter in the analog domain is traditionally done by designing a low-pass filter with some of the desired characteristics and then transforming it to the desired filter type, for example, high-pass. This can be done with transformations like lowpass-to-bandpass transformation or lowpass-to-highpass transformation.

What is more, we can set the cutoff frequency of the low-pass filter to 1, because this frequency will be altered by the bilinear transform anyway.

**So our first goal is to design a low-pass filter with the cutoff frequency equal to 1.**

It's all downhill from there. 😉

## Analog Filters Design Methods

**Filter design in the analog or digital domain is the process of approximating the desired frequency response with a certain set of constraints.** [Smith07]

As such, it may be considered a form of *constrained optimization*.

There are many methods to achieve this, as there are many optimization methods. There are, however, 4 basic filter approximations considered as standard. Each of them is optimal in a different sense [OppenheimSchafer10].

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
        <td>The amplitude response is equiripple (has ripples on the curve of a fixed width) in the passband and monotonic in the stopband.</td>
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

But in equalizer filters mostly Butterworth responses are used, because the amplitude response is monotonic (without any ripples) and the higher the frequency above the cutoff frequency, the bigger the filter's attenuation [Zölzer08]. 

Additionally, it is easy to control the slope of the roll-off above the cutoff frequency with the filter order. If the filter order is $N$, its attenuation in the stopband is $N \cdot 6$ dB per octave (each doubling of frequency) [Zölzer08].

## Analog Prototype Butterworth Low-pass

<iframe width="560" height="315" src="https://www.youtube.com/embed/00hNt7uBpEI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

We know that we want to design an analog prototype low-pass using the Butterworth approximation. What do we want to approximate exactly?

### Approximation Goal

The goal of the approximation is the *ideal low-pass filter*.

![]({{ page.images | absolute_url | append: "/IdealLowPass.webp"}}){: alt="Amplitude response of the ideal low-pass filter."}
_Figure {% increment figureId20211203  %}. Amplitude response of the ideal low-pass filter with cutoff frequency equal to 1._

Frequency $\omega_\text{a}$ is the analog cutoff frequency in radians per second. We assume that $\omega_\text{a} = 1$, i.e., the filter's transfer function is *normalized*.

Our only constraint is the filter order. According to [Zölzer08] the most commonly used orders are $N = 2$ and $N = 4$.

### Butterworth Filter Derivation

**WARNING: This part is math-heavy. It is intended for those who want to fully understand the derivation of analog prototypes. If you don't want to get that deep, just use tabularized, ready-made formulas. You can [skip to their examples here](#butterworth-low-pass-transfer-function).**

*Note: This part is based on the great explanation from [ParksBurrus87].*

The frequency response of an analog filter is found by evaluating its transfer function $H(s)$ along the imaginary axis, i.e., for $s=j\omega$.

We will formulate the problem of approximating the ideal filter in terms of the squared magnitude response $|H(j\omega)|^2$. That is because $|H(j\omega)|^2$ is an analytic, real-valued function of a real variable, i.e., high-school mathematics apply. Another reason is that $|H(j\omega)|^2$ is proportional to the energy or power of the signal, which may be useful depending on the context.

To be able to get from the squared magnitude response to the transfer function, we introduce an intermediate, complex-valued function of the complex variable $s$

$$\mathcal{H}_\text{a}(s) = H_\text{a}(s) H_\text{a}(-s). \quad ({% increment equationId20211203 %})$$

It can be easily shown that

$$\mathcal{H}_\text{a}(s) \Bigr\rvert_{s=j\omega} = |H_\text{a}(j\omega)|^2. \quad ({% increment equationId20211203 %})$$

The Butterworth squared magnitude response $\mathcal{H}_\text{a}(\omega) = |H_\text{a}(j \omega)|^2$ is a *Taylor series approximation* of the ideal squared magnitude response around $\omega=0$.

#### Taylor Series

Taylor series around $\omega=0$ is 

$$H_\text{a}(j\omega) = K_0 + K_1 \omega + K_2 \omega^2 + \dots = \sum_{k=0}^{\infty} K_k \omega^k, \quad ({% increment equationId20211203 %})$$

where

$$K_k = \frac{1}{k!} \frac{d^k H_\text{a}(\omega)}{d\omega^k} \Bigr\rvert_{\omega=0}, \quad ({% increment equationId20211203 %})$$

with $K_0 = H_\text{a}(0)$.

#### General Squared Magnitude Response

The squared magnitude response $\mathcal{H}_\text{a}(j\omega)$ is an *even* function (symmetric with respect to the value axis) so it may be written in a general form as a function of $\omega^2$, i.e., neglecting the odd powers of $\omega$ because they are odd functions. The general form reads

$$\mathcal{H}_\text{a}(j\omega) = \frac{d_0 + d_2 \omega^2 + d_4 \omega^4 + \dots + d_{2M} \omega^{2M}}{c_0 + c_2 \omega^2 + c_4 \omega^4 + \dots + c_{2N} \omega^{2N}}. \quad ({% increment equationId20211203 %})$$

The following observations can already be made with regard to Equation 5.

* We require that $\mathcal{H}_\text{a}(0) = 1$ so we can readily set $c_0 = d_0$.
* We require that $\mathcal{H}_\text{a}(j\infty) = 0$ which leads to the conclusion that the denominator must have a greater order than the numerator, i.e., $N > M$ and $c_{2N} \neq 0$.

#### Error Formulation

We can write $\mathcal{H}_\text{a}(j\omega)$ in terms of the sum of the desired value at $0$ and approximation error $E(\omega)$

$$\mathcal{H}_\text{a}(j\omega) = 1 + E(\omega). \quad ({% increment equationId20211203 %})$$

We can insert Equation 6 into Equation 5 and obtain

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

Equations 8-13 tell us that the numerator of $\mathcal{H}_\text{a}(j\omega)$ from Equation 5 can be arbitrary, because any setting of parameters $d_0, \dots, d_{2M}$ and subsequent setting of parameters $c_0, \dots, c_{2M}$ will yield equally good Taylor approximation.

That allows us to pick the numerator as we wish. In order to have $\mathcal{H}_\text{a}(j \infty) = 0$, we set $c_0 = d_0 = 1$ and $d_2 = d_4 = \dots = d_{2M} = 0$.

We, thus, obtain

$$\mathcal{H}_\text{a}(j \omega) = \frac{1}{1 + c_{2N} \omega^{2N}}. \quad ({% increment equationId20211203 %})$$

#### Determining the Cutoff Frequency

Parameter $c_{2N}$ determines the analog cutoff frequency $\omega_\text{a}$ so that $\mathcal{H}_\text{a}(\omega_\text{a}) = \frac{1}{2}$ (-3 dB point).

We have already decided that for us $\omega_\text{a} = 1$ so we need to set

$$c_{2N} = 1. \quad ({% increment equationId20211203 %})$$

#### Final Squared Magnitude Response

We obtained the final formula for the analog Butterworth low-pass filter of the $N$-th order

$$\mathcal{H}_\text{a}(j\omega) = \frac{1}{1 + \omega^{2N}}. \quad ({% increment equationId20211203 %})$$

Equation 16 is the Taylor approximation of the ideal low-pass filter's squared magnitude response at $\omega = 0$. This means that $\mathcal{H}_\text{a}(j\omega)$ is maximally flat at $\omega = 0$.

It turns out that Equation 16 is at the same time the Taylor approximation at $\omega = \infty$. So $\mathcal{H}_\text{a}(j\omega)$ is maximally flat at both ends: $\omega=0$ and $\omega = \infty$. That is why, Butterworth filter is said to have *maximally flat amplitude response* at the endpoints [Smith07].

#### Transfer Function Derivation

You may wonder:

**Since Equation 16 is the squared magnitude response, how do we obtain the transfer function over the $s$-domain?**

We can use the definition of $\mathcal{H}_\text{a}(s)$ from Equation 1.

$$\mathcal{H}_\text{a}(s) = H_\text{a}(s) H_\text{a}(-s) = \frac{1}{1 + (-s^2)^N}, \quad ({% increment equationId20211203 %})$$

because if we substitute $s = j\omega$, we arrive back at Equation 16.

The fractional on the right side of Equation 17 has exactly $2N$ poles. What are they?

$$(-s^2)^N + 1 = 0, \quad ({% increment equationId20211203 %})$$

$$(-s^2)^N = -1, \quad ({% increment equationId20211203 %})$$

$$(-1)^N s^{2N} = -1, \quad ({% increment equationId20211203 %})$$

$$s^{2N} = (-1)^{N+1}, \quad ({% increment equationId20211203 %})$$

$$s^{2N} = \begin{cases} -1, \quad \text{if } N \text{ is even},\\ 1, \quad \text{if } N \text{ is odd}.\end{cases} \quad ({% increment equationId20211203 %})$$

$$s_k = \begin{cases} e^{i(\pi + 2k\pi)/2N}, \quad \text{if } N \text{ is even},\\ e^{i2k\pi/2N}, \quad \text{if } N \text{ is odd.}\end{cases}, \\ \quad k=-(N-1), -(N-2), \dots, 0, 1, 2, \dots , N-1, N. \quad ({% increment equationId20211203 %})$$

*Note: This indexing of $k$ is chosen so as to simplify further derivations. Another but equivalent indexing is $k=0,1,2,\dots,2N-1$.*

So $\mathcal{H}_\text{a}(s)$ has $2N$ poles evenly spaced around the unit circle. As their number is even, they are placed symmetrically: $N$ on the left half-plane, $N$ on the right half-plane. 

Since we want just $H_\text{a}(s)$, we need to factorize $\mathcal{H}_\text{a}(s)$ into $H_\text{a}(s)$ and $H_\text{a}(-s)$.

For $H_\text{a}(s)$ to be stable, we need all of its poles to lie on the left half-plane of the $s$-plane, i.e., have negative real parts.

We can obtain it by finding the poles of $H_\text{a}(-s)$ (which lie on the right half-plane) and negating their real parts (because the poles are symmetrical with respect to the imaginary axis).

Poles of $H_\text{a}(-s)$ are $s_k$ from Equation 23 with arguments in the $(-\pi/2,\pi/2)$ range, i.e., for $k=0,\pm 1,\pm 2,\dots,\pm (N-1)/2$ if $N$ is odd, and for $k=0, \pm 1, \pm 2, \dots, \pm (N/2 -1),-N/2$ if $N$ is even. After negating the real part of these $s_k$, we obtain the pole locations of $H_\text{a}(s)$

$$s_k^{H_\text{a}(s)} = \begin{cases} -e^{-i(\pi + 2k\pi)/2N},k=0, \pm 1, \dots, \pm (N/2 -1),-N/2 \quad \text{if } N \text{ is even},\\ -e^{-i2k\pi/2N}, k=0,\pm 1,\pm 2,\dots,\pm (N-1)/2 \quad \text{if } N \text{ is odd.}\end{cases} \quad ({% increment equationId20211203 %})$$

*Note: Negating the real part of a complex number is equivalent to negating its complex conjugate.*

Knowing all the poles, we can write out $H_\text{a}(s)$ in the factorized version. Let's consider $N$ odd first (so $k=0,\pm 1,\pm 2,\dots,\pm (N-1)/2$).

$$H_\text{a}(s) = \prod \limits_k \frac{1}{s - s_k} = \prod \limits_k \frac{1}{s + e^{-i 2 k \pi / 2N}}. \quad ({% increment equationId20211203 %})$$

We did it! Now let's just polish this formula.

#### Tidying Up the Product

The polynomial in the denominator of Equation 17 has real coefficients. Therefore, all roots occur in complex conjugate pairs apart from $s_0$, which is a real number (remember, we consider $N$-odd case now).

Since the complex conjugate lies on the same half-plane, we can combine the roots with their conjugates to create a neat-looking real polynomial in the denominator. The single real pole ($-1$) must be factored out of the product, because it doesn't have a conjugate pair.

$$H_\text{a}(s) = \frac{1}{s+1} \prod \limits_k \frac{1}{(s + e^{-i 2 k \pi / 2N})(s + e^{i 2 k \pi / 2N})} \\= \frac{1}{s+1} \prod \limits_k \frac{1}{s^2 + 2 \cos (k \pi / N) s + 1}, \quad ({% increment equationId20211203 %})$$

with $k=1, 2,\dots, (N-1)/2$ (note the lack of nonpositive integers).

For $N$ even, we obtain analogously (without any real roots)

$$H_\text{a}(s) = \prod \limits_m \frac{1}{s^2 + 2 \cos (m \pi / 2N) s + 1}, \quad ({% increment equationId20211203 %})$$

where $m = 1, 3, \dots, N-1$. This comes from having $m=2k +1, k=0, 1, \dots, (N/2 -1)$ to facilitate derivations.
 
According to [ParksBurrus87], Equations 26 and 27 are very convenient forms for implementation.

We did it! We obtained our analog prototype!

Now, let's analyze it a little bit. 😉

### Butterworth Low-pass Transfer Function

As an example, the low-pass transfer function of the second-order Butterworth low-pass is [Zölzer08]

$$H_2(s) = \frac{1}{s^2 + \sqrt{2} s + 1}. \quad ({% increment equationId20211203 %})$$

The fourth-order Butterworth low-pass has the following transfer function

$$H_4(s) = \frac{1}{(s^2 + 1.848 s + 1)(s^2 + 0.765 s + 1)}. \quad ({% increment equationId20211203 %})$$

*Hint: To obtain an arbitrary analog cutoff frequency $\omega_\text{a}$, simply replace $s$ with $s/\omega_\text{a}$ in the above transfer functions.*

### Visualization

To see, how much the Butterworth low-pass filter deviates from the ideal response from Figure 3, let's plot the amplitude responses of both filters against the ideal response.

![]({{ page.images | absolute_url | append: "/ButterworthComparison.webp"}}){: alt="Comparison of Butterworth filters amplitude responses of orders 2, 4, and 11, and the ideal low-pass amplitude response." }
_Figure {% increment figureId20211203 %}. Butterworth low-pass amplitude response of 2nd, 4th, and 11th order plotted against the ideal response._

The 11th order is shown for additional comparison.

We can observe that Butterworth filters cross the cutoff frequency with exactly the same gain, which is $1/\sqrt{2}$. That means that our derivations are correct.

Additionally, we can observe that the higher the filter order, the more steep the slope of the transition band (between the passband and the stopband).

Figure 4 also shows that the Butterworth approximation is indeed maximally flat at frequencies $\omega=0$ and $\omega=\infty$.

Figure 5 shows the same amplitude responses but this time the magnitude is expressed in decibels ($20 \log_{10}(\cdot)$). The -3 dB at cutoff frequency is clearly visible.

![]({{ page.images | absolute_url | append: "/ButterworthComparisonDecibels.webp"}}){: alt="Comparison of Butterworth filters amplitude responses on the decibel scale for orders 2, 4, and 11, and the ideal low-pass amplitude response." }
_Figure {% increment figureId20211203 %}. Butterworth low-pass amplitude response in decibels for 2nd, 4th, and 11th orders plotted against the ideal response._


To obtain the transfer function, I used the `Polynomial` class from the `numpy.polynomial.polynomial` module of the NumPy library.

SciPy has a [ready-made function to obtain the transfer function of an arbitrary analog filter with one of 5 different design methods](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.iirfilter.html). Alternatively, you may check out [my implementation for the Butterworth case](https://github.com/JanWilczek/wolf-sound-blog/tree/master/_py/posts/fx/2021-12-03-analog-prototype/butterworth_response.py).

To obtain plots in Figures 4 and 5, I used the `scipy.signal.freqs` function from the Python SciPy library. 

All these SciPy functions have their equivalents in Matlab.

## Summary

We did it! We obtained the transfer function of an analog low-pass filter which we can now digitize with the bilinear transform and then transform to the desired form (high-pass, band-pass, etc.).

I put a lot of effort into this article: if you find it useful, please, let me know in the comments!

If you have any questions, I would be happy to answer them in the comments as well.

Thank you for reading! 🙂

## Bibliography

[OppenheimSchafer10] [Alan V Oppenheim, Ronald W. Schafer, *Discrete-Time Signal Processing*, 3rd Edition, Pearson 2010.](https://amzn.to/3vygXGl)

[ParksBurrus87]  [T. W. Parks, C. S. Burrus, *Digital Filter Design*, John Wiley & Sons, Inc., 1987.](https://amzn.to/3DyoXJE)

[Smith07] [Julius O. Smith, *Introduction to Digital Filters with Audio Applications*,
http://ccrma.stanford.edu/~jos/filters/](http://ccrma.stanford.edu/~jos/filters/), online book, 2007 edition,
accessed November 26, 2021.

[VälimäkiReiss16] [Vesa Välimäki, Joshua D. Reiss, *All About Audio Equalization: Solutions and Frontiers* [PDF]](https://www.mdpi.com/2076-3417/6/5/129/pdf), Applied Sciences, Vol. 6, Issue 5, May 6, 2016.

[Zölzer08] [Zölzer Udo, *Digital Audio Signal Processing*, 2nd ed., Helmut Schmidt University, Hamburg, Germany, John Wiley & Sons Ltd, 2008.](https://amzn.to/30XUTdn)

{% include affiliate-disclaimer.html %}


