---
title: "Building DAW Software with Dave Rowland (Tracktion, Prism Sound) | WolfTalk #023"
description: "WolfTalk podcast interview with Dave Rowland: architect of the Waveform DAW and senior audio C++ programmer."
date: 2024-07-22
author: Jan Wilczek
layout: post
permalink: /talk023/
background: /assets/img/posts/podcast/talk023/Thumbnail.webp
categories:
  - Podcast
tags:
  - c
  - cpp
  - cmajor
  - digital audio workstation
  - juce
  - career
  - learning
  - plugin
  - software architecture
  - testing
discussion_id: 2024-07-22-dave-rowland
---
Architect of Waveform DAW & real-time C++ programming expert.

<!-- TODO: RedCircle player -->

## Listen on

* 🎧 [Spotify](#)
* 🎥 [YouTube](#)
* 🎧 [Apple Podcasts (iTunes)](#)
* 🎧 [Amazon Music](#)
* 🎧 [Google Podcasts (TBA)](#)
* 🎧 [TuneIn Radio (TBA)](#)

[All podcast episodes.](/podcast)

[Sign up for WolfSound's newsletter!]({% link collections.all, 'newsletter.md' %})

## Introduction

Dave Rowland is the CTO of Audio Squadron: a group of audio-related companies. More specifically, he's the architect and the lead developer of the Waveform digital audio workstation (DAW) and an Audio Manager of Prism Sound (which focuses on audio hardware manufacturing). He's also a very successful speaker, having given talks at conferences like Audio Developer Conference or C++ on Sea.

Given the popularity of Dave's talks and his X-year long experience in developing the Waveform DAW and its open source engine, I am incredibly excited to have him on the WolfTalk podcast.

During the interview, we learn not only Dave's story but we also discuss the challenges of building real-time audio software including DAWs and learning C++, software architecture, and high-performance real-time programming concerning audio. Dave shares a ton of highly useful tips and resources so you don't want to miss out this one!

*Note:* If you like the podcast so far, please, [go to Apple Podcasts and leave me a review there](https://podcasts.apple.com/us/podcast/wolftalk-podcast-about-audio-programming-people-careers/id1595913701). You can [do so on Spotify as well](https://open.spotify.com/show/5xc7EJiH9shG6zdSC5ejyw?si=eb35597e60a54e70). It will benefit both sides: more reviews mean a broader reach on Apple Podcasts and feedback can help me to improve the show and provide better quality content to you. You can also subscribe and give a like on [YouTube](https://youtube.com/c/WolfSoundAudio). Thank you for doing this 🙏

{% render 'google-ad.liquid' %}

## Episode contents

From this podcast episode, you will learn:

* how Dave organizes his day for maximum productivity,
* which tools he's leveraging on the day-to-day basis,
* how he went from being a music systems engineering student to a freelance audio developer to the lead developer on the Tracktion DAW (now Waveform),
* how he approaches creating his widely acclaimed conference talks,
* which resources to use to learn high-performance real-time programming.

<!-- TODO: This podcast was recorded on January 30, 2024. -->

## Dave’s tips on being a good audio programmer

1. If you want to learn something, teach it.
2. Have good test coverage and benchmarks.
3. Write down the requirements (for the project you’re working on).
4. Write tests.
5. Give talks.
6. Approach programming as problem solving.
7. Use tools available to you.
8. Talk to other programmers.
9. Real-time programming is hard because it cannot be tested; RADSan (Realtime-Safety Sanitizer) may help in that.
10. Try NOT to do stuff to optimize; use a profiler.

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
