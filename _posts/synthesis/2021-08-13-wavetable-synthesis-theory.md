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
 * how to generate sound using wavetables
 * step-by-step synthesis algorithm
 * what are pros and cons of wavetable synthesis
 * how is wavetable synthesis related to other synthesis methods

In the follow-up articles, an implementation of this technique in the Python programming language and the JUCE framework will follow.

# A Need for a Fast and Efficient Synthesis Method

*Computer-based sound synthesis is the art of generating sound through software.*

In the early days of digital sound synthesis the sound was also synthesised using specialized digital signal processing hardware but the underlying principles and algorithms remained the same. To obtain real-time performance capabilities with that technology, there was a great need to generate sound efficiently in terms of memory and processing speed. Thus, the wavetable technique was convceived: it is both fast and memory-inexpensive.

# From Gesture to Sound

The process of generating sound begins with a *musician*'s *gesture*. Let's put aside who a musician might be or what kind of gestures they perform. For the purpose of this article, a gesture could be as simple as pressing a key on a MIDI keyboard, clicking on a virtual keybord's key, or pressing a button on any controller device.

<!-- TODO: Add gesture to sound schematic -->

A gesture provides *control information*. In the case of pressing a MIDI note-on event, control information would incorporate information on which key was pressed and how fast was it pressed (*velocity* of a keystroke). We can change the note number information into frequency $f$ and the velocity information into amplitude $A$. This information is sufficient to generate sound using most of the popular synthesis algorithms.

# Sine Generator

Let's imagine that given frequency and amplitude information we want to generate a sine wave. The general formula of a sine waveform is

$$s(t) = A \sin (2 \pi f t + \phi), \quad ({% increment equationId20210813 %})$$

where $f$ is the frequency in Hz, $A$ is the amplitude in range $[0, 1]$, $t$ is time in seconds, and $\phi$ is the initial phase, which we will ignore for now (i.e., assume that $\phi=0$).

As we discussed in the [digital audio basics article]({% post_url 2019-11-12-what-is-sound-the-notion-of-an-audio-signal %}), digital audio operates using samples rather than physical time. The $n$-th sample occurs at time $t$ when

$$n = f_s t, \quad ({% increment equationId20210813 %})$$

where $f_s$ is the sampling rate, i.e., the number of samples per second that the system (software or hardware) produces.

After inserting Equation 2 into Equation 1, we obtain the formula for a digital sine wave

$$s[n] = A \sin (2 \pi f f_s n), \quad ({% increment equationId20210813 %})$$

How to compute the $\sin$ in the above formula? In programming languages (and any calculators for that matter), we often have a `sin()` function, but how does it compute its return value?

`sin()` calls use *Taylor expansion* of the sine function [1]

$$\sin(x) = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} \dots \quad ({% increment equationId20210813 %})$$

Above expansion is infinite, so on real-world hardware, it needs to be truncated at some point (after obtaining sufficient accuracy). Its advantage is, that it uses operations realizable in hardware (multiplication, division, addition, subtraction). Its disadvantage is that it involves **a lot** of these operations. If we need to produce 44100 samples per second and want to play a few hundred sines simultaneously (what is typical of additive synthesis), we need to be able to compute the $\sin$ function more efficiently.

# A Wave Table

A *wave table* is an array in memory in which we store a fragment of a waveform. A waveform is a plot of a signal over time. Thus, one period of a sine wave stored in memory looks as follows:

<!-- TODO: Add a sine figure with 1024 samples. -->

The above wave table uses 1024 samples to store one period of the sine wave.

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

$$\theta_\text{inc}(f) = 2 \pi f f_s (n+1) - 2 \pi f f_s n = 2 \pi f f_s. \quad ({% increment equationId20210813 %})$$

$\theta_\text{inc}(f)$ depends explicitly on $f$ (tone frequency) and implicitly on $f_s$ (which typically remains unchanged during processing so we can treat it as a constant). With $\theta_\text{inc}(f)$ we can initialize a `phase` variable to 0 and increment it by $\theta_\text{inc}(f)$ for each samples. When a key is pressed we reset `phase` to 0, calculate $\theta_\text{inc}(f)$ according to the pressed key, and start producing the samples.

<!-- index increment -->

## Index Increment

Having the information on phase increment, we can calculate the *index increment*, i.e., how the index to the wave table changes with each sample.

$$k_\text{inc} = (k+1) - k = \frac{(\phi_x + \theta_\text{inc})L}{2\pi} - \frac{\phi_x L}{2\pi} = \frac{\theta_\text{inc} L}{2\pi}. \quad ({% increment equationId20210813 %})$$

For each sample, we increase an `index` variable by $k_\text{inc}$ and do a lookup. When key is pressed, we set `index` to 0. As long as it is pressed $k_\text{inc}$ is nonzero and we perform wave table lookup.

## A Note on Efficiency

Phase increment and index increment are two sides of the same coin. The former has a physical meaning, the latter has an implementation meaning. You can keep phase information and use it to calculate the index or you can keep incrementing the index. Index increment is more efficient because we don't need to perform the multiplication by $L$ and division by $2\pi$ for each sample; we calculate the increment only when the instantaneous frequency changes. We'll therefore restrict ourselves to an implementation using index increment.

# Wavetable Synthesis Algorithm

Below is a schematic of how wavetable synthesis using index increment works.

![]({{ page.images | absolute_url | append: "/wavetable-synthesis-algorithm-diagram.png" }}){: alt="A DSP diagram of the wavetable synthesis algorithm" }
_Figure 1. A diagram of the wavetable synthesis algorithm using index increment. After [2]._

$k_\text{inc}[n]$ is the increment of the index into the wave table. It is denoted as a digital signal because in practice it can be changed on a sample-by-sample basis. It is directly dependent on the frequency of the played sound. If no sound is played $k_inc[n]$ is 0 and the `index` should be reset to 0. Alternatively, one could specify that if no sound is played this diagram is inactive (no values are supplied or taken from it).

For each new output sample, index increment is added into the `index` variable stored in a 1-sample buffer (denoted by $z^{-1} as explained in the [article on delays]({% post_url 2021-04-01-identity-element-of-the-convolution %})). This index is then "brought back" into the range of wavetable indices $[0, L)$ using the `fmod` operation. We still keep the fractional part of the index.

Then, we perform the lookup into the wavetable. The lookup can be done using interpolation strategy of choice.

Finally, we multiply the signal by a sample-dependent amplitude $A[n]$. $A[n]$ signal is called the *amplitude envelope*. It may be, for example, a constant, i.e., $A[n] = 1 \quad \forall n \in \mathbb{Z}$.

The output signal $y[n]$ is determined by the wave table used for the lookup and currently generated frequency.

**We thus created a wavetable synthesizer!**

# Oscillator

The diagram in Figure 1 presents an *oscillator*. An oscillator is any unit capable of generating

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

{% endkatexmm %}

