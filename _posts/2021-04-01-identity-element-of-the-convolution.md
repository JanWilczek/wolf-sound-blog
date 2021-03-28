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

And so we have found our neutral element! The signal defined in Equation 3 is called a **unit sample sequence**, a **discrete-time impulse**, or just an **impulse** [2].

# Identity element of the continuous convolution

* no neutral element among functions
* Dirac delta (continuous and discrete)
* convolution with a delta, the sifting property
* the concept of delay and its application in DSP
* notation considerations ([n-n0], etc.)
* discrete-time signal or sampling as a convolutional sum, a weighted sum of impulses

# Bibliography

[1] I.N. Bronshtein *Handbook of Mathematics*, 5th Edition, Springer 2007.

[2] Alan V Oppenheim, Ronald W. Schafer *Discrete-Time Signal Processing*, 3rd Edition, Pearson 2010.

{% endkatexmm %}

