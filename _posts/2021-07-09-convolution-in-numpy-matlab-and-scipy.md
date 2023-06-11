---
title: "Convolution in MATLAB, NumPy, and SciPy"
date: 2021-07-09
author: Jan Wilczek
layout: post
permalink: /convolution-in-matlab-numpy-and-scipy/
images: assets/img/posts/2021-07-09-convolution-in-matlab-numpy-and-scipy
background: /assets/img/posts/2021-07-09-convolution-in-matlab-numpy-and-scipy/Thumbnail.png
categories:
 - Digital Signal Processing
 - Python
tags:
 - convolution
 - matlab
 - python
discussion_id: 2021-07-09-convolution-in-matlab-numpy-and-scipy
---
How to compute convolution using numerical software libraries?

<iframe width="560" height="315" src="https://www.youtube.com/embed/9yVowuBuASQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### The Convolution Series
1. [Definition of convolution and intuition behind it]({% post_url collections.posts, '2020-06-20-the-secret-behind-filtering' %})
1. [Mathematical properties of convolution]({% post_url collections.posts, '2020-07-05-mathematical-properties-of-convolution' %})
1. [Convolution property of Fourier, Laplace, and z-transforms]({% post_url collections.posts, '2021-03-18-convolution-in-popular-transforms' %})
1. [Identity element of the convolution]({% post_url collections.posts, '2021-04-01-identity-element-of-the-convolution' %})
1. [Star notation of the convolution]({% post_url collections.posts, '2021-04-03-star-notation-of-the-convolution-a-notational-trap' %})
1. [Circular vs. linear convolution]({% post_url collections.posts, '2021-05-07-circular-vs-linear-convolution' %})
1. [Fast convolution]({% post_url collections.posts, '2021-05-14-fast-convolution' %})
1. [Convolution vs. correlation]({% post_url collections.posts, '2021-06-18-convolution-vs-correlation' %})
1. **Convolution in MATLAB, NumPy, and SciPy**
1. [Deconvolution: Inverse convolution]({% post_url collections.posts, '2021-07-23-deconvolution' %})
1. [Convolution in probability: Sum of independent random variables]({% post_url collections.posts, '2021-07-30-convolution-in-probability' %})



Most often we won't be implementing convolution every time we need to use it. Therefore, it is important to know functions from numerical software libraries we can use.

The most popular implementation of the convolution are `conv` from Matlab, `convolve` from NumPy, and `convolve` from SciPy. I won't be describing any C/C++ convolution implementations here.

## 3 Modes of Convolution

Before we dive into the specific functions, it is important to understand 3 different 'modes' the convolution can be calculated with.

We will observe their effect using the following signals: $x[n]$

![]({{ images | absolute_url | append: "/x.png" }}){: width="700" }
_Figure 1. $x[n]$._

and $y[n]$

![]({{ images | absolute_url | append: "/y.png" }}){: width="700" }
_Figure 2. $y[n]$._

### Full

'Full' is the mathematical implementation of convolution. Having signals of length $M$ and $N$, the 'full' mode returns a signal of length $M + N - 1$. At points where signals do not overlap, they are padded with zeros.

![]({{ images | absolute_url | append: "/xy_full.png" }}){: width="700" }
_Figure 3. 'Full' mode of the convolution._

This is the default option for Matlab, NumPy, and SciPy.

### Valid

'Valid' mode does not use zero padding at all. The output is calculated only at positions where signals overlap completely. The result is a very short vector of length $\max(M, N) - \min(M, N) + 1$.

![]({{ images | absolute_url | append: "/xy_valid.png" }}){: width="700" }
_Figure 4. 'Valid' mode of the convolution._

Note that using this mode of convolution shrinks the output signal with each application [6].

### Same

'Same' acts as an intermediate level between 'full' and 'valid'; it crops the middle part out of the 'full' mode. Its length is equal to the length of the longer signal (NumPy, SciPy) or the first signal given (Matlab). This approach comes in handy when we want to keep the size of the convolution output constant.

![]({{ images | absolute_url | append: "/xy_same.png" }}){: width="700" }
_Figure 5. 'Same' mode of the convolution._

## Convolution Functions

Knowing the 3 modes, we can present now convolution functions of different numerical software libraries.

### NumPy

`numpy.convolve` has the following signature

```python
output = numpy.convolve(x, y, mode='full')
```

`x` and `y` are 1-D-arrays and `mode` is a string containing the convolution mode name.

### SciPy

`scipy.signal.convolve` has the following signature

```python
output = scipy.signal.convolve(x, y, mode='full', method='auto')
```

`x` and `y` are N-D-arrays, `mode` is a string containing the convolution mode name, and `method` can be `direct` (evaluation according to the convolution definition), `fft` (equivalent to the usage of `scipy.signal.fftconvolve`, i.e., the fast convolution algorithm), or `auto` (let the software decide).

[FFT convolution (fast convolution)]({% post_url collections.posts, '2021-05-14-fast-convolution' %}) is recommended for long signals of similar size.

SciPy has another convolution function, namely, `oaconvolve`. It lets the user pick the axes to compute convolution over. It uses the [overlap-add scheme]({% post_url collections.posts, '2021-05-14-fast-convolution' %}) and, thus, is recommended for long signals of significanlty different sizes.

`oaconvolve` and `fftconvolve` have the same signature: they take two multidimensional input signals, `mode` argument, and axes argument to compute the convolution over (an integer, an array, or `None` to use all axes).

```python
scipy.signal.fftconvolve(x, y, mode='full', axes=None)
scipy.signal.oaconvolve(x, y, mode='full', axes=None)
```

### Matlab

Matlab's `conv` has the following signature

```matlab
output = conv(x, y, shape) % shape is 'full' if not explicitly given
```

`x` and `y` are 1-D, row or column vectors. For 2-D convolution, one may use `conv2` function, and for N-D convolution, there is `convn` function.

## Summary

In this article, we have discussed 3 modes of convolution: `full`, `valid`, and `same` and the implementations of convolution in NumPy, SciPy, and Matlab.

Check out the references below for more details.

## Bibliography

[1] [`numpy.convolve` documentation](https://numpy.org/doc/stable/reference/generated/numpy.convolve.html)

[2] [`scipy.signal.convolve` documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.convolve.html)

[3] [`scipy.signal.fftconvolve` documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.fftconvolve.html)

[4] [`scipy.signal.oaconvolve` documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.oaconvolve.html)

[5] [Matlab's `conv` documentation](https://de.mathworks.com/help/matlab/ref/conv.html)

[6] I. Goodfellow, Y. Bengio, A. Courville *Deep learning*, MIT Press, 2016, [https://www.deeplearningbook.org/](https://www.deeplearningbook.org/).



