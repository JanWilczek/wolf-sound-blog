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

<script async defer onload="redcircleIframe();" src="https://api.podcache.net/embedded-player/sh/bf40a1d2-7e41-4ddb-8c3a-ed82394723ba/ep/acf8e644-e9cb-4511-90c3-7fcb6e92a606"></script> <div class="redcirclePlayer-acf8e644-e9cb-4511-90c3-7fcb6e92a606"></div> <style> .redcircle-link:link { color: #ea404d; text-decoration: none; } .redcircle-link:hover { color: #ea404d; } .redcircle-link:active { color: #ea404d; } .redcircle-link:visited { color: #ea404d; } </style>
<p style="margin-top:3px;margin-left:11px;font-family: sans-serif;font-size: 10px; color: gray;">Powered by <a class="redcircle-link" href="https://redcircle.com?utm_source=rc_embedded_player&utm_medium=web&utm_campaign=embedded_v1">RedCircle</a></p>

## Listen on

* 🎧 [Spotify](https://open.spotify.com/episode/16J1S3poIFclIAfUAmD9mb?si=7OBl92-ORYeCdDJncx9BWw)
* 🎥 [YouTube](https://youtu.be/x3-BIT-1yv8)
* 🎧 [Apple Podcasts (iTunes)](https://podcasts.apple.com/us/podcast/building-daw-software-with-dave-rowland-tracktion/id1595913701?i=1000662958374)
* 🎧 [TuneIn Radio](http://tun.in/tBYccT)

[All podcast episodes.](/podcast)

[Sign up for WolfSound's newsletter!]({% link collections.all, 'newsletter.md' %})

## Introduction

Dave Rowland is the CTO of Audio Squadron: a group of audio-related companies. More specifically, he's the architect and the lead developer of the Waveform digital audio workstation (DAW) and an Audio Manager of Prism Sound (which focuses on audio hardware manufacturing). He's also a very successful speaker, having given talks at conferences like Audio Developer Conference or C++ on Sea.

Given the popularity of Dave's talks and his 11-year long (as of 2024) experience in developing the Waveform DAW and its open source engine, I am incredibly excited to have him on the WolfTalk podcast.

During the interview, we learn not only Dave's story but we also discuss the challenges of building real-time audio software including DAWs and learning C++, software architecture, and high-performance real-time programming concerning audio. Dave shares a ton of highly useful tips and resources so you don't want to miss out on this one!

*Note:* If you like the podcast so far, please, [go to Apple Podcasts and leave me a review there](https://podcasts.apple.com/us/podcast/wolftalk-podcast-about-audio-programming-people-careers/id1595913701). You can [do so on Spotify as well](https://open.spotify.com/show/5xc7EJiH9shG6zdSC5ejyw?si=eb35597e60a54e70). It will benefit both sides: more reviews mean a broader reach on Apple Podcasts and feedback can help me to improve the show and provide better quality content to you. You can also subscribe and give a like on [YouTube](https://youtube.com/c/WolfSoundAudio). Thank you for doing this 🙏

{% render 'google-ad.liquid' %}

## Episode contents

From this podcast episode, you will learn:

* how Dave organizes his day for maximum productivity,
* which tools he's leveraging on the day-to-day basis,
* how he went from being a music technology student to a freelance audio developer to the lead developer on the Tracktion DAW (now Waveform),
* how he approaches creating his widely acclaimed conference talks,
* which resources to use to learn high-performance real-time programming.

This podcast was recorded on March 25, 2024.

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

- People
    - [Dave Rowland](https://www.linkedin.com/in/david-rowland-478a22112/)
    - [Tom Mitchell](https://www.linkedin.com/in/thomas-mitchell-72172013/)
    - [Julian Storer](https://www.linkedin.com/in/julian-storer-2412b194/)
    - Woody from Mackie
    - Dave Christenson from Mackie
        - Before he worked for Mackie was the lead singer of the 80’s pop band [The Stabilizers](https://en.wikipedia.org/wiki/Stabilizers_(band))
    - Roland Rabien
        - https://github.com/FigBug/
        - https://socalabs.com/
    - [Cesare Ferrari](https://www.linkedin.com/in/cesareferrari/)
    - [Fabian Renn-Giles](https://www.linkedin.com/in/fabian-r-8392bb90/)
    - [Timur Doumler](https://timur.audio/about)
    - Wolfram from Tracktion
        - [Stroke Machine iOS app](https://www.kvraudio.com/product/stroke-machine-by-franke-music)
- [University of the West of England](https://www.uwe.ac.uk/)
    - Music Systems Engineering: apparently replaced by [Audio and Music Technology](https://courses.uwe.ac.uk/J932/audio-and-music-technology)
- Programming languages
    - C
    - C++
        - [JUCE C++ framework](https://juce.com/) (podcast sponsor 🎉 )
        - [NanoRange](https://github.com/tcbrindle/NanoRange) library
        - [flux](https://github.com/tcbrindle/flux) library
        - [TartanLlama/expected](https://github.com/TartanLlama/expected) library
        - [magic_enum](https://github.com/Neargye/magic_enum) library
        - [fmt](https://github.com/fmtlib/fmt) formatting library
    - Rust
    - bash scripting language
    - Max/MSP
    - Python
    - [Scratch](https://en.wikipedia.org/wiki/Scratch_(programming_language))
    - [CMajor](https://cmajor.dev/)
- Companies
    - dRowAudio: Dave’s freelance company from before Tracktion
    - [Audio Squadron](https://www.audiosquadron.com/): a group of audio-related companies consisting of
        - [Tracktion Corporation](https://www.tracktion.com/)
            - [Tracktion DAW, currently Waveform](https://www.tracktion.com/products/waveform-pro)
                - [Waveform 13 feature list](https://www.tracktion.com/products/waveform-pro-features)
            - [Tracktion Engine](https://github.com/Tracktion/tracktion_engine): fully featured DAW engine
                - [List of features](https://github.com/Tracktion/tracktion_engine/blob/develop/FEATURES.md)
            - [pluginval](https://github.com/Tracktion/pluginval): audio plugin validation tool
        - [Prism Sound](https://www.prismsound.com/)
        - [SADiE](https://www.sadie.com/sadie_home.php)
            - DAW + dedicated hardware
        - 2JW Design
    - [Mackie](https://mackie.com/)
    - [Native Instruments group](https://www.native-instruments.com/en/)
        - SoundStacks
    - [Roli](https://roli.com/)
    - [PACE](https://paceap.com/)
    - [CMajor Software Ltd.](https://cmajor.dev/)
- Programming concepts
    - [Builder pattern](https://en.wikipedia.org/wiki/Builder_pattern)
    - [Model-View-Controller pattern](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller)
    - JUCE’s [ValueTree](https://docs.juce.com/master/classValueTree.html)
    - Audio Unit: plugin format from Apple
- Resources to learn C++ and audio programming
    - online conference recordings
    - finance industry
    - game industry
    - [Read-Copy-Update talk](https://youtu.be/7fKxIZOyBCE?si=gGt4LA34ZcOKPOyz) by Timur Doumler
    - Low-latency C++ talk by Timur Doumler
        - [Part 1](https://youtu.be/EzmNeAhWqVs?si=xHUh5yOI8txS9IA8)
        - [Part 2](https://youtu.be/5uIsadq-nyk?si=30USxfgTIN9zOZb8)
    - Fedor Pikus’s talks
    - David Gross’s talks
        - E.g., [“Trading at light speed”](https://youtu.be/8uAW5FQtcvE?si=sGJHyg8ntgWIcpRY)
    - Daniel Anderson talks
        - [Concurrent access to smart pointers](https://youtu.be/OS7Asaa6zmY?si=GC-SXIcQmCs17A95)
        - [Lock-free atomic shared pointers](https://youtu.be/lNPZV9Iqo3U?si=PWpHUKcyw9S-7Qvc)
    - Dave’s talks
        - Real-time 101 (with Fabian Renn-Giles)
            - [Part 1](https://youtu.be/Q0vrQFyAdWI?si=JIq5ux_pcbgsGNOn)
            - [Part 2](https://youtu.be/PoZAo2Vikbo?si=uQP7m-GCktsdkngf)
        - [Optimising a real-time audio processing library](https://youtu.be/FpymA7NLNDs?si=FFQbZpo9IPr-gHoJ)
        - [JUCE’s ValueTree](https://youtu.be/3IaMjH5lBEY?si=WnUtP5jUacEWNpKS)
- Audio-related communities
    - [JUCE forum](https://forum.juce.com/)
    - [The Audio Programmer’s Discord](https://www.theaudioprogrammer.com/discord)
- Conferences
    - JUCE Summit (now [Audio Developer Conference](https://audio.dev/))
    - [CppCon](https://www.youtube.com/@CppCon)
    - [Cpp on Sea](https://www.youtube.com/@cpponsea)
    - [C++ Online](https://www.youtube.com/@CppOnline)
    - [Meeting Cpp](https://www.youtube.com/@MeetingCPP)
    - [CppNow](https://www.youtube.com/@BoostCon)
- Tools
    - XCode
    - CLion
    - Github Actions
    - Azure Pipelines
    - Apple Clang
    - [Realtime-Safety Sanitizer (RADSan)](https://github.com/realtime-sanitizer/radsan)
    - [ChatGPT](https://openai.com/chatgpt/)

Thank you for listening! 🙏

**Who should I invite next? Let me know in the comments below!**

