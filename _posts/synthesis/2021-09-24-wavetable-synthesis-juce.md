---
title: "Wavetable Synth in JUCE C++ Framework Tutorial"
description: Learn how to code your own wavetable synthesizer in JUCE C++ framework in one article.
date: 2021-09-24
author: Jan Wilczek
layout: post
permalink: /sound-synthesis/wavetable-synth-in-juce/
images: assets/img/posts/synthesis/2021-09-24-wavetable-synthesis-juce
# background: /assets/img/posts/synthesis/2021-08-27-wavetable-synthesis-python/Thumbnail.png
categories:
 - Sound Synthesis
tags:
 - synthesis
 - wavetable
 - JUCE
 - C++
discussion_id: 2021-09-24-wavetable-synthesis-juce
---
Let's write a wavetable synthesizer in JUCE C++ framework!

In previous articles, I explained [how wavetable synthesis algorithm works]({% post_url synthesis/2021-08-13-wavetable-synthesis-theory %}) and showed [an implementation of it in Python]({% post_url synthesis/2021-08-27-wavetable-synthesis-python %}). Now is the time to write a wavetable synth in C++!

*Note: The article presents only code written by me. For the full, operational project, [see the related repository on GitHub](https://github.com/JanWilczek/wavetable-synth).*

*Note: I am using JUCE v6.0.5.*

*Note: The purpose of the presented code is __educational__. Please, don't complain that the Single Responsibility Principle (SRP) and other object-oriented programming (OOP) rules are violated. Thanks! 😎*

## What is JUCE?

The [JUCE framework](https://juce.com/) is a C++-based framework for developing audio-related software. It is currently the easiest way to build your own digital audio workstation (DAW) plug-ins. That is why a lot of companies include familiarity with JUCE as one of the nice-to-have for audio developer positions. JUCE is free for personal use, which makes it perfect for our goal of developing a C++ wavetable synthesizer!

To understand this article, you only need to know 1 thing about JUCE.

![]({{ page.images | absolute_url | append: "/InceptionJUCEMeme.jpg" }}){: alt="There is 1 thing you need to know about JUCE meme." width="600px" }

Plug-ins built with JUCE consist of two parts:

1. A `PluginEditor`.
1. A `Plugin Processor`.

`PluginEditor` object is responsible for the graphical user interface (GUI) elements. We won't need it for our implementation (yes, you can build a sound synthesizer without a GUI!).

`PluginProcessor` object is concerned with audio processing. More specifically, **the processor connects our processing code with the platform it is running on**. If we are building a VST plug-in, the processor will connect all necessary inputs and output so that we can use the plug-in in a DAW.

`PluginProcessor` has two member functions that we will need:

1. `void prepareToPlay (double sampleRate, int samplesPerBlock)` enables us to configure our synthesizer after plug-in start or after a major settings change, e.g., after changing audio device settings.
1. `void processBlock (juce::AudioBuffer<float>&, juce::MidiBuffer&)` contains the audio processing code that a developer using JUCE should write. `AudioBuffer` object contains audio samples of the current block and `MidiBuffer` object contain MIDI events that happened during that block.

If you don't know what an audio block is, [check out this short paragraph]({% post_url 2021-05-14-fast-convolution %}#block-based-convolution).

**All we need to do is fill two above member functions.**

How do we go about it?

## The Goal

We want to build a sine wavetable synthesizer that is polyphonic (can play multiple tones at once). We will need a plug-in that has a MIDI input, a MIDI output, and an audio output.

## Project Setup in Projucer

JUCE uses Projucer to set up the projects. From the templates I have chosen "Plugin -> Basic".

Then, taking into consideration our specification above, I selected the following options:
* Plugin is a Synth,
* Plugin MIDI Input, and
* Plugin MIDI Output.

I am using Visual Studio, so I generated a solution for Visual Studio 2019; you can go with the IDE you normally use for C++ development. After compilation, the built VST3 plug-in can be imported to a DAW of choice or JUCE's AudioPluginHost.

After opening the project in the IDE you should have source files related to `PluginEditor` and `PluginProcessor`. Eventually, we will just slightly modify the `PluginProcessor` class (*PluginProcessor.cpp* file).

And that's it when it comes to JUCE project setup!

## The WavetableSynth class


We start building our synthesizer by creating `WavetableSynth` class. It will contain the interface to our synthesizer that will be called from within `processBlock()`. Thus, we will follow the top-down approach.

Here are the contents of the *WavetableSynth.h* header file:

_Listing 1. WavetableSynth.h._
```cpp
#pragma once
#include <JuceHeader.h>

#include "WavetableOscillator.h"

class WavetableSynth
{
public:
	void prepareToPlay(double sampleRate, int samplesPerBlock); // [1]
	void processBlock(juce::AudioBuffer<float>& buffer, juce::MidiBuffer& midiMessages);  // [2]

private:
	static std::vector<float> generateSineWaveTable();  // [3]
	void initializeOscillators();  // [4]
	void handleMidiEvent(const juce::MidiMessage& midiMessage);  // [5]
	void render(juce::AudioBuffer<float>& buffer, int beginSample, int endSample);  // [6]

	double sampleRate;
	int samplesPerBlock;
	std::vector<WavetableOscillator> oscillators;  // [7]
};
```

Below are the explanations of the particular functions.

Public interface:
[1] `prepareToPlay()` sets the initial parameters for processing (analogously to `prepareToPlay()` from `PluginProcessor`).
[2] `processBlock()` is called from within `PluginProcessor`'s `processBlock()`.

All other member functions serve only to help in the processing.

[3] `generateSineWaveTable()` generates 64 samples of a sine wave period.
[4] `initializeOscillators()` initializes 200 oscillators as wave table oscillators.
[5] `handleMidiEvent()`, well, handles a MIDI event 😉. It translates a MIDI message to synthesizer's parameters change.
[6] `render()` generates samples in the [`beginSample`, `endSample`) range (Standard Template Library-style ranges).
[7] A `vector` of `oscillators` contains all oscillators created by `initializeOscillators()`. To these oscillators particular notes to be played are assigned.

Note that `WavetableSynth` is default-constructed.
