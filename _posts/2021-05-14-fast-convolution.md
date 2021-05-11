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

*An amazing source about fast convolution techniques is [1]. I highly encourage you to check it out. It's worth it!*

# Notation

In software, the signals are always of finite length. Thus, we will denote a signal $x[n]$ of length $N_x$ by a fixed-size vector $\pmb{x} = [x[0], x[1], \dots, x[N_x-1]]$.

# Naive implementation of convolution

We could implement the convolution between discrete-time signals $x$ and $h$ by implementing the definition directly [1]

$$ y[n] = x[n] \ast h[n] = \sum_{k=\max(0,n)}^{\min(n-N_h+1,N_x-1)} x[k] h[n - k], \\ \quad n \in \{0, \dots, N_x + N_h - 1\}. \quad ({% increment equationId20210514 %})$$

<!-- Check the k range in the above -->

{% highlight python %}
pass


{% endhighlight %}

# FFT-based implementation

As we know from the [article on circular convolution]({% post_url 2021-05-07-circular-vs-linear-convolution %}), mulitplication in the discrete-frequency domain is equivalent to circular convolution in the discrete-time domain. Element-wise multiplication of 2 vectors has time complexity $O(N)$. This is superior to $O(N^2)$ in case of the naive approach. The bottleneck of this approach is the transformation to the discrete-frequency domain, but it can be achieved in $O(N \log N)$ time, which is still better than $O(N^2)$. And so arises the FFT-based fast convolution (Figure 1).

![]({{ page.images | absolute_url | append: "/fft-based-fc.png" }}){: width="700" }
_Figure 1. FFT-based fast convolution. Source: [1]._

In order to make circular convolution correspond to linear convolution we need to pad the input signals with sufficiently many zeros so that the frequency-domain representation has enough capacity to represent the result of the linear convolution. This means, that each signal should be extended to have length $Nx + Nh - 1$. 

We can obtain it using function `pad_zeros_to()`.

{% highlight python %}
def pad_zeros_to(x, new_length):
    """Append new_length - x.shape[0] zeros to x's end via copy."""
    output = np.zeros((new_length,))
    output[:x.shape[0]] = x
    return output
{% endhighlight %}
_Listing 2._

If our signals are sufficiently long we can compute their discrete Fourier transforms (DFTs) using the Fast Fourier Transform (FFT) algorithm. Thanks to the FFT, the transformation from the time domain to the frequency domain can be computed in $O(N \log N)$ time.

In the frequency domain we can multiply our signals element-wise and then come back to the time domain via inverse FFT.

FFT is known to be most computationally efficient if the transformed signal's length is a power of 2. We can compute the exponent of the next largest power of 2 with respect to an integer $n > 0$ using the formula

$$ q_{\text{next}} = \log2(n - 1) + 1. \quad {% increment equationId20210514 %})$$

The above equation allows us to implement another helper function

{% highlight python %}
def next_power_of_2(n):
    return 1 << (int(np.log2(n - 1)) + 1)
{% endhighlight %}
_Listing 3._

Wrapping it all together

{% highlight python %}
def fft_convolution(x, h):
    Nx = x.shape[0]
    Nh = h.shape[0]
    Ny = Nx + Nh - 1

    K = next_power_of_2(Ny)

    X = np.fft.fft(pad_zeros_to(x, K))
    H = np.fft.fft(pad_zeros_to(h, K))

    Y = np.multiply(X, H)

    y = np.real(np.ifft(Y))

    return y[:Ny] # trim the signal to the expected length
{% endhighlight %}
_Listing 4. FFT-based fast convolution._

Remember that the above algorithm is fast *algorithmically*. I am not claiming this code is maximally optimized ;) It is provided for understanding and a possible baseline.

# Bibliography

[1] Frank Wefers *Partitioned convolution algorithms for real-time auralization*, PhD Thesis, Zugl.: Aachen, Techn. Hochsch., 2015.

{% endkatexmm %}
