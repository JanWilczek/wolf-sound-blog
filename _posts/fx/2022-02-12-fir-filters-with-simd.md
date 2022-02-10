---
title: "How To Write Fast FIR Filters with SIMD Instructions"
description: "Leverage Single Instruction, Multiple Data intrinsic functions of your processor for efficient filtering."
date: 2022-02-12
author: Jan Wilczek
layout: post
images: assets/img/posts/fx/2022-02-12-fir-filters-with-simd/
# background: /assets/img/posts/fx/2022-02-12-fir-filters-with-simd/Thumbnail.webp
categories:
  - Audio FX
  - Digital Signal Processing
tags:
  - effects
  - filtering
  - convolution
  - simd
  - C++
  - C
discussion_id: 2022-02-12-fir-filters-with-simd
---
Use vector intrinsics to perform efficient filtering.

Finite-impulse response (FIR) filtering is the cornerstone of digital signal processing. It is especially important in applying reverb to audio, for example, in virtual reality audio or in VST plugins of digital audio workstations. Lately, it has been extensively used on smartphones and embedded devices for sound applications. 

How to perform it fast?

{% katexmm %}
{% capture _ %}{% increment equationId20220212  %}{% endcapture %}

## What Are FIR Filters?

FIR filters are filters, who are defined by their finite-length impulse response, $h[n]$. The output $y[n]$ of an FIR filter is a [convolution]({% post_url 2020-06-20-the-secret-behind-filtering %}) of its input signal $x[n]$ with the impulse response. We can write it as

$$y[n] = x[n] \ast h[n] = \sum \limits_{k=-\infty}^{\infty} x[k] h[n - k].  \quad ({% increment equationId20220212 %})$$

I have published [a number of articles and videos on convolution]({% post_url 2020-06-20-the-secret-behind-filtering %}), which you can check out for more insight.

## 2 Sides of Optimization

In audio programming, we can speed up the software in two ways:

1. **algorithmically**, by choosing an algorithm with a better upper bound on the running time, or
2. **programatically**, by implementing the chosen algorithm in the most efficient way possible, often leveraging the resources of the hardware the software is running on.

## 2 Ways to Fast FIR Filters

Analogously, we can speed up FIR filtering

1. by using the [fast convolution]({% post_url 2021-05-14-fast-convolution %}) algorithm, or
2. by using the single instruction, multiple data (SIMD) instructions available on modern processors.

Sometimes, we simply cannot use fast convolution, because our filters are too short to benefit from the detour via the frequency domain. Therefore, time-domain convolution is incredibly often found in professional applications.

Therefore, for a well-rounded audio programmer, it is important to understand how to implement FIR filtering efficiently in time domain. Additionally, FIR filtering is a fun way to learn about SIMD: an incredibly important subject for programmers dealing with data.

And by the end of this article, you will understand it all 😎

## Why not GPU?

SIMD instructions are not limited to CPUs but are, in general, associated with them. We'll be considering only SIMD from CPUs in this article.

Someone could ask: why don't we use GPUs for FIR filtering?

Well, for the same reason that we don't use multithreading in audio processing code. Audio processing of a plugin/application must fit way below one block of audio (typically 10 milliseconds). Although multi-threaded processing on CPUs and GPUs can be very efficient, it is not predictable: we cannot determine when which resource will be available for processing. The cost of thread synchronization (implying system calls) would be too high. Additionally, transporting data to GPU and from it would incur even more overhead. That is why, in today's real-time audio processing applications single-core CPU processing prevails. The audio thread must never stop!

## What is SIMD?

* Link to the previous article

## How to Perform FIR Filtering with SIMD?

## The Anatomy of a FIR Filter

## Assumptions for Coding the Filter

## Plain C FIR Filter

## 3 Levels of FIR Code Optimization

1. Outer/Inner loop vectorization (VOL/VIL).
2. Outer-inner loop vectorization (VOIL).
3. Aligned data access.

## Inner Loop Vectorization



### Code

## Outer Loop Vectorization

### Code


## Outer-inner Loop Vectorization

## Aligned Data Access
## Bibliography

https://stackoverflow.com/questions/8456236/how-is-a-vectors-data-aligned

https://en.wikipedia.org/wiki/AVX-512




{% endkatexmm %}
