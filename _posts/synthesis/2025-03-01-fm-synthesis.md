---
title: "FM Synthesis Explained For Audio Programmers: Art and Science"
description: "Frequency modulation synthesis explained for audio programmers: a single all-in-one resource"
date: 2025-03-07
author: Jan Wilczek
layout: post
permalink: /fm-synthesis-explained-for-audio-programmers-art-and-science/
background: /assets/img/posts/synthesis/2025-03-01-fm-synthesis/Thumbnail.webp
categories:
  - Sound Synthesis
tags:
  - sound wave
  - waveform
  - maths
  - audio generation
discussion_id: 2025-03-01-fm-synthesis
---
Frequency modulation (FM) synthesis is an exciting topic: with a few simple operations, we can create complex sounds that can instantaneously change in timbre with a few simple coefficient changes.

How does it work? How to control it to produce musical notes? Why was it so popular in the 1980s? We will explore all that in this single article!

{% capture _ %}{% increment figureId20250301  %}{% endcapture %}

1. [Source code of figures and audio examples](#source-code-of-figures-and-audio-examples)
2. [History](#history)
3. [Vibrato](#vibrato)
4. [Basic FM Synth](#basic-fm-synth)
   1. [Proper FM Formula](#proper-fm-formula)
   2. [Simple FM Diagram](#simple-fm-diagram)
5. [Simple FM Spectrum](#simple-fm-spectrum)
   1. [Partials vs harmonics vs overtones](#partials-vs-harmonics-vs-overtones)
6. [Timbre control of simple FM](#timbre-control-of-simple-fm)
7. [Modulation Index](#modulation-index)
8. [Phase Modulation](#phase-modulation)
9. [How to control the timbre of FM?](#how-to-control-the-timbre-of-fm)
   1. [When is FM spectrum harmonic?](#when-is-fm-spectrum-harmonic)
   2. [What’s the fundamental frequency (the pitch) in FM?](#what-s-the-fundamental-frequency-the-pitch-in-fm)
   3. [How to eliminate every $N\_2$-th harmonic?](#how-to-eliminate-every-th-harmonic)
   4. [How to control the brightness of FM spectra?](#how-to-control-the-brightness-of-fm-spectra)
   5. [FM Efficiency](#fm-efficiency)
   6. [How to control the partials’ amplitudes? Bessel functions](#how-to-control-the-partials-amplitudes-bessel-functions)
10. [Extensions of simple FM](#extensions-of-simple-fm)
11. [Summary](#summary)
12. [Bibliography](#bibliography)

{% render 'google-ad.liquid' %}

## Source code of figures and audio examples

All figures and audio examples in this article were generated using [the following Python script](https://github.com/JanWilczek/wolf-sound-blog/blob/master/_py/posts/synthesis/2025-03-01-fm-synthesis/fm_synthesis.py). Feel free to use and tweak it to your needs!

## History

Just as a brief word of history, to give credit to people's hard work, the original publication on FM synthesis came from John Chowning  in 1973 [Chowning1973]. Because of the lack of interest of American manufacturers in using the technique in hardware synths, Chowning turned to Japan-based manufacturer Yamaha in the same year. [SOS2000]

{% image "assets/img/posts/synthesis/2025-03-01-fm-synthesis/Chowning.jpg", "John Chowning" %}
_Figure {% increment figureId20250301  %}. John Chowning. [Source](https://commons.wikimedia.org/wiki/File:Chowning.jpg), accessed March 5, 2025, licensed under the [Creative Commons Attribution-Share Alike 3.0 Unported license](https://creativecommons.org/licenses/by-sa/3.0/deed.en)._

However, it wasn't until 1983, when the first widely successful FM synth was introduced, namely, Yamaha DX7 [Wikipedia]. It took the market by storm and spawned a host of FM-based hardware synths.

That 10-year gap should tell you how much engineering effort was required to make FM commercially usable!

## Vibrato

Before we delve into the frequency modulation synthesis, we should consider what is vibrato.

**Vibrato** is an effect of a sound varying up and down in pitch. In other words, vibrato is a periodical pitch variation [Zölzer2011].

In this sense, we **modulate** the pitch. To achieve the vibrato, the modulation must be quite slow: in the range of 5-14 Hz [Zölzer2011]. Note that this range is below the human hearing range, which is typically associated with the 20-20 000 Hz range.

Here’s how a single musical note (a sine representing the MIDI note 57) sounds without the vibrato.

{% render 'embed-audio.html', src: "/assets/wav/posts/synthesis/2025-03-01-fm-synthesis/plain_note_220Hz.flac" %}

Here’s how the same note sounds when we apply a 6 Hz vibrato to it with a modulation index 2 (which means that the pitch should change by +/- 12 Hz).

{% render 'embed-audio.html', src: "/assets/wav/posts/synthesis/2025-03-01-fm-synthesis/pm_vibrato_note_220Hz.flac" %}

It turns out that if we increase the vibrato frequency and the range over which we change the pitch, we stop hearing a variation in pitch and start hearing a completely different timbre. That is the basis of frequency modulation synthesis.

## Basic FM Synth

Let’s now consider a basic frequency modulation instrument.

In FM, we **modulate the frequency** of a carrier waveform. It means that the **instantaneous frequency** of the waveform (waveform's frequency at a particular time instant) is constantly being changed by a **modulator** (another waveform) in a regular, periodic fashion.

In the simplest FM setup, a sine modulator modulates a sine carrier. In this scenario, the output signal's instantaneous frequency $f(t)$ (which is a function of time) is given by the following formula [Pluta2019]

$$
\begin{equation}
f(t) = f_C + A_M\cos(2\pi f_M t),
\end{equation}
$$

where

- $f_C$ is the frequency of the carrier in Hz, the **carrier frequency**,
- $A_M$ is the amplitude of the modulator (unitless),
- $\cos$ is the cosine function,
- $f_M$ is the frequency of the modulator in Hz, the **modulation frequency**, and
- $t$ is time in seconds.

To create a sine oscillator whose frequency changes according to Equation 1, we cannot simply put it into the sine formula like this

$$
\begin{equation}
\begin{aligned}
s_\text{FM}(t) &\neq A_C \sin\left(2 \pi f(t) t\right),\\
s_\text{FM}(t) &\neq A_C \sin\left(2 \pi (f_C + A_M \cos(2 \pi f_M t))t\right),
\end{aligned}
\end{equation}
$$

because it’s not mathematically correct. Here, $A_C$ stands for the **carrier amplitude**.

If we would apply the thing in "Equation" 2 to generate a signal where $A_C = 1, f_C=220 \text{ Hz}, f_M=110 \text{ Hz},$ and $A_M = 220$, then we would get a signal that sounds like this.

{% render 'embed-audio.html', src: "/assets/wav/posts/synthesis/2025-03-01-fm-synthesis/wrong_fm_220Hz.flac" %}

Instead, we need to use the fact that **angular frequency is the derivative of phase** [Farina2000]. Mathematically speaking,

$$
\begin{equation}
2\pi f(t) = \frac{d \phi(t)}{dt},
\end{equation}
$$

where

- $2 \pi f(t)$ is the instantaneous angular frequency in radians per sample,
- $\phi(t)$ denotes the instantaneous phase (phase at time instant $t$), and
- $\frac{d}{dt}$ denotes the derivative of a function over time.

*Note: if you don’t know what a derivative is, it is a measure of how much a given function changes at every point in time. The derivative is also a function. If you think about Equation 3, it makes total sense: if the phase changes rapidly, the derivative is large, and the frequency is high; if the phase changes slowly, the derivative is small, and the frequency is low.*

The argument of a sine is the phase NOT the frequency. In order to obtain the phase from the equation for frequency (Equation 3), we must perform an operation that is inverse to derivation, namely, integration.

$$
\begin{equation}
\phi(t) = \int \limits_0^t 2\pi f(\tau)d\tau = 2 \pi \int \limits_0^t (f_C + A_M \cos(2 \pi f_M \tau))d\tau.
\end{equation}
$$

*Note: Want to understand the mathematics of DSP? Check out [my online course on digital audio signal processing for beginners]({{ site.dsp_pro_url }})!*

### Proper FM Formula

Now, we can plug the formula for the phase (Equation 4) as the argument of a sine function.

$$
\begin{equation}
\begin{aligned}
s_\text{FM}(t) &= A_C \sin(\phi(t)) =\\&= A_C \sin\left(2 \pi \int \limits_0^t (f_C + A_M \cos(2 \pi f_M \tau))d\tau\right).
\end{aligned}
\end{equation}
$$

**This is the correct formula for a simple FM instrument;** we have a sine carrier with amplitude $A_C$ and frequency $f_C$ and a sine modulator (represented by the cosine) with amplitude $A_M$ and frequency $f_M$. Note that we need to use a different symbol for time than $t$ in the integral because $t$ denotes the time point at which we compute the phase; I chose $\tau$ (tau).

### Simple FM Diagram

FM variants are most often explained on the basis of diagrams. The diagrams can easily show how the interconnection between the oscillators are placed much like in graphical audio programming languages like Max/MSP or PureData.

Here is the diagram of a simple FM instrument [Pluta2019, Dodge1997].

{% image "assets/img/posts/synthesis/2025-03-01-fm-synthesis/SimpleFMInstrument.png", "Simple FM instrument diagram with 2 oscillators: one modulator and one carrier." %}
_Figure {% increment figureId20250301  %}. Simple FM instrument._

Each box with a sine symbol inside is an oscillator. The plus "+" in a circle denotes sample-wise signal summation.

## Simple FM Spectrum

Although FM synthesis timbres sound quite complex, their spectrum structure is very straightforward. The partials are centered around the carrier frequency $f_C$ and spaced by the modulator frequency $f_M$.

You can see exactly how it looks in the frequency domain in this figure.

{% image "assets/img/posts/synthesis/2025-03-01-fm-synthesis/simple_fm_spectrum.png", "Plot of amplitude spectrum of an FM sound with partials spaced around the carrier frequency by the modulator frequency." %}
_Figure {% increment figureId20250301  %}. Magnitude spectrum of a sound generated from the simple FM instrument._

In the middle, there is the carrier frequency and on its sides are the **sidebands**.

In general, the frequency of each partial $f_P$ fulfills the following condition [Pluta2019]

$$
\begin{equation}
f_P = f_C + k f_M, \quad k \in \mathbb{Z},
\end{equation}
$$

where

- $f_C$ is the carrier frequency in Hz,
- $f_M$ is the modulator frequency in Hz, and
- $k$ is any integer (that’s what $k \in \mathbb{Z}$ means).

### Partials vs harmonics vs overtones

To avoid confusion, let me just quickly define partials, harmonics, and overtones.

Various sources use various definitions but I rely on a distinct meaning of each of these terms.

* A **partial** is a spectrum member.
* A **harmonic** is a member of a harmonic spectrum, i.e., spectrum whose partials are in a mathematical relation to each other (e.g., in a sawtooth, harmonics are integer multiples of the **fundamental frequency**).
* An **overtone** is a harmonic that is not the fundamental frequency.

The first harmonic is the fundamental frequency. The second harmonic is the first overtone.

Acoustic instrument spectra often consist of harmonic partials, inharmonic partials, and noise.

You can see a summary of these terms on the following figure.

{% image "assets/img/posts/synthesis/2025-03-01-fm-synthesis/partials_vs_harmonics_vs_overtones.svg", "Plot of the magnitude spectrum of a signal containing harmonic and inharmonic partials." %}
_Figure {% increment figureId20250301  %}. Magnitude spectrum of a signal containing harmonic partials (harmonics) and inharmonic partials._

## Timbre control of simple FM

One of the goals of FM synthesis research was to be able to use a MIDI keyboard to control it. That means we need a way of keeping the timbre somewhat consistent while changing the pitch.

It turns out that **if the ratio of the carrier frequency to the modulation frequency is constant, the partials' structure is preserved.**

In other words, if we multiply the carrier frequency by some real constant, we need to multiply the modulation frequency by the same constant in order to keep the partials' structure intact.

The frequency ratio is sometimes denoted $c:m$ or $R_f$. Mathematically, we can write

$$
\begin{equation}
c:m=R_f=\frac{f_C}{f_M}.
\end{equation}
$$

If $f_C$ and $f_M$ change but their ratio $R_f$ doesn’t, then the timbre shouldn't change either. There are various recipes for $R_f$ to create different timbres; you'll hear more examples later on in the article.

Let’s look at an example. (From now on, you can assume that $A_C = 1$ because changing $A_C$ would only change the volume of the waveform, not its timbre.)

Here’s a sound generated with $f_C = 200 \text{ Hz}, f_M = 400 \text{ Hz},$  and $A_M = 800$.

{% render 'embed-audio.html', src: "/assets/wav/posts/synthesis/2025-03-01-fm-synthesis/basic_signal.flac" %}

Here’s its spectrum.

{% image "assets/img/posts/synthesis/2025-03-01-fm-synthesis/basic_signal_spectrum.png", "Magnitude spectrum of an FM sound" %}
_Figure {% increment figureId20250301  %}. Magnitude spectrum of a sound generated with $f_C = 200 \text{ Hz}, f_M = 400 \text{ Hz},$  and $A_M = 800$._

Let’s now generate a sound that’s twice higher in pitch but has a similar timbre. According to the frequency ratio (Equation 7),

$$
\begin{equation}
R_f = \frac{f_C}{f_M} = \frac{200}{400} = 0.5.
\end{equation}
$$

In this particular case, it suffices to double the modulation frequency $f_M$ to raise the sound by an octave. To preserve the ratio $R_f$ we must double the carrier frequency as well.

Here’s the resulting sound generated with $f_C = 400 \text{ Hz}, f_M = 800 \text{ Hz},$  and $A_M = 800$.

{% render 'embed-audio.html', src: "/assets/wav/posts/synthesis/2025-03-01-fm-synthesis/octave_higher_half_index.flac" %}

And here’s its spectrum.

{% image "assets/img/posts/synthesis/2025-03-01-fm-synthesis/octave_higher_half_index_spectrum.png", "Magnitude spectrum of an FM sound" %}
_Figure {% increment figureId20250301  %}. Magnitude spectrum of a sound generated with $f_C = 400 \text{ Hz}, f_M = 800 \text{ Hz},$  and $A_M = 800$._

You can hear that the octave-higher version has a similar timbre and the partials are correctly spaced, yet their amplitudes look a little bit different. That is because we have not changed the modulation amplitude. If we set $A_M=1600$ (twice the original value), we get the following sound.

{% render 'embed-audio.html', src: "/assets/wav/posts/synthesis/2025-03-01-fm-synthesis/octave_higher.flac" %}

Here’s its spectrum.

{% image "assets/img/posts/synthesis/2025-03-01-fm-synthesis/octave_higher_spectrum.png", "Magnitude spectrum of an FM sound" %}
_Figure {% increment figureId20250301  %}. Magnitude spectrum of a sound generated with $f_C = 400 \text{ Hz}, f_M = 800 \text{ Hz},$  and $A_M = 1600$._

As you can hear, this last one sounds more like the original. As you can see, the partials’ structure is completely preserved, they are just spaced apart more because of the higher pitch.

Why did we need to change the modulation amplitude as well? Because **the amplitude of each partial is determined by both the amplitude and the frequency of modulation** [Dodge1997]. The meaning of the modulation amplitude at modulation frequency equal to 400 Hz is different from its meaning when the modulation frequency is equal to 800 Hz.

That's why we need to use a different parameter to control the timbre: the modulation index.

## Modulation Index

To have a parameter that controls the timbre in a consistent way across all modulation frequencies, it’s more handy to use the **modulation index** than the modulation amplitude. Modulation index will change the modulation amplitude according to the current modulator frequency.

Here’s the formula for the modulation index $I$ [Pluta2019]

$$
\begin{equation}
I = \frac{A_M}{f_M},
\end{equation}
$$

where

- $A_M$ is the modulation amplitude, and
- $f_M$ is the modulation frequency.

We can plug this formula into our simple FM equation (Equation 5)

$$
\begin{equation}
s_\text{FM}(t) = A_C \sin\left(2 \pi \int \limits_0^t (f_C + I f_M \cos(2 \pi f_M \tau))d\tau\right).
\end{equation}
$$

In our previous example, initially we had $A_M=800$ and $f_M=400 \text{ Hz}$ which resulted in $I=\frac{800}{400} = 2$.

After raising the pitch by an octave, we had $A_M = 800$ and $f_M=800 \text{ Hz}$ which resulted in $I = \frac{800}{800} = 1$. Thus, our partials’ amplitudes changed because we had not preserved the modulation index. To remedy this, we doubled the modulation amplitude to 1600 and hence obtained $I=\frac{1600}{800}=2$, i.e., the same modulation index as the initial sound.

**The key takeaways** are:

- use modulation index instead of the modulation amplitude to preserve partials’ amplitudes when changing pitch, and
- use constant carrier-to-modulator frequency ratio to preserve partials' frequencies.

In other words: to preserve the timbre when changing pitch, keep the modulation index $I$ and the carrier-to-modulator frequency ratio $R_f$ fixed.

Now, our simple FM diagram looks as follows.

{% image "assets/img/posts/synthesis/2025-03-01-fm-synthesis/SimpleFMInstrumentWithModulationIndex.png", "Simple FM instrument diagram that takes a modulation index as an input" %}
_Figure {% increment figureId20250301  %}. Simple FM instrument with modulation index $I$._

Again, a box with a sine symbol inside denotes an oscillator. The plus "+" in a circle denotes sample-wise signal summation. The asterisk "$\ast$" denotes sample-wise multiplication.

## Phase Modulation

Since we’ve just revisited the simple FM equation (Equation 10), let’s do one more adjustment to it. If we are less mathematically strict and we attempt to solve the integral in the carrier oscillator’s phase, we obtain the following FM equation [Pluta2019, Tolonen1998]

$$
\begin{equation}
s_\text{PM}(t) = A_C \sin\left(2 \pi f_C t + I \sin(2 \pi f_M t)\right),
\end{equation}
$$

where

- $A_C$ is the carrier amplitude,
- $f_C$ is the carrier frequency in Hz,
- $t$ is time in seconds,
- $I$ is the modulation index,
- $f_M$ is the modulator frequency in Hz.

Why do I say that we are “less mathematically strict”? Well, that’s because $s_\text{PM}(t)$ represents **phase modulation** (PM) not frequency modulation (FM).

What’s the difference? That’s a great question.

Most sources I’ve seen say that the difference between the two is not relevant [Pluta2019, Roads1996, Tolonen1998, DePoli1983] and point to two articles [Bate1990, Holm1992] that explain the difference.

The answer I found in [Holm1992] is that FM and PM are equivalent if the sampling rate is high enough. Then, the numerical integration used to implement the FM equation (Equation 10) approximates the continuous time integration accurately enough. On the other hand, inaccurate integration (when the sample rate is too small) results in diverging partials’ amplitudes between FM and PM.

Take a look at this example. Here, $f_C=200 \text{ Hz}, f_M = 400 \text{ Hz}$ and $I = \pi$.

When the sampling rate is equal to 96 kHz, we obtain the following magnitude spectra of PM and FM.

{% image "assets/img/posts/synthesis/2025-03-01-fm-synthesis/fm_vs_pm_modulation_fs_96000_spectrum.png", "Plot of amplitude spectra of sounds generated with frequency modulation and phase modulation at 96 kiloherz sampling rate" %}
_Figure {% increment figureId20250301  %}. Amplitude spectra of FM and PM sounds at 96 kHz sampling rate._

As you can see, the spectra nicely overlap. Audibly, there is no difference either.

FM at 96 kHz:

{% render 'embed-audio.html', src: "/assets/wav/posts/synthesis/2025-03-01-fm-synthesis/fm_fs_96000.flac" %}

PM at 96 kHz:

{% render 'embed-audio.html', src: "/assets/wav/posts/synthesis/2025-03-01-fm-synthesis/pm_fs_96000.flac" %}

However, if we decrease the sampling rate to 22.05 kHz…

{% image "assets/img/posts/synthesis/2025-03-01-fm-synthesis/fm_vs_pm_modulation_fs_22050_spectrum.png", "Plot of amplitude spectra of sounds generated with frequency modulation and phase modulation at 22.05 kiloherz sampling rate" %}
_Figure {% increment figureId20250301  %}. Amplitude spectra of FM and PM sounds at 22.05 kHz sampling rate._

…the partials’ amplitudes differ much more. FM has stronger first, second, and fourth partial, while PM has stronger third partial.

We can also start hearing a difference between the two sounds.

FM at 22.05 kHz:

{% render 'embed-audio.html', src: "/assets/wav/posts/synthesis/2025-03-01-fm-synthesis/fm_fs_22050.flac" %}

PM at 22.05 kHz:

{% render 'embed-audio.html', src: "/assets/wav/posts/synthesis/2025-03-01-fm-synthesis/pm_fs_22050.flac" %}

To my ear, the FM sound has a more pronounced low-frequency partial.

That’s in essence **the difference between FM and PM: at high enough sampling rates, they are equivalent.** The lower the sampling rate, the more their partials’ amplitudes differ.

To drive this point home, let's take a look at time-domain plots of a carrier at 600 Hz, a modulator at 50 Hz, and the resulting FM and PM signals ($I = 10$).

{% image "assets/img/posts/synthesis/2025-03-01-fm-synthesis/carrier_modulator_fm_pm_signal.png", "Plot of time-domain signals of a 600 hertz carrier, 50 hertz modulator and resulting FM and PM signals. FM and PM signals look identical." %}
_Figure {% increment figureId20250301  %}. A 600-Hz carrier, a 50-Hz modulator and the resulting FM and PM signals. Modulation index equals 10._

As you can see, they are identical.

Looking at Equations 10 and 11, you can tell that implementation-wise it’s way easier to use PM and that’s what we’ll do for the remainder of this article.

So, from now on, our go-to formula for frequency modulation will be the PM formula (Equation 11). This is the formula that we will analyze in the context of FM. So everywhere I write “FM” from now on, I refer to PM.

Just like synth manufacturers!

**Key takeaway**: FM and PM only differ at low sampling rates. For implementation, use phase modulation (Equation 11).

## How to control the timbre of FM?

We said that if the ratio of the carrier frequency to the modulator frequency $R_f$ is constant, the pitch will be constant. But what is the pitch in FM? We have two frequencies, $f_C$ and $f_M$: which one is the pitch?

To answer this, we must answer a different question first…

### When is FM spectrum harmonic?

**Harmonic spectra are obtained only if $R_f$ is rational**, i.e., $R_f = \frac{N_1}{N_2}, N_1, N_2 \in \mathbb{Z}$ ($R_f$ is a ratio of integer numbers) [Pluta2019].

Let’s look at a few examples and listen to them. In all of them, $I=\pi$.

$R_f = 1:2$

{% render 'embed-audio.html', src: "/assets/wav/posts/synthesis/2025-03-01-fm-synthesis/c_1_m_2_f0_200.flac" %}

{% image "assets/img/posts/synthesis/2025-03-01-fm-synthesis/c_1_m_2_f0_200_spectrum.png", "Plot of the amplitude spectrum of an FM sound generated with carrier to modulator frequency ratio equal to one to two" %}
_Figure {% increment figureId20250301  %}. Magnitude spectrum of an FM sound with $c:m=1:2$._

$R_f = 2:1$

{% render 'embed-audio.html', src: "/assets/wav/posts/synthesis/2025-03-01-fm-synthesis/c_2_m_1_f0_200.flac" %}

{% image "assets/img/posts/synthesis/2025-03-01-fm-synthesis/c_2_m_1_f0_200_spectrum.png", "Plot of the amplitude spectrum of an FM sound generated with carrier to modulator frequency ratio equal to two to one" %}
_Figure {% increment figureId20250301  %}. Magnitude spectrum of an FM sound with $c:m=2:1$._

$R_f = \sqrt{2}:1$

{% render 'embed-audio.html', src: "/assets/wav/posts/synthesis/2025-03-01-fm-synthesis/c_1.41_m_1_f0_200.flac" %}

{% image "assets/img/posts/synthesis/2025-03-01-fm-synthesis/c_1.41_m_1_f0_200_spectrum.png", "Plot of the amplitude spectrum of an FM sound generated with carrier to modulator frequency ratio equal to square root of two to one" %}
_Figure {% increment figureId20250301  %}. Magnitude spectrum of an FM sound with $c:m=\sqrt{2}:1$._

As you could hear, as long as $N_1$ and $N_2$ are integer, the sound and the spectra are harmonic. However, as soon as $R_f$ becomes real but not rational (in our case $R_f$ became $\sqrt{2}$), then the sound becomes metallic and inharmonic like a detuned sawtooth.

Let's listen to an extreme example of $R_f = 100:99$:

{% render 'embed-audio.html', src: "/assets/wav/posts/synthesis/2025-03-01-fm-synthesis/c_1_m_0.99_f0_200_I_3.141592653589793.flac" %}

Even here, we still hear a harmonic sound. And that's despite the “beating” effect caused by inharmonic partials close to harmonic ones.

Apart from the rational ratio requirement, the literature says that **if we want to obtain a clearly audible pitch, $N_1$ and $N_2$ after dividing out common factors should be relatively small** [Pluta2019].

What if they aren't small?

Let's listen to an example with $R_f=10:9$.

{% render 'embed-audio.html', src: "/assets/wav/posts/synthesis/2025-03-01-fm-synthesis/c_10_m_9_f0_200.flac" %}

{% image "assets/img/posts/synthesis/2025-03-01-fm-synthesis/c_10_m_9_f0_200_spectrum.png", "Plot of the amplitude spectrum of an FM sound generated with carrier to modulator frequency ratio equal to ten to nine" %}
_Figure {% increment figureId20250301  %}. Magnitude spectrum of an FM sound with $c:m=10:9$._

Here, we can hear what happens when the small ratio requirement is neglected: although the ratio is rational, we have a sense of inharmonicity. The inharmonicity is caused by reflected partials: partials with negative frequencies that are being mirrored back onto the positive frequency axis. Thus, the sound is not as clearly harmonic as in the previous examples with rational $R_f$.

**Key takeaway**: if you want your FM sound to be harmonic, keep the carrier frequency to modulator frequency ratio rational and relatively small in numerator and denominator.

### What’s the fundamental frequency (the pitch) in FM?

The **fundamental frequency** is the difference between the harmonic partials’ frequencies and is typically the lowest harmonic partial. The **pitch** is the sensation of the perceived height of a sound and is most often associated with the fundamental frequency. In the following, I use the two interchangeably.

In FM, if the ratio of the carrier frequency to the modulator frequency is rational, i.e., $\frac{f_C}{f_M} = R_f = \frac{N_1}{N_2}, N_1, N_2 \in \mathbb{Z}$, then the fundamental frequency $f_0$ can be computed as [Pluta2019]

$$
\begin{equation}
f_0 = \frac{f_C}{N_1} = \frac{f_M}{N_2}.
\end{equation}
$$

So if you want to generate a sound with a specific carrier-to-modulator-frequency ratio $R_f$ at pitch $f_0$, you should set the carrier and the modulator frequencies as

$$
\begin{align}
f_C &= N_1f_0,\\
f_M &= N_2f_0.
\end{align}
$$

That’s how I generated the above harmonic and inharmonic examples: by setting $f_0 = 200\text{ Hz}$. Thus, the harmonic examples seem to have the same pitch although they differ in timbre.

### How to eliminate every $N_2$-th harmonic?

The carrier-to-modulator frequency ratio $R_f=\frac{N_1}{N_2}, N_1,N_2 \in \mathbb{Z}$ not only allows us to fix the timbre and steer the pitch but also to eliminate partials [Chowning1973, Pluta2019].

Specifically,

- If $N_2 =1$, all harmonics are present. Example ($f_C=5000\text{ Hz}, f_M=1000 \text{ Hz}, I=2$):
    
    {% render 'embed-audio.html', src: "/assets/wav/posts/synthesis/2025-03-01-fm-synthesis/c_5_m_1_f0_1000.flac" %}
    
    {% image "assets/img/posts/synthesis/2025-03-01-fm-synthesis/c_5_m_1_f0_1000_spectrum.png", "Plot of the amplitude spectrum of an FM sound when carrier-to-modulator frequency ratio is 5 to 1 and modulation index equal to 2" %}
    _Figure {% increment figureId20250301  %}. Magnitude spectrum of an FM sound with $c:m=5:1$ and $I=2$._
    
- If $N_2$ is even, the spectrum is odd, i.e., only odd partials are present. Example ($f_C=5000\text{ Hz}, f_M=2000 \text{ Hz}, I=2$):
    
    {% render 'embed-audio.html', src: "/assets/wav/posts/synthesis/2025-03-01-fm-synthesis/c_5_m_2_f0_1000.flac" %}
    
    {% image "assets/img/posts/synthesis/2025-03-01-fm-synthesis/c_5_m_2_f0_1000_spectrum.png", "Plot of the amplitude spectrum of an FM sound when carrier-to-modulator frequency ratio is 5 to 2 and modulation index equal to 2" %}
    _Figure {% increment figureId20250301  %}. Magnitude spectrum of an FM sound with $c:m=5:2$ and $I=2$._
    
    Note the missing second, fourth, sixth, and eighth harmonics.
    
- If $N_2 =3$, every third harmonic is missing. Example ($f_C=5000\text{ Hz}, f_M=3000 \text{ Hz}, I=2$):
    
    {% render 'embed-audio.html', src: "/assets/wav/posts/synthesis/2025-03-01-fm-synthesis/c_5_m_3_f0_1000.flac" %}
    
    {% image "assets/img/posts/synthesis/2025-03-01-fm-synthesis/c_5_m_3_f0_1000_spectrum.png", "Plot of the amplitude spectrum of an FM sound when carrier-to-modulator frequency ratio is 5 to 3 and modulation index equal to 2" %}
    _Figure {% increment figureId20250301  %}. Magnitude spectrum of an FM sound with $c:m=5:3$ and $I=2$._
    

In general, if $\frac{f_C}{f_M} = \frac{N_1}{N_2}, N_1, N_2 \in \mathbb{Z}$, then every $N_2$-th partial is missing [Pluta2019].

### How to control the brightness of FM spectra?

The brightness of a sound is typically associated with the presence of high frequencies. In FM synthesis, we can control the center of the sound’s spectrum with the carrier frequency, the spacing of the partials with the modulator frequency, and the bandwidth of the spectrum with the modulation frequency and the modulation index. If we want to change the bandwidth of the spectrum (resulting in a brightness change) without changing the pitch, we can simply alter the modulation index.

Specifically, John Chowning computed the bandwidth of a simple FM sound as [Chowning1973]

$$
\begin{equation}
BW_\text{FM} \approx 2 f_M(I + 1),
\end{equation}
$$

where $f_M$ is the modulation frequency in Hz and $I$ is the modulation index. Here, the bandwidth means a frequency range in Hz that encompasses the most significant partials (but not all of the partials).

Let’s look at some examples using $f_C = 1000 \text{ Hz}$ and $f_M = 200 \text{ Hz}.$

Let’s set $I=1$. Here’s the resulting sound.

{% render 'embed-audio.html', src: "/assets/wav/posts/synthesis/2025-03-01-fm-synthesis/c_5_m_1_f0_200_I_1.flac" %}

And here’s its spectrum.

{% image "assets/img/posts/synthesis/2025-03-01-fm-synthesis/c_5_m_1_f0_200_I_1_spectrum.png", "Plot of the amplitude spectrum of an FM sound generated with carrier frequency equal to 1000 Hz, modulator frequency equal to 200 Hz and modulation index equal to 1. The partials occupy an 800-hertz bandwidth." %}
_Figure {% increment figureId20250301  %}. Magnitude spectrum of an FM sound where $f_C = 1000 \text{ Hz}$, $f_M = 200 \text{ Hz}$, and $I=1$._

As you can see, its bandwidth is $BW_\text{FM} = 2 \cdot 200 \text{ Hz} \cdot (1 + 1) = 800 \text{ Hz}$. Although there are partials outside this range, they are not significant.

Here, $I=2$.

{% render 'embed-audio.html', src: "/assets/wav/posts/synthesis/2025-03-01-fm-synthesis/c_5_m_1_f0_200_I_2.flac" %}

{% image "assets/img/posts/synthesis/2025-03-01-fm-synthesis/c_5_m_1_f0_200_I_2_spectrum.png", "Plot of the amplitude spectrum of an FM sound generated with carrier frequency equal to 1000 Hz, modulator frequency equal to 200 Hz and modulation index equal to 2. The partials occupy an 1200-hertz bandwidth." %}
_Figure {% increment figureId20250301  %}. Magnitude spectrum of an FM sound where $f_C = 1000 \text{ Hz}$, $f_M = 200 \text{ Hz}$, and $I=2$._

As you can hear and see, the spectrum got wider and as a result, it sounds brighter.

Here, $I=3$.

{% render 'embed-audio.html', src: "/assets/wav/posts/synthesis/2025-03-01-fm-synthesis/c_5_m_1_f0_200_I_3.flac" %}

{% image "assets/img/posts/synthesis/2025-03-01-fm-synthesis/c_5_m_1_f0_200_I_3_spectrum.png", "Plot of the amplitude spectrum of an FM sound generated with carrier frequency equal to 1000 Hz, modulator frequency equal to 200 Hz and modulation index equal to 3. The partials occupy an 1600-hertz bandwidth." %}
_Figure {% increment figureId20250301  %}. Magnitude spectrum of an FM sound where $f_C = 1000 \text{ Hz}$, $f_M = 200 \text{ Hz}$, and $I=3$._

Here, $I=4$.

{% render 'embed-audio.html', src: "/assets/wav/posts/synthesis/2025-03-01-fm-synthesis/c_5_m_1_f0_200_I_4.flac" %}

{% image "assets/img/posts/synthesis/2025-03-01-fm-synthesis/c_5_m_1_f0_200_I_4_spectrum.png", "Plot of the amplitude spectrum of an FM sound generated with carrier frequency equal to 1000 Hz, modulator frequency equal to 200 Hz and modulation index equal to 4. The partials occupy an 2000-hertz bandwidth." %}
_Figure {% increment figureId20250301  %}. Magnitude spectrum of an FM sound where $f_C = 1000 \text{ Hz}$, $f_M = 200 \text{ Hz}$, and $I=4$._

As you can hear and see, the spectrum gets so wide that it expands over to negative frequencies. Negative frequencies get reflected back and hence the spectrum is no longer symmetric. However, it is still harmonic because just the amplitudes of the partials changed after the reflection, not their positions.

Here, $I=5$.

{% render 'embed-audio.html', src: "/assets/wav/posts/synthesis/2025-03-01-fm-synthesis/c_5_m_1_f0_200_I_5.flac" %}

{% image "assets/img/posts/synthesis/2025-03-01-fm-synthesis/c_5_m_1_f0_200_I_5_spectrum.png", "Plot of the amplitude spectrum of an FM sound generated with carrier frequency equal to 1000 Hz, modulator frequency equal to 200 Hz and modulation index equal to 5. The partials occupy an 2400-hertz bandwidth and are not symmetric in amplitude around the carrier because of wraparound of negative frequency components." %}
_Figure {% increment figureId20250301  %}. Magnitude spectrum of an FM sound where $f_C = 1000 \text{ Hz}$, $f_M = 200 \text{ Hz}$, and $I=5$._

This spectrum is clearly the brightest and it’s not symmetric. We could go even further than this but I’d leave it for your experimentation 🙂

### FM Efficiency

At this point, I would like to point out how efficient in generating rich sounds FM is. With just two table lookups (to get the values of the carrier and the modulator) we are able to generate quite elaborate spectra. With a few simple controls, we are able to change it in a significant but meaningful way. This low computational effort paired with powerful sonics was the reason why FM was one of the first synthesis techniques (if not the first) to be successfully implemented with digital electronics. In the 1980s, the chips were too weak to efficiently implement the alternatives like additive or subtractive synthesis.

If you want to learn how to efficiently generate a sine (or any waveform for that matter) using table lookup, [check out my wavetable synthesis tutorial]({% post_url collections.posts, "2021-08-13-wavetable-synthesis-theory" %})!

### How to control the partials’ amplitudes? Bessel functions

In the examples so far, we could see that the FM spectrum definitely has some pattern to it. Can we accurately predict what the partials’ amplitudes will be for given parameters?

It turns out that we can. As the literature reports [Chowning1973, DePoli1983, Pluta2019], we can write out the PM equation (Equation 11) as

$$
\begin{equation}
s_\text{PM} (t) = \sum \limits_{k=-\infty}^{\infty} J_k(I)\sin|2 \pi (f_C + k f_M)t|,
\end{equation}
$$

where

- $\sum$ is the sum operator; in the above equation, it is an infinite sum where each summand corresponds to one integer value assigned to $k$; here, each value of $k$ corresponds to one partial,
- $J_k(I)$ is a Bessel function of the first kind of order $k$ whose argument is the modulation index $I$,
- $|\cdot|$ denotes the absolute value,
- $f_C$ is the carrier frequency in Hz,
- $f_M$ is the modulator frequency in Hz,
- $t$ is time in seconds.

Bessel functions are a very important concept in mathematics. They appear in the solution of the wave equation: the basic equation of acoustics.

Here’s how Bessel functions of the first kind look for orders from 0 to 3.

{% image "assets/img/posts/synthesis/2025-03-01-fm-synthesis/bessel_functions_first_kind.png", "Plot of Bessel functions of the first kind for orders 0 to 3. Their maxima do not exceed 1 and they are very similar to sines." %}
_Figure {% increment figureId20250301  %}. Bessel functions of the first kind with orders 0 to 3. In FM synthesis, the argument $I$ represents the modulation index._

These are sine-like functions that decrease in amplitude the higher the absolute value of the argument. You can also observe that Bessel functions of even orders are even (symmetrical with respect to the $y$-axis) and Bessel functions of odd orders are odd (symmetrical with respect to the origin of the $xy$-plane).

What is more important, Bessel functions cross the value of 0 for many values of the argument $I$. It means that at particular values of the modulation index, some partials will have amplitude 0. As you remember, when we increase the modulation index, the spectrum gets wider but some partials may temporarily disappear.

It’s hard to get a feeling for the meaning of the partials’ amplitudes equation (Equation 16) without any visuals. Thus, here you can see a plot of how the spectrum changes if we vary the modulation index $I$ in the $[0, 20]$ range [Pluta2019].

{% image "assets/img/posts/synthesis/2025-03-01-fm-synthesis/partials_amplitudes_in_3d.png", "A 3D visualization of the modulation index's influence on FM spectrum. The larger the modulation index the wider the spectrum. A single partial's magnitude follows a Bessel function of the first kind corresponding to its index" %}
_Figure {% increment figureId20250301  %}. FM partials' amplitudes for various values of the modulation index. For a particular value of $I$, partials' amplitudes are represented by the cross-section of the plot along the partial index axis. After [Pluta2019]._

How to read this plot? Say you want to see how the spectrum looks for a particular value of $I$, for example, 10. Then, find 10 on the $I$ axis on the right and mentally cross-sect the 3-dimensional spectrum along the partials’ axis. This cross-section is your sound’s magnitude spectrum at the modulation index 10.

You can see what I mean on the figure below.

{% image "assets/img/posts/synthesis/2025-03-01-fm-synthesis/partials_amplitudes_in_3d_for_specific_modulation_index.png", "A cross-section of the 3D visualization of FM synthesis partials' amplitudes corresponding to the modulation index value of 10." %}
_Figure {% increment figureId20250301  %}. FM partials' amplitudes if the modulation index equals 10._

The 3D Bessel functions plot (Figure 24) gives you the full insight into the spectrum of FM sounds. You can go back to this plot over and over again to discover more and more properties of the FM spectrum. As you can see, it is completely frequency-independent; for each fundamental frequency, the partials behave identically. Of course, this plot does not take reflected frequencies into account but you can visualize them yourself 😉

## Extensions of simple FM

What we have discussed so far is “simple FM”, i.e., we have one sine carrier and one sine modulator.

Simple FM can be extended in various ways to create even more complex sounds [Pluta2019]:

1. We can add feedback, where the output of an FM instrument modulates the modulator. We can do this for any setup of carriers and modulators but the most popular approaches use one, two, or three oscillators within the feedback loop.
2. We can add multiple carriers modulated by the same oscillator. This is called multiple-carrier FM (MCFM). It can be used to create formants in the sound spectrum.
3. We can have non-sine carriers or modulators. However, non sinusoid modulators can result in very dense spectra, so we should be careful when using harmonically rich modulators [Dodge1997].
4. We can add multiple modulators, parallel or serial, that modulate one carrier. This is called multiple-modulator FM (MMFM). This technique increases the number of partials in the output spectrum. Again, multiple non-sine modulators make little sense because the spectrum gets too dense [Dodge1997].
5. We can use oscillators with exponential control which emulates analog gear. This is called exponential FM. Exponential FM is used in Virtual Analog applications.
6. We can combine two or more FM instruments in parallel or in serial. However, this may quickly get too complicated to control.
7. We can add [envelope generators (EGs)]({% post_url collections.posts, "2022-07-03-envelopes" %}) to control various FM parameters. For example, an envelope generator controlling the modulation index can create a naturally sounding effect of timbre brightening with the initial transient. An EG-controlled timbre gets darker and darker the longer the sound is played (or a keyboard key is held).
8. Phase distortion (PD) synthesis is another take on phase modulation. In this technique, the modulator frequency is equal to the carrier frequency or to its multiplicity. Moreover, various modulator waveforms are used, for example, a triangle waveform. A picture sometimes says a thousand words, so [here’s a very short but very good explanation of phase distortion synthesis](https://electricdruid.net/phase-distortion-synthesis/) (accessed February 10, 2024). [Oli Larkin, whom I interviewed in the 15th episode of the WolfTalk podcast]({% post_url collections.posts, '2023-11-09-oliver-larkin' %}), is well known for his implementations of Casio’s phase distortion emulations.

The discussion of all these extensions is beyond the scope of this already quite long article. Should they be discussed in more detail in future articles? Let me know in the comments!

## Summary

In this comprehensive article, you’ve learned about the frequency modulation (FM) and phase modulation (PM) synthesis. You’ve learned how these two are different, how their spectra look and how to control these spectra.

You’ve also learned what Bessel functions are and how the partials' amplitudes in FM synthesis follow Bessel functions with increasing modulation index.

You’ve learned what the modulation index is and how to use it to control the bandwidth of FM spectra.

Finally, we have mentioned various extensions to the simple FM technique.

In future articles, we will look into how to implement the PM synthesis technique using various programming languages. So look out for those!

If you want to become an audio developer today, check out my [free Audio Developer Checklist]({% link collections.all, 'checklist.html' %}). It lists every bit and piece of knowledge I believe is necessary to become a full-fledged audio programmer and be able to create software synths, for example, with FM synthesis.

## Bibliography

[Bate1990] John A. Bate, *The Effect of Modulator Phase on Timbres in FM Synthesis*, Computer Music Journal Vol. 14, No. 3, Autumn 1990.

[Chowning1973] **Original FM paper by John Chowning**: John M. Chowning, *The Synthesis of Complex Audio Spectra by Means of Frequency Modulation*, J. Audio Eng. Soc. 21, 7, 1973. [[PDF](https://web.eecs.umich.edu/~fessler/course/100/misc/chowning-73-tso.pdf), accessed March 5, 2025]

[DePoli1983] Giovanni De Poli, *A Tutorial on Digital Sound Synthesis Techniques*, Computer Music Journal 7(4), October 1983 [[PDF](https://www.researchgate.net/profile/Giovanni-De-Poli/publication/245122776_A_Tutorial_on_Digital_Sound_Synthesis_Techniques/links/5460a5f50cf295b56162786e/A-Tutorial-on-Digital-Sound-Synthesis-Techniques.pdf), accessed March 5, 2025]

[Dodge1997] Charles Dodge, Thomas A. Jerse, *Computer Music: Synthesis, Composition, and Performance*, 2nd ed., Schirmer Books, 1997.

[Farina 2000] Angelo Farina, *Simultaneous Measurement of Impulse Response and Distortion With a Swept-Sine Technique*, 108th AES Convention, Paris, France, 2000. [[PDF](https://www.researchgate.net/publication/2456363_Simultaneous_Measurement_of_Impulse_Response_and_Distortion_With_a_Swept-Sine_Technique), accessed March 5, 2025]

[Holm1992] Frode Holm, *Understanding FM Implementations: A Call for Common Standards*, Computer Music Journal Vol. 16, No. 1, Spring 1992.

[Pluta2019] Marek Pluta, *Sound Synthesis for Music Reproduction and Performance*, monograph, AGH University of Science and Technology Press 2019. [[PDF](https://winntbg.bg.agh.edu.pl/skrypty4/0612/synteza.pdf), (accessed March 6, 2025)]

[SOS2000] [Gordon Reid, An Introduction To Frequency Modulation, Synth Secrets, Sound on Sound](https://www.soundonsound.com/techniques/introduction-frequency-modulation). (accessed March 5, 2025)

[Tolonen1998] Tero Tolonen, Vesa Välimäki, and Matti Karjalainen, *Evaluation of Modern Sound Synthesis Methods*, Report 48, Helsinki University of Technology, Espoo 1998. [[**NOT SECURE** PDF](http://legacy.spa.aalto.fi/publications/reports/sound_synth_report.pdf), accessed March 5, 2025]

[Wikipedia] [Frequency modulation synthesis, Wikipedia](https://en.wikipedia.org/wiki/Frequency_modulation_synthesis). (accessed March 5, 2025)

[Zölzer2011] Udo Zölzer et al., *DAFX: Digital Audio Effects*, 2nd ed., Helmut Schmidt University – University of the Federal Armed Forces, Hamburg, Germany: John Wiley & Sons Ltd, 2011.
