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

{% katexmm %}

{% capture _ %}{% increment equationId20210723  %}{% endcapture %}

# Deconvolution Definition

Given the output of the convolution operation $y[n]$

$$y[n] = x[n] \ast h[n], \quad ({% increment equationId20210618 %})$$

where $x[n]$ is the input signal and $h[n]$ is an impulse response of a [linear time-invariant (LTI) system](https://en.wikipedia.org/wiki/Linear_time-invariant_system), we may want to estimate

1. $x[n]$ given $h[n]$,
1. $h[n]$ given $x[n]$ (so-called system identification),
1. both, $x[n]$ and $h[n]$ (blind deconvolution).

While tasks 1. and 2. are somewhat similar thanks to the commutativity of convolution (identify one signal given two others), task 3. poses a significant challenge that is an active area of research.

This article contains a brief description of various methods used to accomplish deconvolution. By no means is this list complete nor are the explanations in-depth. Nevertheless, it will give you an overview of the methodologies used and when to use them.

But before I give you a tour of the deconvolution methods, I will present two vivid use cases for deconvolution. 

## Example Application of Non-Blind Deconvolution

Imagine a voice-controlled TV. Such a device plays back the sound of a movie and at the same time is controlled by voice commands from the viewer. If the speakers playing back the movie soundtrack and the microphone recording the command are placed in one case, then the loudspeakers' signal will be recorded by the microphone along with the 

## Example Application of Blind Deconvolution

Imagine a voice assistant system in a car. Such a system can recognize and execute spoken commands, such as 'Show route to place X'. When the driver speaks up, the system needs to record that speech, perform automatic speech recognition, understand the message conveyed by speech, and ultimately decide what action to take. All these tasks are significantly more dificult when the recorded speech is noisy. To *denoise* it, we need to remove the impact of noise in the car on the speech recording. However, we do know neither the noise nor the speech signal. We only know the recorded noisy speech. And we can still denoise it!


# Deconvolution Using Frequency-Domain Division

# Deconvolution Using Complex Cepstrum Liftering

The *complex cepstrum* of a discrete signal $x[n]$ is defined as a stable sequence $\hat{x}[n]$ whose $z$-transform is

$$\hat{X}(z) = \log X(z), \quad ({% increment equationId20210618 %})$$

where $X(z)$ is the $z$-transform of $x[n]$.

As we know from the [convolution property of the $z$-transform]({% post_url 2021-03-18-convolution-in-popular-transforms %}), a convolution of time-domain signals is equivalent to multiplication of their $z$-transforms. If we apply a logarithm function to the multiplication of these transforms, we obtain a summation of the logarithms of the individual transforms. Mathematically speaking,

# Linear Predictive Deconvolution

# Parametric Modeling

# Linear Blind Deconvolution

# Nonlinear Blind Deconvolution

# Wiener Filtering (Wiener Deconvolution)

# Deconvolution Via Pseudo-Inverse of the Convolution Matrix

# Iterative Approach To Deconvolution

# Regularized Deconvolution

# H1 Estimator

# Deconvolution Functions in Numerical Software

## SciPy

## Matlab

# Difference Between Deconvolution and Inverse Filtering

# Applications

## Image Processing

# Summary

# Bibliography

[1] DTSP

[2] AFT

{% endkatexmm %}