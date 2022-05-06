---
title: "Allpass-Based Lowpass and Highpass Filters"
description: "Learn how to design and implement easily controllable and efficient lowpass and highpass filters."
date: 2022-05-08
author: Jan Wilczek
layout: post
images: /assets/img/posts/fx/2022-05-08-allpass-based-lowpass-and-highpass-filters/
images_parametric_eq: /assets/img/posts/fx/2021-11-26-parametric-eq-design/
# background: /assets/img/posts/fx/2022-05-08-allpass-based-lowpass-and-highpass-filters/Thumbnail.webp
categories:
  - Digital Signal Processing
  - Audio FX
tags:
  - filtering 
  - effects
  - Python
discussion_id: 2022-05-08-allpass-based-lowpass-and-highpass-filters
---
Control the cutoff with just one coefficient!

{% katexmm %}
{% capture _ %}{% increment equationId20211126  %}{% endcapture %}
{% capture _ %}{% increment figureId20211126  %}{% endcapture %}

You have probably seen it: a low-pass filter digital audio workstation (DAW) plugin.

It could have had a roll-off and a resonance control knob or slider.

But it definitely had the **cutoff frequency control**.

If you learned a little bit about digital signal processing (DSP), you may have come across formulas for different types of filters. However, these formulas typically require to have all their coefficients recalculated as soon as the cutoff frequency changes. That means that their real-time control is inefficient, computationally speaking.

*How to design and implement a lowpass or a highpass filter, where adjusting the cutoff frequency requires a recalculation of just one parameter?*

That is the topic of this article 🙂

<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6611455743195468"
     crossorigin="anonymous"></script><ins class="adsbygoogle"
     style="display:block; text-align:center;"
     data-ad-layout="in-article"
     data-ad-format="fluid"
     data-ad-client="ca-pub-6611455743195468"
     data-ad-slot="7289385396"></ins><script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>

Let's start with the basics.

## Lowpass Filter

For the purpose of this article, we'll define a lowpass filter as a filter that attenuates frequencies above a certain frequency, called the *cutoff frequency*.

The cutoff frequency is typically defined as the frequency at which the attenuation is already 3 dB.

The frequencies below the cutoff frequency aren't affected by it.

The amplitude response (how each frequency is attenuated at the output of the filter) of a lowpass filter is shown in Figure 1.

![]({{ page.images_parametric_eq | absolute_url | append: "/LowPass.webp"}}){: width="70%" alt="Low-pass filter amplitude response."}
_Figure {% increment figureId20211126  %}. Low-pass filter amplitude response._

## Highpass Filter

Contrary to a lowpass filter, a highpass filter attenuates all frequencies below the cutoff frequency.

The amplitude response of a highpass filter is shown in Figure 2.

![]({{ page.images_parametric_eq | absolute_url | append: "/HighPass.webp"}}){: width="70%" alt="High-pass filter amplitude response."}
_Figure {% increment figureId20211126  %}. High-pass filter amplitude response._

## The Need for a Simple Control-to-Coefficients Mapping

Let's recap a "traditional" method of designing an IIR lowpass filter:

1. Design the analog prototype.
2. Digitize it with the bilinear transform.

For example, in the [bilinear transform tutorial]({% post_url fx/2022-01-15-bilinear-transform %}), we digitized the Butterworth lowpass of order 2. The resulting transfer function formula was

$$H_2(z) = \frac{W^2 + 2W^2 z^{-1} + W^2z^{-2}}{1 + W \sqrt{2} + W^2 + 2(W^2 - 1)z^{-1} + (W^2 - W\sqrt{2} + 1)z^{-2}}, \quad ({% increment equationId20220115 %})$$

where $W = \tan(\omega_\text{c} T / 2)$ and $\omega_\text{c}$ is the desired cutoff frequency of the digital filter in radians per second.

Note that if we change the cutoff frequency $\omega_\text{c}$, we need to calculate 6 filter coefficients!

(A reminder: a filter coefficient is a scalar at each power of the $z$ variable in the numerator and the denominator.)

If we wanted to control the cutoff freqency in real time, for example, during a live performance, or using an amplitude envelope, the computational overhead could be troublesome.

Can we have a simple mapping: 1 filter control change requires 1 coefficient change?

That is the promise of allpass-based parametric filters.

To understand them, we first need to recap a few facts about the allpass filter.

## Allpass filter revisited

* formula for c comes from the bilinear transform

## Phase Cancellation

## Allpass-Based Lowpass Filter

* block diagram
* implementation in Python
* transfer function

## Allpass-Based Highpass Filter

* block diagram
* implementation in Python
* transfer function

{% endkatexmm %}

## Bibliography

[DAFX]