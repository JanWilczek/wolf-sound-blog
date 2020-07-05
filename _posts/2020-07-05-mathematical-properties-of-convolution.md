---
title: "Mathematical properties of convolution"
date: 2020-07-05
author: Jan Wilczek
layout: post
permalink: /mathematical-properties-of-convolution/
background:
categories:
 - DSP
tags:
 - convolution
 - filtering
 - maths
 - dsp
---
Inspecting mathematical properties of convolution leads us to interesting conclusions regarding digital signal processing.

{% katexmm %}

In the [previous article]({{"/convolution-the-secret-behind-filtering/" | absoulte_url }}) we discussed the definition of the convolution operation. Now it is time to look more closely at its mathematical properties in the context of digital signal processing.

## Recap 
Let us recap the definition of the discrete convolution:
$$ x[n] \ast h[n] = \sum_{k=-\infty}^{\infty} x[k] h[n - k] = y[n]. $$
Convolution in the continuous domain is defined as follows:
$$ x(t) \ast h(t) = \int \limits_{-\infty}^{\infty} x(\tau) h(t - \tau) d\tau $$

In the following considerations we assume, that $x$ is some signal (e.g., audio signal) and $h$, $h_1$, $h_2$ are arbitrary filters' impulse responses.

# Properties of convolution
In this article the following properties of the convolution are discussed:
 * commutativity: $x \ast h = h \ast x$
 * associativity: $x \ast (h_1 \ast h_2) = (x \ast h_1) \ast h_2$
 * linearity:  
 $(\alpha x_1 + \beta x_2) \ast h = \alpha (x_1\ast h) + \beta (x_2 \ast h)$
*$x$ and $h$ here can be both discrete or both continuous.*

Their formulations and proofs are provided for the discrete as well as continuous cases.

## Commutativity
Commutativity of an operation means that its operands can be exchanged without affecting the result:

$$ x \ast h = h \ast x $$

It has a very interesting interpretation in the context of signal processing: it turns out we can interpret system's impact on the signal as signal's impact on the system's impulse response. In particular, the filtering operation can be viewed as if the input signal was filtering the filter's impulse response. As we already seen, it is completely true: the output of a filter is a sum of its repeatedly scaled and delayed (=filtered) impulse response.

### Proof for the discrete case
$$ x[n] \ast h[n] = \sum_{k=-\infty}^{\infty} x[k] h[n - k] = | k' = n-k; k = n - k'| \\ =\sum_{k'=-\infty}^{\infty} x[n-k'] h[k'] = \sum_{k'=-\infty}^{\infty} h]k'] x[n-k'] = h[n] \ast x[n]. $$

### Proof for the continuous case
$$ x(t) \ast h(t) = \int \limits_{-\infty}^{\infty} x(\tau) h(t - \tau) d\tau \\ = | \tau' = t - \tau; \tau = t - \tau'; d\tau'| \\= -d\tau | = - \int \limits_{\infty}^{-\infty} x(t - \tau') h(\tau') d\tau' = \int \limits_{-\infty}^{\infty} h(\tau') x(t - \tau') d\tau' \\= h(t) \ast x(t).$$

*Note the inversion of boundaries and the resulting change of the sign.*

## Associativity
Associativity of an operation ensures that we can calculate the results of this operation in any order when given a couple of them in series:
$$x \ast (h_1 \ast h_2) = (x \ast h_1) \ast h_2$$

A practical interpretation of this would be that a series of filters applied one after another is an equivalent system to a convolution of their impulse responses. So a superposition of filters is a convolution of their impulse responses.

### Proof for the discrete case
$$x[n] \ast (h_1[n] \ast h_2[n]) = x[n] \ast \sum_{k=-\infty}^{\infty} h_2[k]h_1[n-k] \\= \sum_{l=-\infty}^{\infty}\sum_{k=-\infty}^{\infty} x[l]h_2[k]h_1[n-l-k] \\=  \sum_{k=-\infty}^{\infty} h_2[k] \sum_{l=-\infty}^{\infty} x[l]h_1[n-k-l] \\=   \sum_{k=-\infty}^{\infty} h_2[k] (x \ast h_1)[n-k] \\= ((x \ast h_1) \ast h_2) [n] \\= (x[n] \ast h_1[n]) \ast h_2[n]$$

### Proof for the continuous case
$$x(t) \ast (h_1(t) \ast h_2(t)) \\= x(t) \ast \int \limits_{-\infty}^{\infty} h_2(\tau) h_1(t - \tau) d\tau \\= \int \limits_{-\infty}^{\infty} x(\psi) \int \limits_{-\infty}^{\infty} h_2(\tau) h_1(t - \psi - \tau) d\tau d\psi \\= \int \limits_{-\infty}^{\infty} h_2(\tau) \int \limits_{-\infty}^{\infty} x(\psi)h_1(t - \tau - \psi) d \psi d \tau \\= \int \limits_{-\infty}^{\infty} h_2(\tau) (x \ast h_1)(t - \tau) d\tau = ((x \ast h_1) \ast h_2)(t) = (x(t) \ast h_1(t)) \ast h_2(t).$$

## Linearity
The last property to be examined and proved is the linearity property of convolution:
$$ a(x \ast (h_1 + h_2)) = (ax \ast h_1) + (ax \ast h_2),$$
which consists of *distributivity*:
$$ x \ast (h_1 + h_2) = x \ast h_1 + x \ast h_2$$
and *associativity with scalar multiplication*:
$$ a (x \ast h) = (ax) \ast h.$$

Distributivity means that a signal filtered with *superposition* (a sum) of filters is equivalent to summing the output of the filters if the signal has been filtered by them independently. Summing in digital signal processing corresponds to joining two independent paths of processing. Thanks to this property we can filter the signal only once (with filters' superposition) rather than filtering the signal with each filter separately and only then summing the filtered outputs. As you can imagine, it can be a significant optimization advantage.

Associativity means simply that it doesn't matter if we scale the signal before or after the filtering operation: the resulting signal will be the same.

### Proof for the discrete case
$$a(x[n] \ast (h_1[n] + h_2[n])) \\= a \sum_{k=-\infty}^{\infty} x[k] (h_1[n-k] + h_2[n-k]) \\= \sum_{k=-\infty}^{\infty} ax[k]h_1[n-k] + ax[k]h_2[n-k] \\= \sum_{k=-\infty}^{\infty} ax[k]h_1[n-k] + \sum_{k=-\infty}^{\infty} ax[k]h_2[n-k] \\= (ax[n]) \ast h_1[n] + (ax[n]) \ast h_2[n].$$

### Proof for the continuous case
$$a(x(t) \ast (h1(t) + h2(t))) = a \int \limits_{-\infty}^{\infty} x(\tau) (h_1(t - \tau) + h_2(t - \tau)) d\tau \\= \int \limits_{-\infty}^{\infty} (ax(\tau) h_1(t - \tau) + ax(\tau)h_2(t - \tau))d \tau \\= \int \limits_{-\infty}^{\infty} a x(\tau) h_1(t - \tau) d\tau + \int \limits_{-\infty}^{\infty} ax(\tau) h_2(t - \tau) d\tau \\= (ax(t)) \ast h_1(t) + (ax(t)) \ast h_2(t).$$

# Summary

In this article we have reviewed the most important mathematical properties of convolution, which are:
 * commutativity,
 * associativity,
 * linearity.

 These properties will prove themselves useful in the future considerations of convolution.

{% endkatexmm %}
