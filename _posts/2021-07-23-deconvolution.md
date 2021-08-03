---
title: "Deconvolution: Inverse Convolution"
date: 2021-07-23
author: Jan Wilczek
layout: post
permalink: /deconvolution-inverse-convolution/
images: assets/img/posts/2021-07-23-deconvolution
background: /assets/img/posts/2021-07-23-deconvolution/Thumbnail.png
categories:
 - Digital Signal Processing
tags:
 - convolution
discussion_id: 2021-07-23-deconvolution
---
Can we invert the effect of convolution?

## The Convolution Series
1. [Definition of convolution and intuition behind it]({% post_url 2020-06-20-the-secret-behind-filtering %})
1. [Mathematical properties of convolution]({% post_url 2020-07-05-mathematical-properties-of-convolution %})
1. [Convolution property of Fourier, Laplace, and z-transforms]({% post_url 2021-03-18-convolution-in-popular-transforms %})
1. [Identity element of the convolution]({% post_url 2021-04-01-identity-element-of-the-convolution %})
1. [Star notation of the convolution]({% post_url 2021-04-03-star-notation-of-the-convolution-a-notational-trap %})
1. [Circular vs. linear convolution]({% post_url 2021-05-07-circular-vs-linear-convolution %})
1. [Fast convolution]({% post_url 2021-05-14-fast-convolution %})
1. [Convolution vs. correlation]({% post_url 2021-06-18-convolution-vs-correlation %})
1. [Convolution in MATLAB, NumPy, and SciPy]({% post_url 2021-07-09-convolution-in-numpy-matlab-and-scipy %})
1. **Deconvolution: Inverse convolution**
1. [Convolution in probability: Sum of independent random variables]({% post_url 2021-07-30-convolution-in-probability %})

{% katexmm %}

{% capture _ %}{% increment equationId20210723  %}{% endcapture %}

# Deconvolution Definition

Given the output of the convolution operation $y[n]$

$$y[n] = x[n] \ast h[n], \quad ({% increment equationId20210723 %})$$

where $x[n]$ is the input signal and $h[n]$ is the impulse response of a [linear time-invariant (LTI) system](https://en.wikipedia.org/wiki/Linear_time-invariant_system), we may want to estimate

1. $x[n]$ given $h[n]$ (input signal given the system),
1. $h[n]$ given $x[n]$ (system given the input signal, so-called system identification), or
1. both, $x[n]$ and $h[n]$ (input signal and the system simultaneously, so-called blind deconvolution).

While tasks 1 and 2 are somewhat similar thanks to the commutativity of convolution (identify one signal given two others), task 3 poses a significant challenge that is an active area of research.

This article contains a brief description of various methods used to accomplish deconvolution. By no means is this list complete nor are the explanations in-depth. Nevertheless, it will give you an overview of the methodologies used and when to use them.

But before I give you a tour of the deconvolution methods, I will present two vivid use cases of deconvolution to motivate the topic. 

## Example Application of Non-Blind Deconvolution

A simple example of deconvolution application is frequency response measurement of a loudspeaker. The excitation signal in this case cannot be an impulse because it could damage the loudspeaker. A fairly often used option is to use an exponential sweep: a signal whose frequency rises exponentially over time. Having recorded the response of a loudspeaker to the exponential sweep excitation, we need to deconvolve it to obtain just the loudspeaker's impulse response. The loudspeaker is our unknown $h[n]$, $x[n]$ is the exponential sweep, and $y[n]$ is the recorded response. Thus, it is a system identification problem.

## Example Application of Blind Deconvolution

Imagine a smart home system. Whenever one of the users (residents) speaks up, the system needs to record that speech, perform automatic speech recognition, understand the message conveyed by speech, and ultimately decide what action to take. All these tasks are significantly more dificult when the recorded speech is reverberant, i.e., bears the impact of room acoustics. The system knows neither the speech utterance nor the room impulse response (which varies with user and smart device positions). Thus, it needs to use statistical or machine learning algorithms to infere which is which and improve the quality of the recorded speech.

In this case, $x[n]$ is the speech signal, $h[n]$ is the room's impulse response, and $y[n]$ is the signal recorded by the smart device.

# A Catalogue of Deconvolution Methods

What follows is a quick tour of some of the deconvolution approaches where either the input signal or the system (but not both) are known. If you are interested in the topic, you are welcome to follow the sources specified at the end.

Here's a navigable table of contents:
1. [Deconvolution Using Frequency-Domain Division](#deconvolution-using-frequency-domain-division)
   1. [Deconvolution Functions in Numerical Software](#deconvolution-functions-in-numerical-software)
1. [Deconvolution Via (Pseudo-)Inverse of the Convolution Matrix](#deconvolution-via-pseudo-inverse-of-the-convolution-matrix)
1. [Wiener Filtering (Wiener Deconvolution)](#wiener-filtering-wiener-deconvolution)
1. [Deconvolution Using Complex Cepstrum Liftering](#deconvolution-using-complex-cepstrum-liftering)

## Deconvolution Using Frequency-Domain Division

As we know from the [convolution property of the $z$-transform]({% post_url 2021-03-18-convolution-in-popular-transforms %}), a convolution of time-domain signals is equivalent to multiplication of their $z$-transforms. Thus, why not try to deconvolve the signals in the $z$-domain?

In the following we will assume that capital letters denote the $z$-transforms of the time-domain signals. We have

$$y[n] = x[n] \ast h[n], \quad ({% increment equationId20210723 %})$$

$$Y(z) = X(z)H(z). \quad ({% increment equationId20210723 %})$$

With this formulation we can easily obtain the desired time domain signal $h[n]$ if we know $x[n]$

$$h[n] = \mathcal{Z}^{-1} \{H(z)\} = \mathcal{Z}^{-1} \left\{ \frac{Y(z)}{X(z)} \right\}. \quad ({% increment equationId20210723 %})$$

There are two caveats to this approach:
1. $X(z)$ mustn't be zero for any $z$ (we mustn't divide by 0),
1. The inverse $z$-transform in Equation (4) must exist.

With that in mind, we can present two numerical software functions that use the above approach.

### Deconvolution Functions in Numerical Software

Deconvolution in numerical software is achieved through polynomial division in the $z$-domain, as in Equation (4).

In SciPy and Matlab, we have two very similar functions for deconvolution:

```python
quotient, remainder = scipy.signal.deconvolve(signal, divisor)
```
```matlab
[quotient, remainder] = deconv(signal, divisor)
```

In these functions, the divisor is deconvolved from signal to obtain the quotient. The remainder is the signal that could not be properly deconvolved (typically because of numerical precision). For these operations, the following identities should hold
```python
signal = convolve(divisor, quotient) + remainder
```
```matlab
signal = conv(divisor, quotient) + remainder
```

Keep in mind the caveats above: if the divisor signal has zeros in its $z$-transform, then the application of the above functions will lead to noise amplification and, ultimately, worthless output.

## Deconvolution Via (Pseudo-)Inverse of the Convolution Matrix

If we write the convolution in Equation (1) in a matrix form it should be easier for us to reason about it. First, let's write $x[n]$ in a vector form

$$\pmb{x}[n] = [x[n], x[n-1], \dots, x[n-M-N+1]]^\top, \quad  ({% increment equationId20210723 %})$$

where $M$ is the length of the impulse response $h$ and $N$ is the length of the observation window $\pmb{y}[n]$. 

Second, we can write

$$\pmb{y}[n] = \mathbf{H} \pmb{x}[n], \quad ({% increment equationId20210723 %})$$

where $\mathbf{H}$ is an $N \times (M+N-1)$ *convolution matrix* which has *Toeplitz structure* (identical elements along each diagonal of the matrix)

$$\mathbf{H} = \begin{bmatrix}
    h[0] & h[1] & \dots & h[M-1] & 0 & \dots & 0 \\
    0 & h[0] & h[1] & \dots & h[M-1] & \dots & 0 \\
    \vdots &  & \ddots & & & & \vdots \\
    0 & & \dots & h[0] & h[1] & \dots & h[M-1]
\end{bmatrix}. \quad ({% increment equationId20210723 %})$$

To ensure proper understanding, let's write out the elements of $\pmb{y}[n]$ analogously to $\pmb{x}[n]$

$$\pmb{y}[n] = [y[n], y[n-1], \dots, y[n-N+1]]^\top, \quad  ({% increment equationId20210723 %})$$

Since there is no additive noise, we can obtain $\pmb{x}[n]$ or its estimate $\tilde{\pmb{x}}[n]$ by

* inverting $\mathbf{H}$ if $\mathbf{H}$ is full-rank and not ill-conditioned
  
  $$\pmb{x}[n] = \mathbf{H}^{-1} \pmb{y}[n], \quad  ({% increment equationId20210723 %})$$

* computing the Moore-Penrose pseudoinverse of $\mathbf{H}$ if $\mathbf{H}$ cannot be easily inverted

  $$\tilde{\pmb{x}}[n] = (\mathbf{H}^\top\mathbf{H} + \delta \mathbf{I})^{-1}\mathbf{H}^\top \pmb{y}[n], \quad  ({% increment equationId20210723 %})$$

  where $\delta$ is a small constant added for numerical stability (so-called *Tikhonov regularization*). This is the solution of least squares minimization of the squared difference between the samples of $\pmb{y}[n]$ and $\mathbf{H}\pmb{x}[n]$.

## Wiener Filtering (Wiener Deconvolution)

What if $y[n]$ in Equation (1) is not a perfect convolution of $x[n]$ and $h[n]$ but contains some additive noise? Such situations typically occur if $y[n]$ is measured and real-world phenomena influence the result. We could write it as 

$$y[n] = x[n] \ast h[n] + w[n], \quad ({% increment equationId20210723 %})$$

where $w[n]$ denotes the noise signal that is not correlated with either $x[n]$ or $h[n]$; the crosscorrelation between $w[n]$ and either $x[n]$ or $h[n]$ is 0. That means that noise is not similar to $x$ nor $h$ in any significant way.

Assuming we know $h[n]$, we can obtain an estimate of $x[n]$, $\tilde{x}[n]$, by using a Wiener deconvolution filter [3]. This filter is defined in the frequency domain so we have

$$\tilde{x}[n] = \mathcal{F}^{-1} \{\tilde{X}(j\omega)\} = \mathcal{F}^{-1} \{G(j\omega)Y(j\omega)\}, \quad ({% increment equationId20210723 %})$$

where $\tilde{X}(j\omega)$ and $Y(j\omega)$ denote the Fourier transforms of $\tilde{x}[n]$ and $y[n]$ respectively, and $G(j\omega)$ is the inverse filter specified in the frequency domain.

The formula for $G(j\omega)$ is

$$G(j\omega) = \frac{H^*(j\omega)S_{XX}(j\omega)}{|H(j\omega)|^2 S_{XX}(j\omega) + S_{WW}(j\omega)}, \quad ({% increment equationId20210723 %})$$

where $\cdot^*$ denotes complex conjugate, $H(j\omega)$ is the Fourier transform of $h[n]$, $S_{XX}(j\omega)$ and $S_{WW}(j\omega)$ are mean power spectral densities (PSDs) of $x[n]$ and $w[n]$ respectively. (If you don't know what PSD is, don't worry; think of it as a probabilistic version of the Fourier transform. Actually, it can be estimated by properly averaging the short-time Fourier transform).

I think of the quotient in Equation (14) as a fraction of the clean signal present in the output $Y(j\omega)$. After all, if there was no noise, then $S_{WW}(j\omega) = 0$, and accordingly $G(j\omega) = \frac{1}{H(j\omega)}$, what brings Equation 12 back to Equation 4.

Surprisingly, I wasn't able to find the derivation of Equation 13; it probably can be found in the Wiener's original works from the 1940s.

## Deconvolution Using Complex Cepstrum Liftering

The *complex cepstrum* of a discrete signal $x[n]$ is defined as a stable sequence $\hat{x}[n]$ whose $z$-transform is [1]

$$\hat{X}(z) = \log X(z), \quad ({% increment equationId20210723 %})$$

where $X(z)$ is the $z$-transform of $x[n]$. Thus, $\hat{x}[n]$ can be expressed as

$$\hat{x}[n] = \frac{1}{2 \pi} \int \limits_{-\pi}^{\pi} \log(X(e^{j\omega}))e^{j\omega n} d\omega 
\\=\frac{1}{2 \pi} \int \limits_{-\pi}^{\pi} (\log |X(e^{j\omega})| + j \angle X(e^{j\omega})) e^{j\omega n} d\omega. \quad ({% increment equationId20210723 %})$$

As we know from the [convolution property of the $z$-transform]({% post_url 2021-03-18-convolution-in-popular-transforms %}), a convolution of time-domain signals is equivalent to multiplication of their $z$-transforms. If we apply a logarithm function to the multiplication of these transforms, we obtain a summation of the logarithms of the individual transforms. Mathematically speaking, if

$$y[n] = x[n] \ast h[n], \quad ({% increment equationId20210723 %})$$

then

$$Y(z) = X(z)H(z) \quad ({% increment equationId20210723 %})$$

and

$$\hat{y}[n] = \hat{x}[n] + \hat{h}[n]. \quad ({% increment equationId20210723 %})$$

If the nonzero values of $\hat{x}[n]$ and $\hat{h}[n]$ occupy different ranges of the $n$ index (different *quefrencies* of the cepstrum), we can zero-out the corresponding elements of $\hat{y}[n]$ corresponding to, for example, $\hat{h}[n]$ and after computing the inverse cepstrum obtain the signal $x[n]$. 

The operation of manipulating the elements of the cepstrum is called *liftering*.

Deconvolution via complex cepstrum liftering can be done, for example, to extract the glottal excitation from a recording of a human voice. In this case, $x[n]$ is the glottal exciation, $h[n]$ is the vocal tract impulse response (because vocal tract is a filter) and $y[n]$ is the recorded speech signal. Take note that this is another example of blind deconvolution (we initially know neither $x[n]$ nor $h[n]$).

Of course, typically $\hat{x}[n]$ and $\hat{h}[n]$ will overlap in the cepstral domain what makes the task more difficult and renders perfect deconvolution with this method impossible.

<!-- # Linear Predictive Deconvolution -->

<!-- # Parametric Modeling -->

<!-- # Linear Blind Deconvolution -->

<!-- # Nonlinear Blind Deconvolution -->

<!-- # Iterative Approach To Deconvolution -->

<!-- # Regularized Deconvolution -->

<!-- # H1 Estimator -->

<!-- # Difference Between Deconvolution and Inverse Filtering -->

<!-- # Applications -->

<!-- ## Image Processing -->

# Summary

In this article, we discussed 4 deconvolution techniques out of which 1 works in the presence of noise. For further details, please refer to the sources below.

# Bibliography

[1] Alan V Oppenheim, Ronald W. Schafer *Discrete-Time Signal Processing*, 3rd Edition, Pearson 2010.

[2] Simon Haykin, *Adaptive Filter Theory*, 5th Edition, Pearson 2014.

[3] [Wiener Deconvolution on Wikipedia](https://en.wikipedia.org/wiki/Wiener_deconvolution)

[4] [`scipy.signal.deconvolve` documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.deconvolve.html)

[5] [Matlab's `deconv` documentation](https://mathworks.com/help/matlab/ref/deconv.html)

{% endkatexmm %}
