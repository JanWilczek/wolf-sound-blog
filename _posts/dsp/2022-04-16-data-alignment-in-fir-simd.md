---
title: "Data Alignment in FIR Filter SIMD Implementation"
description: "Learn how to align data in an FIR filter implementation with SIMD instructions."
date: 2022-04-16
author: Jan Wilczek
layout: post
images: /assets/img/posts/dsp/2022-03-28-fir-with-simd/
permalink: /data-alignment-in-fir-filter-simd-implementation/
# background: /assets/img/posts/dsp/2022-04-16-data-alignment-in-fir-simd/Thumbnail.webp
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
discussion_id: 2022-04-16-data-alignment-in-fir-simd
---
How to align data for optimum filtering?

In the [previous article], we discussed how to implement the finite impulse response (FIR) filter using single instruction, multiple data (SIMD) instructions. We used a technique called *loop vectorization* to speed up the computations.

Can we do even more?

Yes, we can!

In this article, you will learn **how to properly align your audio signal data for optimal FIR filtering with SIMD**.

## What is Data Alignment?

If we view the random-access memory (RAM) as consisting of boxes, we could say that the first memory address in each box is aligned with respect to the size of the box.

If we say that our data is aligned as 4 `float`s, we mean that the pointer to our data points to the first memory address in such a box.

C++ has a lot of features concerning alignment. Most notably, from C++ 17, standard containers like `std::array` or `std::vector` are always aligned according to the type they hold.

If you want to learn more about data alignment in general, I have a [dedicated article about it]({% post_url 2020-04-09-what-is-data-alignment %}). There I go into more detail and show concrete C++ features concerning alignment.

In this article, we focus on how to achieve optimal data alignment for FIR filtering.



## Why Does Alignment Matter in SIMD?

In FIR filters implementation with SIMD we are using the load/store instrinsic functions. The load functions move the data from plain C arrays (e.g., `float*`) to dedicated vector registers, which are identified by a type specific to the given SIMD instruction set, e.g., `m256` in the AVX instruction set. The store instructions transport the contents of the given SIMD register to the given C-style array. 

<!-- TODO: load/store infographic -->

These load/store instructions take pointers to C-style arrays. the data under these pointers can be aligned or not. If it is aligned, we can call the aligned version of the load/store instructions, which are typically faster than their unaligned counterparts. If the data under the pointer is not aligned or we don't know, we have to to use the unaligned instrinsic functions.

For example, in the AVX instrinsics, we have the `load` infix for the aligned load and the `loadu` infix for the unaligned load. Example intrinsic functions with these infixes are `_mm256_load_ps` and `_mm256_loadu_ps` respectively.

We strive to operate on aligned data to be able to use the potentially faster aligned load/store instructions.

## Where is Data Alignment Present in FIR Filtering?

In FIR filter implementations using SIMD, we move vectors of samples from the memory to the dedicated registers. We do this many times; if our input signal has length $N_x$, our impulse response has length $N_h$, and we operate on vectors of length 4, we load from memory around $N_x N_h / 4$ times in total and store into memory $(N_x + N_h - 1)/4$ times in total.

Imagine now that we can perform each of these operations a little bit faster. The potential gain can be significant.

### Which Loop Vectorization Techniques Can Benefit From Data Alignment?

In the [loop vectorization techniques]({% post_url dsp/2022-03-28-fir-with-simd %}), optimal data alignment (using the aligned instructions in every case) seems impossible. That is because we always need to load vectors that start at successive samples.

In the inner loop vectorization, if we are lucky to have the vectors used for inner product computation aligned, we know that on the next outer loop iteration, they won't be aligned.

In the outer loop vectorization, if one of the loads of the input signal is aligned, the next bunch won't be. Additionally, filter coefficients are read one by one and copied into every element of the SIMD register so it cannot ever be aligned.

In the outer-inner loop vectorization, one of the input signals could have aligned loads (because we read it in non-overlapping chunks), however, the other signal is being read in overlapping chunks starting with every possible sample.

Out of these, **only the outer-inner loop vectorization can be optimzed to work on fully alined data**.

How? Keep on reading to find out.

## How to Align Data for FIR Filtering?

It may seem that if we must access one of the signal starting with every sample, we cannot ever align the data.

Unless...

**We replicate the signal with each needed access aligned.**

In order to stay efficient, we must do it before any filtering takes place.

Note that it can only be done with a signal that is known before the processing. In our example, it will be the filter's impulse response; that is a use case for writing a convolutional reverb VST plugin.

### Aligning Inputs

Let's revisit how we access the elements in outer-inner loop vectorization (Figure ???).

![]({{ page.images }}/LoopVectorizationVOIL.svg)

The $x$-signal's elements are accesssed starting from every possible sample. The goal is to multiply the short vectors from the input signal with a short vector of the filter's reversed coefficients.

We could copy the short vectors from $x$ so that each access is aligned. Or we could do the same with the filter's coefficients.

Take a look how we can replicate the filter's reversed coefficients to obtain aligned access every time.

![]({{ page.images }}/LoopVectorizationDataAlignment.svg)

As you can see, we perform the same multiplications as before although not in the same order (for example, $x[4]$ is multiplied with $c[3]$ in the second inner loop iteration, not in the first one).

We might have some overhead coming from multiplications with zeros but the aligned load/store speed-up should compensate this easily.

Ain't that neat?

#### Sample Code Aligning Data

To align the data this way, we need a little bit of code. To show this, we'll use the `FilterInput` structure from the previous article. [LINK!]

In places, where we need the size of the short vector, I used the `AVX_FLOAT_COUNT` constant, describing the number of floats in an AVX register. [LINK!]

```cpp
constexpr auto AVX_FLOAT_COUNT = 8u;

template <typename T>
T highestMultipleOfNIn(T x, T N) {
  return static_cast<long long>(x / N);
}

struct FilterInput {
  FilterInput(const std::vector<float>& inputSignal,
              const std::vector<float>& filter,
              size_t alignment = 1u)
      : alignment(alignment) {
    const auto minimalPaddedSize = inputSignal.size() + 2 * filter.size() - 2u;
    const auto alignedPaddedSize =
        alignment *
        (highestMultipleOfNIn(minimalPaddedSize - 1u, alignment) + 1u);
    inputLength = alignedPaddedSize;

    inputStorage.resize(inputLength, 0.f);
    std::copy(inputSignal.begin(), inputSignal.end(),
              inputStorage.begin() + filter.size() - 1u);

    outputLength = inputSignal.size() + filter.size() - 1u;
    outputStorage.resize(outputLength);

    filterLength =
        alignment * (highestMultipleOfNIn(filter.size() - 1u, alignment) + 1);
    reversedFilterCoefficientsStorage.resize(filterLength);

    std::reverse_copy(filter.begin(), filter.end(),
                      reversedFilterCoefficientsStorage.begin());
    for (auto i = filter.size(); i < reversedFilterCoefficientsStorage.size();
         ++i)
      reversedFilterCoefficientsStorage[i] = 0.f;

    x = inputStorage.data();
    c = reversedFilterCoefficientsStorage.data();
    filterLength = reversedFilterCoefficientsStorage.size();
    y = outputStorage.data();

    for (auto k = 0u; k < AVX_FLOAT_COUNT; ++k) {
      const auto alignedStorageSize =
          reversedFilterCoefficientsStorage.size() + AVX_FLOAT_COUNT - 1u;
      alignedReversedFilterCoefficientsStorage[k].resize(alignedStorageSize);

      for (auto i = 0u; i < k; ++i) {
        alignedReversedFilterCoefficientsStorage[k][i] = 0.f;
      }
      std::copy(reversedFilterCoefficientsStorage.begin(),
                reversedFilterCoefficientsStorage.end(),
                alignedReversedFilterCoefficientsStorage[k].begin() + k);
      for (auto i = reversedFilterCoefficientsStorage.size() + k;
           i < alignedStorageSize; ++i) {
        alignedReversedFilterCoefficientsStorage[k][i] = 0.f;
      }
    }
    cAligned = alignedReversedFilterCoefficientsStorage.data();
  }

  std::vector<float> output() {
    auto result = outputStorage;
    result.resize(outputLength);
    return result;
  }

  size_t alignment;
  const float* x;  // input signal
  size_t inputLength;
  const float* c;  // reversed filter coefficients
  size_t filterLength;
  float* y;  // output (filtered) signal
  size_t outputLength;
  std::vector<float>* cAligned;

 private:
  std::vector<float> inputStorage;
  std::vector<float> reversedFilterCoefficientsStorage;
  std::vector<float> outputStorage;
  std::array<std::vector<float>, AVX_FLOAT_COUNT>
      alignedReversedFilterCoefficientsStorage;
};
```

This isn't nice, not at all. Fortunately, aligning the output vector is way easier.

### Aligning Output

We can allocate our temporary output vector as shown in Listing ???.

_Listing {% increment listingId20220416 %}. ._
```cpp
alignas(__m256) std::array<float, AVX_FLOAT_COUNT> outStore;
```

and the intermediate sums as 

```cpp
alignas(__m256) std::array<__m256, AVX_FLOAT_COUNT> outChunk;

// Since C++ 17
std::array<__m256, AVX_FLOAT_COUNT> outChunk;
```

C++ 17 automatically aligns the container according to the alignment of the elements' type.

## Aligned Outer-Inner Loop Vectorization on AVX

In Listing ??, the final filtering code operating on aligned data is shown.

`FilterInput` is initialized as was shown in Listing ???.


```cpp
std::vector<float> applyFirFilterAVX_outerInnerLoopVectorizationAligned(
    FilterInput<float>& input) {
  const auto* x = input.x;
  const auto* cAligned = input.cAligned;

  alignas(__m256) std::array<float, AVX_FLOAT_COUNT> outStore;

  std::array<__m256, AVX_FLOAT_COUNT> outChunk;

  for (auto i = 0u; i < input.outputLength; i += AVX_FLOAT_COUNT) {
    for (auto k = 0u; k < AVX_FLOAT_COUNT; ++k) {
      outChunk[k] = _mm256_setzero_ps();
    }

    for (auto j = 0u; j < input.filterLength; j += AVX_FLOAT_COUNT) {
      auto xChunk = _mm256_loadu_ps(x + i + j);

      for (auto k = 0u; k < AVX_FLOAT_COUNT; ++k) {
        auto cChunk = _mm256_loadu_ps(cAligned[k].data() + j);

        auto temp = _mm256_mul_ps(xChunk, cChunk);

        outChunk[k] = _mm256_add_ps(outChunk[k], temp);
      }
    }

    for (auto k = 0u; k < AVX_FLOAT_COUNT; ++k) {
      _mm256_store_ps(outStore.data(), outChunk[k]);
      if (i + k < input.outputLength)
        input.y[i + k] =
            std::accumulate(outStore.begin(), outStore.end(), 0.f);
    }
  }

  return input.output();
}
```

## Summary

In this article, we learned how to align data for FIR filtering.

To operate on fully aligned data, we need to use the outer-inner loop vectorization and replicate either the input signal or the reversed coefficients signal so that the access to every sample can always be aligned.

Thanks for reading! If you have any questions, just ask them in the comments below! 🙂

## Bibliography

[Code to this article on GitHub.](https://github.com/JanWilczek/fir-simd.git)

[Kutil2009] Rade Kutil, *Short-Vector SIMD Parallelization in Signal Processing*. [[PDF](https://www.cosy.sbg.ac.at/~rkutil/publication/Kutil09b.pdf)]

[Shahbarhrami2005] Asadollah Shahbahrami, Ben Juurlink, and Stamatis Vassiliadis, *Efficient Vectorization of the FIR Filter*. [[PDF](https://www.aes.tu-berlin.de/fileadmin/fg196/publication/old-juurlink/efficient_vectorization_of_the_fir_filter.pdf)]

[Wefers2015] Frank Wefers *Partitioned convolution algorithms for real-time auralization*, PhD Thesis, Zugl.: Aachen, Techn. Hochsch., 2015.
