---
title: "Convolution in Probability: Sum of Independent Random Variables"
date: 2021-07-30
author: Jan Wilczek
layout: post
permalink: /convolution-in-probability-sum-of-independent-random-variables/
images: assets/img/posts/2021-07-30-convolution-in-probability
background: /assets/img/posts/2021-07-30-convolution-in-probability/Thumbnail.png
categories:
 - Digital Signal Processing
tags:
 - convolution
 - probability
discussion_id: 2021-07-30-convolution-in-probability
---
Thanks to convolution, we can obtain the pdf of a sum of independent random variables.

## The Convolution Series
1. [Definition of convolution and intuition behind it]({% post_url 2020-06-20-the-secret-behind-filtering %})
1. [Mathematical properties of convolution]({% post_url 2020-07-05-mathematical-properties-of-convolution %})
1. [Convolution property of Fourier, Laplace, and z-transforms]({% post_url 2021-03-18-convolution-in-popular-transforms %})
1. [Identity element of the convolution]({% post_url 2021-04-01-identity-element-of-the-convolution %})
1. [Star notation of the convolution]({% post_url 2021-04-03-star-notation-of-the-convolution-a-notational-trap %})
1. [Circular vs. linear convolution]({% post_url 2021-05-07-circular-vs-linear-convolution %})
1. [Fast convolution]({% post_url 2021-05-14-fast-convolution %})
1. [Convolution vs. correlation]({% post_url 2021-06-18-convolution-vs-correlation %})
1. [Convolution in MATLAB, NumPy, and SciPy]({% post_url 2021-07-09-convolution-in-numpy-matlab-and-scipy %})
1. [Deconvolution: Inverse convolution]({% post_url 2021-07-23-deconvolution %})
1. **Convolution in probability: Sum of independent random variables**

{% katexmm %}

{% capture _ %}{% increment equationId20210730  %}{% endcapture %}

So far, we have looked into many aspects of convolution. One of its important applications is in probability: thanks to the convolution, we can obtain the *probability density function* (pdf) of a sum of two independent random variables (RVs). It turns out that the pdf of the sum is a convolution of of the individual pdfs.

In this article, we will show the proof of this theorem. This proof takes advantage of the [convolution property of the Fourier transform]({% post_url 2021-03-18-convolution-in-popular-transforms %}).

# Convolution Theorem in Probability

> The pdf of a sum of statistically independent RVs is the convolution of the contributing pdfs. 

# Proof 

Before we conduct the actual proof we need to introduce the concept of the *Characteristic Function*.

## The Characteristic Function

The Characteristic Function $\Phi_X(j \omega)$ of a random variable $X$ is the Fourier transform the its pdf $f_X$ with reversed argument $x$:

$$\Phi_X(j \omega) = \mathbb{E} \left[ e^{j\omega X} \right] = \int \limits_{-\infty}^{\infty} f_X(x) e ^{j\omega x} dx \\= \int \limits_{-\infty}^{\infty} f_X(-x) e ^{-j \omega x} dx = \mathcal{F} \{f_X(-x)\}. \quad ({% increment equationId20210730  %})$$

Let us observe that 

$$\Phi_X(-j \omega) = \mathcal{F} \{f_X(x)\}. \quad ({% increment equationId20210730  %})$$

## Sum of Two Independent Random Variables

We have two independent random variables, $X$ and $Y$, with pdfs $f_X$ and $f_Y$ respectively. We want to know what is the pdf of the sum of $X$ and $Y$, i.e., what is the formula for $f_{X+Y}$. To do that, we calculate the characteristic function of $X+Y$:

$$\Phi_{X+Y}(j \omega) = \mathbb{E} \left[ e^{j\omega (X+Y)} \right] 
\\= \int \limits_{-\infty}^{\infty} \int \limits_{-\infty}^{\infty} f_{X+Y}(x, y) e ^{j\omega (x+y)} dxdy
\\=  \int \limits_{-\infty}^{\infty} f_X(x) e ^{j\omega x} dx  \int \limits_{-\infty}^{\infty} f_Y(y) e ^{j\omega y} dy 
\\= \mathbb{E} \left[ e^{j\omega X} \right] \mathbb{E} \left[ e^{j\omega Y} \right] = \Phi_X(j \omega) \Phi_Y(j \omega). \quad ({% increment equationId20210730  %})$$

Note that we could separate the integrals only thanks to the independence of the two variables.

## Convolution Property of the Fourier Transform

We found out that the characteristic function of a sum of two independent RVs is equal to the product of the individual characteristic functions of these RVs. Additionally, the characteristic function of an RV with negated argument is the Fourier transform of this RV's pdf. We thus have

$$f_{X+Y}(x,y) \stackrel{\mathcal{F}}{\longleftrightarrow} \Phi_{X+Y}(-j \omega), \quad ({% increment equationId20210730  %})$$

and 

$$\Phi_{X+Y}(-j \omega) = \Phi_{X}(-j \omega) \Phi_{Y}(-j \omega) , \quad ({% increment equationId20210730  %})$$

The [convolution property of the Fourier transform]({% post_url 2021-03-18-convolution-in-popular-transforms %}) tells us that the multiplication in the Fourier domain is equivalent to convolution in the other domain (here: the domain of the RV). Therefore,

$$\Phi_{X+Y}(-j \omega) = \Phi_{X}(-j \omega) \Phi_{Y}(-j \omega) \stackrel{\mathcal{F}}{\longleftrightarrow} f_X(x) \ast f_Y(x) 
\\= f_{X+Y}(x), \quad ({% increment equationId20210730  %})$$

what concludes the proof $\Box$.

## Final Remark

This proof can be extended to arbitrary many random variables with the requirement that all of them are mutually independent.

# Summary

In this article, we have proven that the pdf of a sum of independent RVs is a convolution of these RVs' pdfs.

# Bibliography

[1] Walter Kellermann, *Statistical Signal Processing Lecture Notes*, Winter Semester 2019/2020, University of Erlangen-Nürnberg.

{% endkatexmm %}
