---
title: 'Is "Designing Software Synthesizer Plugins in C++" by Will Pirkle for you? Book review'
description: "One of the few books aiming to teach you sound synthesis techniques AND their implementation in C++. Does it live up to expectations? Read the review to find out."
date: 2025-03-27
author: Jan Wilczek
layout: post
permalink: /designing-software-synthesizer-plugins-in-cpp-with-audio-dsp-by-will-pirkle-book-review/
background: /assets/img/posts/synthesis/2025-03-27-designing-software-synthesizer-plugins-in-cpp-book-review/Thumbnail.webp
categories:
  - Sound Synthesis
tags:
  - sound wave
  - sampling (sound generation)
  - learning
  - virtual analog
  - envelope
  - plugin
  - effects
  - book review
  - software architecture
  - cpp
  - filtering
  - wavetable
  - waveform
  - maths
  - audio generation
discussion_id: 2025-03-27-designing-software-synthesizer-plugins-in-cpp-book-review
---
Should you read it? 📚

> "*Designing Software Synthesizer Plugins in C++* provides everything you need to know to start designing and writing your own synthesizer plugins, including theory and practical examples for all of the major synthesizer building blocks, from LFOs and EGs to PCM samples and morphing wavetables, along with complete synthesizer example projects."

Really?

*Side note: if you want to learn how to build a full-fledged sound synthesizer using wavetable, subtractive and waveshaping synthesis, I have released my synthesizer as open source. It is [available on GitHub](https://github.com/JanWilczek/EdenSynth) and I have recently begun [streaming its development](https://www.youtube.com/live/vxzEBgo3lGk?si=gJ44LnCrMerZ2Yzh).*

## What is "Designing Software Synthesizer Plugins in C++" about?

*Designing Software Synthesizer Plugins in C++: With Audio DSP* by Will Pirkle is a book that aims to teach you the basics of sound synthesis and how to implement them in C++.

Given that the other book by Will Pirkle explains writing audio effect plugins in C++, a sound synthesizer book seems like a natural follow up.

*Note: I’ve reviewed the audio FX book on the blog [here.]({% post_url collections.posts, '2023-08-30-designing-audio-effect-plugins-in-cpp-by-will-pirkle-book-review.md' %})*

While it sounds very promising and I was eager to read this book, I was quite a bit disappointed learning that it’s actually about… a library of sorts.

Imagine your university professor writing a sound synthesis library and then writing a book explaining their design and encouraging you to use their code and experiment.

At least that’s the feeling I had with this book.

But before I start complaining, let’s first discuss the good sides of this book.

## The good

I did find quite a few positives about this book.

The first one being the fact that **this book exists**.

There are simply too few books on this subject on the market!

Additionally, **this books contains very good descriptions of analog synthesizers.** I especially enjoyed the explanations of voice stealing strategies and modulation.

**It also references existing designs**, like the general synth architecture from MIDI Manufacturers Association (yes, they’ve published how a generic synthesizer’s architecture looks like).

**You’ll also find here a rich discussion of synth filters.** You can use the presented knowledge to guide your implementation.

Another upside of this book is **the extensive bibliography.** Having a guide where to look for more information is always very useful.

As a plus, one could say that **the source code for this book is still available online** but more on this in a second…

Just let me add that I’m happy to see **`std::unique_ptr` used throughout the book** which isn’t the case for [the other book by this author]({% post_url collections.posts, '2023-08-30-designing-audio-effect-plugins-in-cpp-by-will-pirkle-book-review.md' %}).

Finally, as a point which can be viewed both as a pro and a con, **there’s little source code in the book.** Thanks to this fact, the book is shorter. However, it’s difficult/impossible to jump back and forth between the code and the book. It requires you to either read on a computer or be very dedicated; I am not sure how many people will really read the book and the code side by side. I know I haven't.

## The bad

And now to the not so positive….

To start off, it’s important to state that **this book teaches you the author’s framework SynthLab not a general approach to writing synthesizers.** And this, unfortunately, negatively impacts the educational aspect of the book. While you may be able to extract some code out of the example projects to play with, it’s rather unlikely that you’d be able to create your own synth after reading. Really, if you want to get started creating synth plugins, you’d better check out [my short wavetable synthesizer tutorial]({% post_url collections.posts, '2021-09-24-wavetable-synthesis-juce.md' %}).

If you decide to read this book, you’ll see a lot of SynthLab-specific code that is not relevant to learn synthesis or its implementation.

And this code, to my taste, is simply **poor C++ style**, including

- `k`-prefixing,
- no `std::vector` where it should be used,
- naked `new`, or
- `switch` statements for implementing a finite state machine (which is generally considered hard to understand and maintain and, thus, not recommended).

I can already hear you saying: “But Jan, he’s a university professor, what can you expect?…”

Really, being a professor is a justification for teaching bad code practices? I don’t buy that.

The next thing is that **it is really complicated to get the code running:** I quit after 30 minutes of trying. Call me lazy but I expect code packaged with an educational book to be quick and easy to clone and build. That’s not the case here.

The reason it is so complicated is that you get a bunch of classes without any build system files connecting them and to experience any sound generation you would need to adapt the code yourself to a specific plugin framework like JUCE or iPlug2.

Alternatively, you could use the ASPiK plugin framework created by Will Pirkle… you just need to get it to work first 😉 And the setup instructions are veeery convoluted with lots of links and unclear nomenclature even to me, who read both of Pirkle’s books. There’s no step-by-step walkthrough or tutorial.

But please, prove me wrong. Here are the instructions: [https://www.willpirkle.com/synthlabdm/](https://www.willpirkle.com/synthlabdm/) (accessed March 27, 2025).

By the way, this link is different from what you’ll find in the text: **the documentation website is under a different address than specified in the book.**

If you look at code listings, **the code seems clean but it’s hard to take something out of this for yourself**; I think it’s easier to try implementing your own approach. Especially, that you cannot run the provided code…

On top of it, **class relationships are very complicated and not explained very well in my opinion.**

And if you want to “go and ask on the forum”, well… Will Pirkle’s forum is dead ☹️

Moving on, **I deem the shape of the attack envelope presented here incorrect.** I have discussed the issue of exponential envelopes in [my complete envelope tutorial]({% post_url collections.posts, '2022-07-03-envelopes.md' %}).

Finally, there’s too much self-promotion in this book.

- “Check out in my other book”,
- “on the forum”,
- “SynthLab is flexible”, etc.,

are mostly unnecessary, in my opinion.

But maybe I’m wrong and I should introduce more self-promotion myself! Ok… so for the last point, let me say that if you want to learn more upsides and downsides of this book, [check out my review of Will Pirkle’s other book: *Designing Audio Effect Plugins in C++*]({% post_url collections.posts, '2023-08-30-designing-audio-effect-plugins-in-cpp-by-will-pirkle-book-review.md' %}) 😉 These two books have a lot of common qualities.

(For example, the sin of calling C++ classes “objects” is committed in both books).

## Should you read "Designing Software Synthesizer Plugins in C++"?

That leads me to the conclusion: should you read it?

My honest answer to this question is: no.

If you want to learn sound synthesis techniques, read other synth books like Martin Russ's *Sound Synthesis and Sampling* or Curtis Roads's *Computer Music Tutorial* (2nd edition has been published lately).

(Or follow [this blog’s synthesis section]({% link collections.all, 'sound-synthesis/index.html' %})).

They don’t provide you with C++ code but teach you very well the underlying principles which you can readily apply in your implementations. That’s how I started and that’s the best way to learn sound synthesis inside-out: learn the technique and then implement it.

## Final thoughts

To wrap up, let me share with you that although *Designing Software Synthesizer Plugins* promises a lot to the reader, it simply does not deliver. The book does teach you some synthesis principles but does not effectively teach you how to apply them. You’re probably better off reading books that focus more on sound synthesis techniques and implementing them.

But of course that’s just my opinion; if you read the book and you loved it, let me know in the comments! I’d love to be convinced otherwise 😉
