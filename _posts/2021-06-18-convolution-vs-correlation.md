---
title: "Convolution vs. Correlation in Signal Processing and Deep Learning"
date: 2021-06-18
author: Jan Wilczek
layout: post
permalink: /convolution-vs-correlation-in-signal-processing-and-deep-learning/
images: assets/img/posts/2021-06-18-convolution-vs-correlation
background: /assets/img/posts/2021-06-18-convolution-vs-correlation/Thumbnail.png
categories:
 - Digital Signal Processing
tags:
 - convolution
 - correlation
discussion_id: 2021-06-18-convolution-vs-correlation
---
Can we calculate correlation using convolution?

<iframe width="560" height="315" src="https://www.youtube.com/embed/R7cn9b7BNyk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### The Convolution Series
1. [Definition of convolution and intuition behind it]({% post_url collections.posts, 2020-06-20-the-secret-behind-filtering %})
1. [Mathematical properties of convolution]({% post_url collections.posts, 2020-07-05-mathematical-properties-of-convolution %})
1. [Convolution property of Fourier, Laplace, and z-transforms]({% post_url collections.posts, 2021-03-18-convolution-in-popular-transforms %})
1. [Identity element of the convolution]({% post_url collections.posts, 2021-04-01-identity-element-of-the-convolution %})
1. [Star notation of the convolution]({% post_url collections.posts, 2021-04-03-star-notation-of-the-convolution-a-notational-trap %})
1. [Circular vs. linear convolution]({% post_url collections.posts, 2021-05-07-circular-vs-linear-convolution %})
1. [Fast convolution]({% post_url collections.posts, 2021-05-14-fast-convolution %})
1. **Convolution vs. correlation**
1. [Convolution in MATLAB, NumPy, and SciPy]({% post_url collections.posts, 2021-07-09-convolution-in-numpy-matlab-and-scipy %})
1. [Deconvolution: Inverse convolution]({% post_url collections.posts, 2021-07-23-deconvolution %})
1. [Convolution in probability: Sum of independent random variables]({% post_url collections.posts, 2021-07-30-convolution-in-probability %})



{% capture _ %}{% increment equationId20210618  %}{% endcapture %}

In many contexts, convolution and correlation are mixed up. One of the biggest sources of this confusion is deep learning, where convolutional neural networks are often implemented using discrete correlation rather than discrete convolution. That is possible, because the order of elements in the convolution masks does not matter: it can be simply learned as flipped [3].

Let's explain the difference between correlation and convolution once and for all.


<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6611455743195468"
     crossorigin="anonymous"></script><ins class="adsbygoogle"
     style="display:block; text-align:center;"
     data-ad-layout="in-article"
     data-ad-format="fluid"
     data-ad-client="ca-pub-6611455743195468"
     data-ad-slot="7289385396"></ins><script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>

## Convolution Definition

Continuous convolution is defined as

$$ x(t) \ast h(t) = \int \limits_{-\infty}^{\infty} x(t - \tau) h(\tau) d\tau.   \quad ({% increment equationId20210618 %})$$

Discrete convolution is defined as

$$ x[n] \ast h[n] = \sum_{k=-\infty}^{\infty} x[n - k] h[k], \quad n \in \mathbb{Z}. \quad ({% increment equationId20210618 %})$$

[Click here]({% post_url collections.posts, 2020-06-20-the-secret-behind-filtering %}) to read about the rationale behind these formulas.

## Correlation Definition

Correlation is a notion from the field of stochastic processes. In signal processing we simply use an entity called the *correlation function* [1] 

$$\phi_{xh}(t) = \int \limits_{-\infty}^{\infty} x(t + \tau) h(\tau) d\tau. \quad ({% increment equationId20210618 %})$$

$\phi_{xx}(t)$ is called the *autocorrelation function*, and $\phi_{xh}(t)$ is called the *cross-correlation function*.

Analogously, we have a correlation function for real-valued discrete-time signals [1]

$$\phi_{xh}[n] = \sum \limits_{k=-\infty}^{\infty} x[n + k]h[k]. \quad ({% increment equationId20210618 %})$$

Sometimes $\phi_{xh}[n]$ is referred to as *correlation sequence* to stress its discrete character [2].

In the subsequent discussion, we assume that the integrals in Equations 1 and 3, and sums in Equations 2 and 4 converge.

### Example

Let's assume we have two signals of length 40, $x[n]$

![]({{ page.images | absolute_url | append: "/x.png" }}){: width="700" }
_Figure 1. $x[n]$._

and $y[n]$

![]({{ page.images | absolute_url | append: "/y.png" }}){: width="700" }
_Figure 2. $y[n]$._

The convolution between $x$ and $y$ is shown in Figure 3

![]({{ page.images | absolute_url | append: "/xy_convolution.png" }}){: width="700" }
_Figure 3. Convolution of $x$ and $y$._

and their correlation in Figure 4.

![]({{ page.images | absolute_url | append: "/xy_correlation.png" }}){: width="700" }
_Figure 4. Correlation of $x$ and $y$._

As you can observe, they are kind of similar.

### Correlation as a Similarity Measure

In the context of signal processing, correlation is interpreted as a similarity measure, i.e., how similar are the two correlated signals for a specific lag in samples (relative shift between the signals).

This concept is best visibile for autocorrelation, which is a measure of *self-similarity*.

In Figure 5, we can see the autocorrelation of signal $x$ from Figure 1.

![]({{ page.images | absolute_url | append: "/xx_autocorrelation.png" }}){: width="700" }
_Figure 5. Autocorrelation of $x$._

Obviously, autocorrelation achieves its peak value for lag $n=0$ because signal is most similar to an unshifted version of itself.

However, two clear maxima can be observed for relative shifts of $n=20$ and $n=-20$. That is because the period of the sine in signal $x$ is exactly 20. 

As you can see, autocorrelation can help us determine the periodicity of a signal. This property is used in pitch estimation (e.g., estimation of the fundamental frequency of the human voice) and also for tempo estimation in the domain of music information retrieval. Autocorrelation can also help us determine whether the observed signal is periodic at all.

## Relation Between Convolution and Correlation

As we can observe, Equations 1 and 3, 2 and 4 and Figures 3 and 4 are somewhat similar. Indeed, only the sign of the "shift" in the argument of $x$ differs. We will now show how to obtain correlation using convolution.

### Discrete Correlation Obtained Using Discrete Convolution

$$\phi_{xh}[n] \\
= \sum \limits_{k=-\infty}^{\infty} x[n + k]h[k] \\
= \sum \limits_{k=-\infty}^{\infty} x[-(-n) + k]h[k] \\
= \sum \limits_{k=-\infty}^{\infty} x[-((-n) - k)]h[k] \\
\stackrel{x_1[l]=x[-l]}{=} \sum \limits_{k=-\infty}^{\infty} x_1[((-n) - k)]h[k] \\
= (x_1[n] \ast h[n])[-n] \\
\stackrel{x[-l]=x_1[l]}{=} (x[-n] \ast h[n])[-n]. \quad ({% increment equationId20210618 %})$$

In the above derivation, we used the "helper function trick", which you can read more about [here]({% post_url collections.posts, 2021-04-03-star-notation-of-the-convolution-a-notational-trap %}).
Index $l$ in the substitution formulas was used not to confuse the reader but it still denotes the discrete-time index.

It turned out that correlation can be obtained by convolving the signals to be correlated, with one of them having its element order reversed, and then reversing the output of the convolution.

### Continuous Correlation Obtained Using Continuous Convolution

Analogously to the discrete case,

$$\phi_{xh}(t) = \int \limits_{-\infty}^{\infty} x(t + \tau) h(\tau) d\tau \\
= \int \limits_{-\infty}^{\infty} x(-((-t) - \tau))) h(\tau) d\tau \\
= (x(-t) \ast h(t))(-t). 
\quad ({% increment equationId20210618 %})$$

## Final Test

To ultimately test the validity of Equation 5, we do a quick in-code test: we generate 100000 samples of uniformly distributed noise, apply the correlation-from-convolution formula, and test for equality to direct correlation up to the machine precision.

```python
import numpy as np
from matplotlib import pyplot as plt


def main():
    rg = np.random.default_rng()
    shape = (100000,)
    x = rg.uniform(-1.0, 1.0, shape)
    y = rg.uniform(-1.0, 1.0, shape)

    correlation_from_convolution = np.flip(
        np.convolve(np.flip(x), y, 'full'))
    correlation = np.correlate(x, y, 'full')

    np.testing.assert_array_almost_equal(
        correlation_from_convolution, correlation, decimal=10)

if __name__=='__main__':
    main()
```

## Application

The fact that correlation can be obtained using convolution is significant. For example, one could use the [fast convolution algorithms]({% post_url collections.posts, 2021-05-14-fast-convolution %}) to compute correlation efficiently; that is the basis of *fast correlation* algorithms [2].

This fact also points to how closely convolution and correlation are related. This similarity was mentioned in the introduction in the context of deep learning, where terms "convolution" and "correlation" are used interchangeably [3]. What is more, exactly as we have circular convolution, we also have *circular correlation*. However, the correlation function does not have many useful properties that [convolution has]({% post_url collections.posts, 2020-07-05-mathematical-properties-of-convolution %}), e.g., correlation is not commutative [3].

## Bibliography

[1] Alan V. Oppenheim, Alan S. Willsky, with S. Hamid *Signals and Systems*, 2nd Edition, Pearson 1997.

[2] Alan V Oppenheim, Ronald W. Schafer *Discrete-Time Signal Processing*, 3rd Edition, Pearson 2010.

[3] I. Goodfellow, Y. Bengio, A. Courville *Deep learning*, MIT Press, 2016, [https://www.deeplearningbook.org/](https://www.deeplearningbook.org/).


