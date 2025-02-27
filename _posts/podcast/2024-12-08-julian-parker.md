---
title: "Generating AI Music with Julian Parker (Stability AI, ex-TikTok, ex-Native Instruments) | WolfTalk #025"
description: "Highly inspiring WolfTalk podcast interview with an absurdly productive and successful audio programmer"
date: 2024-12-08
author: Jan Wilczek
layout: post
permalink: /talk025/
background: /assets/img/posts/podcast/talk025/Thumbnail.webp
categories:
  - Podcast
tags:
  - cpp
  - juce
  - career
  - learning
  - plugin
  - deep learning
  - effects
  - filtering
  - hardware
  - research
  - simd
  - virtual analog
  - python
  - maths
  - audio generation
discussion_id: 2024-12-08-julian-parker
---
Learn behind-the-scenes of the most famous audio companies!

{% include 'redcircle-podcast-player', redcircle_podcast_id: '52e4f3d7-8ba8-442d-b5a6-b561c4caecc7' %}

## Listen on

* 🎧 [Spotify](https://open.spotify.com/episode/4hkitf7wiIcfIZsViF0v2L?si=nhQdjkNCSlCneiI9m8b0fQ)
* 🎥 [YouTube](https://youtu.be/NLVM7oiUGMs?si=l-ZTWRbZukltdhD1)
* 🎧 [Apple Podcasts (iTunes)](https://podcasts.apple.com/pl/podcast/generating-ai-music-with-julian-parker-stability-ai-ex/id1595913701?i=1000679632584)
* 🎧 [TuneIn Radio](http://tun.in/tDYcSk)

[All podcast episodes.](/podcast)

[Sign up for WolfSound's newsletter!]({% link collections.all, 'newsletter.md' %})

## Introduction

When I was doing my master’s at the University of Erlangen-Nürnberg, I was eager to learn the internals of the audio programming industry. My supervisor and mentor back then, Maximilian Schäfer, PhD, introduced me to **Julian Parker**, PhD, who was working at Native Instruments (NI) in Berlin at the time (this was before Native Instruments merged with iZotope and a few other audio brands).

Thanks to Julian, I learned the behind-the-scenes of the audio plugin development scene in a few eye-to-eye conversations, which we are happy to summarize publicly in a podcast episode!

Julian’s career is incredible: from natural sciences through a master’s in physical modeling, a PhD in virtual analog modeling, an almost decade-long position at Native Instruments, all the way to TikTok and Stability AI, where he’s working now on generative music algorithms.

There are few people who have such a rich background in audio research and industry and even fewer who are willing to share the details of it publicly. That makes this episode all the more exciting!

{% include 'podcast_cta' %}

## Episode contents

From this podcast, you will learn:

- how machine learning forever changed audio plugin design and development
- how big audio plugin companies operate internally
- how to learn C++ for audio programming
- whether you need to have a PhD to work in an R&D department of an audio company
- what is the state of the art in generative music
- how to learn generating music with AI
- how to be able to focus on research papers even if you read them after hours
- how to produce quality research
- how to rest & recharge after intense and focused work

This episode was recorded on June 26, 2024.

## Julian’s Tips & Observations For Successful DSP Research & Development

1. Best ideas often come in the moments outside of work (during a walk, a shower, etc.).
2. Published research is a sign of competence.
3. Neural networks are like digital signal processing blocks.
4. To create novel research, learn all the existing approaches and think about what you can do better.
5. All of Julian’s favorite works are the ones published for free.
6. People like demo videos.
7. If you want to learn generative AI, go out there and start playing with open-source and open-weight models like LLaMA or Stable Audio Open. Run inference, tweak.
8. C++ is still important for DSP & fast ML inference (low-level, high-performance programming).
9. Try to maximize the day-to-day joy from what you’re doing.
10. If you teach something, you need to learn it very deeply (which is a modus operandi of this blog, by the way).
11. Focus in research comes from interest.
12. If you work on something hard, focus on your work for a short time and relax completely afterward.
13. Writing DSP is a great way to learn a programming language.
14. Steps in VIrtual Analog modeling:
    1. Maths
    2. Coding
    3. Tuning
    4. Optimization

## References

1. People
    1. Julian D. Parker
        1. [MSc thesis on spring reverberation [PDF]](https://www.pure.ed.ac.uk/ws/portalfiles/portal/12456049/Spring_Reverbation_A_Physical_Perspective.pdf)
        2. [PhD thesis on dispersive systems](https://aaltodoc.aalto.fi/items/5b1ff7ca-c56a-4073-9471-06846271625f)
        3. [LinkedIn](https://www.linkedin.com/in/julian-parker-28a49313/)
        4. [Harmonai Discord](https://www.harmonai.org/)
    2. [Stefan Bilbao](https://www.acoustics.ed.ac.uk/people/dr-stefan-bilbao/)
    3. [Vesa Välimäki](https://www.aalto.fi/en/people/vesa-valimaki)
    4. [Julius O. Smith](https://ccrma.stanford.edu/~jos/)
    5. [Lauri Savioja](https://research.aalto.fi/en/persons/lauri-savioja)
    6. [Jonathan Abel](https://ccrma.stanford.edu/people/jonathan-abel)
    7. [Sebastian Schlecht](https://www.sebastianjiroschlecht.com/)
    8. [Mati Karjalainen](https://en.wikipedia.org/wiki/Matti_Antero_Karjalainen)
    9. [Till Bovermann](https://www.linkedin.com/in/tillbovermann/)
    10. [Manfred Schroeder](https://en.wikipedia.org/wiki/Manfred_R._Schroeder)
    11. [Egbert Juergens](https://www.linkedin.com/in/egbertjuergens/)
    12. [Steinunn Arnardottir](https://www.linkedin.com/in/steinunn-arnardottir/)
    13. [Colin Raffael](https://colinraffel.com/) (a co-author of T5 text embedding model)
    14. [Fabian Esqueda](https://www.linkedin.com/in/fabian-esqueda-ba3750157/)
    15. [Hans-Joachim "Eddie" Mond](https://www.linkedin.com/in/hans-joachim-eddie-mond-8525b9265/)
    16. [Ed Newton-Rex](https://ed.newtonrex.com/)
    17. [Lykon: a Twitter user training his image generation model with stable diffusion](https://x.com/Lykon4072)
    18. [AK on Hugging Face](https://huggingface.co/akhaliq)
    19. Music artists
        1. AphexTwin
        2. [Warp Records](https://en.wikipedia.org/wiki/Warp_Records)
        3. [TJ Herz (objekt)](https://soundcloud.com/static_cast)
2. Places
    1. University of Cambridge
        1. [Natural Sciences undergraduate course](https://www.undergraduate.study.cam.ac.uk/courses/natural-sciences-ba-hons-msci)
    2. University of Edinburgh
        1. [MSc in Acoustics and Music Technology](https://postgraduate.degrees.ed.ac.uk/?r=site/view&edition=2025&id=478)
        2. [MSc in Sound Design](https://www.eca.ed.ac.uk/programme/sound-design-msc)
        3. [MMus in Composition](https://www.eca.ed.ac.uk/programme/composition-mmus)
    3. [Aalto University (Acoustics Lab)](https://www.aalto.fi/en/aalto-acoustics-lab)
    4. Native Instruments
    5. Yamaha
    6. KORG
    7. Tik-Tok (ByteDance)
    8. Jukedeck led by Ed Newton-Rex (see above), bought out by Tik-Tok
    9. [Lexicon](https://www.lexicon.com/)
    10. [Alesis](https://www.alesis.com/)
    11. Google
    12. [Stability AI](https://stability.ai/)
    13. [Freesound.org](https://freesound.org/)
    14. SONY
    15. [arxiv.org](https://arxiv.org/)
    16. Meta
    17. GitHub
    18. [Digital Audio FX (DAFX) conference](https://www.dafx.de/)
    19. [Hugging Face](https://huggingface.co/)
3. DSP concepts
    1. [FM Synthesis](https://en.wikipedia.org/wiki/Frequency_modulation_synthesis){:target="_blank"}
    2. [Virtual Analog (VA)](https://en.wikipedia.org/wiki/Analog_modeling_synthesizer){:target="_blank"}
    3. finite difference scheme
    4. [allpass filter](https://www.youtube.com/watch?v=AKMoKWYGe8I&t=1s){:target="_blank"}
    5. dynamic range compression
    6. dispersive systems: different frequencies travel in them at different speeds
    7. Music Information Retrieval (MIR)
    8. analytical signal (Hilbert transform) using a filterbank
    9. reverb
        1. Feedback Delay Network
    10. symbolic music generation
    11. audio generation
    12. AI music generation
    13. style transfer
    14. Machine Learning
    15. [SIMD](https://thewolfsound.com/simd-in-dsp/)
4. Hardware
    1. ZX Spectrum
    2. [Yamaha SG](https://www.guitarguitar.co.uk/news/141247/)
    3. KORG Prophecy
    4. spring reverb
    5. Buchla filter (see below for a paper)
    6. [Clavia Nord Micro Modular](https://www.vintagesynth.com/clavia/nord-micro-modular)
    7. [monome’s norns platform](https://monome.org/docs/norns/)
    8. From Native Instruments
        1. [Maschine](https://www.native-instruments.com/en/products/maschine/production-systems/maschine/?srsltid=AfmBOor8UwDWATYq_jFEK_g90BsLS5hUDeUq13hZ6VEChVbVUMcIWUsY)
        2. [Traktor](https://www.native-instruments.com/en/catalog/hardware/traktor/)
5. Audio software
    1. [JPverb reverb by Julian](https://faustdoc.grame.fr/examples/reverb/)
        1. [Source code](https://github.com/supercollider/sc3-plugins/blob/main/source/DEINDUGens/JPverbRaw.cpp)
    2. [Greyhole reverb by Julian](https://faustdoc.grame.fr/examples/reverb/)
        1. [Source code](https://github.com/supercollider/sc3-plugins/blob/main/source/DEINDUGens/GreyholeRaw.cpp)
    3. [Realms plugin](https://www.samplelogic.com/products/realms/) 
    4. From Native Instruments
        1. [Reaktor Blocks](https://www.native-instruments.com/en/products/komplete/synths/reaktor-6/blocks/?srsltid=AfmBOoqfV8mJ5cdeSyBsCTFIyh-PfVzKVgTzc8VUqf7y9StNWxvPfYb9)
        2. [Reaktor User Library](https://www.native-instruments.com/en/reaktor-community/reaktor-user-library/)
        3. [Replika XT](https://www.native-instruments.com/en/products/komplete/effects/replika-xt/)
        4. [Mod Pack](https://www.native-instruments.com/en/products/komplete/effects/effects-series-mod-pack/)
        5. [Crush Pack](https://www.native-instruments.com/en/products/komplete/effects/effects-series-crush-pack/)
        6. [Guitar Rig](https://www.native-instruments.com/en/products/komplete/guitar/guitar-rig-7-pro/)
        7. [Traktor](https://www.native-instruments.com/en/catalog/hardware/traktor/)
        8. [Raum reverb plugin](https://www.native-instruments.com/en/products/komplete/effects/raum/)
6. Programming languages
    1. FAUST
    2. Super Collider
    3. C++
    4. Max for Live + Gen or Faust
    5. Python
7. Libraries & frameworks
    1. Eigen C++ library
    2. [**JUCE C++ framework (podcast sponsor ♥️)**](https://juce.com/)
    3. Pytorch
    4. TensorFlow
    5. Keras
    6. [jax from Google](https://github.com/jax-ml/jax)
    7. CUDA
8. Research papers
    1. [Manfred Schroeder’s original reverb paper [PDF]](https://hajim.rochester.edu/ece/sites/zduan/teaching/ece472/reading/Schroeder_1962.pdf)
    2. artificial reverberation review paper: [“Fifty Years of Artificial Reverberation” by Julian D. Parker et. al.](https://ieeexplore.ieee.org/document/6161610)
    3. a follow-up to the above: [“More Than 50 Years of Artificial Reverberation” by Vesa Välimäki et. al.](https://www.researchgate.net/publication/296415959_More_Than_50_Years_of_Artificial_Reverberation)
    4. “A digital model for the Buchla lowpass-gate” by Julian D. Parker and [Stefano D’Angelo](https://thewolfsound.com/talk009/) [[PDF](https://dafx.de/paper-archive/2013/papers/44.dafx2013_submission_56.pdf)]
    5. [Diff-a-Riff paper from SONY](https://sonycslparis.github.io/diffariff-companion/)
    6. [Stemgen paper by Julian D. Parker et. al.](https://arxiv.org/abs/2312.08723)
9. Image generation models
    1. DALL-E
    2. [Stable Diffusion](https://en.wikipedia.org/wiki/Stable_Diffusion)
    3. [Mistral](https://mistral.ai/)
    4. [LLaMA](https://www.llama.com/)
10. Music generation models
    1. [MusicLM](https://musiclm.com/)
    2. [Stable Audio 2.0](https://stability.ai/news/stable-audio-2-0)
    3. [Stable Audio Open (trained on CC-0- and CC-BY-licensed music)](https://stability.ai/stable-audio)
    4. [Stable Audio Tools](https://github.com/Stability-AI/stable-audio-tools)

Thank you for listening!
