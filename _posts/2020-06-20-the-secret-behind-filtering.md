---
title: "Convolution: The secret behind filtering"
date: 2020-06-20
author: Jan Wilczek
layout: post
permalink: /convolution-the-secret-behind-filtering/
images: assets/img/posts/2020-06-20-the-secret-behind-filtering
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

$$ x[n] \ast h[n] = \sum_{k=-\infty}^{\infty} x[k] h[n - k] = y[n]. $$

Whoa, what's happened here? Under the sum we have the two signals, but the second one is not only **shifted in time by $n$**, but also **time-reversed**!

# Intuition

## Filtering

Let's consider the above equation with $h[n]$ denoting filter's (or any linear time-invariant (LTI) system) impulse response and $x[n]$ as this filter's input signal. From signal processing we know, that any LTI system is completely specified by its impulse response.

If we denote the output of the filter by $y[n]$ we may look at the output as a weighted sum of filter's impulse responses. How?

Consider $n=0$. At the output we get

$$y[0] = \sum_{k=-\infty}^{\infty} x[k] h[0 - k] = \sum_{k=-\infty}^{\infty} x[k] h[- k] = x[0] h[0],$$ because $h[n] = 0$ and $x[n]=0$ for all $n < 0$. What do we get for $n=1$?

$$y[1] = \sum_{k=-\infty}^{\infty} x[k] h[1 - k] = x[0]h[1] + x[1]h[0].$$ As you can see, x[0] has moved "further down the road" (further into the filter's buffer) and now constitutes the weight for $h[1]$ from filter's impulse response. At the same time $x[1]$ enters the buffer and (as $x[0]$ previously) weights the $h[0]$. The operation repeats for every following input sample. $x[0]$ stops weighting filter's impulse response when it has weighted the last one of them (unless it is an IIR filter; it then weights the filter's impulse response infinitely).

## Another view

We can also look at that operation from a different perspective. What if we fix $k$? In this case it describes the behaviour of the system if only input sample $x[k]$ was given:

$$ y_k[n] = x[k]h[n-k].$$

The above equation basically says, that once $x[k]$ enters the filter, it will weigh its entire impulse response delayed by $k$ samples w.r.t $n$. We then just have to sum up over all possible $k$ to conclude, that $y[n]$ is just filter's impulse response, delayed and weighted by $x[n]$.

This may all get a little bit confusing at this moment, so let's look at an example, shall we?

# Example

Let's consider the following signal $x[n]$:

![]({{ page.images | absolute_url | append: "/x.png"}})

and filter's impulse response $h[n]$:

![]({{ page.images | absolute_url | append: "/h.png"}})

The result of their convolution is the following signal $y[n]$ (filter's output):

![]({{ page.images | absolute_url | append: "/y.png"}})

Not very meaningful, is it? The only thing that we can observe is that output's length is the sum of input's and filter's lengths minus one.

Let's try some color coding. We can depict each of $x[n]$'s samples in a different color:

![]({{ page.images | absolute_url | append: "/x_single.png"}})

We can now examine the impact of particular samples on the filter's output. What would happen if only  blue $x[0]$ entered the filter?

![]({{ page.images | absolute_url | append: "/h_single_0.png"}})

We can see, that the entire impulse response of the filter got scaled by $x[0]$ which in this case is equal to $0.1$.

Now, let's imagine, that only second sample, namely orange $x[1]$, entered the filter. What could we observe at the output?

![]({{ page.images | absolute_url | append: "/h_single_1.png"}})

Notice that at $n=0$ the filter's output is $0$, because at that time $x[1]$ has not yet entered the filter. But from $n=1$ onwards we get again filter's impulse response scaled by the newly entering sample.

The same thing happens for green $x[2]$ and red $x[3]$:
![]({{ page.images | absolute_url | append: "/h_single_2.png"}})
![]({{ page.images | absolute_url | append: "/h_single_3.png"}})

Viewing all these "partial" responses on a plot shows the impact of each individual input sample over time:
![]({{ page.images | absolute_url | append: "/h_superposed.png"}})

Summing them all up (as if summing over $k$ in the convolution formula) we obtain:
![]({{ page.images | absolute_url | append: "/h_single_0.png"}})
what corresponds to the $y[n]$ signal above.

# Continuous convolution
Convolution is defined for continuous signals as well (notice the conventional use of round brackets for non-discrete functions):

$$ x(t) \ast h(t) = \int \limits_{-\infty}^{\infty} x(\tau) h(t - \tau) d\tau $$

Although it may not be as intuitive in interpretation as the discrete convolution, nevertheless, we could try to imagine the continuous case as an infinitely densely sampled discrete signal (so that sum over discrete samples changes to integral over continuous functions). But keep in mind that it is only an intuitive view!

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

{% endkatexmm %}