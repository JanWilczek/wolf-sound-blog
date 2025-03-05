---
title: "FM Synthesis Explained For Audio Programmers: Art and Science"
description: "Frequency modulation synthesis explained for audio programmers: a single all-in-one resource"
date: 2025-03-01
author: Jan Wilczek
layout: post
permalink: /fm-synthesis-explained-for-audio-programmers-art-and-science/
background: /assets/img/posts/synthesis/2025-03-01-fm-synthesis/Thumbnail.webp
draft: true
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

1. [History](#history)
2. [Vibrato](#vibrato)
3. [Basic FM Synth](#basic-fm-synth)
   1. [Proper FM Formula](#proper-fm-formula)
   2. [Simple FM Diagram](#simple-fm-diagram)
4. [Simple FM Spectrum](#simple-fm-spectrum)
5. [Timbre control of simple FM](#timbre-control-of-simple-fm)
6. [Modulation Index](#modulation-index)
7. [Phase Modulation](#phase-modulation)
8. [How to control the timbre of FM?](#how-to-control-the-timbre-of-fm)
   1. [When is FM spectrum harmonic?](#when-is-fm-spectrum-harmonic)
   2. [What’s the fundamental frequency (the pitch) in FM?](#whats-the-fundamental-frequency-the-pitch-in-fm)
   3. [How to eliminate every $N\_2$-th harmonic?](#how-to-eliminate-every-n_2-th-harmonic)
   4. [How to control the brightness of FM spectra?](#how-to-control-the-brightness-of-fm-spectra)
   5. [FM Efficiency](#fm-efficiency)
   6. [How to control the partials’ amplitudes? Bessel functions](#how-to-control-the-partials-amplitudes-bessel-functions)
9. [Presenting FM algorithm visually](#presenting-fm-algorithm-visually)
10. [Example FM sounds](#example-fm-sounds)
11. [Extensions of simple FM](#extensions-of-simple-fm)
12. [Summary](#summary)

{% render 'google-ad.liquid' %}

TODO: Add Python code (at least links to)

## History

Just as a brief word of history, to give credit to people's hard work, the original publication on FM synthesis came from John Chowning  in 1973 [Chowning1973]. Because of lack of interest of American manufacturers in using the technique in hardware synths, Chowning turned to Japan-based manufacturer Yamaha in the same year. [SOS2000]

{% image "assets/img/posts/synthesis/2025-03-01-fm-synthesis/Chowning.jpg", "John Chowning" %}

_Figure . John Chowning. [Source](https://commons.wikimedia.org/wiki/File:Chowning.jpg), accessed March 5, 2025, licensed under the [Creative Commons Attribution-Share Alike 3.0 Unported license](https://creativecommons.org/licenses/by-sa/3.0/deed.en)._

However, it wasn't until 1983, when the first widely successful FM synth was introduced, namely, Yamaha DX7 FM [Wikipedia]. It took the market by storm and spawned a host of FM-based hardware synths.

That 10-year gap should tell you how much engineering effort was required to make FM commercially usable!

## Vibrato

Before we delve into the frequency modulation synthesis, we should consider what is vibrato.

**Vibrato** is a musical effect of a musical sound varying up and down in pitch. In other words, vibrato is a periodical pitch variation [Zölzer2011].

In this sense, we **modulate** the pitch. To achieve the vibrato, the modulation must be quite slow: in the range of 5-14 Hz [Zölzer2011]. Note that this range is below the human hearing range, which is typically associated with the 20-20 000 Hz range.

Here’s how a single musical note (a sine representing the MIDI note 57) without the vibrato sounds.

{% render 'embed-audio.html', src: "/assets/wav/posts/synthesis/2025-03-01-fm-synthesis/plain_note_220Hz.flac" %}

Here’s how the same note sounds when we apply a 10 Hz vibrato to it with a modulation index 2 (which means that the pitch should change by +/- 20 Hz).

{% render 'embed-audio.html', src: "/assets/wav/posts/synthesis/2025-03-01-fm-synthesis/pm_vibrato_note_220Hz.flac" %}

## Basic FM Synth

Let’s now consider a basic frequency modulation instrument.

In FM, we **modulate the frequency** of the carrier waveform. It means that the **instantaneous frequency** (frequency at a particular time instant) is constantly being changed by the **modulator** in a regular fashion.

In the simplest FM setup, a sine modulator modulates a sine carrier. In this scenario, the instantaneous frequency $f(t)$ (which is a function of time) is given by the following formula [Pluta2019]

$$
\begin{equation}
f(t) = f_C + A_M\cos(2\pi f_M t),
\end{equation}
$$

where

- $f_C$ is the frequency of the carrier in Hz,
- $A_M$ is the amplitude of the modulator (unitless),
- $\cos$ is the cosine function,
- $f_M$ is the frequency of the modulator in Hz,
- $t$ is time in seconds.

To create a sine oscillator whose frequency changes according to Equation 1, we cannot simply put it into the sine formula like this

$$
\begin{equation}
s_\text{FM}(t) \neq A_C \sin\left(2 \pi f(t) t\right) = A_C \sin\left(2 \pi (f_C + A_M \cos(2 \pi f_M t))t\right),
\end{equation}
$$

because it’s not mathematically correct. Here, $A_C$ stands for **carrier frequency**. If we would apply this to generate a signal where $A_C = 1, f_C=220 \text{ Hz}, f_M=110 \text{Hz},$ and $A_M = 220 \text{ Hz}$, then we would get a signal that sounds like this.

{% render 'embed-audio.html', src: "/assets/wav/posts/synthesis/2025-03-01-fm-synthesis/wrong_fm_220Hz.flac" %}

Instead, we need to use the fact the **angular frequency is the derivative of phase** [Farina2000]. Mathematically speaking,

$$
\begin{equation}
2\pi f(t) = \frac{d \phi(t)}{dt},
\end{equation}
$$

where

- $2 \pi f(t)$ is the angular frequency in radians per sample,
- $\phi(t)$ denotes the instantaneous phase, and
- $\frac{d}{dt}$ denotes the derivative of a function over time.

*Note: if you don’t know what a derivative is, it is a measure of how much a given function changes at every point in time. The derivative is also a function. If you think about Equation 3, it makes total sense: if the phase is changing rapidly, the derivative is large, and the frequency is high; if the phase changes slowly, the derivative is small, and the frequency is low.*

The argument of a sine is the phase NOT the frequency. In order to obtain the phase from the equation for frequency (Equation 3), we must perform the operation that is inverse to derivation: integration.

$$
\begin{equation}
\phi(t) = \int \limits_0^t 2\pi f(\tau)d\tau = 2 \pi \int \limits_0^t (f_C + A_M \cos(2 \pi f_M \tau))d\tau,
\end{equation}
$$

### Proper FM Formula

Now, we can plug the formula for the phase into the sine function.

$$
\begin{equation}
s_\text{FM}(t) = A_C \sin\left(2 \pi \int \limits_0^t (f_C + A_M \cos(2 \pi f_M \tau))d\tau\right),
\end{equation}
$$

This is the correct formula for a simple FM instrument: we have a sine carrier with amplitde $A_C$ and frequency $f_C$ and a sine modulator (represented by the cosine) with amplitude $A_M$ and frequency $f_M$ (called the **modulation frequency**). Note that we need to use a different symbol for time than $t$ in the integral because $t$ denotes the time point for which we compute the phase for; I chose $\tau$ (tau).

### Simple FM Diagram

FM variants are most often explained on the basis of diagrams. The diagrams can easily show how the interconnection between the oscillators are placed much like in graphical audio programming languages like Max/MSP or PureData.

Here is the diagram of a simple FM instrument [Pluta2019, DodgeJerse].

TODO

## Simple FM Spectrum

Although the spectrum of FM synthesis is quite complex, its structure is very straightforward. The partials are centered around the carrier frequency $f_C$ and spaced by the modulator frequency $f_M$.

You can see exactly how it looks in the frequency domain in this figure.

{% image "assets/img/posts/synthesis/2025-03-01-fm-synthesis/simple_fm_spectrum.png", "Simple FM spectrum" %}

In the middle, there is the carrier frequency and on its sides are the **sidebands**.

In general, the frequency of each partial $f_P$ fulfills the following condition [Pluta2019]

$$
\begin{equation}
f_P = f_C + k f_M, \quad k \in \mathbb{Z},
\end{equation}
$$

where

- $f_C$ is the carrier frequency,
- $f_M$ is the modulator frequency, and
- $k$ is any integer (that’s what $k \in \mathbb{Z}$ means).

## Timbre control of simple FM

One of the goals of FM synthesis research was to be able to use a MIDI keyboard to control it. That means, that we need a way of keeping the timbre somewhat consistent while changing the pitch.

It turns out that if the ratio of the carrier frequency to the modulation frequency is constant, the partials structure is preserved. In other words, if we multiply the carrier frequency by some real constant, we need to multiply the modulation frequency by the same constant in order to keep the partials structure the intact.

The frequency ratio is sometimes denoted $c:m$ or $R_f$. Mathematically, we can write

$$
\begin{equation}
c:m=R_f=\frac{f_C}{f_M}.
\end{equation}
$$

If $f_C$ and $f_M$ change but their ratio $R_f$ doesn’t, then we have a single timbre at our hand. There are various recipes for $R_f$ to create different timbres and we will look into them later on in the article.

Here’s an example. (From now on, you can assume that $A_C = 1$ because changing $A_C$ would only change the volume of the waveform not its timbre.)

Here’s a sound generated with $f_C = 200 \text{ Hz}, f_M = 400 \text{ Hz},$  and $A_M = 800$.

{% render 'embed-audio.html', src: "/assets/wav/posts/synthesis/2025-03-01-fm-synthesis/basic_signal.flac" %}

Here’s its spectrum

{% image "assets/img/posts/synthesis/2025-03-01-fm-synthesis/basic_signal_spectrum.png", "basic_signal_spectrum.png" %}

Let’s now generate a sound that’s twice as high in pitch but has similar timbre. According the frequency ratio (Equation 7),

$$
R_f = \frac{f_C}{f_M} = \frac{200}{400} = 0.5.
$$

In this particular case, it suffices to double the modulation frequency $f_M$ to raise the sound by an octave. To preserve the ratio $R_f$ we must double the carrier frequency as well.

Here’s the resulting sound generated with $f_C = 400 \text{ Hz}, f_M = 800 \text{ Hz},$  and $A_M = 800$.

{% render 'embed-audio.html', src: "/assets/wav/posts/synthesis/2025-03-01-fm-synthesis/octave_higher_half_index.flac" %}

And here’s its spectrum.

{% image "assets/img/posts/synthesis/2025-03-01-fm-synthesis/octave_higher_half_index_spectrum.png", "octave_higher_half_index_spectrum.png" %}

You can hear that the octave-higher version has similar timbre and the partials are correctly spaced, yet their amplitudes look a little bit different. That is because we have not changed the modulation amplitude. If we set $A_M=1600$, we get the following sound.

{% render 'embed-audio.html', src: "/assets/wav/posts/synthesis/2025-03-01-fm-synthesis/octave_higher.flac" %}

Here’s its spectrum.

{% image "assets/img/posts/synthesis/2025-03-01-fm-synthesis/octave_higher_spectrum.png", "octave_higher_spectrum.png" %}

As you can hear, the octave-higher sound sounds more like the original. As you can see, the partials’ structure is completely preserved, they are just spaced apart more because of the higher pitch.

Why did we need to change the modulation amplitude as well? Because the amplitude of each partial is determined by both the amplitude and the frequency of modulation [DodgeJerse]. The meaning of the modulation amplitude at modulation frequency equal to 400 Hz is different from its meaning when the modulation frequency is equal to 800 Hz.

## Modulation Index

To preserve the timbre and be able to have a parameter that controls the timbre in a consistent way across all modulation frequencies, it’s more handy to use the **modulation index** than the modulation amplitude.

Here’s the formula for the modulation index $I$ [Pluta2019]

$$
\begin{equation}
I = \frac{A_M}{f_M},
\end{equation}
$$

where

- $A_M$ is the modulation amplitude and
- $f_M$ is the modulation frequency.

We can plug this formula into our simple FM equation (Equation 5)

$$
\begin{equation}
s_\text{FM}(t) = A_C \sin\left(2 \pi \int \limits_0^t (f_C + I f_M \cos(2 \pi f_M \tau))d\tau\right).
\end{equation}
$$

In our previous example, initially we had $A_M=800$ and $f_M=400 \text{ Hz}$ which results in $I=\frac{800}{400} = 2$.

After raising the pitch by an octave, we had $A_M = 800$ and $f_M=800 \text{ Hz}$ which results in $I = \frac{800}{800} = 1$. Thus, our partials’ amplitudes changed because we had not preserved the modulation index. To remedy this, we doubled the modulation amplitude to 1600 and hence obtained $I=\frac{1600}{800}=2$, i.e., the same modulation index as the initial sound.

The key takeaways are: 

- use modulation index instead of the modulation amplitude to preserve partials’ amplitudes when changing pitch and
- use constant carrier-to-modulator frequency ratio to preserve timbre.

In other words: to preserve the timbre when changing pitch, keep the modulation index $I$ and the carrier-to-modulator frequency ratio $R_f$ fixed.

Now, our simple FM diagram looks as follows.

TODO

## Phase Modulation

Since we’ve just revisited the simple FM equation (Equation 9), let’s do one more adjustment to it. If we are less mathematically strict and we attempt to solve the integral in the carrier oscillator’s phase, we obtain the following FM equation [Pluta2019,Tolonen1998]

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

Why do I say that we are “less mathematically strict”? Well, that’s because $s_\text{PM}(t)$ represents **phase modulation** (PM) not frequency modulation (FM). What’s the difference? That’s a great question. Most sources I’ve seen say that the difference between the two is not relevant [Pluta2019,Roads1996,Tulunen1998,DePoli???] and point to two articles [Bate,Holm] that explain the difference. The answer that I found in [Holm] is that FM and PM are equivalent if the sampling rate is high enough. Then, the numerical integration used to implement the FM equation (Equation 5) approximates the continuous time integration accurately enough. On the other hand, inaccurate integration (when the sample rate is too small) results in diverging partials’ amplitudes between FM and PM.

Take a look at this example. Here, $f_C=200 \text{ Hz}, f_M = 400 \text{ Hz}$ and $I = \pi$.

When the sampling rate is equal to 96 kHz, we obtain the following magnitude spectra of PM and FM.

{% image "assets/img/posts/synthesis/2025-03-01-fm-synthesis/fm_vs_pm_modulation_fs96000_spectrum.png", "fm_vs_pm_modulation_fs=96000_spectrum.png" %}

As you can see, the spectra nicely overlap. Audibly, there is no difference either.

FM at 96 kHz:

{% render 'embed-audio.html', src: "/assets/wav/posts/synthesis/2025-03-01-fm-synthesis/fm_fs_96000.flac" %}

PM at 96 kHz:

{% render 'embed-audio.html', src: "/assets/wav/posts/synthesis/2025-03-01-fm-synthesis/pm_fs_96000.flac" %}

However, if we decrease the sampling rate to 22.05 kHz…

{% image "assets/img/posts/synthesis/2025-03-01-fm-synthesis/fm_vs_pm_modulation_fs22050_spectrum.png", "fm_vs_pm_modulation_fs=22050_spectrum.png" %}

…the partials’ amplitudes differ much more. FM has stronger first, second, and fourth partial, while PM has stronger third partial.

We can also start hearing a difference between the two sounds.

FM at 22.05 kHz:

{% render 'embed-audio.html', src: "/assets/wav/posts/synthesis/2025-03-01-fm-synthesis/fm_fs_22050.flac" %}

PM at 22.05 kHz:

{% render 'embed-audio.html', src: "/assets/wav/posts/synthesis/2025-03-01-fm-synthesis/pm_fs_22050.flac" %}

To my ear, the FM sound has a more pronounced low-frequency partial.

That’s in essence the difference between FM and PM: at high enough sampling rates, they are equivalent. The lower the sampling rates, the more their partials’ amplitudes differ. However, implementation-wise, it’s way easier to use PM and that’s what we’ll do for the remainder of this article.

So, from now on, our go-to formula for frequency modulation will be the PM formula (Equation 10). This is the formula that we will analyze in the context of FM. So everywhere I write “FM” from now on will refer to PM.

## How to control the timbre of FM?

We said that if the ratio of the carrier frequency to the modulator frequency $R_f$ is constant, the pitch will be constant. But what is the pitch in FM? We have two frequencies, $f_C$ and $f_M$: which one is the pitch?

To answer this, we must answer a different question first…

### When is FM spectrum harmonic?

Harmonic spectra are obtained only if $R_f$ is rational, i.e., $R_f = \frac{N_1}{N_2}, N_1, N_2 \in \mathbb{Z}$ ($R_f$ is a ratio of integer numbers) [Pluta2019].

Let’s look at a few examples and listen to them. In all of them, $I=\pi$.

$R_f = 1:2$

{% render 'embed-audio.html', src: "/assets/wav/posts/synthesis/2025-03-01-fm-synthesis/c_1_m_2_f0_200.flac" %}

{% image "assets/img/posts/synthesis/2025-03-01-fm-synthesis/c1_m2_f0200_spectrum.png", "c=1_m=2_f0=200_spectrum.png" %}

$R_f = 2:1$

{% render 'embed-audio.html', src: "/assets/wav/posts/synthesis/2025-03-01-fm-synthesis/c_2_m_1_f0_200.flac" %}

{% image "assets/img/posts/synthesis/2025-03-01-fm-synthesis/c2_m1_f0200_spectrum.png", "c=2_m=1_f0=200_spectrum.png" %}

$R_f = 10:9$

{% render 'embed-audio.html', src: "/assets/wav/posts/synthesis/2025-03-01-fm-synthesis/c_10_m_9_f0_200.flac" %}

{% image "assets/img/posts/synthesis/2025-03-01-fm-synthesis/c10_m9_f0200_spectrum.png", "c=10_m=9_f0=200_spectrum.png" %}

$R_f = \sqrt{2}:1$

{% render 'embed-audio.html', src: "/assets/wav/posts/synthesis/2025-03-01-fm-synthesis/c_1.41_m_1_f0_200.flac" %}

{% image "assets/img/posts/synthesis/2025-03-01-fm-synthesis/c1_spectrum.png", "c=1_spectrum.png" %}

As you could hear, as long as $N_1$ and $N_2$ are integer, the sound and the spectra are harmonic. Even in the extreme case of $R_f = 100:99$, we get the “beating” effect because of the inharmonic partials close to the harmonic ones but this still sounds harmonic. However, as soon as $R_f$ became real but not rational ($\sqrt{2}$), then the sound became metallic and inharmonic like a detuned sawtooth.

Furthermore, the literature says that if we want to obtain a clearly audible pitch, $N_1$ and $N_2$ after dividing out common factors should be relatively small [Pluta2019]. You could hear an opposite effect in the $R_f=10:9$ example, where the ringing started to be strong enough to overshadow the pitch (but not completely).

Although the ratio is rational, the reflected partials (partials with negative frequencies that are being mirrored back onto the positive frequency axis) create the sensation of inhamonicity. Thus, the sound is not as clearly harmonic as in the previous examples with rational $R_f$.

Key takeaway: if you want you FM sound to be harmonic keep the carrier frequency to modulator frequency ratio rational and relatively small in numerator and denominator.

### What’s the fundamental frequency (the pitch) in FM?

The **fundamental frequency** is the difference between the harmonic partials’ frequencies and is typically the lowest harmonic partial. The **pitch** is the sensation of the perceived height of a sound and is most often associated with the fundamental frequency. In the following, I use the two interchangeably.

In FM, if the ratio of the carrier frequency to the modulator frequency is rational, i.e., $\frac{f_C}{f_M} = R_f = \frac{N_1}{N_2}, N_1, N_2 \in \mathbb{Z}$, then the fundamental frequency can be computed as [Pluta2019]

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

The frequency ratio $R_f$ not only allows us to fix the timbre and steer the pitch but also to eliminate the desired partials [Chowning1973,Pluta2019].

Specifically,

- If $N_2 =1$, all harmonics are present. Example ($f_C=5000\text{ Hz}, f_M=1000 \text{ Hz}, I=2$):
    
    {% render 'embed-audio.html', src: "/assets/wav/posts/synthesis/2025-03-01-fm-synthesis/c_5_m_1_f0_1000.flac" %}
    
    {% image "assets/img/posts/synthesis/2025-03-01-fm-synthesis/c5_m1_f01000_spectrum.png", "c=5_m=1_f0=1000_spectrum.png" %}
    
- If $N_2$ is even, the spectrum is odd, i.e., only odd partials are present. Example ($f_C=5000\text{ Hz}, f_M=2000 \text{ Hz}, I=2$):
    
    {% render 'embed-audio.html', src: "/assets/wav/posts/synthesis/2025-03-01-fm-synthesis/c_5_m_2_f0_1000.flac" %}
    
    {% image "assets/img/posts/synthesis/2025-03-01-fm-synthesis/c5_m2_f01000_spectrum.png", "c=5_m=2_f0=1000_spectrum.png" %}
    
    Note the missing second, fourth, sixth, and eighth harmonics.
    
- If $N_2 =3$, every third harmonic is missing. Example ($f_C=5000\text{ Hz}, f_M=3000 \text{ Hz}, I=2$):
    
    {% render 'embed-audio.html', src: "/assets/wav/posts/synthesis/2025-03-01-fm-synthesis/c_5_m_3_f0_1000.flac" %}
    
    {% image "assets/img/posts/synthesis/2025-03-01-fm-synthesis/c5_m3_f01000_spectrum.png", "c=5_m=3_f0=1000_spectrum.png" %}
    

### How to control the brightness of FM spectra?

The brightness of a sound is typically associated with the presence of high frequencies. In FM synthesis, we can control the center of the sound’s spectrum with the carrier frequency, the spacing of the partials with the modulator frequency, and the bandwidth of the spectrum with the modulation frequency and the modulation index. If we want to change the bandwidth of the spectrum (resulting in a change in brightness) without changing the pitch, we can simply alter the modulation index.

Specifically, John Chowning computed the bandwidth of a simple FM sound as [Chowning1973]

$$
\begin{equation}
BW_\text{FM} \approx 2 f_M(I + 1),
\end{equation}
$$

where $f_M$ is the modulation frequency in Hz and $I$ is the modulation index. Here, the bandwidth means a frequency range in Hz that encompasses not all but the most significant partials.

Let’s look at some examples using $f_C = 1000 \text{ Hz}$ and $f_M = 200 \text{ Hz}.$

Let’s set $I=1$. Here’s the resulting sound.

{% render 'embed-audio.html', src: "/assets/wav/posts/synthesis/2025-03-01-fm-synthesis/c_5_m_1_f0_200_I_1.flac" %}

And here’s its spectrum.

{% image "assets/img/posts/synthesis/2025-03-01-fm-synthesis/c5_m1_f0200_I1_spectrum.png", "c=5_m=1_f0=200_I=1_spectrum.png" %}

As you can see, its bandwidth is 800 Hz. Although there are partials outside of this range, they are not significant.

Here, $I=2$.

{% render 'embed-audio.html', src: "/assets/wav/posts/synthesis/2025-03-01-fm-synthesis/c_5_m_1_f0_200_I_2.flac" %}

{% image "assets/img/posts/synthesis/2025-03-01-fm-synthesis/c5_m1_f0200_I2_spectrum.png", "c=5_m=1_f0=200_I=2_spectrum.png" %}

As you can hear and see, the spectrum got wider and as a result, it sounds brighter.

Here, $I=3$.

{% render 'embed-audio.html', src: "/assets/wav/posts/synthesis/2025-03-01-fm-synthesis/c_5_m_1_f0_200_I_3.flac" %}

{% image "assets/img/posts/synthesis/2025-03-01-fm-synthesis/c5_m1_f0200_I3_spectrum.png", "c=5_m=1_f0=200_I=3_spectrum.png" %}

Here, $I=4$.

{% render 'embed-audio.html', src: "/assets/wav/posts/synthesis/2025-03-01-fm-synthesis/c_5_m_1_f0_200_I_4.flac" %}

{% image "assets/img/posts/synthesis/2025-03-01-fm-synthesis/c5_m1_f0200_I4_spectrum.png", "c=5_m=1_f0=200_I=4_spectrum.png" %}

As you can see, the spectrum got so wide that it expanded over to negative frequencies which means that these frequencies got reflected back and hence the spectrum is no longer symmetric. However, it is still harmonic because just the amplitudes of the partials changed after reflection not their positions.

Here, $I=5$.

{% render 'embed-audio.html', src: "/assets/wav/posts/synthesis/2025-03-01-fm-synthesis/c_5_m_1_f0_200_I_5.flac" %}

{% image "assets/img/posts/synthesis/2025-03-01-fm-synthesis/c5_m1_f0200_I5_spectrum.png", "c=5_m=1_f0=200_I=5_spectrum.png" %}

This spectrum is clearly the brightest and it’s not symmetric. We could go even further than this but I’d leave it for your experimentation 🙂

### FM Efficiency

At this point, I would like to point out how efficient in generating rich sounds FM is. With just two table lookups (to get the value of the sine) we are able to generate quite elaborate spectra. With a few simple controls, we are able to change it in a significant but meaningful way. This low computational effort paired with powerful sonics was why FM was one of the first synthesis techniques (if not the first) to be successfully implemented with digital electronics.

TODO: Add link to wavetable synthesis article

### How to control the partials’ amplitudes? Bessel functions

In the examples so far, we could see that the FM spectrum definitely has some pattern to it. Can we accurately predict what the partials’ amplitudes will be given the parameters?

It turns out that we can. As the literature reports [Chowning1973, DePoli, Pluta2019], we can write out the PM equation (Equation 10) as

$$
\begin{equation}
s_\text{PM} (t) = \sum \limits_{k=-\infty}^{\infty} J_k(I)\sin|2 \pi ((f_C + k f_M)t)|,
\end{equation}
$$

where

- $\sum$ is the sum operator; in the above equation, it is an infinite sum where each summand corresponds to one integer value given to $k$; here, each value of $k$ corresponds to one partial,
- $J_k(I)$ are the Bessel function of the first kind of order $k$ whose argument is the modulation index $I$,
- $|\cdot|$ denotes the absolute value,
- $f_C$ is the carrier frequency in Hz,
- $f_M$ is the modulator frequency in Hz,
- $t$ is time in seconds.

Bessel functions are a very important concept in mathematics. They appear in the solution of the wave equation: the basic equation of acoustics.

Here’s how the Bessel functions of the first kind look for orders from 0 to 3.

{% image "assets/img/posts/synthesis/2025-03-01-fm-synthesis/bessel_functions_1st_kind.png", "bessel_functions_1st_kind" %}

These are sine-like functions that are getting damped the higher the absolute value of the argument. You can also observe that Bessel functions of even orders are even (symmetrical with respect to the $y$-axis) and Bessel functions of odd orders are odd (symmetrical with respect to the origin of the $xy$-plane).

What is more important, Bessel functions cross the value of 0 for many values of the argument $I$. It means that with for some modulation index values, some partials will have amplitude 0. As you remember, when we increase the modulation index, the spectrum gets wider but some partials may temporarily disappear.

It’s hard to get a feeling for the meaning of the partials’ amplitudes equation (Equation 15) without any visuals. Thus, here you can see a plot of how the spectrum changes if we vary the modulation index $I$ value in the $[0, 20]$ range [Pluta2019].

{% image "assets/img/posts/synthesis/2025-03-01-fm-synthesis/bessel_functions_3d.png", "bessel_functions_3d" %}

How to read this plot? Say you want to see how the spectrum will look for a particular value of $I$, for example, 10. Then, find 10 on the $I$ axis on the right and mentally cross-sect the 3-dimensional spectrum along the partials’ axis. This cross-section is your sound’s magnitude spectrum at the modulation index 10.

The above plot gives you the full insight into the spectrum of FM sounds. You can go back to it over and over again to discover more and more properties of this spectrum. As you can see, it is completely frequency-independent; for each fundamental frequency, the partials behave identically. Of course, this plot does not take reflected frequencies into account but you can visualize them yourself 😉

## Presenting FM algorithm visually

TODO, p. 165 in [Pluta2019]

## Example FM sounds

## Extensions of simple FM

What we have discussed so far is the “simple FM”, i.e., we have one sine carrier and one sine modulator.

Simple FM can be extended in various ways to create even more complex sounds [Pluta2019]:

1. We can add feedback, where the output of an FM instrument modulates the modulator. We can do this for any setup of carriers and modulators but the most popular approaches use one, two, or three oscillators within the feedback loop.
2. We can add multiple carriers modulated by the same oscillator. This is called multiple-carrier FM (MCFM). It can be used to create formants in the sound spectrum.
3. We can have non-sine carriers or modulators. However, non sinusoid modulators can result in very dense spectra quite quickly, so we should be careful when using harmonically rich modulators [DodgeJerse].
4. We can add multiple modulators, parallel or serial, that modulate one carrier. This is called multiple-modulator FM (MMFM). This technique increases the number of partials in the output spectrum. Again, multiple non-sine modulators make little sense because the spectrum gets too dense [DodgeJerse].
5. We can use oscillators with exponential control which emulates analog gear. This is called exponential FM. This approach is used in Virtual Analog applications.
6. We can combine two or more FM algorithms in parallel or in serial. However, this may get very complicated to control very quickly.
7. We can add envelope generators (EGs) to control various FM parameters. For example, an envelope generator on a modulation index can create a very naturally sounding effect of a brighter timbre after the initial transient that gets darker and darker the longer the sound is played (or a key is held).
8. Phase distortion (PD) synthesis is another spin on phase modulation. In this technique, the modulator’s frequency is fixed to be either the same as the carrier or to be a multiplicity of the carrier frequency. Moreover, various modulator waveforms are used, for example, a triangle waveform. A picture sometimes says a thousand words, so [here’s a very short but very good explanation of phase distortion synthesis](https://electricdruid.net/phase-distortion-synthesis/) (accessed February 10, 2024). [Oli Larkin, whom I interviewed in the episode 15 of the WolfTalk podcast](https://thewolfsound.com/talk015/), is well known for his implementations of Casio’s phase distortion emulations.

The discussion of all these extensions is beyond the scope of this already quite long article. Should they be discussed in more detail in future articles? Let me know in the comments!

## Summary

In this comprehensive article, you’ve learned about the frequency modulation (FM) and phase modulation (PM) synthesis. You’ve learned how these two are different, how their spectra look and how to control these spectra.

You’ve also learned what are Bessel functions and how the partials in FM synthesis follow the Bessel functions in their amplitude with increasing modulation index.

You’ve learned what is the modulation index and how to use it to control the bandwidth of FM spectra.

We’ve looked at how to depict various FM setups and we’ve also listened to a few sounds generated with FM.

Finally, we have mentioned various extensions to the simple FM technique.

In the future articles, we will look into how to implement the PM synthesis technique using various programming languages. So look out for those!

If you want to become an audio developer today, check out my free Audio Developer Checklist. It lists every bit and piece of knowledge I believe is necessary to become a full-fledged audio programmer and be able to create software synths, for example, with FM synthesis.

TODO: Make add link to checklist

TODO: Make links relative

TODO: Create bibliography

## Bibliography

[Chowning1973] **Original FM paper by John Chowning**: J. M. Chowning. The Synthesis of Complex Audio Spectra by Means of Frequency Modulation. J. Audio Eng. Soc. 21, 7, 1973 [[PDF](https://web.eecs.umich.edu/~fessler/course/100/misc/chowning-73-tso.pdf)]

[SOS2000] Gordon Reid, An Introduction To Frequency Modulation, Synth Secrets, Sound on Sound https://www.soundonsound.com/techniques/introduction-frequency-modulation (accessed March 5, 2025)

[Wikipedia] [Frequency modulation synthesis, Wikipedia](https://en.wikipedia.org/wiki/Frequency_modulation_synthesis) (accessed March 5, 2025)
