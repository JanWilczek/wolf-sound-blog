---
title: "How To Build An Audio Plugin With JUCE C++ Framework & CMake In 2023 (With Unit Tests)"
description: "Learn how to easily structure your audio plugin C++ repository and integrate all the libraries that you want with CMake."
date: 2023-08-21
author: Jan Wilczek
layout: post
background: /assets/img/posts/programming-in-general/2023-08-21-audio-plugin-template/Thumbnail.webp
permalink: /how-to-build-audio-plugin-with-juce-cpp-framework-cmake-and-unit-tests/
categories:
  - Programming in general
tags:
  - testing
  - cpp
  - juce
  - cmake
  - plugin
discussion_id: 2023-08-21-audio-plugin-template
custom_js:
 - /assets/vendor/lazyload/lazyload.min.js
 - /assets/js/wolfsound/modules/load_lazyload.js
---
An easy-to-use template to kick-start your every audio plugin C++ project!

{% include 'youtube-video', video_id: 'Uq7Hwt18s3s' %}

Get the [template repository on GitHub.](https://github.com/JanWilczek/audio-plugin-template)

From the video you will learn:

- how to start any audio plugin C++ project
- how to structure your code repository for maximum clarity and productivity
- why using CMake is better than using the Projucer that ships with JUCE
- how to integrate CMake and JUCE (including important compilation flags you shouldn’t miss)
- how to generate a Visual Studio/XCode/Make/etc. project out of your CMake project
- how to effortlessly integrate third-party (external) libraries to your CMake project with the CPM package manager
- how to ensure maximum safety of your code by raising the warning level and treating warnings as errors
- how to build you audio plugin CMake project
- how to introduce unit tests for your audio plugin with GoogleTest
- how to run the unit tests

{% render 'google-ad.liquid' %}
