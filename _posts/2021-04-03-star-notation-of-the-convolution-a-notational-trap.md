---
title: "Star notation of the convolution: a notational trap"
date: 2021-04-03
author: Jan Wilczek
layout: post
permalink: /star-notation-of-the-convolution-a-notational-trap/
background: /assets/img/posts/2021-04-03-star-notation-of-the-convolution-a-notational-trap/Thumbnail.png
images: assets/img/posts/2021-04-03-star-notation-of-the-convolution-a-notational-trap
categories:
 - DSP
tags:
 - convolution
 - maths
discussion_id: 2021-04-03-star-notation-of-the-convolution-a-notational-trap
---
How not to fall victim to the star notation of the convolution?

<iframe width="560" height="315" src="https://www.youtube.com/embed/cMagZegrIns" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

{% katexmm %}

## The Convolution Series
1. [Definition of convolution and intuition behind it]({% post_url 2020-06-20-the-secret-behind-filtering %})
1. [Mathematical properties of convolution]({% post_url 2020-07-05-mathematical-properties-of-convolution %})
1. [Convolution property of Fourier, Laplace, and z-transforms]({% post_url 2021-03-18-convolution-in-popular-transforms %})
1. [Identity element of the convolution]({% post_url 2021-04-01-identity-element-of-the-convolution %})
1. **Star notation of the convolution**
1. [Circular vs. linear convolution]({% post_url 2021-05-07-circular-vs-linear-convolution %})
1. [Fast convolution]({% post_url 2021-05-14-fast-convolution %})

# Introduction

{% capture _ %}{% increment page.equationId2  %}{% endcapture %}

Taking advantage of the introduction of delays in [the previous article]({% post_url 2021-04-01-identity-element-of-the-convolution %}), I wanted to warn you against a common pitfall when talking about the convolution [1]. 

The star notation $x[n] \ast h[n]$ is very convenient. It must, however, be used with caution.

The following notation should be clear to you by now

$$y[n] = x[n] \ast h[n], n \in \mathbb{Z}. \quad ({% increment page.equationId2  %})$$

What if we wanted to obtain a delayed version of $y[n]$, i. e., $y[n-n_0]$? A natural move would be to substitute $n \leftarrow n-n_0$

$$y[n-n_0] \stackrel{?}{=} x[n-n_0] \ast h[n-n_0], \quad ({% increment page.equationId2  %})$$

but...

![]({{ page.images | absolute_url | append: "/trap.jpg" }})

Let's evaluate the right hand side of "Equation" 2

$$x[n-n_0] \ast h[n-n_0] = \sum_{k=-\infty}^{\infty} x[k-n_0] h[n-n_0 - k] = \\ \sum_{k=-\infty}^{\infty} x[k] h[n-2n_0 - k] = y[n-2n_0]. \quad ({% increment page.equationId2  %})$$

By blindly substituting $n \leftarrow n-n_0$, we overshot the desired delay by a factor of two.

The correct way to write this is [1, Eq. 2.52]

$$y[n-n_0] = x[n] \ast h[n-n_0] = \sum_{k=-\infty}^{\infty} x[k] h[n-n_0 - k]. \quad ({% increment page.equationId2  %})$$

This is just one of many problems that arise when using the star notation.

## Useful notational tip

When the convolution looks any way different from the typical $x[n] \ast h[n]$, I try to bring it back to that basic form by defining "helper functions". Then I use the definition of the convolution and substitute the original functions again, inserting the correct argument.

How this works is best explained through an example.
## Example 1: Both convolved signals delayed

Let's say the operands of the convolution we need to perform are both delayed by different amounts, i. e., we want to calculate

$$x[n-n_x] \ast h[n-n_h] = \dots \quad n,n_x,n_h \in \mathbb{Z}. \quad ({% increment page.equationId2  %})$$

Let's define two "helper functions" $x_1[n], h_1[n]$

$$x_1[n] = x[n-n_x], \quad ({% increment page.equationId2  %})$$

$$h_1[n] = h[n-n_h]. \quad ({% increment page.equationId2  %})$$

Now we can insert these functions into Equation 5

$$x[n-n_x] \ast h[n-n_h] = x_1[n] \ast h_1[n], \quad ({% increment page.equationId2  %})$$

use the definition of the convolution

$$ x_1[n] \ast h_1[n] = \sum_{k=-\infty}^{\infty} x_1[k] h_1[n-k], \quad ({% increment page.equationId2  %}) $$

and finally substitute the original functions $x[n]$ and $h[n]$ according to Equations 6 and 7 respectively

$$\sum_{k=-\infty}^{\infty} x_1[k] h_1[n-k] = \sum_{k=-\infty}^{\infty} x[k-n_x] h[n - k - n_h]. \quad ({% increment page.equationId2  %})$$

This approach always works for me. At the same time, any shortcuts in an attempt not to use it inevitably led me to an error in calculations.

## Example 2: One of the convolved signal is time-reversed

This final example should make clear why "helper functions" ensure us that we correctly evaluate the star notation. In this example, one of the operands is time-reversed.

$$x[n] \ast h[-n] \stackrel{h_2[n]=h[-n]}{=} x[n] \ast h_2[n] = \sum_{k=-\infty}^{\infty} x[k] h_2[n-k]\\
\stackrel{h_2[n-k]=h[-(n-k)]}{=} \sum_{k=-\infty}^{\infty} x[k] h[k-n]. \quad ({% increment page.equationId2  %})$$

Is it possible to guess the correct answer right away? Yes, definitely. But it is not easy, especially if the arguments get even more complicated and the convolution is a part of a much larger body of derivations.

# Summary

In this article, we discussed notational issues concerning the discrete convolution and how to avoid common pitfalls when using the star notation. It all boils down to the idea of using "helper functions".


# Bibliography

[1] A. V. Oppenheim, R. W. Schafer *Discrete-Time Signal Processing*, 3rd Edition, Pearson 2010.

{% endkatexmm %}

