---
id: 249
title: 'Creating the slow motion audio effect: variable speed replay algorithm.'
date: 2019-12-16T09:59:31+00:00
author: Jan Wilczek
excerpt: Do you remember the slowdown of time in "Inception"? How to create such a slow motion effect in the audio domain?
layout: post
guid: https://thewolfsound.com/?p=249
permalink: /creating-the-slow-motion-audio-effect-variable-speed-replay-algorithm/
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
image: /wp-content/uploads/2019/12/thumbnail.png
categories:
  - Audio FX
  - Digital Signal Processing
tags:
  - audio
  - dsp
  - fx
  - slow motion
---

<iframe width="560" height="315" src="https://www.youtube.com/embed/HuYc0azu00s" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/DAbXW6Nbvu0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Do you remember the slowdown of time in &#8220;Inception&#8221;? Or the &#8220;bullet time&#8221; in &#8220;The Matrix&#8221;? How to create such a slow motion effect in the audio domain? That is the topic of today&#8217;s article!

In this article we will prove the usefulness of the sampling theory in music and audio effects. If you don&#8217;t know what sampling is all about check out [this](https://thewolfsound.com/how-to-represent-digital-sound-sampling-sampling-rate-quantization/) article. If you need a revision on aliasing check out [this](https://thewolfsound.com/what-is-aliasing-what-causes-it-how-to-avoid-it/) article.

## Decimation in time

What would happen if we removed every other sample from the signal? To simplify things, let&#8217;s look at an example.

Here we have a 500 Hz sine wave sampled at 16 kHz:

<div class="wp-block-image">
  <figure class="aligncenter size-large is-resized"><img src="https://thewolfsound.com/wp-content/uploads/2019/12/Sine500HzSampled16000.0HzOriginal-1024x741.png" alt="" class="wp-image-292" width="768" height="556" srcset="https://thewolfsound.com/wp-content/uploads/2019/12/Sine500HzSampled16000.0HzOriginal-1024x741.png 1024w, https://thewolfsound.com/wp-content/uploads/2019/12/Sine500HzSampled16000.0HzOriginal-300x217.png 300w, https://thewolfsound.com/wp-content/uploads/2019/12/Sine500HzSampled16000.0HzOriginal-768x556.png 768w, https://thewolfsound.com/wp-content/uploads/2019/12/Sine500HzSampled16000.0HzOriginal-1536x1112.png 1536w, https://thewolfsound.com/wp-content/uploads/2019/12/Sine500HzSampled16000.0HzOriginal.png 1884w" sizes="(max-width: 768px) 100vw, 768px" /><figcaption>500 Hz sine sampled at 16,000 Hz.</figcaption></figure>
</div>

Let&#8217;s note, that one period is 2 ms long.

Removing every second sample we obtain:

<div class="wp-block-image">
  <figure class="aligncenter size-large is-resized"><img src="https://thewolfsound.com/wp-content/uploads/2019/12/Sine500HzSampled16000.0HzDecimated-1024x741.png" alt="" class="wp-image-293" width="768" height="556" srcset="https://thewolfsound.com/wp-content/uploads/2019/12/Sine500HzSampled16000.0HzDecimated-1024x741.png 1024w, https://thewolfsound.com/wp-content/uploads/2019/12/Sine500HzSampled16000.0HzDecimated-300x217.png 300w, https://thewolfsound.com/wp-content/uploads/2019/12/Sine500HzSampled16000.0HzDecimated-768x556.png 768w, https://thewolfsound.com/wp-content/uploads/2019/12/Sine500HzSampled16000.0HzDecimated-1536x1112.png 1536w, https://thewolfsound.com/wp-content/uploads/2019/12/Sine500HzSampled16000.0HzDecimated.png 1884w" sizes="(max-width: 768px) 100vw, 768px" /><figcaption>The signal after removing every other sample.</figcaption></figure>
</div>

We can see, that the duration of the sine shrunk to 2.5 ms, what is no surprise, since we basically removed half of the signal and 2.5 ms corresponds to half of 5 ms.

But if duration changed, with sample rate remaining constant, the frequency changed as well! The new period length is 1 ms, so the frequency of the sine is not 500 Hz anymore, but<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-7085c429d24db9117e309f7c9152f53d_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#92;&#102;&#114;&#97;&#99;&#123;&#49;&#125;&#123;&#48;&#46;&#48;&#48;&#49;&#125;&#32;&#61;&#32;&#49;&#48;&#48;&#48;" title="Rendered by QuickLaTeX.com" height="23" width="93" style="vertical-align: -7px;" /> Hz!

The process of removing particular samples is called **decimation** or **downsampling** and here we performed decimation with **decimation factor** equal to 2 (2 times less samples). It sometimes involves the **antialiasing filter**, which will be explained below in more detail.

## Tape replay

If you ever rewinded a cassette magnetic tape, you were able to hear a quickened version of the recording, what enabled you to find the exact spot you wanted to hear. That&#8217;s exactly the same effect you can witness by sample decimation.

We can view that change in the signal as though the **replay sample rate has changed**. If we output the samples with two times the original sample rate we will run out of samples in half of the duration of the original signal, since we are outputting twice as many samples per second as before.

### Mathematical formulation

We may express it in mathematical terms as the length of the output signal&#8217;s period in seconds:

<a name="id4093198884"></a>

<p class="ql-center-displayed-equation" style="line-height: 37px;">
  <span class="ql-right-eqno"> (1) </span><span class="ql-left-eqno"> &nbsp; </span><img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-44a34fab5c5a1c6f50a6e2cc4135e7b9_l3.png" height="37" width="105" class="ql-img-displayed-equation quicklatex-auto-format" alt="&#92;&#98;&#101;&#103;&#105;&#110;&#123;&#101;&#113;&#117;&#97;&#116;&#105;&#111;&#110;&#42;&#125;&#84;&#95;&#123;&#114;&#101;&#112;&#108;&#97;&#121;&#125;&#32;&#61;&#32;&#92;&#102;&#114;&#97;&#99;&#123;&#84;&#95;&#123;&#105;&#110;&#125;&#125;&#123;&#118;&#125;&#44;&#32;&#92;&#101;&#110;&#100;&#123;&#101;&#113;&#117;&#97;&#116;&#105;&#111;&#110;&#42;&#125;" title="Rendered by QuickLaTeX.com" />
</p>

where<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-1f2e39685fb18d9d52545792cb558b48_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#84;&#95;&#123;&#114;&#101;&#112;&#108;&#97;&#121;&#125;" title="Rendered by QuickLaTeX.com" height="18" width="49" style="vertical-align: -6px;" /> is the time period of the output signal,<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-a47abc60c2c43f32db1b5912a7f64e9f_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#84;&#95;&#123;&#105;&#110;&#125;" title="Rendered by QuickLaTeX.com" height="15" width="23" style="vertical-align: -3px;" /> is the time period of the original signal and<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-ef71511c70f0e4b25cc6bd69f3bc20c2_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#118;" title="Rendered by QuickLaTeX.com" height="8" width="9" style="vertical-align: 0px;" /> is the relative speed of the &#8220;tape&#8221; (i.e., how many times quicker we output the sound) compared to the original or default. For instance, playing the sound two times faster (<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-54f591239b2a5c66bd279a7d507af6fe_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#118;&#32;&#61;&#32;&#50;" title="Rendered by QuickLaTeX.com" height="12" width="41" style="vertical-align: 0px;" />) produces a two times shorter waveform at the output (of time period length equal to<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-c3d8f6e9cf14328942a24d0005a9d89b_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#92;&#102;&#114;&#97;&#99;&#123;&#84;&#95;&#123;&#105;&#110;&#125;&#125;&#123;&#50;&#125;" title="Rendered by QuickLaTeX.com" height="22" width="21" style="vertical-align: -6px;" /> seconds).

Converting to the frequency domain means taking the reciprocal of equation<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-100f1d6087cdb62de24299faa0a71e55_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#92;&#114;&#101;&#102;&#123;&#101;&#113;&#58;&#118;&#115;&#114;&#95;&#116;&#105;&#109;&#101;&#125;" title="Rendered by QuickLaTeX.com" height="12" width="18" style="vertical-align: 0px;" /> what results in the following frequency scaling:

<a name="id3427098436"></a>

<p class="ql-center-displayed-equation" style="line-height: 18px;">
  <span class="ql-right-eqno"> (2) </span><span class="ql-left-eqno"> &nbsp; </span><img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-972433ad3a4b25a7dc038a5edc4141c2_l3.png" height="18" width="107" class="ql-img-displayed-equation quicklatex-auto-format" alt="&#92;&#98;&#101;&#103;&#105;&#110;&#123;&#101;&#113;&#117;&#97;&#116;&#105;&#111;&#110;&#42;&#125;&#102;&#95;&#123;&#114;&#101;&#112;&#108;&#97;&#121;&#125;&#32;&#61;&#32;&#102;&#95;&#123;&#105;&#110;&#125;&#32;&#118;&#44;&#92;&#101;&#110;&#100;&#123;&#101;&#113;&#117;&#97;&#116;&#105;&#111;&#110;&#42;&#125;" title="Rendered by QuickLaTeX.com" />
</p>

where<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-9efd10ba8a637c317a2e987b1c884ad2_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#102;&#95;&#123;&#114;&#101;&#112;&#108;&#97;&#121;&#125;" title="Rendered by QuickLaTeX.com" height="18" width="47" style="vertical-align: -6px;" /> denotes the frequency of the output signal given the frequency of the input signal<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-bae22e6dde50028bb9a9d259adc81788_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#102;&#95;&#123;&#105;&#110;&#125;" title="Rendered by QuickLaTeX.com" height="16" width="22" style="vertical-align: -4px;" /> and the scaling (replay speed)<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-ef71511c70f0e4b25cc6bd69f3bc20c2_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#118;" title="Rendered by QuickLaTeX.com" height="8" width="9" style="vertical-align: 0px;" /> . This result is very descriptive, because it basically says, that the frequency of the transformed signal will be scaled along with<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-ef71511c70f0e4b25cc6bd69f3bc20c2_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#118;" title="Rendered by QuickLaTeX.com" height="8" width="9" style="vertical-align: 0px;" /> .

### Possible ways to rescale signal&#8217;s time

How can we achieve the effect of variable speed replay using digital devices rather than a tape player? There are basically two ways:

  * change the sampling frequency of the DAC (e.g., in a stage setting),
  * resample the signal before output.

As this is a blog about audio _programming_ we will deal with the second option, namely the **variable speed replay algorithm.**

## Variable speed replay algorithm

Assuming that<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-ef71511c70f0e4b25cc6bd69f3bc20c2_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#118;" title="Rendered by QuickLaTeX.com" height="8" width="9" style="vertical-align: 0px;" /> can be displayed as a ratio of integer numbers<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-333959b06439ff4e227bb8868be76497_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#118;&#32;&#61;&#32;&#92;&#102;&#114;&#97;&#99;&#123;&#78;&#125;&#123;&#77;&#125;" title="Rendered by QuickLaTeX.com" height="22" width="50" style="vertical-align: -6px;" /> , the schema of the variable speed replay algorithm is as follows:<figure class="wp-block-image size-large">

<img src="https://thewolfsound.com/wp-content/uploads/2019/12/VariableSpeedReplayScheme-1024x223.png" alt="" class="wp-image-300" srcset="https://thewolfsound.com/wp-content/uploads/2019/12/VariableSpeedReplayScheme-1024x223.png 1024w, https://thewolfsound.com/wp-content/uploads/2019/12/VariableSpeedReplayScheme-300x65.png 300w, https://thewolfsound.com/wp-content/uploads/2019/12/VariableSpeedReplayScheme-768x167.png 768w, https://thewolfsound.com/wp-content/uploads/2019/12/VariableSpeedReplayScheme-1536x334.png 1536w, https://thewolfsound.com/wp-content/uploads/2019/12/VariableSpeedReplayScheme-2048x445.png 2048w" sizes="(max-width: 1024px) 100vw, 1024px" /> <figcaption>Variable speed replay algorithm scheme.</figcaption></figure> 

Here<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-5983fd41f37601a428f9cbb2c59829d7_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#115;&#95;&#123;&#105;&#110;&#125;&#40;&#116;&#41;" title="Rendered by QuickLaTeX.com" height="18" width="41" style="vertical-align: -4px;" /> and<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-10b0267a34d9544f86b6301cc6fc88b2_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#115;&#95;&#123;&#111;&#117;&#116;&#125;&#40;&#116;&#41;" title="Rendered by QuickLaTeX.com" height="18" width="48" style="vertical-align: -4px;" /> denote discrete-time input and output signals respectively,<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-6b075c9bf2aaf4bda5700c368152dc68_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#102;&#95;&#99;" title="Rendered by QuickLaTeX.com" height="16" width="15" style="vertical-align: -4px;" /> the cutoff frequency of the low-pass filter,<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-8672b0e2192d97d6cd1fc6e3bdf45936_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#102;&#95;&#123;&#115;&#44;&#32;&#105;&#110;&#125;" title="Rendered by QuickLaTeX.com" height="18" width="32" style="vertical-align: -6px;" /> sample rate of the input signal, and<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-10ebb71bad275c1815a8f2a8c5dea0be_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#77;" title="Rendered by QuickLaTeX.com" height="12" width="19" style="vertical-align: 0px;" /> and<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-5793832f979c2268e3694c246d53b1bb_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#78;" title="Rendered by QuickLaTeX.com" height="12" width="16" style="vertical-align: 0px;" /> are integers such that<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-83823bd1f59008275c11ea266f71595f_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#118;&#61;&#92;&#102;&#114;&#97;&#99;&#123;&#78;&#125;&#123;&#77;&#125;" title="Rendered by QuickLaTeX.com" height="22" width="50" style="vertical-align: -6px;" /> . The following subsequent operations are applied to the input signal:

  * upsampling by a factor of M (inserting M-1 zeros after each sample),
  * low-pass filtering with cutoff frequency set to<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-41b2b68504579c7394f7a7dbd2a46e24_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#92;&#102;&#114;&#97;&#99;&#123;&#102;&#95;&#123;&#115;&#44;&#32;&#105;&#110;&#125;&#125;&#123;&#50;&#77;&#125;" title="Rendered by QuickLaTeX.com" height="24" width="29" style="vertical-align: -6px;" /> (to remove the repeated spectral components that were dragged below the Nyquist frequency as a result of lowering the frequency of the repeated digital spectra),
  * low-pass filtering with cutoff frequency set to<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-1b9ae0d914c04aab2bd1bac654f14c6d_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#92;&#102;&#114;&#97;&#99;&#123;&#102;&#95;&#123;&#115;&#44;&#32;&#105;&#110;&#125;&#125;&#123;&#50;&#78;&#125;" title="Rendered by QuickLaTeX.com" height="24" width="29" style="vertical-align: -6px;" /> (to prevent the aliasing of the stretched spectra, since all repeated spectral components will be stretched by downsampling),
  * downsampling by a factor of N (removing N-1 samples from each block of N samples, exactly what we did to our 500 Hz sine).

Note the usage of low-pass filters. They are crucial to prevent any additional components from appearing in the processed signal&#8217;s spectrum. So whether we are raising the frequency or we are lowering it, we must always filter, to remove the extra components interfering with our original signal. 

Upsampling is performed first, because downsampling (removing certain samples) may be considered a removal of information, therefore it&#8217;s done best at the end of processing.

All in all, this scheme is a typical resampling scheme. The only difference in the variable speed replay algorithm is that we treat the output signal, as if it still had the original sample rate<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-8672b0e2192d97d6cd1fc6e3bdf45936_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#102;&#95;&#123;&#115;&#44;&#32;&#105;&#110;&#125;" title="Rendered by QuickLaTeX.com" height="18" width="32" style="vertical-align: -6px;" /> and thus the difference in pitch when playing it out.

## The outcome of variable speed replay application

We can reason about the result of such signal rescaling in two domains: time and frequency.

### Modified frequency structure

The frequency structure changes with the scaling accordingly:

  * if we are quickening the signal (scaling the time speed up) we receive a &#8220;Mickey Mouse&#8221; or a &#8220;Chipmunk&#8221; effect (especially powerful when applied to speech),
  * if we are slowing the signal (scaling the time speed down) we perceive a &#8220;slow motion&#8221; effect (exactly like the one in &#8220;Inception&#8221; or &#8220;The Matrix&#8221;)

### Modified time structure

The time structure is altered with the following perceivable changes:

  * the transients are spread (slower) or contracted (more rapid),
  * the vibrato technique (changing the frequency of the instrument in a certain range around the played note) loses its characteristics: it becomes a slower (when slowing down time) or faster modulation.

### Negative speed?!

If we set<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-27026c55c532b7eaf7be698a38f1a529_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#118;&#61;&#45;&#49;" title="Rendered by QuickLaTeX.com" height="13" width="55" style="vertical-align: -1px;" /> we get&#8230; a time-reversed signal! This technique is extremely powerful, especially in experimental or progressive music, e.g. solo on &#8220;[Misunderstood](https://www.youtube.com/watch?v=mdpCnRSeshU)&#8221; by Dream Theater has been time-reversed (check out the whole story on [Wikipedia](https://en.wikipedia.org/wiki/Six_Degrees_of_Inner_Turbulence)) or ending of &#8220;[A Day in the Life](https://www.youtube.com/watch?v=UYeV7jLBXvA)&#8221; by The Beatles, where one can hear reversed recordings being played in a loop.

Keeping the<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-ef71511c70f0e4b25cc6bd69f3bc20c2_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#118;" title="Rendered by QuickLaTeX.com" height="8" width="9" style="vertical-align: 0px;" /> &#8216;s value negative we can change the scaling of the inversed time signal&#8230; What gives an enormous amount of possibilities! Check out [this example in Ludger Brümmer&#8217;s &#8220;The Gates Of H&#8221;](https://youtu.be/ea4USmvezl0?t=106) musique concreté piece.

Above examples show that **variable speed replay algorithm is a creative application of the sampling theory**.

## Unity Time.timeScale correspondence

If you ever worked with the Unity Editor, you may have stumbled upon the _Time.timeScale_ parameter. It basically changes the speed at which things are happening. If set to 1 the time flows normally, however, if you decrease it to 0.5 the events happen two times slower, so the _Time.timeScale_ parameter corresponds to the<img src="https://thewolfsound.com/wp-content/ql-cache/quicklatex.com-ef71511c70f0e4b25cc6bd69f3bc20c2_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#118;" title="Rendered by QuickLaTeX.com" height="8" width="9" style="vertical-align: 0px;" /> parameter in the variable speed replay algorithm. It doesn&#8217;t change the pitch and time duration of audio though, but&#8230; you could do that using the algorithm described here! Actually that&#8217;s what the _pitch_ parameter of _AudioSource_ component does: it changes pitch **and** time simultaneously, taking advantage of the Variable Speed Replay algorithm. Read the corresponding Unity manual parts [here](https://docs.unity3d.com/ScriptReference/Time-timeScale.html) for the _timeScale_ parameter and [here](https://docs.unity3d.com/ScriptReference/AudioSource-pitch.html) for the _pitch_ parameter.

_Note: the Time.timeScale parameter also does not change the rate at which physics engine is updating. Thus the corresponding Time.fixedDeltaTime parameter should be updated accordingly (typically Time.fixedDeltaTime = 0.02f * Time.timeScale, where 0.02f denotes the typical default value of Time.fixedDeltaTime, but it can be different of course)._

## Time scaling preserving pitch

It is not trivial to scale the signal in time without altering the pitch (i.e. to lengthen or shorten the signal). Here, a variety of Overlap-Add methods apply, which are beyond the scope of this article. However, they are likely to appear in the future WolfSound&#8217;s articles, so stay tuned!

## Summary

We have discussed the variable speed replay algorithm, which enables to manipulate the relative feeling of time flow in the signal and explored its consequences and applications.

If you want to learn more I highly encourage you to check out this book &#8220;Digital Audio FX&#8221; by Udo Zölzer et. al.:

<a target="_blank" href="https://www.amazon.com/gp/product/0470665998/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0470665998&linkCode=as2&tag=wolfsound-20&linkId=7934fe656d8291d10cddaa0a7598f2ba" rel="noopener noreferrer"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=0470665998&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL250_&tag=wolfsound-20" /></a><img src="//ir-na.amazon-adsystem.com/e/ir?t=wolfsound-20&l=am2&o=1&a=0470665998" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /> 

It contains an even broader perspective on the variable speed replay algorithm and many more; it is one of the best books to learn about audio algorithms!

## Code example

The following code is a command-line tool to create the slow-motion or &#8216;chipmunk&#8217; sound effect. The &#8216;crude&#8217; version is a direct implementation of the algorithm as presented on the scheme above, the &#8216;smart&#8217; version uses the resampling facility of SciPy and is significantly faster.

<pre class="brush: python; title: ; notranslate" title="">#!/usr/bin/env python3
"""
Variable speed replay algorithm implementation.

A command-line tool that processes the supplied wave file and plays out the result.
"""
import argparse
from scipy.io.wavfile import read
from scipy.signal import resample, butter, lfilter
import sounddevice as sd
import numpy as np
__author__  = "Jan Wilczek"
__license__ = "GPL"
__version__ = "1.0.0"


def parse_args():
    parser = argparse.ArgumentParser(description='Apply the Variable Speed Replay algorithm to an audio file '
                                                 'and play it out.')
    parser.add_argument('-f', '--filename', type=str, required=True, help='filename of the wave file to process',
                        dest='filename')
    parser.add_argument('-N', type=int, required=True, help='numerator of the time scale parameter (v = N / M)',
                        dest='N')
    parser.add_argument('-M', type=int, required=True, help='denominator of the time scale parameter (v = N / M)',
                        dest='M')
    parser.add_argument('-c', '--crude', dest='process_frame', action='store_const', const=process_frame_crude,
                        default=process_frame_smart,
                        help='process each frame with brute force implementation '
                        '(default: process each frame optimally)')
    return parser.parse_args()

def read_and_preprocess_file(filename):
    sample_rate, data = read(filename)
    data = data[:, 0]                           # extract first channel
    normalized_data = data / np.amax(abs(data)) # convert to [-1, 1] range
    return sample_rate, normalized_data

def play_samples_blocking(samples, sample_rate, volume=1.0):
    sd.play(volume * samples, samplerate=sample_rate)
    sd.wait()

def upsample(frame, M):
    M_minus_1_zeros = (M - 1) * [0.0]
    for i in range(1, len(frame)):
        next_sample_id = (i-1) * M + 1
        frame = np.insert(frame, next_sample_id, M_minus_1_zeros)
    return frame

def filter_frame(frame, nyquist_frequency, M, N):
    order = 5
    cutoff_frequency = min(nyquist_frequency / M, nyquist_frequency / N)
    normalized_cutoff = cutoff_frequency / nyquist_frequency
    b, a = butter(order, normalized_cutoff, btype='low', analog=False)
    return lfilter(b, a, frame)

def downsample(frame, N):
    return [frame[i] for i in range(0, len(frame)) if i % N == 0]

def process_frame_crude(frame, M, N, fs):
    upsampled = upsample(frame, M)
    filtered = filter_frame(upsampled, fs / 2, M, N)
    downsampled = downsample(filtered, N)
    return downsampled

def process_frame_smart(frame, M, N, _):
    return resample(frame, int(len(frame) / (N / M)))

def variable_speed_replay(samples, fs, M, N, process_frame_function, frame_size=16384):
    if N / M == 1:
        return samples

    output = np.empty((0,))
    for i in range(0, len(samples), frame_size):
        end = min(i + frame_size, len(samples))
        resampled_frame = process_frame_function(samples[i:end], M, N, fs)
        output = np.append(output, resampled_frame)
    return output


if __name__ == '__main__':
    args = parse_args()

    sample_rate, data = read_and_preprocess_file(args.filename)

    transformed = variable_speed_replay(data, sample_rate, args.M, args.N, args.process_frame)

    play_samples_blocking(transformed, sample_rate, volume=0.4)

</pre>

Feel free to copy and test out the above code. If you are not sure how to use it, then run `variable_speed_replay.py --help` (assuming you copied the code into &#8216;variable\_speed\_replay.py&#8217; file) and follow the instructions given.

## References

[1] Zölzer, U. DAFX: Digital Audio Effects. 2nd ed. Helmut Schmidt University – University  
of the Federal Armed Forces, Hamburg, Germany: John Wiley & Sons Ltd, 2011.



<!--themify-builder:block-->