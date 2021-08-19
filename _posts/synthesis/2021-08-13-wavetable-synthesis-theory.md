---
title: "Wavetable Synthesis Algorithm Explained"
description: Wavetable is a synthesis technique that loops over a waveform stored in a memory array according to the desired frequency and sampling rate.
date: 2021-08-13
author: Jan Wilczek
layout: post
permalink: /sound-synthesis/wavetable-synthesis-algorithm/
images: assets/img/posts/synthesis/2021-08-13-wavetable-synthesis-theory
background: /assets/img/posts/2021-08-13-wavetable-synthesis-theory/Thumbnail.png
categories:
 - Sound Synthesis
tags:
 - synthesis
 - wavetable
 - waveform
discussion_id: 2021-08-13-wavetable-synthesis-theory
---
How to generate sound in code using the wavetable synthesis technique?

{% katexmm %}

{% capture _ %}{% increment equationId20210813 %}{% endcapture %}

In this article, you will learn:
 * how to generate sound using wavetables,
 * step-by-step wavetable synthesis algorithm,
 * what are pros and cons of wavetable synthesis, and
 * how is wavetable synthesis related to other synthesis methods.

In the follow-up articles, an implementation of this technique in the Python programming language and the JUCE framework will follow.

# A Need for a Fast and Efficient Synthesis Method

*Computer-based sound synthesis is the art of generating sound through software.*

In the early days of digital sound synthesis, sound was synthesised using specialized digital signal processing hardware. Later on, the community started using software for the same purposes but the underlying principles and algorithms remained the same. To obtain real-time performance capabilities with that technology, there was a great need to generate sound efficiently in terms of memory and processing speed. Thus, the wavetable technique was convceived: it is both fast and memory-inexpensive.

# From Gesture to Sound

The process of generating sound begins with a *musician*'s *gesture*. Let's put aside who a musician might be or what kind of gestures they perform. For the purpose of this article, a gesture could be as simple as pressing a key on a MIDI keyboard, clicking on a virtual keybord's key, or pressing a button on any controller device.

![]({{ page.images | absolute_url | append: "/gesture_to_sound.png" }}){: alt="Sound synthesis pipeline: gesture, synthesis algorithm, sound." width="600px" }
_Figure 1. In sound synthesis, a gesture of the musician controls the sound generation process._

A gesture provides *control information*. In the case of pressing a MIDI note-on event, control information would incorporate information on which key was pressed and how fast was it pressed (*velocity* of a keystroke). We can change the note number information into frequency $f$ and the velocity information into amplitude $A$. This information is sufficient to generate sound using most of the popular synthesis algorithms.

# Sine Generator

Let's imagine that given frequency and amplitude information we want to generate a sine wave. The general formula of a sine waveform is

$$s(t) = A \sin (2 \pi f t + \phi), \quad ({% increment equationId20210813 %})$$

where $f$ is the frequency in Hz, $A$ is the amplitude in range $[0, 1]$, $t$ is time in seconds, and $\phi$ is the initial phase, which we will ignore for now (i.e., assume that $\phi=0$).

As we discussed in the [digital audio basics article]({% post_url 2019-11-12-what-is-sound-the-notion-of-an-audio-signal %}), digital audio operates using samples rather than physical time. The $n$-th sample occurs at time $t$ when

$$n = f_s t, \quad ({% increment equationId20210813 %})$$

where $f_s$ is the sampling rate, i.e., the number of samples per second that the system (software or hardware) produces.

After inserting Equation 2 into Equation 1, we obtain the formula for a digital sine wave

$$s[n] = A \sin (2 \pi f n / f_s), \quad ({% increment equationId20210813 %})$$

How to compute the $\sin$ in the above formula? In programming languages (and any calculators for that matter), we often have a `sin()` function, but how does it compute its return value?

`sin()` calls use *Taylor expansion* of the sine function [1]

$$\sin(x) = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} \dots \quad ({% increment equationId20210813 %})$$

Above expansion is infinite, so on real-world hardware, it needs to be truncated at some point (after obtaining sufficient accuracy). Its advantage is, that it uses operations realizable in hardware (multiplication, division, addition, subtraction). Its disadvantage is that it involves **a lot** of these operations. If we need to produce 44100 samples per second and want to play a few hundred sines simultaneously (what is typical of additive synthesis), we need to be able to compute the $\sin$ function more efficiently.

# A Wave Table

A *wave table* is an array in memory in which we store a fragment of a waveform. A *waveform* is a plot of a signal over time. Thus, one period of a sine wave stored in memory looks as follows:

![]({{ page.images | absolute_url | append: "/sine_wave_table.png" }}){: alt="A wave table with 64 samples of the sine waveform." width="600px" }
_Figure 2. A wave table with 64 samples of the sine waveform._

The above wave table uses 64 samples to store one period of the sine wave.

$\sin$ period is exactly $2 \pi$. The period of a wave table is its length, let's denote it by $L$. For each sample index $k \in [0, \dots, L-1]$ in the wave table, there exists a corresponding argument $\theta \in [0, 2\pi]$ of the sine function.

$$\frac{k}{L} = \frac{\theta}{2 \pi}. \quad ({% increment equationId20210813 %})$$

The above equation tells us, that there is a mapping between the values in the wave table and the values of the original waveform.

# Computing a Waveform Value from the Wave Table

Equation 5 holds for $\theta \in [0, 2\pi]$. If we want to calculate the values of arbitrary $x \in \mathbb{R}$, we need to remove the multiplicity of $2 \pi$ contained in $x$ to bring it to the $[0, 2\pi]$ range. In other words, if

$$x = 2\pi l + \phi_x, \quad \phi_x \in [0, 2\pi], \quad ({% increment equationId20210813 %})$$

then we want to find $\phi_x$. In software, it can be done by subtracting or adding $2 \pi$ to $x$ until we obtain a value in the desired range. Alternatively, we can use a function called `fmod()`, which allows us to obtain the remainder of a floating-point division.

We can subsequently compute the corresponding index in the wave table from the proportion in Equation 5.

$$k = \frac{\phi_x L}{2\pi}. \quad ({% increment equationId20210813 %})$$

Now `waveTable[k]` should return the value of $\sin(x)$, right? There is one more step that is needed...

# What If $k$ Is Non-Integer?

In most cases, $k$ computed in Equation 7 won't be an integer. It will rather be a floating-point number between some two integers denoting the wave table indices, e.g., $i <= k < i+1, \quad i \in \mathbb{Z}, k \in \mathbb{R}$.

To make $k$ an integer, we have 3 options:
 * *truncation (0th-order interpolation)*: removing the non-integer part of $k$, a.k.a. `floor(k)`,
 * *rounding*: rounding $k$ to $i$ or $i+1$, whichever is nearest, a.k.a. `round(k)`,
 * *linear interpolation (1st-order interpolation)*: using the wave table values corresponding to $i$ and $i+1$ to compute a weighted sum with weights corresponding to $k$ distance to $i+1$ and $i$ respectively, i.e., instead of `waveTable[k]` we return `(k-i)*waveTable[i+1] + (i+1 - k)*waveTable[i]`,
 * ~~*higher-order interpolation*~~: too expensive and unnecessary for wavetable synthesis.

Each recall of a wave table value is called *wave table lookup*.

# Wave Table Looping

We know how to efficiently compute a waveform's value for an arbitrary argument. In theory, given amplitude $A$, frequency $f$, and sampling rate $f_s$ we are able to evaluate Equation 3 for any integer $n$. It means, we can generate an arbitrary waveform at an arbitrary frequency! Now, how to implement it algorithmically?

Thanks to the information on $f$ and $f_s$, we don't have to calculate the $2 \pi f f_s n$ argument of $\sin$ in Equation 3 for each $n$ separately. $n$ gets incremented by 1 on a sample-by-sample basis, so as long $f$ does not change (i.e., we play the same tone), the argument of $\sin$ gets incremented in a predictable manner. Actually, the argument $2 \pi f f_s n + \phi$ is called the *phase* of the sine (again, in our considerations $\phi=0$). The difference between the phase of the waveform for neighboring samples is called *phase increment* and can be calculated as

$$\theta_\text{inc}(f) = 2 \pi f (n+1) / f_s - 2 \pi f n / f_s = 2 \pi f / f_s. \quad ({% increment equationId20210813 %})$$

$\theta_\text{inc}(f)$ depends explicitly on $f$ (tone frequency) and implicitly on $f_s$ (which typically remains unchanged during processing so we can treat it as a constant). With $\theta_\text{inc}(f)$ we can initialize a `phase` variable to 0 and increment it by $\theta_\text{inc}(f)$ for each samples. When a key is pressed we reset `phase` to 0, calculate $\theta_\text{inc}(f)$ according to the pressed key, and start producing the samples.

<!-- index increment -->

## Index Increment

Having the information on phase increment, we can calculate the *index increment*, i.e., how the index to the wave table changes with each sample.

$$k_\text{inc} = (k+1) - k = \frac{(\phi_x + \theta_\text{inc})L}{2\pi} - \frac{\phi_x L}{2\pi} \\= \frac{\theta_\text{inc} L}{2\pi} = \frac{fL}{f_s}. \quad ({% increment equationId20210813 %})$$

For each sample, we increase an `index` variable by $k_\text{inc}$ and do a lookup. When key is pressed, we set `index` to 0. As long as it is pressed $k_\text{inc}$ is nonzero and we perform wave table lookup.

When `index` exceeds the wave table size, we need to bring it back to the $[0, \dots, L-1]$. It can be done by subtracting $L$ from `index` but this approach is not always correct. In implementation we can subtract $L$ as long as `index` is greater or equal to $L$ or we can use the `fmod` operation. This "index wrap" results from *phase wrap*: since the signal is periodic, we can shift its phase by the period without changing the signal.

## A Note on Efficiency

Phase increment and index increment are two sides of the same coin. The former has a physical meaning, the latter has an implementation meaning. You can keep phase information and use it to calculate the index or you can keep incrementing the index. Index increment is more efficient because we don't need to perform the multiplication by $L$ and division by $2\pi$ for each sample; we calculate the increment only when the instantaneous frequency changes. We'll therefore restrict ourselves to an implementation using index increment.

# Wavetable Synthesis Algorithm

Below is a schematic of how wavetable synthesis using index increment works.

![]({{ page.images | absolute_url | append: "/wavetable-synthesis-algorithm-diagram.png" }}){: alt="A DSP diagram of the wavetable synthesis algorithm" }
_Figure 3. A diagram of the wavetable synthesis algorithm using index increment. After [2]._

$k_\text{inc}[n]$ is the increment of the index into the wave table. It is denoted as a digital signal because in practice it can be changed on a sample-by-sample basis. It is directly dependent on the frequency of the played sound. If no sound is played $k_\text{inc}[n]$ is 0 and the `index` should be reset to 0. Alternatively, one could specify that if no sound is played this diagram is inactive (no values are supplied or taken from it).

For each new output sample, index increment is added into the `index` variable stored in a 1-sample buffer (denoted by $z^{-1}$ as explained in the [article on delays]({% post_url 2021-04-01-identity-element-of-the-convolution %})). This index is then "brought back" into the range of wavetable indices $[0, L)$ using the `fmod` operation. We still keep the fractional part of the index.

Then, we perform the lookup into the wavetable. The lookup can be done using interpolation strategy of choice.

Finally, we multiply the signal by a sample-dependent amplitude $A[n]$. $A[n]$ signal is called the *amplitude envelope*. It may be, for example, a constant, i.e., $A[n] = 1, \forall n \in \mathbb{Z}$.

The output signal $y[n]$ is determined by the wave table used for the lookup and currently generated frequency.

**We thus created a wavetable synthesizer!**

# Oscillator

The diagram in Figure 3 presents an *oscillator*. An oscillator is any unit capable of generating sound. It is typically depicted as a rectangle combined with a half-circle [3, 4] as in Figure 4. That symbol typically has an amplitude input A ($A[n]$ in Figure 3) and a frequency input $f$ (used to calculate $k_\text{inc}[n]$ in Figure 3). 

![]({{ page.images | absolute_url | append: "/oscillator.png" }}){: alt="Oscillator symbol" }
_Figure 4. The oscillator symbol._

Additionally, an oscillator pictogram has some indication of what type of waveform is generated, for example, it may have the sine symbol <i class="fas fa-wave-sine"></i> inside to show that it outputs the sine wave.

Oscillators are sometimes denoted as VCO, which stands for *voltage-controlled oscillator*. This term originates from the analog days of sound synthesis, when electric voltage determined oscillators' amplitude and frequency.

Oscillators are the workhorse of sound synthesis. What is presented in Figure 3 is one realization of an oscillator but the oscillator itself is a more general concept. Wavetable synthesis is just one way of implementing an oscillator.

# Sound Example: Sine

Let's use a precomputed wave table with 64 samples of one sine period from Figure 2 to generate 5 seconds of a sine waveform at 440 Hz using 44100 Hz sampling rate.

We thus have $L = 64$, $f=440$, $f_s=44100$, $k_\text{inc} = 0.6395\dots$. The resulting sound is:

{% include embed-audio.html src="/assets/wav/posts/synthesis/2021-08-13-wavetable-synthesis-theory/sine.wav" %}

The magnitude spectrum of this tone is shown below.

![]({{ page.images | absolute_url | append: "/sine_spectrum.png" }}){: alt="Magnitude frequency spectrum of a sine generated with wavetable synthesis" }
_Figure 5. Magnitude frequency spectrum of a sine generated with wavetable synthesis._

Great! It sounds like a sine and we obtain just one frequency component. Everything as expected! Now, let's generate sound using a different wavetable, shall we?

# Sound Example: Sawtooth

To generate a sawtooth, we use the same parameters as before just a different wave table:

![]({{ page.images | absolute_url | append: "/sawtooth_wave_table.png" }}){: alt="A wave table with 64 samples of the sawtooth waveform." width="600px" }
_Figure 6. A wave table with 64 samples of the sawtooth waveform._

Let's listen to the output:

{% include embed-audio.html src="/assets/wav/posts/synthesis/2021-08-13-wavetable-synthesis-theory/sawtooth.wav" %}

That sounds ok, but we get some ringing. How does it look in the spectrum?

![]({{ page.images | absolute_url | append: "/sawtooth_spectrum.png" }}){: alt="Magnitude frequency spectrum of a sawtooth generated with wavetable synthesis" }
_Figure 7. Magnitude frequency spectrum of a sawtooth generated with wavetable synthesis._

We can notice that there are some inharmonic frequency components that do not correspond to the typical decay of the sawtooth spectrum. These are aliased frequencies which occur because the spectrum of the sawtooth crossed the Nyquist frequency. To learn more about why this happens, you can [check out my article on aliasing]({% post_url 2019-11-28-what-is-aliasing-what-causes-it-how-to-avoid-it %})

Aliasing increases if we go 1 octave higher:

{% include embed-audio.html src="/assets/wav/posts/synthesis/2021-08-13-wavetable-synthesis-theory/sawtooth880.wav" %}

Ouch, that doesn't sound nice. The frequency spectrum reveals aliased partials that appear as inharmonicities:

![]({{ page.images | absolute_url | append: "/sawtooth880_spectrum.png" }}){: alt="Magnitude frequency spectrum of a 880 Hz sawtooth generated with wavetable synthesis" }
_Figure 8. Magnitude frequency spectrum of a 880Hz sawtooth generated with wavetable synthesis._

We've just discovered the main drawback of wavetable synthesis: aliasing at higher frequencies. If we went even higher with the pitch, we would obtain completely distorted signal. 

How to fix aliasing for wave tables that have partials crossing the Nyquist frequency. We can only increase the sampling rate of the system. Since it is not something we would like to do, most often other algorithms are used. This digital distortion was typical of the early digital synthesizers of the 1980s. A lot of effort was put to develop alternative algorithms to synthesize sound. The main focus was to obtain an algorithm that would produce partial-rich waveforms at low frequencies and partial-poor waveforms at high frequencies. These algorithms are sometimes called *antialiasing oscillators*. An example of this can be found in ["Oscillator and Filter Algorithms for Virtual Analog Synthesis" paper by Vesa Välimäki and Antti Huovilainen](https://www.researchgate.net/publication/220386519_Oscillator_and_Filter_Algorithms_for_Virtual_Analog_Synthesis) [5].

# Sampling: Extended Wavetable Synthesis?

Sampling is a technique of recording real-world instruments and playing back these sounds according to user input. We could, for example, record single guitar notes with pitches corresponding to all keys on the piano keyboard. In practice, however, notes for only some of the keys are recorded and the notes in between are interpolated versions of its neighbors. In this way, we store separate samples for high-pitched notes and thus avoid the problem of aliasing because it's not present in the data in the first place.

With sampling a lot more implementation issues come up. Since sampling is not the topic of this article, we will postpone its discussion for now.

# Multiple Wavetable
# Single-Cycle and Multi-Cycle Wavetable

<!-- Pluta p. 61 -->


# Summary

Wavetable synthesis is an efficient method that allows us to generate arbitrary waveforms at arbitrary frequencies. Its low complexity comes at a cost of high amounts of digital distortions coming from the partials crossing the Nyquist frequency at higher pitches. One typically would turn to more sophisticated algorithms for sound synthesis. Nevertheless, wavetable synthesis is a great method to understand the principles of software sound synthesis.


# Garbage

<!-- TODO: Probably delete this -->
The whole generation algorithm can now be simplified to a few cases:
* if there is a note-on event 

As we said, the whole generation process begins with a note-on event. The sound should be generated so long as there is no note-off event (i.e., so long as a key is pressed). Incrementing $n$ from 0 to the last sample to be generated may not be possible; most probably we would exceed $n$'s range in hardware representation. Therefore, we cannot simply increment $n$ and read out the values from the table.

Instead of incrementing the argument into infinity and bringing it back to the desired range, we can simply loop around the wave table; as soon as the index goes out of the feasible range, we subtract the length of the whole waveform.

$$, \quad ({% increment equationId20210813 %})$$

<!-- End delete -->

# Bibliography

[1] [Taylor series expansion of the sine function on MIT Open CourseWare](https://ocw.mit.edu/courses/mathematics/18-01sc-single-variable-calculus-fall-2010/unit-5-exploring-the-infinite/part-b-taylor-series/session-99-taylors-series-continued/MIT18_01SCF10_Ses99c.pdf)

[2] [F. Richard Moore, *Elements of Computer Music*, Prentice Hall 1990](https://www.amazon.com/gp/product/0132525526/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0132525526&linkCode=as2&tag=wolfsound05-20&linkId=71285ec31668f2e8d8cf81094ff51f5f)

[3] [Curtis Roads, *Computer Music Tutorial*, MIT Press 1996](https://www.amazon.com/gp/product/0262680823/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0262680823&linkCode=as2&tag=wolfsound05-20&linkId=86e6c4d45c7126d32c13ab2deff2afa2)

[4] Marek Pluta, *Sound Synthesis for Music Reproduction and Performance*, monograph, AGH University of Science and Technology Press 2019.

[5] [Vesa Välimäki and Antti Huovilainen, *Oscillator and Filter Algorithms for Virtual Analog Synthesis*, Computer Music Journal 30(2):19-31, June 2006](https://www.researchgate.net/publication/220386519_Oscillator_and_Filter_Algorithms_for_Virtual_Analog_Synthesis)

<!-- DePoli -->
<!-- Russ -->

{% endkatexmm %}

