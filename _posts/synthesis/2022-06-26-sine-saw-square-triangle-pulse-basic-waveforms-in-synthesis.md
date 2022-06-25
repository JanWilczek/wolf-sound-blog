---
title: "Sine, Saw, Square, Triangle, Pulse: Basic Waveforms in Synthesis and Their Properties"
description: "TODO"
date: 2022-06-26
author: Jan Wilczek
layout: post
images: /assets/img/posts/synthesis/2022-06-26-sine-saw-square-triangle-basic-waveforms-in-synthesis/
background: /assets/img/posts/synthesis/2022-06-26-sine-saw-square-triangle-basic-waveforms-in-synthesis/Thumbnail.webp
categories:
  - Sound Synthesis
tags:
  - sound wave
  - maths
  - waveform
discussion_id: 2022-06-26-sine-saw-square-triangle-basic-waveforms-in-synthesis
---
Read this to use their full potential and avoid any caveats!

{% katexmm %}
{% capture _ %}{% increment equationId20220626  %}{% endcapture %}

A **waveform** is a graphical representation of a wave.

Sound synthesis is based on 5 waveforms: sine, triangle, sawtooth (saw), pulse, square (which is a particular case of pulse).

To use them effectively is sound synthesis composition or audio programming, you need to know their basic properties:

* mathematical formula to generate them,
* time-domain visualization,
* amplitude spectrum: which harmonics are present and how their amplitude decays, and
* how they sound!

In this article, you will learn all these properties about the 5 basic waveforms.

*Note: this article shows the waveforms in their continuous (analog) form, which means that issues such as aliasing or efficient generation are not considered.*

### Jump to the Waveform of Choice

1. [Sine](#sine)
2. [Triangle](#triangle)
3. [Square](#square)
4. [Sawtooth (Saw)](#sawtooth-saw)
5. [Pulse](#pulse)

## Sine

A sine is the most basic of sound synthesis waveforms.

Its formula is simple:

$$s(t) = \sin (2 \pi f t), \quad ({% increment equationId20220626  %})$$

where $f$ is the frequency of the sine in Hz and $t$ is time in seconds.

* Sound example
* Formula
* Time-domain signal
* Amplitude spectrum
* Which harmonics are present and how their amplitude decays

## Triangle

## Square

## Sawtooth (Saw)

## Pulse
 
 - Mention the danger of DC component
## Summary


{% endkatexmm %}
