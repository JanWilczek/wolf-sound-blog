---
id: 92
title: How to represent digital sound? Sampling, sampling rate, quantization.
date: 2019-11-19T17:07:29+00:00
author: Jan Wilczek
layout: post
guid: https://thewolfsound.com/?p=92
permalink: /how-to-represent-digital-sound-sampling-sampling-rate-quantization/
content_width:
  - default_width
hide_post_title:
  - default
unlink_post_title:
  - default
hide_post_date:
  - default
hide_post_image:
  - default
unlink_post_image:
  - default
header_wrap:
  - solid
background_repeat:
  - fullcover
themify_used_global_styles:
  - 'a:1:{i:0;s:0:"";}'
tbp_custom_css:
  - ""
categories:
  - Digital Signal Processing
tags:
  - quantization
  - sample rate
  - sampling
---
<figure class="wp-block-embed-youtube wp-block-embed is-type-video is-provider-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio">

<div class="wp-block-embed__wrapper">
  <div class="post-video">
  </div>
</div></figure> 



To process the audio signal, we need to somehow represent it on our machine. Several different options are possible, but the most common and useful one for sound processing is the discrete sample representation. That&#8217;s where the concepts of sampling and quantization come into play.

Mind you, that in this article expressions _function_ and _signal_ are used interchangeably. Both function and signal can be continuous or discrete.

## How to represent a continuous function through discrete values?

The computers and hardware we are using are only capable of storing finite-valued numbers, e.g. 2, -5, 9.5, 10e3, some with less accuracy than others due to binary representation. How to represent a continuous (analog) function through such numbers?

If we know that the observed function of time<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-b4e3cbf5d4c5c6d9b702dd139f14c147_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#116;" title="Rendered by QuickLaTeX.com" height="12" width="6" style="vertical-align: 0px;" /> is affine we can write:

<p class="ql-center-displayed-equation" style="line-height: 18px;">
  <span class="ql-right-eqno"> (1) </span><span class="ql-left-eqno"> &nbsp; </span><img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-d13f34dad6df05bce5099ebd52fd6491_l3.png" height="18" width="98" class="ql-img-displayed-equation quicklatex-auto-format" alt="&#92;&#98;&#101;&#103;&#105;&#110;&#123;&#101;&#113;&#117;&#97;&#116;&#105;&#111;&#110;&#42;&#125;&#115;&#40;&#116;&#41;&#32;&#61;&#32;&#97;&#116;&#32;&#43;&#32;&#98;&#92;&#101;&#110;&#100;&#123;&#101;&#113;&#117;&#97;&#116;&#105;&#111;&#110;&#42;&#125;" title="Rendered by QuickLaTeX.com" />
</p>

and store the a and b coefficients, which are discrete numbers. Whenever someone asks for the<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-ae1901659f469e6be883797bfd30f4f8_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#115;" title="Rendered by QuickLaTeX.com" height="8" width="8" style="vertical-align: 0px;" /> value at a particular time<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-b4e3cbf5d4c5c6d9b702dd139f14c147_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#116;" title="Rendered by QuickLaTeX.com" height="12" width="6" style="vertical-align: 0px;" /> we can easily calculate the output using the formula above.

If the signal is a sinusoid, it is completely determined by its amplitude<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-25b206f25506e6d6f46be832f7119ffa_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#65;" title="Rendered by QuickLaTeX.com" height="12" width="13" style="vertical-align: 0px;" /> , frequency<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-9c09a708375fde2676da319bcdfe8b24_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#102;" title="Rendered by QuickLaTeX.com" height="16" width="10" style="vertical-align: -4px;" /> and phase offset<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-5b2be26c0c1341f54b29baddda771346_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#92;&#112;&#104;&#105;" title="Rendered by QuickLaTeX.com" height="16" width="11" style="vertical-align: -4px;" /> :

<p class="ql-center-displayed-equation" style="line-height: 18px;">
  <span class="ql-right-eqno"> (2) </span><span class="ql-left-eqno"> &nbsp; </span><img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-8b14ee027cfc8072462c982cce25e2e1_l3.png" height="18" width="173" class="ql-img-displayed-equation quicklatex-auto-format" alt="&#92;&#98;&#101;&#103;&#105;&#110;&#123;&#101;&#113;&#117;&#97;&#116;&#105;&#111;&#110;&#42;&#125;&#115;&#40;&#116;&#41;&#32;&#61;&#32;&#65;&#92;&#115;&#105;&#110;&#40;&#50;&#92;&#112;&#105;&#32;&#102;&#32;&#116;&#32;&#43;&#32;&#92;&#112;&#104;&#105;&#41;&#92;&#101;&#110;&#100;&#123;&#101;&#113;&#117;&#97;&#116;&#105;&#111;&#110;&#42;&#125;" title="Rendered by QuickLaTeX.com" />
</p>

In general, we do not know how does the signal we are observing look like: that&#8217;s the whole point of observing it, right? That&#8217;s where sampling comes in.

<div class="wp-block-columns">
  <div class="wp-block-column">
    <figure class="wp-block-image size-large is-resized"><img src="https://thewolfsound.com/wp-content/uploads/2019/11/Sine1Hz-1-1024x723.png" alt="" class="wp-image-157" width="350" height="250" /><figcaption> An example of the observed signal: a 1 Hz sine (one period). </figcaption></figure>
  </div>
  
  <div class="wp-block-column">
    <figure class="wp-block-image size-large is-resized"><img src="https://thewolfsound.com/wp-content/uploads/2019/11/Sine1HzSamples8Hz-2-1024x723.png" alt="" class="wp-image-156" width="350" height="250" /><figcaption>1 Hz sine sampled with sample rate equal to 8 Hz. Red dots mark the samples taken. Clearly the original signal can be reconstructed.</figcaption></figure>
  </div>
</div>

**Sampling** is the process of measuring and storing values of the observed continuous function<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-a041b68ebbaa6df4e193ec93fb94e088_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#115;&#40;&#116;&#41;" title="Rendered by QuickLaTeX.com" height="18" width="27" style="vertical-align: -4px;" /> at discrete time intervals<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-9664e083f6e632f711cbadf4f4da9d33_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#110;&#84;" title="Rendered by QuickLaTeX.com" height="12" width="24" style="vertical-align: 0px;" /> . From mathematical point of view, we can present it as:

<p class="has-text-align-left">
  <a name="id2915933369"></a>
  
  <p class="ql-center-displayed-equation" style="line-height: 18px;">
    <span class="ql-right-eqno"> (3) </span><span class="ql-left-eqno"> &nbsp; </span><img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-d5479b8527a9f7637501a20aca82693d_l3.png" height="18" width="425" class="ql-img-displayed-equation quicklatex-auto-format" alt="&#92;&#98;&#101;&#103;&#105;&#110;&#123;&#101;&#113;&#117;&#97;&#116;&#105;&#111;&#110;&#42;&#125;&#115;&#95;&#123;&#100;&#105;&#115;&#99;&#114;&#101;&#116;&#101;&#125;&#40;&#110;&#41;&#32;&#61;&#32;&#115;&#95;&#123;&#99;&#111;&#110;&#116;&#105;&#110;&#117;&#111;&#117;&#115;&#125;&#40;&#116;&#41;&#32;&#112;&#40;&#116;&#41;&#32;&#61;&#32;&#32;&#115;&#95;&#123;&#99;&#111;&#110;&#116;&#105;&#110;&#117;&#111;&#117;&#115;&#125;&#40;&#116;&#41;&#32;&#92;&#100;&#101;&#108;&#116;&#97;&#32;&#40;&#116;&#32;&#45;&#32;&#110;&#32;&#84;&#41;&#92;&#101;&#110;&#100;&#123;&#101;&#113;&#117;&#97;&#116;&#105;&#111;&#110;&#42;&#125;" title="Rendered by QuickLaTeX.com" />
  </p>
</p>

where

<p class="ql-center-displayed-equation" style="line-height: 52px;">
  <span class="ql-right-eqno"> (4) </span><span class="ql-left-eqno"> &nbsp; </span><img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-ef63827af7b3b40d848076628083acba_l3.png" height="52" width="173" class="ql-img-displayed-equation quicklatex-auto-format" alt="&#92;&#98;&#101;&#103;&#105;&#110;&#123;&#101;&#113;&#117;&#97;&#116;&#105;&#111;&#110;&#42;&#125;&#112;&#40;&#116;&#41;&#32;&#61;&#32;&#32;&#32;&#92;&#115;&#117;&#109;&#95;&#123;&#110;&#61;&#45;&#92;&#105;&#110;&#102;&#116;&#121;&#125;&#94;&#123;&#43;&#92;&#105;&#110;&#102;&#116;&#121;&#125;&#92;&#100;&#101;&#108;&#116;&#97;&#32;&#40;&#116;&#32;&#45;&#32;&#110;&#32;&#84;&#41;&#92;&#101;&#110;&#100;&#123;&#101;&#113;&#117;&#97;&#116;&#105;&#111;&#110;&#42;&#125;" title="Rendered by QuickLaTeX.com" />
</p>

is called an a _sampling function_ or an _impulse-train_ (a series of discrete Dirac impulses spaced at time intervals<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-f9ed275b0bf1633b7ee83b78fcc28273_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#84;" title="Rendered by QuickLaTeX.com" height="12" width="13" style="vertical-align: 0px;" /> ). In the equations above,<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-b4e3cbf5d4c5c6d9b702dd139f14c147_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#116;" title="Rendered by QuickLaTeX.com" height="12" width="6" style="vertical-align: 0px;" /> is the continuous time, whereas<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-b170995d512c659d8668b4e42e1fef6b_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#110;" title="Rendered by QuickLaTeX.com" height="8" width="11" style="vertical-align: 0px;" /> is the index of the sample taken. Discrete Dirac&#8217;s delta<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-2d8a857f6b6e8b7855e709be558e3ef5_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#92;&#100;&#101;&#108;&#116;&#97;&#32;&#40;&#120;&#41;" title="Rendered by QuickLaTeX.com" height="18" width="32" style="vertical-align: -4px;" /> is equal to<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-4868771cbc422b5818f85500909ce433_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#49;" title="Rendered by QuickLaTeX.com" height="13" width="7" style="vertical-align: -1px;" /> if<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-ede05c264bba0eda080918aaa09c4658_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#120;" title="Rendered by QuickLaTeX.com" height="8" width="10" style="vertical-align: 0px;" /> is equal to<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-a5e437be25f29374d30f66cd46adf81c_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#48;" title="Rendered by QuickLaTeX.com" height="12" width="9" style="vertical-align: 0px;" /> and<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-a5e437be25f29374d30f66cd46adf81c_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#48;" title="Rendered by QuickLaTeX.com" height="12" width="9" style="vertical-align: 0px;" /> everywhere else:

<p class="ql-center-displayed-equation" style="line-height: 54px;">
  <span class="ql-right-eqno"> (5) </span><span class="ql-left-eqno"> &nbsp; </span><img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-79259232557fc5c2f7ade92b855e8432_l3.png" height="54" width="174" class="ql-img-displayed-equation quicklatex-auto-format" alt="&#92;&#98;&#101;&#103;&#105;&#110;&#123;&#101;&#113;&#117;&#97;&#116;&#105;&#111;&#110;&#42;&#125;&#92;&#100;&#101;&#108;&#116;&#97;&#32;&#40;&#120;&#41;&#32;&#61;&#32;&#92;&#98;&#101;&#103;&#105;&#110;&#123;&#99;&#97;&#115;&#101;&#115;&#125;&#49;&#32;&#38;&#32;&#92;&#113;&#117;&#97;&#100;&#92;&#116;&#101;&#120;&#116;&#123;&#105;&#102;&#32;&#125;&#32;&#120;&#32;&#61;&#32;&#48;&#32;&#32;&#92;&#92;&#48;&#32;&#38;&#32;&#92;&#113;&#117;&#97;&#100;&#92;&#116;&#101;&#120;&#116;&#123;&#105;&#102;&#32;&#125;&#32;&#120;&#32;&#92;&#110;&#101;&#32;&#48;&#32;&#32;&#92;&#92;&#92;&#101;&#110;&#100;&#123;&#99;&#97;&#115;&#101;&#115;&#125;&#92;&#101;&#110;&#100;&#123;&#101;&#113;&#117;&#97;&#116;&#105;&#111;&#110;&#42;&#125;" title="Rendered by QuickLaTeX.com" />
</p>

so the right hand side expression in (ref{eq:sampling}) is equal to<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-a5e437be25f29374d30f66cd46adf81c_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#48;" title="Rendered by QuickLaTeX.com" height="12" width="9" style="vertical-align: 0px;" /> unless<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-9b470f1001b56cd887eff171807c3de7_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#116;&#32;&#61;&#32;&#110;&#84;" title="Rendered by QuickLaTeX.com" height="12" width="54" style="vertical-align: 0px;" /> .<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-f9ed275b0bf1633b7ee83b78fcc28273_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#84;" title="Rendered by QuickLaTeX.com" height="12" width="13" style="vertical-align: 0px;" /> is called the _sampling period_ and is equal to the reciprocal of the _sampling frequency_:

<p class="ql-center-displayed-equation" style="line-height: 36px;">
  <span class="ql-right-eqno"> (6) </span><span class="ql-left-eqno"> &nbsp; </span><img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-804505f2386a2da1d867ab842ef04001_l3.png" height="36" width="54" class="ql-img-displayed-equation quicklatex-auto-format" alt="&#92;&#98;&#101;&#103;&#105;&#110;&#123;&#101;&#113;&#117;&#97;&#116;&#105;&#111;&#110;&#42;&#125;&#102;&#95;&#115;&#32;&#61;&#32;&#92;&#102;&#114;&#97;&#99;&#123;&#49;&#125;&#123;&#84;&#125;&#92;&#101;&#110;&#100;&#123;&#101;&#113;&#117;&#97;&#116;&#105;&#111;&#110;&#42;&#125;" title="Rendered by QuickLaTeX.com" />
</p>

**Sampling frequency** (or **sampling rate**) is the number of samples of the continuous function (signal) we observe during one second. It is expressed in Hz (<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-56f3096c4cfcac2ff29e4aab6a43dcbe_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#92;&#102;&#114;&#97;&#99;&#123;&#49;&#125;&#123;&#115;&#125;" title="Rendered by QuickLaTeX.com" height="22" width="7" style="vertical-align: -6px;" />).

Sampling rate is one of the most fundamentals parameters of any digital system we work with. It determines the behavior of many algorithms and the way we process sound. Most importantly, it specifies how we store and reproduce the sound.

A theorem of utmost importance is the _sampling theorem_.

## The sampling theorem

If<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-71bb6069be79963fa181192fd4c18b4f_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#102;&#95;&#123;&#109;&#97;&#120;&#125;" title="Rendered by QuickLaTeX.com" height="16" width="36" style="vertical-align: -4px;" /> is the maximum frequency in the observed signal<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-a041b68ebbaa6df4e193ec93fb94e088_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#115;&#40;&#116;&#41;" title="Rendered by QuickLaTeX.com" height="18" width="27" style="vertical-align: -4px;" /> , it can be uniquely represented by a discrete sequence<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-d5e10cbada5d6be0f6bb3b8062661dc7_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#115;&#40;&#110;&#84;&#41;" title="Rendered by QuickLaTeX.com" height="18" width="45" style="vertical-align: -4px;" /> if

<p class="has-text-align-center">
  <p class="ql-center-displayed-equation" style="line-height: 36px;">
    <span class="ql-right-eqno"> (7) </span><span class="ql-left-eqno"> &nbsp; </span><img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-09d968c4b005ca88b382bf53e5cad9d3_l3.png" height="36" width="84" class="ql-img-displayed-equation quicklatex-auto-format" alt="&#92;&#98;&#101;&#103;&#105;&#110;&#123;&#101;&#113;&#117;&#97;&#116;&#105;&#111;&#110;&#42;&#125;&#102;&#95;&#123;&#109;&#97;&#120;&#125;&#32;&#60;&#32;&#92;&#102;&#114;&#97;&#99;&#123;&#102;&#95;&#115;&#125;&#123;&#50;&#125;&#44;&#92;&#101;&#110;&#100;&#123;&#101;&#113;&#117;&#97;&#116;&#105;&#111;&#110;&#42;&#125;" title="Rendered by QuickLaTeX.com" />
  </p>
</p>

where<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-a888294c1312057cfc47f87d3455578b_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#116;&#32;&#92;&#105;&#110;&#32;&#92;&#109;&#97;&#116;&#104;&#98;&#98;&#123;&#82;&#125;" title="Rendered by QuickLaTeX.com" height="13" width="41" style="vertical-align: -1px;" /> ,<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-99d1c594479400a10d54e8668db60c41_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#110;&#32;&#92;&#105;&#110;&#32;&#92;&#109;&#97;&#116;&#104;&#98;&#98;&#123;&#90;&#125;" title="Rendered by QuickLaTeX.com" height="13" width="44" style="vertical-align: -1px;" /> and<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-76ecdcc71175854cf39974ec7add250d_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#84;&#32;&#61;&#32;&#92;&#102;&#114;&#97;&#99;&#123;&#49;&#125;&#123;&#102;&#95;&#115;&#125;" title="Rendered by QuickLaTeX.com" height="25" width="52" style="vertical-align: -9px;" /> .

What sampling theorem says, is that you need to take at least 3 samples per function&#8217;s period in order to be able to restore it to the continuous form. How the restoration will not be explained here.

This theorem goes by many names, among which different combinations of names Nyquist, Shannon and Kotelnikov are used. Its significance can be seen in its multiple corollaries and many applications, also in sound programming.

The quantity of<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-a593f0d1f67ebfe0ee1a026824cfe6df_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#92;&#102;&#114;&#97;&#99;&#123;&#102;&#95;&#115;&#125;&#123;&#50;&#125;" title="Rendered by QuickLaTeX.com" height="23" width="14" style="vertical-align: -6px;" /> is referred to as _Nyquist frequency_. In general, the signal we wish to observe, should not contain frequencies above the Nyquist frequency. Otherwise our sampling is prone to _aliasing_ which will be explained in another article. Suffice it to say, that it disturbes our view of the signal.

## Quantization

Not only we are not able to store continuous functions directly on digital machines, but we also fail to represent all its values precisely. **Quantization** describes, which values can we store adequately.

**Quantization in time** directly follows from the sampling methodology. We are only able to sample as fast as our _analog-to-digital_ _converters_ (ADCs) let us. From a practical perspective, it is quite desirable to have evenly spaced samples, rather than intervals of varying length between successive samples. It lets us analyze the signal more easily and apply various mathematical operations (e.g. we are able to formulate it with the use of the impulse-train function<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-c7bd0d6cbbf9516f73e9757ea88a7b85_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#112;&#40;&#116;&#41;" title="Rendered by QuickLaTeX.com" height="18" width="29" style="vertical-align: -4px;" /> ).

**Quantization in amplitude** restricts the precision of our observation in the value of the samples we take. It starts in ADCs and can be changed throughout the digital system. Whenever we change quantization to a less fine-grained system, we lose information.

On a machine samples&#8217; values can be stored as _integers_ (integer numbers of range specified by the number of bits used to represent them) or _floating-point numbers_ (capable of capturing very small as well as very large quantities). The former can be met in programming under the names of _short, int, long_ and the latter as _float_ or _double_. It is not within the scope of this article to explain the above-mentioned formats, but all of them are well-documented throughout the web.

Having discussed the basics of sampling and quantization, we are ready to put them into practice!

## Sampling code example

This example code samples a 1 Hz sine with the sample rate of 8 Hz and displays the results:

<pre class="brush: python; title: ; notranslate" title="">#!/usr/bin/env python3
"""Example of sine sampling"""
import numpy as np
import matplotlib.pyplot as plt
__author__  = "Jan Wilczek"
__license__ = "GPL"
__version__ = "1.0.0"

# Plotting parameters
plt.rcParams.update({'font.size': 18})
xlim = [-0.01, 1.01]
yticks = [-1.0, 0.0, 1.0]

def signal(A, f, t):
    """
    :param A: amplitude
    :param f: frequency in Hz
    :param t: time in s
    :return: sine with amplitude A at frequency f over time t
    """
    return A * np.sin(2 * np.pi * f * t)

# Observed signal's parameters
A = 1       # amplitude
f = 1       # frequency of the observed signal in Hz
fs = 48000  # basic sampling rate in Hz, to make observed signal seem "continuous"

# Signal's generation
t = np.linspace(0, 1, fs)   # "continuous" time in s
s_t = signal(A, f, t)

plt.figure(figsize=(10,7))
plt.title(f'Sine to be sampled at f={f} Hz')
plt.plot(t, s_t, linewidth=3)
plt.hlines(0, xmin=xlim[0], xmax=xlim[1], colors='black')
plt.xlim(xlim)
plt.xlabel('t [s]')
plt.ylabel('s(t)')
plt.yticks(yticks)
plt.show()

# The sample rate we are sampling the observed signal with
sample_rate = 8     # Hz

# Actual sampling
sampled_time = np.linspace(0, 1, sample_rate)
sampled_signal = signal(A, f, sampled_time)

plt.figure(figsize=(10,7))
plt.title(f'Sampled sine at f={f} Hz sampled at fs={sample_rate} Hz')
plt.plot(t, s_t, linewidth=3)
plt.stem(sampled_time, sampled_signal, linefmt='r-', markerfmt='ro', basefmt=' ')
plt.hlines(0, xmin=xlim[0], xmax=xlim[1])
plt.xlim(xlim)
plt.xlabel('t [s]')
plt.ylabel('s(t)')
plt.yticks(yticks)
plt.show()
</pre>

You can copy the above code and run it yourself!

Reference:  
[1] Oppenheim, A. V. and Willsky, A. S. Signals & Systems. 2nd ed. Upper Sadle River, New Jersey: Prentice Hall, 1997.

<!--themify-builder:block-->