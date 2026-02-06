---
title: "Don't use AI for audio programming"
description: "Without proper knowledge and experience, AI can make your audio plugin glitch, or even cause your users to go deaf. Read the article to find how AI may negatively impact audio code."
date: 2026-01-14
author: Jan Wilczek
layout: post
permalink: /dont-use-ai-for-audio-programming/
background: /assets/img/posts/programming-in-general/2026-01-14-dont-use-ai-for-audio-programming/Thumbnail.webp
categories:
  - Programming In General
tags:
  - ai
  - learning
  - research
discussion_id: 2026-01-14-dont-use-ai-for-audio-programming
---
Are you using AI for audio programming? You may go deaf.

{% include 'youtube-video', video_id: '7SuZO5FQCwM' %}

{% capture _ %}{% increment figureId20250114  %}{% endcapture %}
{% capture _ %}{% increment listingId20250114  %}{% endcapture %}

At the Audio Developer Conference 2025 last November, one topic dominated the conversation: AI and its applications in audio programming.

I’ve asked a few senior programmers I deeply admire whether they use AI. I’ve also talked to a few junior developers, some of whom are students of my [DSP Pro](https://www.wolfsoundacademy.com/dsp?utm_source=dont-use-ai-article&utm_medium=blog) or [JUCE](https://www.wolfsoundacademy.com/juce?utm_source=dont-use-ai-article&utm_medium=blog) courses. Finally, I reviewed the latest research on AI usage in programming.

All of these investigations converged in a single conclusion: don’t use AI for audio programming if you’re a beginner.

And even if you’re not, think twice before using AI.

Before I explain my point of view, let me share with you a quick story.

## AI can make your speakers explode

A friend of my friend is a musician, and they wanted to create a sound synthesizer plugin for their live performance.

Since they didn’t know programming, they decided to vibe-code the whole thing.

(If you don’t know what **vibe coding** is, it’s prompting AI to generate code until you are satisfied with the result. In theory, you don’t have to write any code yourself).

Once they tested the software locally, they were happy to bring it to the stage. The initial checks went well, and so the musician was excited for the concert to start. 

But once they started playing to the audience, they noticed that something was off. They were getting constant static in the speakers. The static was getting louder and louder, until eventually, when the musician played a crescendo, the speakers exploded leaving most of the attendees with impaired hearing.

{% image "assets/img/posts/programming-in-general/2026-01-14-dont-use-ai-for-audio-programming/Boomm.png", "comic book boom depiction"  %}

Is this story true? No. At least not yet. But there’s a high chance that it will be true soon. And here’s why.

## What is audio programming?

If you’re new to this blog, you can find here resources to learn audio programming; the science and art of writing code that processes sound.

Digital (audio) signal processing (DSP) is the theory behind audio programming, much like Algorithms and Data Structures are the theory behind general-purpose programming.

If you have ever used any music-related tools on a computer or smartphone, you have used audio software. I teach others how to write such software.

Good examples are digital audio workstations (DAWs) and the audio plugins they run. For this discussion, it’s helpful to note that these two types of software (as well as many others) can be created using the JUCE C++ framework, which is the tool most audio plugin developers use. At the same time, there are many other tools you can use for this purpose.

Audio programming is a complicated topic. But it is a topic that **anyone** can learn.

For example, you can go through [the official JUCE audio plugin development course available for free.](https://www.wolfsoundacademy.com/juce?utm_source=dont-use-ai-article&utm_medium=blog)

As a teacher, I see that **all** beginners use AI code generation or vibe coding for audio, even though they’re exactly the ones who should not be doing it, because they are harming themselves, and they can easily harm others.

Let me tell you how.

## Assumptions for this discussion

Let’s leave ethical considerations of large language models (LLMs, the technology behind ChatGPT, Claude, Gemini, and others) aside; let’s pretend they do not infringe anyone’s copyrights, are trained only on data willingly provided for this purpose, and do not burden the environment.

Why not use them for audio programming?

I start by discussing how you can hurt others with AI audio coding, and then proceed to how you can hurt yourself with it.

## AI often fails to generate real-time-safe code or correct DSP code

**Real-time-safe programming** is a constraint most audio developers face. To play back sound, your computer’s sound device queries your application for a block of samples at regular time intervals.

If you don’t supply the block within the prescribed deadline, you get a glitch.

A glitch can break your speakers or leave you deaf; that’s the reason why you should not test your audio plugins with headphones on.

To ensure that the deadline is met, programmers must follow certain rules:

- No system calls on the audio thread, for example,
    - no allocations or deallocations
    - no mutex locks
    - no waiting for threads or spawning threads
    - no network requests
    - no reading from or writing to files
- No algorithms with unbounded execution time
- No algorithms with poor worst-case performance
- And much much more…

Let me tell you one shocking fact: the AI has no idea about these rules. Why? Well, maybe because 99% of programmers don’t (of course, that number is not based on data). Even some of the audio programmers!

Additionally, try asking AI for DSP algorithms or implementations; what you receive is often pure garbage.

But yes, AI models are getting better all the time, so by the time you read this, who knows? But even then, will you be able to verify the AI output?

### Example: AI fails to generate DSP code

To show how this looks, please consider the `processBlock()` method of a vibe-coded phaser audio plugin:

_Listing {% increment listingId20250114  %}._
```cpp
void PhaserAudioProcessor::processBlock (juce::AudioBuffer<float>& buffer, juce::MidiBuffer& midiMessages)
{
    juce::ScopedNoDenormals noDenormals;
    auto totalNumInputChannels  = getTotalNumInputChannels();
    auto totalNumOutputChannels = getTotalNumOutputChannels();

    for (auto i = totalNumInputChannels; i < totalNumOutputChannels; ++i)
        buffer.clear (i, 0, buffer.getNumSamples());

    auto lfoRateParam = valueTreeState.getRawParameterValue("lfoRate");
    auto modDepthParam = valueTreeState.getRawParameterValue("modDepth");
    
    float lfoRate = lfoRateParam->load();
    float modDepth = modDepthParam->load();
    
    lfo.setFrequency(lfoRate);

    for (int channel = 0; channel < totalNumInputChannels; ++channel)
    {
        auto* channelData = buffer.getWritePointer(channel);
        
        for (int sample = 0; sample < buffer.getNumSamples(); ++sample)
        {
            float input = channelData[sample];
            float lfoValue = lfo.processSample(0.0f);
            float delayTime = minDelayTime + (maxDelayTime - minDelayTime) * 
                            (0.5f + 0.5f * lfoValue) * modDepth;
            
            float output = input;
            for (auto& filter : allPassFilters)
            {
                output = filter.processSample(output, delayTime);
                delayTime *= 1.5f;
            }
            
            channelData[sample] = (input + output) * 0.5f;
        }
    }
}

// Members of PhaserAudioProcessor:
class PhaserAudioProcessor : public juce::AudioProcessor
{
//...
private:
  juce::AudioProcessorValueTreeState valueTreeState;
  
  struct AllPassFilter
  {
    float delay = 0.0f;
    float feedback = 0.7f;
    juce::dsp::DelayLine<float, juce::dsp::DelayLineInterpolationTypes::Linear> delayLine;
    
    void prepare(double sampleRate, int samplesPerBlock);
    float processSample(float input, float delayTime);
  };
  
  std::array<AllPassFilter, 4> allPassFilters;
  juce::dsp::Oscillator<float> lfo;
  
  float sampleRate = 44100.0f;
  float lfoPhase = 0.0f;
  
  static constexpr float minDelayTime = 1.0f;
  static constexpr float maxDelayTime = 10.0f;
};
```

Can you spot what the error is in the `processBlock()` function? I noticed two, but I haven’t analyzed the code in detail, so there may be more 😉

(If you say, “you just need to prompt it right!” then, please note that we’re talking about beginners here; how should they know what “right” in audio programming is?) 

<details>
<summary>Answer</summary>
The LFO oscillator is shared between the channels. If there is more than one channel, the user may hear a glitch (but more likely a peculiar phaser behavior). The solution is either to have a separate LFO oscillator for each channel or to pre-generate the LFO signal before iterating over the channels. This is a common beginner mistake (maybe that’s how AI learned that!). I discuss the proper solution in the <a href="https://www.wolfsoundacademy.com/juce?utm_source=dont-use-ai-article&utm_medium=blog">JUCE audio plugin development course</a>.
</details>

For a professional, finding a bug in this blob of code is difficult.

I challenged the participants of the [Audio Developer Meetup Berlin](https://www.meetup.com/audio-developer-meetup-berlin/) to find it, and even on zoom, it wasn’t easy for them (to be completely fair, I didn’t give them much time).

Finding it for a beginner, is impossible, in my opinion. As a beginner, you will only wonder “why is my plugin glitching?”

Of course, you can discuss with the AI coding agent, but to understand the errors and how to fix them, you need to know C++ and JUCE. And so we’re in this chicken-and-egg problem, where you use AI generators because you don’t know audio programming, but verifying AI output requires the knowledge of audio programming. There’s no escaping it.

*Disclaimer: I am not suggesting that AI cannot generate correct audio code. I claim that if you cannot verify their output, you can never be sure that it’s correct. In a [September 2025 paper,](https://arxiv.org/pdf/2509.04664) OpenAI researchers admitted that AI will probably continue to hallucinate due to the way it is trained.*

### Why is AI making audio/DSP code mistakes?

My guess is that there simply isn't enough training data for LLMs to learn real-time-safe audio programming or audio DSP algorithms.

Most of the “good” audio programming code from companies like Apple, Steinberg, or Native Instruments is proprietary, i.e., LLMs cannot learn from it. I don’t know the exact data sources used to teach LLMs audio programming, but there is a huge discrepancy between their count and the number of sources to learn, say, the React JavaScript framework.

Thus, AI tries to interpolate from other sources, which typically leads to a mess.

So, **if you don’t understand audio programming, you won’t be able to apply critical thinking to LLMs’ output.**

But that’s not the only aspect where AI fails when it comes to audio code…

## AI-generated code has poor quality

Professional audio developers report negative feedback on vibe-coded plugins.

- I’ve heard a few opinions coming from the industry how awful vibe-coded plugins are. They are considered “big balls of mud,” that don’t follow any good (not to mention best) software engineering practices.
- I’ve had this experience myself when mentoring an intern. They didn’t do any vibe-coding but they used AI to generate non-audio parts of the code. Although they thought they understood the code, in reality, they didn’t. That resulted in buggy and duplicated code.
- If you are a beginner, you probably don’t have an idea of what high-quality code is. Using AI can give you a false sense of confidence and a false idol to follow. But I admit, it’s difficult to find high-quality open-source audio code. Personally, I can recommend [Jatin Chowdhury’s work.](https://github.com/Chowdhury-DSP)

## Experts say: beginners should not generate audio code with AI

But don’t take my word for it. What do the experts say?

In the [Audio Developer Conference 2025](https://audio.dev/archive/adc25-bristol/) keynote entitled “ADC 2015 to 2035: Looking Back at 10 Years of Audio Dev, and Peering Forward at the Next 10,” Julian Storer showed two points on a slide:

- “If you don’t need a code agent, they can be a lot of fun.”
- “If you do need one, they are dangerous.”

{% image "assets/img/posts/programming-in-general/2026-01-14-dont-use-ai-for-audio-programming/jules-slide.webp", "Julian Storer's ADC25 keynote slide on using AI code agents" %}
_Figure {% increment figureId20250114  %}. Julian Storer's ADC25 keynote slide on using AI code agents._

He followed it up by saying, "To use these things well, you have to be a good programmer, you have to have a lot of experience."

**So, while all senior audio developers I talked to use AI to generate code, as a beginner, you definitely shouldn’t, because you cannot verify if the generated code is correct.**

But generating audio code with AI can actually hurt you; let me tell you how.

## Using AI may make you less productive

[A 2025 study by METR](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) indicates that using AI to complete development tasks may result in longer delivery times. While statistically significant, this study included only 16 developers, all experienced programmers, so we should not generalize these results prematurely.

{% image "assets/img/posts/programming-in-general/2026-01-14-dont-use-ai-for-audio-programming/ai-productivity-predictions.webp", "Plot of predictions and measurement of programming with AI. Measurements showed that programmers were actually slower with AI." %}

_Figure {% increment figureId20250114  %}. Predictions vs reality of productivity increase when using AI for coding. [Source](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/), accessed January 14, 2026._

There’s one disturbing detail to the results of the study, though.

After the observation phase but before seeing the measurement results, the participating developers were surveyed on how much AI had sped them up. All of them said the AI made them more productive (=allowed to develop the features faster). All of them were wrong. On average, they were slower when using AI.

I dedicate this observation to all senior programmers I talked to who swore by AI making them more productive. It would be awesome, if you could measure that somehow and report the results.

## Using AI for programming turns off your brain

Unfortunately, the ease with which AI provides solutions has its negative effects—it turns off our brains. Let me give you two examples.

### AI “fixes” triangle-generating function

In [the official JUCE online course](https://www.wolfsoundacademy.com/juce?utm_source=dont-use-ai-article&utm_medium=blog), I teach students how to generate a [triangle LFO]({% post_url collections.posts, "synthesis/2022-07-03-envelopes.md" %}).

That’s the code I’m sharing:

_Listing {% increment listingId20250114  %}._
```cpp
float triangle(float phase) {
    const auto ft = phase / (2.f * std::numbers::pi_v<float>);
    return 4.f * std::abs(ft - std::floor(ft + 0.5f)) - 1.f;
}
```

One of the students reported that the code didn’t work for them, so they asked AI to fix it. Here’s the “fixed” code given by AI.

_Listing {% increment listingId20250114  %}._
```cpp
float triangle_ai(float phase) {
    const auto ft = phase / (2.f * std::numbers::pi_v<float>);
    return 2.f * std::abs(2.f * (ft - std::floor(ft + 0.5f))) - 1.f;
}
```

Can you see the difference between these functions?

<details>
<summary>Answer</summary>
The AI function has 2*2 instead of 4 and one of the 2s is moved into the <code>std::abs()</code> argument.</details>

So mathematically, the two functions are identical, yet the student never reflected on why one works and the other seemingly doesn’t. As it turned out, they had a typo in their initial implementation. By refusing to investigate the error themselves and blindly following AI advice, they prevented learning.

### The Tab addiction

I see my students often blindly accept inline AI suggestions without much thought.

{% image "assets/img/posts/programming-in-general/2026-01-14-dont-use-ai-for-audio-programming/ai-suggestion.webp", "VS Code AI autocomplete suggestion" %}

_Figure {% increment figureId20250114 %}. Seeing the suggestion, you just want to hit that sweet little Tab button, don’t you?_

It’s hard for them to resist hitting the Tab button. They don’t consider *what* they want to achieve or *how* they could achieve it. They just accept whatever is suggested to them, thinking that they are learning from that. But in fact, they are just mindlessly hitting Tab. Without the mental strain of thinking about what to write first, they don’t develop proper programming habits and increase their mental capacity. And the resulting code is awful (as anecdotally confirmed by my colleagues, who were asked to fix vibe-coded audio software).

I see my students often cargo-cult following AI suggestions without understanding. Please, don’t do that if you’re a beginner.

## AI takes away your code ownership

One of the best things about programming is the satisfaction that comes from completing a feature, creating a neat code design, or fixing a bug. Seeing and hearing the result of your code is priceless.

Professional programmers have a strong sense of **code ownership**. They are responsible for the code they wrote: its good and bad sides.

Code ownership is what often drives people to become better programmers.

If you generate code with AI, can you really say that it is your own?

Can you be proud of AI-generated code?

And if it doesn’t work, who will you blame? Yourself or the AI?

If you want to become a better programmer, write the code and own it.

## The ultimate reason not to use AI for audio programming

The last reason not to use AI for audio programming is purely subjective.

Namely, audio programming is fun and challenging.

Offloading the coding process to AI agents deprives you of the joy of coding and of the pleasure of cognitive strain.

At the same time, it puts on you the burden of even more code review. I have met hundreds of people who love to code, but none who like to review code.

When you code, you develop a mental model of the program and the domain. This way you can think of better designs in the future. With AI that whole expertise is gone.

The human brain is a wonderful tool. Programming is an amazing way to sharpen that tool.

Just like Steven Covey wrote in his book “The 7 Habits of Highly Effective People”: you need to sharpen the saw.

Our brains are responsible for creating the rich experience of life. Don’t you want to have it as sharp as possible?

Improving your cognitive capacity can be achieved by learning complex concepts and solving challenging problems. It requires strain. Strain is good. Mental effort is good.

I understand that you may need a Python script that copies and renames your files ASAP, and so you use AI for this purpose.

But if you’re learning audio programming, generating the audio code and then analyzing it (assuming it is correct, which it probably isn’t), is much less cognitively demanding than designing and writing it from scratch.

The more you write code yourself, the better your brain is, the more complex challenges you can tackle, and the better your life becomes.

The more you use AI and get distracted waiting for the answer to be generated, the lazier your brain becomes.

Let’s not neglect the beautiful tool that is our brain. Let’s sharpen the saw.

## Is using AI all bad?

The last point I’d like to make is that using AI is not all bad. I’m certainly using it for many scenarios (although not for generating audio code or this blog’s content, for that matter).

Here are a couple of scenarios that seem good use cases for AI:

- Checking your grammar
- Being an enabler: starting a project for you if you are completely stuck
- Vibe-coding prototypes you throw away
- Serving as a peer reviewer of your code
- Setting up your development environment (for example, [NeoVim config](https://github.com/JanWilczek/neovim-config.git) or PyCharm setup)
- Writing simple scripts, e.g., in Python
- Preliminary research, where you try to find research papers on a topic. That can be misleading though because of the possible bias in the training data and online resources (most scientific journals are behind paywalls)
- Writing regression unit tests (**not** regular unit tests)

## Everything flows

The world of AI is rapidly evolving.

I write these words on January 14, 2026. Who knows if tomorrow’s model won’t be able to explain you audio programming correctly?

But even if that happens, how can you tell, unless you know it already?

## Summary

In summary, I believe that if you are a beginner in audio programming, you should not use AI to generate audio code or to build your understanding of digital signal processing or audio development. AI can easily mislead you in this area.

Instead, consider human-created resources, like [the official JUCE audio plugin development course](https://www.wolfsoundacademy.com/juce?utm_source=dont-use-ai-article&utm_medium=blog), which is completely free and dedicated to beginners.

Furthermore, even if you are not a junior developer, research suggests that AI can make you less productive than you would be without it. Further research is needed, though.

Even if you are an expert, you must hand-review every line AI outputs. That’s a matter of professionalism.

And, ultimately, what is more enjoyable to you? Solving problems with your brain, extending your knowledge, writing code, and becoming better, or code review?

Let me leave you with this quote from Cal Newport:

> *"Learning requires strain. Learning is hard."* [Source](https://youtu.be/ohruWW2WxYY?si=tCvygZAJEdXO9diZ)

And there’s nothing wrong with hard things and strain. You can do this, too, and become an audio programmer.

Do you agree? Do you disagree? Did you have a positive experience with AI and audio? Let me know in the comments! I’d be happy to discuss and be proven wrong. After all, I’m always learning, too!
