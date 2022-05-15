---
title: "Lowpass and Highpass Filter Plugin with JUCE Tutorial for Beginners"
description: "Full implementation of a lowpass and highpass filter audio plugin with cutoff control. Contains thoroughly explained source code."
date: 2022-05-17
author: Jan Wilczek
layout: post
images: /assets/img/posts/fx/2022-05-17-lowpass-highpass-filter-plugin-with-juce/
# background: /assets/img/posts/fx/2022-05-17-lowpass-highpass-filter-plugin-with-juce/Thumbnail.webp
categories:
  - Audio FX
tags:
  - filtering 
  - effects
  - JUCE
  - C++
discussion_id: 2022-05-17-lowpass-highpass-filter-plugin-with-juce
---
Let's build a lowpass/highpass filter audio plugin from scratch!

{% capture _ %}{% increment listingId20220517  %}{% endcapture %}

## Introduction

In this article, I will guide you step-by-step through the process of implementing a lowpass/highpass filter audio plugin with the JUCE framework.

The structure, that we are going to implement, is the [allpass-based parametric lowpass/highpass filter from the previous article]({% post_url fx/2022-05-08-allpass-based-lowpass-and-highpass-filters %}). If you want, to understand how this structure works and why is it performing filtering, I invite you to read that article first. This article is purely the implementation of the previously presented algorithm.

## JUCE Framework

The [JUCE framework](https://github.com/juce-framework/JUCE) is a C++ framework for building audio plugins and applications. It is very handy in audio plugin creation because it provides wrappers around specific APIs like VST3 or AAX. Therefore, we can write the plugin code once and simply build for various digital audio workstations (e.g., Reaper, Ableton, ProTools, etc.).

We will use it for convenience.

This tutorial does not assume that you worked in JUCE before.

And if you haven't, you will learn plenty of useful stuff that you can readily apply in professional audio programming market 🙂

So let's start building our plugin!

## Plugin Project Setup in Projucer

After you [install JUCE](https://juce.com/get-juce/download), launch the *Projucer* app and select *File -> New Project*.

<!-- TODO: Projucer image -->

Choose *Plugin->Basic* type, write your *Project Name*, select the target IDE (mine is *Visual Studio 2019*), and click *Create Project*.

You then will have to choose the folder which will contain your project folder (mine is called *JUCEprojects*, since I put there most of my JUCE projects).

At this point, you could already generate your project but you may want to provide some additional metadata. If so, click on the *Project Settings* icon next to the project name.

<!-- TODO: Projucer image -->

For example, I decided to only generate the VST3 plugin format and use the C++ 20 standard.

After you completed the setup, click on *Save and Open in IDE*.

<!-- TODO: Projucer image -->

## JUCE Plugin Project Structure

*If you already know JUCE, you can skip this paragraph.*



## LowpassHighpassFilter Class

## Plugin Processor

## Plugin Editor



