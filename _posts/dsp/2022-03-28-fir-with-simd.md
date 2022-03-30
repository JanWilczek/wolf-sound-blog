---
title: "Efficient FIR Filter Implementation with SIMD"
description: "Speed up time-domain filtering via vectorization for virtual reality, computer games, and digital audio workstation plugins."
date: 2022-03-28
author: Jan Wilczek
layout: post
images: /assets/img/posts/dsp/2022-03-28-fir-with-simd/
# background: /assets/img/posts/dsp/2022-03-28-fir-with-simd/Thumbnail.webp
categories:
  - Digital Signal Processing
  - Audio FX
tags:
  - filtering 
  - effects
  - simd
  - C++
  - C
discussion_id: 2022-03-28-fir-with-simd
---
How to make your FIR filters fast in the time domain?

{% katexmm %}
{% capture _ %}{% increment equationId20220328  %}{% endcapture %}
{% capture _ %}{% increment listingId20220328  %}{% endcapture %}
{% capture _ %}{% increment figureId20220328  %}{% endcapture %}

If you want to make any software execute as fast as possible, there are two ways in which you can achieve this:

1. Optimal algorithm.
2. Efficient implementation.

The same principles apply to digital signal processing (DSP) code. To have a fast [finite-impulse response (FIR) filter]({% post_url 2020-06-20-the-secret-behind-filtering %}) in code, you can either

1. use an algorithm with a optimal lower bound on execution time, such as [fast convolution via the Fourier transform domain]({% post_url 2021-05-14-fast-convolution %}), or
2. take advantage of hardware and software resources to efficiently implement time-domain convolution. This typically means using the [single instruction, multiple data (SIMD) instructions]({% post_url fx/2022-02-12-simd-in-dsp %}) to vectorize your code.

<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6611455743195468"
     crossorigin="anonymous"></script><ins class="adsbygoogle"
     style="display:block; text-align:center;"
     data-ad-layout="in-article"
     data-ad-format="fluid"
     data-ad-client="ca-pub-6611455743195468"
     data-ad-slot="7289385396"></ins><script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>

## When Should We Use Time-Domain Filtering?

You may be asking yourself

> Since we have **fast** convolution, why would we ever need a time-domain implementation of it?

The fast convolution algorithm's lower bound on its execution time is of $O(N \log N)$ type, where $N$ could be the length of the input signal or the filter (let's not specify this exactly because it depends on the case). The lower bound on the linear convolution's execution time is of $O(N^2)$ type [Wefers2015].

First of all, it means that for sufficiently small $N$, the linear convolution algorithm will be faster than the fast convolution algorithm.

Second of all, if we vectorize our code wisely, we may be able to create an even larger advantage for the linear convolution. That is thanks to the fact, that fast convolution operates on complex numbers, whereas linear convolution always uses real numbers.

If that confuses you, think about sorting algorithms. In general, [Quicksort](https://en.wikipedia.org/wiki/Quicksort) is considered to be the fastest sorting algorithm. But if you look at sorting implementations, such as `std::sort`, you will see that after dividing the sorted container into sufficiently small parts, a quadratic algorithm, such as [insertion sort](https://en.wikipedia.org/wiki/Insertion_sort) is used to sort the elements within. (I've just found that this strategy is called [Introsort](https://en.wikipedia.org/wiki/Introsort) 😃).

With that explain, we can look into how to efficiently implement FIR filtering in the time domain.

## How to speed up FIR filter Implementation?

In short: via SIMD.

The best way to speed up filtering is to process multiple samples at once using single instruction, multiple data instructions. To achieve this, we need to rewrite the linear convolution algorithm so that it our code operates on vectors.

This process is called *loop vectorization*.

Loop vectorization is often done by the compiler but the degree of this vectorization is insufficient for real-time DSP. Instead, we need to instruct the compiler what to do.

SIMD instructions achieve the best performance when they operate on [aligned data]({% post_url 2020-04-09-what-is-data-alignment %}). Therefore, data alignment is another factor we should take into account.

In summary, an efficient FIR filter implementation uses 2 strategies in tandem:

1. Loop vectorization
2. Data alignment.

We will now discuss these two strategies in detail.

## Preliminary Assumptions

The [linear convolution formula]({% post_url 2020-06-20-the-secret-behind-filtering %}#definition) is

$$ x[n] \ast h[n] = \sum_{k=-\infty}^{\infty} x[k] h[n - k] = y[n], \quad n \in \mathbb{Z}. \quad ({% increment equationId20220328  %})$$

As you might guess, an infinite sum is not very practical. Additionally, reversing the time in the $h$ signal is quite problematic to think about in code. Therefore, we will make some assumptions, which, however, won't change the general nature of our discussion.

### Finite-Length Signals

We will assume that our signals are finite. This was of course true of $h$ but not necessarily of $x$.

We will denote $x$'s length by $N_x$ and $h$'s length by $N_h$.

For indices below 0 or above signals' lengths, the signal is assumed to be 0.

### Time-Reversing the Filter Coefficients

In practical real-time audio scenarios, like virtual reality, computer games, or digital audio workstations, we know $h$ but don't know $x$.

Therefore, we can time-reverse $h$ right away and reason only about the reversed signal.

In other words, we define signal $c$ of length $N_h$

$$c[n] = h[N_h - n - 1], \quad n = 0, \dots, N_h - 1, \quad ({% increment equationId20220328  %}).$$

**We assume that $c$ is 0 everywhere else.**

### Practical Convolution Formula

After introducing these two assumptions, we can rewrite the convolution formula from Equation 1 into 

$$ y[n] = (x[n] \ast h[n])[n] \\= \sum_{k=0}^{N_h-1} x[n+k] c[k], \quad n = 0, \dots, N_x + N_h - 1. \quad ({% increment equationId20220328  %})$$

This formulation resembles the [correlation]({% post_url 2021-06-18-convolution-vs-correlation %}#correlation-definition) formula a lot but remember that it's still [convolution]({% post_url 2021-06-18-convolution-vs-correlation %}#convolution-definition) albeit written differently.

Note also that Equation 3 is convolution in [same]({% post_url 2021-07-09-convolution-in-numpy-matlab-and-scipy %}#same) mode, i.e., $y[0]$ corresponds to $y[N_h-1]$ of the full mode. 

If we prepend $x$ with $N_h - 1$ zeros, we will get convolution in the [full]({% post_url 2021-07-09-convolution-in-numpy-matlab-and-scipy %}#full) mode.

As you will see, this will simplify our discussion significantly.

### Visualization of Convolution

Equation 3 is visualized on Figure 1. It show which elements are multiplied to calculate $y[0]$.

![]({{ page.images | append: "LoopVectorizationSingle.svg" }}){: alt="Scalar linear convolution visualization."}
_Figure {% increment figureId20220328 %}. Convolution as an inner product of the input vector and the reversed filter coefficients vector._

Orange frames mark which elements are multiplied together to compute $y[0]$. The results of multiplications are then summed for the final result.

With the above assumptions and the convolution format, we may write its implementation.

## Naive Linear Convolution

Before we improve on the speed of our FIR filter with SIMD, we need to start with a baseline: a non-SIMD implementation.

_The full (very ugly) code referenced in this article [can be found in my GitHub repository](https://github.com/JanWilczek/fir-simd.git)._

That can be implemented as follows.

_Listing {% increment listingId20220328  %}._
```cpp
struct FilterInput {
// assume that these fields are correctly initialized
  const float* x;  // input signal
  size_t inputLength;
  const float* c;  // reversed filter coefficients
  size_t filterLength;
  float* y;  // output (filtered) signal
  size_t outputLength;
};


float* applyFirFilterSingle(FilterInput<float>& input) {
  const auto* x = input.x;
  const auto* c = input.c;
  auto* y = input.y;

  for (auto i = 0u; i < input.outputLength; ++i) {
    y[i] = x[0] * c[0];
    for (auto j = 1u; j < input.filterLength; ++j) {
      y[i] += x[i + j] * c[j];
    }
  }
  return y;
}
```

Each multiplication in the inner loop corresponds to one orange frame from Figure 1.

As you can see, this code is not very efficient; we iterate by samples, one-by-one.

Because of the zero-padding, the time complexity of this code is $O(N_h (N_h + N_x - 1))$ (we multiply $N_h$ filter coefficients as many times as there are output samples).

Let's see how we can vectorize this code...


## Loop Vectorization

There are 3 types of loop vectorization in the context of FIR filtering:

1. Inner loop vectorization (VIL),
2. Outer loop vectorization (VOL),
3. Outer and inner loop vectorization (VOIL).

Their names specify where we load the data to the SIMD registers. The easiest one to understand is the inner loop vectorization.

## Inner Loop Vectorization (VIL)

In _inner loop vectorization_, we vectorize (rewrite in vector notation) the behavior of the inner loop from Listing 1. 

Let's write that in a verbose manner (Listing 2). We assume that our vectors are of length 4. That would correspond to registers that can fit 4 floats (for example, [ARM's Neon registers]({% post_url fx/2022-02-12-simd-in-dsp %}#mmx-sse-avx-neon)).

_Listing {% increment listingId20220328 %}_
```cpp
std::vector<float> applyFirFilterInnerLoopVectorization(
    FilterInput<float>& input) {
  const auto* x = input.x;
  const auto* c = input.c;
  auto* y = input.y;

  for (auto i = 0u; i < input.outputLength; ++i) {
    y[i] = 0.f;
    for (auto j = 0u; j < input.filterLength; j += 4) {
      y[i] += x[i + j] * c[j] + x[i + j + 1] * c[j + 1] +
              x[i + j + 2] * c[j + 2] + x[i + j + 3] * c[j + 3];
    }
  }
  return input.output();
}
```

Verbalizing the above code, we can say that in each iteration of the inner loop we do the inner product of 4-element vectors $[x[i + j], x[i + j + 1], x[i + j + 2], x[i + j + 3]]$ and $[c[j], c[j+1], c[j+2], c[j+3]]$. With this, we compute a part of the convolution sum from Equation 3.

Mind you that we assume that the passed in vectors are already zero-padded and are of length which is a multiplicity of 4.

Of course, code from Listing 2 is not more optimal than the code from Listing 1. It is merely rewritten into vector form. But this vector form is now easy to implement with vector instructions.

How does this implementation look in real SIMD code?

### VIL AVX Implementation

For convenience, I am using the [AVX instruction set] to show example implementations. Its instructions are the most readable from all SIMD I know so they should be easy to understand.

Listing 3 shows how to implement the FIR filter using inner loop vectorization.

_Listing {% increment listingId20220328 %}_
```cpp
#ifdef __AVX__
// The number of floats that fit into an AVX register.
constexpr auto AVX_FLOAT_COUNT = 8u;

float* applyFirFilterAVX_innerLoopVectorization(
    FilterInput<float>& input) {
  const auto* x = input.x;
  const auto* c = input.c;
  const auto* y = input.y;

  // A fixed-size array to move the data from registers into
  std::array<float, AVX_FLOAT_COUNT> outStore;

  // Inner loop vectorization
  for (auto i = 0u; i < input.outputLength; ++i) {
    // Set a SIMD register to all zeros;
    // we will use it as an accumulator
    auto outChunk = _mm256_setzero_ps();

    for (auto j = 0u; j < input.filterLength; j += AVX_FLOAT_COUNT) {
      // Load the unaligned input signal data into a SIMD register
      auto xChunk = _mm256_loadu_ps(x + i + j);
      // Load the unaligned reversed filter coefficients into a SIMD register
      auto cChunk = _mm256_loadu_ps(c + j);

      // Multiply both above registers element-wise
      auto temp = _mm256_mul_ps(xChunk, cChunk);

      // Element-wise add to the accumulator
      outChunk = _mm256_add_ps(outChunk, temp);
    }

    // Transfer the contents of the accumulator the array
    _mm256_storeu_ps(outStore.data(), outChunk);

    // Sum the partial sums in the accumulator and assign to the output
    y[i] = std::accumulate(outStore.begin(), outStore.end(), 0.f);
  }

  return y;
}
#endif
```

Again, we assume that the passed in vectors are already zero-padded and are of length which is a multiplicity of 8 (number of floats we can fit into an AVX register).

This has time complexity equal to $O(\frac{N_h}{8} (N_h + N_x -1))$. Of course, in complexity theory that's the same as the above algorithm. But notice that in the inner loop we do 8 times less iterations. That is because we can operate on vectors of 8 floats with single AVX instructions. So excuse my improper math 😉 

## Outer Loop Vectorization (VOL)

Outer loop vectorization is a little bit crazy. In this approach we try to compute a vector of outputs at once in one outer iteration.

In Listing 4, there is the FIR filter code from Listing 1 rewritten in terms of vectors.

_Listing {% increment listingId20220328 %}_
```cpp
std::vector<float> applyFirFilterOuterLoopVectorization(
    FilterInput<float>& input) {
  const auto* x = input.x;
  const auto* c = input.c;
  auto* y = input.y;

  for (auto i = 0u; i < input.outputLength; i += 4) {
    y[i] = 0.f;
    y[i + 1] = 0.f;
    y[i + 2] = 0.f;
    y[i + 3] = 0.f;
    for (auto j = 0u; j < input.filterLength; ++j) {
      y[i] += x[i + j] * c[j];
      y[i + 1] += x[i + j + 1] * c[j];
      y[i + 2] += x[i + j + 2] * c[j];
      y[i + 3] += x[i + j + 3] * c[j];
    }
  }
  return input.output();
}
```

Again, we assume that the passed in vectors are already zero-padded and are of length which is a multiplicity of 4.

This code is now easy to implement with SIMD instructions.

### VOL AVX Implementation

Listing 5 shows how to implement FIR filtering in AVX instructions using outer loop vectorization.

_Listing {% increment listingId20220328 %}_
```cpp
#ifdef __AVX__
float* applyFirFilterAVX_outerLoopVectorization(
    FilterInput<float>& input) {
  const auto* x = input.x;
  const auto* c = input.c;
  auto* y = input.y;

  for (auto i = 0u; i < input.outputLength; i += AVX_FLOAT_COUNT) {
    auto yChunk = _mm256_setzero_ps();

    for (auto j = 0u; j < input.filterLength; ++j) {
      auto xChunk = _mm256_loadu_ps(x + i + j);
      auto cChunk = _mm256_set1_ps(c[j]);

      auto temp = _mm256_mul_ps(xChunk, cChunk);

      yChunk = _mm256_add_ps(yChunk, temp);
    }

    _mm256_storeu_ps(y + i, yChunk);
  }

  return y;
}
#endif
```

This code should be 8 times faster than the one in Listing 1. Of course, the typical speedup wili much smaller.

<!-- TODO: How much smaller? -->

A question arises: can we do even better? Yes, we can!

## Outer and Inner Loop vectorization (VOIL)

The real breakthrough comes when we combine both types of vectorization.

In this approach, we compute 4 outputs on each pass of the outer loop (outer loop vectorization) and compute an inner product of 4-element vectors (a part of the convolution sum) in each pass of the inner loop (inner loop vectorization).

In verbose code, VOIL is presented in Listing 6.

_Listing {% increment listingId20220328 %}_
```cpp
std::vector<float> applyFirFilterOuterInnerLoopVectorization(
    FilterInput<float>& input) {
  const auto* x = input.x;
  const auto* c = input.c;
  auto* y = input.y;

  for (auto i = 0u; i < input.outputLength; i += 4) {
    y[i] = 0.f;
    y[i + 1] = 0.f;
    y[i + 2] = 0.f;
    y[i + 3] = 0.f;
    for (auto j = 0u; j < input.filterLength; j += 4) {
      y[i] += x[i + j] * c[j] + x[i + j + 1] * c[j + 1] +
              x[i + j + 2] * c[j + 2] + x[i + j + 3] * c[j + 3];

      y[i + 1] += x[i + j + 1] * c[j + 1] + x[i + j + 2] * c[j + 2] +
                  x[i + j + 3] * c[j + 3] + x[i + j + 4] * c[j + 4];

      y[i + 2] += x[i + j + 2] * c[j + 2] + x[i + j + 3] * c[j + 3] +
                  x[i + j + 4] * c[j + 4] + x[i + j + 5] * c[j + 5];

      y[i + 3] += x[i + j + 3] * c[j + 3] + x[i + j + 4] * c[j + 4] +
                  x[i + j + 5] * c[j + 5] + x[i + j + 6] * c[j + 6];
    }
  }
  return input.output();
}
```

### VOIL AVX Implementation

```cpp
#ifdef __AVX__
std::vector<float> applyFirFilterAVX_outerInnerLoopVectorization(
    FilterInput<float>& input) {
  const auto* x = input.x;
  const auto* c = input.c;

  std::array<float, AVX_FLOAT_COUNT> outStore;

  alignas(AVX_FLOAT_COUNT * alignof(float)) std::array<__m256, AVX_FLOAT_COUNT>
      outChunk;

  for (auto i = 0u; i < input.outputLength; i += AVX_FLOAT_COUNT) {
    for (auto k = 0u; k < AVX_FLOAT_COUNT; ++k) {
      outChunk[k] = _mm256_setzero_ps();
    }

    for (auto j = 0ul; j < input.filterLength; j += AVX_FLOAT_COUNT) {
      auto cChunk = _mm256_loadu_ps(c + j);

      for (auto k = 0ul; k < AVX_FLOAT_COUNT; ++k) {
        auto xChunk = _mm256_loadu_ps(x + i + j + k);

        auto temp = _mm256_mul_ps(xChunk, cChunk);

        outChunk[k] = _mm256_add_ps(outChunk[k], temp);
      }
    }

    for (auto k = 0u; k < AVX_FLOAT_COUNT; ++k) {
      _mm256_storeu_ps(outStore.data(), outChunk[k]);

      if (i + k < input.outputLength)
        input.y[i + k] = std::accumulate(outStore.begin(), outStore.end(), 0.f);
    }
  }

  return input.output();
}
#endif
```

## Data alignment

## Bibliography

{% endkatexmm %}
