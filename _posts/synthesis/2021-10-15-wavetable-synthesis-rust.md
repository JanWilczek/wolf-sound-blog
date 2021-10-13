---
title: "Simple Wavetable Synth in Rust Tutorial"
description: Learn to code the wavetable synthesis algorithm in the Rust programming language.
date: 2021-10-15
author: Jan Wilczek
layout: post
permalink: /sound-synthesis/wavetable-synth-in-rust/
images: assets/img/posts/synthesis/2021-10-15-wavetable-synthesis-rust
background: /assets/img/posts/synthesis/2021-08-13-wavetable-synthesis-theory/Thumbnail.png
categories:
 - Sound Synthesis
tags:
 - synthesis
 - wavetable
 - Rust
discussion_id: 2021-10-15-wavetable-synthesis-rust
---
Let's write a wavetable synthesizer in Rust!

There are so many programming languages out there. Why would we want to write a wavetable synth in Rust?

## What is Rust?

Rust is a general-purpose programming language designed for high-performance and high-reliability computing. While these two goals may seem contradictory, Rust actually manages to accomplish both of them thanks to the concept of ownership, similar to C++'s `unique_ptr`s.

![]({{ page.images | absolute_url | append: "/Rust_programming_language_black_logo.svg" }}){: alt="Rust programming language logo." width="600px" }

Being optimized and safe makes Rust an attractive alternative to C or C++: we could possibly get the same speed and memory performance but at the same time avoid the pitfalls of the C family, for example, invalid pointers.

Although I really appreciate the features of Rust, I still think that the amount of code written in C ensures that C and C++ programmers will be needed for many years to come 🙂 It also must take some time for Rust to mature... But this language is definitely worth exploring!

I personally find its clear compiler messages most useful. Although I am a newbie to Rust, with the help of the compiler, [*The Rust Programming Language* book](https://doc.rust-lang.org/book/), and googling, I was able to write a wavetable synthesizer. In this article, I will walk you through that process, showing you **the minimum amount of features and knowledge needed to do audio programming in Rust**. 

*Note: If you don't know how wavetable synthesis algorithm works, [check out my article on the theory behind it]({% post_url synthesis/2021-08-13-wavetable-synthesis-theory %}). I also have articles on [wavetable synthesis implementation in Python]({% post_url synthesis/2021-08-27-wavetable-synthesis-python %}) and [wavetable synth plugin in the JUCE C++ framework]({% post_url synthesis/2021-09-24-wavetable-synthesis-juce %}).*

*At [WolfSound]({% link index.html %}) you are fully covered!*

## Project Setup

Let's assume you have Rust installed on your system.

To create a project in Rust we will use **Cargo: Rust's build system and package manager**. It helps you organize your files and manage dependencies easily.

To create the project directory we will use the `cargo new PROJECTNAME` command:

```bash
$ cd ~/projects
$ cargo new wavetable_synth
    Created binary (application) `wavetable_synth` package
$ cd wavetable_synth
$ ls -R
.:
Cargo.toml  src

./src:
main.rs
```
As you can see, Cargo created the *wavetable_synth* folder. Inside there is the *Cargo.toml* file with our project's metadata and the *src* folder with the source code in Rust. Inside the *src* folder there is the *main.rs* file that is the entry point for each binary application in Rust.

To finish the setup, run the `cargo run` command inside the *wavetable_synth* folder. You should see "Hello, world!" printed in your shell.

```bash
$ cd ~/projects/wavetable_synth
$ cargo run
   Compiling wavetable_synth v0.1.0 (/home/jawi/projects/wavetable_synth)
    Finished dev [unoptimized + debuginfo] target(s) in 0.73s
     Running `target/debug/wavetable_synth`
Hello, world!
```



<!-- TODO: Link the synth articles together! -->