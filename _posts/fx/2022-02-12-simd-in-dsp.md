---
title: "What is SIMD in Digital Signal Processing?"
description: "Leverage intrinsic vector functions of your processor for efficient signal processing."
date: 2022-02-12
author: Jan Wilczek
layout: post
images: assets/img/posts/fx/2022-02-12-simd-in-dsp/
# background: /assets/img/posts/fx/2022-02-12-simd-in-dsp/Thumbnail.webp
categories:
  - Audio FX
  - Digital Signal Processing
tags:
  - simd
  - C++
  - C
discussion_id: 2022-02-12-simd-in-dsp
---
Speed up DSP operations with vector instructions.

<!-- TOC -->

## Introduction

Digital signal processing of images or sound requires complicated operations on large amounts of data. For example, to scale (change volume) a second of audio data, we may have to perform 44100 multiplications.

If we want to perform these operations in real time with less than 10 milliseconds reserved for an entire processing pipeline, things get even more difficult.

Thankfully, there are some programming tools that allow us handle these scenarios efficiently. One of them is SIMD, the topic of this article.

## What is SIMD?

Single instruction, multiple data (SIMD) are special processor instructions that perform some operation on more than 1 variable at a time.

In mathematical terms, we could say that SIMD operate on vectors ("arrays") of variables as "normal" code operates on single variables.

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

And if we use 16-bit `int`egers, we optimistically get... That's right, a 32-fold speed-up.

That's the power of SIMD.

## How is SIMD Implemented?

SIMD instruction sets are provided by microprocessor manufacturers.

In general, there are a few processor architecture families. The main ones are x86 and ARM.

Each architecture family has a core set of registers and associated instructions that will work on any processor from that family. Each new generation of processors from a family expands upon the instruction set available for the previous generation. Additionally, each processor can have some instructions that are unique to that particular processor model.

Both the generation-specific instruction sets and the processor-specific instructions typically take advantage of additional architectural elements, like additional registers or dedicated arithmetic units.

You may be asking yourself:

> How is it possible to write one version of source code when each processor accepts different instructions?

That's why the presence of high-level programming languages such as C (sic!) is a blessing. 🙂

The role of a compiler is to take the source code that you've written and translate it to processor-specific assembly language. The compilers are very wise at which processors contain which instructions. They are also great at determining which of these instructions to call and in which order to make the software as efficient as possible. In fact, they are better at it than at least 95% of programmers (including me).

Unfortunately, they don't know what we want to achieve with our code. For example, they don't know that this huge amount of multiplications and additions is in fact finitie-impulse response (FIR) filtering. Therefore, they often cannot utilize the full potential of the underlying hardware.

That's where you come in: a programmer, who knows how to code DSP algorithms with processor-specific instructions.

## What SIMD Instructions Are Available?

Let's state that again: SIMD instructions are simply special processor instructions. That means that they can be found in assembly code, the one that operates directly on registers and memory.

### Load/Store

SIMD typically uses dedicated registers. That means that two kinds of instructions must be available for sure:

* transfer data from memory to the special registers (load),
* transfer data from the special registers to memory (store), and
* set the value of the special registers (set).

For example, the [AVX instruction set] for x86 processors has the `vmovups` instruction that loads (`mov`) a vector (`v`) of eight 32-bit floating point numbers (`ps`, single precision) into an AVX register. `u` in the instructions stands for "unaligned", which means that the memory location we load from does not have to be aligned on a 32-byte boundary.

### Operations on Registers

Once the data is in the dedicated registers, we can perform a number of operations on them:

* perform arithmetic operations on 1 register (for example, floor, ceiling, square root),
* perform arithmetic operations on 2 registers (for example, add, subtract, multiply, or divide them),
* perform logical operations on 2 registers (for example, logical `AND`, `OR`),
* convert data types in the register,
* manipulate variable positions in the registers (for example, permute),
* perform different operations on even and odd variables in the registers,
* compare the values in the registers, or even
* perform DSP operations, like multiply-and-add.

As you can see, the number of the available operations is huge.

To effectively leverage the power of SIMD on any given hardware, one can use the documentation provided by the processor manufacturers.

For example, the list of all available instructions for the AVX instruction set can be found at [Intel's site](https://www.intel.com/content/www/us/en/docs/intrinsics-guide/index.html#techs=AVX).
  
## How to Access SIMD Instructions?

We know what SIMD instructions are and what they can do.

How can we as software developers access them?

I see 3 ways you can embed SIMD instructions in your code

1. **Auto-vectorization.** In certain situations, compilers themselves can be smart enough to vectorize code written without vector instructions.
1. **Using assembly commands.** One can write entire software in assembly or use just `asm` blocks in C or C++ programming language.
2. **Intrinsic functions.** Processor manufacturers typically provide C functions that execute the dedicate processor instructions (or their combination) under the hood. The programmer must simply include relevant headers and compile their programs with dedicated compiler options.
    
    For example, Intel has published a list of all available SIMD instruction on their architectures called [Intel Instrinsics Guide](https://www.intel.com/content/www/us/en/docs/intrinsics-guide/index.html). ARM has published a [similar list for ARM-based architectures](https://developer.arm.com/architectures/instruction-sets/intrinsics/).

    Examples of special compilation flags are `/arch:AVX` on MSVC and `-mavx` on gcc and clang (to be able to use AVX instructions). The catch is that the processor running the software must have those instructions implemented. That's an additional responsibility put on the developer.
3. **Dedicated libraries.** There exist software libraries that provide an abstraction layer between the written code and the hardware it runs on. If we think of vector addition, we may guess that every processor that supports SIMD probably has some vector addition instruction. It may be called differently but the functionality will be the same. An example of such a library may be [Open Computing Language (OpenCL)](https://www.khronos.org/opencl/). An example closer to the hearts of audio developers is the [JUCE framework](https://juce.com/). JUCE provides abstractions such as [`SIMDRegister`](https://docs.juce.com/master/structdsp_1_1SIMDRegister.html), which is a wrapper around the platform-native extended register type.
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
<td>* only integer operations</td>
</tr>
<tr>
<td>Intel® SSE</td>
<td>Streaming SIMD Extensions</td>
<td>x86</td>
<td>eight 128-bit registers</td>
<td>* successor of MMX™ with floating-point processing</td>
</tr>
<tr>
<td>Intel® AVX</td>
<td>Advanced Vector Extensions</td>
<td>x86</td>
<td>eight 256-bit registers (512-bit for AVX-512)</td>
<td>* successor of SSE</td>
</tr>
<tr>
<td>Arm Neon</td>
<td>&nbsp;</td>
<td>ARM</td>
<td>thirty-two 128-bit registers</td>
<td>* available on all devices running Android 6.0 or higher,
<!-- TODO: source -->
* available on Apple products: iPhones, iPads, and Macs,
* can be used on x86 architectures with [NEON_2_SSE conversion headers](https://github.com/intel/ARM_NEON_2_x86_SSE).
</td>
</tr>
</tbody>
</table>

## Which SIMD To Use?

Since there are many instruction sets to choose from, one may wonder: how to choose the proper one?

The answer is, as always, it depends.

The first consideration is the architecture family you are writing software for.

For example, if you write software for Android devices, you most likely will use Neon. But not always! There are Android-driven devices that run on x86 architectures.

If you target x86 architectures only and want to leverage SIMD as much as possible, you should provide implementations for all x86 SIMD instruction sets and give software the fallback possibility: if, for example, AVX-512 is not present, maybe SSE can be used. Keep in mind that there is SSE, SSE2, SSE3, SSE4... And there are minor versions too.

If you don't have a clue on which platform your software will run on, you are facing the possibility of implementing every available instruction set support.

That's why compilers are such a blessing: they can do this heavy lifting for us. And make much fewer mistakes along the way. 🙂

## Why is SIMD useful in DSP?

SIMD is especially advantageous in digital signal processing applications. Why?

1. **DSP algorithm are often defined in terms of vectors.**
2. **DSP algorithms often require the same tasks on different data.**
3. **Signal processing is most often done in blocks.**
4. **SIMD instruction sets often contain DSP-specific functions.**

## The Disadvantages of SIMD

1. **Programmer's nightmare: supporting all instruction sets.**
2. **Run-time availability checks.**
3. **Unaligned data.**
4. **Edge cases, single samples.**

## Simple SIMD Code Example

## Summary

## Bibliography

https://stackoverflow.com/questions/8456236/how-is-a-vectors-data-aligned

https://en.wikipedia.org/wiki/AVX-512

