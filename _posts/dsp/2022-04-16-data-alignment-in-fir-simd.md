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
How to align data for optimal filtering?

{% katexmm %}
{% capture _ %}{% increment equationId20220416  %}{% endcapture %}
{% capture _ %}{% increment listingId20220416 %}{% endcapture %}
{% capture _ %}{% increment figureId20220416  %}{% endcapture %}

In the [previous article]({% post_url dsp/2022-03-28-fir-with-simd %}), we discussed how to implement the finite impulse response (FIR) filter using single instruction, multiple data (SIMD) instructions. We used a technique called *loop vectorization* to speed up the computations.

Can we do even more?

Yes, we can!

In this article, you will learn **how to properly align your audio signal data for optimal FIR filtering with SIMD**.

## What is Data Alignment?

If we view the random-access memory (RAM) as consisting of boxes, we could say that the first memory address in each box is aligned with respect to the size of the box.

If we say that our data is aligned as 4 `float`s, we mean that the pointer to our data points to an address which is a multiplicity of 4 times the size of a `float` on the given platform.

C++ has a lot of features concerning alignment. Most notably, from C++ 17, standard containers like `std::array` or `std::vector` are always aligned according to the type they hold.

If you want to learn more about data alignment in general, I have a [dedicated article about it]({% post_url 2020-04-09-what-is-data-alignment %}). There I go into more detail and show concrete C++ features concerning alignment.

In this article, we focus on how to achieve optimal data alignment for FIR filtering.



## Why Does Alignment Matter in SIMD?

In [FIR filters implementation with SIMD]({% post_url dsp/2022-03-28-fir-with-simd %}#vil-avx-implementation), we are using the load/store instrinsic functions. The load functions move the data from plain C arrays (e.g., `float*`) to dedicated vector registers, which are identified by a type specific to the given SIMD instruction set, e.g., `__m256` in the AVX instruction set. The store instructions transport the contents of the given SIMD register to the given C-style array. 

These transitions are shown in Figure 1.

![]({{ page.images }}/load_store_instructions.webp){: width="60%" alt="Explanation diagram of the load/store instructions" }
_Figure {% increment figureId20220416 %}. Load/store instructions transport the data between the memory and the SIMD registers._

These load/store instructions take pointers to C-style arrays. The data under these pointers can be aligned or not. If it is aligned, we can call the aligned version of the load/store instructions, which are typically faster than their unaligned counterparts. If the data under the pointer is not aligned or we don't know if it is aligned, we have to to use the unaligned instrinsic functions.

For example, in the AVX instrinsics, we have the `load` infix for the aligned load and the `loadu` infix for the unaligned load. Example intrinsic functions with these infixes are `_mm256_load_ps` and `_mm256_loadu_ps` respectively.

We strive to operate on aligned data to be able to use the potentially faster aligned load/store instructions.

## Where is Data Alignment Present in FIR Filtering?

In FIR filter implementations using SIMD, we move vectors of samples from the memory to the dedicated registers. We do this many times; if our input signal has length $N_x$, our impulse response has length $N_h$, and we operate on vectors of length 4, we load from memory around $N_x N_h / 4$ times in total and store into memory $(N_x + N_h - 1)/4$ times in total.

Imagine now that we can perform each of these operations a little bit faster. The potential gain can be significant.

### Which Loop Vectorization Techniques Can Benefit From Data Alignment?

In the [loop vectorization techniques]({% post_url dsp/2022-03-28-fir-with-simd %}#loop-vectorization), optimal data alignment (one that allows using the aligned load/store instructions in every case) seems impossible. That is because we always need to load vectors that start at successive samples.

In the [inner loop vectorization]({% post_url dsp/2022-03-28-fir-with-simd %}#inner-loop-vectorization-vil), if we are lucky to have the vectors used for inner product computation aligned, we know that on the next outer loop iteration, they won't be aligned.

In the [outer loop vectorization]({% post_url dsp/2022-03-28-fir-with-simd %}#outer-loop-vectorization-vol), if one of the loads of the input signal is aligned, the next couple of loads won't be. Additionally, filter coefficients are read one by one and copied into every element of the SIMD register so this part cannot ever be aligned.

In the [outer-inner loop vectorization]({% post_url dsp/2022-03-28-fir-with-simd %}#outer-and-inner-loop-vectorization-voil), one of the input signals could have aligned loads (because we read it in non-overlapping chunks), however, the other signal is being read in overlapping chunks starting at every possible sample.

Out of these, **only the outer-inner loop vectorization can be optimzed to work on fully alined data**.

How? Keep reading to find out.

## How to Align Data for FIR Filtering?

It may seem that if we must access one of the signal at every sample, we cannot ever align the data.

Unless...

**We replicate the signal with each needed access aligned.**

In order to stay efficient, we must do it before any filtering takes place.

Note that it can only be done with a signal that is known before the processing. In our example, it will be the filter's impulse response; that is a use case for writing a convolutional reverb VST plugin.

### Aligning Inputs

Let's revisit how we access the elements in the [outer-inner loop vectorization]({% post_url dsp/2022-03-28-fir-with-simd %}#outer-and-inner-loop-vectorization-voil) (Figure 2).

![]({{ page.images }}/LoopVectorizationVOIL.svg){: alt="Outer-inner loop vectorization diagram."}
_Figure {% increment figureId20220416 %}. Data accessed in one iteration of the outer loop in the outer-inner loop vectorization technique._

The $x$-signal's elements are accesssed starting at every possible sample. The goal is to multiply the short vectors from the input signal with the short vectors of the filter's reversed coefficients.

We could copy the short vectors from $x$ so that each access is aligned. Or we could do the same with the filter's coefficients.

Take a look at how we can replicate the filter's reversed coefficients to obtain aligned access every time (Figure 3).

![]({{ page.images }}/LoopVectorizationDataAlignment.svg){: alt="Aligned data access in outer-inner loop vectorization."}
_Figure {% increment figureId20220416 %}. Copying filter coefficients allows aligned access._

As you can see, we perform the same multiplications as before although not in the same order (for example, $x[4]$ is multiplied with $c[3]$ in the second inner loop iteration, not in the first one).

We might have some overhead coming from multiplications with zeros but the aligned load/store speed-up should compensate this easily.

Ain't that neat?

## C++ Data-Aligning Code

Here, I would really like to present you code that allows properly reversing the filter coefficients, allocating the separate arrays for its shifted versions, zero padding, and aligning the data. However, that part is really difficult to write in a general manner. Instead, I decided to list here the possible approaches to alignment you can take in C++.

### 1. Use the `alignas` Specifier

With the [`alignas` specifier](https://en.cppreference.com/w/cpp/language/alignas), we can create aligned short vectors of fixed size. For example, an AVX short vector has length 8 and can be allocated as shown in Listing 1.

_Listing {% increment listingId20220416 %}. A short vector aligned for the AVX instruction set using the `alignas` specifier._
```cpp
constexpr auto AVX_FLOAT_COUNT = 8u;
struct alignas(AVX_FLOAT_COUNT * alignof(float)) avx_t {
    float avx_data[AVX_FLOAT_COUNT];
};
```

What this definition says is "align each `avx_t` object on a boundary that is a mutliplicity of eight times the alignment of a regular `float`". For example, on my machine, `alignof(float)` returns 4 (each `float`, which is 32-bit, is aligned on a 4-byte boundary) and, thus, the array in `avx_t` will by aligned on a 64-byte boundary, which is the needed alignment for the aligned load/store instructions. `AVX_FLOAT_COUNT * alignof(float)` is equal to `alignof(__mm256)`, i.e., the AVX register type.

If we omitted the `alignas` part, `avx_t` would be aligned as a regular `float` so on a 4-byte boundary.

The obvious limitation of this approach is that we can only use arrays of length known at compile time.

### 2. Use the `align_t` Type in Allocation Function

Since C++ 17, we are able to allocate aligned memory dynamically using language features. For example, we can use `new` with alignment as shown in Listing 2.

_Listing {% increment listingId20220416 %}. Aligned `new`._
```cpp
#include <memory> // for the aligned new

constexpr auto AVX_FLOAT_COUNT = 8u;
auto shortVectorsCount = 94u; // as many as you like
std::unique_ptr<float[]> signal {
    new(std::align_val_t{AVX_FLOAT_COUNT * alignof(float)}) 
    float[AVX_FLOAT_COUNT * shortVectorsCount]
};
signal[0] = 0.f; // usual array syntax
```

In the above code, the dynamically allocated `signal` array is aligned according to the alignment required by the AVX instruction set.

We can use this approach, to allocate the arrays needed to store the shifted and zero-padded filter coefficients as well as the input signal.

If you want to go to an even lower level, you can use [`std::aligned_alloc`](https://en.cppreference.com/w/cpp/memory/c/aligned_alloc) to allocate raw, aligned memory.

### 3. Write Your Own Allocator For Standard Containers

Standard containers can be instantiated with an allocator class as their template parameter, for example

_Listing {% increment listingId20220416 %}._
```cpp
std::vector<T, MyCustomAllocator<T>>  v;
```

The member functions of this allocator class are used to allocate and deallocate memory. A specific implementation (for example using `std::aligned_alloc`) can make sure that the allocated memory is always aligned according to some alignment specification. For all the requirements on an allocator class, check the [C++ standard's requirements on an allocator.](https://en.cppreference.com/w/cpp/named_req/Allocator).

As writing your own aligned allocator is difficult, I suggest you use an available one, for example, [the one from the `boost` library](https://www.boost.org/doc/libs/1_63_0/doc/html/align/tutorial.html#align.tutorial.aligned_allocator).

## Aligned Outer-Inner Loop Vectorization in AVX

The outer-inner loop vectorization with the AVX instructions was explained in the [previous article]({% post_url dsp/2022-03-28-fir-with-simd %}).

With properly aligned data, we must simply change all calls to `_mm256_loadu_ps` and `_mm256_storeu_ps` to `_mm256_load_ps` and `_mm256_store_ps` respectively. We must, of course, pass it pointers to aligned data.

Alternatively, you can check out the [code to this article on GitHub](https://github.com/JanWilczek/fir-simd.git), where I already put the aligned AVX filtering function.

## Summary

In this article, we learned how to align data for FIR filtering.

To operate on fully aligned data, we need to use the outer-inner loop vectorization and replicate either the input signal or the reversed coefficients signal so that the access to every sample can always be aligned.

Thanks for reading! If you have any questions, just ask them in the comments below! 🙂

## Bibliography

[Code to this article on GitHub.](https://github.com/JanWilczek/fir-simd.git)

[Kutil2009] Rade Kutil, *Short-Vector SIMD Parallelization in Signal Processing*. [[PDF](https://www.cosy.sbg.ac.at/~rkutil/publication/Kutil09b.pdf)]

[Shahbarhrami2005] Asadollah Shahbahrami, Ben Juurlink, and Stamatis Vassiliadis, *Efficient Vectorization of the FIR Filter*. [[PDF](https://www.aes.tu-berlin.de/fileadmin/fg196/publication/old-juurlink/efficient_vectorization_of_the_fir_filter.pdf)]

[Wefers2015] Frank Wefers *Partitioned convolution algorithms for real-time auralization*, PhD Thesis, Zugl.: Aachen, Techn. Hochsch., 2015.

{% endkatexmm %}
