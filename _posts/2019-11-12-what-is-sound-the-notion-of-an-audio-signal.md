---
id: 70
title: What is sound? The notion of an audio signal.
date: 2019-11-12T15:39:14+00:00
author: Jan Wilczek
layout: post
guid: https://thewolfsound.com/?p=70
permalink: /what-is-sound-the-notion-of-an-audio-signal/
themify_used_global_styles:
  - 'a:1:{i:0;s:0:"";}'
tbp_custom_css:
  - ""
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
image: /wp-content/uploads/2019/10/thumbnail_what_is_sound.png
background: /wp-content/uploads/2019/10/thumbnail_what_is_sound.png
categories:
  - Sound in general
tags:
  - audio signal
  - digital audio
  - sound wave
---
<iframe width="560" height="315" src="https://www.youtube.com/embed/Q6NldT7pgEY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Sound is everywhere around us, when we speak, when we listen to music, when we hear traffic noise and even when everything seems to be silent. But what is sound actually? We need to understand this phenomenon before we are able to store it on a machine and process it.

**Sound** is a _mechanical wave_ that travels in an _elastic medium_. Mechanical wave here means, that material particles are involved and the wave results from particles&#8217; interaction. Elastic medium on the other hand is anything that contains particles with the ability to interact. The simplest example is, of course, the air, but an elastic medium may be any other gas, liquid (like water) or even concrete. You probably know, that sound cannot propagate in space-that&#8217;s because there are no particles there to interact.

A source of any sound is a vibrating element. The simplest one you can think of are your own vocal cords. When you speak, you thighten them and as a result of tension being applied by the air flowing through them, they start to vibrate in a rhythmic manner. This initial vibration causes in turn the air to vibrate, i.e., the vibrating element hits the air particles at a particular spot at more or less equal intervals, which in turn causes these particles to hit other ones, which in turn hit the next ones and so on.

How do you hear then? Well, the propagating wave (groups of particles hitting against the others farther and farther from the source) reaches the tympanic membrane in your ear what causes it to vibrate as well. In a series of resulting interactions of various ear elements the vibration is transformed into a neural signal transported into the brain, where it is interpreted. It is of course a simplified description, but for now it suffices.<figure class="wp-block-image is-resized">

![A vibrating object causes the surrounding medium to vibrate. The induced sound wave travels through the medium and reaches receivers: an ear and a microphone. Suitable processing follows.](https://thewolfsound.com/wp-content/uploads/2019/11/img1-1024x685.png)
*The sound as a mechanical wave travelling through the air medium and reaching receivers: an ear and a microphone. Audio processing (by human body or a machine) follows.*

The same mechanism is used to capture the sound through a microphone. The diaphragm of the microphone vibrates under the incident particles what is transformed into electrical voltage at microphone&#8217;s output. Such output may be then recorded and stored.

Whatever the medium is, the sound preserves its characteristics of a wave. The vibrations are changes of placement of the vibrating object. In the air the vibrations are transported by more and less dense groups of particles. At microphone&#8217;s output the vibration is the rising and falling voltage.

Whatever the type of these vibrations, we can always call it a sound wave and plot it against time. The abscissa of such a plot is usually time in units of second or millisecond. The ordinate of such a plot may be pressure (in pascals), voltage (in volts) or displacement from the equilibrium (in meters). However, on a computer, we can assign it an arbitrary unit, because it merely represents the notion of amplitude.

To store the continuous (analog) representation of sound on a computer, we need to transform the signal into the digital domain. To do this, we use the notion of **sampling**, i.e., recording the value of the analog signal at regular time intervals. Sampled sound may be then processed and played through loudspeakers, that in turn change the digial signal into analog one in the form of voltage, that causes the membrane of the speaker to move in a rhythmic manner, that in turn moves the air particles, what enables us to hear the sound again, thus completing the circle of sound-record-store-process-output-sound. 

The topic of sampling and digital representation will be discussed in the next week&#8217;s article, so stick around!
