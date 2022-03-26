---
id: 92
title: How to represent digital sound? Sampling, sampling rate, quantization.
date: 2019-11-19T17:07:29+00:00
author: Jan Wilczek
layout: post
guid: https://thewolfsound.com/?p=92
permalink: /how-to-represent-digital-sound-sampling-sampling-rate-quantization/
content_width:
  - default_width
hide_post_title:
  - default
unlink_post_title:
  - default
hide_post_date:
  - default
hide_post_image:
  - default
unlink_post_image:
  - default
header_wrap:
  - solid
background_repeat:
  - fullcover
themify_used_global_styles:
  - 'a:1:{i:0;s:0:"";}'
tbp_custom_css:
  - ""
image: /wp-content/uploads/2019/11/thumbnail_sampling.png
background: /wp-content/uploads/2019/11/thumbnail_sampling.png
categories:
  - Digital Signal Processing
tags:
  - quantization
  - sample rate
  - sampling (A/D conversion)
discussion_id: 2019-11-19-how-to-represent-digital-sound-sampling-sampling-rate-quantization
---
To process the audio signal, we need to somehow represent it on our machine. Several different options are possible, but the most common and useful one for sound processing is the discrete sample representation. That&#8217;s where the concepts of sampling and quantization come into play.

<iframe width="560" height="315" src="https://www.youtube.com/embed/f53m72uLa2I" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

{% katexmm %}


Mind you, that in this article expressions _function_ and _signal_ are used interchangeably. Both function and signal can be continuous or discrete.

## How to represent a continuous function through discrete values?

The computers and hardware we are using are only capable of storing finite-valued numbers, e.g. 2, -5, 9.5, 10e3, some with less accuracy than others due to binary representation. How to represent a continuous (analog) function through such numbers?

If we know that the observed function of time $t$ is affine we can write:

$$s(t) = at + b$$

and store the a and b coefficients, which are discrete numbers. Whenever someone asks for the $s$ value at a particular time $t$ we can easily calculate the output using the formula above.

If the signal is a sinusoid, it is completely determined by its amplitude $A$ , frequency  $f$ and phase offset $\phi$:

$$s(t) = A\sin(2\pi f t + \phi)$$

In general, we do not know how does the signal we are observing look like: that&#8217;s the whole point of observing it, right? That&#8217;s where sampling comes in.

![](https://thewolfsound.com/wp-content/uploads/2019/11/Sine1Hz-1-1024x723.png)
*An example of the observed signal: a 1 Hz sine (one period).*
  
![](https://thewolfsound.com/wp-content/uploads/2019/11/Sine1HzSamples8Hz-2-1024x723.png)
*1 Hz sine sampled with sample rate equal to 8 Hz. Red dots mark the samples taken. Clearly the original signal can be reconstructed.*

**Sampling** is the process of measuring and storing values of the observed continuous function $s(t)$ at discrete time intervals $nT$. From mathematical point of view, we can present it as:

$$s_{discrete}(n) = s_{continuous}(t) p(t) =  s_{continuous}(t) \delta (t - n T) \text{   \{eq:sampling\}}$$

<!--  \label{eq:sampling} - not yet supported by KaTeX -->

where

$$p(t) =   \sum_{n=-\infty}^{+\infty}\delta (t - n T)$$

is called an a _sampling function_ or an _impulse-train_ (a series of discrete Dirac impulses spaced at time intervals $T$). In the equations above, $t$ is the continuous time, whereas $n$ is the index of the sample taken. Discrete Dirac&#8217;s delta $\delta (x)$ is equal to $1$ if $x$ is equal to $0$ and $0$ everywhere else:

$$\delta (x) = \begin{cases}1 & \quad\text{if } x = 0  \\  0 & \quad\text{if } x \ne 0 \end{cases}$$

so the right hand side expression in {eq:sampling} is equal to $0$ unless $t = nT$. $T$ is called the sampling period and is equal to the reciprocal of the _sampling frequency_:

$$f_s = \frac{1}{T}$$

**Sampling frequency** (or **sampling rate**) is the number of samples of the continuous function (signal) we observe during one second. It is expressed in Hz ($\frac{1}{s}$).

Sampling rate is one of the most fundamentals parameters of any digital system we work with. It determines the behavior of many algorithms and the way we process sound. Most importantly, it specifies how we store and reproduce the sound.

A theorem of utmost importance is the _sampling theorem_.

## The sampling theorem

If $f_{max}$ is the maximum frequency in the observed signal $s(t)$, it can be uniquely represented by a discrete sequence $s(nT)$ if

$$f_{max} < \frac{f_s}{2},$$

where $t \in \mathbb{R}$, $n \in \mathbb{Z}$ and $T = \frac{1}{f_s}$.

What sampling theorem says, is that you need to take at least 3 samples per function&#8217;s period in order to be able to restore it to the continuous form. How the restoration will not be explained here.

This theorem goes by many names, among which different combinations of names Nyquist, Shannon and Kotelnikov are used. Its significance can be seen in its multiple corollaries and many applications, also in sound programming.

The quantity of $\frac{f_s}{2}$ is referred to as _Nyquist frequency_. In general, the signal we wish to observe, should not contain frequencies above the Nyquist frequency. Otherwise our sampling is prone to _aliasing_ which will be explained in another article. Suffice it to say, that it disturbes our view of the signal.

## Quantization

Not only we are not able to store continuous functions directly on digital machines, but we also fail to represent all its values precisely. **Quantization** describes, which values can we store adequately.

**Quantization in time** directly follows from the sampling methodology. We are only able to sample as fast as our _analog-to-digital_ _converters_ (ADCs) let us. From a practical perspective, it is quite desirable to have evenly spaced samples, rather than intervals of varying length between successive samples. It lets us analyze the signal more easily and apply various mathematical operations (e.g. we are able to formulate it with the use of the impulse-train function $p(t)$).

**Quantization in amplitude** restricts the precision of our observation in the value of the samples we take. It starts in ADCs and can be changed throughout the digital system. Whenever we change quantization to a less fine-grained system, we lose information.

On a machine samples&#8217; values can be stored as _integers_ (integer numbers of range specified by the number of bits used to represent them) or _floating-point numbers_ (capable of capturing very small as well as very large quantities). The former can be met in programming under the names of _short, int, long_ and the latter as _float_ or _double_. It is not within the scope of this article to explain the above-mentioned formats, but all of them are well-documented throughout the web.

Having discussed the basics of sampling and quantization, we are ready to put them into practice!

## Sampling code example

This example code samples a 1 Hz sine with the sample rate of 8 Hz and displays the results:

```python
#!/usr/bin/env python3
"""Example of sine sampling"""
import numpy as np
import matplotlib.pyplot as plt
__author__  = "Jan Wilczek"
__license__ = "GPL"
__version__ = "1.0.0"

# Plotting parameters
plt.rcParams.update({'font.size': 18})
xlim = [-0.01, 1.01]
yticks = [-1.0, 0.0, 1.0]

def signal(A, f, t):
    """
    :param A: amplitude
    :param f: frequency in Hz
    :param t: time in s
    :return: sine with amplitude A at frequency f over time t
    """
    return A * np.sin(2 * np.pi * f * t)

# Observed signal's parameters
A = 1       # amplitude
f = 1       # frequency of the observed signal in Hz
fs = 48000  # basic sampling rate in Hz, to make observed signal seem "continuous"

# Signal's generation
t = np.linspace(0, 1, fs)   # "continuous" time in s
s_t = signal(A, f, t)

plt.figure(figsize=(10,7))
plt.title(f'Sine to be sampled at f={f} Hz')
plt.plot(t, s_t, linewidth=3)
plt.hlines(0, xmin=xlim[0], xmax=xlim[1], colors='black')
plt.xlim(xlim)
plt.xlabel('t [s]')
plt.ylabel('s(t)')
plt.yticks(yticks)
plt.show()

# The sample rate we are sampling the observed signal with
sample_rate = 8     # Hz

# Actual sampling
sampled_time = np.linspace(0, 1, sample_rate)
sampled_signal = signal(A, f, sampled_time)

plt.figure(figsize=(10,7))
plt.title(f'Sampled sine at f={f} Hz sampled at fs={sample_rate} Hz')
plt.plot(t, s_t, linewidth=3)
plt.stem(sampled_time, sampled_signal, linefmt='r-', markerfmt='ro', basefmt=' ')
plt.hlines(0, xmin=xlim[0], xmax=xlim[1])
plt.xlim(xlim)
plt.xlabel('t [s]')
plt.ylabel('s(t)')
plt.yticks(yticks)
plt.show()
```

You can copy the above code and run it yourself!

Reference:  
[1] Oppenheim, A. V. and Willsky, A. S. Signals & Systems. 2nd ed. Upper Sadle River, New Jersey: Prentice Hall, 1997.

{% endkatexmm %}