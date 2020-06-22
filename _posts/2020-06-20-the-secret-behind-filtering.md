---
title: "Convolution: The secret behind filtering"
date: 2020-06-20
author: Jan Wilczek
layout: post
permalink: /convolution-secret-behind-filtering/
background:
categories:
 - DSP
tags:
 - convolution
 - filtering
 - maths
 - dsp
---
Why does filtering work? What enables us to enhance the bass in our audio players?

{% katexmm %}

There is one operation that stands behind it all: **convolution**.

In order to fully master filtering, be it **finite impulse response (FIR)** or **infinite impulse response (IIR)** filtering, one needs to understand the definition, derivation and the properties of the convolution operation very well. That will be the topic of this and a few following articles.

We are going to dig **deep** into the convolution and we will get to know it so well, that it won't surprise us any more and we'll be able to recognize it from afar.

This article will outline the mathematical definition, give You an intuition behind it and introduce some basic properties along with their proofs (told You it's going to go deep).

Are You ready?

# Definition

In its simplest form the convolution between two discrete signals $x[n]$ and $h[n]$ can be expressed as an **infinite sum**:

$$ x[n] \ast h[n] = \sum_{k=-\infty}^{\infty} x[k] h[n - k] = y[n] $$.

Whoa, what's happened here? Under the sum we have the two signals, but the second one is not only **shifted in time by $n$**, but also **time-reversed**!

{% endkatexmm %}