---
title: "Audio Developers Conference 2022 Highlights"
description: "My personal summary and top picks from the Audio Developers Conference 2022 in London."
date: 2022-12-14
author: Jan Wilczek
layout: post
images: /assets/img/posts/programming-in-general/2022-12-14-adc22-highlights/
background: /assets/img/posts/programming-in-general/2022-12-14-adc22-highlights/ADC22-Logo..webp
permalink: /audio-developers-conference-2022-highlights/
categories:
  - Programming in general
tags:
  - effects
  - testing
  - C++
  - JUCE
  - career
  - learning
  - deep learning
  - hardware
discussion_id: 2022-12-14-adc22-highlights
custom_js:
 - /assets/vendor/lazyload/lazyload.min.js
 - /assets/js/wolfsound/modules/load_lazyload.js
---
My personal summary of ADC 22 in London!

<iframe width="560" height="315" src="https://www.youtube.com/embed/Aeq5Egj6TW0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

{% capture _ %}{% increment figureId202211214  %}{% endcapture %}

From November 13 to November 16 2022, I took part in the Audio Developers Conference 2022 in London. My talk proposal was accepted in a voting round, which granted me the conference ticket and the company I'm working at, [Loudly](https://www.loudly.com), sponsored the in-person trip and the workshop ticket.

<div markdown="0">
<img class="lazyload" data-src="{{ images | absolute_url | append: "ADC22-Logo..webp" }}" alt="ADC22 Conference logo.">
</div>
_Figure {% increment figureId202211214  %}. Audio Developers Conference 2022 logo._

From what I understood, there were 1052 attendees of which around 700 were present online and around 300 attended in person. There were 93 talk submissions, out of which around half was voted in.

The event was an incredible experience. All talks will be published on YouTube at the beginning of 2023 but to give you a short summary or a heads-up on what to look out for, I have prepared a list of my personal favorites from the conference.

Yes, this is not a comprehensive summary of the conference (which would be rather boring and unmanageable to read, IMO) but a list of my "top picks" that is completely subjective and entirely non-exhaustive.

These are the highlights of ADC 2022 as seen by an audio C++ developer:

### Table of Contents

1. [Eliminating Undefined Behavior From C++ Code](#eliminating-undefined-behavior-from-c-code)
2. [Efficient Pseudorandom Number Generation](#efficient-pseudorandom-number-generation)
3. [Audio Code Unit Testing](#audio-code-unit-testing)
4. [RNBO in Max from Cycling '74](#rnbo-in-max-from-cycling-74)
5. [How to Optimize a Real-Time Audio Library](#how-to-optimize-a-real-time-audio-library)
6. [Details on MIDI 2.0 from the MIDI Association, Microsoft, Google, and Apple](#details-on-midi-20-from-the-midi-association-microsoft-google-and-apple)
7. [Accessibility](#accessibility)
8. [How to Secure Your Plugin Against Cracking?](#how-to-secure-your-plugin-against-cracking)
9. [Stefano D'Angelo's talk](#stefano-dangelos-talk)
10. [Cmajor Language Announcement](#cmajor-language-announcement)
11. [Vox Synth from Supertone](#vox-synth-from-supertone)
12. [Elk Audio Operating System](#elk-audio-operating-system)
13. [How to Run Your Trained Neural Networks in a Plugin?](#how-to-run-your-trained-neural-networks-in-a-plugin)
14. [Jumpstart Guide to Deep Learning in Audio for Absolute Beginners](#jumpstart-guide-to-deep-learning-in-audio-for-absolute-beginners)
15. [Biggest Personal Highlight](#biggest-personal-highlight)

## Eliminating Undefined Behavior From C++ Code

<div markdown="0">
<img class="lazyload article-img" data-src="{{ images | absolute_url | append: "RussellMcClellan..webp" }}" alt="Russell McClellan.">
</div>
_Figure {% increment figureId202211214  %}. Russell McClellan._

This talk was given by Russell McClellan from Soundwide and is my personal favorite of all the talks. Mostly thanks to its illustrative and insightful examples.

If you don't know what undefined behavior or UB is in C++, it is basically everything in code that the standard or the implementations don't define. Every C++ program that contains undefined behavior is malformed.

The worst part is that undefined behavior may cause trouble but doesn't have to. What's more, it's more likely to cause trouble in a release build but not in a debug build, which happens to be the build programmers spend most time with.

Russell presented a number of options how to combat UB. Out of these, here are my favorite:

1. Have a good compiler and pay attention to its warnings. Optionally, enable "treat warnings as errors".
2. Use the clang-tidy program.
3. Use address sanitizers and undefined behavior sanitizers.
4. Ensure that your plugin does not break the plugin contract using, for example, the [pluginval tool by Tracktion](https://github.com/Tracktion/pluginval).

The CppCon 2022 version of this talk was given by Roth Michaels and can be found on YouTube [here](https://youtu.be/vEtGtphI3lc).

<script defer src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6611455743195468"
     crossorigin="anonymous"></script><ins class="adsbygoogle"
     style="display:block; text-align:center;"
     data-ad-layout="in-article"
     data-ad-format="fluid"
     data-ad-client="ca-pub-6611455743195468"
     data-ad-slot="7289385396"></ins><script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>

## Efficient Pseudorandom Number Generation

<div markdown="0">
<img class="lazyload article-img" data-src="{{ images | absolute_url | append: "RothMichaels..webp" }}" alt="Roth Michaels.">
</div>
_Figure {% increment figureId202211214  %}. Roth Michaels._

Another great C++-related talk was given by a colleague of Russell from iZotope (Soundwide), Roth Michaels.

Similarly, it had also been previously [given at CppCon 2022.](https://youtu.be/I5UY3yb0128)

The topic of Roth's talk was efficient random number generation in C++ for real-time audio purposes. This assumes that we don't care about cryptographic security of the random numbers but simply want the user to feel that some part of sound processing is random. At the same time, we have to be able to strictly control the degree of randomness for the repeatability of results and guarantee real-time safety.

All of these requirements can be fulfilled by using the [Xoroshiro128+ pseudorandom number generator](https://en.wikipedia.org/wiki/Xoroshiro128%2B). This generator is real-time safe and faster than other compared approaches.

## Audio Code Unit Testing

<div markdown="0">
<img class="lazyload article-img" data-src="{{ images | absolute_url | append: "EsaJaaskela.webp" }}" alt="Esa Jääskelä.">
</div>
_Figure {% increment figureId202211214  %}. Esa Jääskelä._

An interesting talk was given by Esa Jääskelä, who advocated for testing your digital signal processing code. I am a big believer in unit and integration testing, thus, I was very happy to listen to his ideas and evangelism on this topic.

Example: to test a high-pass filter, you can use the FFT and programmatically check if the energy in the low band decreased at the output of the filter. You may go as detailed or as coarse as you wish with this but it's already a step toward test-driven development in audio software.

He also showed the usefulness of the [Pamplejuce template](https://github.com/sudara/pamplejuce), which I have been using actively since his talk.

## RNBO in Max from Cycling '74

<div markdown="0">
<img class="lazyload" data-src="{{ images | absolute_url | append: "rnbo-intro.webp" }}" alt="RNBO.">
</div>
_Figure {% increment figureId202211214  %}. RNBO._

This major announcement from Cycling '74 could be a real game-changer in the long run.

[RNBO](https://rnbo.cycling74.com/) is a technology within Max that allows you to generate C++ plugin code, WebAssembly modules, or Raspberry Pi programs from Max patches.

Since Max is so ubiquitous, I am curious to see if the release of RNBO results in an abundance of plugins being released that use it.

I took part in the workshop on RNBO and the generated code compiled under Windows as well 🙂 It was also great to meet one of the people behind the project, Sam Tarakajian.

<div markdown="0">
<img class="lazyload article-img" data-src="{{ images | absolute_url | append: "SamTarakajian.webp" }}" alt="Sam Tarakajian.">
</div>
_Figure {% increment figureId202211214  %}. Sam Tarakajian._

The only caveat of RNBO is that you need a dedicated license for it. But for people using Max, this should come as no surprise.

## How to Optimize a Real-Time Audio Library

<div markdown="0">
<img class="lazyload article-img" data-src="{{ images | absolute_url | append: "DavidRowland.webp" }}" alt="David Rowland.">
</div>
_Figure {% increment figureId202211214  %}. David Rowland._

A great talk from David Rowland, the CTO of [Tracktion](https://www.tracktion.com/), in which he showed a complete guide to optimizing audio code on a rather high level including everything from performance measurement to automated reporting to regression benchmarks (ones that send you an email once a performance dropped in a specific area of code).

Not only did it instruct how to speed up your code but also showed a nice way to think about benchmarking as a form of unit testing. If your software gets slower in benchmarks, it may mean that some unnecessary code was checked into the codebase.

However, it wasn't a talk discussing low-level optimizations, like loop unrolling or assembly excerpts.

## Details on MIDI 2.0 from the MIDI Association, Microsoft, Google, and Apple

<div markdown="0">
<img class="lazyload" data-src="{{ images | absolute_url | append: "MIDI2.0Logo.webp" }}" alt="MIDI 2.0 Logo.">
</div>
_Figure {% increment figureId202211214  %}. MIDI 2.0 Logo._

MIDI 2.0 is slowly introduced to all major operating systems (OSs). Representatives of the MIDI Association presented the current state of the standard and representatives of the Windows, Mac/iOS, and Android teams discussed the changes to their APIs.

A great new feature of MIDI 2.0 is the "MIDI device discovery," which lets you query around for available MIDI 2.0 devices you could talk to.

It will still take time to implement this standard in full on all OSs but it's coming.

For me personally, it was great to hear that the MIDI 2.0 standard is extensible, i.e., (hopefully) future-proof.

## Accessibility

<div markdown="0">
<img class="lazyload" data-src="{{ images | absolute_url | append: "SoundWithoutSightLogoBlack.webp" }}" alt="Sound Without Sight Logo." width="60%">
</div>
_Figure {% increment figureId202211214  %}. Sound Without Sight Logo._

It was amazing to learn how differently abled musicians closely collaborate with companies on product development. A lot in this area is done by [Jason Dasent](https://www.jasondasentinstudio.com/) and the [Sound Without Sight](https://soundwithoutsight.org/) organization.

It was of great value to me because I finally saw how accessible audio software looks in practice.

## How to Secure Your Plugin Against Cracking?

A very insightful talk by Chase Kanipe on how hackers crack plugin licenses and how you could prevent it from happening to your software.

I found it fascinating to see how crackers can inspect your binary code and be able to bypass or override your license checks.

## Stefano D'Angelo's talk

<div markdown="0">
<img class="lazyload article-img" data-src="{{ images | absolute_url | append: "BrickworksLogo.svg" }}" alt="Brickworks Logo.">
</div>
_Figure {% increment figureId202211214  %}. Brickworks Logo._

This talk gave a nice overview of the whole audio programming business and the technologies involved. In a rather streamlined way, Stefano managed to capture the current state of digital signal processing engineering industry and the challenges the DSP engineers must face.

Interestingly, to help push things in the right direction, he proposed a code library with digital signal processing "building blocks" called [Brickworks](https://www.orastron.com/brickworks).

## Cmajor Language Announcement

<div markdown="0">
<img class="lazyload" data-src="{{ images | absolute_url | append: "CmajorLogo.webp" }}" alt="Cmajor Logo.">
</div>
_Figure {% increment figureId202211214  %}. Cmajor Logo._

A major announcement came from [SoundStacks](https://www.soundwide.com/en/sound-stacks.html) (which is a part of SoundWide): [the Cmajor language for audio-specific software.](https://cmajor.dev/)

One of the creators of this language is [Julian Storer](https://uk.linkedin.com/in/julian-storer-2412b194), the creator of [the JUCE framework.](https://github.com/juce-framework/JUCE)

Cmajor is a new language specifically for audio DSP.

It's main features are:

1. Easy installation in Visual Studio Code.
2. Just-in-time compilation or "hot reload" of code inside a running plugin, which should speed up the development immensely.
3. Allegedly, very good performance; I don't know, I haven't tested it yet.
4. A possibility to include a web interface.
5. Transpiling the code to a JUCE C++ framework project.

These points make the language very exciting but the question remains on how this technology will develop. Call me skeptical but I simply hate libraries or frameworks turning deprecated 😉

What's your opinion on this? Have you tried out the language already?

## Vox Synth from Supertone

Attendees of ADC 2022 could see and listen to incredible voice transfer demos of the [Supertone](https://www.youtube.com/channel/UCA-f3J0XX0Rdj8bSfgq0N5g) company. Their software allows you to

1. imitate someone's voice from just a few dozen seconds of recording or even
2. change entire spoken sequences in post-production.

Since it's an Asia-based company, it's hard to find something about them in the English-language side of the Internet… You need to wait for ADC22 videos to go live at the beginning of 2023 to find out more about the project 😉

## Elk Audio Operating System

<div markdown="0">
<img class="lazyload" data-src="{{ images | absolute_url | append: "ElkLogo.svg" }}" alt="Elk Logo.">
</div>
_Figure {% increment figureId202211214  %}. Elk Logo._

This technology by [Elk Audio](https://www.elk.audio/) allows you to control remote audio software in real time (for example, running on an embedded device) without a loss in performance.

You are able to control the parameters of your embedded plugin, for example, with an auto-generated remote graphical user interface (GUI).

I took a part in Elk's workshop and I must admit that Elk Audio OS is a very handy approach to developing embedded or headless audio software. After consulting projects in the area of embedded software, I know what a pain lack of remote control (a terminal, a GUI) can be.

Additionally, the Elk Audio team is awesome!

## How to Run Your Trained Neural Networks in a Plugin?

[Neutone](https://neutone.space/) by Qosmo, Inc. is a technology allowing you to rather easily deploy trained neural networks in audio plugins. Unfortunately, Mac-only for now, it allows you to transfer your Pytorch neural network models to run inside a real-time audio plugin.

I am looking forward to a Windows version of this software that allows researchers quickly validate their models on "live" audio.

It was also great to talk to [Andrew Fyfe](https://www.linkedin.com/in/andrewfyfe93/) and [Christopher Mitcheltree](https://www.linkedin.com/in/christhetree/) who actively develop the software!

<script defer src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6611455743195468"
     crossorigin="anonymous"></script><ins class="adsbygoogle"
     style="display:block; text-align:center;"
     data-ad-layout="in-article"
     data-ad-format="fluid"
     data-ad-client="ca-pub-6611455743195468"
     data-ad-slot="7289385396"></ins><script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>

## Jumpstart Guide to Deep Learning in Audio for Absolute Beginners

a.k.a. my talk…

<div markdown="0">
<img class="lazyload" data-src="{{ images | absolute_url | append: "JumpstartGuideToDeepLearningInAudioTitleSlide.webp" }}" alt="Title slide of my presentation.">
</div>
_Figure {% increment figureId202211214  %}. Title slide of my presentation._

I would like to mention here my talk not because of its quality (that's not for me to judge) but because I was honored (and surprised, to be honest) to be able to speak at the Audio Developers Conference 2022.

The goal of my talk was to show that deep learning in audio is not reserved for universities or research departments of big audio companies. On the contrary, the resources and tools to start with deep learning in audio are readily available online for free. I tried to present a step-by-step approach that you can take to learn deep learning even when you've never done anything similar before.

The talk went well, even the live coding part. I was happy to receive positive feedback after the talk, which resulted in a few interesting conversations. However, I would also like to hear some criticism 😉 That may happen after the video recording of my talk gets published on YouTube.

Until then, [the slides and the code are available on GitHub.](https://github.com/JanWilczek/adc22)

## Biggest Personal Highlight

The conference was nice and all but there's one thing that will stay in my memory for sure…

It's YOU.

<div markdown="0">
<img class="lazyload" data-src="{{ images | absolute_url | append: "ADC22-Thank-You.webp" }}" alt="ADC22 thank you banner.">
</div>
_Figure {% increment figureId202211214  %}._

Thanks to all of you who walked up to me to say "hi" or "thank you for your tutorials." I really appreciate every gesture like this and I hope to continue to serve you in the field of audio programming education in 2023 to the best of my ability.

Speaking of which…

If you haven't yet retrieved my free Audio Plugin Developer Checklist, you can do so [here]({% link collections.all, 'single-pages/checklist.html' %}). It will show you which bits and pieces of knowledge are needed to… attend Audio Developers Conference one day 😉

Thanks a lot to the organizers, the sponsors, and the attendees of the Audio Developers Conference 2022; I hope to see everyone next year...

Thanks for reading and take care!
