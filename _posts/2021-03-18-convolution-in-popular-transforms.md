---
title: "Convolution Property of Fourier, Laplace, and Z-Transforms"
date: 2021-03-18
author: Jan Wilczek
layout: post
permalink: /convolution-property-of-fourier-laplace-and-z-transforms/
background: /assets/img/posts/2021-03-18-convolution-in-popular-transforms/Thumbnail.png
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
How does the convolution relate to the most popular transforms in signal processing?

<iframe width="560" height="315" src="https://www.youtube.com/embed/f3pjtqYUlW0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

{% katexmm %}

The *convolution property* appears in at least in three very important transforms: the Fourier transform, the Laplace transform, and the $z$-tranform. These are the most often used transforms in continuous and discrete signal processing, so understanding the significance of convolution in them is of great importance to every engineer. In this article the definitions of the aforementioned transforms are presented, followed by their respective convolution property versions with their proofs.

## The Convolution Series
1. [Definition of convolution and intuition behind it]({% post_url 2020-06-20-the-secret-behind-filtering %})
1. [Mathematical properties of convolution]({% post_url 2020-07-05-mathematical-properties-of-convolution %})
1. **Convolution property of Fourier, Laplace, and z-transforms**
1. [Identity element of the convolution]({% post_url 2021-04-01-identity-element-of-the-convolution %})
1. [Star notation of the convolution]({% post_url 2021-04-03-star-notation-of-the-convolution-a-notational-trap %})
1. [Circular vs. linear convolution]({% post_url 2021-05-07-circular-vs-linear-convolution %})

# Recap
Let us briefly recap the definition of the discrete convolution
$$ x[n] \ast h[n] = \sum_{k=-\infty}^{\infty} x[k] h[n - k], \quad n \in \mathbb{Z} \quad (1)$$
and the continuous convolution
$$ x(t) \ast h(t) = \int \limits_{-\infty}^{\infty} x(\tau) h(t - \tau) d\tau, \quad t \in \mathbb{R}. \quad (2)$$
Here we assume that $x[n], h[n]$ are discrete-time, square-summable signals and $x(t), h(t)$ are continuous-time, square-integrable signals.

To understand these properties more easily, we can think of $h$ as a filter's impulse response and $x$ as an input signal to that filter. But I wouldn't like this intuition to cloud the bigger picture; these properties are much more general than this particular interpretation.

# In Short
The main takeaway from this article is that convolution in the time domain changes to multiplication (possibly with some additional constraints) in the transform domain. In particular,
1. For the Fourier transform, $x(t) \ast h(t) \stackrel{\mathcal{F}}{\longleftrightarrow} X(j\omega)H(j\omega)$.
1. For the Laplace transform, $x(t) \ast h(t) \stackrel{\mathcal{L}}{\longleftrightarrow} X(s)H(s)$ with the region of convergence (ROC) containing the intersection of $X(s)$'s ROC and $H(s)$'s ROC.
1. For the $z$-transform, $x[n] \ast h[n] \stackrel{\mathcal{Z}}{\longleftrightarrow} X(z)H(z)$ with the ROC containing the intersection of $X(z)$'s ROC and $H(z)$'s ROC.

Analogously, convolution in the transform domain changes to multiplication in the time domain. This symmetry should be clear from the derivations, so I only mention it once.

The article explains these relations in detail and gives proofs of the corresponding convolution property versions.

# Fourier Transform

The Fourier transform is without a doubt the most important transform in signal processing. For a continuous signal $x(t)$ it is defined as follows [1, Eq. 4.25]

$$ \mathcal{F}\{x(t)\} = X(j\omega) = \int \limits_{-\infty}^{\infty} x(t) e^{-j\omega t} dt. \quad (3) $$

$x(t)$ and $X(j\omega)$ are referred to as as a **Fourier transform pair**. We can denote this by

$$ x(t) \stackrel{\mathcal{F}}{\longleftrightarrow} X(j\omega). \quad (4) $$

While $t$ is interpreted as continuous time, $\omega$ is interpreted as **angular frequency** with the unit of rad/s.

## The Convolution Property
The behavior of convolution under any of the three discussed transforms bears the name of the **convolution property**. When the following transforms exist

$$ x(t) \stackrel{\mathcal{F}}{\longleftrightarrow} X(j\omega), \quad (5) $$

$$ h(t) \stackrel{\mathcal{F}}{\longleftrightarrow} H(j\omega), \quad (6) $$

the transform of their convolution is the multiplication of their transforms [1, Eq. 4.56]

$$x(t) \ast h(t) \stackrel{\mathcal{F}}{\longleftrightarrow} X(j\omega)H(j\omega). \quad (7)$$

*Note: The same holds for the Fourier transform of discrete signals (not to be confused with the discrete Fourier transform). For details, see [2, p. 60].*

### Proof

We can prove the convolution property by definining

$$ y(t) = x(t) \ast h(t) \quad (8) $$

and deriving its Fourier transform

$$  Y(j\omega) = \mathcal{F}\{y(t)\} = \int \limits_{-\infty}^{\infty} y(t) e^{-j\omega t} dt \\
    = \int \limits_{-\infty}^{\infty} (x \ast h)(t) e^{-j\omega t} dt \\
    = \int \limits_{-\infty}^{\infty} \int \limits_{-\infty}^{\infty} x(\tau)h(t - \tau) e^{-j\omega t} dt d\tau\\
    = \int \limits_{-\infty}^{\infty} x(\tau) e^{-j\omega \tau} \int \limits_{-\infty}^{\infty} h(t - \tau) e^{-j\omega (t-\tau)} dt d\tau\\
    = \int \limits_{-\infty}^{\infty} x(\tau) e^{-j\omega \tau} H(j\omega) d\tau\\
    = \int \limits_{-\infty}^{\infty} x(\tau) e^{-j\omega \tau} d\tau H(j\omega) \\
    = X(j\omega) H(j\omega). \quad \Box$$

### Application

The convolution property of the Fourier transform has a number of practical applications, namely, it enables
* fast convolution algorithms,
* efficient implementations of various signal processing algorithms via frequency-domain filtering,
* deconvolution in the frequency domain,
* frequency-based filter design,
* cascaded systems analysis,
* further transform properties derivations.

Additionally, the convolution property makes the commutativity property from the [previous article]({% post_url 2020-07-05-mathematical-properties-of-convolution %}) immediately obvious, as the multiplication operands $X(j\omega)$ and $H(j\omega)$ can be exchanged.

# Laplace transform
The Laplace transform is another frequently used transform even outside the field of engineering. For example, it plays an important role in solving differential equations. 

The Laplace transform of $x(t)$ is defined as follows [1, Eq. 9.3]

$$ X(s) = \mathcal{L} \{x(t)\} = \int \limits_{-\infty}^{\infty} x(t) e^{-st} dt, \quad s \in \mathbb{C}, \quad (9) $$

where $s$ is a complex-frequency variable. It is important to note that $X(s)$ may only exist for certain values of $s$. The region in the complex-frequency plane containing all values of $s$ for which the integral in Equation 9 converges is called the **region of convergence (ROC)** of the Laplace transform. In this article, I denote ROC of $X(s)$ by $R_X$. (Thus, in Equation 9 I should have written $s \in R_X$).

The relationship between $x(t)$ and $X(s)$ is denoted by

$$ x(t) \stackrel{\mathcal{L}}{\longleftrightarrow} X(s). \quad (10) $$

## Convolution Property
When the following transforms exist

$$ x(t) \stackrel{\mathcal{L}}{\longleftrightarrow} X(s), \quad s \in R_X, \quad (11) $$

$$ h(t) \stackrel{\mathcal{L}}{\longleftrightarrow} H(s), \quad s \in R_H, \quad (12) $$

the Laplace transform of their convolution is the multiplication of their transforms [1, Eq. 9.95]

$$x(t) \ast h(t) \stackrel{\mathcal{L}}{\longleftrightarrow} X(s)H(s), \quad s \in R_{XH}, \quad (13)$$

where $R_{XH}$ denotes the region of convergence of the transform. It is guaranteed that $(R_X \cap R_H) \subseteq R_{XH}$, but $R_{XH}$ may be larger than just the intersection of the two ROCs. Note that convolution implicitly alters the region of convergence of both involed signals' transforms. 

### Proof
By substituting $s = j\omega$ we can notice that the Fourier transform is a special case of the Laplace transform. As such, it is no surprise that the proof of the convolution property of the Laplace transform is analogous to the respective proof for the Fourier transform. Thus, refer back to that proof replacing $j\omega$ with $s$; the result is the same.

### Application
Without going into details, let me just mention that the convolution property of the Laplace transform plays an important role in the analysis of [linear time-invariant (LTI) systems](https://en.wikipedia.org/wiki/Linear_time-invariant_system).

# Z-transform
What the Laplace transform does for continuous-time systems, the $z$-transform does for discrete-time systems. System analysis is typically easier in the complex-frequency domain than directly in the time domain.

The $z$-transform of a discrete signal $x[n]$ is defined as follows

$$ \mathcal{Z}\{x[n]\} = X(z) = \sum \limits_{n=-\infty}^{\infty} x[n] z^{-n}, \quad z \in R_X, \quad (14)$$

where $R_X$ denotes the region of convergence of the transform, i. e., the set of values for which the infinite sum in Equation 14 converges.

Again, the relation between $x[n]$ and $X(z)$ is denoted by

$$ x[n] \stackrel{\mathcal{Z}}{\longleftrightarrow} X(z), \quad z \in R_X. \quad (15)$$

## Convolution Property
When the following transforms exist

$$ x[n] \stackrel{\mathcal{Z}}{\longleftrightarrow} X(z), \quad z \in R_X, \quad (16) $$

$$ h[n] \stackrel{\mathcal{Z}}{\longleftrightarrow} H(z), \quad z \in R_H, \quad (17) $$

the $z$-transform of their convolution is the multiplication of their transforms [1, Eq. 10.81]

$$x[n] \ast h[n] \stackrel{\mathcal{Z}}{\longleftrightarrow} X(z)H(z), \quad z \in R_{XH}, \quad (13)$$

where $R_{XH}$ denotes the region of convergence of the transform. As in the case of the Laplace transform, it is guaranteed that $(R_X \cap R_H) \subseteq R_{XH}$, but $R_{XH}$ may be larger than the intersection of the two ROCs.

### Proof
The proof of the convolution property is rather straightforward
$$ \mathcal{Z}\{x[n] \ast h[n]\} = \sum \limits_{n=-\infty}^{\infty} (x \ast h)[n] z^{-n} \\
    = \sum \limits_{n=-\infty}^{\infty} \left(\sum \limits_{k=-\infty}^{\infty} x[k] h[n-k]\right) z^{-n} \\
    = \sum \limits_{k=-\infty}^{\infty} x[k] z^{-k} \sum \limits_{n=-\infty}^{\infty} h[n-k] z^{-(n-k)} \\
    = \sum \limits_{k=-\infty}^{\infty} x[k] z^{-k} H(z) \\
    = X(z)H(z). \quad \Box$$

# Summary
In this article the convolution property of the Fourier, Laplace, and $z$-transform were shown along with their proofs. In general, convolution in the time domain corresponds to multiplication in the transform domain. Keep this simple rule in mind, and you'll be able to simplify or speed up your signal processing tasks at hand.

# Bibliography

[1] Alan V. Oppenheim, Alan S. Willsky, with S. Hamid *Signals and Systems*, 2nd Edition, Pearson 1997.

[2] Alan V. Oppenheim, Ronald W. Schafer *Discrete-Time Signal Processing*, 3rd Edition, Pearson 2010.

{% endkatexmm %}
