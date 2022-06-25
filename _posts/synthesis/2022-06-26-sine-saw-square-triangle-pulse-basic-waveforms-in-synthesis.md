---
title: "Sine, Saw, Square, Triangle, Pulse: Basic Waveforms in Synthesis and Their Properties"
description: "TODO"
date: 2022-06-26
author: Jan Wilczek
layout: post
images: /assets/img/posts/synthesis/2022-06-26-sine-saw-square-triangle-basic-waveforms-in-synthesis/
# background: /assets/img/posts/synthesis/2022-06-26-sine-saw-square-triangle-basic-waveforms-in-synthesis/Thumbnail.webp
audio_examples: /assets/wav/posts/synthesis/2022-06-26-sine-saw-square-triangle-basic-waveforms-in-synthesis/
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
{% capture _ %}{% increment figureId20220626  %}{% endcapture %}

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

Sine formula is simple:

$$s(t) = \sin (2 \pi f t), \quad ({% increment equationId20220626  %})$$

where $f$ is the frequency of the sine in Hz and $t$ is time in seconds.

A sine at 220 Hz sounds like this:

{% include embed-audio.html src="/assets/wav/posts/synthesis/2022-06-26-sine-saw-square-triangle-basic-waveforms-in-synthesis/sine_example.flac" %}

The time-domain representation (waveform) of the sine looks like this:

![]({{ page.images | absolute_url | append: "/sine_signal.webp" }}){: alt="The sine waveform" }
_Figure {% increment figureId20220626  %}. Sine waveform: time-domain representation of the sine wave._

The amplitude spectrum of a sine is very boring because it consists of just one partial: the fundamental frequency.

![]({{ page.images | absolute_url | append: "/sine_harmonics.webp" }}){: alt="Amplitude spectrum of a sine" }
_Figure {% increment figureId20220626  %}. Amplitude spectrum of a sine._

As you can see, it has only one harmonic. That makes sense because spectrum calculation assumes that the analyzed signal is a superposition (a sum) of sines. And one sine consists of just... one sine 🙃


## Triangle

A triangle is just a little bit more complicated than the sine.

The triangle formula is as follows [Wikipedia]:

$$s(t) = 4 | ft - \lfloor ft + \frac{1}{2} \rfloor | - 1, \quad ({% increment equationId20220626  %})$$

where $f$ is the triangle's frequency in Hz and $t$ is time in seconds.

A triangle wave at 220 Hz sounds like this:

{% include embed-audio.html src="/assets/wav/posts/synthesis/2022-06-26-sine-saw-square-triangle-basic-waveforms-in-synthesis/triangle_example.flac" %}

As you can hear, it's a bit brighter than sine.

The triangle waveform in the time-domain looks as follows.

![]({{ page.images | absolute_url | append: "/triangle_signal.webp" }}){: alt="The triangle waveform" }
_Figure {% increment figureId20220626  %}. Triangle waveform: time-domain representation of the triangle wave._

The plot in Figure 3 indeed looks like a triangle.

This makes the formula from Equation 2 more intuitive: a triangle waveform is in essence, the difference between a linear function and a shifted step function. This difference grows and shrinks piecewise linearly and so we obtain a triangle.

The amplitude spectrum of the triangle waveform contains only odd harmonics (Figure 4).

![]({{ page.images | absolute_url | append: "/triangle_harmonics.webp" }}){: alt="Amplitude spectrum of a triangle" }
_Figure {% increment figureId20220626  %}. Amplitude spectrum of a triangle._

The amplitudes of the harmonics decay as $\frac{1}{n^2}$, where $n$ is the harmonic's index (the fundamental has $n=1$, the first overtone has $n=2$, and so on).

## Square

The square wave is more interesting than the sine or the triangle because of its characteristic, "empty" timbre.

The square wave at 220 Hz sounds like this:

{% include embed-audio.html src="/assets/wav/posts/synthesis/2022-06-26-sine-saw-square-triangle-basic-waveforms-in-synthesis/square_example.flac" %}

For me, the simplest formula for the square waveform is just taking the sign of the sine:

$$s(t) = \text{sgn} (\sin (2 \pi f t)), \quad ({% increment equationId20220626  %})$$

where $f$ is the square's frequency in Hz and $t$ is time in seconds.

Of course, alternative formulas are possible, like ones using the modulo operation.

The square waveform in the time-domain has a rectangular shape (Figure 5).

![]({{ page.images | absolute_url | append: "/square_signal.webp" }}){: alt="The square waveform" }
_Figure {% increment figureId20220626  %}. Square waveform: time-domain representation of the square wave._

The amplitude spectrum of the square wave consists of only odd harmonics, exactly as was the case for the triangle (Figure 6).

![]({{ page.images | absolute_url | append: "/square_harmonics.webp" }}){: alt="Amplitude spectrum of a square" }
_Figure {% increment figureId20220626  %}. Amplitude spectrum of a square._

The amplitudes of square's harmonics decay slower than in the case of the triangle: they decay as $\frac{1}{n}$, where $n$ is the harmonic's index ($n=1$ corresponds to the fundamental).

## Sawtooth (Saw)

The sawtooth (or simply "saw") waveform is my favorite waveform, thanks to its rich, "fat" sound that plays incredibly well with a good low-pass filter.

The sawtooth wave atr 220 Hz sounds like this:

{% include embed-audio.html src="/assets/wav/posts/synthesis/2022-06-26-sine-saw-square-triangle-basic-waveforms-in-synthesis/sawtooth_example.flac" %}

Ah, that's so beautiful ❤️

The simplest formula for the sawtooth wave is a modulo approach:

$$s(t) = 2 (ft \% \frac{1}{f}) f - 1, \quad ({% increment equationId202206026 %})$$

where $f$ is the sawtooth's frequency in Hz and $t$ is time in seconds.

* Sound example
* Formula
* Time-domain signal
* Amplitude spectrum
* Which harmonics are present and how their amplitude decays

## Pulse
 
 * Sound example
* Formula
* Time-domain signal
* Amplitude spectrum
* Which harmonics are present and how their amplitude decays
 - Mention the danger of DC component

## Summary

* Link to the checklist

## Bibliography

[Pluta]

[Valimaki]

[Wikipedia]

{% endkatexmm %}
