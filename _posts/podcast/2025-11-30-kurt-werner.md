---
title: "Wave Digital Filters with Kurt Werner (Soundtoys, ex-Native Instruments, ex-iZotope) | WolfTalk #030"
description: "Kurt explains Wave Digital Filters, nonlinear circuit modeling, and the research behind some of the most popular audio plugins."
date: 2025-11-30T07
author: Jan Wilczek & Sathira Tennakoon
layout: post
permalink: /talk030/
background: /assets/img/posts/podcast/talk030/Thumbnail.webp
categories:
  - Podcast
tags:
  - filtering
  - maths
  - fourier
  - transform
  - matlab
  - juce
  - career
  - learning
  - research
  - reverb
  - virtual analog
  - amplifiers
  - plugin
  - cpp
  - cmajor
discussion_id: 2025-11-30-kurt-werner
---
Learn the secrets of RX, Ozone, Neoverb, Vinyl, and more!

{% include 'redcircle-podcast-player', redcircle_podcast_id: '0bfe72a5-ba48-498c-b4df-306cbb11877e' %}

## Listen on

* 🎧 [Spotify](https://open.spotify.com/episode/0jwvKlpWfPeJVjwBtJHW3e?si=b0LuF7qHR4yyVYWrRAFIZQ)
* 🎥 [YouTube](https://youtu.be/ZMbnvEWT6nY)
* 🎧 [Apple Podcasts](https://podcasts.apple.com/us/podcast/wave-digital-filters-with-kurt-werner-soundtoys-ex/id1595913701?i=1000738980955)
* 🎧 [TuneIn Radio](http://tun.in/tI8FdG)

[All podcast episodes.](/podcast)

[Sign up for WolfSound's newsletter!]({% link collections.all, 'newsletter.md' %})

## Introduction

Kurt James Werner, PhD, is a senior research scientist at Soundtoys and one of my favorite researchers in audio DSP (virtual analog modeling in particular).

While you may not have read his papers, it's very likely that you used one of the plugins he worked on:
- Neoverb
- Vinyl
- RX
- Guitar Rig (Hammond vibrato/chorus)
- Ozone
- Neutron
- Trash

If you start peeking into the research of modeling analog audio effects in plugins, you stumble across his name right away.

I consider him not only brilliant, but also insanely productive. Definitely a role model for me!

In the research world, he's mostly known for his work on **Wave Digital Filters (WDFs)**. It's a technique for creating a mathematical model of an analog circuit that once done is easy to implement (provided you use a WDF library).

WDFs are great for modeling analog audio effects to put them inside plugins.

But as a true researcher, Kurt is involved many other audio subfields that we discuss in the podcast!

Did I mention that he's a graduate from Stanford's CCRMA?

In this episode, you'll learn about Kurt’s transition from academia to industry, his work on products at iZotope, Native Instruments, and Soundtoys, and the realities of being a research scientist in an audio plugin company.

You'll also learn all about WDFs, which is a powerful tool to master.

Trust me, you don't want to miss this one 😉

{% include 'podcast_cta' %}

## Episode Contents

From this episode, you will learn:

1. How Kurt’s early musical and DIY electronics experiments led him toward audio DSP
1. How was it like to study at CCRMA under Julius Smith, Jonathan Abel, and Ge Wang
4. A clear, high-level explanation of Wave Digital Filters, their origins, and why they matter in virtual analog modeling
7. Insights from his work at iZotope
8. His current work at Soundtoys
9. Creative music practices like circuit bending and 1-bit music
1. Whether you need a PhD to work at an audio plugin company
1. How audio research translates into plugins

### Tips & Advice

1. A DSP algorithm's performance is not determined by counting adds and multiplies (as often done in research papers); you need a proper benchmark
2. Getting a research position in the audio industry requires demonstarting research ability through
    1. a PhD (or a very good Master’s thesis),
    1. written papers
    1. published papers
3. A PhD is not required for DSP engineering roles; for these, practical C++ experience is often more valuable
1. To write good papers, you need to read a lot of other papers, understand them, and critically analyze them; "You need to read all the papers" 😉
1. In your WDF models, consider that the circuit must warm up before proper audio samples processing can start; slamming a battery (even a virtual one) into a circuit will always produce a sharp transient!
6. Attending conferences like DAFX is important not only for being up-to-date with the latest research, but also for career prospects

This episode was recorded on February 25, 2025.

## References

### People

#### Kurt Werner

* [CCRMA - Dr. Kurt James Werner](https://ccrma.stanford.edu/~kwerner/)
* [Bandcamp - Kurt James Werner](https://kurtjameswerner.bandcamp.com)

#### Academia & Research

* [Julius O. Smith III](https://ccrma.stanford.edu/~jos/)
* [Jonathan Abel](https://music.stanford.edu/people/jonathan-abel)
* [Alfred Fettweis](https://ethw.org/Oral-History:Alfred_Fettweis)
* [Maximilian Schäfer](https://www.maximilianschaefer.org/)
* [Scott Wyatt](https://scottawyatt.com)
* [Paul Stapleton](https://www.paulstapleton.net/portfolio/about-me)
* [Victor Zappi](/talk029)
* [Jatin Chowdhury](/talk024)
* [Maximilian Rest](https://ccrma.stanford.edu/people/maximilian-rest)
* [David Yeh](https://ccrma.stanford.edu/~dtyeh/)
* [Stefano D’Angelo](https://www.linkedin.com/in/stefanodangeloaudio/)
* [Vesa Välimäki](https://www.linkedin.com/in/vesavalimaki/)
* [Matti Karjalainen](https://en.wikipedia.org/wiki/Matti_Antero_Karjalainen)
* [Augusto Sarti](https://sarti.faculty.polimi.it/Augusto_Sarti/CV_and_publications.html)
* [Alberto Bernardini](https://www.deib.polimi.it/eng/people/details/936408)
* [Sebastian Schlecht](https://www.sebastianjiroschlecht.com)

#### Industry and Creative Figures

* [Ken Bogdanowicz](https://www.linkedin.com/in/ken-bogdanowicz-b092476/)
* [Chris Santoro](https://www.linkedin.com/in/chris-santoro-9773059/)
* [Pete Edwards](https://www.instagram.com/casperelectronics/)
* [Russell McClellan](https://www.linkedin.com/in/russell-mcclellan-20ba9854/)
* [Andy Saroff](https://www.linkedin.com/in/sarroff/)
* [Shahan Nercessian](https://www.linkedin.com/in/shahan-nercessian-84960b100/)
* [Alexey Lukin](https://www.linkedin.com/in/alexey-lukin-7b4915b0/)
* [François Germain](https://www.linkedin.com/in/francoisggermain/)
* [John Bailey](https://www.linkedin.com/in/jonathangbailey/)
* [Fabian Esqueda ](https://www.linkedin.com/in/fabian-esqueda-ba3750157/)
* [Julian Storer](https://www.linkedin.com/in/julian-storer/)
* [Julian Parker](/talk025)
* [Reed Ghazala](http://www.anti-theory.com/bio/)
* [Tristan Perich](https://www.tristanperich.com)

### Educational & Research Institutes

* [CCRMA – Stanford University](https://ccrma.stanford.edu)
* [Stanford Laptop Orchestra (SLOrk)](https://slork.stanford.edu)
* [SARC – Queen’s University Belfast](https://www.qub.ac.uk/research-centres/sarc/)
* [UIUC – University of Illinois Urbana-Champaign](https://illinois.edu)
* [EMS (Experimental Music Studios) – UIUC](https://music.illinois.edu/about-us/facilities/experimental-music-studios/)
* [FAU Erlangen–Nürnberg](https://www.fau.eu)
* [University of Michigan](https://umich.edu)
* [Aalto University – Finland](https://www.aalto.fi/en)
    - [Acoustics Lab](https://www.aalto.fi/en/aalto-acoustics-lab)
* [Politecnico di Milano – Italy](https://www.polimi.it)
* [MIT – Massachusetts Institute of Technology](https://www.mit.edu)
* [Tufts University](https://www.tufts.edu)
* [WPI – Worcester Polytechnic Institute](https://www.wpi.edu)
* [CAMD - Northeastern University](https://camd.northeastern.edu)
* [Bangor University – Wales](https://www.bangor.ac.uk)
* [Curry College](https://www.curry.edu)
* [Stockhausen Studio for Electronic Music (WDR)](https://en.wikipedia.org/wiki/Studio_for_Electronic_Music_(WDR))
* [SEAMUS – Society for Electro-Acoustic Music in the US](https://seamusonline.org)

### Companies & Products

* [iZotope](https://www.izotope.com)
    * [Neoverb](https://www.izotope.com/en/products/neoverb)
    * [RX](https://www.izotope.com/en/products/rx)
    * [Ozone](https://www.izotope.com/en/products/ozone)
    * [Neutron](https://www.izotope.com/en/products/neutron)
    * [Trash](https://www.izotope.com/en/products/trash)
    * [Vinyl](https://www.izotope.com/en/products/vinyl)
        * [Interview with Russell McClellan and Kurt Werner on Vinyl R2R DAC modeling](https://www.izotope.com/en/learn/lo-fi-a-hip-hop-story)
* [Native Instruments](https://www.native-instruments.com)
    * [Guitar Rig](https://www.native-instruments.com/en/products/komplete/guitar/guitar-rig-7-pro/)
* [Soundtoys](https://www.soundtoys.com)
    * [Superplate](https://www.soundtoys.com/product/superplate/)
* [SoundStacks](https://cmajor.dev)
* [Exponential Audio](https://sonicscoop.com/inside-the-acquisition-why-izotope-set-its-sights-on-exponential-audio/#:~:text=It%20seems%20relatively%20rare%20in,brain%20trust%20are%20all%20covered.)
* [Brainworx](https://www.brainworx.audio)
* [Plugin Alliance](https://www.plugin-alliance.com/)
* [Apple Garage Band](https://www.apple.com/mac/garageband/)
* [PlayStation MTV Music Generator](https://en.wikipedia.org/wiki/Music_2000)

### Hardware & Gear

#### Classic audio hardware

* [Roland TR-808](https://en.wikipedia.org/wiki/Roland_TR-808)
* [Roland TR-505](https://en.wikipedia.org/wiki/Roland_TR-505)
* [Casio SK-1](https://en.wikipedia.org/wiki/Casio_SK-1)
* Altec 9062A (Graphic EQ)
* [RCA Mark II](https://en.wikipedia.org/wiki/RCA_Mark_II_Sound_Synthesizer)
* [E-mu SP-1200](https://en.wikipedia.org/wiki/E-mu_SP-1200)
* Tascam Digital Four-Track Recorder
* [Atari Punk Console](https://adamgulyas.ca/projects/APC.html#:~:text=Background,was%20probably%20thinking%20of%20phreaking.)

#### Retro platforms

* [NES - Nintendo Entertainment System](https://en.wikipedia.org/wiki/Nintendo_Entertainment_System)
* [GameBoy](https://en.wikipedia.org/wiki/Game_Boy)
* [ZX Spectrum](https://en.wikipedia.org/wiki/ZX_Spectrum)

### Software, Frameworks & Tools

* [JUCE](https://juce.com)
* [Max/MSP](https://cycling74.com/products/max) & Gen
* [Max for Live](https://www.ableton.com/en/live/max-for-live/)
* [ChucK](https://chuck.stanford.edu)
* [LTSpice](https://www.analog.com/en/resources/design-tools-and-calculators/ltspice-simulator.html)
* [MATLAB](https://www.mathworks.com/products/matlab.html)
* [OWL Platform](https://www.openwarelab.org)
* [LaTeX](https://en.wikipedia.org/wiki/LaTeX)
* [TikZ](https://tikz.dev)
* [C++](https://en.wikipedia.org/wiki/C%2B%2B)
* [Octave](https://octave.org)
* [Python](https://www.python.org)

#### WDF libraries

* [Chowdhury-DSP/chowdsp_wdf](https://github.com/Chowdhury-DSP/chowdsp_wdf)
* [droosenb/faust-wdf-library](https://github.com/droosenb/faust-wdf-library)
* [gusanthon/pywdf](https://github.com/gusanthon/pywdf)

### Books

* [Physical Audio Signal Processing — Julius O. Smith](https://ccrma.stanford.edu/~jos/pasp/)
* [Tuning, Timbre, Spectrum, Scale — William Sethares](https://link.springer.com/book/10.1007/b138848)
* [Bits and Pieces: A History of Chiptunes — Kenneth McAlpine](https://www.amazon.co.uk/Bits-Pieces-Chiptunes-Kenneth-McAlpine-ebook/dp/B07HCF4ZDX)
* [Circuit-Bending: Build Your Own Alien Instruments — Reed Ghazala](https://archive.org/details/CircuitBendingBuildYourOwnAlienInstruments)
* [DAFX: Digital Audio Effects](https://dafx.de/DAFX_Book_Page_2nd_edition/index.html)

### Academic Papers & Theses

* Werner, K. J. (2016). Virtual analog modeling of audio circuitry using wave digital filters (Doctoral dissertation, Stanford University). [[PDF] stanford.edu](https://stacks.stanford.edu/file/druid:jy057cz8322/KurtJamesWernerDissertation-augmented.pdf)
* Werner, K. J., & Burtlington, V. T. (2024). Graphic equalizers based on limited action networks. [[PDF] dafx.de](https://dafx.de/paper-archive/2024/papers/DAFx24_paper_83.pdf)
* Werner, K. J., Abel, J., & Smith, J. (2014, September). A physically-informed, circuit-bendable, digital model of the Roland TR-808 bass drum circuit. [[PDF] qub.ac.uk](https://pureadmin.qub.ac.uk/ws/portalfiles/portal/124500900/dafx14_kurt_james_werner_a_physically_informed_ci.pdf)
* Werner, K. J. (2019). Generalizations of velvet noise and their use in 1-bit music. [[PDF] dafx.de](https://www.dafx.de/paper-archive/2019/DAFx2019_paper_53.pdf)
* Fettweis, A. (1986), Wave Digital Filters: Theory and Practice [[PDF] CCRMA](https://ccrma.stanford.edu/~jingjiez/portfolio/gtr-amp-sim/pdfs/Wave%20Digital%20Filters%20Theory%20and%20Practice.pdf)
* Franken, D., Ochs, J., & Ochs, K. (2005). Generation of wave digital structures for networks containing multiport elements. [[PDF] IEEE Xplore]](https://doi.org/10.1109/TCSI.2004.843056)

### Conferences & Journals

* [DAFX — Digital Audio Effects Conference](https://www.dafx.de)
* [NIME — New Interfaces for Musical Expression](https://nime.org)
* [Computer Music Journal](https://direct.mit.edu/comj)
* [Sound On Sound – Synth Secrets series](https://www.soundonsound.com/series/synth-secrets-sound-sound)

### Research/technical concepts

* Wave Digital Filters (WDFs)
* SPQR tree decomposition
* R-Type adapters
* Modified Nodal Analysis (MNA)
* state-space modeling
* Port-Hamiltonian modeling
* N-Extra Element Theorem (R. D. Middlebrook)
* Newton solvers
* delay-free loop handling
* 1-bit audio
* Pulse Width Modulation (PWM)
* velvet noise
* impulse trains
* hard sync
* deep learning
* virtual analog modeling
* R2R DAC
* passive EQs
* operational amplifiers (op-amps)
* voltage dividers
* Chebyshev filters
* biquad filters

