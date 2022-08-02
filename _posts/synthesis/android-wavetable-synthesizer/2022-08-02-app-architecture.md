---
title: "Android Synthesizer App Tutorial Part 1: App Architecture"
description: "A tutorial on building an Android wavetable synthesizer from scratch using Compose UI, Oboe library, and modern architecture guidelines."
date: 2022-08-02
author: Jan Wilczek
layout: post
permalink: /android-synthesizer-1-app-architecture/
# images: /assets/img/posts/synthesis/2022-07-03-envelopes/
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
---
Built using Jetpack Compose, Oboe library, C++, Kotlin, and modern architecture guidelines.

## Introduction

Recently, thanks to my employer [Loudly](https://www.loudly.com/), I went to droidcon Berlin 2022 and learned a lot about modern Android development. That is, "modern" as of 2022 😉

<!-- TODO: Me at Droidcon with Manuel Vivo -->

Recent developments on this platform, especially, the brand-new Compose UI framework, inspired me to write a synthesizer app for Android.

What kind of synthesizer? [Wavetable synthesizer]({% post_url synthesis/2021-08-13-wavetable-synthesis-theory %}), of course!

We've built one in [Python]{% post_url synthesis/2021-08-27-wavetable-synthesis-python.md %}, another one in [Rust]({% post_url synthesis/2021-10-15-wavetable-synthesis-rust.md %}), and another one in [C++ as an audio plugin]({% post_url synthesis/2021-09-24-wavetable-synthesis-juce %}). So why not Android?

## Project Goal

The goal of the app is build a wavetable synthesizer on Android with the following controls.

<!-- TODO: App UI -->

The secondary goal is to use cutting-edge Android audio tools and practices like

* [Kotlin programming language](https://kotlinlang.org/),
* [Jetpack Compose UI framework](https://developer.android.com/jetpack/compose),
* [Oboe audio library](https://github.com/google/oboe),
* and [modern Android architecture guidelines](https://developer.android.com/topic/architecture).

## What Will You Learn?

Thanks to this tutorial, you will learn

* Kotlin basics in a fun and easy way, including [Kotlin Coroutines](https://kotlinlang.org/docs/coroutines-overview.html),
* Android development basics,
* Jetpack Compose framework basics,
* Interfacing Kotlin code with C++,
* Controlling audio output on Android,
* How to implement Android architecture guidelines.

## Who Is This Tutorial For?

This tutorial is for:

* Complete Android beginners who want to learn app development basics in an enjoyable way,
* Android developers who want to learn the audio side of Android apps,
* Kotlin developers who want to understand coroutines,
* Android developers who want to see modern Android architecture in action,
* Android developers who want to learn Jetpack Compose.
* C++ developers who want to learn how to interface with Android audio-wise and UI-wise.

## Full Source Code

The complete source code is available on [GitHub](https://github.com/JanWilczek/android-wavetable-synthesizer).

## App Architecture