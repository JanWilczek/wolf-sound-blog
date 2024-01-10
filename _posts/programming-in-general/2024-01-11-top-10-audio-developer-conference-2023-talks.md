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
  - rust
  - cpp
  - c
  - deep learning
discussion_id: 2024-01-11-top-10-audio-developer-conference-2023-talks
custom_js:
 - /assets/vendor/lazyload/lazyload.min.js
 - /assets/js/wolfsound/modules/load_lazyload.js
---
Welcome to a detailed summary of the Audio Developer Conference 2023. I'm Jan Wilczek, and I run the blog and YouTube channel TheWolfSound.com, where I share insights into software development, digital signal processing, and audio programming. This article is your gateway to understanding the essence of ADC 2023, especially if you couldn't attend in person.

**Table of Contents**

1. **General Vibe of the Conference**
2. **Workshops Highlights**
3. **Top 10 Talks at ADC 2023**
   3.1 **Developing an AI-powered karaoke experience by Thomas Hézard & Clément Tabary**
   3.2 **Creating ubiquitous, composable, performant DSP modules by Stefano D'Angelo**
   3.3 **An Introduction to CLAP, a new plug-in standard by Alexandre Bique**
   3.4 **Exploration of strongly-typed units: a case-study from digital audio by Roth Michaels**
   3.5 **RADSan: a realtime-safety sanitizer by David Trevelyan & Ali Barker**
   3.6 **Writing elegant DSP code with Rust by Chase Kanipe**
   3.7 **Lessons learned from implementing a real-time multichannel audio application on Linux by Olivier Petit**
   3.8 **The architecture of digital audio workstations (and other time-based media software) by Ilias Bergström**
   3.9 **A more intuitive approach to optimising audio DSP code – Guiding the compiler through optimising your code for you by Gustav Andersson**
   3.10 **Real-time confessions: the most common “sins” in real-time code by Fabian Renn-Giles**
4. **My Talk: Bug-free audio code: leverage simple DSP principles to write rock-solid music software every time**
5. **Conclusion and Further Resources**
6. **Stay Connected**

### General Vibe of the Conference

This year's conference was marked by a significant focus on **Artificial Intelligence** in audio development. There was a noticeable increase in software engineering talks, reflecting the evolving landscape of audio programming. The event was intensely packed with sessions, providing an enriching but exhaustive experience. Personally, it was exhilarating to meet many of my DSP Pro online course students and be recognized by the community.

### Workshops Highlight

**Workshops at the Audio Developer Conference**

Before diving into the top talks of the ADC, it's worth highlighting the workshops that prefaced the conference. The workshops are an integral part of ADC, offering hands-on experiences in various audio development aspects.

**Rust Workshop: Joe Noel, Nico Chatzigianis, James Hallowell**

The first workshop I attended was about integrating C audio code into Rust, a language that's increasingly popular among developers. This workshop, led by Joel Knoll, Nico Chatzigianis, and James Hallowell from Focusrite, was an eye-opener. It was a practical, step-by-step guide on writing applications in Rust that interact with C code. The experience was enlightening, blending two significant programming domains. I even shared my results on LinkedIn, proud of the progress and the knowledge gained.

**Accessibility workshop with a panel: Jay Pocknell (episode 13 of the WolfTalk podcast) & Harry Morley**: 

The next workshop that caught my attention was the Accessibility Panel organized by Jay Pocknell, founder of the Sound Without Sight organization. This workshop brought together up to ten experts discussing the various aspects of creating accessible audio software. It included a powerful presentation by Harry Morley from Focusrite, demonstrating the difference between accessible and non-accessible apps. The discussions were incredibly informative, shedding light on the importance and methods of making audio software accessible to all users.

These workshops were not just informative but also inspirational, offering fresh perspectives on audio software development. They provided practical knowledge and demonstrated the conference's commitment to addressing both technical and inclusive aspects of audio development. For those interested in the detailed nuances of audio software, these workshops were a treasure trove of knowledge.

### Top 10 Talks at ADC 2023

Before jumping into the crux of the top 10 talks at the Audio Developer Conference, let me share a couple of disclaimers. First, despite having access to the recordings, time constraints prevented me from watching every single talk. So, I might have missed some hidden gems. Secondly, the talks I found most engaging and insightful are based on my personal experience and perspective as an audio developer deeply involved in mobile apps, audio plugins, and teaching audio programming. My tools of the trade are primarily C and Python, so my views are shaped through this lens. Remember, there's a vast array of talks catering to diverse interests, and what resonates with me might differ from your areas of interest or expertise.

That said, the top 10 talks I'm about to share were, in my opinion, the standouts of the conference, each for its unique contribution to the field of audio development. Whether it was groundbreaking new technology, innovative techniques, or inspiring insights, these talks represent the cutting edge of audio development. So, let's dive in and explore the highlights and key takeaways from each of these illuminating presentations.

**Developing an AI-powered karaoke experience by Thomas Hézard & Clément Tabary**

Alright, so the tenth talk I watched was about creating an AI-powered karaoke app, led by Thomas Hazard and Clement Tabary from MWM. They walked us through how they built this karaoke application, which was pretty cool. What I found great about their presentation was how they highlighted every single problem they bumped into and the ways they tackled them. It was like a real-world case study in problem-solving with AI in audio. They dived deep into how deep learning can play a big role, especially in audio applications that are already out there. If you’re into how deep learning meshes with audio, especially in practical, in-market apps, this talk is definitely worth your time.

**Creating ubiquitous, composable, performant DSP modules by Stefano D'Angelo**

Now, the ninth talk that grabbed my attention was by Stefano D'Angelo. He's the brain behind Orastron and their DSP component library, Brickworks. This wasn't just a showcase of their library, though. Stefano provided a comprehensive view on building composable and efficient DSP modules. It was like a deep dive into the nuts and bolts of digital signal processing, and how you can make your DSP code not just good, but top-notch in terms of performance. If you're looking to get your hands dirty with real-deal DSP implementation, Stefano's insights are gold. Plus, checking out the Brickworks library could give you some solid leads on how to shape your own DSP code.

**An Introduction to CLAP, a new plug-in standard by Alexandre Bique**

The eighth talk, which I managed to catch, was Alexander Bique's introduction to a new plugin standard called CLAP. This topic intrigued me – why do we need another plugin standard? As it turns out, CLAP addresses several non-obvious issues. It's a free standard, which is quite a rarity, and it clearly defines the responsibilities of both the plugin and the host. This clarity is essential because, often, plugins are developed according to one format, but hosts might operate differently, leading to compatibility issues. 
CLAP also employs a C-based API, meaning it's versatile across platforms. I'm keen to see how it evolves, particularly with potential support from the Guice team. Given Guice's current approach of extensions, official support for CLAP could be a game-changer. For anyone in the plugin development space, this is a talk that's bound to pique your interest.

**Exploration of strongly-typed units: a case-study from digital audio by Roth Michaels**

Number seven on my list was a must-see for me – Roth Michaels' talk. The title itself, "Exploration of Strongly Typed Units, a Case Study from Digital Audio," had my full attention. Roth tackled a common issue in C coding, the 'primitive obsession', where everything is passed around as floats, doubles, or integers. This can become a major headache, especially in larger codebases. What I found particularly enlightening was Roth's approach to this problem using pre-written libraries for a more generalized solution, moving away from primitive data types to more explicit, strongly typed units. This not only improves the quality of the code but also its readability and reliability. Adding to the intrigue was the library discussed by Roth, developed by Mateusz Pusch, a prominent figure in the C community. As a fellow Polish, it's always great to see such recognition in the programming and audio world. For anyone coding in C, especially in digital audio, Roth's talk is a goldmine of insights.

**RADSan: a realtime-safety sanitizer by David Trevelyan & Ali Barker**

At number six was the intriguing talk on "RADSan: A Real-Time Safety Sanitizer" by David Trevelyan and Ali Barker. For those not in the know, a sanitizer is a tool in the compilation process that adds extra code to enhance runtime safety. This talk was especially relevant for anyone dealing with memory and undefined behavior issues in software. AddressSanitizer and UndefinedBehaviourSanitizer, commonly used with the Clang compiler, are prime examples of such tools, detecting memory errors and undefined behaviors respectively.
But RADSan? It's a new player in the game, focusing on ensuring real-time code doesn't violate its runtime guarantees. Considering audio plugins process sound on a real-time thread, meeting deadlines without causing glitches is paramount. This means avoiding allocations, system calls, and locks. RADSan envelops your audio code in additional layers to check its behavior, a crucial step if you're incorporating third-party libraries or uncertain code. It’s a topic that piqued my curiosity, and I'm eager to see how RADSan evolves and gets adopted in audio development circles.

**Writing elegant DSP code with Rust by Chase Kanipe**

Landing at number five was Chase Kanipe's talk on "Writing Elegant DSP Code with Rust." I had the pleasure of watching Chase's presentation last year on license checking, which was nothing short of impressive. This year, he shifted his focus to Rust for DSP coding — a topic I couldn't miss. However, the experience was marred by technical hiccups during the remote session, with poor video quality and small font sizes rendering the code unreadable on screen. It was disappointing to see attendees, including myself, having to leave due to these issues.
Despite these setbacks, I later watched the talk on my computer and it was thoroughly enlightening. Chase's ability to delve into the nuances of Rust in DSP coding was remarkable. For those interested in the intersection of Rust and audio processing, this talk is a must-watch once it’s available on YouTube. I'm also excited about the possibility of hosting Chase on the Wolf Talk podcast, so stay tuned for that!

**Lessons learned from implementing a real-time multichannel audio application on Linux by Olivier Petit**

Ranked fourth in my list of top talks at the conference was Olivier Petit's presentation on "Lessons Learned from Implementing a Real Time Multi Channel Audio Application on Linux." This session was a real gem for anyone interested in the practicalities of audio engineering, especially in a Linux environment. Olivier methodically outlined the challenges encountered when running real-time audio applications on Linux and shared step-by-step solutions.
What stood out to me in this talk was the practical advice on using system traces — a common recommendation that often lacks detailed guidance. Olivier's hands-on approach not only made the concept clear but also demonstrated its application in real-world scenarios. His talk is an invaluable resource, particularly for those not deeply versed in Linux, offering insights that are both accessible and immensely useful. I highly recommend watching this talk for a deeper understanding of real-time audio processing in Linux systems.

**The architecture of digital audio workstations (and other time-based media software) by Ilias Bergström**

Securing the third spot on my list was a fascinating talk by Ilyas Bergstrom from Elk Audio, focusing on "The Architecture of Digital Audio Workstations and Other Time-Based Media Software." Ilyas, with his profound experience at Elk Audio, shared the architecture of two digital audio workstations he's been a part of. This talk was a deep dive into the intricacies of audio software design, an area that’s not often discussed in detail.
What makes this talk stand out is its focus on design and architectural choices in audio software development. For anyone curious about the internal workings of digital audio workstations or looking to structure their audio applications efficiently, Ilyas' insights are invaluable. He brought to light the often-overlooked aspects of design that can significantly impact the functionality and user experience of audio software. I highly recommend this talk to those interested in audio software design, as it offers a rare glimpse into the complex world of digital audio workstations.

**A more intuitive approach to optimising audio DSP code – Guiding the compiler through optimising your code for you by Gustav Andersson**

Coming in at number two on my top talks list was Gustav Andersson's "A More Intuitive Approach to Optimizing Audio DSP Code." Gustav, a developer at Elk Audio, presented a highly approachable talk on optimizing DSP (Digital Signal Processing) code in C. This talk was particularly notable for its accessibility, even for those who may not be deep into assembly language or advanced optimization techniques.
Gustav's approach in this talk was to demystify the optimization process. He emphasized the use of simple, logical strategies to guide the compiler in optimizing code. What stood out was his candid admission of not being an 'ultra advanced' professional in this area, making his insights and methods more relatable and applicable to a wider audience.
This talk is a must-watch for anyone interested in DSP code optimization. Gustav’s methods offer a practical and understandable way to improve processing efficiency, making it a valuable resource for both beginners and experienced developers looking to enhance their skills in audio DSP code optimization.

**Real-time confessions: the most common “sins” in real-time code by Fabian Renn-Giles**

Topping my list at number one was "Real Time Confessions: The Most Common Sins in Real Time Code" by Fabian Renn-Giles. This talk was a much-anticipated follow-up to the renowned "Real Time 101" talk from ADC 2018, a session frequently cited in many other talks at this year’s conference.
Fabian Renn-Giles captivated the audience with a deep dive into the intricacies of real-time audio coding. His talk was a masterful blend of expertise, practical insights, and the unveiling of common misconceptions in the field. He skillfully debunked several preconceived notions in audio software engineering, offering a fresh perspective on widely held beliefs.
The talk was particularly significant because it underscored the complexities and challenges of writing real-time audio software. Rengils' experience shone through as he discussed the evolution and rectification of concepts from his earlier talk, showcasing the dynamic nature of learning and growth in software development.
For anyone involved in audio development, especially in real-time contexts, this talk is an invaluable resource. Rengils' insights offer a rare glimpse into the thought processes of a seasoned developer, making it a must-watch for those aspiring to master the art of real-time audio coding.

### My Talk: Bug-free audio code: leverage simple DSP principles to write rock-solid music software every time

 While I covered the top talks, I can't skip mentioning my own presentation, which was an absolute favorite of mine. Titled "Bug-Free Audio Code: Leverage Simple DSP Principles to Write Rock Solid Music Software Every Time," it was focused on ensuring the reliability and functionality of audio software. I aimed to provide insights on how to confidently present and release audio code, ensuring it operates flawlessly. I'm thrilled that my session was held in the largest auditorium, receiving great attendance and positive feedback. 

Lastly, for those eager to delve into audio programming, don’t forget to check out my audio plugin developer checklist on dwolfsound.com, a comprehensive guide to mastering the essentials in this field. 

ADC 2023 was a melting pot of ideas, innovations, and insights, reflecting the dynamic nature of audio development.

### Stay Connected

For more insights and resources, including the Audio Developer Checklist, visit [TheWolfSound.com](https://thewolfsound.com/).