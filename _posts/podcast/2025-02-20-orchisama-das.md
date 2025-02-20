---
title: "Reverb, Spatial & Immersive Audio with Orchisama Das | WolfTalk #026"
description: "Podcast interview with an audio researcher from CCRMA, Meta, Tesla, Uni Surrey, Sonos & King's College"
date: 2025-02-20
author: Sathira Tennakoon
layout: post
permalink: /talk026/
background: /assets/img/posts/podcast/talk026/Thumbnail.webp
categories:
  - Podcast
tags:
  - effects
  - python
  - convolution
  - filtering
  - impulse
  - matlab
  - juce
  - career
  - learning
  - research
  - reverb
  - deep learning
  - java
  - virtual reality
  - spatial audio
  - acoustics
  - plugin
discussion_id: 2025-02-20-orchisama-das
---
Recreating room acoustics using feedback delay networks, scattering delay networks, and more!

{% include 'redcircle-podcast-player', redcircle_podcast_id: '6584fddd-d8b9-4f60-81bc-16f92a77fc80' %}

## Listen on

* 🎧 [Spotify](https://open.spotify.com/episode/2GeSXmtBopJcSFcedfsJ1v?si=bAGMkXK6SbGXVdbWQVCyMA)
* 🎥 [YouTube](https://youtu.be/UaWuxYKQhu8?si=hmsMc45rEF1-4omI)
* 🎧 [Apple Podcasts (iTunes) (TBA)](#)
* 🎧 [TuneIn Radio (TBA)](#)

[All podcast episodes.](/podcast)

[Sign up for WolfSound's newsletter!]({% link collections.all, 'newsletter.md' %})

## Introduction

Orchisama Das is an outstanding audio researcher known for her work in virtual acoustics, artificial reverberation, and immersive audio. She holds a PhD from Stanford University’s prestigious CCRMA and has contributed to groundbreaking research at leading universities and major tech companies.

During this interview, we talk about her path in academia and industry. Orchisama shares her thoughts about the realities of audio research, offering great insights and a very frank and honest perspective on her journey.

We dive into technical topics such as artificial reverberation, virtual acoustics, immersive audio, and open problems in DSP, as well as topics like the gender imbalance in the audio research industry and how to stay productive and motivated during research.

The episode is scattered with many resources and tips for anyone interested in learning the mentioned topics. It is a very inspiring and informative talk for people who are doing audio research, or curious about getting started.

{% include 'podcast_cta' %}

## Episode contents

From this podcast, you will learn:

- How Orchisama Das started her journey in audio research and her path to earning a PhD at Stanford University’s CCRMA.
- About her internships at Tesla and Meta Reality Labs, as well as tips and advice on how to get internships as a researcher.
- A big picture technical overview of artificial reverberation, virtual room acoustics, and immersive audio.
- Resources for learning about these topics, including books, papers, and tools.
- Tips and advice for a good research carrer.
- Her thoughts on the gender imbalance in audio research and ways to address it.

This episode was recorded on November 21, 2024.

## Topics Mentioned

1. Methods for simulating room acoustics (artificial reverberation)
   1. Geometric methods
      1. Image-Source Method
      2. Ray tracing
   2. Parametric networks (recursive filters)
      1. Feedback Delay Network
      2. Scattering Delay Network
   3. Wave-based physics solvers
   4. Convolution reverb (measuring impulse responses)
      1. [Partitioned convolution]({% post_url collections.posts, '2021-05-14-fast-convolution' %})
2. Challenges in artificial reverberation
   1. Listener movement (6 degrees of freedom)
   2. Modeling reverb in complex geometries
   3. Real-time implementation
3. Spatial audio
   1. Sound source localization
   2. Binaural rendering
   3. Vector-based amplitude panning (VBAP)
   4. Ambisonics
   5. Soundfield reconstruction
   6. Object-based audio
   7. [Dolby Atmos](https://www.dolby.com/technologies/dolby-atmos/)
4. Audio Industry
   1. Women@Sonos
   2. Inclusivity in immersive audio
   3. The Leaky Pipeline

## References

1. People
    1. Orchisama Das
        1. [CCRMA webpage](https://ccrma.stanford.edu/~orchi/)
        2. [Email](mailto:odas@stanford.edu)
        3. [LinkedIn Profile](https://www.linkedin.com/in/orchisamadas/)
        4. [SoundCloud](https://soundcloud.com/orchisama-das)
    2. CCRMA Faculty
        1. [Julius Smith III](https://ccrma.stanford.edu/~jos/)
        2. [Jonathan Abel](https://ccrma.stanford.edu/people/jonathan-abel)
        3. [Chris Chafe](https://ccrma.stanford.edu/people/chris-chafe)
        4. [Jonathan Berger](https://ccrma.stanford.edu/people/jonathan-berger)
        5. [Ge Wang](https://ccrma.stanford.edu/people/ge-wang)
        6. [Takako Fujioka](https://ccrma.stanford.edu/people/takako-fujioka)
    3. [Leslie Gaston-Bird](https://www.linkedin.com/in/lesliegaston/)
2. Academic Institutions and Programs
    1. [Jadavpur University](https://jadavpuruniversity.in)
    2. [Mitacs Globalink](https://www.mitacs.ca/our-programs/globalink-research-internship-students/)
    3. [University of Calgary](https://www.ucalgary.ca)
        1. [Research on The Ranchlands' Hum](https://calgaryherald.com/news/local-news/researchers-develop-app-to-record-ranchlands-hum)
    4. [Stanford University](https://www.stanford.edu)
        1. [Centre for Computer Research in Music (CCRMA)](https://ccrma.stanford.edu)
    5. [University of Surrey](https://www.surrey.ac.uk)
        1. [Institute of Sound Recording (IoSR)](https://iosr.surrey.ac.uk)
        2. [Tonmeister Program](https://www.surrey.ac.uk/undergraduate/music-and-sound-recording-tonmeister)
    6. [King’s College London](https://www.kcl.ac.uk)
    7. [University of Southampton](https://www.southampton.ac.uk)
    8. [Aalto University](https://www.aalto.fi/en)
        1. [Aalto Acoustics Lab](https://www.aalto.fi/en/aalto-acoustics-lab)
    9. [Technical University Berlin](https://www.tu.berlin)
    10. [IRCAM](https://www.ircam.fr)
3. Companies and Startups
    1. [Tesla](https://www.tesla.com)
        1. Noise, vibration, and harshness (NVH) Engineering
    2. [Meta Reality Labs](https://about.meta.com/realitylabs/)
    3. [Sonos](https://www.sonos.com)
        1. [Sonos Ace Headphones](https://www.sonos.com/en/shop/sonos-ace)
        2. [Sonos Arc Smart Soundbar](https://www.sonos.com/en/shop/arc-black)
    4. [Treble](https://www.treble.tech)
4. Resources
    1. Books
        1. [Physics of Music Instruments](https://link.springer.com/book/10.1007/978-0-387-21603-4)
        2. [Room Acoustics](https://www.routledge.com/Room-Acoustics/Kuttruff-Vorlander/p/book/9781032478258?srsltid=AfmBOoq32MjSfMUMVw73SWFnWipv3xAiWXCQiLAn8IynWiLk81JkfunE)
        3. [Physical Audio Signal Processing](https://ccrma.stanford.edu/~jos/pasp/)
        4. [Mathematics of the Discrete Fourier Transform](https://ccrma.stanford.edu/~jos/st/)
        5. [Introduction to Digital Filters with Audio Applications](https://ccrma.stanford.edu/~jos/filters/)
        6. [Parametric Time-Frequency Domain Spatial Audio](https://onlinelibrary.wiley.com/doi/book/10.1002/9781119252634)
    2. Research Papers
        1. [Orchi's PhD Thesis - Close Microphone Cross-talk Cancellation in Ensemble Recordings with Statistical Estimation](https://ccrma.stanford.edu/~orchi/Documents/odas_thesis_final.pdf)
        2. [Allen & Berkley - Image method for efficiently simulating small‐room acoustics](https://pubs.aip.org/asa/jasa/article-abstract/65/4/943/765693/Image-method-for-efficiently-simulating-small-room?redirectedFrom=fulltext) 
        3. [M. Schroeder - Natural Sounding Artifical Reverberation](https://hajim.rochester.edu/ece/sites/zduan/teaching/ece472/reading/Schroeder_1962.pdf)
        4. [Fifty Years of Artificial Reverberation](https://ieeexplore.ieee.org/document/6161610)
        5. [More Than 50 Years of Artificial Reverberation](https://www.researchgate.net/publication/296415959_More_Than_50_Years_of_Artificial_Reverberation)
    3. Academic Conferences
        1. [IEEE Workshop on Applications of Signal Processing to Audio and Acoustics  (WASPAA)](https://waspaa.com)
        2. [International Conference on Digital Audio Effects (DAFx)](https://www.dafx.de)
    4. Other Resources
        1. [3Blue1Brown Series on Neural Networks](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi)
        2. [Signal Processing Stack Exchange](https://dsp.stackexchange.com)
5. Programming languages
    1. Java
    2. MATLAB
    3. Python
    4. C++
6. Tools used by Orchi
    1. Libraries and Frameworks
        1. [**JUCE C++ framework (podcast sponsor ♥️)**](https://juce.com/)
        2. [PyTorch](https://pytorch.org)
        3. [Jupyter](https://jupyter.org/)
        4. [Pydantic](https://docs.pydantic.dev/latest/) ([YAML](https://yaml.org))
    2. Tools
        1. [Sublime Text](https://www.sublimetext.com)
        2. [Xcode](https://developer.apple.com/xcode/)
        3. [Reaper (DAW)](https://www.reaper.fm)
        4. [Max/MSP](https://cycling74.com/products/max)
        5. [Zotero Reference Manager](https://www.zotero.org)

Thank you for listening!
