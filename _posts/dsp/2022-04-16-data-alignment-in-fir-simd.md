---
title: "Data Alignment in FIR Filter SIMD Implementation"
description: "Learn how to align data in an FIR filter implementation with SIMD instructions."
date: 2022-04-16
author: Jan Wilczek
layout: post
images: /assets/img/posts/dsp/2022-04-16-data-alignment-in-fir-simd/
permalink: /data-alignment-in-fir-filter-simd-implementation/
# background: /assets/img/posts/dsp/2022-04-16-data-alignment-in-fir-simd/Thumbnail.webp
categories:
  - Digital Signal Processing
  - Audio FX
tags:
  - filtering 
  - effects
  - simd
  - convolution
  - C++
  - C
discussion_id: 2022-04-16-data-alignment-in-fir-simd
---
How to align data for optimum filtering?

In the [previous article], we discussed how to implement the finite impulse response (FIR) filter using single instruction, multiple data (SIMD) instructions. We used a technique called *loop vectorization* to speed up the computations.

Can we do even more?

Yes, we can!

In this article, you will learn **how to properly align your audio signal data for optimal FIR filtering with SIMD**.

## What is Data Alignment?

If we view the random-access memory (RAM) as consisting of boxes, we could say that the first memory address in each box is aligned with respect to the size of the box.

If we say that our data is aligned as 4 `float`s, we mean that the pointer to our data points to the first memory address in such a box.

C++ has a lot of features concerning alignment. Most notably, from C++ 17, standard containers like `std::array` or `std::vector` are always aligned according to the type they hold.

If you want to learn more about data alignment in general, I have a [dedicated article about it]({% post_url 2020-04-09-what-is-data-alignment %}). There I go into more detail and show concrete C++ features concerning alignment.

In this article, we focus on how to achieve optimal data alignment for FIR filtering.

### Which Loop Vectorization Techniques Can Benefit From Data Alignment?



## Assumptions (Recap)

## Why Does Alignment Matter in SIMD?

In FIR filters implementation with SIMD we are using the load/store instrinsic functions. The load functions move the data from plain C arrays (e.g., `float*`) to dedicated vector registers, which are identified by a type specific to the given SIMD instruction set, e.g., `m256` in the AVX instruction set. The store instructions transport the contents of the given SIMD register to the given C-style array. 

<!-- TODO: load/store infographic -->

These load/store instructions take pointers to C-style arrays. the data under these pointers can be aligned or not. If it is aligned, we can call the aligned version of the load/store instructions, which are typically faster than their unaligned counterparts. If the data under the pointer is not aligned or we don't know, we have to to use the unaligned instrinsic functions.

For example, in the AVX instrinsics, we have the `load` infix for the aligned load and the `loadu` infix for the unaligned load. Example intrinsic functions with these infixes are `_mm256_load_ps` and `_mm256_loadu_ps` respectively.

We strive to operate on aligned data to be able to use the potentially faster aligned load/store instructions.

## Where is Data Alignment Present in FIR Filtering?

In FIR filter implementations using SIMD, we move vectors of samples from the memory to the dedicated registers. We do this many times; if our input signal has length $N_x$, our impulse response has length $N_h$, and we operate on vectors of length 4, we load from memory around $N_x N_h / 4$ times in total and store into memory $(N_x + N_h - 1)/4$ times in total.

Imagine now that we can perform each of these operations a little bit faster. The potential gain can be significant.

But how to do it?

## How to Align Data for FIR Filtering?

Let's start with what is easy to align: the output. We can allocate our output vector as shown in Listing ???.

_Listing {% increment listingId20220416 %}. ._
```cpp
constexpr auto FLOATS_IN_SIMD_REGISTER = 4;
alignas(FLOATS_IN_SIMD_REGISTER * sizeof(float)) float output[outputLength];

// Example: AVX
alignas(m256) float output[outputLength];

// Since C++ 17
std::vector<m256> output(outputLength);
```



**Useful graphic**.

## Sample Code Aligning Data

## Summary

## Bibliography

