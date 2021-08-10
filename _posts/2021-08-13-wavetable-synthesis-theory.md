---
title: "Wavetable Synthesis Algorithm Explained"
description: Wavetable is a synthesis technique that loops over a waveform stored in a memory array according to the desired frequency and sampling rate.
date: 2021-08-13
author: Jan Wilczek
layout: post
permalink: /wavetable-synthesis-algorithm/
images: assets/img/posts/2021-08-13-wavetable-synthesis-theory
background: /assets/img/posts/2021-08-13-wavetable-synthesis-theory/Thumbnail.png
categories:
 - Sound Synthesis
tags:
 - synthesis
 - wavetable
 - waveform
discussion_id: 2021-08-13-wavetable-synthesis-theory
---
How to generate sound in code using the wavetable synthesis technique?

{% katexmm %}

{% capture _ %}{% increment equationId20210813 %}{% endcapture %}

In this article, you will learn:
 * how to generate sound using wavetables
 * step-by-step synthesis algorithm
 * what are pros and cons of wavetable synthesis
 * how is wavetable synthesis related to other synthesis methods

In the follow-up articles, an implementation of this technique in the Python programming language and the JUCE framework will follow.

# A Need for a Fast and Efficient Synthesis Method

*Computer-based sound synthesis is the art of generating sound through software.*

In the early days of digital sound synthesis the sound was also synthesised using specialized digital signal processing hardware but the underlying principles and algorithms remained the same. To obtain real-time performance capabilities with that technology, there was a great need to generate sound efficiently in terms of memory and processing speed. Thus, the wavetable technique was convceived: it is both fast and memory-inexpensive.

# From Gesture to Sound

The process of generating sound begins with a *musician*'s *gesture*. Let's put aside who a musician might be or what kind of gestures they perform. For the purpose of this article, a gesture could be as simple as pressing a key on a MIDI keyboard, clicking on a virtual keybord's key, or pressing a button on any controller device.

<!-- TODO: Add gesture to sound schematic -->

A gesture provides *control information*. In the case of pressing a MIDI note-on event, control information would incorporate information on which key was pressed and how fast was it pressed (*velocity* of a keystroke). We can change the note number information into frequency $f$ and the velocity information into amplitude $A$. This information is sufficient to generate sound using most of the popular synthesis algorithms.

# Sine Generator

Let's imagine that given frequency and amplitude information we want to generate a sine wave. The general formula of a sine waveform is

$$s(t) = A \sin (2 \pi f t + \phi), \quad ({% increment equationId20210813 %})$$

where $f$ is the frequency in Hz, $A$ is the amplitude in range $[0, 1]$, $t$ is time in seconds, and $\phi$ is the initial phase, which we will ignore for now (i.e., assume that $\phi=0$).

As we discussed in the [digital audio basics article]({% post_url 2019-11-12-what-is-sound-the-notion-of-an-audio-signal %}), digital audio operates using samples rather than physical time. The $n$-th sample occurs at time $t$ when

$$n = f_s t, \quad ({% increment equationId20210813 %})$$

where $f_s$ is the sampling rate, i.e., the number of samples per second that the system (software or hardware) produces.

After inserting Equation 2 into Equation 1, we obtain the formula for a digital sine wave

$$s[n] = A \sin (2 \pi f f_s n), \quad ({% increment equationId20210813 %})$$

How to compute the $\sin$ in the above formula? In programming languages (and any calculators for that matter), we often have a `sin()` function, but how does it compute its return value?

`sin()` calls use *Taylor expansion* of the sine function [1]

$$\sin(x) = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} \dots \quad ({% increment equationId20210813 %})$$

Above expansion is infinite, so on real-world hardware, it needs to be truncated at some point (after obtaining sufficient accuracy). Its advantage is, that it uses operations realizable in hardware (multiplication, division, addition, subtraction). Its disadvantage is that it involves **a lot** of these operations. If we need to produce 44100 samples per second and want to play a few hundred sines simultaneously (what is typical of additive synthesis), we need to be able to compute the $\sin$ function more efficiently.

# Bibliography

[1] [Taylor series expansion of the sine function on MIT Open CourseWare](https://ocw.mit.edu/courses/mathematics/18-01sc-single-variable-calculus-fall-2010/unit-5-exploring-the-infinite/part-b-taylor-series/session-99-taylors-series-continued/MIT18_01SCF10_Ses99c.pdf)

{% endkatexmm %}

