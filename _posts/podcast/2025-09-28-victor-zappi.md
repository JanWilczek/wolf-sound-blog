---
title: "Designing Digital Musical Instruments with Victor Zappi | WolfTalk #029"
description: "Podcast interview with Victor Zappi: Assistant Professor of Music Technology at Northeastern University"
date: 2025-09-28
author: Jan Wilczek & Sathira Tennakoon
layout: post
permalink: /talk029/
background: /assets/img/posts/podcast/talk029/Thumbnail.webp
categories:
  - Podcast
tags:
- hardware
- cpp
- research
- career
- learning
- android
- virtual reality
- simd
discussion_id: 2025-09-28-victor-zappi
---

{% include 'redcircle-podcast-player', redcircle_podcast_id: ______________ %}

## Listen on

* 🎧 [Spotify](#)
* 🎥 [YouTube](#)
* 🎧 [Apple Podcasts](#)
* 🎧 [TuneIn Radio](#)

[All podcast episodes.](/podcast)

[Sign up for WolfSound's newsletter!]({% link collections.all, 'newsletter.md' %})

## Introduction

Victor Zappi is a creator, researcher, and educator at the intersection of music, technology, and interaction design. He is currently an Assistant Professor of Music Technology at Northeastern University. In his career, among others, he worked on the Bela hardware platform during his time at Queen Mary University of London's prestigious Centre for Digital Music (C4DM).

I had the pleasure of meeting Victor at the DAFx 2024 conference, where we immediately connected over his paper on running neural networks on Android devices. It turned out he used [my Android wavetable synthesizer tutorial]({% post_url collections.posts, 'synthesis/android-wavetable-synthesizer/2022-08-02-app-architecture' %}) in one of his research experiments (with proper citation, of course 😉).

In this episode, apart from Victor's inspirating career, we focus on digital musical instruments:

* What is a "good" digital musical intrument like?
* Is it a fixed "box" that you should learn how to play?
* Or should it be "abused" by opening "the box," and messing with its internals?
* Can an artist change the digital intrument to make it their own?

We conclude with the discussion of Victor's LDSP C++ framework to enable low-level audio device control on Android devices.

This episode is a must-listen for anyone interested in the future of musical interfaces, hackable hardware, and the technology that drives them!

{% include 'podcast_cta' %}

## Episode Contents

From this episode, you will learn:

* How Victor Zappi's journey led him through several disciplines to reach a unique intersection.
* The story behind creating the Bela platform and its mission to provide ultra-low latency for interactive audio.
* The philosophy of "hackable instruments" and "appropriation" in musical expression, inspired by concepts like John Cage's prepared piano.
* Insights into the LDSP C++ framework for achieving low-level audio device access on rooted Android devices.
* The technology behind the Hyper Drumhead instrument and the potential of GPU-accelerated audio.
* Practical advice for getting started in audio programming, DSP, and academic research.
* An inside look at the NIME (New Interfaces for Musical Expression) community.

This episode was recorded on February 18, 2025.

## References

### People

1. Victor Zappi
   * [Institution Webpage](https://camd.northeastern.edu/people/victor-zappi/)
   * [GitHub](https://github.com/victorzappi)
2. [Andrew McPherson](https://andrewmcpherson.org/bio)
3. [Joshua Reiss](https://www.eecs.qmul.ac.uk/~josh/)

### Universities & Research Labs

1. [Queen Mary University of London (QMUL)](https://www.qmul.ac.uk/)
    * [Centre for Digital Music (C4DM)](https://www.c4dm.eecs.qmul.ac.uk/)
    * [Augmented Instruments Laboratory](https://instrumentslab.org/)
2. [IRCAM](https://www.ircam.fr/)
    * [Sound Music Movement Interaction Team](https://ircam-ismm.github.io/)
3. [University of British Columbia, Canada](https://www.ubc.ca/)
    *  [Marie Skłodowska-Curie Fellowship](https://www.postdocs.ubc.ca/award/marie-sklodowska-curie-actions-postdoctoral-fellowship)
4. [Northeastern University, Boston](https://www.northeastern.edu/)
    * [College of Arts, Media and Design](https://camd.northeastern.edu/)

### Conferences & Communities

1. [DAFx (International Conference on Digital Audio Effects)](https://www.dafx.de/)
2. [Audio Developer Conference (ADC)](https://audio.dev/)
3. [NIME (International Conference on New Interfaces for Musical Expression)](https://nime.org/)
4. [ACM (Association for Computing Machinery)](https://www.acm.org/)
    * [CHI (Conference on Human Factors in Computing Systems)](https://chi2025.acm.org/)
    * [SIGGRAPH](https://www.siggraph.org/)
5. [International Computer Music Association (ICMC Conference)](https://www.computermusic.org/)


### Key Publications by Victor Zappi

1. [Neural Audio Processing on Android Phones (2024)](https://www.dafx.de/paper-archive/2024/papers/DAFx24_paper_78.pdf)
2. [Non-Rigid Musical Interfaces: Exploring Practices, Takes, and Future Perspective (2020)](https://www.nime.org/proceedings/2020/nime2020_paper3.pdf)
3. [Hackable Instruments: Supporting Appropriation and Modification in Digital Musical Interaction (2018)](https://www.frontiersin.org/journals/ict/articles/10.3389/fict.2018.00026/full)
4. [Extended Playing Techniques on an Augmented Virtual Percussion Instrument (2018)](https://ieeexplore.ieee.org/document/8391040)
5. [The Hyper Drumhead: Making Music with a Massive Real-time Physical Model (2017)](https://dblp.org/rec/conf/icmc/ZappiAF17.html)
6. [An Environment for Submillisecond-Latency Audio and Sensor Processing on BeagleBone Black (2015)](https://www.eecs.qmul.ac.uk/~andrewm/mcpherson_aes2015.pdf)

### Books
1. [Audio Effects - Theory, Implementation and Application](https://www.routledge.com/Audio-Effects-Theory-Implementation-and-Application/Reiss-McPherson/p/book/9781466560284)

### Hardware & Platforms

1. [Bela](https://bela.io/)
    * [C++ Real-Time Audio Programming with Bela course on YouTube](https://www.youtube.com/playlist?list=PLCrgFeG6pwQmdbB6l3ehC8oBBZbatVoz3)
2. [BeagleBone Black](https://www.beagleboard.org/boards/beaglebone-black)
3. [Daisy Seed](https://daisy.audio/hardware/Seed/)
4. [Raspberry Pi](https://www.raspberrypi.com/)
5. Serial communication protocols
   * I2S (protocol)
   * SPI (protocol)
6. [The D-Box](https://andrewmcpherson.org/project/dbox)

### Software

1. Audio Programming Languages and Frameworks
   1. [Max/MSP (Cycling '74)](https://cycling74.com)
   2. [Csound](https://csound.com)
   3. [Pure Data (Pd)](https://puredata.info)
   4. [Faust](https://faust.grame.fr)
   5. [LDSP C++ Framework](https://github.com/victorzappi/LDSP)
   6. [JUCE C++ Framework](https://juce.com)
2. OS and Libraries
   1. [LineageOS](https://lineageos.org/)
   2. [ALSA (Advanced Linux Sound Architecture)](https://www.alsa-project.org/wiki/Main_Page)
   3. [TinyALSA (Tiny ALSA Library)](https://github.com/tinyalsa/tinyalsa)
   4. [OpenGL](https://www.opengl.org)
   5. [Xenomai](https://xenomai.org)

3. Digital Audio Workstations (DAWs)
   1. [FL Studio (FruityLoops)](https://www.image-line.com)
   2. [Ableton Live](https://www.ableton.com/en/live/)
   3. [eJay Virtual Music Studio](https://www.ejayshop.com/product/ejay-virtual-music-studio/)

4. Tools for research
   1. [Google Scholar](https://scholar.google.com)
   2. [HuggingFace](https://huggingface.co)
   3. [Kaggle](https://www.kaggle.com)

### Concepts & Technologies

1. Research Fields & Design Paradigms
   1. Human-Computer Interaction (HCI)
   2. Virtual Reality (VR)
   3. Audio First Virtual Reality
   4. Hackable Instruments
   5. Appropriation & Customization

2. Audio & DSP
   1. Real-time DSP
   2. Audio Plugins
   3. Latency & Jitter
   4. Physical Modeling
   5. Wave Equation & Numerical Solvers
   6. Finite-Difference Time-Domain (FDTD) solver
   7. Synthesis Techniques
      1. Articulatory / Vocal Tract Synthesis
      2. Granular Synthesis
      3. FM/AM Synthesis
   8. MIDI

3. Computing
   1. GPU Accelerated Audio & Synthesis
   2. SIMD (Single Instruction, Multiple Data)
      * NEON
   3. Unified Memory Architecture
   4. Neural Networks & Deep Learning
   5. Embedded & Mobile Audio
   6. Rooted Android Devices

4. Social & Philosophical Concepts
   1. Circuit Bending
   2. Right to Repair Movement
   3. Experiential Learning
   4. Open Source
   5. E-waste & Sustainability
   6. Democratization of Digital Musical Instruments

### Artistic & Musical References

1. [John Cage](https://www.johncage.org)
   * Prepared Piano
2. [Devin Townsend](https://hevydevy.com)
3. [Murcof - La Sangre Illuminada (Album)](https://murcofmusic.bandcamp.com/album/la-sangre-iluminada)
