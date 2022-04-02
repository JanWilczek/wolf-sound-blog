---
title: "Efficient FIR Filter Implementation with SIMD"
description: "Speed up time-domain filtering via vectorization for virtual reality, computer games, and digital audio workstation plugins."
date: 2022-03-28
author: Jan Wilczek
layout: post
images: /assets/img/posts/dsp/2022-03-28-fir-with-simd/
permalink: /fir-filter-with-simd/
# background: /assets/img/posts/dsp/2022-03-28-fir-with-simd/Thumbnail.webp
categories:
  - Digital Signal Processing
  - Audio FX
tags:
  - filtering 
  - effects
  - simd
  - convolution
  - C++
  - C
discussion_id: 2022-03-28-fir-with-simd
---
How to make your FIR filters fast in the time domain?

Finite-impulse response (FIR) filtering is the cornerstone of digital signal processing (DSP). It is especially important in applying reverberation to the audio signal, for example, in virtual reality audio or in VST plugins of digital audio workstations. It has also been extensively used on mobile phones (even pre-smartphones!) and embedded devices for sound applications. 

How to perform it fast?

### Table of Contents

1. [What Are FIR Filters?](#what-are-fir-filters)
2. [2 Sides of Optimization](#2-sides-of-optimization)
3. [When Should We Use Time-Domain Filtering?](#when-should-we-use-time-domain-filtering)
4. [How to Speed Up FIR Filter Implementation?](#how-to-speed-up-fir-filter-implementation)
5. [Preliminary Assumptions](#preliminary-assumptions)
   1. [Finite-Length Signals](#finite-length-signals)
   2. [Time-Reversing the Filter Coefficients](#time-reversing-the-filter-coefficients)
   3. [Practical Convolution Formula](#practical-convolution-formula)
   4. [Visualization of Convolution](#visualization-of-convolution)
6. [Naive Linear Convolution](#naive-linear-convolution)
7. [Loop Vectorization](#loop-vectorization)
8. [Inner Loop Vectorization (VIL)](#inner-loop-vectorization-vil)
   1. [VIL AVX Implementation](#vil-avx-implementation)
9. [Outer Loop Vectorization (VOL)](#outer-loop-vectorization-vol)
   1. [VOL AVX Implementation](#vol-avx-implementation)
1. [Outer and Inner Loop vectorization (VOIL)](#outer-and-inner-loop-vectorization-voil)
   1. [Why Is This More Optimal?](#why-is-this-more-optimal)
      1. [Data Alignment](#data-alignment)
   2. [VOIL AVX Implementation](#voil-avx-implementation)
1. [Summary](#summary)
1. [Bibliography](#bibliography)

{% katexmm %}
{% capture _ %}{% increment equationId20220328  %}{% endcapture %}
{% capture _ %}{% increment listingId20220328  %}{% endcapture %}
{% capture _ %}{% increment figureId20220328  %}{% endcapture %}

## What Are FIR Filters?

FIR filters are filters, which are defined by their finite-length impulse response, $h[n]$. The output $y[n]$ of an FIR filter is a [convolution]({% post_url 2020-06-20-the-secret-behind-filtering %}) of its input signal $x[n]$ with the impulse response. We can write it as

$$y[n] = x[n] \ast h[n] = \sum \limits_{k=-\infty}^{\infty} x[k] h[n - k].  \quad ({% increment equationId20220212 %})$$

I have published [a number of articles and videos on convolution]({% post_url 2020-06-20-the-secret-behind-filtering %}), which you can check out for more insight.

<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6611455743195468"
     crossorigin="anonymous"></script><ins class="adsbygoogle"
     style="display:block; text-align:center;"
     data-ad-layout="in-article"
     data-ad-format="fluid"
     data-ad-client="ca-pub-6611455743195468"
     data-ad-slot="7289385396"></ins><script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>

## 2 Sides of Optimization

If you want to make any software execute as fast as possible, there are two ways in which you can achieve this:

1. Optimal algorithm.
2. Efficient implementation.

The same principles apply to DSP code. To have a fast [finite-impulse response (FIR) filter]({% post_url 2020-06-20-the-secret-behind-filtering %}) in code, you can either

1. use an algorithm with a optimal lower bound on execution time, such as the [fast convolution via the Fourier transform domain]({% post_url 2021-05-14-fast-convolution %}), or
2. take advantage of hardware and software resources to efficiently implement time-domain convolution. This typically means using [single instruction, multiple data (SIMD) instructions]({% post_url fx/2022-02-12-simd-in-dsp %}) to vectorize your code.



## When Should We Use Time-Domain Filtering?

You may be asking yourself

> Since we have a **fast** convolution algorithm, why would we ever need a time-domain implementation of it?

The fast convolution algorithm's lower bound on its execution time is of $O(N \log N)$ type, where $N$ could be the length of the input signal or the filter (let's not specify this exactly because it depends on the case). The lower bound on the linear convolution's execution time is of $O(N^2)$ type [Wefers2015].

First of all, it means that for sufficiently small $N$, the linear convolution algorithm will be faster than the fast convolution algorithm.

Second of all, fast convolution operates on complex numbers, whereas linear convolution always uses real numbers. This effectively means that the fast convolution needs to process twice as much data as the linear convolution. 

If the fact that the time-domain convolution may be faster than the fast convolution confuses you, think about sorting algorithms. In general, [quicksort](https://en.wikipedia.org/wiki/Quicksort) is considered to be the fastest sorting algorithm. But if you look at sorting implementations, such as `std::sort`, you will see that it only initially uses the quicksort. After dividing the sorted container into sufficiently small parts, a quadratic algorithm, such as [insertion sort](https://en.wikipedia.org/wiki/Insertion_sort), is used to sort the elements within. (I've just found that this strategy is called [introsort](https://en.wikipedia.org/wiki/Introsort) 😃).

With that explained, we can look into how to efficiently implement FIR filtering in the time domain.

## How to Speed Up FIR Filter Implementation?

In short: via SIMD.

The best way to speed up filtering is to process multiple samples at once using single instruction, multiple data (SIMD) instructions. To achieve this, we need to rewrite the linear convolution algorithm so that our code operates on vectors.

This process is called *loop vectorization*.

Loop vectorization is often done by the compiler but the degree of this automatic vectorization is typically insufficient for real-time DSP. Instead, we need to instruct the compiler exactly what to do.

SIMD instructions achieve the best performance when they operate on [aligned data]({% post_url 2020-04-09-what-is-data-alignment %}). Therefore, data alignment is another factor we should take into account.

In summary, an efficient FIR filter implementation uses 2 strategies in tandem:

1. Loop vectorization and
2. Data alignment.

We will now discuss these two strategies in detail.

<div class="card summary">
    <div class="card-body">
    <h3 class="card-title">Why not GPU?</h3>
    <hr>

    <p>
    SIMD instructions are not limited to CPUs but we'll be considering only SIMD from CPUs in this article.
    </p>

    <p>
    Someone could ask: *why don't we use GPUs for FIR filtering?*
    </p>

    <p>
    Well, for the same reason that we don't use multithreading in real-time audio processing code. 
    </p>
    
    <p>
    A complete audio processing chain must typically be calculated within one block of audio (typically 10 milliseconds). Although multi-threaded processing on CPUs and GPUs can be very efficient, it is not 100% predictable; we cannot determine when which resource will be available for processing. The cost of thread synchronization (implying system calls) would be too high. Additionally, transporting data to GPU and retrieving it incurs even more unknown overhead.
    </p>

    <p>
    That is why, in today's real-time audio processing applications, single-core CPU processing prevails. The audio thread must never stop!
    </p>

    </div>
</div>

## Preliminary Assumptions

The [linear convolution formula]({% post_url 2020-06-20-the-secret-behind-filtering %}#definition) is

$$ x[n] \ast h[n] = \sum_{k=-\infty}^{\infty} x[k] h[n - k] = y[n], \quad n \in \mathbb{Z}. \quad ({% increment equationId20220328  %})$$

As you might guess, an infinite sum is not very practical for implementation. Additionally, reversing the time in the $h$ signal is quite problematic to think about in code. Therefore, we will make some assumptions, which, however, won't change the general nature of our discussion.

### Finite-Length Signals

We will assume that our signals are finite. This was of course true of $h$ but not necessarily of $x$.

We will denote $x$'s length by $N_x$ and $h$'s length by $N_h$.

We also assume that $N_x$ > $N_h$.

For indices below 0 or above signals' lengths, the signals are assumed to be 0.

### Time-Reversing the Filter Coefficients

In practical real-time audio scenarios, like virtual reality, computer games, or digital audio workstations, we know $h$ but don't know $x$.

Therefore, we can time-reverse $h$ right away and reason only about the reversed signal.

In other words, we define signal $c$ of length $N_h$ such that

$$c[n] = h[N_h - n - 1], \quad n = 0, \dots, N_h - 1. \quad ({% increment equationId20220328  %}).$$

We assume that $c$ is 0 everywhere else.

### Practical Convolution Formula

After introducing these two assumptions, we can rewrite the convolution formula from Equation 1 into 

$$ y[n] = (x[n] \ast h[n])[n] \\= \sum_{k=0}^{N_h-1} x[n+k] c[k], \quad n = 0, \dots, N_x - 1. \quad ({% increment equationId20220328  %})$$

This formulation resembles the [correlation]({% post_url 2021-06-18-convolution-vs-correlation %}#correlation-definition) formula a lot but remember that it's still [convolution]({% post_url 2021-06-18-convolution-vs-correlation %}#convolution-definition) albeit written differently.

In this new formulation, one convolution output is simply an *inner product* of two vectors $\pmb{x}$ and $\pmb{c}$, each containing $N_h$ values from $x$ and $c$ respectively.

Note also that Equation 3 is a convolution in the ["same"]({% post_url 2021-07-09-convolution-in-numpy-matlab-and-scipy %}#same) mode, i.e., $y[0]$ corresponds to $y[N_h-1]$ of the full mode. 

If we prepend $x$ with $N_h - 1$ zeros, we will get a convolution in the ["full"]({% post_url 2021-07-09-convolution-in-numpy-matlab-and-scipy %}#full) mode.

As you will see, this will simplify our discussion significantly.

### Visualization of Convolution

Equation 3 is visualized on Figure 1. It show which elements are multiplied to calculate $y[0]$.

![]({{ page.images | append: "LoopVectorizationSingle.svg" }}){: alt="Scalar linear convolution visualization."}
_Figure {% increment figureId20220328 %}. Convolution as an inner product of the input vector and the reversed filter coefficients vector._

The orange frames mark which elements are multiplied together to compute $y[0]$. The results of multiplications are then summed up for the final result.

With the above assumptions and the convolution format, we may write its implementation.

## Naive Linear Convolution

Before we improve on the speed of our FIR filter with SIMD, we need to start with a baseline: a non-SIMD implementation.

_The full code referenced in this article [can be found in my GitHub repository](https://github.com/JanWilczek/fir-simd.git)._

That can be implemented as follows.

_Listing {% increment listingId20220328  %}. Plain linear convolution._
```cpp
struct FilterInput {
// assume that these fields are correctly initialized
  const float* x;  // input signal with (N_h-1) zeros appended
  size_t inputLength;   // N_x
  const float* c;  // reversed filter coefficients
  size_t filterLength;  // N_h
  float* y;  // output (filtered) signal; 
             // pointer to preallocated, uninitialized memory
  size_t outputLength; // should be N_x in our context
};


float* applyFirFilterSingle(FilterInput& input) {
  const auto* x = input.x;
  const auto* c = input.c;
  auto* y = input.y;

  for (auto i = 0u; i < input.outputLength; ++i) {
    y[i] = 0.f;
    for (auto j = 0u; j < input.filterLength; ++j) {
      y[i] += x[i + j] * c[j];
    }
  }
  return y;
}
```

Each multiplication in the inner loop corresponds to one orange frame from Figure 1.

As you can see, this code is not very efficient; we iterate the samples one by one.

The time complexity of this code is $O(N_h N_x)$ (we perform $N_h$ multiplications as many times as there are output samples).

Let's see how we can vectorize this code...


## Loop Vectorization

There are 3 types of loop vectorization in the context of FIR filtering:

1. Inner loop vectorization (VIL),
2. Outer loop vectorization (VOL),
3. Outer and inner loop vectorization (VOIL).

Their names specify at which line of Listing 1 we load the data to the SIMD registers. The easiest one to understand is the inner loop vectorization.

## Inner Loop Vectorization (VIL)

In the _inner loop vectorization_, we vectorize (rewrite in vector notation) the behavior of the inner loop from Listing 1. 

Let's write that in a verbose manner (Listing 2). We assume that our vectors are of length 4. That would correspond to registers that can fit 4 floats (for example, [ARM's Neon registers]({% post_url fx/2022-02-12-simd-in-dsp %}#mmx-sse-avx-neon)).

_Listing {% increment listingId20220328 %}. Conceptual inner loop vectorization_
```cpp
float* applyFirFilterInnerLoopVectorization(
    FilterInput& input) {
  const auto* x = input.x;
  const auto* c = input.c;
  auto* y = input.y;

  for (auto i = 0u; i < input.outputLength; ++i) {
    y[i] = 0.f;
    // Note the increment by 4
    for (auto j = 0u; j < input.filterLength; j += 4) {
      y[i] += x[i + j] * c[j] + 
              x[i + j + 1] * c[j + 1] +
              x[i + j + 2] * c[j + 2] + 
              x[i + j + 3] * c[j + 3];
    }
  }
  return y;
}
```

Verbalizing the above code, we can say that in each iteration of the inner loop we do the inner product of two 4-element vectors $[x[i + j], x[i + j + 1], x[i + j + 2], x[i + j + 3]]$ and $[c[j], c[j+1], c[j+2], c[j+3]]$. With this, we compute a part of the convolution sum from Equation 3.

Mind you that we assume that the passed-in vectors are already zero-padded and are of length which is a multiplicity of 4.

Figure 2 shows what happens in inner loop vectorization.

![]({{ page.images | append: "LoopVectorizationVIL.svg" }}){: alt="Convolution via inner loop vectorization visualization."}
_Figure {% increment figureId20220328 %}. Inner loop vectorization._

Vectors in orange frames have their inner product calculated in the inner loop (hence the name). Again, one orange frame corresponds to one inner loop iteration.

Of course, the code from Listing 2 is not more optimal than the code from Listing 1. It is merely rewritten in the vector form. But this vector form is now easy to implement with vector instructions.

How does this implementation look in real SIMD code?

### VIL AVX Implementation

For convenience, I am using the [intrinsic functions]({% post_url fx/2022-02-12-simd-in-dsp %}#how-to-access-simd-instructions) of the [AVX instruction set]({% post_url fx/2022-02-12-simd-in-dsp %}#mmx-sse-avx-neon) to show example implementations. Its instructions are the most readable from all SIMD instruction sets I know so they should be easy to understand.

Listing 3 shows how to implement the FIR filter using the inner loop vectorization.

_Listing {% increment listingId20220328 %}. Inner loop vectorization with AVX._
```cpp
#ifdef __AVX__
// The number of floats that fit into an AVX register.
constexpr auto AVX_FLOAT_COUNT = 8u;

float* applyFirFilterAVX_innerLoopVectorization(
    FilterInput& input) {
  const auto* x = input.x;
  const auto* c = input.c;
  const auto* y = input.y;

  // A fixed-size array to move the data from registers into
  std::array<float, AVX_FLOAT_COUNT> outStore;

  for (auto i = 0u; i < input.outputLength; ++i) {
    // Set a SIMD register to all zeros;
    // we will use it as an accumulator
    auto outChunk = _mm256_setzero_ps();

    // Note the increment
    for (auto j = 0u; j < input.filterLength; j += AVX_FLOAT_COUNT) {
      // Load the unaligned input signal data into a SIMD register
      auto xChunk = _mm256_loadu_ps(x + i + j);
      // Load the unaligned reversed filter coefficients 
      // into a SIMD register
      auto cChunk = _mm256_loadu_ps(c + j);

      // Multiply the both registers element-wise
      auto temp = _mm256_mul_ps(xChunk, cChunk);

      // Element-wise add to the accumulator
      outChunk = _mm256_add_ps(outChunk, temp);
    }

    // Transfer the contents of the accumulator 
    // to the output array
    _mm256_storeu_ps(outStore.data(), outChunk);

    // Sum the partial sums in the accumulator and assign to the output
    y[i] = std::accumulate(outStore.begin(), outStore.end(), 0.f);
  }

  return y;
}
#endif
```

Again, we assume that the passed-in vectors are already zero-padded and are of length which is a multiplicity of 8 (the number of floats we can fit into an AVX register).

This has time complexity equal to $O(N_h N_x / 8)$. Of course, in complexity theory that's the same as the non-vectorized algorithm. But notice that in the inner loop we do 8 times fewer iterations. That is because we can operate on vectors of 8 floats with single AVX instructions. So excuse my improper math 😉 

## Outer Loop Vectorization (VOL)

Outer loop vectorization is a little bit more crazy. In this approach, we try to compute a vector of outputs at once in one outer iteration.

In Listing 4, there is the FIR filter code from Listing 1 rewritten in terms of 4-element vectors.

_Listing {% increment listingId20220328 %}. Conceptual outer loop vectorization._
```cpp
float* applyFirFilterOuterLoopVectorization(
    FilterInput& input) {
  const auto* x = input.x;
  const auto* c = input.c;
  auto* y = input.y;

  // Note the increment by 4
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
  return y;
}
```

Again, we assume that the passed-in vectors are already zero-padded and are of length which is a multiplicity of 4.

Figure 3 shows how code from Listing 4 works.

![]({{ page.images | append: "LoopVectorizationVOL.svg" }}){: alt="Convolution via outer loop vectorization visualization."}
_Figure {% increment figureId20220328 %}. Outer loop vectorization._

Again, one frame corresponds to one inner loop iteration and again it shows which elements of $x$ and $h$ are multiplied to compute $y[0]$. In a way, it can be thought of as multiplying each 4-element vector from $x$ by a scalar (one element from $c$).

The resulting 4-element vectors (results of multiplications within the frames) are summed up to produce 4 outputs in one iteration of the outer loop.

So instead of computing 4 elements from the convolution sum in the inner loop (as in VIL), we compute 1 element from 4 convolution sums. In VIL we had 4 times fewer inner loop iterations, in VOL we have 4 times fewer outer loop iterations.

Thus, VOL is not more optimal than VIL.

This code is now easy to implement with SIMD instructions.

### VOL AVX Implementation

Listing 5 shows how to implement FIR filtering in AVX instructions using outer loop vectorization.

`FilterInput` and `AVX_FLOAT_COUNT` are defined as before.

_Listing {% increment listingId20220328 %}. Outer loop vectorization in AVX._
```cpp
#ifdef __AVX__
float* applyFirFilterAVX_outerLoopVectorization(
    FilterInput& input) {
  const auto* x = input.x;
  const auto* c = input.c;
  auto* y = input.y;

  // Note the increment
  for (auto i = 0u; i < input.outputLength; i += AVX_FLOAT_COUNT) {
    // Set 8 computed outputs initially to 0
    auto yChunk = _mm256_setzero_ps();

    for (auto j = 0u; j < input.filterLength; ++j) {
      // Load an 8-element vector from x into an AVX register
      auto xChunk = _mm256_loadu_ps(x + i + j);

      // Load c[j] filter coefficient into every variable
      // of an 8-element AVX register
      auto cChunk = _mm256_set1_ps(c[j]);

      // Element-wise multiplication
      auto temp = _mm256_mul_ps(xChunk, cChunk);

      // Add to the accumulators
      yChunk = _mm256_add_ps(yChunk, temp);
    }

    // Store 8 computed values in the result vector
    _mm256_storeu_ps(y + i, yChunk);
  }

  return y;
}
#endif
```

As for VIL, this code should be 8 times faster than the one in Listing 1. In practice, because of the additional code, the typical speedup will be smaller.

<!-- TODO: How much smaller? -->

A question arises: can we do even better? Yes, we can!

## Outer and Inner Loop vectorization (VOIL)

The real breakthrough comes when we combine both types of vectorization.

In this approach, we compute a vector of outputs in each pass of the outer loop (outer loop vectorization) using an a number of inner product of vectors (a parts of the convolution sums) in each pass of the inner loop (inner loop vectorization).

In verbose code operating on 4-element vectors, VOIL is presented in Listing 6.

_Listing {% increment listingId20220328 %}. Conceptual outer-inner loop vectorization._
```cpp
float* applyFirFilterOuterInnerLoopVectorization(
    FilterInput& input) {
  const auto* x = input.x;
  const auto* c = input.c;
  auto* y = input.y;

  // Note the increment
  for (auto i = 0u; i < input.outputLength; i += 4) {
    y[i] = 0.f;
    y[i + 1] = 0.f;
    y[i + 2] = 0.f;
    y[i + 3] = 0.f;
    
    // Note the increment
    for (auto j = 0u; j < input.filterLength; j += 4) {
      y[i] += x[i + j] * c[j] +
              x[i + j + 1] * c[j + 1] +
              x[i + j + 2] * c[j + 2] +
              x[i + j + 3] * c[j + 3];

      y[i + 1] += x[i + j + 1] * c[j + 1] +
                  x[i + j + 2] * c[j + 2] +
                  x[i + j + 3] * c[j + 3] +
                  x[i + j + 4] * c[j + 4];

      y[i + 2] += x[i + j + 2] * c[j + 2] +
                  x[i + j + 3] * c[j + 3] +
                  x[i + j + 4] * c[j + 4] +
                  x[i + j + 5] * c[j + 5];

      y[i + 3] += x[i + j + 3] * c[j + 3] +
                  x[i + j + 4] * c[j + 4] +
                  x[i + j + 5] * c[j + 5] +
                  x[i + j + 6] * c[j + 6];
    }
  }
  return y;
}
```

This can be visualized as shown in Figure 4.

![]({{ page.images | append: "LoopVectorizationVOIL.svg" }}){: alt="Convolution via outer-inner loop vectorization visualization."}
_Figure {% increment figureId20220328 %}. Outer-inner loop vectorization._

Now one **frame style** corresponds one inner loop iteration. Each frame marks 1 inner product.

As you can see, in one inner loop iteration we compute 4 elements of 4 convolution sums, i.e., 16 elements in total.

### Why Is This More Optimal?

You may think to yourself: *"Okay, but this is just a manual loop unrolling! Why is it faster?"*.

That is because SIMD instructions using multiple registers at once as in the VOIL case give more space for the processor to execute them faster. This is in contrast to using just one or two registers as in the VIL or VOL case.

When I say "at once", I don't mean multithreading. I mean holding references to various registers. That enables the processor handling things most efficiently.

#### Data Alignment

Another reason why VOIL has such a potential for optimization is that we can use *aligned* load/store SIMD instructions to implement it. How? That will be the topic of the next article!

Let's see how to implement VOIL in AVX instructions.

### VOIL AVX Implementation

Listing 7 shows the implementation of FIR filtering with VOIL vectorization using the AVX intrinsics.

_Listing {% increment listingId20220328 %}. Outer-inner loop vectorization in AVX._
```cpp
#ifdef __AVX__
float* applyFirFilterAVX_outerInnerLoopVectorization(
    FilterInput& input) {
  const auto* x = input.x;
  const auto* c = input.c;
  auto* y = input.y;

  // An 8-element array for transferring data from AVX registers
  std::array<float, AVX_FLOAT_COUNT> outStore;

  // 8 separate accumulators for each of the 8 computed outputs
  std::array<__m256, AVX_FLOAT_COUNT> outChunk;

  // Note the increment
  for (auto i = 0u; i < input.outputLength; i += AVX_FLOAT_COUNT) {
    // Initialize the accumulators to 0
    for (auto k = 0u; k < AVX_FLOAT_COUNT; ++k) {
      outChunk[k] = _mm256_setzero_ps();
    }

    // Note the increment
    for (auto j = 0u; j < input.filterLength; j += AVX_FLOAT_COUNT) {
      // Load filter coefficients into an AVX register
      auto cChunk = _mm256_loadu_ps(c + j);

      for (auto k = 0u; k < AVX_FLOAT_COUNT; ++k) {
        // Load the input samples into an AVX register
        auto xChunk = _mm256_loadu_ps(x + i + j + k);

        // Element-wise multiplication
        auto temp = _mm256_mul_ps(xChunk, cChunk);

        // Add to the dedicated accumulator
        outChunk[k] = _mm256_add_ps(outChunk[k], temp);
      }
    }

    // Summarize the accumulators
    for (auto k = 0u; k < AVX_FLOAT_COUNT; ++k) {
      // Transfer the data into the helper array
      _mm256_storeu_ps(outStore.data(), outChunk[k]);

      if (i + k < input.outputLength)
        // Final sum for each of the 8 outputs 
        // computed in 1 outer loop iteration
        y[i + k] = std::accumulate(outStore.begin(), outStore.end(), 0.f);
    }
  }

  return y;
}
#endif
```

In this code, zero-padding is even more important because we may easily try to access an out-of-memory element. Hence the `if` statement near the end of the outer loop.

## Summary

In this article, we have discussed what is a FIR filter and how it can be efficiently realized; either by choosing the fast convolution algorithm or by using single instruction, multiple data instructions of modern processors. Of course, you can do both!

We redefined the convolution sum to facilitate the discussion and implementation.

We looked into the implementation of the FIR filter using a technique called *loop vectorization*. We showed plain C implementations of the inner, outer, and outer-inner loop vectorizations, discussed their visualizations, and showed their SIMD equivalents using the AVX instruction set.

Finally, we indicated that we can do even better with aligned data. This will be discussed in the next article.

Please, check out the useful references below. The whole code is [available in my GitHub repository](https://github.com/JanWilczek/fir-simd.git).

And as always, if you have any questions, feel free to post them below.

## Bibliography

[Code to this article on GitHub.](https://github.com/JanWilczek/fir-simd.git)

[Kutil2009] Rade Kutil, *Short-Vector SIMD Parallelization in Signal Processing*. [[PDF](https://www.cosy.sbg.ac.at/~rkutil/publication/Kutil09b.pdf)]

[Shahbarhrami2005] Asadollah Shahbahrami, Ben Juurlink, and Stamatis Vassiliadis, *Efficient Vectorization of the FIR Filter*. [[PDF](https://www.aes.tu-berlin.de/fileadmin/fg196/publication/old-juurlink/efficient_vectorization_of_the_fir_filter.pdf)]

[Wefers2015] Frank Wefers *Partitioned convolution algorithms for real-time auralization*, PhD Thesis, Zugl.: Aachen, Techn. Hochsch., 2015.


{% endkatexmm %}
