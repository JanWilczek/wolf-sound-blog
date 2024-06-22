---
title: "Top 10 Audio Developer Conference 2023 Talks | ADC23 Summary"
description: "You haven't attended ADC but want to know the most important highlights? Wonder which talks to watch on YouTube? Read this conference summary!"
date: 2024-01-11
author: Jan Wilczek
layout: post
images: /assets/img/posts/programming-in-general/2024-01-11-top-10-audio-developer-conference-2023-talks/
background: /assets/img/posts/programming-in-general/2024-01-11-top-10-audio-developer-conference-2023-talks/Thumbnail.webp
categories:
  - Programming in general
tags:
  - accessibility
  - software architecture
  - learning
  - virtual analog
  - spatial audio
  - rust
  - cpp
  - c
  - deep learning
discussion_id: 2024-01-11-top-10-audio-developer-conference-2023-talks
custom_js:
 - /assets/vendor/lazyload/lazyload.min.js
 - /assets/js/wolfsound/modules/load_lazyload.js
---
Missed the conference? Read this article!

{% capture _ %}{% increment figureId20240111  %}{% endcapture %}

<div markdown="0">
<img class="lazyload" data-src="{{ images | append: "ADC23-banner.webp" }}" alt="Audio Developer Conference 2023 banner" width="50%">
</div>

_Figure {% increment figureId20240111  %}. Audio Developer Conference 2023 banner._

Welcome to a detailed summary of the Audio Developer Conference 2023. I'm Jan Wilczek, and I run the blog and YouTube channel TheWolfSound.com, where I share insights into software development, digital signal processing, and audio programming. This article is your gateway to learning the essence of ADC 2023, especially if you couldn't attend in person.

### Table of Contents

1. [General Vibe of the Conference](#general-vibe-of-the-conference)
2. [Workshops at the Audio Developer Conference](#workshops-at-the-audio-developer-conference)
   1. [Rust Workshop: Joe Noël, Nico Chatzigianis, James Hallowell](#rust-workshop-joe-noel-nico-chatzigianis-james-hallowell)
   2. [Accessibility panel led by Jay Pocknell \& Harry Morley](#accessibility-panel-led-by-jay-pocknell-and-harry-morley)
3. [Top 10 Talks at ADC 2023](#top-10-talks-at-adc-2023)
   1. [Developing an AI-powered karaoke experience by Thomas Hézard \& Clément Tabary](#developing-an-ai-powered-karaoke-experience-by-thomas-hezard-and-clement-tabary)
   2. [Creating ubiquitous, composable, performant DSP modules by Stefano D'Angelo](#creating-ubiquitous-composable-performant-dsp-modules-by-stefano-d-angelo)
   3. [An Introduction to CLAP, a new plug-in standard by Alexandre Bique](#an-introduction-to-clap-a-new-plug-in-standard-by-alexandre-bique)
   4. [Exploration of strongly-typed units: a case-study from digital audio by Roth Michaels](#exploration-of-strongly-typed-units-a-case-study-from-digital-audio-by-roth-michaels)
   5. [RADSan: a realtime-safety sanitizer by David Trevelyan \& Ali Barker](#rad-san-a-realtime-safety-sanitizer-by-david-trevelyan-and-ali-barker)
   6. [Writing elegant DSP code with Rust by Chase Kanipe](#writing-elegant-dsp-code-with-rust-by-chase-kanipe)
   7. [Lessons learned from implementing a real-time multichannel audio application on Linux by Olivier Petit](#lessons-learned-from-implementing-a-real-time-multichannel-audio-application-on-linux-by-olivier-petit)
   8. [The architecture of digital audio workstations (and other time-based media software) by Ilias Bergström](#the-architecture-of-digital-audio-workstations-and-other-time-based-media-software-by-ilias-bergstroem)
   9. [A more intuitive approach to optimising audio DSP code – Guiding the compiler through optimising your code for you by Gustav Andersson](#a-more-intuitive-approach-to-optimising-audio-dsp-code-guiding-the-compiler-through-optimising-your-code-for-you-by-gustav-andersson)
   10. [Real-time confessions: the most common “sins” in real-time code by Fabian Renn-Giles](#real-time-confessions-the-most-common-sins-in-real-time-code-by-fabian-renn-giles)
4. [Surprise mention](#surprise-mention)
5. [Summary](#summary)

{% render 'google-ad.liquid' %}

## General Vibe of the Conference

This year's conference was marked by a significant focus on **Artificial Intelligence** in audio development. There was a noticeable increase in software engineering talks, reflecting the evolving landscape of audio programming. The event was intensely packed with sessions, providing an enriching but exhaustive experience. Personally, it was exhilarating to meet many of my DSP Pro online course students and be recognized by the community.

## Workshops at the Audio Developer Conference

Before diving into the top talks of the ADC, it's worth highlighting the workshops that prefaced the conference. The workshops are an integral part of ADC, offering hands-on experiences in various audio development aspects.

### Rust Workshop: Joe Noël, Nico Chatzigianis, James Hallowell

<div markdown="0">
<img class="lazyload" data-src="{{ images | append: "Joe Noel.webp" }}" width="50%">
</div>

_Figure {% increment figureId20240111  %}. Joe Noël._

<div markdown="0">
<img class="lazyload" data-src="{{ images | append: "Nico Chatzigianis.webp" }}" width="50%">
</div>

_Figure {% increment figureId20240111  %}. Nico Chatzigianis._

<div markdown="0">
<img class="lazyload" data-src="{{ images | append: "James Hallowell.webp" }}" width="50%">
</div>

_Figure {% increment figureId20240111  %}. James Hallowell._

The first workshop I attended was about integrating C++ audio code into Rust, a language that's increasingly popular among developers. This workshop, led by Joe Noël, Nico Chatzigianis, and James Hallowell from Focusrite, was an eye-opener. It was a practical, step-by-step guide on writing applications in Rust that interact with C++ code. The experience was very fun and, most importantly, very educative. I even shared my results on LinkedIn, proud of the progress and the knowledge gained.

If you want to learn more about Rust for audio programming, definitely listen to the [16th episode of the WolfTalk podcast]({% link collections.all, '2024-01-04-ian-hobson.md' %}), where I interviewed Ian Hobson, a great proponent of Rust!

### Accessibility panel led by Jay Pocknell & Harry Morley

<div markdown="0">
<img class="lazyload" data-src="{{ images | append: "Jay Pocknell.webp" }}" width="50%">
</div>

_Figure {% increment figureId20240111  %}. Jay Pocknell._

<div markdown="0">
<img class="lazyload" data-src="{{ images | append: "Harry Morley.webp" }}" width="50%">
</div>

_Figure {% increment figureId20240111  %}. Harry Morley._

The next workshop that caught my attention was the accessibility panel organized by Jay Pocknell, founder of the Sound Without Sight organization. This workshop brought together up to ten experts discussing the various aspects of creating accessible audio software. It included a powerful presentation by Harry Morley from Focusrite, demonstrating the difference between accessible and non-accessible apps. The discussions were incredibly informative, shedding light on the importance and methods of making audio software accessible to all users.

I was lucky to interview Jay for in the [13th episode of the WolfTalk podcast]({% link collections.all, '2023-06-19-jay-pocknell.md' %}): if you haven't listened to it, I highly encourage you to do so!

These workshops were not just informative but also inspirational, offering fresh perspectives on audio software development. They provided practical knowledge and demonstrated the conference's commitment to addressing both technical and inclusive aspects of audio development. For those interested in the detailed nuances of audio software, these workshops were a treasure trove of knowledge.

## Top 10 Talks at ADC 2023

Before jumping into the crux of the top 10 talks at the Audio Developer Conference, let me share a couple of disclaimers.

First, despite having access to the recordings, time constraints prevented me from watching every single talk. So, I might have missed some hidden gems.

Second, the talks I found most engaging and insightful are based on my personal experience and perspective as an audio developer deeply involved in mobile apps, audio plugins, and teaching audio programming. My tools of the trade are primarily C++ and Python, so my views are shaped through this lens. Remember, there's a vast array of talks catering to diverse interests, and what resonates with me might differ from your areas of interest or expertise.

That said, the top 10 talks I'm about to share were, in my opinion, the standouts of the conference, each for its unique contribution to the field of audio development. Whether it was groundbreaking new technology, innovative techniques, or inspiring insights, these talks represent the cutting edge of audio development. So, let's dive in and explore the highlights and key takeaways from each of these illuminating presentations.

### Developing an AI-powered karaoke experience by Thomas Hézard & Clément Tabary

<div markdown="0">
<img class="lazyload" data-src="{{ images | append: "Thomas Hézard.webp" }}" width="50%">
</div>

_Figure {% increment figureId20240111  %}. Thomas Hézard._

<div markdown="0">
<img class="lazyload" data-src="{{ images | append: "Clément Tabary.webp" }}" width="50%">
</div>

_Figure {% increment figureId20240111  %}. Clément Tabary._

Alright, so the number 10 talk was about creating an AI-powered karaoke app, led by Thomas Hézard and Clément Tabary from MWM. They walked us through how they built this karaoke application, which was pretty cool. What I found great about their presentation was how they highlighted every single problem they bumped into and the ways they tackled them. It was like a real-world case study in problem-solving with AI in audio. It's quite surprising that they managed to solve almost every problem with deep learning. If you’re into how deep learning meshes with audio, especially in practical, in-market apps, this talk is definitely worth your time.

### Creating ubiquitous, composable, performant DSP modules by Stefano D'Angelo

<div markdown="0">
<img class="lazyload" data-src="{{ images | append: "Stefano D'Angelo.webp" }}" width="50%">
</div>

_Figure {% increment figureId20240111  %}. Stefano D'Angelo._

Now, the number 9 talk that grabbed my attention was by Stefano D'Angelo. He's the brain behind Orastron and their DSP components library, Brickworks. This wasn't just a showcase of their library, though. Stefano provided a comprehensive view on building composable and efficient DSP modules. It was like a deep dive into the nuts and bolts of digital signal processing, and how you can make your DSP code not just good, but top-notch in terms of stability and performance. If you're looking to get your hands dirty with real-deal DSP implementation, Stefano's insights are gold. Plus, checking out the Brickworks library could give you some solid leads on how to shape your own DSP code.

### An Introduction to CLAP, a new plug-in standard by Alexandre Bique

<div markdown="0">
<img class="lazyload" data-src="{{ images | append: "Alexandre Bique.webp" }}" width="50%">
</div>

_Figure {% increment figureId20240111  %}. Alexandre Bique._

The eighth talk, which I managed to catch, was Alexander Bique's introduction to a new plugin standard called CLAP. This topic intrigued me – why do we need another plugin standard? As it turns out, CLAP addresses several non-obvious issues. It's a free standard, which is quite a rarity, and it clearly defines the responsibilities of both the plugin and the host. This clarity is essential because, often, plugins are developed according to a format, but hosts might violate the format requirements, leading to compatibility issues.

CLAP also employs a C-based API, meaning it's versatile across platforms. I'm keen to see how it evolves, particularly with potential support from the JUCE team (currently there are only [CLAP extensions for JUCE](https://github.com/free-audio/clap-juce-extensions)). For anyone in the plugin development space, this is a talk that's bound to pique your interest.

### Exploration of strongly-typed units: a case-study from digital audio by Roth Michaels

<div markdown="0">
<img class="lazyload" data-src="{{ images | append: "Roth Michaels.webp" }}" width="50%">
</div>

_Figure {% increment figureId20240111  %}. Roth Michaels._

Number seven on my list was a must-see for me – Roth Michaels' talk. Roth tackled a common issue in C++ coding, the 'primitive obsession', where everything is passed around as floats, doubles, or integers. This can become a major headache, especially in larger codebases.

What I found particularly enlightening was Roth's approach to this problem using pre-written libraries for a more generalized solution, moving away from primitive data types to more explicit, strongly typed units. This not only improves the quality of the code but also its readability and reliability. Adding to the intrigue was the library discussed by Roth, developed by Mateusz Pusz, a prominent figure in the C++ community. As a fellow Polish, it's always great to see such recognition in the programming and audio world. For anyone coding in C++, especially in digital audio, Roth's talk provides a valuable insight.

### RADSan: a realtime-safety sanitizer by David Trevelyan & Ali Barker

<div markdown="0">
<img class="lazyload" data-src="{{ images | append: "David Trevelyan.webp" }}" width="50%">
</div>

_Figure {% increment figureId20240111  %}. David Trevelyan._

At number six was the intriguing talk on "RADSan: A Real-Time Safety Sanitizer" by David Trevelyan and Ali Barker. A sanitizer is a tool in the compilation process that adds extra code to report possible faults of the implementation. AddressSanitizer and UndefinedBehaviorSanitizer, shipped with the Clang compiler, are prime examples of such tools, detecting memory errors and undefined behaviors respectively.

But RADSan? It's a new player in the game, focusing on ensuring real-time code doesn't violate its runtime guarantees. Since audio plugins process sound on a real-time thread, audio code can only perform actions that are guaranteed to complete in a fixed time period. This means avoiding allocations, system calls, and locks. RADSan envelops your audio code in additional layers to check its behavior, a crucial step if you're incorporating third-party libraries or uncertain code. The talk was widely regarded as a breakthrough, and I'm eager to see how RADSan evolves and gets adopted in audio development circles.

### Writing elegant DSP code with Rust by Chase Kanipe

<div markdown="0">
<img class="lazyload" data-src="{{ images | append: "Chase Kanipe.webp" }}" width="50%">
</div>

_Figure {% increment figureId20240111  %}. Chase Kanipe._

Landing at number five was Chase Kanipe's talk on "Writing Elegant DSP Code with Rust." I had the pleasure of watching Chase's presentation last year on license checking, which was nothing short of impressive. This year, he shifted his focus to Rust for DSP coding — a topic I couldn't miss. However, the experience was marred by technical hiccups during the remote session, with poor video quality and small font sizes rendering the code unreadable on screen. It was disappointing to see attendees, including myself, having to leave due to these issues.

Despite these setbacks, I later watched the talk on my computer and it was thoroughly enlightening. Chase presented how Rust's type system can be leveraged to provide a generic and abstract interface for an audio processing chain. I'm also excited about the possibility of hosting Chase on the Wolf Talk podcast, so stay tuned for that!

### Lessons learned from implementing a real-time multichannel audio application on Linux by Olivier Petit

<div markdown="0">
<img class="lazyload" data-src="{{ images | append: "Olivier Petit.webp" }}" width="50%">
</div>

_Figure {% increment figureId20240111  %}. Olivier Petit._

Ranked fourth in my list of top talks at the conference was Olivier Petit's presentation on "Lessons Learned from Implementing a Real Time Multi Channel Audio Application on Linux." This session was a real gem for anyone interested in the practicalities of audio development, especially in a Linux environment. Olivier methodically outlined the challenges encountered when building real-time audio applications on Linux and shared step-by-step solutions.

What stood out to me in this talk was the practical advice on using system traces — a common recommendation that often lacks detailed guidance. Olivier's hands-on approach not only made the concept clear but also demonstrated its application in real-world scenarios. A lot of impact was put on ensuring that the audio thread is scheduled even if the CPU is occupied with a lot of other tasks such as networking.

### The architecture of digital audio workstations (and other time-based media software) by Ilias Bergström

<div markdown="0">
<img class="lazyload" data-src="{{ images | append: "Ilias Bergström.webp" }}" width="50%">
</div>

_Figure {% increment figureId20240111  %}. Ilias Bergström._

Securing the third spot on my list was a fascinating talk by Ilias Bergström from Elk Audio, focusing on "The Architecture of Digital Audio Workstations and Other Time-Based Media Software." Ilias, with his profound experience at Elk Audio, shared the architecture of two digital audio workstations he's worked on. This talk was a deep dive into the intricacies of audio software design, an area that’s not often discussed in detail.

What makes this talk stand out is its focus on design and architectural choices in audio software development. For anyone curious about the internal workings of digital audio workstations or looking to structure their audio applications efficiently, Ilias's insights are invaluable. I highly recommend this talk to those interested in audio software design, as it offers a rare glimpse into the complex world of digital audio workstations.

### A more intuitive approach to optimising audio DSP code – Guiding the compiler through optimising your code for you by Gustav Andersson

[Video](https://youtu.be/HdyiQLQCvfs?si=0Yi26KVDWurYweUf)

<div markdown="0">
<img class="lazyload" data-src="{{ images | append: "Gustav Andersson.webp" }}" width="50%">
</div>

_Figure {% increment figureId20240111  %}. Gustav Andersson._

Coming in at number two on my top talks list was Gustav Andersson's "A More Intuitive Approach to Optimizing Audio DSP Code." Gustav, a developer at Elk Audio, presented a highly approachable talk on optimizing DSP (Digital Signal Processing) code in C++. This talk was particularly notable for its accessibility, even for those who may not be deep into assembly language or advanced optimization techniques.

Gustav's approach in this talk was to demystify the optimization process. What stood out was his candid admission of not being an 'ultra advanced' professional in this area, making his insights and methods more relatable and applicable to a wider audience.
This talk is a must-watch for anyone interested in DSP code optimization. Gustav’s methods offer a practical and understandable way to improve processing efficiency, making it a valuable resource for both beginners and experienced developers looking to enhance their skills in audio DSP code optimization.

### Real-time confessions: the most common “sins” in real-time code by Fabian Renn-Giles

<div markdown="0">
<img class="lazyload" data-src="{{ images | append: "Fabian Renn-Giles.webp" }}" width="50%">
</div>

_Figure {% increment figureId20240111  %}. Fabian Renn-Giles._

Topping my list at number one was "Real Time Confessions: The Most Common Sins in Real Time Code" by Fabian Renn-Giles. This talk was a much-anticipated follow-up to the renowned "Real Time 101" talk from ADC 2018, a session frequently cited in many other talks at this year’s conference.

Fabian Renn-Giles captivated the audience with a deep dive into the intricacies of real-time audio coding. He focused mainly on synchronization mechanisms in passing data between the real-time and non-real-time threads. He underlined the importance of tooling and pointed to a few valuable resources. It's interesting that he and Gustav both discussed the usage of the `__restrict__` keyword in C++.

The talk was particularly significant because it underscored the complexities and challenges of writing real-time audio software. If such pros as Fabian can make mistakes, how should we, poor folk, fare? 😉

For anyone involved in audio development, especially in real-time contexts, this talk is an invaluable resource. Fabian's insights offer a rare glimpse into the thought processes of a seasoned developer, making it a must-watch for those aspiring to master the art of real-time audio coding.

## Surprise mention

<div markdown="0">
<img class="lazyload" data-src="{{ images | append: "Bug-free audio code-_Title Card_cropped.webp" }}" width="50%">
</div>

_Figure {% increment figureId20240111  %}. My talk on how to write bug-free audio code._

While I covered the top talks, I can't skip mentioning my own presentation, which was an absolute favorite of mine. Titled "Bug-Free Audio Code: Leverage Simple DSP Principles to Write Rock Solid Music Software Every Time," it was focused on ensuring the reliability and functionality of audio software. I aimed to provide insights on how to confidently present and release audio code, ensuring it operates flawlessly.

[Check out the slides and example code here.](https://github.com/JanWilczek/adc23)

I'm thrilled that my session was held in the largest auditorium, receiving great attendance and positive feedback. Thank you for attending!

## Summary

ADC 2023 was a melting pot of ideas, innovations, and insights, reflecting the dynamic nature of audio development. Your top 10 talks list will definitely differ from mine: how? Let me know in the comments below. What was YOUR favorite talk? What are you looking forward to at ADC24? I hope to see you there!

Lastly, for those eager to delve into audio programming, don’t forget to check out my [Audio Plugin Developer Checklist]({% link collections.all, 'checklist.html' %}), a list of essentials to master this field.
