---
title: "Audio and the C++ Standard with Timur Doumler | WolfTalk #028"
description: "Timur Doumler discusses audio programming, JUCE, Cradle, C++ standardization, real-time systems, and the future of C++ for audio."
date: 2025-11-30
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
  - hardware
  - juce
  - plugin
  - software architecture
  - testing
  - research
  - career
  - learning
discussion_id: 2025-11-30-timur-doumler
---

{% include 'redcircle-podcast-player', redcircle_podcast_id: ______________ %}

## Listen on

* 🎧 [Spotify]()
* 🎥 [YouTube]()
* 🎧 [Apple Podcasts]()
* 🎧 [TuneIn Radio]()

[All podcast episodes.](/podcast)

[Sign up for WolfSound's newsletter!]({% link collections.all, 'newsletter.md' %})

## Introduction

Timur Doumler is an audio programming consultant, C++ developer, and a major voice for audio programmers in the wider
developer community. He has worked with renowned organizations such as Native Instruments, ROLI, Bloomberg, and
JetBrains. At ROLI he contributed to early versions of the JUCE framework and became a familiar voice within the audio
developer community. He later joined JetBrains as a Developer Advocate and is known for his talks on modern C++ and 
real-time audio.

Timur is an active member of the ISO C++ Standards Committee, helping represent the needs of real-time audio
developers and influencing proposals for upcoming C++ standards. He is also the co-founder and CTO of Cradle, a company
building modern, artist-focused audio plugins.

In this episode, we discuss the direction of C++26, upcoming features that may transform real-time software, and what
it’s like advocating for performance-critical use cases inside a general-purpose language committee. We also explore
Timur’s career and experiences in a witty and enjoyable conversation.

{% include 'podcast_cta' %}

## Episode Contents

From this episode, you will learn:

- How Timur’s early interests and experiences led him toward audio programming.
- His early engineering work at Native Instruments, including contributions to Kontakt and NI’s internal C++ libraries.
- How he joined ROLI and worked on the development of JUCE.
- The story behind founding Cradle.
- How he became involved in the ISO C++ Standards Committee and helped bring audio industry needs to the wider C++
  community.
- Key features coming in the C++26 standard.
- Real-time and low-latency programming considerations in audio software.
- Practical advice on working with C++, designing audio software, and dealing with real-time constraints.

This episode was recorded on ______________

## People

- [Timur Doumler](https://timur.audio/about)
- [Julian Storer](https://www.linkedin.com/in/julian-storer/)
- [Fabian Renn-Giles](https://www.linkedin.com/in/fabian-r-8392bb90/)
- [Matthew Fudge](https://www.linkedin.com/in/matthew-fudge-2b79081b6/) - Co-founder of Cradle
- [Jaycen Joshua](http://www.jaycenjoshua.com) - Producer behind *The God Particle*
- [Louis Bell](https://www.instagram.com/louisbell/) - Vocal producer behind *The Spirit*
- [Scott Meyers](https://www.aristeia.com) - Author of *Effective C++*
- [Jon Kabat-Zinn](https://jonkabat-zinn.com)

## Companies & Organizations

- [Cradle](https://cradle.app)
- [Native Instruments](https://www.native-instruments.com/)
- [Ableton](https://www.ableton.com/en/)
- [ROLI](https://roli.com)
- [JetBrains](https://www.jetbrains.com/)
- [Bloomberg](https://www.bloomberg.com/)
- [ISO C++ Standards Committee](https://isocpp.org/std/the-committee)
- [ANSI](https://www.ansi.org)
- [BSI](https://www.bsigroup.com)
- [DIN](https://www.din.de/en)

## Universities & Research Institutions

- [Freie Universität Berlin](https://www.fu-berlin.de/en/index.html)
- [Université Claude Bernard Lyon 1](https://www.univ-lyon1.fr/en)
- [Leibniz Institute for Astrophysics Potsdam](https://www.aip.de/en/)

## Conferences, Communities & Media

- [Audio Developer Conference (ADC)](https://audio.dev)
- [CppCon](https://cppcon.org)
- CppCon Back To Basics Track
    - [2023](https://www.youtube.com/playlist?list=PLHTh1InhhwT6NbFOtrjCep42dSNstruLx)
    - [2022](https://www.youtube.com/playlist?list=PLHTh1InhhwT47Xpx7Cn-bPw9Qygjr98rs)
    - [2021](https://www.youtube.com/playlist?list=PLHTh1InhhwT4TJaHBVWzvBOYhp27UO7mI)
    - [2020](https://www.youtube.com/playlist?list=PLHTh1InhhwT5o3GwbFYy3sR7HDNRA353e)
- [CppCast Podcast](https://cppcast.com)
- [The Audio Programmer Community](https://www.theaudioprogrammer.com)
- [Audio Programmer Discord](https://www.theaudioprogrammer.com/learn-audio-programming)
- [C++ Language Slack Workspace](https://cppalliance.org/slack/)

## Talks & Publications by Timur

### Talks Mentioned

- [C++ in the Audio Industry (CppCon 2015)](https://youtu.be/boPEO2auJj4)
- [C++ in the Audio Industry — Part 2 (JUCE Summit 2015)](https://youtu.be/2vmXy7znEzs)
- [Demystifying std::memory_order (ADC 2025)](https://conference.audio.dev/session/2025/demystifying-stdmemory_order/)

### C++ Standard Proposals (Authored / Contributed)

- `[[assume]]`
- `[[assume_aligned]]`
- `start_lifetime_as`
- *in-place vector*
- Contract assertions (Design by Contract)

## Software, Tools & Technologies

### Programming Languages

- C++
- C
- FORTRAN
- Java
- Kotlin
- Rust

### Frameworks & Protocols

- [JUCE](https://juce.com)
- MPE (MIDI Polyphonic Expression)
- OSC (Open Sound Control)

### Audio Software & Plugins

- Native Instruments
    - [Guitar Rig](https://www.native-instruments.com/en/products/komplete/guitar/guitar-rig-7-pro/)
    - [Kontakt](https://www.native-instruments.com/en/products/komplete/samplers/kontakt-8)
- ROLI
    - [BLOCKS](https://www.soundonsound.com/reviews/roli-blocks)
    - [NOISE](https://apps.apple.com/uk/app/noise/id1011132019)
- Cradle
    - [The Prince](https://cradle.app/products/the-prince)
    - [The God Particle](https://cradle.app/products/the-god-particle)
    - [The Spirit](https://cradle.app/products/the-spirit)

### Developer Tools & Practices

- [Git](https://git-scm.com)
- [CLion](https://www.jetbrains.com/clion)
- IDE workflows
- Test-Driven Development (TDD)
- Real-time programming
- Low-latency programming
- [GCC](https://gcc.gnu.org)
- [Clang/LLVM](https://clang.llvm.org)
- [MSVC](https://learn.microsoft.com/en-us/cpp/?view=msvc-170)

## Technical Concepts

- Real-time audio constraints
- Lock-free / wait-free data structures
- Lock-free queues
- Seqlocks
- SIMD and vectorization
- Memory ordering
- Compiler considerations (GCC, Clang, MSVC)
- RealTimeSanitizer
- `std::execution` (C++26)
- Hardware Architectures
    - [PowerPC](https://www.ibm.com/docs/en/aix/7.3.0?topic=storage-power-family-powerpc-architecture-overview)
    - [RISC-V](https://riscv.org)

## Artistic & Cultural References

- [Star Trek](https://www.startrek.com/en-un)
- [Meshuggah](https://www.meshuggah.net)
- [Animals As Leaders](https://animalsasleaders.org)
- [Dream Theater](https://dreamtheater.net)

Thank you for listening! 🙏
