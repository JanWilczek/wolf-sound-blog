---
title: "Efficient FIR Filter Implementation with SIMD"
description: "Speed up time-domain filtering via vectorization for virtual reality, computer games, and digital audio workstation plugins."
date: 2022-03-28
author: Jan Wilczek
layout: post
images: assets/img/posts/dsp/2022-03-28-fir-with-simd/
# background: /assets/img/posts/dsp/2022-03-28-fir-with-simd/Thumbnail.webp
categories:
  - Digital Signal Processing
  - Audio FX
tags:
  - filtering 
  - effects
  - simd
  - C++
  - C
discussion_id: 2022-03-28-fir-with-simd
---
How to make your FIR filters fast in the time domain?

{% katexmm %}
{% capture _ %}{% increment equationId20220328  %}{% endcapture %}

If you want to make any software execute as fast as possible, there are two ways in which you can achieve this:

1. Optimal algorithm.
2. Efficient implementation.

The same principles apply to digital signal processing (DSP) code. To have a fast [finite-impulse response (FIR) filter]({% post_url 2020-06-20-the-secret-behind-filtering %}) in code, you can either

1. use an algorithm with a optimal lower bound on execution time, such as [fast convolution via the Fourier transform domain]({% post_url 2021-05-14-fast-convolution %}), or
2. take advantage of hardware and software resources to efficiently implement time-domain convolution. This typically means using the [single instruction, multiple data (SIMD) instructions]({% post_url fx/2022-02-12-simd-in-dsp %}) to vectorize your code.

<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6611455743195468"
     crossorigin="anonymous"></script><ins class="adsbygoogle"
     style="display:block; text-align:center;"
     data-ad-layout="in-article"
     data-ad-format="fluid"
     data-ad-client="ca-pub-6611455743195468"
     data-ad-slot="7289385396"></ins><script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>

## When Should We Use Time-Domain Filtering?

You may be asking yourself

> Since we have **fast** convolution, why would we ever need a time-domain implementation of it?

The fast convolution algorithm's lower bound on its execution time is of $O(N \log N)$ type, where $N$ could be the length of the input signal or the filter (let's not specify this exactly because it depends on the case). The lower bound on the linear convolution's execution time is of $O(N^2)$ type [Wefers2015].

First of all, it means that for sufficiently small $N$, the linear convolution algorithm will be faster than the fast convolution algorithm.

Second of all, if we vectorize our code wisely, we may be able to create an even larger advantage for the linear convolution. That is thanks to the fact, that fast convolution operates on complex numbers, whereas linear convolution always uses real numbers.

If that confuses you, think about sorting algorithms. In general, [Quicksort](https://en.wikipedia.org/wiki/Quicksort) is considered to be the fastest sorting algorithm. But if you look at sorting implementations, such as `std::sort`, you will see that after dividing the sorted container into sufficiently small parts, a quadratic algorithm, such as [insertion sort](https://en.wikipedia.org/wiki/Insertion_sort) is used to sort the elements within. (I've just found that this strategy is called [Introsort](https://en.wikipedia.org/wiki/Introsort) 😃).

With that explain, we can look into how to efficiently implement FIR filtering in the time domain.

## How to speed up FIR filter Implementation?

In short: via SIMD.

The best way to speed up filtering is to process multiple samples at once using single instruction, multiple data instructions. To achieve this, we need to rewrite the linear convolution algorithm so that it our code operates on vectors.

This process is called *loop vectorization*.

Loop vectorization is often done by the compiler but the degree of this vectorization is insufficient for real-time DSP. Instead, we need to instruct the compiler what to do.

SIMD instructions achieve the best performance when they operate on [aligned data]({% post_url 2020-04-09-what-is-data-alignment %}). Therefore, data alignment is another factor we should take into account.

In summary, an efficient FIR filter implementation uses 2 strategies in tandem:

1. Loop vectorization
2. Data alignment.

We will now discuss these two strategies in detail.

## Preliminary Assumptions

The [linear convolution formula]({% post_url 2020-06-20-the-secret-behind-filtering %}#definition) is

$$ x[n] \ast h[n] = \sum_{k=-\infty}^{\infty} x[k] h[n - k] = y[n], \quad n \in \mathbb{Z}. \quad ({% increment equationId20220328  %})$$

As you might guess, an infinite sum is not very practical. Additionally, reversing the time in the $h$ signal is quite problematic to think about in code. Therefore, we will make some assumptions, which, however, won't change the general nature of our discussion.

### Finite-Length Signals

We will assume that our signals are finite. This was of course true of $h$ but not necessarily of $x$.

We will denote $x$'s length by $N_x$ and $h$'s length by $N_h$.

### Time-Reversing the Filter Coefficients

In practical real-time audio scenarios, like virtual reality, computer games, or digital audio workstations, we know $h$ but don't know $x$.

Therefore, we can time-reverse $h$ right away and reason only about the reversed signal.

In other words, we define signal $c$ of length $N_h$

$$c[n] = h[N_h - n - 1], \quad n = 0, \dots, N_h - 1, \quad ({% increment equationId20220328  %}).$$

**We assume that $c$ is 0 everywhere else.**

### Practical Convolution Formula

After introducing these two assumptions, we can rewrite the convolution formula from Equation 1 into 

$$ y[n] = (x[n] \ast h[n])[n] \\= \sum_{k=0}^{N_h-1} x[n-N_h+1+k] c[k], \quad n = 0, \dots, N_x + N_h - 1. \quad ({% increment equationId20220328  %})$$

As you will see, this will simplify our discussion significantly.

## Naive Linear Convolution


## Loop vectorization

There are 3 types of loop vectorization in the context of FIR filtering:

1. Inner loop vectorization,
2. Outer loop vectorization,
3. Outer and inner loop vectorization.


## Inner loop vectorization

## Outer loop vectorization

## Outer and inner loop vectorization

## Data alignment

## Bibliography

{% endkatexmm %}
