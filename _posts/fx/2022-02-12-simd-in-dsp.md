---
title: "What is SIMD in Digital Signal Processing?"
description: "Leverage intrinsic vector functions of your processor for efficient signal processing."
date: 2022-02-12
author: Jan Wilczek
layout: post
images: assets/img/posts/fx/2022-02-12-simd-in-dsp/
background: /assets/img/posts/fx/2022-02-12-simd-in-dsp/Thumbnail.webp
categories:
  - Audio FX
  - Digital Signal Processing
tags:
  - simd
  - cpp
  - c
discussion_id: 2022-02-12-simd-in-dsp
---
Speed up DSP operations with vector instructions.

<iframe width="560" height="315" src="https://www.youtube.com/embed/XiaIbmMGqdg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Table of Contents

1. [Introduction](#introduction)
2. [What is SIMD?](#what-is-simd)
3. [SIMD Pseudocode Example](#simd-pseudocode-example)
4. [How is SIMD Implemented?](#how-is-simd-implemented)
5. [What SIMD Instructions Are Available?](#what-simd-instructions-are-available)
   1. [Load/Store](#loadstore)
   2. [Operations on Registers](#operations-on-registers)
6. [How to Access SIMD Instructions?](#how-to-access-simd-instructions)
7. [MMX, SSE, AVX, NEON...](#mmx-sse-avx-neon)
8. [Which SIMD To Use?](#which-simd-to-use)
9. [Why is SIMD useful in DSP?](#why-is-simd-useful-in-dsp)
10. [Disadvantages of SIMD](#disadvantages-of-simd)
11. [Simple SIMD Code Example](#simple-simd-code-example)
12. [Summary](#summary)
13. [Bibliography, Reference, and Further Reading](#bibliography-reference-and-further-reading)



## Introduction

Digital signal processing of images or sound requires complicated operations on large amounts of data. For example, to scale (change volume) of a second of audio data, we may have to perform 44100 multiplications.

If we want to perform these operations in real time with less than 10 milliseconds reserved for an entire processing pipeline, things get even more difficult.

Thankfully, there are some programming tools that allow us handle these scenarios efficiently. One of them is SIMD, the topic of this article.

## What is SIMD?

Single instruction, multiple data (SIMD) are special processor instructions that perform some operation on more than 1 variable at a time.

In mathematical terms, we could say that SIMD operates on vectors ("arrays") of variables as "normal" code operates on single variables.

<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6611455743195468"
     crossorigin="anonymous"></script><ins class="adsbygoogle"
     style="display:block; text-align:center;"
     data-ad-layout="in-article"
     data-ad-format="fluid"
     data-ad-client="ca-pub-6611455743195468"
     data-ad-slot="7289385396"></ins><script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>

## SIMD Pseudocode Example

Imagine that we have two 8-element vectors (arrays), $\pmb{v}_1$ and $\pmb{v}_2$, both containing 32-bit floating-point variables,. Let's assume that $\pmb{v}_{12} = \pmb{v}_1 + \pmb{v}_2$.

To calculate $\pmb{v}_{12}$ in plain C code, we would need to write

```cpp
for (auto i = 0; i < 8; ++i)
    v12[i] = v1[i] + v2[i];
```

That means 8 additions, 8 "add" operations.

What if instead we could simply write

```cpp
v12 = vector8x32_add(v1, v2); // add eight 32-bit floats
```

which would result in 1 "add" operation?

In theory, such a program would be 8 times faster. And that's not actually far from the truth!

Whereas the speed-up in execution does not have to increase proportionally with the usage of multiple threads, SIMD often delivers speed-ups directly proportional to the number of variables that can fit into a data vector.

In AVX-512 instructions, one can operate on 16 `float`s with a single instruction. Can you imagine a 16-fold decrease in the processing time of your code?

And if we use 16-bit integers, we optimistically get... That's right, a 32-fold speed-up.

That's the power of SIMD.

*Note: Performance of implementations using SIMD has to be measured on each processor separately. Moreover, the linear speed-up is very unlikely at the first attempt. But that's a topic for a whole different article.*

## How is SIMD Implemented?

SIMD instruction sets are provided by microprocessor manufacturers.

In general, there are a few processor architecture families. The main ones are x86 and ARM.

Each architecture family has a core set of registers and associated instructions that will work on any processor from that family. Each new generation of processors from a family expands upon the instruction set available for the previous generation. Additionally, each processor can have some instructions that are unique to that particular processor model.

Both the generation-specific instruction sets and the processor-specific instructions typically take advantage of additional architectural elements, like additional registers or dedicated arithmetic units.

You may be asking yourself:

> How is it possible to write one version of source code when each processor accepts different instructions?

That's why the presence of high-level programming languages such as C (sic!) is a blessing. 🙂

The role of a compiler is to take the source code that you've written and translate it to the processor-specific assembly language. The compilers are very wise about which processors contain which instructions. They are also great at determining which of these instructions to call and in which order to make the software as efficient as possible. In fact, they are better at it than at least 95% of programmers (including me).

Unfortunately, they don't know what we want to achieve with our code. For example, they don't know that this huge amount of multiplications and additions is in fact finite-impulse response (FIR) filtering. Therefore, they often cannot utilize the full potential of the underlying hardware.

That's where you come in: a programmer, who knows how to code DSP algorithms with processor-specific instructions.

## What SIMD Instructions Are Available?

Let's state that again: SIMD instructions are simply special processor instructions. That means that they can be found in assembly code, the one that operates directly on registers and memory.

### Load/Store

SIMD typically uses dedicated registers. That means that three kinds of instructions must be available for sure:

* transfer data from memory to the special registers (load),
* transfer data from the special registers to memory (store), and
* set the value of the special registers (set).

For example, the [AVX instruction set](https://www.intel.com/content/www/us/en/docs/intrinsics-guide/index.html#techs=AVX) for x86 processors has the `vmovups` instruction that loads (`mov`) a vector (`v`) of eight 32-bit floating point numbers (`ps`, "single precision") into an AVX register. `u` in the instruction stands for "unaligned", which means that the memory location we load from does not have to be aligned on a 32-byte boundary.

### Operations on Registers

Once the data is in the dedicated registers, we can perform a number of operations on them:

* perform arithmetic operations on 1 register (for example, floor, ceiling, square root),
* perform arithmetic operations on 2 registers (for example, add, subtract, multiply, or divide them),
* perform logical operations on 2 registers (for example, logical `AND`, `OR`),
* convert data types in the register, for example, from integers to floating-point numbers,
* manipulate variable positions in the registers (for example, permute),
* perform different operations on variables in the registers depending on whether their indices are even or odd,
* compare the values in the registers, or even
* perform DSP operations, like multiply-and-add.

As you can see, the number of the available operations is huge.

To effectively leverage the power of SIMD on any given hardware, one can use the documentation provided by the processor manufacturers.

For example, the list of all available instructions for the AVX instruction set can be found at [Intel's site](https://www.intel.com/content/www/us/en/docs/intrinsics-guide/index.html#techs=AVX).
  
## How to Access SIMD Instructions?

We know what SIMD instructions are and what they can do.

How can we as software developers access them?

I see 4 ways in which you can embed SIMD instructions in your code.

1. **Auto-vectorization.** In certain situations, compilers themselves can be smart enough to vectorize code written without vector instructions.
1. **Using assembly commands.** One can write entire software in assembly or use just `asm` blocks in C or C++ programming language.
1. **Intrinsic functions.** Processor manufacturers typically provide C functions that execute the dedicated processor instructions (or their combinations) under the hood. The programmer must simply include relevant headers and compile their programs with dedicated compiler options.
    
    For example, Intel has published a list of all available SIMD instructions on their architectures called [Intel Instrinsics Guide](https://www.intel.com/content/www/us/en/docs/intrinsics-guide/index.html). ARM has published a [similar list for ARM-based architectures](https://developer.arm.com/architectures/instruction-sets/intrinsics/).

    Examples of special compilation flags are `/arch:AVX` on MSVC and `-mavx` on gcc and clang (to be able to use AVX instructions). The catch is that the processor running the software must have those instructions implemented. That's an additional responsibility put on the developer.
1. **Dedicated libraries.** There exist software libraries that provide an abstraction layer between the written code and the hardware it runs on. If we think of vector addition, we may guess that every processor that supports SIMD probably has some vector addition instruction. It may be called differently but the functionality will be the same. An example of such a library may be [Open Computing Language (OpenCL)](https://www.khronos.org/opencl/). An example closer to the hearts of audio developers is the [JUCE framework](https://juce.com/). JUCE provides abstractions such as [`SIMDRegister`](https://docs.juce.com/master/structdsp_1_1SIMDRegister.html), which is a wrapper around the platform-specific extended register type.
   This approach is probably the most comfortable one but it requires you to use (and often pay for) 3rd party software.

## MMX, SSE, AVX, NEON...

You may have come across many abbreviations that represent the families of SIMD instruction sets. Below I listed the ones most important for digital signal processing along with short descriptions.

<table class="table table-striped table-responsive small"><caption>Table 1. SIMD instruction sets</caption>
<thead>
<tr>
<th>Abbreviation</th>
<th>Full Name</th>
<th>Architecture</th>
<th>Available Registers</th>
<th>Remarks</th>
</tr>
</thead>
<tbody>
<tr>
<td>Intel® MMX™</td>
<td></td>
<td>x86</td>
<td>eight 64-bit registers</td>
<td><ul><li>only integer operations</li></ul></td>
</tr>
<tr>
<td>Intel® SSE</td>
<td>Streaming SIMD Extensions</td>
<td>x86</td>
<td>eight 128-bit registers</td>
<td><ul><li>successor of MMX™ with floating-point processing</li></ul></td>
</tr>
<tr>
<td>Intel® AVX</td>
<td>Advanced Vector Extensions</td>
<td>x86</td>
<td>eight 256-bit registers (512-bit for AVX-512)</td>
<td><ul><li>successor of SSE</li></ul></td>
</tr>
<tr>
<td>Arm Neon</td>
<td>&nbsp;</td>
<td>ARM</td>
<td>thirty-two 128-bit registers</td>
<td>
<ul>
<li> available on all devices running Android 6.0 or higher [<a target="_blank" href="https://source.android.com/compatibility/6.0/android-6.0-cdd#3_3_native_api_compatibility">source</a>],</li>
<li> available on Apple products: iPhones, iPads, and some Macs,</li>
<li> can be used on x86 architectures with <a target="_blank" href="https://github.com/intel/ARM_NEON_2_x86_SSE">NEON_2_SSE conversion headers</a>.</li>
</ul>
</td>
</tr>
</tbody>
</table>

## Which SIMD To Use?

Since there are many instruction sets to choose from, one may wonder: how to choose the proper one?

The answer is, as always, it depends.

The first consideration is the architecture family you are writing software for.

For example, if you write software for Android devices, you most likely will use Neon. But not always! There are Android-driven devices that run on x86 architectures as well.

If you target x86 architectures only and want to leverage SIMD as much as possible, you should provide implementations for all x86 SIMD instruction sets and give software the fallback possibility; if, for example, AVX-512 is not present, maybe SSE can be used. Keep in mind that there is SSE, SSE2, SSE3, SSE4... And there are minor versions too.

If you don't have a clue on which platform your software will run on, you are facing the possibility of implementing every available instruction set support.

That's why compilers are such a blessing: they can do this heavy lifting for us. And make much fewer mistakes along the way. 🙂

## Why is SIMD useful in DSP?

SIMD is especially advantageous in digital signal processing applications. Why?

1. **DSP algorithms are often defined in terms of vectors.** Additionally, scientists are used to operating on vectors in Matlab or Python. With the power of SIMD, we can efficiently use vectors in C/C++ code as well.
2. **DSP algorithms often perform the same tasks on different data.** SIMD instructions are meant to perform the same operations on multiple variables at once.
3. **Signal processing is most often done in blocks.** Blocks of audio samples, image data, or film data typically have length equal to a multiplicity of SIMD registers' size. That makes them easy to vectorize.
4. **SIMD instruction sets often contain DSP-specific functions.** For example, Neon instructions contain a [multiply-and-add operation](https://developer.arm.com/architectures/instruction-sets/intrinsics/vmlaq_f32). That means that we can perform the dot product with a single command.

## Disadvantages of SIMD

The SIMD is not all blue skies, unfortunately. Here are some disadvantages of SIMD in the context of DSP (but not only).

1. **A programmer's nightmare: supporting all instruction sets.** If you build not just cross-platform applications but applications that are supposed to work similarly on different processor architectures, you may run into the problem of determining the underlying architecture, its features, and handling every possible case. Think about it: you will not only have to write code using specific AVX, SSE, or Neon instructions. You will also need to implement everywhere compile-time or even run-time checks of which routines to use. This adds *a lot* of additional code on top of the algorithm code including macro trickery.

   Don't think that if you write Android-only code, your code will always run on ARM architectures. Nowadays, there are lots of devices running Android on a processor from the x86 family. That is why, it is best to use a library that informs you about current processor's capabilities such as Google's [cpu_features](https://github.com/google/cpu_features) library.
1. **Run-time availability checks.** As mentioned above, you sometimes need to determine at run time which instruction set to use. That adds additional code and execution time overhead.
2. **Unaligned data.** Extended instructions sets work best on [aligned data]({% post_url collections.posts, '2020-04-09-what-is-data-alignment' %}). Unfortunately, your data typically won't be aligned by itself. The necessity to align the vectors on a specific boundary adds yet another layer of code and complexity on top of your algorithm.
3. **Edge cases, single samples.** What if the signal data that you want to process does not come in blocks which are of size equal to the multiplicity of the SIMD register size? You will then need to "manually" finish off the algorithm with its scalar version. That means even more complexity.
4. **Little resources on the topic.** Processing signals with SIMD is not a very well explained topic on the web or on YouTube. One needs to turn to specialized books and research papers to understand the basics. SIMD is a topic that must be discussed in the context it is applied in. It's not easy to transfer tutorials from image processing or 3D graphics to audio processing. These reasons make the entry barrier quite high.
5. **Low readability.** SIMD code is full of functions like `vrecpeq_f32` or `_mm256_testnzc_ps`, which are not easy to read and understand when you look at the code or pronounce when you talk to your colleagues. On the other hand, these names make very good mnemonics once you get a bit into the intrinsic functions.

## Simple SIMD Code Example

To round off this article, we will code  small example in C++ using intrinsics.

Specifically, we will use the AVX instruction set available on Intel processors.

The goal of this little program is to compute the inner product of two vectors of floating-point numbers. AVX registers have 256 bits so each should fit exactly 8  32-bit `float`s.

```cpp
#include <vector>
#include <array>
#include <cassert>
#include <random>
#include <algorithm>
#include <chrono>
#include <iostream>

#include <immintrin.h>

using Vector = std::vector<float>;

Vector scalarAdd(const Vector& a, const Vector& b) {
    assert(a.size() == b.size());

    Vector result(a.size());

    for (auto i = 0u; i < a.size(); ++i) {
        result[i] = a[i] + b[i];
    }

    return result;
}

Vector simdAdd(const Vector& a, const Vector& b) {
    assert(a.size() == b.size());

    Vector result(a.size());

    constexpr auto FLOATS_IN_AVX_REGISTER = 8u;

    const auto vectorizableSamples = (a.size() / FLOATS_IN_AVX_REGISTER) 
                                     * FLOATS_IN_AVX_REGISTER;

    auto i = 0u;
    for (; i < vectorizableSamples; i += FLOATS_IN_AVX_REGISTER) {
        // load unaligned data to SIMD registers
        auto aRegister = _mm256_loadu_ps(a.data() + i);
        auto bRegister = _mm256_loadu_ps(b.data() + i);

        // perform the addition
        auto intermediateSum = _mm256_add_ps(aRegister, bRegister);

        // store data back in the data vector
        _mm256_storeu_ps(result.data() + i, intermediateSum);
    }
    // process the remaining (unvectorized) samples
    for (; i < a.size(); ++i) {
        result[i] = a[i] + b[i];
    }

    return result;
}

Vector randomVector(Vector::size_type size) {
    Vector v(size);

    auto randomEngine = std::default_random_engine();
    std::uniform_real_distribution<float> uniformDistribution(-1.f, 1.f);
    auto generator = [&]() { return uniformDistribution(randomEngine); };
    std::generate(v.begin(), v.end(), generator);

    return v;
}

int main() {
    constexpr auto TEST_VECTOR_SIZE = 1000001;

    const auto a = randomVector(TEST_VECTOR_SIZE);
    const auto b = randomVector(TEST_VECTOR_SIZE);

    assert(scalarAdd(a, b) == simdAdd(a, b));

    constexpr auto TEST_RUN_COUNT = 1000;

    using namespace std::chrono;
    milliseconds totalScalarTime{};
    for (auto i = 0u; i < TEST_RUN_COUNT; ++i) {
        auto start = high_resolution_clock::now();
        auto result = scalarAdd(a, b);
        auto end = high_resolution_clock::now();
        totalScalarTime += duration_cast<milliseconds>(end - start);
    }

    std::cout << "Average scalarAdd() execution time: " 
              << totalScalarTime.count() / static_cast<float>(TEST_RUN_COUNT) 
              << " ms." << std::endl;

    milliseconds totalSimdTime{};
    for (auto i = 0u; i < TEST_RUN_COUNT; ++i) {
        auto start = high_resolution_clock::now();
        auto result = simdAdd(a, b);
        auto end = high_resolution_clock::now();
        totalSimdTime += duration_cast<milliseconds>(end - start);
    }

    std::cout << "Average simdAdd() execution time: " 
              << totalSimdTime.count() / static_cast<float>(TEST_RUN_COUNT) 
              << " ms." << std::endl;
}
```

Compile with

```bash
g++ -mavx -Wall -O0 InnerProductSIMD.cpp -o InnerProductSIMD.exe 
```

Sample output:

```bash
.\InnerProductSIMD.exe 
Average scalarAdd() execution time: 11.695 ms.
Average simdAdd() execution time: 4.113 ms.
```

## Summary

In this article, we discussed the usefulness of single instruction, multiple data (SIMD) instructions in digital signal processing.

SIMD instructions let us perform operations on more than one variable at once using dedicated processor registers.

Different processor architectures and models have different SIMD instructions available.

The main takeaway should be: SIMD instructions can make your DSP code significantly faster at the cost of

* code complexity.
* portability,
* expert knowledge on processors.

If you have any questions, feel free to ask them in the comments below!

In the next article, I will show you how to implement FIR filtering using SIMD instructions, so stay tuned! 🙂



## Bibliography, Reference, and Further Reading

[Intel® SIMD technology comparison](https://www.intel.com/content/www/us/en/develop/documentation/cpp-compiler-developer-guide-and-reference/top/compiler-reference/intrinsics/details-about-intrinsics.html)

[Intel® Intrinsics Reference](https://www.intel.com/content/www/us/en/docs/intrinsics-guide/index.html#ig_expand=6926,4362,6209,6201,7244,6247,4362,156,6926)

[Arm Neon Intrinsics Reference](https://developer.arm.com/architectures/instruction-sets/intrinsics/#f:@navigationhierarchiessimdisa=[Neon]&first=100)

[Advanced Vector Extensions (AVX) on Wikipedia](https://en.wikipedia.org/wiki/Advanced_Vector_Extensions)

