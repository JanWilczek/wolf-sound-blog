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

{% capture _ %}{% increment equationId20210507  %}{% endcapture %}

Circular convolution is a term that arises in discussions about the discrete Fourier transform (DFT) and fast convolution algorithms. What is it and how does it differ from the linear convolution?

Before we answer that question we need to (somewhat surprisingly) examine the DFT more closely.

# Convolution Theorem of the DFT?

## Definition of the DFT

Let us recap the definition of the discrete Fourier transform of a finite, discrete-time signal $x[n]$ of length $N \in \mathbb{Z}$

$$ X[k] = \mathcal{DFT}\{x[n]\} = \sum \limits_{n=0}^{N-1} x[n] e^{-j(2\pi/N)kn}, k \in \mathbb{Z}, \quad ({% increment equationId20210507 %})$$

## Convolution Theorem of the Fourier Transform

In [one of the previous articles]({% post_url 2021-03-18-convolution-in-popular-transforms %}) we argued that for the continuous-time Fourier transform it holds

$$x(t) \ast h(t) \stackrel{\mathcal{F}}{\longleftrightarrow} X(j\omega)H(j\omega), \quad ({% increment equationId20210507 %})$$

i.e., the Fourier transform of a convolution equals the multiplication of the Fourier transforms of the convolved signals. A similar property holds for the Laplace and z-transforms. However, **it does not**, in general, hold for the discrete Fourier transform. Instead, multiplication of discrete Fourier transforms corresponds to the *circular convolution* of the corresponding time-domain signals [1].

## Convolution Theorem of the DFT

In mathematical terms, given two finite, discrete-time signals $x[n]$ and $h[n]$, both of length $N$, and their DFTs

$$ x[n] \stackrel{\mathcal{DFT}}{\longleftrightarrow} X[k] \quad n, k \in \{0, \dots, N-1\}, \quad ({% increment equationId20210507 %})$$

$$ h[n] \stackrel{\mathcal{DFT}}{\longleftrightarrow} H[k] \quad n, k \in \{0, \dots, N-1\}, \quad ({% increment equationId20210507 %})$$

the multiplication of their DFTs corresponds to their circular convolution in the time domain

$$ x[n] \circledast h[n] \stackrel{\mathcal{DFT}}{\longleftrightarrow} X[k] H[k]. \quad ({% increment equationId20210507 %}) $$

## Circular Convolution Definition

Here, $\circledast$ symbol denotes the circular convolution. It is defined as

$$ x[n] \circledast h[n] = \sum \limits_{m=0}^{N-1} x[m] h[(n-m) \% N], \quad ({% increment equationId20210507 %})$$

where $\%$ denotes the modulo operation, i.e., $0 \% N = 0; 1 \% N = 1; N-1 \% N = N-1; N \% N = 0,$ etc.

Since, both signals are of length $N$ (or shorter) it is called an *N-point circular convolution*.

## Linear Convolution Definition

The name "circular" distinguishes it from the *linear convolution*, as we introduced it in the previous articles

$$ x[n] \ast h[n] = \sum_{m=-\infty}^{\infty} x[m] h[n - m], \quad n \in \mathbb{Z}. \quad ({% increment equationId20210507 %})$$

Note the absence of the modulo operation. Although we do not prove it here, **circular convolution is commutative** exactly like linear convolution.

# Circular Convolution Example

Let's look at a comparisaon between a linear and circular convolution.

Let's assume we have a signal $x[n]$

![]({{ page.images | absolute_url | append: "/x_short.png" }}){: width="600" }
_Figure 1. $x[n]$._

and a [unit delay]({% post_url 2021-04-01-identity-element-of-the-convolution %}) $h[n]$

![]({{ page.images | absolute_url | append: "/unit_delay.png" }}){: width="600" }
_Figure 2. $h[n]$._

The linear convolution between the two delays $x[n]$ by one sample, as expected

![]({{ page.images | absolute_url | append: "/linear_convolution_shift.png" }}){: width="600" }
_Figure 3. Linear convolution between $x[n]$ and $h[n]$._

However, the circular convolution performs a **circular shift** of the signal $x[n]$

![]({{ page.images | absolute_url | append: "/circular_shift.png" }}){: width="600" }
_Figure 4. Circular convolution between $x[n]$ and $h[n]$._

Circular shift means that whichever samples "fall off" one end they will reappear at the other end of the signal vector. The excessive samples "wrap around" the signal buffer.

# Why Is the Convolution Circular?

The convolution property of the DFT results directly from the periodicity of the DFT.

The periodicity itself can be explained in at least two ways:
1. From the relation of the DFT and the discrete Fourier series (DFS).
1. From the sampling of the discrete-time Fourier transform around the unit circle on the z-plane.

## Discrete Fourier Transform and Discrete Fourier Series

Discrete Fourier series is a representation of a **periodic** discrete signal $\tilde{x}[n]$ with period $N$ via a summation

$$ \tilde{x}[n] = \frac{1}{N} \sum \limits_{k=0}^{N-1} \tilde{X}[k] e^{j(2\pi/N)kn}, \quad ({% increment equationId20210507 %})$$

where

$$ \tilde{X}[k] = \sum \limits_{n=0}^{N-1} \tilde{x}[n] e^{-j(2\pi/N)kn}. \quad ({% increment equationId20210507 %})$$

Equation 9 is identical to Equation 1, i.e, the definition of the DFT with the exception that the signal under the sum is periodic (denoted by the tilde). While the DFS assumes that the signal is periodic, i.e., it repeats itself modulo $N$, the DFT assumes that $x[n]$ is 0 for $n$ outside the $\{0, \dots, N-1\}$ index set [1].

The same holds for the DFT coefficients $X[k]$

$$X[k] = \begin{cases} \tilde{X}[k] \quad \text{if } k\in \{0, \dots, N-1\},\\ 0 \quad \text{otherwise}. \end{cases} \quad ({% increment equationId20210507 %})$$

Unfortunately, the fact that $x[n]$ and $X[k]$ are 0 for $n,k \notin \{0, \dots, N-1\}$ is only **implicit**. It means, we can state it, but we cannot enforce it. Since the DFT uses directly the formulas of the DFS, the DFT will behave as if the signal $x[n]$ was periodic with period $N$. The only solution to that, would be padding signal vector $x[n]$ with infinitely many zeros. Hence, the DFT $X[k]$ will also be periodic with period $N$.

### Example

Let's say we have a signal $x[n]$ given as a vector with four samples

![]({{ page.images | absolute_url | append: "/x_vector.png" }}){: width="600" }
_Figure 5. $x[n]$._

You may think it is defined as follows

![]({{ page.images | absolute_url | append: "/x_zeros.png" }}){: width="600" }
_Figure 6. $x[n]$ as we wish it to be._

but the DFS (and DFT accordingly) treat it as

![]({{ page.images | absolute_url | append: "/x_repeated.png" }}){: width="600" }
_Figure 7. $x[n]$ as seen by discrete Fourier series and the discrete Fourier transform._

Analogously, in the discrete frequency domain, we can obtain the magnitude Fourier coefficients $|X[k]|$ from Equation 1. This yields

![]({{ page.images | absolute_url | append: "/X_vector.png" }}){: width="600" }
_Figure 8. Magnitude discrete-frequency coefficients of $x[n]$._

Again, one may assume that it is defined as follows

![]({{ page.images | absolute_url | append: "/X_zeros.png" }}){: width="600" }
_Figure 9. Magnitude DFT of $x[n]$ naively visualized with zeros surrounding the 4 nonzero coefficients._

but the inherent periodicity of the DFT results in

![]({{ page.images | absolute_url | append: "/X_repeated.png" }}){: width="600" }
_Figure 10. True magnitude DFT of $x[n]$._

## Sampling of the Fourier transform

All of the above observations are confirmed when one treats DFT as sampled version of the band-limited discrete-time Fourier transform. Discrete-time Fourier transform is the z-transform evaluated on the unit circle [2]. The DFT samples the DTFT at the points fixed by the sampling rate. Since we sample around a circle, after $N$ samples we wrap around and start sampling the same points again. Refer to [1] for a more detailed explanation of this approach to DFT's periodicity.

## Aliasing in the Time Domain

Having established that the DFT is periodic, we can now explain the circular convolution phenomenon. I like to think of it as **aliasing in the time domain**.

*Note: We have discussed the notion of aliasing in the frequency domain in [one of the previous articles]({% post_url 2019-11-28-what-is-aliasing-what-causes-it-how-to-avoid-it %}).*

### Output Length of Discrete Convolution

Let's recall our signal $x[n]$ from Figure 1. In vector notation, we could denote it as $\pmb{x} = [1, 0.7, 0.3, 0.1]^\text{T}$, where T denotes transposition to make $\pmb{x}$ a column vector. Analogously, $\pmb{h} = [0, 1]^\text{T}$.

Signal $\pmb{x}$ is of length 4, signal $\pmb{h}$ is of length 2. In Figure 3 we can see that the linear convolution between $\pmb{x}$ and $\pmb{h}$ is of length 5. In general, convolution of two sequences of length $N$ and $M$ yields a signal of length $N + M - 1$. <!-- Quotation needed -->

How does it look when we go through the DFT domain?

### Multiplication in the DFT domain

Adopting the notation from Equations 3 and 4, let's denote by $Y[k]$ the multiplication of $x$ and $h$ DFT's

$$ Y[k] = X[k]H[k] \quad k \in \mathbb{Z}. \quad ({% increment equationId20210507 %})$$

In order to make the index $k$ correspond to the same discrete frequencies, $\pmb{X}$ and $\pmb{H}$ need to be of equal length. We achieve it by padding $\pmb{h}$ with 2 zeros, i.e., $\pmb{h} = [0, 1, 0, 0]^\text{T}$. Now $\pmb{x}$ and $\pmb{h}$ are of equal length and their DFTs are as well. We obtain

$$\pmb{Y} = \pmb{X} \odot \pmb{H}, \quad ({% increment equationId20210507 %})$$

where $\odot$ denotes the Hadamard product of vectors (element-wise multiplication).

### Back to the time domain

We now want to find signal $y[n]$ that corresponds to $Y[k]$, i.e.,

$$ y[n] \stackrel{\mathcal{DFT}}{\longleftrightarrow} Y[k]. \quad ({% increment equationId20210507 %})$$

We can achieve it via inverse discrete Fourier transform (iDFT)

$$y[n] = \mathcal{IDFT}\{Y[k]\} = \sum \limits_{k=0}^{N-1} Y[k] e^{j(2\pi/N)kn}. \quad ({% increment equationId20210507 %})$$

If $x$ and $h$ were continuous-time and we were using Fourier transform instead of discrete Fourier transform, the [convolution theorem]({% post_url 2021-03-18-convolution-in-popular-transforms %}) would tell us that $y$ is the convolution of $x$ and $h$. We explicitly showed that the convolution of $x$ and $h$ should be a discrete signal of length 5. How long is $y$?

Inverse DFT inherently assumes that the time domain signal is of the same length as the frequency-domain coefficient vector. Thus, $y[n]$ is of length 4. So by multiplying frequency-domain vectors $\pmb{X}$ and $\pmb{H}$ and going back to the discrete-time domain we squashed a 5-element-long vector into a 4-element-long vector. Thus, we introduced aliasing in the time domain; hence the wrap-around of the last sample in Figure 4, and more broadly, circular convolution effect.

In mathematical terms,

$$y[n] =  x[n] \circledast h[n]. \quad ({% increment equationId20210507 %})$$

### An Important Conclusion

We have seen that the circular convolution somehow distorts the linear convolution. But in our example, $x$ was circularly shifted, not completetely destroyed. Moreover, all but the first and the last samples were valid samples of the linear convolution. Thus, we might suspect that sufficiently lenghtening $\pmb{x}$ and $\pmb{h}$ with zero-padding would allow us to obtain linear convolution out of the circular convolution result. This is the basis of **fast convolution** algorithms, which will be discussed in one of the following articles.

# Circular vs. Linear Convolution

The conclusion from the previous section is that

> A subset of the circular convolution result corresponds to the linear convolution result.

The question is: which subset?

## Example: Common Samples of Linear and Circular Convolution

<!-- Insert convolution comparison with matching samples marked -->

To understand fully which samples in the circular convolution correspond to the correct samples of linear convolution we need to look at a concept broader than circular convolution: periodic convolution.

# Periodic Convolution

Circular convolution is an example of *periodic convolution*&#8211;a convolution of two periodic sample sequences (with the same period) evaluated over only one period [1]. "But in our case $x$ and $h$ are not periodic!", you might say. Yes, they are not periodic, unless we compute their DFTs. DFT assumes the signal to be perodic and, thus, going into the DFT domain introduces the periodicity permanently. It does not have to be harmful; on the contrary, it can be quite useful. It just requires us to be extra cautious.

# Summary

In this article, we looked at the difference between the circular and linear convolution. The former treats both given sequences as periodic and is evaluated only for the number of samples corresponding to the period. A subset of samples resulting from circular convolution corresponds to the samples in the linear convolution's output.

# Bibliography

[1] Alan V Oppenheim, Ronald W. Schafer *Discrete-Time Signal Processing*, 3rd Edition, Pearson 2010.

[2] Alan V. Oppenheim, Alan S. Willsky, with S. Hamid *Signals and Systems*, 2nd Edition, Pearson 1997.

{% endkatexmm %}
