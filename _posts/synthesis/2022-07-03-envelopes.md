---
title: "Envelopes in Sound Synthesis"
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

{% capture _ %}{% increment figureId20220703  %}{% endcapture %}

* Why envelopes?
  * make the sound more lively
  * make the sound more instrument-like; envelopes imitate real instruments' envelopes
  * fade-in and fade-out are also envelopes
  * applications:
    * envelopes of partials in additive synthesis
    * envelope of the amplitude and the cutoff frequency in subtractive synthesis
    * extreme case: frequency envelope of an oscillator
* What is an envelope?
  * English: to envelope something
  * DSP perspective
    * An envelope is a curve that outlines the extremes of a signal [Pluta2019]. (analysis)
  * sound synthesis perspective
    * A control data source: a curve that controls something (synthesis)
* What is controlled?
  * amplitude
  * cutoff
* EGs
* Envelope segments (ramps)
  * Delay
  * Attack
  * Hold
  * Decay
  * Sustain
  * Release
* Types of an envelope with sound examples

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

* Linear vs exponential change
* How to code envelopes

[Pluta2019]
[Russ]
