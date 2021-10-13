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

{% katexmm %}

There are so many programming languages out there. Why would we want to write a wavetable synth in Rust?

After reading this article you will know
* how to output sound with Rust,
* how to implement a sine oscillator in Rust with wavetable synthesis,
* how a Rust project is structured,
* how to manage dependencies in Rust, and
* how to compile and run Rust project.

## What is Rust?

Rust is a general-purpose programming language designed for high-performance and high-reliability computing. While these two goals may seem contradictory, Rust actually manages to accomplish both of them thanks to the concept of ownership, similar to C++'s `unique_ptr`s.

![]({{ page.images | absolute_url | append: "/Rust_programming_language_black_logo.svg" }}){: alt="Rust programming language logo." width="600px" }

Being optimized and safe makes Rust an attractive alternative to C or C++: we could possibly get the same speed and memory performance but at the same time avoid the pitfalls of the C family, for example, invalid pointers.

Although I really appreciate the features of Rust, I still think that the amount of code written in C ensures that C and C++ programmers will be needed for many years to come 🙂 It also must take some time for Rust to mature... But this language is definitely worth exploring!

I personally find its clear compiler messages most useful. Although I am a newbie to Rust, with the help of the compiler, [*The Rust Programming Language* book](https://doc.rust-lang.org/book/), and googling, I was able to write a wavetable synthesizer. In this article, I will walk you through that process, showing you **the minimum amount of features and knowledge needed to do audio programming in Rust**. 

*Note: If you don't know how wavetable synthesis algorithm works, [check out my article on the theory behind it]({% post_url synthesis/2021-08-13-wavetable-synthesis-theory %}). I also have articles on [wavetable synthesis implementation in Python]({% post_url synthesis/2021-08-27-wavetable-synthesis-python %}) and [wavetable synth plugin in the JUCE C++ framework]({% post_url synthesis/2021-09-24-wavetable-synthesis-juce %}).*

*At [WolfSound]({% link index.html %}), you are fully covered!*

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

For simplicity, we will put all of our code in the *src/main.rs* file. Before we write any code, let's bring it to this state:

```rust
// main.rs

fn main() {

}
```

With these formalities out of the way, let's start with arranging a basic audio output with Rust.

## How to Output Sound in Rust?

To play back audio in Rust, we will use the `rodio` library. In Rust, libraries can be imported from so-called crates. A public repository of all publicly available crates is [crates.io](https://crates.io). There, one can find the crate of interest and import it in their project.

## Importing a Dependency

Including a dependency in your Rust project is simple: just add crate name and its version in the *Cargo.toml* file under "[dependencies]". In our case it will look as follows:

```yaml
# Cargo.toml
# (...)
[dependencies]
rodio = "0.14.0"
```

If you now execute `cargo run`, the dependency will be immediately installed.

<!-- TODO: Add a link to the part of the article where we implement the Source trait -->

## Wave Table Generation

To use the [wavetable synthesis algorithm]({% post_url synthesis/2021-08-13-wavetable-synthesis-theory %}), one needs to generate a wave table first.

Just as a quick reminder: a wave table is an array in memory, which contains 1 period of the waveform we want to play out through our oscillator.

### Variable Declaration

Let's define the size of our wave table:
```rust
# main.rs

fn main() {
    let wave_table_size = 64;
}
```

Rust will deduct the type of the declared variable based on the right hand-side literal. This deduction may also be based on the context that the variable is used in later in code. For example, in this declaration `wave_table_size` is of `i32` type (32-bit signed integer). However, after we use it in the following paragraph, it will have changed its type to `usize` (unsigned size type, platform-dependent).

### Vector: A Flexible Container

To store the values of our wave table, we'll use a vector: `Vec` struct (Rust's name for a class). It is a flexible array type that allows us to store arrays of variable size in memory. All elements stored should be of the same type. It sounds a lot like a C++ `std::vector`, right?

```rust
# main.rs: main()
(...)
    let mut wave_table: Vec<f32> = Vec::with_capacity(wave_table_size);
```

First, we declare a **mutable** variable (i.e., its value can be changed in the program). **Variables in Rust are immutable by default.** We need to have it mutable to fill it with values.

Second, we specify the type of the variable. In our case, it is a vector filled with 32-bit floating-point values, i.e., `Vec<f32>`.

Third, we construct our vector. Constructors in Rust are regular functions. They take arguments and return an instance of the struct. Here, the `with_capacity` constructor, allows us to specify how many elements should be possible to fit into our vector without reallocation.

### Filling the Wave Table

To fill our wave table with the values of 1 sine period, we will use a for-loop:

```rust
for n in 0..wave_table_size {
    wave_table.push((2.0 * std::f32::consts::PI * n as f32 / wave_table_size as f32).sin());
}
```

`0..wave_table_size` returns a range (`std::ops::Range`) from 0 to `wave_table_size - 1`. As in C++, vectors in Rust are indexed from 0.

In the loop, we append values to the end of the vector with the `push()` function. Interesting is the sine calculation. To perform successful multiplication and division, we need to bring all expressions to a common type (here: `f32`). Rust readily provides the $\pi$ constant.

As I explained in the [Python tutorial]({% post_url synthesis/2021-08-27-wavetable-synthesis-python %}), in the loop, we calculate the value of the sin waveform for arguments linearly increasing from $0$ to $2\pi$. To calculate the sin for argument `x`, we write `x.sin()` instead of `sin(x)`.

We have generated our wave table. Now, it is time to initialize an oscillator with it.

## WavetableOscillator Struct

We want to write an oscillator: an object that iterates over a specific wave table with speed dictated by the frequency it should use. That object needs to store the sampling rate, the wave table, current index into the wave table, and frequency-dependent index increment.

Let's define our struct:

```rust
struct WavetableOscillator {
    sample_rate: u32,
    wave_table: Vec<f32>,
    index: f32,
    index_increment: f32,
}
```

### Constructor

Methods of structs are stored in a separate structure called `impl`. That is a way of decoupling the data stored from the implementation.

As I mentioned, structs in Rust don't have constructors. Instead, there is a convention that says, we should write a `new()` function. In our case, it will look as follows:

```rust
impl WavetableOscillator {
    fn new(sample_rate: u32, wave_table: Vec<f32>) -> WavetableOscillator {
        return WavetableOscillator {
            sample_rate: sample_rate,
            wave_table: wave_table,
            index: 0.0,
            index_increment: 0.0,
        };
    }
}
```   

We could also create a `WavetableOscillator` explicitly in code, but it would force us to know that `index` and `index_increment` need to be initialized to 0. Now, the `new()` function will do this for us.

Note that we need to specify the returned type. Here, it is the `WavetableOscillator` struct.

### Setting Oscillator's Frequency

<!-- TODO: Link the synth articles together! -->

{% endkatexmm %}