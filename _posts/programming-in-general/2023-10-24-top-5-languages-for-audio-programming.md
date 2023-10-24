---
title: "Top 5 Languages For Audio Programming"
description: "My personal favorite list of programming languages best for audio processing. Which for prototyping and which for real time?"
date: 2023-10-24
author: Jan Wilczek
layout: post
images: /assets/img/posts/programming-in-general/2023-10-24-top-5-languages-for-audio-programming/
background: /assets/img/posts/programming-in-general/2023-10-24-top-5-languages-for-audio-programming/Thumbnail.webp
categories:
  - Programming in general
tags:
  - c
  - cpp
  - python
  - matlab
  - rust
  - career
  - learning
  - java
  - javascript
  - typescript
  - cmake
  - puredata
  - android
  - juce
  - plugin
discussion_id: 2023-10-24-top-5-languages-for-audio-programming
custom_js:
 - /assets/vendor/lazyload/lazyload.min.js
 - /assets/js/wolfsound/modules/load_lazyload.js
---
Which language should you learn first for audio programming?

So... you would like to write software that processes sound and for this you need a programming language. But there are so many of them out there! Which one to
 use? That's why in this article I'm going to discuss my personal top 5 programming languages for audio programming.

WolfSound is a place where you can learn how to process sound using self-written software and of course we need some programming language to write software. Taking into account my experience during studying, research, industry career, tutorials, prototyping, and all the conversations I had with fellow developers and researchers, I decided to come up with a list of top 5 programming languages that you should use if you would like to get a job in the audio programming industry or you would like to pursue your hobbies.

### Table of Contents

1. [(Dis)honorable mentions](#dishonorable-mentions)
   1. [MATLAB®️](#matlab️)
   2. [Max/MSP](#maxmsp)
   3. [Zig/Nim/etc](#zignimetc)
   4. [JavaScript (TypeScript)](#javascript-typescript)
   5. [C-Major](#c-major)
2. [Number 5: PureData](#number-5-puredata)
3. [Number 4: Rust](#number-4-rust)
4. [Number 3: C](#number-3-c)
5. [Number 2: Python](#number-2-python)
6. [Number 1: C++](#number-1-c)
7. [Summary](#summary)

## (Dis)honorable mentions

Before we jump into the list of the five programming languages, I would like to highlight some honorable (or dishonorable) mentions. These are the languages that are known to me and I would like to explain why they aren't in the top five.

### MATLAB®️

The first honorable/dishonorable mention is MATLAB®️. MATLAB®️ is a huge programming environment created by MathWorks that is very popular in academia. If you go to university to study audio programming, you are likely to use MATLAB®️ and for a good reason: it's a very powerful environment. It's pros are:

- you can code even very advanced algorithms very fast,
- visualization is amazing,
- thanks to all the available functions, prototyping is very fast,

but... the main problem with MATLAB®️ is that it's crazy expensive: it's so expensive that basically as an individual, I don't see a way how I could afford it. I'm not sure if one would be able to use MATLAB®️ even at a moderately sized company. Even if you have a MATLAB®️ license and you want to share a piece of MATLAB®️ code with someone, it's likely that the other person doesn't have a license. Because of these limitations, I wouldn't advise choosing this language. Actually, i have quite a good alternative in my top five list so keep on reading!

### Max/MSP

The next honorable mention is Max/MSP. I must admit out of the box that I don't have much experience with with it and that's the main reason why it's not in the top five. Also, again, it needs a license but if you can afford it and you think it's worth it, then go for it! It's simply not for me.

### Zig/Nim/etc

The next ones on this list are languages like Zig, Nim, or maybe some other language that I don't even know that has come up in the last years. New languages seem to sprout everywhere these days. I prefer stable, widely used languages that are well supported, have their package managers, coding environments, etc. Maybe Zig and Nim are super fast and maybe there's something amazing about them; I just haven't seen them widely adopted in the industry. For example, at the Audio Developer Conference 2022, few people talked about them. Maybe that's a good reason why you shouldn't use them either.

### JavaScript (TypeScript)

Another honorable mention here and one that I'm really curious to observe in the coming years is JavaScript. (We could also extend it to include TypeScript). This is something to look out for in the near future. Will the web audio community grow exponentially? I don't know. But if you have watched or listened to my recent interview with Christoph Guttandin, who is a web audio developer, you have learned how many amazing things you can do in the browser with
 audio. As Chris said: it's so easy to share a link with someone nowadays so it's really amazing what will be possible in the future. Right now, I just don't feel that we are in that spot yet but who knows, maybe it's soon to come!

### C-Major

The last honorable mention is the C-Major programming language: it was announced last year during the Audio Developer Conference by SoundStacks. It's a new programming language dedicated to prototyping audio plugins. I haven't used it extensively and I also haven't heard about people using it. There are some tutorials on the Internet so if you find it interesting, of course, check it out. I just feel that maybe we need to wait a few years before it's widely adopted; I don't know.

With this out of the way, here are now my top 5 languages that I believe are great for audio programming.

## Number 5: PureData

The number five is PureData. Sometimes PureData is described as Max/MSP for poor people; I disagree with this statement completely. I have had a great pleasure of meeting Miller Puckette, the creator of PureData, in person. What's interesting, PureData was licensed to become the foundation of Max/MSP. What's great about PureData is that it's free. It is also widely used by sound designers and composers. Additionally, a lot of industry books explain DSP topics using PureData (for example, *The Theory and Technique of Electronic Music* by Miller Puckette) so I really believe that it's highly beneficial to learn this language. I experimented with it a bit but I plan to learn it more and more, maybe even make some tutorials about it on the YouTube channel. Whats great about PureData is that there are so many resources on it available: not just books but also a huge number of YouTube videos where people do crazy stuff using PureData as LEGO bricks; I imagine it must be a lot of fun! Of course, visually it may not be as attractive as Max/MSP but, nevertheless, it's completely free and it seems crazy powerful.

## Number 4: Rust

Number four on this list is Rust. Rust is a language that's very popular in the programming community in general. I see it also adopted more and more in the DSP community and for a good reason: it's designed in a way to ensure memory safety and in my opinion it simply has so many great defaults:

- you have a naming convention as a default,
- you have constness as a default,
- you are required to handle all exceptional cases without exceptions,
- you have a package manager and a linter that ship with Rust.

There really are so many amazing things that you get out of the box as a default which make me think that it's a beautiful language. I know programming enthusiasts out there who use it all the time. I just don't see as many job postings using Rust for audio but I know such jobs exists: I have a few friends who actually worked in Rust audio. Even on the Rust's Discord, you have a "Rust audio" channel so it's definitely something to check out. If you're just starting out, it may be a good choice for you but the problems of course are that it's not compatible with legacy code and it is still a relatively new language so there's not so much code written in it in contrast to number three on this list which is...

## Number 3: C

We have lots and lots of audio code written in C. For example, PureData (which was number five) is written in C. C is so widespread that it may be really beneficial to learn this language. I believe that if you know C, it should be quite easy for you to find an audio related job, especially related to embedded software where the programming environment is more restricted in terms of languages or frameworks. So definitely C still holds strong; I don't know what the future will bring but at the moment, the amount of audio code written in C is so huge that I doubt that it will go away soon. But of course, it has its disadvantages like manual memory management and lack of type safety.

## Number 2: Python

Number two and my favorite language for prototyping is Python. I love Python:

- the syntax is great,
- you have a package manager,
- prototyping is super super easy,
- you can code anything you can imagine,
- IMO it's much easier and faster to run than MATLAB®️ (which takes quite a long time to launch),
- you can use Python with any IDE.

Python is simply so enjoyable: you write a few lines of code and create a powerful audio effect. I use Python all the time for prototyping, for understanding various audio algorithms but also for creating figures, for creating plots, for creating diagrams related to DSP: it's just such a versatile language! I have a friend who is actually doing audio programming only in Python. Additionally, with Python, he's able to write microservices, he's able to write whole websites, he's able to write desktop apps, he's able to write audio renderers; it's simply incredible how much you can do with Python.

The only downsides of Python are its optimality and threading because of the global interpreter lock. So if you're looking for something performant or real-time capable then maybe Python is not the best option. But for single scripts, understanding  algorithms, and especially prototyping, I think it's simply amazing: I love Python!

## Number 1: C++

The number one in the top 5 languages for audio programming is, of course, (we all have seen it coming) C++.

The C++ programming language is so ubiquitous in the audio community that it's hard to find a project that is not using C++ in one way or another. It can also be used on embedded devices provided a proper cross-compiler is available. In general, every audio plugin that I see is written in C++. You have the JUCE C++ framework and the iPlug2 framework which make writing audio plugins even simpler. The community of C++ is huge. There are so many resources on it and there are so many C++ job openings.

In year-to-year developer surveys (like [Stack Overflow Developer Survey 2023](https://survey.stackoverflow.co/2023/#section-most-popular-technologies-programming-scripting-and-markup-languages)), C++ is the most popular language that doesn't use a virtual machine. So typically, the most popular language is JavaScript/TypeScript, then you get, of course, Python, and then C# and Java but then always comes C++.

It's really amazing how fine-grained this language is. You can do everything with it. A lot of things are more difficult to code than, for example, in Python or managed languages but at the same time, the sky is the limit in what you can code. When it comes to the real-time performance and optimization, I don't know if there is any other compiled language that results in programs as fast as C++: so much engineering that went into creating the C++ compilers that it's simply hard to match.

C++ seems to be a language that was popular, is popular, and will be popular, simply considering the amount of code that has already been written in C++, how much money and effort was put into developing its compilers, and finally thanks to the advances of the C++ standard. What we've seen in C++ 2023 is simply amazing and I really hope that with time we'll be able to have C++ safer, easier to use, and more understandable. I know that [Herb Sutter has his CppFront or cpp2 syntax](https://youtu.be/ELeZAKCN4tY?si=FkO8vi_c_IUev_Wo) that's using good defaults: who knows where it'll end up? We already have C++ package managers, we have quite established tools like CMake, Visual Studio, and Xcode.

Additionally, C++ is compatible with C so there's another huge body of code that you can reuse thanks to C++.

What is more C++ is used for programming every operating system out there. Even on Android on iOS you can interact with C++ and use the audio drivers thanks to C++. On top of it, you have the interoperability with other languages: Python, C#, Java, Rust, and more. Basically, everywhere I look in the audio landscape, I see C++.

Sometimes C++ is annoying because writing stuff takes more time than I would like but, in general, it's a great language.

If you consider learning just one language for audio programming and you would like to do anything that has to do with real time then C++ is your safest bet. If you don't have to run your code in real time, then probably Python is fine for you because there you also get all those fancy deep learning features. But if you want to do anything with real time and audio, I think C++ should be your number one choice.

If you would like to know what to learn from C++ specifically for audio programming, you can find it on my [free audio plugin developer checklist]({% link collections.all, 'single-pages/checklist.html' %}).

## Summary

Okay so that was my list of top 5 languages for audio programming: PureData, Rust, C, Python, and C++! What are your top languages for audio programming? Let me know in the comments down below 😉
