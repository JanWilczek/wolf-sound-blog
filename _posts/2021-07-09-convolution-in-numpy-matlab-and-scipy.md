---
title: "Convolution in MATLAB, NumPy, and SciPy"
date: 2021-07-09
author: Jan Wilczek
layout: post
permalink: /convolution-in-matlab-numpy-and-scipy/
images: assets/img/posts/2021-07-09-convolution-in-matlab-numpy-and-scipy
# background: /assets/img/posts/2021-07-09-convolution-in-matlab-numpy-and-scipy/Thumbnail.png
categories:
 - Digital Signal Processing
 - Python
tags:
 - convolution
 - Matlab
discussion_id: 2021-07-09-convolution-in-matlab-numpy-and-scipy
---
How to compute convolution using numerical libraries?

## The Convolution Series
1. [Definition of convolution and intuition behind it]({% post_url 2020-06-20-the-secret-behind-filtering %})
1. [Mathematical properties of convolution]({% post_url 2020-07-05-mathematical-properties-of-convolution %})
1. [Convolution property of Fourier, Laplace, and z-transforms]({% post_url 2021-03-18-convolution-in-popular-transforms %})
1. [Identity element of the convolution]({% post_url 2021-04-01-identity-element-of-the-convolution %})
1. [Star notation of the convolution]({% post_url 2021-04-03-star-notation-of-the-convolution-a-notational-trap %})
1. [Circular vs. linear convolution]({% post_url 2021-05-07-circular-vs-linear-convolution %})
1. [Fast convolution]({% post_url 2021-05-14-fast-convolution %})
1. [Convolution vs. correlation]({% post_url 2021-06-18-convolution-vs-correlation %})
1. **Convolution in MATLAB, NumPy, and SciPy**

Most often we won't be implementing convolution every time we need to use it. Therefore, it is important to know functions from numerical libraries we can use.

The most popular implementation of the convolution are `conv` from Matlab, `convolve` from NumPy, and `convolve` from SciPy. I won't be describing any C/C++ convolution implementations here.

# 3 Modes of Convolution

Before we dive into the specific functions, it is important to understand 3 different "modes" the convolution can be calculated with.

## Full

This is the mathematical implementation of convolution. Having signals of length $M$ and $N$ the 'full' mode returns a signal of length $M + N - 1$. Index 
