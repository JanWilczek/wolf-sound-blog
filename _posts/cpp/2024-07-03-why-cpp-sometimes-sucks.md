---
title: "Why C++ Sometimes Sucks: 17 Reasons Why C++ Development Is Difficult"
description: "Why is C++ so difficult? What are problems in large-scale C++ development? Learn all the reasons from this post!"
date: 2024-07-03
author: Jan Wilczek
layout: post
background: /assets/img/posts/cpp/2024-07-03-why-cpp-sometimes-sucks/Thumbnail.webp
permalink: /why-cpp-sucks-17-reasons-why-cpp-development-is-difficult/
categories:
  - C/C++
tags:
  - cpp
  - juce
  - plugin
  - software architecture
  - cmake
  - rust
discussion_id: 2024-07-03-why-cpp-sometimes-sucks
custom_js:
 - /assets/vendor/lazyload/lazyload.min.js
 - /assets/js/wolfsound/modules/load_lazyload.js
---
It’s time for a small rant! 😈

{% include 'youtube-video', video_id: 'y37NzWaqpbI' %}

I have recently worked as an architect and a lead developer on a green-field C++ project and I found a few big pain points of C++.

I had been a huge supporter of C++. I read the C++ Programming Language by Bjarne Stroustrup and a few other C++ books but now I have a love-hate relationship with it. I do realize that a lot of these issues are there because of historical reasons and I highly respect C++ for being able to stay in the game for so long.

I've come up with a list to add my voice to the discussion that goes on in the C++ community: I’d love to hear your feedback.

I’m not an expert C++ developer: that probably takes years and even the standard committee members happen to get things wrong. But I’m not a C++ newbie.

I work in audio programming which includes a mix of standard business/UI C++ programming and real-time, high-performance programming.

## Biggest pains of C++ development

1. Compiler support is lagging behind the standard on certain platforms.
    1. Example: as of July the 3rd, 2024, Apple Clang still doesn’t support std::expected, `std::jthread` (joinable thread), or `std::stop_token`.
    2. Surprisingly, Microsoft is in the lead with the C++ standard implementation including C++ modules.
2. Declaration/definition split (header files and source files).
    1. Very elegant solution for old times. Now, doesn’t seem necessary and lengthens the development time significantly (you need to write everything twice).
3. It’s hard/impossible to write C++ modules cross-platform.
4. Slow compilation of templates.
5. Poor compiler messages, especially when using templates. C++ concepts help but there they still require a lot of effort to be understood on compilation error. Rust is better at this.
6. No standard dependency management.
    1. Using [Conan](https://conan.io/) or [vcpkg](https://vcpkg.io/en/) is difficult.
    2. [CPM package manager](https://github.com/cpm-cmake/CPM.cmake) is the most promising and least difficult to set up. [Check out my tutorial on JUCE with CPM setup.]({% post_url collections.posts, 'programming-in-general/2023-08-21-audio-plugin-template.md' %})
    3. No standard “recipes” to build 3rd-party libraries; each has custom build.
    4. It’s hard to predict if a third-party library will run on all platforms: Windows, macOS, Linux, Android, and iOS. It’s simply too difficult for most library developers to test.
7. Third-party libraries warnings are not easy to suppress on all platforms.
8. Unchecked memory access is very easy to do.
    1. Out-of-range access.
    2. Memory leaks.
    3. Double delete.
    4. Use after delete/move.
9. Macros are confusing. It’s easy to hurt yourself.
10. Poor linting. C++ linters often get lost because of transitive inclusion of header files.
11. There are a 1000 style guides (Google, Chromium, LLVM, Microsoft, all with their variations). In contrast, Rust has just the standard one.
12. C++ lacks good defaults.
    1. There is a ton of argued “good practices” some of which are still debated, for example,
        1. Should I set a pointer to `nullptr` after `delete`?
        2. Should I pass by const reference, by value, or by rvalue reference?
    2. An exception to this are lambdas.
        1. They are immutable by default.
        2. They can infer the return type as well as the argument type.
        3. Lifetime of objects in lambda captures are very well defined and clear.
13. C++ has still quite small standard library.
    1. There are no networking utilities.
    2. There aren’t any utilities for JSON parsing.
    3. The number of threading utilities is small. std::execution has been proposed to the standard so there’s hope threading support will be improved.
    4. Fortunately, there are libraries that provide the missing pieces like the [Boost library](https://www.boost.org/) or the [JUCE C++ framework](https://github.com/juce-framework/JUCE).
14. Strings and UTF-8 string handling surprisingly difficult. The library support for UTF-8 emerges just now.
15. There isn’t a standard way of structuring multithreaded-code.
16. C++ coroutines are complex to understand and use. 
17. C++ community can be tough at times: if you ask a question related to raw pointers, people will scream at you that you should be using smart pointers. The thing is that when you interact with C-based APIs and 3rd-party libraries, you must use raw pointers. But maybe that was just my bad impression.

## It’s not all bad

1. In C++, you are in control 100%.
2. C++ standard is evolving at a rapid pace and it’s awesome. It’s a pity that compilers often lag behind (I’m talking about you Apple Clang).
3. You don’t need to know all of C++. Check out my [free Audio Plugin Developer Checklist]({% link collections.all, 'single-pages/checklist.html' %}) to learn what you need to know for audio programming in C++.
4. As mentioned, 3rd party libraries and frameworks like Boost, [Qt](https://www.qt.io/), or JUCE can make your C++ life easier and more enjoyable.
6. [SerenityOS](https://github.com/SerenityOS/serenity) is an example of a very clean, very readable codebase, even though the project deals with the most complex software type: an operating system.
7. Will Rust take over? It still doesn’t have such powerful libraries and frameworks as C++ does.

## Summary

These were the biggest pains of C++ development.

It’s not a rant; these were things I found difficult. Do you struggle with them as well? Or maybe you solved or understood them already: if so, then please, share the resources in the comments so that others (myself included) can understand them.

What are your solutions to these problems? Which problems do you personally see as the most painful? **Let me know in the comments!**

And if you want to become an audio programmer, check out my [free Audio Plugin Developer Checklist]({% link collections.all, 'single-pages/checklist.html' %})!

