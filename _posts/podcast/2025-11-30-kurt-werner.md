---
title: "Wave Digital Filter with Kurt Werner (Soundtoys, ex-Native Instruments, ex-iZotope)"
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

{% include 'redcircle-podcast-player', redcircle_podcast_id: '__________' %}

## Listen on

* 🎧 [Spotify]()
* 🎥 [YouTube]()
* 🎧 [Apple Podcasts]()
* 🎧 [TuneIn Radio]()

[All podcast episodes.](/podcast)

[Sign up for WolfSound's newsletter!]({% link collections.all, 'newsletter.md' %})

## Introduction

Dr. Kurt James Werner is a senior research scientist at Soundtoys, a former researcher at iZotope, and one of the most influential figures in modern Virtual Analog modeling. His research areas include Wave Digital Filters (WDFs), nonlinear circuit analysis, reverb design, and the mathematical foundations that make today’s plugins sound the way they do.

Kurt’s path into audio is unusual and inspiring. From early experiments with saxophone and GarageBand, to circuit bending Casio keyboards, and pursuing two bachelor’s degrees at UIUC: one in Industrial Engineering and one in Music Composition. His academic journey eventually led him to Stanford’s legendary CCRMA, where under the guidance of Julius O. Smith, he helped modernize the WDF framework and remove long-standing limitations that prevented realistic modeling of complex analog circuits.

In this episode, we explore Kurt’s transition from academia to industry, his work on products at iZotope and Soundtoys, and the realities of being a research scientist inside an audio plugin company. What does the day-to-day look like? How does research feed into shipping products? And what role does a PhD play in shaping an audio DSP career?

This conversation is a blend of practical engineering insights, deep DSP theory, and candid career reflection, and is a must-listen for anyone interested in audio DSP, virtual analog modeling, circuit simulation, or the technology behind modern sound design tools.

{% include 'podcast_cta' %}



## Episode Contents

### From this episode, you will learn:

1.	How Kurt’s early musical and DIY electronics experiments led him toward audio DSP.
2.	What studying Industrial Engineering and Music Composition at UIUC taught him about sound, systems, and creativity.
3.	How the CCRMA environment shaped his research, from psychoacoustics to DSP with Julius O. Smith.
4.	A clear, high-level explanation of Wave Digital Filters, their origins, and why they matter in virtual analog modeling.
5.	Kurt’s contributions to modern WDFs, including topology handling, SPQR decomposition, and R-type adaptors.
6.	How these methods enable accurate modeling of real-world circuits, including iconic drum machines and analog hardware.
7.	Insights from his work at iZotope, including reverb design, DAC modeling, distortion research, and product integration.
8.	His current work at Soundtoys, contributing to products like SuperPlate and exploring long-horizon research in a small team.
9.	How creative hacking practices like circuit bending and 1-bit music inform his DSP thinking.
10.	Kurt’s advice for building a research or engineering career in audio, including the role of a PhD and how to stay productive.


### Tips & Advice
1. Real DSP efficiency is not determined by counting multipliers, because actual performance depends on memory access, platform behaviour, and algorithm structure, so you must measure real throughput rather than theoretical cost.
2. Becoming an audio research scientist requires demonstrated research ability, usually through a PhD or a publication-heavy Master’s, because companies expect proof that you can navigate the full research process.
3. A PhD is not required for DSP engineering roles, and practical C++, debugging ability, and hands-on product development experience are often more valuable than academic credentials.
4. Strong research writing comes from deep reading, and understanding the full history of a topic is essential for producing meaningful papers and effective related-work sections.
5. When modeling nonlinear circuits you must warm up the system before audio begins, and WDFs are most efficient for reactive circuits but perform poorly on large resistive networks.
6. Audio careers often move between academia and industry, and attending conferences like DAFx plays an important role in staying connected to the research community.

This episode was recorded on __________

## References

### People

#### Kurt Werner
* [CCRMA - Dr. Kurt James Werner](https://ccrma.stanford.edu/~kwerner/)
* [Bandcamp - Kurt James Werner](https://kurtjameswerner.bandcamp.com)

#### Academia & Research
* [Julius O. Smith III](https://ccrma.stanford.edu/~jos/)
* [Jonathan Abel](https://music.stanford.edu/people/jonathan-abel)
* [Alfred Fettweis](https://ethw.org/Oral-History:Alfred_Fettweis)
* [Maximilian Schäfer](https://max-schaefer.org)
* [Scott Wyatt](https://scottawyatt.com)
* [Paul Stapleton](https://www.paulstapleton.net/portfolio/about-me)
* [Victor Zappi](https://toomuchidle.com)
* [Jatin Chowdhury](https://ccrma.stanford.edu/~jatin/about.html)
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
* [Julian Parker](https://www.linkedin.com/in/julian-parker-28a49313/)
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

#### Classic Hardware
* [Roland TR-808](https://www.roland.com/us/products/rc_tr-808/)
* [Roland TR-505](https://support.roland.com/hc/en-us/articles/201940129-TR-505-Technical-Specifications)
* [Casio SK-1](https://en.wikipedia.org/wiki/Casio_SK-1)
* [Hammond Organ (Vibrato/Chorus)](https://en.wikipedia.org/wiki/Hammond_organ)
* [Altec 9062A (Graphic EQ)](https://gearspace.com/board/reviews/925123-altec-9062a-passive-graphic-equalizer.html#:~:text=It%20is%20a%20very%20simple,2%2Dbuss%20cannot%20be%20overstated.)
* [RCA Mark II](https://en.wikipedia.org/wiki/RCA_Mark_II_Sound_Synthesizer)
* [E-mu SP-1200](https://en.wikipedia.org/wiki/E-mu_SP-1200)
* Tascam Digital Four-Track Recorder

#### Retro / Chiptune   
* [NES - Nintendo Entertainment System](https://en.wikipedia.org/wiki/Nintendo_Entertainment_System)
* [GameBoy](https://en.wikipedia.org/wiki/Game_Boy)
* [ZX Spectrum](https://en.wikipedia.org/wiki/ZX_Spectrum)
* [Atari Punk Console](https://adamgulyas.ca/projects/APC.html#:~:text=Background,was%20probably%20thinking%20of%20phreaking.)
* [Music tracker](https://en.wikipedia.org/wiki/Music_tracker)
* Dancing Hamster Toy
* Casio Keyboards (circuit-bent)

### Software, Frameworks & Tools
* [JUCE](https://juce.com)
* [Max/MSP](https://cycling74.com/products/max) & Gen~
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
* [Chowdhury-DSP/chowdsp_wdf](https://github.com/Chowdhury-DSP/chowdsp_wdf)
* [droosenb/faust-wdf-library](https://github.com/droosenb/faust-wdf-library)
* [gusanthon/pywdf](https://github.com/gusanthon/pywdf)

### Books
* [Physical Audio Signal Processing — Julius O. Smith](https://ccrma.stanford.edu/~jos/pasp/)
* [Tuning, Timbre, Spectrum, Scale — William Sethares](https://link.springer.com/book/10.1007/b138848)
* [Bits and Pieces: A History of Chiptunes — Kenneth McAlpine](https://www.amazon.co.uk/Bits-Pieces-Chiptunes-Kenneth-McAlpine-ebook/dp/B07HCF4ZDX)
* [Circuit-Bending: Build Your Own Alien Instruments — Reed Ghazala](https://archive.org/details/CircuitBendingBuildYourOwnAlienInstruments)
* [DAFx: Digital Audio Effects](https://dafx.de/DAFX_Book_Page/index.html)

### Academic Papers & Theses
* Werner, K. J. (2016). Virtual analog modeling of audio circuitry using wave digital filters (Doctoral dissertation, Stanford University). [[PDF] stanford.edu](https://stacks.stanford.edu/file/druid:jy057cz8322/KurtJamesWernerDissertation-augmented.pdf)
* Werner, K. J., & Burtlington, V. T. (2024). GRAPHIC EQUALIZERS BASED ON LIMITED ACTION NETWORKS. [[PDF] dafx.de](https://dafx.de/paper-archive/2024/papers/DAFx24_paper_83.pdf)
* Werner, K. J., Abel, J., & Smith, J. (2014, September). A physically-informed, circuit-bendable, digital model of the Roland TR-808 bass drum circuit. [[PDF] qub.ac.uk](https://pureadmin.qub.ac.uk/ws/portalfiles/portal/124500900/dafx14_kurt_james_werner_a_physically_informed_ci.pdf)
* Werner, K. J. (2019, September). Generalizations of velvet noise and their use in 1-bit music. [[PDF] dafx.de](https://www.dafx.de/paper-archive/2019/DAFx2019_paper_53.pdf)
* Franken, D., Ochs, J., & Ochs, K. (2005). Generation of wave digital structures for networks containing multiport elements. [https://doi.org/10.1109/TCSI.2004.843056](https://doi.org/10.1109/TCSI.2004.843056)

### Events, Journals, Conferences

* [DAFx — Digital Audio Effects Conference](https://www.dafx.de)
* [NIME — New Interfaces for Musical Expression](https://nime.org)
* [Computer Music Journal](https://direct.mit.edu/comj)
* [Sound On Sound – Synth Secrets series](https://www.soundonsound.com/series/synth-secrets-sound-sound)

### Concepts & Technologies

* Wave Digital Filters (WDFs)
* SPQR Tree Decomposition
* R-Type Adapters
* Modified Nodal Analysis (MNA)
* State-Space Modeling
* Port-Hamiltonian Systems
* N-Extra Element Theorem (Middlebrook)
* Newton Solvers
* Delay-Free Loop Handling
* 1-bit Audio
* Pulse Width Modulation (PWM)
* Velvet Noise
* Impulse Trains
* Hard Sync
* Deep Learning for Virtual Analog
* Startup Transients in WDF
* R2R DAC
* Passive EQs
* Operational Amplifiers (Op-Amps)
* Voltage Dividers
* Chebyshev Filters
* Biquad Filters
* Digital Logic Chips
