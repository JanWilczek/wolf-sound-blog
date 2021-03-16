---
title: "Convolution in popular transforms"
date: 2021-03-18
author: Jan Wilczek
layout: post
permalink: /convolution-in-popular-transforms/
background: /assets/img/posts/2020-06-20-the-secret-behind-filtering/h_superposed.png
categories:
 - DSP
tags:
 - convolution
 - fourier
 - laplace
 - transform
 - maths
 - dsp
---
How does convolution relate to the most popular transforms in signal processing?

{% katexmm %}

The *convolution property* appears in at least in three very important transforms: the Fourier transform, the Laplace transform, and the $z$-tranform. These are the most often used transforms in continuous and discrete signal processing, so understanding the significance of convolution in them is of great importance to every engineer. In this article the definitions of the aforementioned transforms are presented, followed by their respective convolution property versions and the respective proofs.

## The Convolution Series
1. [Definition of convolution and intuition behind it]({% post_url 2020-06-20-the-secret-behind-filtering %})
1. [Mathematical properties of convolution]({% post_url 2020-07-05-mathematical-properties-of-convolution %})
1. **Convolution in popular transforms**

# Recap
Let us briefly recap the definition of the discrete convolution
$$ x[n] \ast h[n] = \sum_{k=-\infty}^{\infty} x[k] h[n - k], \quad n \in \mathbb{Z} \quad (1)$$
and the continuous convolution
$$ x(t) \ast h(t) = \int \limits_{-\infty}^{\infty} x(\tau) h(t - \tau) d\tau, \quad t \in \mathbb{R}. \quad (2)$$
Here we assume that $x[n], h[n]$ are discrete-time signals and $x(t), h(t)$ are continuous-time signals. No further assumptions on these are made.

To understand these properties more easily, we can think of $h$ as a filter's impulse response and $x$ as an input signal to that filter. But I wouldn't like this intuition to cloud the bigger picture; these properties are much more general than this simple intuition.

# In Short
The main takeaway from this article is that convolution in the time domain changes to multiplication (possibly with some additional constraints) in the transform domain. In particular,
1. For the Fourier transform $x(t) \ast h(t) \stackrel{\mathcal{F}}{\longleftrightarrow} X(j\omega)H(j\omega)$.
1. For the Laplace transform $x(t) \ast h(t) \stackrel{\mathcal{L}}{\longleftrightarrow} X(s)H(s)$ with the region of convergence (ROC) being the intersection of $X(s)$'s ROC and $H(s)$'s ROC.
1. For the $z$-transform $x[n] \ast h[n] \stackrel{\mathcal{Z}}{\longleftrightarrow} X(z)H(z)$ with the ROC being the intersection of $X(z)$'s ROC and $H(z)$'s ROC.

Analogously, convolution in the transform domain changes to multiplication in the time domain.

The article explains these relations in detail and gives proofs of the corresponding convolution property versions.

# Fourier Transform

The Fourier transform is without a doubt the most important transform in signal processing. For a continuous signal $x(t)$ it is defined as follows [1, Eq. 4.25]

$$ \mathcal{F}\{x(t)\} = X(j\omega) = \int \limits_{-\infty}^{\infty} x(t) e^{-j\omega t} dt. \quad (3) $$

$x(t)$ and $X(j\omega)$ are referred to as as a **Fourier transform pair**. We can denote this as

$$ x(t) \stackrel{\mathcal{F}}{\longleftrightarrow} X(j\omega). \quad (4) $$

While $t$ is interpreted as continuous time, $\omega$ is interpreted as **angular frequency** with the unit of rad/s.

## The Convolution Property
The behavior of convolution under any of the three discussed transforms bears the name of the **convolution property**. When the following transforms exist

$$ x(t) \stackrel{\mathcal{F}}{\longleftrightarrow} X(j\omega), \quad (5) $$

$$ h(t) \stackrel{\mathcal{F}}{\longleftrightarrow} H(j\omega), \quad (6) $$

the transform of their convolution is the multiplication of their transforms

$x(t) \ast h(t) \stackrel{\mathcal{F}}{\longleftrightarrow} X(j\omega)H(j\omega). (7)$

### Proof

We can prove the convolution property by definining

$$ y(t) = x(t) \ast h(t) (8) $$

and deriving its Fourier transform



### Interpretation


# Laplace transform
## Definition

## Convolution Property

### Proof

# Z-transform
## Definition

## Convolution Property

### Proof

# Summary



# Bibliography

[1] Alan V. Oppenheim, Alan S. Willsky, with S. Hamid *Signals and Systems*, 2nd Edition, Pearson 1997.

[2] Alan V Oppenheim, Ronald W. Schafer *Discrete-Time Signal Processing*, 3rd Edition, Pearson 2010.

{% endkatexmm %}
