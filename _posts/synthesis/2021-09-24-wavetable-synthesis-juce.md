---
title: "Wavetable Synth Plugin in JUCE C++ Framework Tutorial"
description: Learn how to code your own wavetable synthesizer plugin in JUCE C++ framework in one article.
date: 2021-09-24
author: Jan Wilczek
layout: post
permalink: /sound-synthesis/wavetable-synth-plugin-in-juce/
images: assets/img/posts/synthesis/2021-09-24-wavetable-synthesis-juce
background: /assets/img/posts/synthesis/2021-09-24-wavetable-synthesis-juce/Thumbnail.png
categories:
 - Sound Synthesis
tags:
 - wavetable
 - juce
 - cpp
discussion_id: 2021-09-24-wavetable-synthesis-juce
---
Let's write a wavetable synthesizer in JUCE C++ framework!

<iframe width="560" height="315" src="https://www.youtube.com/embed/Ah4P-zOfdYc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>



In previous articles, I explained [how wavetable synthesis algorithm works]({% post_url collections.posts, 'synthesis/2021-08-13-wavetable-synthesis-theory' %}) and showed [an implementation of it in Python]({% post_url collections.posts, 'synthesis/2021-08-27-wavetable-synthesis-python' %}). Now is the time to write a real-time wavetable synth in C++!

*Note: The article presents only code written by me. For the full, operational project, [see the related repository on GitHub](https://github.com/JanWilczek/wavetable-synth).*

*Note: I am using JUCE v6.0.5.*

*Note: The purpose of the presented code is __educational__. Please, don't complain that the Single Responsibility Principle (SRP) and other object-oriented programming (OOP) rules are violated. Thanks!* 😎

## What is JUCE?

The [JUCE framework](https://juce.com/) is a C++-based framework for developing audio-related software. It is currently the easiest way to build your own digital audio workstation (DAW) plugins and other audio-related software. That is why, a lot of companies include familiarity with JUCE as one of the nice-to-haves for audio developer positions. 

JUCE is free for personal use, which makes it perfect for our goal of developing a C++ wavetable synthesizer!

To understand this article, you only need to know 1 thing about JUCE.

![]({{ images | absolute_url | append: "/InceptionJUCEMeme.jpg" }}){: alt="There is 1 thing you need to know about JUCE meme." width="600px" }

Plugins built with JUCE consist of two parts:

1. A `PluginEditor`.
1. A `Plugin Processor`.

`PluginEditor` object is responsible for the graphical user interface (GUI) elements. We won't need it for our implementation (yes, you can build a sound synthesizer without a GUI!).

`PluginProcessor` object is concerned with audio processing. More specifically, **the processor connects our processing code with the platform it is running on**. If we are building a VST plugin, the processor will connect all necessary inputs and outputs so that we can use the plugin in a DAW.

`PluginProcessor` has two member functions that we will need:

1. `void prepareToPlay (double sampleRate, int samplesPerBlock)` enables us to configure our synthesizer after plugin start or after a major settings change, e.g., after changing the audio device settings.
1. `void processBlock (juce::AudioBuffer<float>&, juce::MidiBuffer&)` contains the audio processing code that a developer using JUCE should write. `AudioBuffer` object contains audio samples of the current block and `MidiBuffer` object contains MIDI events that happened during that block.

If you don't know what an audio block is, [check out this short paragraph]({% post_url collections.posts, '2021-05-14-fast-convolution' %}#block-based-convolution).

**All we need to do is fill two above member functions.**

How do we go about it?

## The Goal

We want to build a sine wavetable synthesizer that is polyphonic (can play multiple tones at once). We will need a plugin that has a MIDI input, a MIDI output, and an audio output.

## Project Setup in Projucer

JUCE uses Projucer to set up the projects. From the templates, I chose *Plugin -> Basic*.

Then, taking into the consideration our specification above, I selected the following options:
* Plugin is a Synth,
* Plugin MIDI Input, and
* Plugin MIDI Output.

I am using Visual Studio, so I generated a solution for Visual Studio 2019; you can go with the IDE you normally use for C++ development.

After compilation, the built plugin can be imported to a DAW of choice or JUCE's AudioPluginHost.

After opening the project in the IDE, you should see the source files related to `PluginEditor` and `PluginProcessor`. Eventually, we will just slightly modify the `PluginProcessor` class (*PluginProcessor.cpp* file).

And that's it for the JUCE project setup!

## The WavetableSynth class

We start building our synthesizer by creating the `WavetableSynth` class. It will contain the interface to our synthesizer that will be called from within `processBlock()`. Thus, we will follow the top-down approach.

Here are the contents of the *WavetableSynth.h* header file:

_Listing 1. WavetableSynth.h._
```cpp
#pragma once
#include <JuceHeader.h>

#include "WavetableOscillator.h"

class WavetableSynth
{
public:
   void prepareToPlay(double sampleRate); // [1]
   void processBlock(juce::AudioBuffer<float>& buffer, juce::MidiBuffer& midiMessages);  // [2]

private:
   static std::vector<float> generateSineWaveTable();  // [3]    
   static float midiNoteNumberToFrequency(int midiNoteNumber);  // [3.5]
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

[1] `prepareToPlay()` sets the sample rate for processing (analogously to `prepareToPlay()` from `PluginProcessor`).

[2] `processBlock()` is called from within `PluginProcessor`'s `processBlock()`.

All other member functions serve only to help in the processing.

[3] `generateSineWaveTable()` generates 64 samples of a sine wave period.

[3.5] `midiNoteNumberToFrequency()` converts a MIDI note number (an integer corresponding to a key on a MIDI keyboard) to frequency in Hz (assuming a certain tuning of the piano).

[4] `initializeOscillators()` initializes 128 oscillators as wave table oscillators.

[5] `handleMidiEvent()`, well, handles a MIDI event 😉. It translates a MIDI message to the synthesizer's parameters change.

[6] `render()` generates samples in the [`beginSample`, `endSample`) range (Standard Template Library-style range).

[7] A `vector` of `oscillators` contains all oscillators created by `initializeOscillators()`. To these oscillators, particular notes are assigned.

Note that `WavetableSynth` is default-constructed.

## Prepare To Play

Let's implement how our synthesizer will learn about the environment it works in.

_Listing 2. WavetableSynth.cpp: prepareToPlay()._
```cpp
void WavetableSynth::prepareToPlay(double sampleRate)
{
    this->sampleRate = sampleRate;

    initializeOscillators();
}
```
We store the sample rate and initialize the oscillators.

### Oscillator Initialization

_Listing 3. WavetableSynth.cpp: initializeOscillators()._
```cpp
void WavetableSynth::initializeOscillators()
{
   oscillators.clear(); // [1]
   constexpr auto OSCILLATOR_COUNT = 128;
   const auto sineWaveTable = generateSineWaveTable(); // [2]

   for (auto i = 0; i < OSCILLATOR_COUNT; ++i)   // [3]
   {
      oscillators.emplace_back(sineWaveTable, sampleRate); // [4]
   }
}
```

Oscillator initialization consists of

1. clearing the `oscillators` vector [1] (it could be nonempty if the change in parameters happened during processing),
1. generating the sine wave table [2],
1. and instantiating the oscillators [3].

Here the number of oscillators created (128) is the number of possible MIDI note number values. This number could also be specified by the user, but I decided to fix it for simplicity.

Oscillators are instances of `WavetableOscillator`. `WavetableOscillator` produces samples by looping over the wavetable. To this end, it needs the sample rate information, the wave table to loop over, and, eventually, (at run time) the frequency it should play. We pass the first two to the constructor of `WavetableOscillator` ([4] in Listing 3).

### Sine Wave Table Generation

Generating the sine wave table is quite straightforward.

_Listing 4. WavetableSynth.cpp: generateSineWaveTable()._
```cpp
std::vector<float> WavetableSynth::generateSineWaveTable()
{
   constexpr auto WAVETABLE_LENGTH = 64;
   const auto PI = std::atanf(1.f) * 4;
   std::vector<float> sineWaveTable = std::vector<float>(WAVETABLE_LENGTH);

   for (auto i = 0; i < WAVETABLE_LENGTH; ++i)
   {
      sineWaveTable[i] = std::sinf(2 * PI * static_cast<float>(i) / WAVETABLE_LENGTH);
   }

    return sineWaveTable;
}
```

The length of the wave table (64) could be a parameter, but I decided to fix it for simplicity.

In `generateSineWaveTable()` we create a vector of a fixed length and fill it with samples of one period of the sine. Sine's period is $2\pi$ so we increase the phase linearly from 0 to $2\pi - \frac{2\pi}{64}$.

### Connection to PluginProcessor

To connect our `WavetableSynth` with `PluginProcessor`, we create a member variable in `PluginProcessor`.

_Listing 5. PluginProcessor.h: synth member variable._
```cpp
class WavetableSynthAudioProcessor  : public juce::AudioProcessor
{
//...
private:
    WavetableSynth synth;
//...
};
```

`synth` will be default-initialized.

We now can implement `PluginProcessor`'s `prepareToPlay()`:

_Listing 6. PluginProcessor.cpp: prepareToPlay()._
```cpp
void WavetableSynthAudioProcessor::prepareToPlay (double sampleRate, int)
{
    synth.prepareToPlay(sampleRate);
}
```

We are prepared to play! Before we write the processing code, let's implement `WavetableOscillator` so that it is capable of producing samples.

## WavetableOscillator

Here is the full interface of `WavetableOscillator`:

_Listing 7. WavetableOscillator.h._
```cpp
#pragma once
#include <vector>

class WavetableOscillator
{
public:
   WavetableOscillator(std::vector<float> waveTable, double sampleRate); // [1]
   WavetableOscillator(const WavetableOscillator&) = delete; // [2]
   WavetableOscillator& operator=(const WavetableOscillator&) = delete; // [2]
   WavetableOscillator(WavetableOscillator&&) = default; // [3]
   WavetableOscillator& operator=(WavetableOscillator&&) = default; //[3]

   float getSample();   // [4]
   void setFrequency(float frequency);   // [5]
   void stop();   // [6]
   bool isPlaying() const;   // [7]

private:
   float interpolateLinearly() const;   // [8]

   float index = 0.f;   // [9]
   float indexIncrement = 0.f;   // [10]
   std::vector<float> waveTable;    //  [11]
   double sampleRate;   //  [12]
};
```

Let's quickly cover what's involved here.

The constructor [1] takes the `waveTable` and the `samplingRate` and stores them in member variables `waveTable` [11] and `sampleRate` [12] respectively using an initializer list.

_Listing 8. WavetableOscillator.cpp: constructor._
```cpp
WavetableOscillator::WavetableOscillator(std::vector<float> waveTable, double sampleRate)
: waveTable{ std::move(waveTable) },
   sampleRate{ sampleRate }
{}
```

Copying oscillators means copying wave tables; it may be expensive. In order to prevent from accidentally copying an oscillator, I declared their copy constructor and copy assignment operator as `delete`d [2].

Specifying one of the constructors prevents the default generation of other constructors. I want to be able to `std::move` my oscillators so I marked the move constructor and the move assignment operator to be `default`-generated by the compiler [3].

### Wave Table Looping

`getSample()` [4] should return 1 sample of the oscillator and advance the `index` member variable [9] by `indexIncrement` member variable [10] which is frequency-dependent. This is the core of the wavetable synthesis algorithm; as a reminder I put it here again:

![]({{ "assets/img/posts/synthesis/2021-08-13-wavetable-synthesis-theory/wavetable-synthesis-algorithm-diagram.png" | absolute_url }}){: alt="A DSP diagram of the wavetable synthesis algorithm" }
_Figure 1. A diagram of the wavetable synthesis algorithm using index increment. After [F. Richard Moore, Elements of Computer Music, Prentice Hall 1990](https://www.amazon.com/gp/product/0132525526/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0132525526&linkCode=as2&tag=wolfsound05-20&linkId=71285ec31668f2e8d8cf81094ff51f5f)._

The implementation looks as follows:

_Listing 9. WavetableOscillator.cpp: getSample()._
```cpp
float WavetableOscillator::getSample()
{
   jassert(isPlaying());
   index = std::fmod(index, static_cast<float>(waveTable.size()));
   const auto sample = interpolateLinearly();
   index += indexIncrement;
   return sample;
}
```

To enforce the invariant that only an active oscillator will have its `getSample()` member function called, I have added an assertion that it `isPlaying()`.

The next step is to bring the `index` into the range of wave table indices using `std::fmod`. `std::fmod` returns the floating-point remainder of a division and, thus, keeps the `index` within the [0, `waveTable.size()`) range.

Afterwards, we perform a linear interpolation of wave table values to get the output sample.

Only then do we increment the index; otherwise, we would never start playing a note with `index` equal to 0 (we would always start looping at `indexIncrement`).

Then we return the generated sample.

The DSP diagram is bigger than the code 😏.

### Setting the Frequency

`setFrequency()` [5] implements Equation 9 from [the wave table theory article]({% post_url collections.posts, 'synthesis/2021-08-13-wavetable-synthesis-theory' %}).

_Listing 10. WavetableOscillator.cpp: setFrequency()._
```cpp
void WavetableOscillator::setFrequency(float frequency)
{
   indexIncrement = frequency * static_cast<float>(waveTable.size()) 
                                        / static_cast<float>(sampleRate);
}
```

Casting is necessary, because `vector`'s `size_type` is implementation-dependent and `sampleRate` is a `double`.

This implementation of `setFrequency()` allows continuous frequency changes on a sample-by-sample basis.

### Stopping the Oscillator

`stop()` [6] resets the `index` and the `indexIncrement` to 0, making further looping impossible.

_Listing 11. WavetableOscillator.cpp: stop()._
```cpp
void WavetableOscillator::stop()
{
   index = 0.f;
   indexIncrement = 0.f;
}
```

We can query if the oscillator is producing samples with `isPlaying()` [7].

_Listing 12. WavetableOscillator.cpp: isPlaying()._
```cpp
bool WavetableOscillator::isPlaying() const
{
   return indexIncrement != 0.f;
}
```

Obviously, if `indexIncrement` is 0, we cannot move forward in wave table looping so the oscillator is not playing.

### Linear Interpolation

Finally, we need to linearly interpolate between the values in the wave table [8]. This should be delegated to a different class (because an oscillator is not an interpolator) but for simplicity and brevity, I put the interpolation functionality in the `WavetableOscillator` class. 

This member function does not alter any member variables so it can be `const`.

_Listing 13. WavetableOscillator.cpp: interpolateLinearly()._
```cpp
float WavetableOscillator::interpolateLinearly() const
{
    const auto truncatedIndex = static_cast<typename  decltype(waveTable)::size_type>(index);
    const auto nextIndex = static_cast<typename  decltype(waveTable)::size_type>
                                                    (std::ceil(index)) % waveTable.size();
    const auto nextIndexWeight = index - static_cast<float>(truncatedIndex);
    return waveTable[nextIndex] * nextIndexWeight + 
                            (1.f - nextIndexWeight) * waveTable[truncatedIndex];
}
```

* `truncatedIndex` is the largest integer index not larger than `index`.

* `nextIndex` is the smallest integer index larger than `index` or 0 if `truncatedIndex` is equal to `waveTable.size() - 1`.

* `nextIndexWeight` is the weight we put on `waveTable[nextIndex]` in the returned sum.

In linear interpolation, we want to return `a * waveTable[truncatedIndex] + b * waveTable[nextIndex]`, where `a + b == 1`. Additionally, we fix the ratio `b / a` to be equal to the ratio `(index - truncatedIndex) / (nextIndex - index)` (apart from the edge case where `nextIndex` is 0). 

For example, if `index` is nearer to `nextIndex` than to `truncatedIndex`, `b` should be larger than `a` so that the returned value is closer to `waveTable[nextIndex]`. 

Since the samples lie at integer indices, the distance between successive samples is 1 (conceptually also between the last index in the wave table and the first). So we can simply use distances of `index` to neighboring indices as weights, because these distances sum to 1.

At the end, we return the neighboring samples in the wave table multiplied by their corresponding weights.

*Note: I am sorry for the explicit casts but they are really important. Please, learn from my mistakes...* 😉

## Actual Processing Code

After implementing the `WavetableOscillator`, we can implement the two remaining member functions of `WavetableSynth`. Let's start with `processBlock()`.

_Listing 14. WavetableSynth.cpp: processBlock()._
```cpp
void WavetableSynth::processBlock(juce::AudioBuffer<float>& buffer, 
                                  juce::MidiBuffer& midiMessages)
{
    auto currentSample = 0;

    for (const auto midiMetadata : midiMessages)
    {
        const auto message = midiMetadata.getMessage();
        const auto messagePosition = static_cast<int>(message.getTimeStamp());

        render(buffer, currentSample, messagePosition);
        currentSample = messagePosition;
        handleMidiEvent(message);
    }

    render(buffer, currentSample, buffer.getNumSamples());
}
```

Processing amounts to simply reading out available MIDI messages, acting on them, and rendering sound in between. 

Between adjacent MIDI messages, no synthesizer parameters are changed (we have no GUI) so the rendering environment stays constant and we can simply render all the samples in that interval.

## Sound Rendering

Sound rendering means iterating over active oscillators and retrieving samples from them.

_Listing 15. WavetableSynth.cpp: render()._
```cpp
void WavetableSynth::render(juce::AudioBuffer<float>& buffer, 
                            int beginSample, int endSample)
{
    auto* firstChannel = buffer.getWritePointer(0);
    for (auto& oscillator : oscillators)
    {
        if (oscillator.isPlaying())
        {
            for (auto sample = beginSample; sample < endSample; ++sample)
            {
                firstChannel[sample] += oscillator.getSample();
            }
        }
    }

    for (int channel = 1; channel < buffer.getNumChannels(); ++channel)
    {
        auto* channelData = buffer.getWritePointer(channel);
        std::copy(firstChannel + beginSample, 
            firstChannel + endSample, 
            channelData + beginSample);
    }
}
```

We render the samples to the first channel only (which we assume is empty before the processing). We do that only in the specified interval.

Note that we *add samples* instead of assigning them. This gives us polyphony (multiple oscillators playing at once).

Afterwards, we copy the contents of that channel to all other channels.

## Note Dispatching

The last function to implement for `WavetableSynth` is handling MIDI events:

_Listing 16. WavetableSynth.cpp: handleMidiEvent()._
```cpp
void WavetableSynth::handleMidiEvent(const juce::MidiMessage& midiMessage)
{
    if (midiMessage.isNoteOn())
    {
        const auto oscillatorId = midiMessage.getNoteNumber();
        const auto frequency = midiNoteNumberToFrequency(oscillatorId);
        oscillators[oscillatorId].setFrequency(frequency);
    }
    else if (midiMessage.isNoteOff())
    {
        const auto oscillatorId = midiMessage.getNoteNumber();
        oscillators[oscillatorId].stop();
    }
    else if (midiMessage.isAllNotesOff())
    {
        for (auto& oscillator : oscillators)
        {
            oscillator.stop();
        }
    }
}
```

Here, we check for "interesting" MIDI message types and act on them.

If a key was pressed ("note on"), we convert its number to frequency in Hz and inform the oscillator under that number that it should start playing by setting its frequency.

If a key was released ("note off"), we stop the oscillator responsible for that key.

If an "all notes off" message was issued, we stop all oscillators. Such messages are more likely to be present in MIDI files rather than during live performances.

### How to Convert a MIDI Note Number to Frequency?

A MIDI note number takes a value from the [0, 127] integer range. Number 69 corresponds to the A4 note in the scientific pitch notation. In modern-day music, A4 is most often tuned to have a fundamental frequency of 440 Hz [Müller2015].

A formula for converting a MIDI note number $p$ to frequency $f$ is

$$f(p) = 440 \cdot 2^{(p - 69) / 12}. \quad (1)$$

Here, 440 is the tuning we chose for the A4 note in Hz. 69 is the MIDI note number of A4 on the keyboard. 12 is the number of notes in an octave (from C to B).

In code, it looks as follows:

_Listing 17. WavetableSynth.cpp: midiNoteNumberToFrequency()._
```cpp
float WavetableSynth::midiNoteNumberToFrequency(const int midiNoteNumber)
{
    constexpr auto A4_FREQUENCY = 440.f;
    constexpr auto A4_NOTE_NUMBER = 69.f;
    constexpr auto NOTES_IN_AN_OCTAVE = 12.f;
    return A4_FREQUENCY * 
            std::powf(2, 
                (static_cast<float>(midiNoteNumber) - A4_NOTE_NUMBER) / NOTES_IN_AN_OCTAVE);
}
```

`float`s instead of `int`s enable floating-point division.

## Plugging Processing into the Processor

To wrap up the implementation, we need to connect our `WavetableSynth`'s `processBlock()` with `PluginProcessor`'s `processBlock()`.

_Listing 18. PluginProcessor.cpp: processBlock()._
```cpp
void WavetableSynthAudioProcessor::processBlock (juce::AudioBuffer<float>& buffer, 
                                                 juce::MidiBuffer& midiMessages)
{
    juce::ScopedNoDenormals noDenormals;

    for (auto i = 0; i < buffer.getNumChannels(); ++i)
        buffer.clear(i, 0, buffer.getNumSamples());

    synth.processBlock(buffer, midiMessages);
}
```

First, we clean the channels by setting all samples to 0. In this way, we make sure that there is no garbage in them.

Then we call the `processBlock()` member function of `WavetableSynth` passing it the audio buffer and MIDI messages.

## Launching the Synthesizer Plugin

That's it! We successfully implemented the plugin.

After compilation, you can import it in a digital audio workstation of your choice or the JUCE's AudioPluginHost.

One thing you will hear instantly after playing some notes is that there are audible clicks when you press or release a key. That is because we didn't implement a fade-in nor a fade-out amplitude envelope. But that could be a topic of another article 😉

## Summary

In this article, we implemented a wavetable synthesizer plugin in the JUCE C++ framework. If you have any questions or comments, don't hesitate to write them below!

If you would like to see a wavetable synthesis implementation in other programming languages, I have [one in Python]({% post_url collections.posts, 'synthesis/2021-08-27-wavetable-synthesis-python' %}) and [one in Rust]({% post_url collections.posts, 'synthesis/2021-10-15-wavetable-synthesis-rust' %}) as well. Make sure to check them out!

## Bibliography

Here is a list of useful references for the topic:

[My article on how wavetable synthesis algorithm works]({% post_url collections.posts, 'synthesis/2021-08-13-wavetable-synthesis-theory' %}).

[Repository for this article containing the full code and source files](https://github.com/JanWilczek/wavetable-synth)

[JUCE] [JUCE C++ framework](https://juce.com/).

[Müller2015] [Meinard Müller, *Fundamentals of Music Processing*, Springer International Publishing Switzerland 2015](https://amzn.to/39vzWqR) (link leads to an updated, 2021 edition of the book).

[MIDI] [MIDI Standard Specification, retrieved 24.09.2021](https://www.midi.org/specifications).

{% include 'affiliate-disclaimer.html' %}


