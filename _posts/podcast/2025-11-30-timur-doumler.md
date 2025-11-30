---
title: "Audio and the C++ Standard with Timur Doumler | WolfTalk #031"
description: "Timur Doumler discusses audio programming, JUCE, Cradle, C++ standardization, real-time systems, and the future of C++ for audio."
date: 2025-11-30T08
author: Jan Wilczek & Sathira Tennakoon
layout: post
permalink: /talk031/
background: /assets/img/posts/podcast/talk031/Thumbnail.webp
categories:
  - Podcast
tags:
  - cpp
  - c
  - simd
  - juce
  - plugin
  - testing
  - career
  - learning
  - rust
discussion_id: 2025-11-30-timur-doumler
---
C++ Standards Committee member, ex-Native Instruments, ex-JUCE, ex-JetBrains, oh my!

{% include 'redcircle-podcast-player', redcircle_podcast_id: '2ecd4477-4ea1-4d35-8154-9b6f95255d2d' %}

## Listen on

* 🎧 [Spotify](https://open.spotify.com/episode/0GZAhxELCsnonYvoEwP3hd?si=ATHDSZ1eQW22cdH953CotA)
* 🎥 [YouTube](https://youtu.be/_ErQlwHJQL8)
* 🎧 [Apple Podcasts]()
* 🎧 [TuneIn Radio]()

[All podcast episodes.](/podcast)

[Sign up for WolfSound's newsletter!]({% link collections.all, 'newsletter.md' %})

## Introduction

How do you become a C++ Standards Committee member?

Why is C++ prevalent in audio?

Should you still use it for audio software?

Honestly, Timur Doumler is someone I have looked up to ever since I saw his "C++ in the audio industry" talk at CppCon 2015.

He has a rich development history with C++ and/or audio:

- developer at Native Instruments
- developer of the JUCE C++ framework (podcast sponsor ❤️)
- C++ linter developer and developer advocate at JetBrains (who make the CLion IDE)
- founder of Cradle, an audio plugin startup
- C++ Standards Committee member
- CppCast podcast host
- notorious Audio Developer Conference and CppCon speaker

I have probably missed a ton of stuff here, but that should already give you a flavor of what Timur is up to 😉

I especially enjoy his technical talks on synchronization with the (real-time) audio thread; For example, at the Audio Developer Conference 2025, he made me finally understand memory ordering in C++ (or so I believe 😅)

In the podcast interview, we discuss his story, tactics, and tips, which I hope will inspire you to follow his footsteps (as they sure did me).

It also turns out we are both fond of the same music band... Listen to the interview to find out which one 😁

All in all, **this one of my favorite podcast episodes** (audio & C++, what more do you need?), so don't miss it!

{% include 'podcast_cta' %}

## Episode Contents

From this episode, you will learn:

- How Timur’s early interests and experiences led him toward audio programming
- His early engineering work at Native Instruments, including contributions to Kontakt and NI’s internal C++ libraries
- How he joined ROLI and worked on the development of JUCE
- The story behind founding Cradle
- How he became involved in the ISO C++ Standards Committee including his audio-related contributions
- What he's most excited for in the upcoming C++26 standard
- How he approaches software development and maintaining a healthy work-life balance (that was a great one to learn for me personally, too)

This episode was recorded on September 26, 2025.

## References

### People

- [Timur Doumler](https://timur.audio/about)
- [Julian Storer](https://www.linkedin.com/in/julian-storer/)
- [Fabian Renn-Giles](https://www.linkedin.com/in/fabian-r-8392bb90/)
- [Matthew Fudge](https://www.linkedin.com/in/matthew-fudge-2b79081b6/) - Co-founder of Cradle
- [Jaycen Joshua](http://www.jaycenjoshua.com) - Producer behind *The God Particle*
- [Louis Bell](https://www.instagram.com/louisbell/) - Vocal producer behind *The Spirit*
- [Scott Meyers](https://www.aristeia.com) - Author of *Effective C++*
- [Jon Kabat-Zinn](https://jonkabat-zinn.com)

### Companies & Organizations

- [Cradle](https://cradle.app)
    - [The Prince plugin](https://cradle.app/products/the-prince)
    - [The God Particle plugin](https://cradle.app/products/the-god-particle)
    - [The Spirit plugin](https://cradle.app/products/the-spirit)
- [Native Instruments](https://www.native-instruments.com/)
    - [Guitar Rig plugin](https://www.native-instruments.com/en/products/komplete/guitar/guitar-rig-7-pro/)
    - [Kontakt plugin](https://www.native-instruments.com/en/products/komplete/samplers/kontakt-8)
- [Ableton](https://www.ableton.com/en/)
- [ROLI](https://roli.com)
    - [BLOCKS device](https://www.soundonsound.com/reviews/roli-blocks)
    - [NOISE app](https://apps.apple.com/uk/app/noise/id1011132019)
- [JetBrains](https://www.jetbrains.com/)
- [Bloomberg](https://www.bloomberg.com/)
- [ISO C++ Standards Committee](https://isocpp.org/std/the-committee)
- [ANSI](https://www.ansi.org)
- [BSI](https://www.bsigroup.com)
- [DIN](https://www.din.de/en)

### Universities & Research Institutions

- [Freie Universität Berlin](https://www.fu-berlin.de/en/index.html)
- [Université Claude Bernard Lyon 1](https://www.univ-lyon1.fr/en)
- [Leibniz Institute for Astrophysics Potsdam](https://www.aip.de/en/)

### Conferences, Communities & Media

- [Audio Developer Conference (ADC)](https://audio.dev)
- [CppCon](https://cppcon.org)
- [CppCon Back To Basics Track](https://www.youtube.com/@CppCon/search?query=back%20to%20basics)
- [CppCast Podcast](https://cppcast.com) - C++ podcast co-hosted by Timur
- [The Audio Programmer](https://www.theaudioprogrammer.com)
- [C++ Language Slack Workspace](https://cppalliance.org/slack/)

### Timur's Talks Mentioned

- [C++ in the Audio Industry (CppCon 2015)](https://youtu.be/boPEO2auJj4)
- [C++ in the Audio Industry — Part 2 (JUCE Summit 2015)](https://youtu.be/2vmXy7znEzs)
- [Demystifying std::memory_order (ADC 2025)](https://conference.audio.dev/session/2025/demystifying-stdmemory_order/)

### Timur's C++ Standard Proposals (Authored / Contributed)

- [`[[assume]]`](https://en.cppreference.com/w/cpp/language/attributes/assume.html)
- [`[[assume_aligned]]`](https://en.cppreference.com/w/cpp/memory/assume_aligned.html)
- [`std::start_lifetime_as`](https://en.cppreference.com/w/cpp/memory/start_lifetime_as.html)
- [`std::inplace_vector`](https://en.cppreference.com/w/cpp/container/inplace_vector.html)
- [Contract assertions](https://en.cppreference.com/w/cpp/language/contracts.html)

### Programming Languages

- C++
- C
- FORTRAN
- Java
- Kotlin
- Rust

### Developer Tools

- [JUCE](https://juce.com) - podcast sponsor ❤️
- [Git](https://git-scm.com)
- [CLion](https://www.jetbrains.com/clion)
- [GCC](https://gcc.gnu.org)
- [Clang/LLVM](https://clang.llvm.org)
- [MSVC](https://learn.microsoft.com/en-us/cpp/?view=msvc-170)

### Technical Concepts

- MPE (MIDI Polyphonic Expression)
- OSC (Open Sound Control)
- Test-Driven Development (TDD)
- Real-time/low-latency programming
- Lock-free / wait-free data structures
    - Lock-free queues
- [Seqlock](https://en.wikipedia.org/wiki/Seqlock)
- SIMD and vectorization
- Memory ordering
- [RealTimeSanitizer](https://clang.llvm.org/docs/RealtimeSanitizer.html)
- [`[[std::execution]]`](https://en.cppreference.com/w/cpp/experimental/execution.html)
- Hardware architectures
    - [PowerPC](https://www.ibm.com/docs/en/aix/7.3.0?topic=storage-power-family-powerpc-architecture-overview)
    - [RISC-V](https://riscv.org)

### Music & Film

- [Star Trek](https://www.startrek.com/en-un)
- [Meshuggah](https://www.meshuggah.net)
- [Animals As Leaders](https://animalsasleaders.org)
- [Dream Theater](https://dreamtheater.net)

Thank you for listening! 🙏

