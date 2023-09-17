---
title: "Should You Read \"Designing Audio Effect Plugins In C++\" by Will Pirkle?"
description: "Book review from a perspective of a C++ audio programmer."
date: 2023-08-30
author: Jan Wilczek
layout: post
images: /assets/img/posts/fx/2023-08-30-designing-audio-effect-plugins-in-cpp-book-review/
background: /assets/img/posts/fx/2023-08-30-designing-audio-effect-plugins-in-cpp-book-review/Thumbnail.webp
categories:
  - Audio FX
tags:
  - book review
  - cpp
  - juce
  - cmake
  - plugin
  - maths
  - learning
  - reverb
  - virtual analog
  - amplifiers
  - envelope
discussion_id: 2023-08-30-designing-audio-effect-plugins-in-cpp-book-review
custom_js:
 - /assets/vendor/lazyload/lazyload.min.js
 - /assets/js/wolfsound/modules/load_lazyload.js
---
Book review from the perspective of a C++ audio programmer.

<iframe width="560" height="315" src="https://www.youtube.com/embed/8VPdm-yNCsk?si=r6uMbAtXIItY1N6m" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

"Designing Audio Effect Plugins in C++" by Will Pirkle is one of the most widely recommended books to learn audio programming. As it's quite a long and expensive book, I've decided to read it cover-to-cover and give an honest and unbiased opinion on it so that you can consciously decide whether to read it or not. So… is it worth the hype? Let's find out!

### Table of Contents

1. [What is "Designing Audio Effect Plugins in C++" about?](#what-is-designing-audio-effect-plugins-in-c-about)
2. [What makes it good or bad?](#what-makes-it-good-or-bad)
   1. [The Good](#the-good)
   2. [The Bad](#the-bad)
3. [Why should you read "Designing Audio Effect Plugins in C++"?](#why-should-you-read-designing-audio-effect-plugins-in-c)
4. [My final thoughts](#my-final-thoughts)

{% render 'google-ad.liquid' %}

## What is "Designing Audio Effect Plugins in C++" about?

*In this book review, I have decided to follow the format of my favorite BookTube channel: [Mike's Book Reviews](https://www.youtube.com/@mikesbookreviews). Don't forget to check it out!*

Let's start with what is this book about.

<div markdown="0">
<img class="lazyload" data-src="{{ images | append: "DesigningAudioEffectPluginsInCppBookCover.webp" }}" alt="\"Designing Audio Effect Plugins in C++: For AAX, AU, and VST3 With DSP Theory\" (2nd edition) by Will Pirkle book cover" max-width="100%">
</div>

_Figure 1. "Designing Audio Effect Plugins in C++: For AAX, AU, and VST3 With DSP Theory" (2nd edition) by Will Pirkle book cover._

"Designing Audio Effect Plugins in C++: For AAX, AU, and VST3 With DSP Theory" (2nd edition) by Will Pirkle aims to be a tutorial on creating audio plugins for digital audio workstations (DAWs). It stands exactly in the middle of the ground that WolfSound covers: a place where digitial signal processing theory, C++, music, and operating systems theory meet to allow sound engineers, composers, sound designers, and musicians come up with sonically amusing landscapes.

This is quite a long book. A few chapters of the book deal very briefly with digital audio signal processing. The introduction is more of a review than an explanation so don't approach it thinking that you'll learn digital signal processing (DSP) in this way.

The next few chapters deal with the architecture of audio plugins. Each of the most popular plugin application programming interfaces (APIs), namely, VST3, AAX, and AU are explained in dedicated chapters with specific instructions on how a programmer should use them.

There is a chapter on Will Pirkle's own version of the JUCE C++ framework, called ASPiK and a chapter on his RackAFX environment for coding audio effects and audio plugins.

There are three huge chapters on filters alone followed by a gallery of audio effects: low frequency oscillators (LFOs), envelope detectors, delay-based effects, reverb, compressors, expanders, distortion effects, tube emulations, phase vocoder (with robotization, fast convolution and pitch shifting), concluded with a chapter on resampling.

Each chapter starts with theory and ends with the actual code implementation. That's why you should not be scared of the book's length: it's just the code listings that make it so large but, in my opinion, the code listings are an essential part of every programming book and I love to read them.

The promise of the book is that you'll be able to create various audio effects and use them in your DAW. Does it deliver?

Let's answer this question by focusing on what makes it good or bad.

## What makes it good or bad?

Let's start with the good.

### The Good

The greatest point of this book, in my opinion, which could be the sole reason to read it, is the extensive **audio plugin APIs description**. You get a very precise description of how the 3 main APIs (VST3, AAX, AU) work and how to use them.

This should give you a sense of **what the architecture of an audio plugin is**. It should also show you how similar all the APIs are. This, in turn, can help you understand what the JUCE C++ framework does under the hood.

Somewhat surprisingly, I believe it's much faster to read these 3 chapters than to browse manually the APIs' documentation and try to understand how to use them. I benefited immensely from these chapters.

The next biggest advantage of this book is the **great variety of audio effects presented**. Where else would you find a book that lists so many of them in such detail? Obviously, Will Pirkle loves filters and analog amplifier emulations. So if you're a fan of analog filters and analog distortion circuits, you should feel at home. One of my students really loves these parts of the book.

In general, there are **lots of effects to learn and implement** in this book.

What I love about great books is that they point you to other books. And indeed, this book has **quite a few references** which makes it easy to deepen your knowledge if you want to. And a lot of the cited research papers are available for free on the internet!

The book conveys **some good DSP practices**, e.g., "first calculate the output, THEN update the buffers." And the circular buffer implementation trick was very interesting and nicely explained as well! (Hint: if you want to wrap the binary value 1000 back to 0000, use a logical `and` operation with the wrap mask 0111; works like a charm!)

Finally, I really admire putting the code into the book. Thanks to it, you always get an **end-to-end effect code**. That's an important point because for many people the biggest difficulty is "how do I translate the algorithm on paper to functioning code?". These step-by-step instructions can really help get your head around audio plugin implementation. Additionally, this code should be easy to implement in JUCE.

These were the advantages of the book what are its downsides?

### The Bad

Well, there were a few things I didn't like…

First of all, a perfectionist like me cannot stand **not conforming to the best C++ practices**.

Some of the "sins" that struck me where

- manual memory allocation (naked `new`) instead of `make_shared` or `make_unique`,
- not using `std::vector<T>`; the author used `std::unique_ptr<T[]>` instead and I still don't know why (it wasn't an alignment issue),
- manual specification of copy constructor and copy assignment operators; in C++ code like this:

```cpp
struct PSMVocoderParameters {
    PSMVocoderParameters() {}
    PSMVocoderParameters& operator=(. . .){ . . . }
    // --- params
    double pitchShiftSemitones = 0.0; // half-steps
    bool enablePeakPhaseLocking = false;
    bool enablePeakTracking = false;
};
```

i.e, explicit empty default constructor and a copy assignment operator for a plain-old-data (POD) type are completely unnecessary. Worse; they prevent the compiler from generating the remaining  (copy constructor, move constructor, and move assignment). In C++, whatever the compiler can generate, it should generate.

If you are interested in this topic, you can read up on [the rule of three/five/zero in the CPP reference.](https://en.cppreference.com/w/cpp/language/rule_of_three)

In general, the code presented has the "**academia vibe**" to it not the "industry standard" vibe… That was my impression at least 😉

Another tiny thing that annoyed me was that **Will Pirkle keeps using the term "C++ object" instead of "C++ class".** I have no idea why because it's quite clear in Computer Science and in the C++ standard [what is an object](https://en.cppreference.com/w/cpp/language/object) and [what is a class](https://en.cppreference.com/w/cpp/language/class).

That's a class:

```cpp
class EmptyAudioEffect {};
```

That's an object of this class:

```cpp
EmptyAudioEffect emptyAudioEffectInstance;
```

Don't trust me? A quote from [the C++ standard](https://en.cppreference.com/w/cpp/language/object) (boldface by me):

> The following entities **are not objects**: value, reference, function, enumerator, **type**, non-static class member, template, **class** or function template specialization, namespace, parameter pack, and `this``.

Objects are instances of classes. Period. Otherwise we would have "2 objects which are instances of the EmptyAudioEffect object…" What?!

Some more **C++ and software engineering sins** of the code presented in the book (listed to be brief):

- not using `auto`, `const`, or `constexpr`,
- using modifying getters (a `getSomeInfo()` function that under the hood changes the object's state),
- primitive obsession (using `int`s, `float`s, and `double`s to represent delay, phase, magnitude, frequency, amplitude, pitch shift in semitones…),
- using C-style arrays instead of `std::array`,
- using manual for-loops instead of `std::copy`,
- not using `std::complex` ,
- (unnecessarily) explicitly declared default constructors.

These points are not just annoying: since this book may be the only resource people read before writing audio code, they will inevitable duplicate these bad practices and carry them over to new projects resulting in contagious poor-quality code spreading over code editors all around the world…

Another thing that I didn't like (but it may be just my personal thing) is the **amount of self-promotion in this book**, especially toward the ASPiK and RackAFX frameworks and the "Designing Software Synthesizer Plugins in C++: With Audio DSP" book by Will Pirkle.

Expressions like

> With ASPiK that's easy, you just need to do 3 things…

> Of course, if you use ASPiK, you have it out of the box…

> You would like to learn that? Only in my other book…

> Just go to Will Pirkle forums…

come up a little bit too often to my taste. Especially, that I don't trust ASPiK or RackAFX if they have the same code style as this book does.

As a matter of fact, I have not seen ASPiK or RackAFX used commercially, not have I seen any job postings involving them… Have you? If so, please, let me know in the comments below.

On top of it, the Will Pirkle forums doesn't seem very active. At least it didn't when I last checked because now they are completely removed.

The bad news is that **this book won't teach you digital signal processing (DSP).** But of course I understand it; a book cannot be infinitely long and the author must make a decision where to stop the depth of explanations. So make sure you know some basic DSP before you pick it up.

The book will probably **not explain sufficiently the presented audio algorithms.** That's simply because some of them are very complex, like digital waveguides. When a lot of research goes into a particular area, it's hard to summarize it in a half of a chapter. You'll need to pick up the references to fully grasp the presented techniques.

The amount of knowledge packed into this book is a little bit daunting sometimes. So much so that **it's easy to get lost in the formulas** and lose track of what each of the variables meant. I'm used to reading scientific literature but this book provides too little explanations at times. But I get that it's a difficult task to explain these topics well and, of course, it's very easy to criticize someone. So, please, understand that these are just my opinions.

Finally, there is a handful of **editing errors**, mostly coming from copying and pasting whole paragraphs from other chapters. I guess it was done to speed up the writing process because a lot of code description parts are similar. Unfortunately, these weren't caught before the book release. **Typos** are present as well.

But **what I cannot forgive is referring to the term "Hanning" as a name**. A quote from the book:

> Because of the similarity of the names Hamming and Hanning, we will always refer to the Hanning window as simply "Hann"(…)

At this point, it should already be widely known that there is a von Hann window and a Hamming window but no "Hanning" window. This mistake has been introduced in the history of DSP through inaccurate citations ([read the explanation on Wikipedia](https://en.wikipedia.org/wiki/Hann_function#Name)). Please, correct it in the next edition of the book!

These where my thoughts on what makes "Designing Audio Effect Plugins in C++" good or bad. Now, should you read it?

## Why should you read "Designing Audio Effect Plugins in C++"?

I believe you can get a lot of benefits from reading this book on condition that you already know some digital audio signal processing and the basics of the C++ programming language. Without these two preconditions it may be quite difficult for you to understand this book given all the "mental shortcuts" that the author is taking.

This book is great for audio programmers to get a quick overview of the existing APIs and which resources to check out to implement a particular effect.

If you want to implement the presented audio effect algorithms without understanding them or knowing how to code, you'll likely run into trouble.

This book is also math-heavy. If that's something that discourages you, then it may not be a book for you.

So if you want to get a high-level view on the most popular audio APIs and audio effects and you promise not to follow the presented coding style, you can find it a good but slow read.

## My final thoughts

As some closing thoughts, I'd like to say that I personally benefited from the book although I was often annoyed by it.

In the end, the biggest value of this book is in its existence. I cannot think of any other book on the market right now that would combine C++ code and audio effects theory apart from ["Audio Effects" by Reiss and McPherson]({% link collections.all, 'resources/index.html' %}#other-digital-audio-books). So thank you, Will Pirkle, for your efforts to bring audio programming to more people.

This book does check off a few marks on my [audio plugin developer checklist]({% link collections.all, 'single-pages/checklist.html' %}). Does it for you too?

Ultimately, it comes to your needs and preference. So what's your opinion on this book? Have you read it? Do you plan to read it? Let me know in the comments below.