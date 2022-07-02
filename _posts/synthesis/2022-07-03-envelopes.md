---
title: "Envelopes in Sound Synthesis: The Ultimate Guide"
description: "TODO"
date: 2022-07-03
author: Jan Wilczek
layout: post
images: /assets/img/posts/synthesis/2022-07-03-envelopes/
# background: /assets/img/posts/synthesis/2022-07-03-envelopes/Thumbnail.webp
audio_examples: /assets/wav/posts/synthesis/2022-07-03-envelopes/
categories:
  - Sound Synthesis
tags:
  - sound wave
  - maths
  - waveform
  - sampling (sound generation)
discussion_id: 2022-07-03-envelopes
---
Everything you need for coding your own synthesizer.

{% capture _ %}{% increment figureId20220703  %}{% endcapture %}

If you have ever used a synthesizer, you definitely stumbled upon an **envelope**.

Sometimes it is referred to as **contour** or simply **ADSR** (the most popular type of envelope).

These synthesizer elements help the musicians and sound designers to effortlessly make the sound more lively, more interesting. They achieve it via automatic control of:

* sound's amplitude (volume),
* cutoff frequency of a low-pass filter,
* oscillator frequency.

In this article, you will learn what is an envelope, all the types of envelopes, and what to consider when implementing them.

## What Is An Envelope?

From the digital signal processing (DSP) perspective, **an envelope is a curve that outlines the extremes of a signal** [Pluta2019].

As such, it relates to the _analysis_ of the signal: we have a waveform, we connect its peaks and obtain an envelope.

<!-- TODO: Plot envelope of a sine -->

From the sound synthesis perspective, **an envelope is a curve that controls a certain parameter of the generated signal.**

As such, it relates to the _synthesis_ of the signal: we want to generate a certain waveform and, thus, we apply an envelope to it; an envelope is a control data source [Pluta2019]

According to the [Merriam-Webster dictionary](https://www.merriam-webster.com/dictionary/envelop), _to envelop_ means "to enclose or enfold completely with or as if with a covering." So an envelope is a curve that is _enclosing_ the signal.

In this article, we consider the sound synthesis perspective of the envelope: we use it to control some parameter of the generated sound.

## What Can an Envelope Control?

In principle, an envelope can control just about anything.

In sound synthesis, it is typically used to control the amplitude, cutoff frequency of a low-pass filter, or the frequency of the generated signal itself.

### Amplitude Envelope

An **amplitude envelope** is the most commonly found envelope application. Why?

Because they are everywhere!

A fade-in and a fade-out of a song (also after pausing or playing your YouTube video) are forms of an envelope. But the origins of the amplitude envelope are far more ancient.

Originally, amplitude envelopes appeared with the invention of the first musical instruments. Every one of them has a characteristic amplitude envelope.

Plucking a string has a sharp attack and an automatic release.

Hitting a key on the piano starts with an increasing volume, which then decays to a certain level, which is slowly fading until the key is released and then the sound fades out.

On a more fine-grained level, each of the partials in the amplitude spectrum of an instrument sound can have its own amplitude envelope.

Synthesizers tried to mimic the behavior of natural instruments and so they introduced amplitude envelopes, somewhat simplified with respect to the naturally occurring ones.

<!-- TODO: Sound example -->

But this single change sufficed to make the synthesizers sound more natural. But to make it even more natural, another envelope was needed...

### Cutoff Envelope

The **cutoff envelope** controls the cutoff of a low-pass filter.

When we hit a piano key, its timbre is bright at first (high energy in the high-frequency partials in the amplitude spectrum) and then softens (low energy in the high-frequency partials).

Synthesizers imitate this by an envelope of the cutoff of a low-pass filter.

When we hit a synthesizer key, the cutoff frequency rises, the sound becomes brighter and brighter. After some time (or after releasing the key), the sound becomes darker as the cutoff lowers and high-frequency components are more attenuated.

<!-- TODO: Sound example -->

I specifically mention cutoff envelope not cutoff frequency envelope. That is because we typically want the cutoff frequency to increase with the pitch of the key that we hit. Otherwise, high notes could not be audible.

The cutoff envelope controls what percentage of the cutoff frequency should be set. Typically, the value of 1 (100%) means that the cutoff frequency corresponds to the value set by the user.

Sometimes the synthesizers allow the user to control the **contour amount**, i.e., the range of cutoff change. For example, we may want to have the cutoff change only between 80% and 100% because starting the envelope always from 0% tends to sound too repetitive.

### Frequency Envelope

In some sound design scenarios, I can imagine envelopes controlling the frequency of an oscillator.

In these cases, the sound's pitch would change over time according to the envelope.

As this is very specialized and does not concern traditional sound synthesizers (with a MIDI-based control), I won't discuss it here in detail.

## What Are Envelope Generators (EGs)?

In analog sound synthesis, **an envelope generator (EG) is a source of the control signal (the envelope).**

Therefore, on module connection diagrams, you can often see EG blocks connected to VCA blocks (voltage-controlled amplifiers), or VCF blocks (voltage-controlled filters), or (in rare cases) to VCO blocks (voltage-controlled oscillators).

<!-- TODO: Sample diagram -->

The connection between any module and an EG means that this EG is controlling a parameter of that module. For VCAs, that's amplitude, for VCFs, it's cutoff, and for VCOs, it's frequency.

Nowadays, EG blocks are also used to depict the interconnections of digital modules but their meaning is the same: they are sources of a control signal, an envelope.

## Applications of Envelopes

Amplitude and cutoff envelopes are used for various purposes. For example, to

* make the sound more lively,
* make the sound more natural by imitating real instruments' envelopes,
* make the sound less natural with obscure envelopes,
* avoid clicks and other artifacts (e.g., with fade-in and fade-out).
  
Some more specialized applications of envelopes in sound synthesis include

* amplitude envelopes of partials in additive synthesis,
* envelope of the amplitude and the cutoff frequency in subtractive synthesis,
* frequency envelope of an oscillator for sound design purposes.

## Types of Envelope Segments

Envelopes consist of segments (ramps). For example, the most popular Attack-Decay-Sustain-Release (ADSR) envelope consists of 4 segments: Attack, Decay, Sustain, and Release.

<!-- TODO: ADSR image -->

The segments are crude approximations to the natural envelopes but they represent a good trade-off between the quality of the result and the complexity of control.

The following is a comprehensive (to my best knowledge) list of envelope segment types:

* Delay: the amount of time between the _note-on_ event and the start of the attack segment. Delaying the appearance of sound after a key-press is especially important in ambient music, where the musician can use this time to adjust the timbre parameters. We can control the length of this delay.
* Attack: the initial portion of every envelope after a _note-on_ event. In this segment the value is rising from 0 (minimum envelope value) to 1 (maximum envelope value). When we "control the attack" we change the duration of this segment.
* Hold: a segment where the envelope value is 1; by controlling its length, we adjust how long will the controlled parameter be at its peak value.
* Decay: the segment where the envelope falls from the peak value to the initial sustain value. The value change is faster (more dynamic) than in the sustain (or "decay 2") phase. We can control its length.
* Sustain: the segment where the envelope maintains a constant level until a _note-off_ event. We set the value of this level but its length is controlled by the performer.
* Release: the final segment of any envelope, where the value falls from its current value to 0.

## Linear or Exponential?

A very important consideration when implementing any envelope is how its value should change.

To be exact, should the amplitude increase linearly or exponentially (linearly on the logarithmic scale)? Below is a comparison of these two approaches:

![]({{ page.images | absolute_url | append: "linear_vs_exponential.webp" }}){: alt="" }
_Figure {% increment figureId20220703  %}. ._

The caveat here is that we perceive the exponential change as a linear one. To hear this, listen to these two examples.

Each one plays a sine at 220 Hz.

This one has the linear attack envelope (left in Figure ???).

{% include embed-audio.html src="assets/wav/posts/synthesis/2022-07-03-envelopes/linear.flac" %}

This one has the exponential attack envelope (right in Figure ???).

{% include embed-audio.html src="assets/wav/posts/synthesis/2022-07-03-envelopes/exponential.flac" %}

Which change sounds more "linearly" to you?

For me, the exponential envelope.

In the linear envelope case, I can hear the sound instantaneously and then it becomes kind of louder whereas in the exponential case, I can hear a steady increase in volume.

After learning the building blocks of envelopes, now it is time to see what types of envelope are out there.

## The Catalog of Envelopes

Below, I listed all types of envelopes that exist based on [Pluta2019, Russ].

Their visualizations were created by me but I was heavily inspired by those great books so they should take all the credit.

### AD

![]({{ page.images | absolute_url | append: "AD.webp" }}){: alt="" }
_Figure {% increment figureId20220703  %}. ._

### AR

![]({{ page.images | absolute_url | append: "AR.webp" }}){: alt="" }
_Figure {% increment figureId20220703  %}. ._


### ADR

![]({{ page.images | absolute_url | append: "ADR.webp" }}){: alt="" }
_Figure {% increment figureId20220703  %}. ._

### ADS

![]({{ page.images | absolute_url | append: "ADS.webp" }}){: alt="" }
_Figure {% increment figureId20220703  %}. ._

![]({{ page.images | absolute_url | append: "ADSD.webp" }}){: alt="" }
_Figure {% increment figureId20220703  %}. ._

### ADSR

![]({{ page.images | absolute_url | append: "ADSR.webp" }}){: alt="" }
_Figure {% increment figureId20220703  %}. ._

* Sound example

### AHDSR

![]({{ page.images | absolute_url | append: "AHDSR.webp" }}){: alt="" }
_Figure {% increment figureId20220703  %}. ._

### ADBDR

![]({{ page.images | absolute_url | append: "ADBDR.webp" }}){: alt="" }
_Figure {% increment figureId20220703  %}. ._

* Sound example

### Arbitrary

## How to code envelopes

[Pluta2019]
[Russ]
