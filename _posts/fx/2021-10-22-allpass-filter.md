---
title: "Allpass Filter: All You Need To Know"
description: "Condensed knowledge on the digital allpass filter: all necessary definitions, diagrams, equations, and applications clearly explained."
date: 2021-10-22
author: Jan Wilczek
layout: post
images: assets/img/posts/fx/2021-10-22-allpass-filter
categories:
  - Audio FX
  - Digital Signal Processing
tags:
  - effects
  - filters
discussion_id: 2021-10-22-allpass-filter
---
What is an allpass filter? What is it used for?

An *allpass filter* is a filter with a **unity gain across all frequencies**. This means that no frequency passing through that filter will be boosted or attenuated. It introduces, however, a *frequency-dependent delay*. 

So although the output of an allpass filter doesn't sound different from the input, this simple structure used in conjunction with other elements has an incredible power which is present in almost all music software.

Allpass filter can be implemented as finite impulse response (FIR) filters or infinite impulse response (IIR) filters, typically of first or second order. It applications are manifold: it used to implement

* reverb
* basic filters (highpass, lowpass, notch),
* audio effects (e.g., phaser),
* phase equalization, and more.

In this article, we will discuss the allpass filter in detail, present its various forms, provide their characteristics, schematics, and implementation, and, finally, discuss how you can use it in your musical software like VST plugins.

<div class="card summary" style="width: 36rem;">
  <div class="card-body">
  <h5 class="card-title">In Short</h5>
  <h6 class="card-subtitle mb-2 text-muted">Allpass Filter</h6>
    <ul>
    <li>Allpass filter has gain equal to 1 at all frequencies.</li>
    <li>It delays all frequency components of the input, each with by its own phase shift.</li>
    <li>It comes in various forms, but the most popular are first- and second-order IIR form.</li>
    <li>It is a building block of a huge number of audio processing algorithms, like reverb or EQ.</li>
    </ul>
  </div>
</div>
