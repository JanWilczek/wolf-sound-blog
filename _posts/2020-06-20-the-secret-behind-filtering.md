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

This article will outline the mathematical definition and give You some intuition behind it. In the next article we will introduce some basic properties along with their proofs (told You it's going to go deep).

Are You ready?

# Definition

In its simplest form the convolution between two discrete signals $x[n]$ and $h[n]$ can be expressed as an **infinite sum**:

$$ x[n] \ast h[n] = \sum_{k=-\infty}^{\infty} x[k] h[n - k] = y[n], \quad n \in \mathbb{Z}. $$

Whoa, what's happened here? Under the sum we have the two signals, but the second one is not only **shifted in time by $n$**, but also **time-reversed**!

### Important assumptions

In order to make this discussion feasible, we must enforce $x[n]$ and $h[n]$ to have _finite energy_. A signal $s[n]$ is said to have finite energy, if

$$ \sum_{n=-\infty}^{\infty} s^2[n] < \infty, $$

i. e., $s[n]$ is square-summable.

Additionally, we also assume that all considered signals are 0 for negative time indices, i. e., $s[n] = 0 \quad \forall n < 0$.

# Intuition

In order to understand the intuition behind convolution we should look at it from different perspectives.

## Filtering perspective

Let's consider the above equation with $h[n]$ denoting filter's (or any linear time-invariant (LTI) system) impulse response and $x[n]$ as this filter's input signal. From signal processing we know, that any LTI system is completely specified by its impulse response.

If we denote the output of the filter by $y[n]$ we may look at the output as a weighted sum of filter's impulse responses. How?

Consider $n=0$. At the output we get

$$y[0] = \sum_{k=-\infty}^{\infty} x[k] h[0 - k] = \sum_{k=-\infty}^{\infty} x[k] h[- k] = x[0] h[0],$$ because $h[n] = 0$ and $x[n]=0$ for all $n < 0$. What do we get for $n=1$?

$$y[1] = \sum_{k=-\infty}^{\infty} x[k] h[1 - k] = x[0]h[1] + x[1]h[0].$$ As you can see, x[0] has moved "further down the road" (further into the filter's buffer) and now constitutes the weight for $h[1]$ from filter's impulse response. At the same time $x[1]$ enters the buffer and (as $x[0]$ previously) weights the $h[0]$. The operation repeats for every following input sample. $x[0]$ stops weighting filter's impulse response when it has weighted the last one of them (unless it is an IIR filter; it then weights the filter's impulse response infinitely).

## Delaying-and-summing perspective

We can also look at that operation from a different perspective. What if we fix $k$? In this case it describes the behaviour of the system if only input sample $x[k]$ was given:

$$ y_k[n] = x[k]h[n-k].$$

The above equation basically says, that once $x[k]$ enters the filter, it will weigh its entire impulse response delayed by $k$ samples w.r.t $n$. We then just have to sum up over all possible $k$ to conclude, that $y[n]$ is just filter's impulse response, delayed and weighted by $x[n]$.

This may all get a little bit confusing at this moment, so let's look at an example, shall we?

### Example

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
![]({{ page.images | absolute_url | append: "/h_summed.png"}})
what corresponds to the $y[n]$ signal above.

# Continuous convolution
Convolution is defined for continuous signals as well (notice the conventional use of round brackets for non-discrete functions):

$$ x(t) \ast h(t) = \int \limits_{-\infty}^{\infty} x(\tau) h(t - \tau) d\tau $$

Although it may not be as intuitive in interpretation as the discrete convolution, nevertheless, we could try to imagine the continuous case as an infinitely densely sampled discrete signal (so that sum over discrete samples changes to integral over continuous functions). But keep in mind that it is only an intuitive view!

# Summary

In this article we have introduced the mathematical operation of convolution and given the justification for its form and provided a little bit of intuition how can we view the convolution from different angles. In the next articles we are going to study convolution more closely.

Up next: [mathematical properties of convolution]({{"/mathematical-properties-of-convolution/" | absolute_url}})!.

{% endkatexmm %}