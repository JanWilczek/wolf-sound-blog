---
title: "JUCE Framework with vcpkg: Quick Guide to C++ Dependency Management"
description: "Learn how to use the JUCE framework with vcpkg for efficient C++ dependency management. Follow this step-by-step guide to easily integrate JUCE into your audio plugin or C++ application projects."
date: 2024-08-04
author: Jan Wilczek
layout: post
background: /assets/img/posts/programming-in-general/2024-08-04-how-to-use-juce-with-vcpkg/Thumbnail-1024w.webp
permalink: /using-juce-framework-with-vcpkg-quick-cpp-dependency-management-guide/
categories:
  - C/C++
tags:
  - cpp
  - juce
  - plugin
  - cmake
discussion_id: 2024-08-04-how-to-use-juce-with-vcpkg
---
C++ package management made easy.

If you want to create an audio plugin or a C++ application and you want to use for that purpose the [JUCE C++ framework](https://github.com/juce-framework/JUCE),  you always have the problem of how to include JUCE as a dependency.

You can

- download the sources,
- use git submodules, or
- use a C++ package manager.

One of the most popular C++ package managers is [vcpkg](https://vcpkg.io/en/).

On this blog, I've already covered [how to use JUCE with the CPM package manager]({% post_url collections.posts, 'programming-in-general/2023-08-21-audio-plugin-template' %}).

Today we'll see exactly step by step how to use the vcpkg package manager to have JUCE as a dependency.

## How to use JUCE with vcpkg

1. Init an empty repository
    
    ```bash
    git init .
    ```
    
2. Add vcpkg as a submodule
    
    ```bash
    git submodule add https://github.com/microsoft/vcpkg.git
    git commit -m "Added vcpkg as a submodule"
    ```
    
3. Initialize vcpkg
    
    ```bash
    .\vcpkg\bootstrap-vcpkg.bat -disableMetrics # Windows
    vcpkg/bootstrap-vcpkg.sh -disableMetrics    # macOS, Linus
    ```
    
4. Create the vcpkg manifest
    
    ```bash
    .\vcpkg\vcpkg.exe new --application # Windows
    vcpkg/vcpkg new --application       # macOS, Linux
    ```
    
    - *vcpkg-configuration.json* is the info of the package registry to download packages from
    - *vcpkg.json* is the “manifest”: it’s where your dependencies will be listed
5. Add the JUCE package
    
    ```bash
    .\vcpkg\vcpkg.exe add port juce  # Windows
    vcpkg/vcpkg add port juce        # macOS, Linux
    ```
    
6. Create a top-level *CMakeLists.txt* file
    
    ```bash
    cmake_minimum_required(VERSION 3.22)
    project(JuceVcpkgDemo)
    
    find_package(juce CONFIG REQUIRED)
    ```
    
7. Generate the CMake project with the correct toolchain file.
    
    ```bash
    cmake -S . -B build -DCMAKE_TOOLCHAIN_FILE="vcpkg/scripts/buildsystems/vcpkg.cmake"
    ```
    
    You can simplify this step if you create *CMakePresets.json* file in the root folder:
    
    ```json
    {
      "version": 2,
      "configurePresets": [
        {
          "name": "default",
          "generator": "Visual Studio 17 2022",
          "binaryDir": "${sourceDir}/build",
          "cacheVariables": {
            "CMAKE_TOOLCHAIN_FILE": "vcpkg/scripts/buildsystems/vcpkg.cmake"
          }
        }
      ]
    }
    ```
    
    With *CMakePresets.json*, you can simply run
    
    ```bash
    cmake --preset default
    ```
    
8. Now you are ready to use JUCE. You can follow their [CMake examples](https://github.com/juce-framework/JUCE/tree/master/examples/CMake) to get started, for example,
    1. copy the AudioPlugin folder and
    2. `add_subdirectory(AudioPlugin)` on it in the top-level *CMakeLists.txt*.

**Want create audio plugins with JUCE? Check what you need to know in the [free Audio Developer Checklist]({% link collections.all, 'single-pages/checklist.html' %}).**
