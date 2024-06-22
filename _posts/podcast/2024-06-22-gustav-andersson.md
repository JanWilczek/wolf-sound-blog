---
title: "Audio C++ Architecture, Optimization & Best Practices With Gustav Andersson | WolfTalk #022"
description: "Interview with Gustav Andersson: senior C++ audio developer at Elk Audio. Learn how to write well-structured, highly-optimized real-time C++ audio code."
date: 2024-06-22
author: Jan Wilczek
layout: post
permalink: /talk022/
background: /assets/img/posts/podcast/talk022/Thumbnail.webp
categories:
  - Podcast
tags:
  - cpp
  - juce
  - career
  - learning
  - plugin
  - software architecture
  - testing
  - hardware
  - effects
discussion_id: 2024-06-22-gustav-andersson
---
Learn how to write well-structured, highly-optimized real-time C++ audio code from a senior C++ audio developer at Elk Audio.

## Listen on

* 🎧 [Spotify](#)
* 🎥 [YouTube](#)
* 🎧 [Apple Podcasts (iTunes)](#)
* 🎧 [Amazon Music](#)
* 🎧 [Google Podcasts](#)
* 🎧 [TuneIn Radio](#)

[All podcast episodes.](/podcast)

[Sign up for WolfSound's newsletter!]({% link collections.all, 'newsletter.md' %})

## Introduction

One of [my top 10 Audio Developer Conference 2023 talks]({% post_url collections.posts, 'programming-in-general/2024-01-11-top-10-audio-developer-conference-2023-talks.md' %}) was [Gustav Andersson’s talk on optimizing C++ audio code](https://youtu.be/HdyiQLQCvfs?si=0Yi26KVDWurYweUf).

This made it all the more exciting to have Gustav on the show!

**Gustav Andersson** is a Swedish senior C++ audio developer at Elk Audio. He has worked on their Sensus guitar featuring a rich set of controls, Elk Audio OS for embedded platforms, Sushi digital audio workstation, and Elk Live software for live music collaboration over the internet.

Having studied Electrical Engineering and Digital Signal Processing, Gustav had been looking for a very long time to get into the audio industry. As for many developers, getting his first audio-related job was like a dream come true.

In his free time, Gustav plays and composes his own music.

In the interview, we discuss Gustav’s story, his journey to learn audio programming in C++, and his software projects, including his own plugin. We don’t shy away from software engineering details and architectural challenges of complex software like DAWs.

We mention a ton of resources and tips for learning real-time & scalable audio C++, so stay tuned for these!

*Note:* If you like the podcast so far, please, [go to Apple Podcasts and leave me a review there](https://podcasts.apple.com/us/podcast/wolftalk-podcast-about-audio-programming-people-careers/id1595913701). You can [do so on Spotify as well](https://open.spotify.com/show/5xc7EJiH9shG6zdSC5ejyw?si=eb35597e60a54e70). It will benefit both sides: more reviews mean a broader reach on Apple Podcasts and feedback can help me to improve the show and provide better quality content to you. You can also subscribe and give a like on [YouTube](https://youtube.com/c/WolfSoundAudio). Thank you for doing this 🙏

{% render 'google-ad.liquid' %}

## Episode contents

From this podcast episode, you will learn:

* How Gustav’s interest in music and electronics led him to study digital signal processing,
* How he landed his first (and last) job in the audio industry,
* What he needed to learn from C++ for audio programming and which resources he used,
* What are the challenges of building digital audio workstations,
* How to approach building audio software in general,
* How to learn C++ optimization (fast!),
* How to relax and disengage from focused work 😎

This podcast was recorded on January 30, 2024.

## References

Below you’ll find all people, places, and references mentioned in the podcast episode.

- Gustav Andersson
    - [NB01 plugin](https://www.kvraudio.com/product/nb01---distortion-sustainer-by-noizebox-industries)
- [Chalmers University of Technology](https://www.chalmers.se/en/)
- Programming languages
    - C
    - C++
        - [Dear ImGui GUI library for C++](https://github.com/ocornut/imgui)
        - [OpenGL graphics library](https://www.opengl.org/)
        - [Vulkan graphics library](https://www.vulkan.org/)
        - [Compiler Explorer](https://godbolt.org/)
        - [Google Benchmark benchmarking library](https://github.com/google/benchmark)
        - [Valgrind](https://valgrind.org/): a suite of tools for detecting memory management and threading bugs, and profiling
        - [Twine: C++ threading library](https://codeberg.org/jfinkhaeuser/twine)
    - Java
    - Python
    - SuperCollider
    - Lua
- Companies
    - Elk Audio (Mind Music Labs)
        - People:
            - [Stefano Zambon](https://www.linkedin.com/in/stefano-zambon-38113410a?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAABttfBEB_ouCihI5cIyESCoAUvPBxj5i2_w&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_all%3BAy3ZCttkRiaiH66wd7G5CA%3D%3D) (founder)
            - [Ilias Bergström](https://www.linkedin.com/in/ilias-bergstr%C3%B6m-0ba8aa4?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAAADYDg4Bbu5bPW5JVA2E1VNQkjffAC15sT4&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_all%3BjdVdrBVGSmCK%2BnNsipYTNg%3D%3D)
        - Products
            - Sensus guitar [(demo video](https://youtu.be/fqzEQnsSIoY?si=z52M9HwSJ7Q0mgfC))
            - Elk Audio OS (open source)
            - Sushi digital audio workstation (open source)
            - ElkLive (2.0) standalone + plugin
    - Ericsson
    - [Arturia](https://www.arturia.com/)
    - [Fishman guitar pickups](https://www.fishman.com/)
- Resources on C++ and audio programming
    - [KVR developer forum](https://www.kvraudio.com/forum)
    - [Ross Bencina’s blog](http://www.rossbencina.com/)
    - [C++ Core Guidelines](https://github.com/isocpp/CppCoreGuidelines)
    - [Audio Developer Conference](https://audio.dev/)
    - [CppCon](https://cppcon.org/)
    - Andrei Alexandrescu: *Modern C++ Design* book
- Technology concepts
    - [Serial Peripheral Interface (SPI) communication](https://en.wikipedia.org/wiki/Serial_Peripheral_Interface)
    - [UDP hole punching](https://en.wikipedia.org/wiki/UDP_hole_punching)
    - ISP: internet service provider
    - COM: Component Object Model, a standard for software components and a C++ programming paradigm on Windows
- Software
    - [Ardour digital audio workstation](https://github.com/Ardour/ardour)
    - [JACK Audio Connection Kit](https://wiki.archlinux.org/title/JACK_Audio_Connection_Kit)
    - [Yocto Project for creating Linux distros](https://www.yoctoproject.org/)
    - CLion IDE
    - [No Budget Orchestra (NBO) plugins](https://linuxmusicians.com/viewtopic.php?t=25459)
- Hardware
    - Amiga personal computer
    - Printed ciruit boards (PCBs)
    - Roland Funny Cat guitar pedal
- Music
    - MUSE (band)
        - Matt Bellamy
    - [Music for Programming](https://musicforprogramming.net/latest/)

Thank you for listening! 🙏

**Who should I invite next? Let me know in the comments below!**
