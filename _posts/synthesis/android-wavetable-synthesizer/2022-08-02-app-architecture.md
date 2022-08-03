---
title: "Android Synthesizer App Tutorial Part 1: App Architecture"
description: "A tutorial on building an Android wavetable synthesizer from scratch using Compose UI, Oboe library, and modern architecture guidelines."
date: 2022-08-02
author: Jan Wilczek
layout: post
permalink: /android-synthesizer-1-app-architecture/
images: /assets/img/posts/synthesis/android-wavetable-synthesizer
# background: /assets/img/posts/synthesis/2022-07-03-envelopes/sine_adsr.webp
# audio_examples: /assets/wav/posts/synthesis/2022-07-03-envelopes/
categories:
  - Sound Synthesis
tags:
  - android
  - wavetable
  - kotlin
  - C++
discussion_id: 2022-08-02-app-architecture
custom_js:
 - /assets/vendor/lazyload/lazyload.min.js
 - /assets/js/wolfsound/modules/load_lazyload.js
---
Built using Jetpack Compose, Oboe library, C++, Kotlin, and modern architecture guidelines.

{% capture _ %}{% increment figureId20220802  %}{% endcapture %}

<!-- TODO: Here there will be a table of contents -->

## Introduction

Recently, thanks to my employer [Loudly](https://www.loudly.com/), I went to droidcon Berlin 2022 and learned a lot about modern Android development. That is, "modern" as of 2022 😉

<!-- TODO: Me at Droidcon with Manuel Vivo -->

<div markdown="0">
<img class="lazyload" data-src="{{ page.images | absolute_url | append: "/JanWilczekAndManuelVivo.webp" }}" alt="Jan Wilczek and Manuel Vivo at droidcon Berlin 2022" width="60%">
</div>

_Figure {% increment figureId20220802 %}. At droidcon Berlin 2022, I was lucky to meet [Manuel Vivo](https://manuelvivo.dev/) of Google and listen to his talk on modern Android architecture. And I was happy to get some German pretzels too!_

Recent developments on this platform, especially, the brand-new Compose UI framework, inspired me to write a synthesizer app for Android.

What kind of synthesizer? [Wavetable synthesizer]({% post_url synthesis/2021-08-13-wavetable-synthesis-theory %}), of course!

We've built one in [Python]{% post_url synthesis/2021-08-27-wavetable-synthesis-python %}, another one in [Rust]({% post_url synthesis/2021-10-15-wavetable-synthesis-rust %}), and another one in [C++ as an audio plugin]({% post_url synthesis/2021-09-24-wavetable-synthesis-juce %}). So why not Android?

## Project Goal

The goal of the app is build a wavetable synthesizer on Android with basic controls. You can see them in the user interface (UI) of the app.

<!-- TODO: App UI -->
<div markdown="0">
<img class="lazyload" data-src="{{ page.images | absolute_url | append: "/SynthesizerUI.webp" }}" alt="Graphical user interface of the synthesizer app">
</div>

_Figure {% increment figureId20220802 %}. Graphical user interface of the synthesizer app we are going to build._

The secondary goal is to use cutting-edge Android audio tools and practices like

* [Kotlin programming language](https://kotlinlang.org/),
* [Jetpack Compose UI framework](https://developer.android.com/jetpack/compose),
* [Oboe audio library](https://github.com/google/oboe),
* and [modern Android architecture guidelines](https://developer.android.com/topic/architecture).

## What Will You Learn?

Thanks to this tutorial, you will learn

* How [wavetable synthesis]({% post_url synthesis/2021-08-13-wavetable-synthesis-theory %}) works can be implemented in an app,
* Kotlin basics in a fun and easy way, including [Kotlin Coroutines](https://kotlinlang.org/docs/coroutines-overview.html),
* Android development basics,
* Jetpack Compose framework basics,
* Interfacing Kotlin code with C++,
* Controlling audio output on Android,
* How to implement Android architecture guidelines.

## Who Is This Tutorial For?

This tutorial is for:

* Complete Android beginners who want to learn app development basics in an enjoyable way,
* People who want to learn [wavetable synthesis]({% post_url synthesis/2021-08-13-wavetable-synthesis-theory %}) and its implementation,
* Android developers who want to learn the audio side of Android apps,
* Kotlin developers who want to understand coroutines,
* Android developers who want to see modern Android architecture in action,
* Android developers who want to learn Jetpack Compose.
* C++ developers who want to learn how to interface with Android audio-wise and UI-wise.

## Full Source Code

The complete source code is available on [GitHub](https://github.com/JanWilczek/android-wavetable-synthesizer).

## App Architecture

<!-- TODO: Insert link to the next article in project setup -->
Before we start with the project setup, I want to discuss the architecture of our app.

How can one come up with architecture at the very beginning?

The answer is: one doesn't.

<!-- TODO: Boromir meme "One does not simply come up with software architecture at a project's start -->
<div markdown="0">
<img class="lazyload" data-src="{{ page.images | absolute_url | append: "/BoromirArchitectureMeme.webp" }}" alt="One does not simply fix architecture at project start">
</div>

_Figure {% increment figureId20220802 %}. Boromir knows what he's saying 😉._

The architecture is something that should be kind of a sketch in our minds or on paper that only guides us in the right direction.

To keep architecture flexible, I always try to follow advice from "Software Architecture" by Robert C. Martin and abstract out the details.

In practice, this means using interfaces when we're unsure how will implement certain functionalities.

So here I will show you the architecture of the app after I've finished it. The initial idea was similar but still different from the end product.

### Architecture Diagram

[Android architecture guidelines](https://developer.android.com/topic/architecture) encourage the developers to build their apps in layers.

<!-- TODO: Layers figure from the guidelines -->
<div markdown="0">
<img class="lazyload" data-src="{{ page.images | absolute_url | append: "/ModernAndroidArchitectureOverview.webp" }}" alt="Diagram of a generic architecture of an Android app as recommended by Google">
</div>

_Figure {% increment figureId20220802 %}. Officially recommended app architecture by Google ([source](https://developer.android.com/topic/architecture))._

In general, I prefer the [ports and adapters](https://en.wikipedia.org/wiki/Hexagonal_architecture_(software)) approach. As a result, our app is a mix of the two.

<!-- TODO: Wavetable synthesizer app architecture -->
<div markdown="0">
<img class="lazyload" data-src="{{ page.images | absolute_url | append: "/SynthesizerArchitecture.svg" }}" alt="Component diagram of the app">
</div>

_Figure {% increment figureId20220802 %}. Architecture of our wavetable synthesizer Android app._

We can observe that our app consists of 7 parts:

1. UI layer, which defines how our app will look.
2. ViewModel layer which holds the UI state (e.g., sliders' values) and communicates the changes to the `WavetableSynthesizer`.
3. A very small and very "dirty" (i.e., concrete, non-abstract) `MainActivity` to connect to Android ecosystem, initialize the app, and connect everything.
4. Kotlin-side wavetable synthesizer representation, which can be a gateway to the native C++ synthesizer or a dummy class for testing purposes.
5. Java Native Interface (JNI) code that allows interfacing Kotlin and C++.
6. C++-side wavetable synthesizer that contains actual business logic regarding the synthesizer. `WavetableSynthesizer` C++ class delegates its functionalities to a handful of smaller classes that aren't shown in the diagram.
7. Sound playback layer that is conveniently abstracted behind an interface so that it can be easily replaced in the future. In our app, we will implement the `AudioPlayer` interface using the Oboe library from Google.

Actually, this architecture could be used for any synthesizer that doesn't use keys or MIDI. For example, with more sliders, we could build a frequency modulation (FM) synthesizer. But let's leave that for another occasion! 😉

## Tech Stack

Finally, I want to list all the tools and libraries that I'm using with their respective versions.

* Android Studio Chipmunk 2021.2.1 Patch 1
* CMake 3.18.1
* Jetpack Compose 1.1.1
* Kotlin 1.8.0
* C++ 20
* Oboe 1.6.1

The remaining dependencies can be found in the [_build.gradle_ file](https://github.com/JanWilczek/android-wavetable-synthesizer/blob/main/app/build.gradle).

## Part 1 Summary

In this introductory part of the tutorial, we discussed the goals of the project and the architecture of our app. Following this tutorial in full or in parts will allow you to learn a handful of modern technologies in an easy and enjoyable way. You can code it yourself or you can download the source code from GitHub. Have fun!

If you want to check out my guidelines on what knowledge is needed to write sound-processing software, [download my free audio plugin developer checklist]({% link single-pages/checklist.html %}).

Up next: implementing the UI in Jetpack Compose!



