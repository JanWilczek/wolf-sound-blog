---
title: "Fast Convolution"
date: 2021-05-14
author: Jan Wilczek
layout: post
permalink: /fast-convolution/
# background: /assets/img/posts/2021-04-03-star-notation-of-the-convolution-a-notational-trap/Thumbnail.png
images: assets/img/posts/2021-05-14-fast-convolution
categories:
 - DSP
tags:
 - convolution
 - filters
 - dsp
---
How to compute convolution fast for real-time applications?

{% katexmm %}

## The Convolution Series
1. [Definition of convolution and intuition behind it]({% post_url 2020-06-20-the-secret-behind-filtering %})
1. [Mathematical properties of convolution]({% post_url 2020-07-05-mathematical-properties-of-convolution %})
1. [Convolution property of Fourier, Laplace, and z-transforms]({% post_url 2021-03-18-convolution-in-popular-transforms %})
1. [Identity element of the convolution]({% post_url 2021-04-01-identity-element-of-the-convolution %})
1. [Star notation of the convolution]({% post_url 2021-04-03-star-notation-of-the-convolution-a-notational-trap %})
1. [Circular vs. linear convolution]({% post_url 2021-05-07-circular-vs-linear-convolution %})
1. **Fast convolution**

{% capture _ %}{% increment equationId20210514  %}{% endcapture %}

# Introduction

Sound engineering and Virtual Reality audio demand real-time performance. Convolutions are inherently embedded in their inner workings, e.g., in the form of FIR-filtering for artificial reverberation. Convolution evaluated according to the definition is too slow to keep up and introduces latency. To mitigate this we reach for the **fast convolution** methods.

But speed itself is not enough. In the above-mentioned applications we need to process sound in a block-based fashion. They are called **partitioned convolution techniques**.

In this article, we first show why the naive approach to the convolution is inefficient, then show the FFT-based fast convolution. What follows is a description of two of the most popular block-based convolution methods: overlap-add and overlap-save. Finally, we outline the method of uniformly partitioned convolution and its application in real-time audio programming.

# Notation

In software, the signals are always of finite length. Thus, we will denote a signal $x[n]$ of length $N_x$ by a fixed-size vector $\pmb{x} = [x[0], x[1], \dots, x[N_x-1]]$.

# Naive implementation of convolution

We could implement the convolution between discrete-time signals $x$ and $h$ by implementing the definition directly [1]

$$ y[n] = x[n] \ast h[n] = \sum_{k=\max(0,n)}^{\min(n-N_h+1,N_x-1)} x[k] h[n - k], \\ \quad n \in \{0, \dots, N_x + N_h - 1\}. \quad ({% increment equationId20210514 %})$$

<!-- Check the k range in the above -->

{% highlight python %}



{% endhighlight %}

# Bibliography

[1] Frank Wefers *Partitioned convolution algorithms for real-time auralization*, PhD Thesis, Zugl.: Aachen, Techn. Hochsch., 2015.

{% endkatexmm %}
