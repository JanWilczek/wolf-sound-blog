---
title: "Convolution in Probability: Sum of Independent Random Variables (With Proof)"
date: 2021-07-30
author: Jan Wilczek
layout: post
permalink: /convolution-in-probability-sum-of-independent-random-variables-with-proof/
images: assets/img/posts/2021-07-30-convolution-in-probability
background: /assets/img/posts/2021-07-30-convolution-in-probability/Thumbnail.png
categories:
 - Digital Signal Processing
tags:
 - convolution
 - probability
discussion_id: 2021-07-30-convolution-in-probability
---
Thanks to convolution, we can obtain the probability distribution of a sum of independent random variables.

<iframe width="560" height="315" src="https://www.youtube.com/embed/9ytYz9upnG4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### The Convolution Series
1. [Definition of convolution and intuition behind it]({% post_url collections.posts, 2020-06-20-the-secret-behind-filtering %})
1. [Mathematical properties of convolution]({% post_url collections.posts, 2020-07-05-mathematical-properties-of-convolution %})
1. [Convolution property of Fourier, Laplace, and z-transforms]({% post_url collections.posts, 2021-03-18-convolution-in-popular-transforms %})
1. [Identity element of the convolution]({% post_url collections.posts, 2021-04-01-identity-element-of-the-convolution %})
1. [Star notation of the convolution]({% post_url collections.posts, 2021-04-03-star-notation-of-the-convolution-a-notational-trap %})
1. [Circular vs. linear convolution]({% post_url collections.posts, 2021-05-07-circular-vs-linear-convolution %})
1. [Fast convolution]({% post_url collections.posts, 2021-05-14-fast-convolution %})
1. [Convolution vs. correlation]({% post_url collections.posts, 2021-06-18-convolution-vs-correlation %})
1. [Convolution in MATLAB, NumPy, and SciPy]({% post_url collections.posts, 2021-07-09-convolution-in-numpy-matlab-and-scipy %})
1. [Deconvolution: Inverse convolution]({% post_url collections.posts, 2021-07-23-deconvolution %})
1. **Convolution in probability: Sum of independent random variables**



{% capture _ %}{% increment equationId20210730  %}{% endcapture %}

So far, we have looked into various aspects of convolution. One of its important applications is in probability: thanks to the convolution, we can obtain the *probability density function* (pdf) of a sum of two independent random variables (RVs). It turns out that the pdf of that sum is a convolution of pdfs of the two random variables.

In this article, we will show the proof of this theorem. This proof takes advantage of the [convolution property of the Fourier transform]({% post_url collections.posts, 2021-03-18-convolution-in-popular-transforms %}).

## Convolution Theorem in Probability

> The probability density function of a sum of statistically independent random variables is the convolution of the contributing probability density functions. 

## Proof 

Before we conduct the actual proof, we need to introduce the concept of the *characteristic function*.

### The Characteristic Function

The characteristic function $\Phi_X(j \omega)$ of a random variable $X$ is the Fourier transform of its probability density function $f_X$ with a negated argument $x$:

$$\Phi_X(j \omega) = \mathbb{E} \left[ e^{j\omega X} \right] = \int \limits_{-\infty}^{\infty} f_X(x) e ^{j\omega x} dx \\= \int \limits_{-\infty}^{\infty} f_X(-x) e ^{-j \omega x} dx = \mathcal{F} \{f_X(-x)\}. \quad ({% increment equationId20210730  %})$$

Let us observe that 

$$\Phi_X(-j \omega) = \mathcal{F} \{f_X(x)\}. \quad ({% increment equationId20210730  %})$$

Another building block of the proof is the independence assumption which we examine next.

### Independence of Random Variables

Two random variables are called **statistically independent** if their joint probability density function factorizes into the respective pdfs of the RVs.

If we have two RVs, $X$ and $Y$, they are independent if and only if

$$ f_{XY}(x,y) = f_X(x)f_Y(y), \quad ({% increment equationId20210730  %})$$

where $f_{XY}$ is the joint pdf of $X$ and $Y$ (probability density of all possible combinations of $X$ and $Y$ values).

### Sum of Two Independent Random Variables

Now to the main part of the proof!

We have two independent random variables, $X$ and $Y$, with probability density functions $f_X$ and $f_Y$ respectively. We want to know what is the probability density function of the sum of $X$ and $Y$, i.e., what is the formula for $f_{X+Y}$. To discover that formula, we calculate the characteristic function of $X+Y$:

$$\Phi_{X+Y}(j \omega) = \mathbb{E} \left[ e^{j\omega (X+Y)} \right] 
\\= \int \limits_{-\infty}^{\infty} \int \limits_{-\infty}^{\infty} f_{XY}(x, y) e ^{j\omega (x+y)} dxdy
\\=  \int \limits_{-\infty}^{\infty} f_X(x) e ^{j\omega x} dx  \int \limits_{-\infty}^{\infty} f_Y(y) e ^{j\omega y} dy 
\\= \mathbb{E} \left[ e^{j\omega X} \right] \mathbb{E} \left[ e^{j\omega Y} \right] = \Phi_X(j \omega) \Phi_Y(j \omega). \quad ({% increment equationId20210730  %})$$

Note that we could separate the integrals only thanks to the independence of the two random variables: splitting $f_{XY}$ into a product of $f_X$ and $f_Y$.

### Convolution Property of the Fourier Transform

We found out that the characteristic function of a sum of two independent random variables is equal to the product of the individual characteristic functions of these random variables (Equation 4). Additionally, the characteristic function of a random variable with a negated argument is the Fourier transform of this RV's probability density function (Equation 3). We thus have

$$f_{X+Y}(x) \stackrel{\mathcal{F}}{\longleftrightarrow} \Phi_{X+Y}(-j \omega), \quad ({% increment equationId20210730  %})$$

and 

$$\Phi_{X+Y}(-j \omega) = \Phi_{X}(-j \omega) \Phi_{Y}(-j \omega) , \quad ({% increment equationId20210730  %})$$

The [convolution property of the Fourier transform]({% post_url collections.posts, 2021-03-18-convolution-in-popular-transforms %}) tells us that the multiplication in the Fourier domain is equivalent to convolution in the other domain (here: the domain of the random variable). Therefore,

$$\Phi_{X+Y}(-j \omega) = \Phi_{X}(-j \omega) \Phi_{Y}(-j \omega) \stackrel{\mathcal{F}}{\longleftrightarrow} f_X(x) \ast f_Y(x) 
\\= f_{X+Y}(x), \quad ({% increment equationId20210730  %})$$

what concludes the proof $\Box$.

*Note: $x$ is used instead of $y$ as the argument of $f_Y$ in Equation 7 because it doesn't matter what letter we use; $f_X$, $f_Y$, and $f_{X+Y}$ are all pdfs of one-dimensional random variables.*

### Final Remark

This proof can be extended to arbitrarily many random variables with the requirement that all of them are mutually independent.

## Summary

In this article, we have proven that the probability distribution of a sum of independent random variables is a convolution of probability distributions of these random variables.

## Bibliography

[1] Walter Kellermann, *Statistical Signal Processing Lecture Notes*, Winter Semester 2019/2020, University of Erlangen-Nürnberg.


