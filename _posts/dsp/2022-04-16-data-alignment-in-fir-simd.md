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

## Where is Data Alignment Present in FIR Filtering?

### Which Loop Vectorization Technique Can Benefit most From Data Alignment?

## Assumptions (Recap)

## Why Does Alignment Matter in SIMD?

## How to Align Data for FIR Filtering?

**Useful graphic**.

## Sample Code Aligning Data

## Summary

## Bibliography

