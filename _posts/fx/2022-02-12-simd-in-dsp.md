---
title: "What is SIMD in Digital Signal Processing?"
description: "Leverage intrinsic vector functions of your processor for efficient signal processing."
date: 2022-02-12
author: Jan Wilczek
layout: post
images: assets/img/posts/fx/2022-02-12-simd-in-dsp/
# background: /assets/img/posts/fx/2022-02-12-simd-in-dsp/Thumbnail.webp
categories:
  - Audio FX
  - Digital Signal Processing
tags:
  - simd
  - C++
  - C
discussion_id: 2022-02-12-simd-in-dsp
---
Speed up DSP operations with vector instructions.

<!-- TOC -->

## Introduction

Digital signal processing of images or sound requires complicated operations on large amounts of data. For example, to scale (change volume) a second of audio data, we may have to perform 44100 multiplications.

If we want to perform these operations in real time with less than 10 milliseconds reserved for an entire processing pipeline, things get even more difficult.

Thankfully, there are some programming tools that allow us handle these scenarios efficiently. One of them is SIMD, the topic of this article.

## What is SIMD?

Single instruction, multiple data (SIMD) are special processor instructions that perform some operation on more than 1 variable at a time.

In mathematical terms, we could say that SIMD operate on vectors ("arrays") of variables as "normal" code operates on single variables.

## SIMD Pseudocode Example

Imagine that we have two 8-element vectors (arrays), $\pmb{v}_1$ and $\pmb{v}_2$, both containing 32-bit floating-point variables,. Let's assume that $\pmb{v}_{12} = \pmb{v}_1 + \pmb{v}_2$.

To calculate $\pmb{v}_{12}$ in plain C code, we would need to write

```cpp
for (auto i = 0; i < 8; ++i)
    v12[i] = v1[i] + v2[i];
```

That means 8 additions, 8 "add" operations.

What if instead we could simply write

```cpp
v12 = vector8x32_add(v1, v2); // add eight 32-bit floats
```

which would result in 1 "add" operation?

In theory, such a program would be 8 times faster. And that's not actually far from the truth!

Whereas the speed-up in execution does not have to increase proportionally with the usage of multiple threads, SIMD often delivers speed-ups directly proportional to the number of variables that can fit into a data vector.

In AVX-512 instructions, one can operate on 16 `float`s with a single instruction. Can you imagine a 16-fold decrease in the processing time of your code?

And if we use 16-bit `int`egers, we optimistically get... That's right, a 32-fold speed-up.

That's the power of SIMD.

## How is SIMD Implemented?

* shipped with certain processors
* special instructions: each processor has their own
* usually compilers should be aware of them
* special registers

## What SIMD Instructions Are Available?

* add, multiply
* sometimes dedicated DSP operations
  
## How to Access SIMD Instructions?

* assembly
* intrinsic functions
  * Intel documentation link
  * ARM documentation link
* libraries, e.g., JUCE

## MMX, SSE, AVX, NEON...

## Which SIMD To Use?

* NEON2SSE

## The Disadvantages of SIMD


## Simple SIMD Code Example

## Summary

## Bibliography

https://stackoverflow.com/questions/8456236/how-is-a-vectors-data-aligned

https://en.wikipedia.org/wiki/AVX-512

