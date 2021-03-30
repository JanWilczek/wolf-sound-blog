---
title: "Identity element of the convolution"
date: 2021-04-01
author: Jan Wilczek
layout: post
permalink: /identity-element-of-the-convolution/
background: /assets/img/posts/2020-06-20-the-secret-behind-filtering/h_superposed.png
categories:
 - DSP
tags:
 - convolution
 - impulse
 - maths
 - dsp
---
How to convolve and do nothing at the same time?

{% katexmm %}

For any operation, a very important concept is the *neutral* or *identity element*. Adding 0 to any number results in the same number. Multiplying any number by 1 results in the same number. These trivial facts are extensively used to prove numerous theorems of mathematics, especially in engineering. Particularly popular is adding and subtracting a variable or a constant (so adding 0) to introduce a desired element in an inspected equality.

More formally, a **neutral element** or an **identity element** with respect to a binary operation $\ast$ defined on a set $A$ is an element $e \in A$ such that [1, Sec. 5.3.1.2]

$$e \ast a = a \ast e = a \quad \forall a \in A. \quad (1)$$

What is the identity element of convolution?

## The Convolution Series
1. [Definition of convolution and intuition behind it]({% post_url 2020-06-20-the-secret-behind-filtering %})
1. [Mathematical properties of convolution]({% post_url 2020-07-05-mathematical-properties-of-convolution %})
1. [The convolution property in popular transforms]({% post_url 2021-03-18-convolution-in-popular-transforms %})
1. **Identity element of the convolution**

# Why do we need a neutral element?

We often want to represent a "do nothing" operation in our processing. That holds for the examples mentioned in the introduction. Another example could be the NOP ("no operation") instruction of processors used, for instance, for [memory alignment]({% post_url 2020-04-09-what-is-data-alignment %}).

Imagine that you would like to identify the impulse response of a certain system. As we know from [one of the previous articles]({% post_url 2020-06-20-the-secret-behind-filtering %}) the output of an LTI system is the convolution of its impulse response with the input. What if the system does nothing? We need a way to represent the resulting impulse response we obtained.

# Identity element of the discrete convolution

Let's focus first on discrete convolution. We are looking for a discrete signal, let's denote it $\delta[n]$, such that for any signal $x[n]$ it holds (according to Equation 1) that

$$x[n] \ast \delta[n] = \delta[n] \ast x[n] = \sum_{k=-\infty}^{\infty} x[k] \delta[n - k] = x[n], \quad n \in \mathbb{Z}. \quad (2)$$

From the above it is clear that $\delta[n-k]$ should be equal to 1 if $k = n$ and 0 for every other $k$. In this way, we can pick out untouched $x[n]$ from the infinite sum and **only** $x[n]$.

If $\delta[n-k] = 1$ for $k = n$, then $\delta[0]=1$. Thus,

$$\delta[n] = \begin{cases} 1 &\text{ if } n=0,\\ 0 &\text{ if } n \neq 0. \end{cases}\quad (3)$$

And so we have found our neutral element! The signal defined in Equation 3 is called a **unit sample sequence**, a **discrete-time impulse**, or just an **impulse** [2]. I have also often stumbled upon the name **discrete (Dirac) delta**.

The definition in Equation 3 makes sense also from a different perspective. In [the first post in the series]({% post_url 2020-06-20-the-secret-behind-filtering %}), we said that convolution in the context of filtering means scaling and delaying the impulse response by the samples of the input signal. If the impulse response consists of a single sample with value 1, convolving a signal with it should yield only delayed successive weights, i. e., just the input signal.

# Identity element of the continuous convolution

How does the neutral element look in case of continuous convolution. According to Equation 2, we obtain

$$x(t) \ast \delta(t) = \delta(t) \ast x(t) = \int \limits_{-\infty}^{\infty} x(\tau) \delta(t - \tau) d\tau = x(t). \quad (4) $$

Are you able to extract the formula for $\delta(t)$ out of this equation? Me neither. So how is our $\delta(t)$ defined, then?

It turns out that there exists no *function* satisfying Equation 4. We need another type of entity called a **generalized function** or a **distribution**. Then our $\delta(t)$ is called the **Dirac $\delta$ function** and can be *approximated* by [1, Eq. 15.33a]

$$\delta(t) = \lim_{\epsilon \rightarrow 0} f(t,\epsilon), \quad (5)$$

where

$$ f(t,\epsilon) = \begin{cases} \frac{1}{\epsilon} &\text{ if } |t|<\frac{\epsilon}{2},\\ 0 &\text{ if } |t|\geq\frac{\epsilon}{2}. \end{cases}\quad (6)$$

How to tackle this definition? I try to think about it as a function being 0 everywhere apart from $t=0$. At $t=0$, $\delta(t)$ tends to $+\infty$ like an infinitesimally narrow impulse. But it is just an intuition; a correct mathematical definition is beyond the scope of this article.

Dirac $\delta$ function is ubiquitious in mathematics and engineering. It is often used for defining initial conditions for partial differential equations (PDEs), e.g., the influence of a hammer strucking a piano string in physical modeling sound synthesis. 

# The sifting property

Dirac $\delta$ function has a valuable property

$$ \int \limits_{t-\tau}^{t+\tau} x(\tau) \delta(t-\tau) d\tau = x(t) \quad \forall a > 0.\quad (7)$$

Substituting $a=\infty$ (what we **can** do) yields exactly our desired Equation 4.

The property in Equation 7 is called the **sifting property** of the $\delta$ function, because the $\delta$ function "sifts" our signal only to return the value of $x$ at a point where the argument of $\delta$ is equal to 0.

In the discrete case, the sifting property was shown in action in Equation 2: there we extracted a single element $x[n]$ out of the (possibly infinite) $x$ sequence.

# Delay

What happens if we shift the argument of the discrete-time impulse by 1?

$$x[n] \ast \delta[n-1] = \sum_{k=-\infty}^{\infty} x[k] \delta[n - 1 - k] = x[n-1], \quad n \in \mathbb{Z}. \quad (8)$$

Looking at the discrete-time instant $n$, applying a convolution with argument-shifted impulse, $\delta[n-1]$, yielded $x[n-1]$, i. e., a samples that was already "known" to us (we are at time $n$ so we already observed $x[n-1]$ at time $n-1$). That is the concept of a unit **delay**.

By adjusting the shift of the argument $n_0$ of $\delta[n-n_0]$ and convolving the result with a signal we can obtain an arbitrarily delayed signal. If $n_0 < 0$, we can even obtain "samples from the future", i. e., $x[n] \ast \delta[n+1] = x[n+1]$. 

The concept of the delay and its application in digital signal processing and audio programming is very profound. Delay is an inherent property of any filter, or more generally, any LTI system. You may have stumbled upon the "Delay effect" as an audio plug-in to a digital audio workstation (DAW); the underlying principle is just that. Examples of other applications of the delay just in the domain of audio effects include artificial reverberation, comb filter, flanger, chorus, Karplus-Strong synthesis, and many more.

In DSP diagrams, unit delay, i. e., with $n_0=1$, is often marked with a $z^{-1}$ box. 

<!-- Figure needed -->

That is because the $z$-transform of $\delta[n-1]$ is equal to $z^{-1}$

$$ \mathcal{Z}\{\delta[n-1]\} = \sum_{n=-\infty}^{\infty} \delta[n-1] z^{-n} = z^{-1}. \quad (9)$$

Notice that Equation 9 could be viewed as another application of the sifting property. From an infinite "stream" of $z^{-n}$ we pick only the one for $n=1$.

# What is a signal, really?


* discrete-time signal or sampling as a convolutional sum, a weighted sum of impulses
* notation considerations ([n-n0], etc.)

# Bibliography

[1] I.N. Bronshtein et. al. *Handbook of Mathematics*, 5th Edition, Springer 2007.

[2] Alan V Oppenheim, Ronald W. Schafer *Discrete-Time Signal Processing*, 3rd Edition, Pearson 2010.

{% endkatexmm %}

