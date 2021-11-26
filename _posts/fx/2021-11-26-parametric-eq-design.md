---
title: "How to Design a Parametric EQ Plugin in 4 Simple Steps"
description: "PLACEHOLDER"
date: 2021-11-26
author: Jan Wilczek
layout: post
images: assets/img/posts/fx/2021-11-26-parametric-eq-design/
# background: /assets/img/posts/fx/2021-10-22-allpass-filter/first_order_allpass_filter.webp
categories:
  - Audio FX
  - Digital Signal Processing
tags:
  - effects
  - filtering
discussion_id: 2021-11-26-parametric-eq-design
---
Code your own low-pass or shelving filter plugins.

You probably have seen some form of a parametric equalizer in your digital audio workstation. You may be familiar with low-pass or notch filters. How to design them? How to implement them in code as plugins? 

In this article, I will outline 4 steps necessary to create such software. By the end of this article, you will know exactly what to do when you want to implement a parametric filter, even if it’s just for a university or hobby project.

{% katexmm %}
{% capture _ %}{% increment equationId20211126  %}{% endcapture %}

## Basic Definitions

An **equalizer (EQ)** is a software program or a device that allows you to adjust the volume of specific frequency ranges. Two main classes of equalizers are parametric equalizers and graphic equalizers [Valimaki].

A **parametric equalizer** is an equalizer that gives you a great amount of control: you can specify exactly which frequency ranges you want to affect and how much. As such is the most powerful and flexible equalizer of all. We could say that a parametric EQ consists of different types of *parametric filters*.

<!-- ReaEQ image -->

An **audio plugin** is a piece of software that runs inside a digital audio workstation (DAW) to modify a certain track containing audio recordings. Sample plugin formats are: VST, AAX, AU.

In this article, we discuss *how to design and implement a parametric EQ audio effect plugin*.

## Plugin Requirements

Let’s ask ourselves a question: what are the design requirements of our filter plugin? 

If you come from the digital signal processing field, you may be familiar with finite impulse response (FIR) filters or infinite impulse response (IIR) filters. You may know that there are dozens of methods for creating these filters. However, in the context of audio plugins, our filters need to have specific properties:

###	1. Meaningful Controls

For example, a low-pass filter may have a cutoff frequency parameter and a resonance parameter, both of which are well defined and are understandable even to people untrained in audio.

 <!-- LOWPASS IN REAEQ IMAGE.  -->
 
As opposed to that, if I gave you control over filter coefficients, like $a_1$, $a_2$, or $b_1$, you probably wouldn’t know what to do with it to achieve the desired filtering. Well, neither would I.

### 2. Computational Efficiency

In the context of filters, it usually means that we will favor IIR filters. There is an additional reason for this: the controls to coefficients mapping must be fast as well. If we were to design the transfer function and derive the impulse response of an FIR filter every time we turn a knob on our plugin, we wouldn’t be able to do that in real time.

### 3. Stability For Any Meaningful Parameter Setups

In other words, if you turn the knob, we must be sure, that the output of the plugin won’t run into increasing (?) self-oscillations. The stability is acquired through using so-called analog prototypes, which I will cover shortly.

## 4 Steps To Design A Parametric Filter Plugin

Now when we know, what is important for a musically useful plug-in filter we can cover the 4 steps necessary to design it:
1.	Decide on the filter type you want to implement.
2.	Design an analog prototype.
3.	Digitize the analog prototype using the bilinear transform.
4.	Implement the digital filter in code.

*There’s one additional step that I encourage you to do now that will allow you to excel at audio programming in general: [subscribing to the WolfSound email list]({% link newsletter.md %}). If you haven’t done that already, please, do it now. Thank you: each and every subscriber makes me want to do more articles and videos so that you can enjoy the beauty of audio programming.*

Let’s now expand on every of the 4 steps.

## Step 1: Decide On The Filter Type.

<!-- Follow editing from here -->

In digital signal processing, there are lots of filter types but in parametric EQs there are only a few. I will shortly explain the most important ones now. The amplitude response of each filter is shown on the example of the ReaEQ plugin from Reaper.
<!-- TODO: Add a link to the ReaEQ plugin -->

<div class="card summary">
  <div class="card-body">
  <h5 class="card-title">In Short</h5>
  <h6 class="card-subtitle mb-2 text-muted">Filter Controls</h6>
    <table class="table">
    <tr>
        <th>Filter Type</th>    
        <th>Controllable Parameters</th>
    </tr>
    <tr>
        <td>Low-Pass, High-Pass</td>
        <td>
            <ul>
                <li>cutoff frequency,</li>
                <li>resonance</li>
            </ul>
        </td>
    </tr>
    <tr>
        <td>Band-Pass, Notch</td>
        <td>
            <ul>
                <li>center frequency,</li>
                <li>bandwidth</li>
            </ul>
        </td>
    </tr>
    <tr>
        <td>Shelving</td>
        <td>
            <ul>
                <li>crossover frequency,</li>
                <li>bandwidth</li>
            </ul>
        </td>
    </tr>
    <tr>
        <td>Peak</td>
        <td>
            <ul>
                <li>center frequency,</li>
                <li>bandwidth,</li>
                <li>gain</li>
            </ul>
        </td>
    </tr>
    </table>
  </div>
</div>

### Low-Pass Filter

A *low-pass filter* attenuates all frequencies higher than the cutoff frequency.

![]({{ page.images | absolute_url | append: "/LowPass.webp"}}){: width="70%" alt="Low-pass filter amplitude response."}


<!-- TODO: Mention the Q factor -->

The *cutoff frequency* is the frequency at which the filter attenuation is -3 dB relative to the unfiltered signal. Another parameter is *resonance*. Resonance let’s you create a peak around the cutoff frequency in the amplitude response of the filter. The resonance was probably the main factor behind the success of the Moog synthesizer filter section.

 <!-- MOOG/EMERSON PICTURE.  -->
 
Additionally, we can control the slope of the filter, so how fast is the amplitude response decaying above the cutoff filter. 
 
In itself, the low-pass filter is a powerful musical tool.

### High-Pass Filter

A *high-pass filter* works exactly the same as the low-pass filter, except that it attenuates frequencies below the cutoff frequency. All the parameters are the same as for the low-pass filter.

![]({{ page.images | absolute_url | append: "/HighPass.webp"}}){: width="70%" alt="High-pass filter amplitude response."}

High-pass filter is usually used to remove undesired frequencies below 100 Hz.

### Band-Pass Filter

A *band-pass filter* passes through frequencies only in a certain range. It cannot additionally boost or attenuate them. The only two parameters it lets us control is the *center frequency* of the band and the *bandwidth*.

![]({{ page.images | absolute_url | append: "/Bandpass.webp"}}){: width="70%" alt="Band-pass filter amplitude response."}

### Notch Filter

A *notch filter* also called a *band-stop* or *band-reject* filter does the opposite than the band-pass filter: it eliminates a certain frequency range from the signal. Again, we can control it through center frequency and bandwidth parameter.

![]({{ page.images | absolute_url | append: "/Notch.webp"}}){: width="70%" alt="Notch filter amplitude response."}

### Shelving Filter

Milder versions of the low-pass and high-pass filters are high-shelving and low-shelving filters respectively.

A *high-shelving filter* lets us boost or attenuate frequencies above the crossover frequency. The crossover frequency specifies the frequency at which the gain reaches half of the shelf gain. Apart from the crossover frequency and the gain of the shelf, we can also control the steepness or the width of the slope in the transition band.

![]({{ page.images | absolute_url | append: "/HighShelving.webp"}}){: width="70%" alt="High-shelving filter amplitude response."}

A *low-shelving filter*, as you might guess at this point, lets us manipulate the shelf below the crossover frequency. It has exactly the same parameters as the high-shelving filter.

![]({{ page.images | absolute_url | append: "/LowShelving.webp"}}){: width="70%" alt="Low-shelving filter amplitude response."}

### Band Filter

The final filter that is musically useful is the *band filter*. A band filter lets us boost or attenuate a frequency range. We can control the center frequency and the bandwidth so the steepness of the slope on the sides of the amplitude response of the band.

![]({{ page.images | absolute_url | append: "/Peak.webp"}}){: width="70%" alt="Peak filter amplitude response."}

Now that you know the types of the filters, you can decide on which of them you want to implement. Even if you want to implement them all, start with 1. You have it? Then it’s time for step 2.

## Step 2: Design an Analog Prototype.

An analog prototype ensures that we have meaningful controls-to-coefficients mapping and we obtain a computationally efficient and stable IIR filter. To design an analog prototype to obtain a desired filter type, we need to turn to analog filter design theory.

Without going into much detail, there are 3 main classes of analog filter design [Smith07]: Butterworth, Chebyshev, and Elliptic Functions. Each of them is optimal in some sense. Using these, we can construct any of the above-specified filters in the analog domain. The output of this design is an analog transfer function in the Laplace or s-domain.

For example, a first-order analog Butterworth low-pass has the following transfer function:

$$H_\text{a}(s) = \frac{\omega_\text{c}}{s + \omega_\text{c}}, \quad ({% increment equationId20211126  %})$$

where $s = \sigma + j \omega$ is the complex variable and $\omega_\text{c}$ is the analog cutoff frequency in radians per second.

## Step 3: Digitize the Analog Prototype.

The third step to implement a filter plugin is the digitization of the analog prototype. Again, there are many ways to do this but in practice the most practical one is the *bilinear transform*, also called *Tustin's method*. 

The bilinear transform maps the analog frequencies from the $j\omega$ analog frequency axis in the $s$-plane to digital frequencies on the unit circle in the $z$-plane. This may seem kind of complicated, and frankly it is, but fortunately there are ready-made formulas for this:

![]({{ page.images | absolute_url | append: "/BilinearTransform.webp"}}){: width="70%" alt="Bilinear transform formulas."}

For audio purposes, $c$ is typically set to align cutoff frequencies of $H_\text{a}(s)$ and $H_\text{d}(z)$. You can make these substitutions in your analog transfer functions and voilà: you have a digital filter!

<!-- For example, the first-order low-pass filter from Eq. 1, after digitization becomes -->

<!-- $$H_\text{d}(z) = , \quad ({% increment equationId20211126  %})$$ -->

## Shortcut Steps 2 and 3

There is a trick that allows you to shortcut steps 2 and 3. The so-called [Audio EQ Cookbook](https://webaudio.github.io/Audio-EQ-Cookbook/audio-eq-cookbook.html), compiled by Robert Bristow-Johnson (thus, sometimes called "RBJ Cookbook"), already lists most of the musically useful filters in their digital forms so you don’t have to derive them all over again. Nevertheless, I still believe it is beneficial to understand the process that stands behind these formulas in order to use them to their full capacity and be able to extend them if necessary.

## Step 4: Implement the Digital Filter.

The last step in the process is to take that digital filter and implement it in the technology of your choice. Sample technologies may be 

* Python, 
* Rust,
* Matlab, 
* CSound, 
* Pure Data, 
* Android, 
* iOS,
* JavaScript
* Arduino, 
* Raspberry Pi, or… 
* JUCE. 
 
The last option may seem the most obvious choice for audio plugin developers, that is why, *I will be showing you how to implement each and every of the mentioned filters in the JUCE C++ framework over the course of the following articles and videos*. So stay tuned!

## Applications of Parametric Filters

So where can these parametric filters be applied? One obvious answer is your digital audio workstation. In this software, you can use a parametric EQ plugin to manipulate the frequency content of your audio tracks. Thanks to these plugins, you can remove unwanted tones or noise and add coloration to the timbre. However, that’s not the only use.

Efficient filters are especially important in game audio, virtual reality, or, in a broader sense, the field of sound design. Any virtual environment must be able to dynamically control user’s environment and tune the system so that the changes in player movements are reflected in the changes in sound. One example could be filtering applied when a player finds themselves behind a curtain; the sounds coming from behind should sound muffled what can be achieved with a low-pass or a high-shelving filter. A similar effect can be put on audio when the player finds themselves under water.

## Summary

In summary, in this article I showed you 4 steps to create a filter plugin: from an idea to the implementation. I have also showed you a shortcut in the form of Audio EQ Cookbook. 

Over the next couple of articles and videos, I will discuss in detail every step so that you can understand fully the process behind parametric EQ design and implementation. Then I will show you sample implementations of the parametric filters in the JUCE C++ framework in the form of do-it-yourself plugin tutorials. So there is a lot ahead of us!

If you want to be notified about weekly WolfSound content in a condensed form [subscribe to my email list.]({% link newsletter.md %}). Thank you!

## Bibliography

[Smith07] [Smith, J.O. *Introduction to Digital Filters with Audio Applications*,
http://ccrma.stanford.edu/~jos/filters/](http://ccrma.stanford.edu/~jos/filters/), online book, 2007 edition,
accessed November 26, 2021.


{% endkatexmm %}
