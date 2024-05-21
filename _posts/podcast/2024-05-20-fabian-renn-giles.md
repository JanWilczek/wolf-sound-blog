---
title: "How To Master Real-Time Audio C++ With Fabian Renn-Giles | WolfTalk #021"
description: "Interview with one of the most famous audio programmers in the world: author of many audio plugins, libraries, and apps. Learn his strategies for real-time, performant C++ audio code."
date: 2024-05-20
author: Jan Wilczek
layout: post
permalink: /talk021/
background: /assets/img/posts/podcast/talk021/Thumbnail.webp
categories:
  - Podcast
tags:
  - cpp
  - juce
  - career
  - learning
  - plugin
  - python
  - software architecture
  - testing
  - template metaprogramming
  - simd
  - swift
discussion_id: 2024-05-20-fabian-renn-giles
---
Former lead developer of JUCE shares his journey and insights into audio programming!

<script async defer onload="redcircleIframe();" src="https://api.podcache.net/embedded-player/sh/bf40a1d2-7e41-4ddb-8c3a-ed82394723ba/ep/04962693-6dc4-41a3-b5ca-1a80921df0ca"></script> <div class="redcirclePlayer-04962693-6dc4-41a3-b5ca-1a80921df0ca"></div> <style> .redcircle-link:link { color: #ea404d; text-decoration: none; } .redcircle-link:hover { color: #ea404d; } .redcircle-link:active { color: #ea404d; } .redcircle-link:visited { color: #ea404d; } </style>
<p style="margin-top:3px;margin-left:11px;font-family: sans-serif;font-size: 10px; color: gray;">Powered by <a class="redcircle-link" href="https://redcircle.com?utm_source=rc_embedded_player&utm_medium=web&utm_campaign=embedded_v1">RedCircle</a></p>

## Listen on

* 🎧 [Spotify](https://open.spotify.com/episode/0fQw83kqXXXAy4BZj7L0jf?si=jVpQMeL9Qry16Rww103OuA)
* 🎥 [YouTube](https://youtu.be/VysC2eET5K8)
* 🎧 [Apple Podcasts (iTunes)](https://podcasts.apple.com/us/podcast/how-to-master-real-time-audio-c-with-fabian-renn-giles/id1595913701?i=1000656174630)
* 🎧 [Amazon Music](https://music.amazon.com/podcasts/b42682b5-61ba-4a6f-8b11-aed42b07ef9f/episodes/d06ac668-48cb-44d6-8d75-95c908f77ad5/how-to-master-realtime-audio-c-with-fabian-renngiles-wolftalk-021)
* 🎧 [Google Podcasts](https://podcasts.google.com/feed/aHR0cHM6Ly9mZWVkcy5yZWRjaXJjbGUuY29tL2JmNDBhMWQyLTdlNDEtNGRkYi04YzNhLWVkODIzOTQ3MjNiYQ/episode/OTM0NTIwYTMtZjNjZi00ZTVjLWFjOWYtMDI3YWU2NzhmMmJi?sa=X&ved=0CAUQkfYCahcKEwiIzuKvgJ2GAxUAAAAAHQAAAAAQAQ)
* 🎧 [TuneIn Radio](http://tun.in/tBl1zt)

[All podcast episodes.](/podcast)

[Sign up for WolfSound's newsletter!]({% link collections.all, 'newsletter.md' %})

## Introduction

In this podcast episode, I was delighted to be able one of the most prominent people of the audio developer landscape: Fabian Renn-Giles.

Fabian is a former lead developer of JUCE, currently working as an independent contractor. He has worked with many great companies (e.g., iZotope, Behringer) and has an incredible [portfolio](https://www.linkedin.com/in/fabian-r-8392bb90/). He is regarded as an expert of real-time, low-latency C++ audio programming.

You may know him from his talks at the Audio Developer Conference or at CppCon.

He’s also an incredibly kind and modest person; anyone that I’ve talked to about Fabian only had praise for his skills and his very down-to-earth attitude.

In the light of all the above, this interview is a real treat for everyone who’d like to become a real-time audio C++ expert!

*Note:* If you like the podcast so far, please, [go to Apple Podcasts and leave me a review there](https://podcasts.apple.com/us/podcast/wolftalk-podcast-about-audio-programming-people-careers/id1595913701). You can [do so on Spotify as well](https://open.spotify.com/show/5xc7EJiH9shG6zdSC5ejyw?si=eb35597e60a54e70). It will benefit both sides: more reviews mean a broader reach on Apple Podcasts and feedback can help me to improve the show and provide better quality content to you. You can also subscribe and give a like on [YouTube](https://youtube.com/c/WolfSoundAudio). Thank you for doing this 🙏

{% render 'google-ad.liquid' %}

## Episode contents

In this podcast episode, you will learn:

* how Fabian self-taught himself programming at the age of 6 (sic!),
* how he co-founded Fielding DSP, which serves as his professional outlet for programming services,
* how he became the lead developer of the JUCE C++ framework and what he learned from it,
* how to learn real-time audio C++ programming even if you are just starting out,
* how to become a freelance audio developer like Fabian (what you won’t learn at a university),
* how to optimize your audio code for maximum performance,
* the secret story of the “Real-Time 101” talk that Fabian did together with Dave Rowland and which is one of the most widely cited talks in the audio programming space,
* what are the issues in audio software architecture and how to conceptualize them,
* what are Fabian’s day-to-day programming tools for optimal productivity.

This episode was recorded on January 26, 2024.

## Tips from Fabian on C++ audio programming

1. A mentors should let their mentees fail and learn from their mistakes.
2. Always be proud of your code.
3. Find a good company to learn at.
4. (on writing clean C++) “How would you write it in Java?”
5. Zoom out code to see if code looks good.
6. Don’t use auto-formatters.
7. To get contracting jobs, do conference talks.
8. There’s more audio-related work out there than you think.
9. Network with other developers.
10. Work on your CV; climb the ladder of well-known companies.
11. Don’t be too hard on yourself, follow your passion and interests (but take it with a grain of salt).
12. Good learning strategy of audio: bottom-up, close to the hardware.
13. Use Godbolt; learn to read assembly.
14. Command to ChatGPT: “Explain it to me like a C++ developer”.
15. Use study groups.
16. You can learn a lot from debugging code.
17. Did the compiler vectorize? (It should, for optimality).
18. Is there a call instruction in assembly? (There should not be, something did not inline).
19. Vector instructions are rare to write manually.
20. Compiler can have bugs.
21. Think of end value for your customer.
22. Split your app into business logic and a real-time audio part.
23. Use VST3 or AAX SDKs directly to learn the architecture.
24. 80% of the work is groundwork (easy coding).

## References

Below you’ll find all people, places, and references mentioned in the podcast episode.

1. People
    1. Fabian Renn-Giles
        1. [Fielding DSP](https://www.fieldingdsp.com/home)
            1. [Reviver plugin](https://www.fieldingdsp.com/reviver)
        2. [LinkedIn](https://www.linkedin.com/in/fabian-r-8392bb90)
    2. [Tom Poole](https://www.linkedin.com/in/tbpoole/)
    3. [Julian “Jules” Storer](https://www.linkedin.com/in/julian-storer-2412b194/)
    4. [Andre Bergner](https://www.linkedin.com/in/andrebergner/)
    5. [Timur Doumler](https://timur.audio/)
2. Companies & products
    1. MetroWerks’s [CodeWarrior](https://en.wikipedia.org/wiki/CodeWarrior)
    2. [Behringer](https://www.behringer.com/)
    3. [IBM PC](https://en.wikipedia.org/wiki/IBM_Personal_Computer)
    4. LCSI LogoWriter
        1. [Manual on Internet Archive](https://archive.org/details/logowriterteachersmanual)
    5. [iZotope](https://www.izotope.com/)
    6. [Syng](https://syngspace.com/)
    7. [PACE](https://paceap.com/)
    8. [Tracktion](https://www.tracktion.com/)
3. Universities
    1. [Heidelberg University](https://www.uni-heidelberg.de/en)
    2. [Imperial College London](https://www.imperial.ac.uk/)
4. Programming languages
    1. C++
        1. [JUCE framework](https://juce.com/)
            1. [Forum](https://forum.juce.com/)
            2. [Multibus API](https://forum.juce.com/t/multibus-api/18491)
    2. Python
    3. [SOUL](https://soul.dev/)
    4. Swift
    5. Rust
    6. Java
    7. HTML
    8. JavaScript
    9. Lua (integrates well with C++, very simple)
5. Plugin formats
    1. AU
    2. VST
    3. AAX
6. Software Engineering Concepts
    1. Model-View-Presenter (MVP) pattern
    2. Test-driven development (TDD)
7. Software
    1. [Crill project by Timur and Fabian](https://github.com/crill-dev/crill)
    2. [WebKit](https://webkit.org/)
    3. Digital Audio Workstations
        1. Logic (currently Logic Pro)
        2. [Ardour](https://ardour.org/)
        3. [Digital Performer](https://motu.com/en-us/products/software/dp/)
8. IDEs
    1. eMacs
    2. Visual Studio Code
9. Conference talks
    1. Real-Time 101 from ADC 2019 by Fabian and Dave
        1. [Part 1](https://youtu.be/Q0vrQFyAdWI?si=ppAemJP-O7118OZZ)
        2. [Part 2](https://youtu.be/PoZAo2Vikbo?si=gJHqlga6_br-8uSS)
    2. [Audio playback synchronization from ADC 2021 by Fabian](https://www.youtube.com/watch?v=8jHLusUVa2Y&ab_channel=ADC-AudioDeveloperConference)
    3. [Real-time sins & confessions in C++ from ADC 2023 by Fabian](https://www.youtube.com/watch?v=JG7lqt7V1uY&ab_channel=ADC-AudioDeveloperConference)
    4. [Linux Audio API (ALSA) from The Audio Programmer Meetup by Fabian](https://youtu.be/-wDVPreDNjE?si=MoT2hxIcQGDK7Oya)
    5. [Herb Sutter’s talk on a garbage collector from CppCon](https://youtu.be/JfmTagWcqoE?si=G1x2ztWVyucKPet1)
    6. [Clang performance annotations talk from CppCon by Ofek Shilon](https://www.youtube.com/watch?v=qmEsx4MbKoc&ab_channel=CppCon)
10. Resources for learning audio programming
    1. [ADC mentorship program](https://audio.dev/mentorship/)
    2. [Fabian’s JUCE forum post on vectorization](https://forum.juce.com/t/simdregister-is-it-worth-it/53362/4)
    3. [ChatGPT](https://chatgpt.com/)

Thank you for listening! 🙏

**Who should I invite next? Let me know in the comments below!**
