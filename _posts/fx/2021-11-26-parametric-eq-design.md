---
title: "How to Design a Parametric Filter Plugin in 4 Simple Steps"
description: "PLACEHOLDER"
date: 2021-11-26
author: Jan Wilczek
layout: post
# images: assets/img/posts/fx/2021-10-22-allpass-filter
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

## Step 1: Decide On The Filter Type You Want to Implement.

<!-- Follow editing from here -->

In digital signal processing, there are lots of filter types but in parametric EQ there are only a few. I will shortly explain the most important ones now. The effect of each filter is shown on the example of the pink noise signal. Unfiltered pink noise sounds like this: [PLAY PINK NOISE].

[SIDE BY SIDE FILTER NAME-PROPERTIES AND REAEQ]

A low-pass filter attenuates all frequencies higher than the cutoff frequency. The cutoff frequency specifies the frequency at which the filter attenuation is -3 dB relative to the unfiltered signal. Another parameter is resonance. Resonance let’s you create a peak around the cutoff frequency in the amplitude response of the filter. The resonance was probably the main factor behind the success of the Moog synthesizer filter section. [MOOG/EMERSON PICTURE]. Additionally, we can control the slope of the filter, so how fast is the amplitude response decaying above the cutoff filter. Here’s how a low-pass filter sounds [REAEQ EXAMPLE PLAY]. In itself, the low-pass filter is a powerful musical tool.

A high-pass filter works exactly the same as the low-pass filter, except that it attenuates frequencies below the cutoff frequency. All the parameters are the same as for the low-pass filter. Here’s how a high-pass filter sounds [REAEQ EXAMPLE PLAY].

A band-pass filter passes through frequencies only in a certain range. It cannot additionally boost or attenuate them. The only two parameters it lets us control is the center frequency of the band and the bandwidth. Here’s how a band-pass filter sounds [REAEQ EXAMPLE PLAY].

A notch filter also called a band-stop or band-reject filter does the opposite than the band-pass filter: it eliminates a certain frequency range from the signal. Again, we can control it through center frequency and bandwidth parameter. Here’s how a notch filter sounds [REAEQ EXAMPLE PLAY].

Milder versions of the low-pass and high-pass filters are high-shelving and low-shelving filters respectively. A high-shelving filter lets us boost or attenuate frequencies above the cutoff frequency. Apart from the cutoff frequency and the gain of the shelf, we can also control the steepness or the width of the slope in the transition band. Here’s how a high-shelving filter sounds [REAEQ EXAMPLE PLAY].

A low-shelving filter, as you might guess at this point, lets us manipulate the shelf below the cutoff frequency. It has exactly the same parameters as the high-shelving filter. Here’s how a low-shelving filter sounds [REAEQ EXAMPLE PLAY].

The final filter that is musically useful is the band filter. A band filter lets us boost or attenuate a frequency range. We can control the center frequency and the bandwidth so the steepness of the slope on the sides of the amplitude response of the band. Here’s how a band filter sounds [REAEQ EXAMPLE PLAY].

Now that you know the types of the filters, you can decide on which of them you want to implement. Even if you want to implement them all, start with 1. You have it? Then it’s time for step 2: designing an analog prototype [TRANSITION].

Digitizing an analog prototype ensures that we have meaningful controls-to-coefficients mapping and we obtain a computationally efficient and stable IIR filter. To design an analog prototype to obtain a desired filter type, we need to turn to analog filter design theory.

Without going into much detail, there are 3 main classes of analog filter design [SmithDigFil]: Butterworth, Chebyshev, and Elliptic Functions. Each of them is optimal in some sense. Using these, we can construct any of the above-specified filters in the analog domain. The output of this design is an analog transfer function in the Laplace or s-domain. [SHOW AN EXAMPLE TRANSFER FUNCTION FORMULA] [TRANSITION]

The third step to implement a filter plugin is a digitization of the analog prototype. Again, there are many ways to do this but in practice the most practical one is the bilinear transform, also called {FILL HERE}. The bilinear transform maps the analog frequencies from the jomega analog frequency axis in the s-plane to digital frequencies on the unit circle in the z-plane. This may seem kind of complicated, and frankly it is, but fortunately there are ready-made formulas for this [SHOW THE FORMULAS]. You can make these substitutions in your analog transfer functions and voila: you have a digital filter!

There is 1 trick that allows you to shortcut steps 2 and 3. The so-called RBJ Cookbook, compiled by Robert Bristow-Johnson, already lists all musically useful filters in their digital forms so you don’t have to derive them all over again. I have linked to the cookbook in the description below. Nevertheless, I still believe it is beneficial to understand the process that stands behind these formulas in order to use them to their full capability and be able to extend them if necessary. [TRANSITION]

The last step in the process is to take that digital filter and implement it in the technology of your choice. Sample technologies may be Python, Matlab, CSound, Pure Data, Android, iOS, Arduino, Raspberry Pi, or… JUCE. The last one may seem the most obvious choice for DAW plugin developers, that is why, I will be showing you how to implement each and every of the mentioned filters in the JUCE C++ framework over the course of the following videos. So stay tuned! [TRANSITION]

So where can these parametric filters be applied? One obvious answer is your digital audio workstation. In this software, you can use a parametric EQ plugin to manipulate the frequency content of your audio tracks. However, that’s not the only use.

Efficient filters are especially important in game audio or, in a broader sense, the field of sound design. [VIDEO GAME EXCERPT] In games, the designer must be able to dynamically control user’s environment and tune the system so that the changes in player movements are reflected in the changes of sound. One example could be filtering applied when the player finds themselves behind the curtain; the sounds coming from behind should sound muffled what can be achieved with a low-pass or a high-shelving filter. A similar effect can be put on audio when the player finds themselves under water.

Another important aspect of parametric EQ is the equalization applied to loudspeaker playback. When striving towards a perfect sound, each loudspeaker should have adjustable characteristics. And although these are often tuned with other techniques or even analog filters, the parametric EQ can still be employed for this purpose.

Finally, where you are listening to music from your computer or mobile phone, you may want to adjust certain frequencies, for example, add more bass. [MOBILE PHONE/COMPUTER STOCK FOOTAGE]. Since the changes in user controls must be immediately reflected in the played back sound, these EQs are often implemented using parametric filters as specified above. [TRANSITION]

In summary, in this video I showed you 4 steps to create a filter plugin: from an idea to the implementation. I have also showed you a shortcut in the form of RBJ Cookbook. Over the next couple of videos, I will discuss in detail every step so that you can understand fully the process behind it. Then I will show you sample implementations of the parametric filters in the JUCE C++ framework in the form of plugin design tutorials. So there is a lot ahead of us! If you want to stay up to date with the upcoming videos, subscribe to the channel and turn on notifications so that you are notified when the mentioned videos are published. As usual, I have put the content of this video in an article form on TheWolfSound.com so you can bookmark it for future reference. A big shout-out to Aalto Acoustics lab for letting me record this video in their offices. Thanks for watching and see you in the next one! Take care. 

{% endkatexmm %}
