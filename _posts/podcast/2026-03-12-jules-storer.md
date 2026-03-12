---
title: "Julian Storer: Creator of JUCE C++ Framework | WolfTalk #032"
description: "Julian Storer discusses JUCE, Cmajor, Tracktion, compiler design, clean code, and using AI in audio development."
date: 2026-03-12
author: Jan Wilczek & Sathira Tennakoon
layout: post
permalink: /talk032/
background: /assets/img/posts/podcast/talk032/Thumbnail.webp
categories:
  - Podcast
tags:
  - cpp
  - juce
  - cmajor
  - plugin
  - digital audio workstation
  - software architecture
  - design principles
  - career
  - learning
  - cmake
  - hardware
  - java
  - rust
  - testing
discussion_id: 2026-03-12-julian-storer
---
Does Jules really hate CMake?

{% include 'redcircle-podcast-player', redcircle_podcast_id: '06926890-3c61-4601-be6b-a2ae32eb771c' %}

## Listen on

* 🎧 [Spotify (TBA)](#)
* 🎥 [YouTube](https://youtu.be/svAdgZrkUV8)
* 🎧 [Apple Podcasts (iTunes) (TBA)](#)
* 🎧 [TuneIn Radio (TBA)](#)

[All podcast episodes.](/podcast)

[Sign up for WolfSound's newsletter!]({% link collections.all, 'newsletter.md' %})

## Introduction

Julian "Jules" Storer is the creator of the JUCE C++ framework and the Cmajor programming language dedicated to audio.

He created JUCE in the late 90s, and it grew to become the most popular audio plugin development framework in the world. Apart from audio capabilities, it is a general-purpose cross-platform application development framework (Windows, macOS, Linux, Android, iOS, and embedded platforms). Most plugin companies use JUCE; whether you like it or not, it has become a de facto industry standard.

You know that I love JUCE; I created the [official JUCE audio plugin development course](https://www.wolfsoundacademy.com/juce?utm_source=julian-storer-podcast&utm_medium=blog) with them, and they are the sponsor of the podcast. So naturally, I was super excited to be able to interview Jules!

His next big thing is the Cmajor programming language. It is a C-like, LLVM-backed programming language dedicated solely to audio.

He has also given many talks at the Audio Developer Conference, so I encourage you to check them out as a way to relax and get inspired.

Jules is known for his strong opinions and dry humor, so I guarantee you'll find yourself chuckling every few minutes 😉

{% include 'podcast_cta' %}

## Episode contents

From this episode, you will learn:

- How Jules created the JUCE framework and distributed it initially
- How to maintain such huge codebases as JUCE
- Julian's coding principles that will make you (and me) a better dev
- What problem does CMajor solve, and how
- Which tools is Jules using when coding, especially when it comes to AI
- His exact everyday work routines and relaxation strategies, and
- Does Jules really hate CMake?

This episode was recorded on January 30, 2026.

## References

### People

1. Julian "Jules" Storer
   - [GitHub](https://github.com/julianstorer)
   - [LinkedIn](https://uk.linkedin.com/in/julian-storer)
2. JUCE Team at ROLI
   - [Fabian Renn-Giles](https://www.linkedin.com/in/fabian-r-8392bb90/)
   - [Timur Doumler](https://timur.audio/about)
   - [Tom Poole](https://www.linkedin.com/in/tbpoole/)
   - [Ed Davies](https://www.linkedin.com/in/ed-davies-833964115/)
3. Tracktion Team
   - [David Rowland](https://www.linkedin.com/in/david-rowland-478a22112/)
   - [James Woodburn](https://www.linkedin.com/in/james-woodburn-6b62304/)
   - Dave Christensen
4. Cmajor Team
   - [Cesare Ferrari](https://www.linkedin.com/in/cesareferrari/)
5. [Andrej Karpathy](https://karpathy.ai/)

### Jules' projects

1. JUCE (podcast sponsor ❤️)
   - [JUCE Website](https://juce.com)
   - [Official JUCE audio plugin development course](https://www.wolfsoundacademy.com/juce?utm_source=julian-storer-podcast&utm_medium=blog)
2. [Waveform DAW (previously Tracktion)](https://www.tracktion.com/products/waveform-pro)
3. [Tracktion Engine](https://github.com/Tracktion/tracktion_engine)
4. [Cmajor](https://cmajor.dev)

### Companies

- [Tracktion](https://www.tracktion.com)
- [ROLI](https://roli.com)
- [Native Instruments](https://www.native-instruments.com)
- [Lightworks](https://lwks.com)
- [Mackie](https://mackie.com)
- [Prism Sound](https://www.prismsound.com)
- [Anthropic](https://www.anthropic.com)
- [Suno](https://suno.com)

### Conferences & communities

- [Audio Developer Conference (ADC)](https://audio.dev)
- [JUCE Forum](https://forum.juce.com/)
- [KVR Audio Forum](https://www.kvraudio.com/forum/)

### Developer Tools

#### AI tools

- [Claude](https://claude.ai)
- [GPT-5](https://openai.com/gpt-5/)

#### IDEs

- [VS Code](https://code.visualstudio.com)
- [Visual Studio](https://visualstudio.microsoft.com)
- [Xcode](https://developer.apple.com/xcode)

#### Version control

- [Git](https://git-scm.com)
- [GitHub](https://github.com)
- [SourceTree](https://www.sourcetreeapp.com)
- [CVS](https://cvs.nongnu.org/)

#### Build systems

- [CMake](https://cmake.org)
- [Make](https://www.gnu.org/software/make/)

#### Compilers

- [LLVM](https://llvm.org)
- [Clang](https://clang.llvm.org)

#### Code instrumentation tools

- [Valgrind](https://valgrind.org)
- [Puppeteer](https://pptr.dev)
- [Cppcheck](https://cppcheck.sourceforge.io)

#### Frameworks

- [Qt](https://www.qt.io)

### Programming languages

- [C++](https://isocpp.org)
- [Cmajor](https://cmajor.dev)
- [Rust](https://www.rust-lang.org)
- [Java](https://www.java.com)
- [Go](https://go.dev)
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [Python](https://www.python.org)
- [Faust](https://faust.grame.fr)
- [WebAssembly](https://webassembly.org)
- HTML/CSS

### Hardware

- [Novation Launchpad](https://novationmusic.com/launchpad)
- [Dream ADA-128 Modular AD/DA Converter](https://beta.prismsound.com/products/ada-128/)

### Technical concepts

- [GNU General Public License](https://www.gnu.org/licenses/gpl-3.0.en.html)
- Plugin formats (VST / AU / AAX / LV2)
- JIT compilation
- Real-time / low-latency audio
- Test-driven development (TDD)
- Shader languages
- Static analysis and linting

Thank you for listening! 🙏

