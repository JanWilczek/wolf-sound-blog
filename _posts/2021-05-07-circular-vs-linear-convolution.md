---
title: "Circular vs. Linear Convolution: What's the difference?"
date: 2021-05-07
author: Jan Wilczek
layout: post
permalink: /circular-vs-linear-convolution-whats-the-difference/
# background: /assets/img/posts/2021-04-03-star-notation-of-the-convolution-a-notational-trap/Thumbnail.png
images: assets/img/posts/2021-05-07-circular-vs-linear-convolution
categories:
 - DSP
tags:
 - convolution
 - maths
 - dsp
---
What is the circular convolution and how does it differ from the linear convolution?

{% katexmm %}

## The Convolution Series
1. [Definition of convolution and intuition behind it]({% post_url 2020-06-20-the-secret-behind-filtering %})
1. [Mathematical properties of convolution]({% post_url 2020-07-05-mathematical-properties-of-convolution %})
1. [Convolution property of Fourier, Laplace, and z-transforms]({% post_url 2021-03-18-convolution-in-popular-transforms %})
1. [Identity element of the convolution]({% post_url 2021-04-01-identity-element-of-the-convolution %})
1. [Star notation of the convolution]({% post_url 2021-04-03-star-notation-of-the-convolution-a-notational-trap %})
1. **Circular vs. linear convolution**

# Introduction

Circular convolution is a term that arises in discussions about the discrete Fourier transform (DFT) and fast convolution algorithms. What is it and how does it differ from the linear convolution?

Before we answer that question we need to (somewhat surprisingly) examine the DFT more closely.

# Convolution Theorem of the DFT?

In [one of the previous articles]({% post_url 2021-03-18-convolution-in-popular-transforms %}) we argued that for the continuous-time Fourier transform it holds

{% capture _ %}{% increment equationId20210507  %}{% endcapture %}

$$x(t) \ast h(t) \stackrel{\mathcal{F}}{\longleftrightarrow} X(j\omega)H(j\omega), \quad ({% increment equationId20210507 %})$$

i.e., the Fourier transform of a convolution equals the multiplication of the Fourier transforms of the convolved signals. A similar property holds for the Laplace and z-transforms. However, **it does not**, in general, hold for the discrete Fourier transform. Instead, multiplication of discrete Fourier transforms corresponds to the *circular convolution* of the corresponding time-domain signals [1].

In mathematical terms, given two finite, discrete-time signals $x[n]$ and $h[n]$, both of length $N$, and their DFTs

$$ x[n] \stackrel{\mathcal{DFT}}{\longleftrightarrow} X[k] \quad n, k \in \{0, \dots, N-1\}, \quad ({% increment equationId20210507 %})$$

$$ h[n] \stackrel{\mathcal{DFT}}{\longleftrightarrow} H[k] \quad n, k \in \{0, \dots, N-1\}, \quad ({% increment equationId20210507 %})$$

the multiplication of their DFTs corresponds to their circular convolution in the time domain

$$ x[n] \circledast h[n] \stackrel{\mathcal{DFT}}{\longleftrightarrow} X[k] H[k]. \quad ({% increment equationId20210507 %}) $$

Here, $\circledast$ symbol denotes the circular convolution. It is defined as

$$ x[n] \circledast h[n] = \sum \limits_{m=0}^{N-1} x[m] h[(n-m) \% N], \quad ({% increment equationId20210507 %})$$

where $\%$ denotes the modulo operation, i.e., $0 \% N = 0; 1 \% N = 1; N-1 \% N = N-1; N \% N = 0,$ etc.

Since, both signals are of length $N$ (or shorter) it is called an *N-point circular convolution*.



# Bibliography

[1] Alan V Oppenheim, Ronald W. Schafer *Discrete-Time Signal Processing*, 3rd Edition, Pearson 2010.

[2] Alan V. Oppenheim, Alan S. Willsky, with S. Hamid *Signals and Systems*, 2nd Edition, Pearson 1997.

{% endkatexmm %}
