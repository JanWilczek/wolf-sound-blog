---
title: "How To Digitize an Analog Filter with the Bilinear Transform"
description: "Learn how to derive and use the bilinear transform to convert analog systems into digital ones."
date: 2022-01-15
author: Jan Wilczek
layout: post
images: assets/img/posts/fx/2022-01-15-bilinear-transform/
# background: /assets/img/posts/fx/2022-01-15-bilinear-transform/Thumbnail.webp
categories:
  - Audio FX
  - Digital Signal Processing
tags:
  - effects
  - filtering
discussion_id: 2022-01-15-bilinear-transform
---
Learn how to derive and use the bilinear transform to convert analog systems into digital ones.

To design and implement a parametric filter, [4 steps are needed]({% post_url fx/2021-11-26-parametric-eq-design %}):

1.	[Decide on the filter type you want to implement.]({% post_url fx/2021-11-26-parametric-eq-design %}#step-1-decide-on-the-filter-type)
2.	[Design an analog prototype.]({% post_url fx/2021-12-03-analog-prototype %})
3.	Digitize the analog prototype using the bilinear transform.
4.	Implement the digital filter in code.

In this article, we'll explain the second step of that process: how to go from an analog prototype to a digital form of the parametric filter.

## System Digitization Methods

<!-- Different transforms -->
* impulse-invariant transformation
* bilinear transformation

## The Bilinear Transform

<!-- numerator and denominator are linear in z -->
<!-- mapping of poles and zeros? -->
<!-- stable analog filters are stable digital filters -->
<!-- same filter order of the prototype and digital filter -->
<!-- optimality is preserved -->
<!-- cascade of a transformed sections is equivalent to a transform of a cascade of sections -->
## Frequency Warping

<!-- Add a visualization of the frequency warping with marks -->

## Derivation

<!--  Something about the allpass filter? -->

## Example: Digitization of the Butterworth Low-Pass

