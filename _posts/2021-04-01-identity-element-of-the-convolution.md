---
title: "Identity element of the convolution"
date: 2021-04-01
author: Jan Wilczek
layout: post
permalink: /identity-element-of-the-convolution/
background: /assets/img/posts/2021-04-01-identity-element-of-the-convolution/Thumbnail.png
images: assets/img/posts/2021-04-01-identity-element-of-the-convolution
categories:
 - DSP
tags:
 - convolution
 - impulse
 - maths
 - dsp
discussion_id: 2021-04-01-identity-element-of-the-convolution
---
How to convolve and do nothing at the same time?

<iframe width="560" height="315" src="https://www.youtube.com/embed/XIWXmV92ju4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

{% katexmm %}

## The Convolution Series
1. [Definition of convolution and intuition behind it]({% post_url 2020-06-20-the-secret-behind-filtering %})
1. [Mathematical properties of convolution]({% post_url 2020-07-05-mathematical-properties-of-convolution %})
1. [Convolution property of Fourier, Laplace, and z-transforms]({% post_url 2021-03-18-convolution-in-popular-transforms %})
1. **Identity element of the convolution**
1. [Star notation of the convolution]({% post_url 2021-04-03-star-notation-of-the-convolution-a-notational-trap %})
1. [Circular vs. linear convolution]({% post_url 2021-05-07-circular-vs-linear-convolution %})
1. [Fast convolution]({% post_url 2021-05-14-fast-convolution %})

# Table of Contents
1. [Introduction](#introduction)
1. [Justification of the need for an identity element](#why-do-we-need-a-neutral-element)
1. [Identity element of the discrete convolution](#identity-element-of-the-discrete-convolution)
1. [Identity element of the continuous convolution](#identity-element-of-the-continuous-convolution)
1. [The sifting property](#the-sifting-property)
1. [Delay](#delay)
1. [Signal representation using the delay](#what-is-a-signal-really)
1. [Summary](#summary)

# Introduction

For any operation, a very important concept is the *neutral* or *identity element*. Adding 0 to any number results in the same number. Multiplying a number by 1 results in the same number. These trivial facts are extensively used to prove numerous theorems of mathematics, especially in engineering. Particularly popular is adding and subtracting a variable or a constant (effectively adding 0) to introduce a desired element in the inspected (in)equality.

More formally, a **neutral element** or an **identity element** with respect to a binary operation $\ast$ defined on a set $A$ is an element $e \in A$ such that [1, Sec. 5.3.1.2]

{% capture _ %}{% increment page.equationId  %}{% endcapture %}

$$e \ast a = a \ast e = a \quad \forall a \in A. \quad ({% increment page.equationId  %})$$

What is the identity element of convolution?

# Why do we need a neutral element?

We often want to represent a "do nothing" operation in our processing, regardless of the domain. Examples of such operations are "add 0" for addition and "multiply by 1" for multiplication, as mentioned in the introduction. Another example is the NOP ("no operation") instruction of processors used, for instance, for [memory alignment]({% post_url 2020-04-09-what-is-data-alignment %}).

Imagine that you would like to identify the impulse response of a certain system. As we know from [one of the previous articles]({% post_url 2020-06-20-the-secret-behind-filtering %}), the output of an LTI system is the convolution of its impulse response with the input. What if the system does nothing? We need a way to represent its impulse response (Figure 1).

![]({{ page.images | absolute_url | append: "/identity_block.png" }}){: width="350" }
_Figure 1. How to represent a system that does not alter our signal at all?_

# Identity element of the discrete convolution

Let's focus on the discrete convolution first. We are looking for a discrete signal, let's denote it by $\delta[n]$, such that for any signal $x[n]$ it holds (according to Equation 1) that

$$x[n] \ast \delta[n] = \delta[n] \ast x[n] = \sum_{k=-\infty}^{\infty} x[k] \delta[n - k] = x[n], \quad n \in \mathbb{Z}. \quad ({% increment page.equationId  %})$$

From the above it is clear that $\delta[n-k]$ should be equal to 1 if $k = n$ and 0 for every other $k$. In this way, we can pick out untouched $x[n]$ from the infinite sum and **only** $x[n]$.

If $\delta[n-k] = 1$ for $k = n$, then $\delta[0]=1$. Thus,

$$\delta[n] = \begin{cases} 1 &\text{ if } n=0,\\ 0 &\text{ if } n \neq 0. \end{cases}\quad ({% increment page.equationId  %})$$

And so we have found our neutral element! The signal defined in Equation 3 is called a **unit sample sequence**, a **discrete-time impulse**, or just an **impulse** [2]. I have also often stumbled upon the name **discrete (Dirac) delta (impulse)**.

The definition in Equation 3 makes sense also from a different perspective. In [the first article in the convolution series]({% post_url 2020-06-20-the-secret-behind-filtering %}), we said that convolution in the context of filtering means delaying and scaling the impulse response by the samples of the input signal. If the impulse response consists of a single sample with value 1, convolving a signal with it should yield only delayed successive weights, i. e., just the input signal.

# Identity element of the continuous convolution

How does the neutral element look in the case of continuous convolution? According to Equation 2, we obtain

$$x(t) \ast \delta(t) = \delta(t) \ast x(t) = \int \limits_{-\infty}^{\infty} x(\tau) \delta(t - \tau) d\tau = x(t). \quad ({% increment page.equationId  %}) $$

Are you able to extract the formula for $\delta(t)$ out of this equation? Me neither. So how is our $\delta(t)$ defined, then?

It turns out that there exists no *function* satisfying Equation 4. We need another type of entity called a **generalized function** or a **distribution**. Then our $\delta(t)$ is called the **Dirac $\delta$ function** and can be *approximated* by [1, Eq. 15.33a]

$$\delta(t) = \lim_{\epsilon \rightarrow 0} f(t,\epsilon), \quad ({% increment page.equationId  %})$$

where

$$ f(t,\epsilon) = \begin{cases} \frac{1}{\epsilon} &\text{ if } |t|<\frac{\epsilon}{2},\\ 0 &\text{ if } |t|\geq\frac{\epsilon}{2}. \end{cases}\quad ({% increment page.equationId  %})$$

How to tackle this definition? I try to think about it as a function being 0 everywhere apart from $t=0$. At $t=0$, $\delta(t)$ tends to $+\infty$ like an infinitesimally narrow impulse of infinite height. But it is just an intuition; a correct mathematical definition is beyond the scope of this article.

Dirac $\delta$ function is ubiquitious in mathematics and engineering. It is often used to define *empirical probability distributions* (i.e., the ones resulting directly from data) [3]. Additionally, I have seen it in action when defining the excitation function of partial differential equations (PDEs), e.g., representing the influence of a hammer strucking a piano string in physical modeling sound synthesis [4]. 

# The sifting property

Dirac $\delta$ function has a valuable property

$$ \int \limits_{t-a}^{t+a} x(\tau) \delta(t-\tau) d\tau = x(t) \quad \forall a > 0.\quad ({% increment page.equationId  %})$$

Substituting $a=\infty$ (what we **can** do) yields exactly our desired Equation 4.

The property in Equation 7 is called the **sifting property** of the $\delta$ function, because the $\delta$ function "sifts" our signal only to return the value of $x$ at a point where the argument of $\delta$ is equal to 0.

In the discrete case, the sifting property was shown in action in Equation 2; there we extracted a single element $x[n]$ out of the (possibly infinite) $x$ sequence.

# Delay

What happens if we shift the argument of the discrete-time impulse by 1?

$$x[n] \ast \delta[n-1] = \sum_{k=-\infty}^{\infty} x[k] \delta[n - 1 - k] = x[n-1], \quad n \in \mathbb{Z}. \quad ({% increment page.equationId  %})$$

Looking at the discrete time instant $n$, the convolution with an argument-shifted impulse, $\delta[n-1]$, yielded $x[n-1]$, i. e., a sample that was already "known" to us (we are at time $n$ so we already observed $x[n-1]$ at time $n-1$). That is the concept of a unit **delay**.

By adjusting the argument shift $n_0$ of $\delta[n-n_0]$ and convolving the result with a signal we can obtain an arbitrarily delayed signal. If $n_0 < 0$, we can even obtain "samples from the future", i. e., $x[n] \ast \delta[n+1] = x[n+1]$. $n_0$ is called the **delay length** or simply the delay.

The concept of the delay and its application in digital signal processing and audio programming is very profound. Delay is an inherent property of any filter, or more generally, any LTI system. You may have stumbled upon the "Delay effect" as an audio plug-in to a digital audio workstation (DAW); the underlying principle relies on delaying the input signal and possibly adding it to the original. Delaying one channel with respect to the other helps to set up panning based on interaural time difference (ITD). Examples of other applications of the delay, just in the domain of audio effects, include artificial reverberation, comb filter, flanger, chorus, and Karplus-Strong synthesis.

## Graphical representation

In DSP diagrams, the delay by $n_0$ samples is marked with a $z^{-n_0}$ box (Figure 2). 

![]({{ page.images | absolute_url | append: "/delay.png" }}){: width="350" }
_Figure 2. Representation of a delay by $n_0$ samples as a functional block in a DSP diagram._

That is because the $z$-transform of $\delta[n-n_0]$ is equal to $z^{-n_0}$

$$ \mathcal{Z}\{\delta[n-n_0]\} = \sum_{n=-\infty}^{\infty} \delta[n-n_0] z^{-n} = z^{-n_0}. \quad ({% increment page.equationId  %})$$

Notice that Equation 9 could be viewed as an application of the sifting property. From an infinite "stream" of $z^{-n}$ we pick out only the one for which $n=n_0$.

## Arranging delays in a series

From the associativity property of the convolution, which we derived in [one of the previous articles]({% post_url 2020-07-05-mathematical-properties-of-convolution %}), it can be inferred that arranging delays in a series results in a delay of length equal to the sum of the individual delay lengths. That is because

$$\delta[n-n_0] \ast \delta[n-n_1] = \sum_{k=-\infty}^{\infty} \delta[k - n_0]\delta[n-n_1 - k] \\= \delta[n-n_0-n_1]. \quad ({% increment page.equationId  %})$$

($\delta[k - n_0]\delta[n-n_1 - k]=1$ only if $k-n_0=0$ what results in $k=n_0$).

That means we can stack the delays one after another to increase the delay length (Figure 3).

![]({{ page.images | absolute_url | append: "/delay-series.png" }})
_Figure 3. Appending a delay element to the system results in adding its delay length to the original delay of the system._

Unsurprisingly, the $z^{-n}$ notation in Figure 3 results directly from the convolution property of the $z$-transform, which we discussed in [the previous article]({% post_url 2021-03-18-convolution-in-popular-transforms %})

$$ \mathcal{Z}\{\delta[n-n_0] \ast \delta[n-n_1]\} = \mathcal{Z}\{\delta[n-n_0] \} \mathcal{Z}\{\delta[n-n_1]\} \\= z^{-n_0} z^{-n_1} = z^{-(n_0+n_1)}. \quad ({% increment page.equationId %})$$

# What is a signal, really?

Let's recap once again the convolutional sum of Equation 2 [2, Eq. 2.5]

$$x[n] = \sum_{k=-\infty}^{\infty} x[k] \delta[n - k], \quad n \in \mathbb{Z}. \quad ({% increment page.equationId  %})$$

Let's evaluate it for a few conrete values of $n$.

$$x[0] = \sum_{k=-\infty}^{\infty} x[k] \delta[0 - k] = x[0]\delta[0 - 0] = x[0],$$
$$x[1] = \sum_{k=-\infty}^{\infty} x[k] \delta[1 - k] = x[1]\delta[1 - 1] = x[1],$$
$$x[2] = \sum_{k=-\infty}^{\infty} x[k] \delta[2 - k] = x[2]\delta[2 - 2] = x[2],$$
$$\vdots$$
$$x[n] = \sum_{k=-\infty}^{\infty} x[k] \delta[n - k] = x[n]\delta[n - n] = x[n].$$

As the value of $n$ changes, the corresponsing shift $k$ of the delta argument must change as well to make $n-k$ equal to 0 and produce a single result $x[n]$. We could think of this change of $k$ as a change of the delay length.

Let's now assume that $x[n]$ starts at 0, i. e., $x[n]=  0 \forall n <0$. Writing down the sum in Equation 12 explicitly yields [2]

$$x[n] = x[0]\delta[n] + x[1]\delta[n-1] + x[2]\delta[n-2] + \dots \\+ x[n-1]\delta[n-(n-1)] x[n]\delta[n - n] + \dots \quad ({% increment page.equationId  %})$$

Can you see the beauty of it? **$x[n]$ already contains all possible samples of the sequence $x$; we just need to delay it properly to receive the desired sample.** In other words, any discrete-time signal is a convolutional sum, a weighted sum of delayed impulses. Fixing index $n$ to some concrete value sets the delay length accordingly so as to return the signal value for that particular $n$.

# Summary

In this article we examined the identity element of the convolution, i. e., $\delta[n]$ for the discrete convolution (Equation 3) and $\delta(t)$ for the continuous convolution (Equation 5). The former is much more easily tractable mathemathically [2].

We introduced the sifting property of the delta impulse and interpreted it as the delay in the context of digital signal processing. 

Finally, we looked at a discrete-time signal as a weighted sum of delayed impulses.

# Bibliography

[1] I.N. Bronshtein et. al. *Handbook of Mathematics*, 5th Edition, Springer, 2007.

[2] A. V. Oppenheim, R. W. Schafer *Discrete-Time Signal Processing*, 3rd Edition, Pearson, 2010.

[3] I. Goodfellow, Y. Bengio, A. Courville *Deep learning*, MIT Press, 2016, [https://www.deeplearningbook.org/](https://www.deeplearningbook.org/).

[4] M. Schäfer *Simulation of Distributed Parameter Systems by Transfer Function
Models* Ph.D. dissertation, Friedrich-Alexander-Universität Erlangen-Nürnberg
(FAU), 2020.


{% endkatexmm %}

