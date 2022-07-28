---
title: "Sine, Saw, Square, Triangle, Pulse: Basic Waveforms in Synthesis and Their Properties"
description: "Learn the properties of 5 basic waveforms in sound synthesis to use their full potential in your synthesizer performance or design."
date: 2022-06-26
author: Jan Wilczek
layout: post
images: /assets/img/posts/synthesis/2022-06-26-sine-saw-square-triangle-basic-waveforms-in-synthesis
background: /assets/img/posts/synthesis/2022-06-26-sine-saw-square-triangle-basic-waveforms-in-synthesis/sawtooth_signal.webp
audio_examples: /assets/wav/posts/synthesis/2022-06-26-sine-saw-square-triangle-basic-waveforms-in-synthesis/
categories:
  - Sound Synthesis
tags:
  - sound wave
  - maths
  - waveform
discussion_id: 2022-06-26-sine-saw-square-triangle-basic-waveforms-in-synthesis
custom_js:
 - /assets/vendor/lazyload/lazyload.min.js
 - /assets/js/wolfsound/modules/load_lazyload.js
---
Read this to use their full potential and avoid any caveats!

<iframe width="560" height="315" src="https://www.youtube.com/embed/7E8Ou6DYsJQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

{% katexmm %}
{% capture _ %}{% increment equationId20220626  %}{% endcapture %}
{% capture _ %}{% increment figureId20220626  %}{% endcapture %}

A **waveform** is a graphical representation of a wave.

Sound synthesis is based on 5 waveforms: the sine, the triangle, the sawtooth (saw), the pulse, and the square (which is a particular case of the pulse).

To use them effectively in sound synthesis compositions or audio programming, you need to know their basic properties:

* mathematical formula to generate it,
* time-domain visualization,
* amplitude spectrum: which harmonics are present and how their amplitudes decay, and
* how it sounds!

In this article, you will learn all these properties about the 5 basic waveforms.

*Note: this article shows the waveforms in their continuous (analog) form, which means that issues such as aliasing or efficient generation are not considered. Keep in mind that all of these waveforms (apart from the sine) have an infinite amplitude spectrum.*

<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6611455743195468"
     crossorigin="anonymous"></script><ins class="adsbygoogle"
     style="display:block; text-align:center;"
     data-ad-layout="in-article"
     data-ad-format="fluid"
     data-ad-client="ca-pub-6611455743195468"
     data-ad-slot="7289385396"></ins><script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>

## Why Learn About Basic Waveforms?

Learning about basic waveforms in sound synthesis will help you

* exploit the capabilities of modern synthesizers,
* achieve the desired timbre even during live performances,
* understand the behavior of oscillators (often marked as VCO, voltage-controlled oscillator) and modulators (often marked as LFO, low-frequency oscillator),
* employ these waveforms in mathematical derivations of analysis, synthesis, and audio effects,
* write efficient code to generate these waveforms for sound synthesis and audio effects algorithms,
* detect any inconsistencies in these signals in a system,
* avoid potential issues with aliasing, and
* discover where aliasing may come from (e.g., from an unbounded spectrum).

## The Waveforms


### Jump to the Waveform of Choice

1. [Sine](#sine)
2. [Triangle](#triangle)
3. [Square](#square)
4. [Sawtooth (Saw)](#sawtooth-saw)
5. [Pulse](#pulse)

## Sine

The **sine** is the most basic of sound synthesis waveforms.

The sine formula is simple

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

A **triangle** is just a little bit more complicated than the sine.

The triangle formula is [Wikipedia]

$$s(t) = 4 \left| ft - \left\lfloor ft + \frac{1}{2} \right\rfloor \right| - 1, \quad ({% increment equationId20220626  %})$$

where $f$ is the triangle's frequency in Hz and $t$ is time in seconds.

A triangle wave at 220 Hz sounds like this:

{% include embed-audio.html src="/assets/wav/posts/synthesis/2022-06-26-sine-saw-square-triangle-basic-waveforms-in-synthesis/triangle_example.flac" %}

As you can hear, it's a bit brighter than the sine.

The triangle waveform in the time-domain looks as follows.

![]({{ page.images | absolute_url | append: "/triangle_signal.webp" }}){: alt="The triangle waveform" }
_Figure {% increment figureId20220626  %}. Triangle waveform: time-domain representation of the triangle wave._

The plot in Figure 3 indeed looks like a triangle.

This makes the formula from Equation 2 more intuitive: a triangle waveform is, in essence, the difference between a linear function and a shifted step function. This difference increases and decreases piecewise linearly and so we obtain a triangle.

The amplitude spectrum of the triangle waveform contains only odd harmonics (Figure 4).

![]({{ page.images | absolute_url | append: "/triangle_harmonics.webp" }}){: alt="Amplitude spectrum of a triangle" }
_Figure {% increment figureId20220626  %}. Amplitude spectrum of a triangle._

The amplitudes of the harmonics decay as $\frac{1}{n^2}$, where $n$ is the harmonic's index (the fundamental has $n=1$, the first overtone has $n=2$, and so on).

## Square

The **square wave** is more interesting than the sine or the triangle because of its characteristic, "empty" timbre.

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

The **sawtooth** (or simply **"saw"**) waveform is my favorite waveform, thanks to its rich, "fat" sound that plays incredibly well with a good low-pass filter.

The sawtooth wave at 220 Hz sounds like this:

{% include embed-audio.html src="/assets/wav/posts/synthesis/2022-06-26-sine-saw-square-triangle-basic-waveforms-in-synthesis/sawtooth_example.flac" %}

Ah, that's so beautiful ❤️

The simplest formula for the sawtooth wave is a modulo approach:

$$s(t) = 2 \left( ft \% \frac{1}{f} \right) f - 1, \quad ({% increment equationId202206026 %})$$

where $f$ is the sawtooth's frequency in Hz, $t$ is time in seconds, and $\%$ is the modulo operator applied to real values.

The formula reads, "increase the value linearly ($ft$), jump back to 0 every period ($\% \frac{1}{f}$), scale to the $[0, 1]$ range (multiplication by $f$), and then expand the range from $[0, 1]$ to $[-1, 1]$ (multiplication by $2$ and subtraction of $1$)."

The sawtooth waveform in the time domain is shown in Figure 7.

![]({{ page.images | absolute_url | append: "/sawtooth_signal.webp" }}){: alt="The sawtooth waveform" }
_Figure {% increment figureId20220626  %}. Sawtooth waveform: time-domain representation of the sawtooth wave._

This is the so-called **ramp-up** sawtooth because its slope is rising within each period. Should it be falling, it would be called **ramp-down** sawtooth. Since it's just a matter of phase inversion, ramp-up and ramp-down variants have the same properties. The slope matters the most when we use the sawtooth waveform to modulate some other parameter, i.e., when we use the sawtooth in a low-frequency oscillator (LFO). Then we can create a periodically rising sensation (ramp-up) or periodically falling (ramp-down).

The name "saw" comes from the teeth-like shape of the waveform.

The amplitude spectrum of the sawtooth can be seen in Figure 8.

![]({{ page.images | absolute_url | append: "/sawtooth_harmonics.webp" }}){: alt="Amplitude spectrum of a sawtooth" }
_Figure {% increment figureId20220626  %}. Amplitude spectrum of a sawtooth._

The spectrum of the sawtooth waveform contains odd and even harmonics. The amplitudes of sawtooth's harmonics decay as $\frac{1}{n}$, where $n$ is the harmonic's index ($n=1$ corresponds to the fundamental frequency).

## Pulse
 
The **pulse waveform** (also called a **pulse train**) is a generalization of the square waveform.

An example pulse waveform in the time domain is shown in Figure 9.

![]({{ page.images | absolute_url | append: "/pulse_signal.webp" }}){: alt="The pulse waveform" }
_Figure {% increment figureId20220626  %}. Pulse waveform: time-domain representation of the pulse wave with 20% duty cycle._

This waveform's **duty cycle** is 20%. It means that for 20% of its period, the value is 1. For the remaining 80%, the value is -1.

Duty cycle specifies for which fraction of the period the value of the waveform is 1.

For $D=0.5$, we obtain the square waveform.

The pulse waveform with 20% duty cycle at 220 Hz sounds like this:

{% include embed-audio.html src="/assets/wav/posts/synthesis/2022-06-26-sine-saw-square-triangle-basic-waveforms-in-synthesis/pulse_example.flac" %}

The pulse wave could be generated in various ways. I used a Fourier series-based formula [Pluta2019]

$$s(t) = (2D - 1) + \sum_{k=1}^{\infty} \frac{4}{k\pi} \sin (\pi k D) \cos (2 \pi k f_0 t - \pi k D), {% increment figureId20220626  %}$$

where $D$ is the duty cycle, $k$ is the harmonic's index, $f_0$ is the fundamental frequency in Hz, and $t$ is time in seconds.

The amplitude spectrum of the pulse wave for $D=0.2$ case is shown in Figure 10.

![]({{ page.images | absolute_url | append: "/pulse_harmonics.webp" }}){: alt="Amplitude spectrum of a pulse wave" }
_Figure {% increment figureId20220626  %}. Amplitude spectrum of a pulse wave with 20% duty cycle._

However, the amplitude spectrum changes dynamically with the duty cycle. I have visualized it on Figure 11.

<div markdown="0">
<img class="lazyload" src="{{ page.images | absolute_url | append: "/duty_cycle_visualization_placeholder.webp" }}" data-src="{{ page.images | absolute_url | append: "/duty_cycle_visualization.gif" }}" alt="Visualization of the duty cycle influence on the pulse wave">
</div>

_Figure {% increment figureId20220626  %}. Time-domain waveform and the amplitude spectrum of a pulse wave for different values of the duty cycle._

As you can see in the figure, for duty cycle equal to 50% we get the square wave and its odd-harmonics-only amplitude spectrum.

The first dip from the left in the amplitude spectrum is determined by the duty cycle: the dip occurs at the $D^{-1}$-th harmonic.

For example, for the square wave, $D=0.5$ so the first dip occurs at the $\left(\frac{1}{2}\right)^{-1} = 2$-nd harmonic.

In the figure, you can also see a small glitch around the DC (0 Hz) frequency. That is because for very high or very low values of the duty cycle, the DC component is pretty significant (the mean of the waveform's values is significantly nonzero). I have deliberately hidden the DC component from the plots for clarity but some of it is still present because of the [spectral leakage](https://en.wikipedia.org/wiki/Spectral_leakage).

The DC component must be kept in mind in musical applications because it adds no musical information (we cannot hear it) but it can damage the hardware that it runs through.

## Summary

In this article, you learned everything about the basic waveforms (sine, triangle, square, saw, pulse) that you need for sound synthesis. Being familiar with these waveforms will help you in exploiting synthesizers' capabilities and coding your own.

These waveforms are one piece of the puzzle when it comes to developing your own software sound synthesizers. If you want to know what other information is necessary to develop audio plugins, [download my free Ultimate Audio Plugin Developer Checklist]({% link single-pages/checklist.html %}).

## Bibliography

[Pluta2019] Marek Pluta, _Sound Synthesis for Music Reproduction and Performance_, monograph, AGH University of Science and Technology Press, Kraków 2019.

[VälimäkiHuovilainen2006] Vesa Välimäki and Antti Huovilainen, _Oscillator and Filter Algorithms for Virtual Analog Synthesis_, Computer Music Journal, 30:2, pp. 19–31, Summer 2006. [PDF](https://www.researchgate.net/publication/220386519_Oscillator_and_Filter_Algorithms_for_Virtual_Analog_Synthesis)

[Wikipedia] [Triangle wave on Wikipedia](https://en.wikipedia.org/wiki/Triangle_wave). Access: 28.06.2022.

{% endkatexmm %}
