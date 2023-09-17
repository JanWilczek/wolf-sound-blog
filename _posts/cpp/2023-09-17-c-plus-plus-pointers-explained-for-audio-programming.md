---
title: "C++ Pointers Explained For Audio Programming"
description: "One-stop shop for audio programmers to understand C and C++ pointers containing real-world audio code examples."
date: 2023-09-17
author: Jan Wilczek
layout: post
images: /assets/img/posts/cpp/2023-09-17-c-plus-plus-pointers-explained-for-audio-programming/
background: /assets/img/posts/cpp/2023-09-17-c-plus-plus-pointers-explained-for-audio-programming/Thumbnail.webp
categories:
  - C/C++
tags:
  - c
  - cpp
  - android
  - juce
  - plugin
discussion_id: 2023-09-17-c-plus-plus-pointers-explained-for-audio-programming
custom_js:
 - /assets/vendor/lazyload/lazyload.min.js
 - /assets/js/wolfsound/modules/load_lazyload.js
---
Understand what are pointers, where to use them, and how to avoid common pitfalls.

In audio programming, we often deal with **audio callbacks**: functions, which in their simplest form have the following signature:

```cpp
void audioCallback(float* samplesToProcess, int samplesCount);
```

The arguments are respectively:

- `samplesToProcess`: a pointer to an array of samples of the `float` type (smallest floating-point type in C++); these samples are meant to be processed by your audio algorithm,
- `samplesCount`: the number of samples in the `samplesToProcess` array.

Right of the bat, a lot of my students are confused: “What? A pointer to an array? What is it? How does it differ from a pointer to a variable? And when to use pointers at all?”

That’s why in this article, we’ll clarify the topic of C++ pointers in audio programming once and for all.

### Table of Contents

1. [What is a pointer?](#what-is-a-pointer)
2. [Static arrays (=size known at compile time)](#static-arrays-size-known-at-compile-time)
3. [Dynamic arrays (=size known at run time)](#dynamic-arrays-size-known-at-run-time)
4. [Dynamic objects (=allocated on the heap)](#dynamic-objects-allocated-on-the-heap)
5. [Stack vs Heap](#stack-vs-heap)
   1. [When to use dynamically allocated objects?](#when-to-use-dynamically-allocated-objects)
   2. [In audio programming](#in-audio-programming)
6. [How to point nowhere: `nullptr`](#how-to-point-nowhere-nullptr)
7. [What is `void*`?](#what-is-void)
8. [Double pointer? `float**`](#double-pointer-float)
   1. [When memory allocation fails: `std::bad_alloc`](#when-memory-allocation-fails-stdbad_alloc)
   2. [Audio Callbacks and `float**`](#audio-callbacks-and-float)
9. [Pointers and `const`](#pointers-and-const)
   1. [Why cannot we cast from `float**` to `const float**`?](#why-cannot-we-cast-from-float-to-const-float)
10. [Why passing a raw pointer to an array and its size to a function is problematic?](#why-passing-a-raw-pointer-to-an-array-and-its-size-to-a-function-is-problematic)
11. [Summary](#summary)

{% render 'google-ad.liquid' %}

## What is a pointer?

In essence, a pointer is a variable of a pointer type. The value of a valid, non-null pointer is an address in memory:

```cpp
float x = 1.f;
float* addressOfX = &x;

std::cout << x << std::endl; // prints 1
std::cout << addressOfX << std::endl; // prints, for example, 0x7ffdad564474
```

In the above listing, I am **taking the address of `x`** using the address-of operator `&`. The type of variable `addressOfX` is `float*`, which can be read as a “pointer to `float`".

## Static arrays (=size known at compile time)

Since a pointer can point to any variable, it can also point to the first element of an array:

```cpp
float array[4] = { 1.f, 2.f, 3.f, 4.f }; // never use these in C++!
float* addressOfFirstElement = &array[0];

// prints 1 (the first element), good boy
std::cout << array[0] << std::endl;

// prints the address as expected, e.g., 0x7ffd19746b20
std::cout << addressOfFirstElement << std::endl;

// surprise? prints the same address!
std::cout << array << std::endl;
```

In the above listing, I declared a 4-element **C-style array**. To everyone’s surprise, directly “printing out” the `array` variable, printed the address of the first element. That’s because C-style arrays are implicitly convertible to pointers. Thus, I can do the following:

```cpp
float array[4] = { 1.f, 2.f, 3.f, 4.f };

// implicit conversion to a pointer; does not even emit a compiler warning
float* addressOfFirstElement = array;
```

Unfortunately, I can also do the following:

```cpp
// 4-element array
float array[4] = { 1.f, 2.f, 3.f, 4.f };

// access "the 5th element"
std::cout << array[4] << std::endl; // ouch!
```

This compiles, runs, and… does not crash! At least sometimes… Surprised?

People used to programming languages like Python, Java, or C# would expect here something like the `IndexOutOfRangeException` being thrown. That’s not the case in C++.

In C++, the compiler assumes (in this case) that you know what you’re doing. And throwing exceptions is expensive so it cannot be the default behavior.

What’s even worse, I can do something like this:

```cpp
// 4-element array
float array[4] = { 1.f, 2.f, 3.f, 4.f };

// write to memory that doesn't belong to you
array[4] = 1.f;
```

And this still may not crash! Reading from or writing to memory that does not belong to you is **undefined behavior**: the program is not guaranteed to be correct anymore after executing such code.

Moreover, since `array` in this example is a “raw pointer” as we say, it doesn’t have `size()` or `length()` member functions. So you need to remember what’s the size of the array. If you decide to change the size of this array, you need to find all the places, where its used and change it there… or use a separate constant… what a nightmare.

To have the array “remember” what’s its size, use `std::array` which is a thin wrapper around C-style arrays whose size is known at compile time. And no, using `std::array` does not make your program slower or less performant.

```cpp
#include <array>
//...
std::array<float, 4> array = { 1.f, 2.f, 3.f, 4.f };

std::cout << array.size() << std::endl; // prints 4

// still no compiler warning, still no crash, just undefined behavior
array[5] = 1.f;
```

Unfortunately, as you can see above, I can still freely access memory that does not belong to me and cause undefined behavior.

BUT `std::array` has another huge advantage: we can use the `at()` member function which checks at runtime if we’re not accessing an out-of-bounds index and throws an exception if we do:

```cpp
std::array<float, 4> array = { 1.f, 2.f, 3.f, 4.f };

// throws std::out_of_range at run time
array.at(5) = 1.f;
```

If you need to access the underlying C-style array, use the `data()` member function: it will return the address of the first element as usual.

```cpp
#include <cassert>
//...
std::array<float, 4> array = { 1.f, 2.f, 3.f, 4.f };
assert(array.data() == &array[0]);
```

The key point is:

> Never use C-style arrays for static arrays: use `std::array` instead **always**.
> 

## Dynamic arrays (=size known at run time)

What if we don’t know at compile time what the size of the array will be?

For example, in the audio callback, we may be given different values of the “buffer size”, like 96 samples, 128 samples, 256 samples, or other.

If we don’t know what the size of the array is going to be at compile time, we need to **allocate** the array at run time like this:

```cpp
// allocate a 4-element array
float* dynamicArray = new float[4];

// use as before...

// deallocate: REMEMBER TO DO THIS!
delete[] dynamicArray;
```

The caveat here is that we need to **deallocate** the array as well. Otherwise, the operating system will still think of that piece of memory as occupied by your program until your program terminates. In a short program, it may not be a big deal but most programs run for a long time (longer than you could expect) and if they have such **memory leaks** (allocated memory to which there is no pointer anymore or which is never used) they will fill up the RAM pretty quickly.

Now comes the best part: you are almost guaranteed to “forget” about deallocating memory. One reason for this is that we are humans. If we need to remember to do things only in pairs (allocate-deallocate) we are bound to forget about the second part of the task mid-way. Or maybe that’s just me 😉

But the true reason of “forgetting” to deallocate is simply the flow of control:

```cpp
void foo() {
    float* dynamicArray = new float[4];

    if (alreadyDone()) {
        return; // memory leak!
    }

    if (error()) {
        throw std::exception{}; // memory leak!
    }

    delete[] dynamicArray;
}
```

In the above case, if we return from the function earlier than with the closing brace, the memory won’t be deallocated. If we throw an exception, the memory won’t be deallocated.

How to overcome this? The best solution here is to use `std::vector`:

```cpp
void foo() {
    auto vector = std::vector<float>(4);

    if (alreadyDone()) {
         // 100% safe, memory allocated by the vector will be
         // deallocated in the vector's destructor
        return;
    }

    if (error()) {
         // 100% safe, memory allocated by the vector will be
         // deallocated in the vector's destructor
        throw std::exception{};
    }
}
```

Problem solved! So

> Never use manually allocated C-style arrays for dynamic arrays: use `std::vector` instead in 99% of the cases.
> 

Yes, there are cases where a vector may not be the best solution ([cases where C++ 17 is not available and data alignment is important](https://thewolfsound.com/data-alignment-in-fir-filter-simd-implementation/), [read additional explanation here](https://stackoverflow.com/a/8456491/13488227)). But they come up so rarely that you should not worry about them too much.

`std::vector` has `data()`, `size()`, `at()`, and a few other cool member functions which you can [check out in the documentation.](https://en.cppreference.com/w/cpp/container/vector)

## Dynamic objects (=allocated on the heap)

Not only arrays with size known only at run time are eligible for dynamic allocation.

With `new` you can also allocate single objects.

```cpp
// allocate
float* pointerToSingleFloat = new float;

// use
*pointerToSingleFloat = 1.f;
std::cout << pointerToSingleFloat << std::endl;
std::cout << *pointerToSingleFloat << std::endl;

// deallocate
delete pointerToSingleFloat;
```

Sample output:

```cpp
0x13b52b0
1
```

Here you can see that putting `*` before the address, allows us to access the underlying value.

```cpp
float a = 1.f;
float addressOfA = &a;
assert(*addressOfA == 1.f);
```

The operation of addressing the value pointed to by a pointer with `*` is called **dereferencing**.

Are you confused that `float*` can point to a single `float` or an array of `float`s? Yeah, welcome to the club.

## Stack vs Heap

What’s the difference between the stack and the heap? Put simply:

> *The **stack** is a place in a process’s memory where all variables of the process whose size is known at compile time are placed.*
> 

> *The **heap** is a place in a process’s memory where the process can dynamically allocate objects.*
> 

Local variables are always on the stack. Objects allocated with `new`, `std::malloc()`, `std::make_unique()`, `std::make_shared()`, etc., are physically on the heap.

So when we refer to objects on the heap, we mean objects that were dynamically allocated and must be eventually freed.

All objects on a process’s heap are automatically freed when the process terminates. I have once thought that it alleviates the problem of memory leaks: after all, the memory will be freed up in the end anyway, right? Unfortunately, even in a short-running program a memory leak can dramatically increase RAM consumption, which can slow down the machine, and annoy the user. Also it increases chances of failing to allocate new memory.

TODO: Link to the bad_alloc section

TODO: Cite operating systems by Silberschatz

### When to use dynamically allocated objects?

If you

- have a large object, or
- you want to use polymorphism, or
- you want to indicate that a variable may be missing, or
- you want the object to outlive its scope (not be automatically deleted when it goes out of scope), or
- you want to pass an object somewhere (e.g., to a function) without copying it and for some reason you cannot use a reference, or
- you want to use the [PIMPL idiom](https://en.cppreference.com/w/cpp/language/pimpl) (an advanced technique to reduce compilation time and hide implementation details), or
- you need to interface with C code or some library

you may **consider** using a pointer.

For example, large objects cannot be allocated on the stack but must be allocated on the heap (i.e., dynamically).

```cpp
class LargeClass {
//... lots of large members
};

//...

// allocate a LargeClass instance dynamically
LargeClass* largeObject = new LargeClass{};

// use it...

// deallocate memory
delete largeObject;
```

*The **stack** is the place where all variables whose size is known at compile time are placed, the **heap** is the place where a program can dynamically allocate objects.*

But again, we are prone to “forgetting” to delete objects, that’s why we should prefer using `[std::unique_ptr<>](https://en.cppreference.com/w/cpp/memory/unique_ptr)` and [`std::shared_ptr<>`](https://en.cppreference.com/w/cpp/memory/shared_ptr) instead just like we should prefer using `std::vector` instead of dynamically allocated C-style arrays. They are called “smart pointers” and ensure that we don’t leak any memory.

To directly create a `unique_ptr` or a `shared_ptr` without using `new`, use `[std::make_unique](https://en.cppreference.com/w/cpp/memory/unique_ptr/make_unique)` and `[std::make_shared](https://en.cppreference.com/w/cpp/memory/shared_ptr/make_shared)` functions.

### In audio programming

We use raw pointers to use polymorphism and interact with audio APIs like the VST3 API or the JUCE C++ framework.

An example of this is JUCE’s `createPluginFilter()` function which allocates a new audio plugin processor and returns it:

```cpp
juce::AudioProcessor* JUCE_CALLTYPE createPluginFilter() {
    return new AudioPluginAudioProcessor(); // polymorphic instance
}
```

We also use raw pointers to pass arrays of samples:

```cpp
float gain = 0.5f;
//...
void applyGainTo(float* samples, int samplesToProcess) {
  for (auto i = 0; i < samplesToProcess; ++i) {
    samples[i] *= gain; // use as an array
  }
}
```

## How to point nowhere: `nullptr`

Since pointers point to memory addresses, how to represent a pointer value that points nowhere?

We cannot point to an arbitrary memory address because how would we know then that this memory cannot be accessed?

The C language used the `NULL` macro, which was essentially an alias for an `int` of value 0.

The C++ language improved upon this design by introducing `nullptr`: a special value of `nullptr_t` type that is NOT an `int`.

If something is `nullptr`, it means that it doesn’t point to any memory and should not be dereferenced.

```cpp
float* notPointingToAnything = nullptr;

// this should crash
std::cout << *notPointingToAnything << std::endl;
```

You can check if a pointer points somewhere by comparing it against the `nullptr`.

```cpp
float* ptr;
//...
if (ptr != nullptr) {
  // ptr (hopefully) points somewhere meaningful
}
```

We can simplify this comparison by using a pointer as the condition directly.

```cpp
float* ptr;
//...
if (ptr) {
  // ptr (hopefully) points somewhere meaningful
}
```

Unfortunately, a check against `nullptr` doesn’t protect us against accessing memory that does not belong to us. That’s why you can often find code like this.

```cpp
float* ptr = new float[5];
//...
delete[] ptr;
ptr = nullptr; // mark that ptr does not point to valid memory
```

Whereas this is good practice or not is still debated. My opinion is to avoid naked `new` and `delete` altogether by using smart pointers (`std::unique_ptr<T>` and `std::shared_ptr<T>`). And if you do need raw pointers (for example, when interacting with a C API), wrap the pointer in a class that will deallocate the memory in its destructor because destructors are guaranteed to be called in all situations.

## What is `void*`?

When you deal with audio, you stumble across the type `void*`. Now, `void` before the function declaration indicates that the function does not return any value.

```cpp
void returnImmediately() {
  return;
}
```

So when people see `void*`, they are like “what the heck?”

`void*` simply points to a “raw” memory block. Such a memory block can be anything so you as the programmer must know what it points to.

`void*` cannot be used per se, it must always be cast to an appropriate type.

For example, if for some reason you need to allocate memory using `std::malloc` or a similar C-style function, you need to cast the obtained result to the desired type (in the below example, `float*`).

```cpp
#include <cstdlib>

//...
void* rawMemoryPtr = std::malloc(4 * sizeof(float));
float* arrayOfFloats = reinterpret_cast<float*>(rawMemoryPtr);
    
// use as a dynamic array
arrayOfFloats[0] = 0.1f;
//...

// free the memory
std::free(rawMemoryPtr);
rawMemoryPtr = nullptr;
arrayOfFloats = nullptr;
```

As you can see, we need to pass the correct size to `std::malloc`, cast the result to our desired type, and then remember to free the memory when we’re done with the array.

In the above example, `std::free(arrayOfFloats)` would also work but remember to free memory only once; the fact that we have two pointers to the same piece of memory is no exception.

Another example (which is very important) is passing data to some operating system callback. For example, in [OpenSL ES](https://www.khronos.org/api/opensles) which was the original audio API on Android, you would need to call the `RegisterCallback` function with `void*` argument `pContext` to register your callback for retrieving playback events.

```cpp
typedef void (SLAPIENTRY *slPlayCallback) (
  SLPlayItf caller,
  void *pContext,
  SLuint32 event
);

SLresult (*RegisterCallback) (
    SLPlayItf self,
    slPlayCallback callback,
    void *pContext
  );
```

You can pass some additional data like a pointer to a class instance in the callback to redirect the callback to a more appropriate place than a free function or a global instance. Here’s an example based on the [OpenSL ES specification](https://registry.khronos.org/OpenSL-ES/specs/OpenSL_ES_Specification_1.0.1.pdf) with as many details as possible omitted.

```cpp
struct PlaybackEventHandler {
void handle(SLuint32 playEvent) {
  //...
}
};

// the callback function
void playEventCallback(SLPlayItf caller, void* pContext, SLuint32 playEvent) {
 // retrieve the handler from the context
 PlaybackEventHandler* handler
                        = reinterpret_cast<PlaybackEventHandler*>(pContext);
 // redirect the callback to the actual handler
 handler->handle(playEvent);
}

//...
// create the actual handler
auto handler = std::make_unique<PlaybackEventHandler>();

// register the callback which can only be a free function
// (but I'm not 100% sure on this)
// pass the handler as "raw" memory
res = (*playItf)->RegisterCallback(playItf, playEventCallback,
                                   reinterpret_cast<void*>(handler.get()));
```

So `void*` does come up in audio processing because audio code often deals with low-level C-style application programming interfaces (APIs).

Note that to call a member function of a class using a pointer to its instance, we can use the arrow operator `->` instead of dereferencing the pointer with `*` and using the dot operator `.`.

```cpp
#include <memory>

struct PlaybackEventHandler {
void handle(SLuint32 playEvent) {
  //...
}
};
std::unique_ptr<PlaybackEventHandler> handler
                = std::make_unique<PlaybackEventHandler>();
PlaybackEventHandler* handlerRawPtr = handler.get();

// these are equivalent but -> is more handy
handler->handle(0);
(*handler).handle(0);
handlerRawPtr->handle(0);
(*handlerRawPtr).handle(0);
```

## Double pointer? `float**`

Let’s get meta…

You know that `float*` points to a single float or an array of `float`s (and you need to remember which along with the size of the array...).

What is `float**` then?

Well, again, it may mean a few different things.

1. `float**` can be a “pointer to a pointer to a `float`”. We can get it when we take the address of a pointer to `float`.

```cpp
float x = 1.f;
float* addressOfX = &x;
float** pointerToAddressOfX = &addressOfX;
```

A use case for it in C-style APIs is to change the value of a pointer variable passed to a function (in C, there are no references).

```cpp
#include <cassert>

void allocate(float** p) {
    // p's value can be manipulated
    *p = new float;
}

float* p = nullptr;
allocate(&p); // pass the address of p
assert(p); // ensure that p is not null; allocate succeeded
delete p; // remember to deallocate
```

This is recursive, so we get `float***` as well but I have never seen it in actual code and I cannot think of any applications other than annoying other developers 😉

1. `float**` can be an array of arrays: a pointer to an array of pointers to `float`s. Although each of the pointers in the array can point to an array of an arbitrary size, even of size one, typically all pointed to arrays will be of the same size. Otherwise, we enter the programming hell. If you don’t believe me, see how cumbersome is the code below.

```cpp
// allocate the arrays
float** arrayOfArrays = new float*[2];
arrayOfArrays[0] = new float[2];
arrayOfArrays[1] = new float[3];

// fill the arrays (all possible values are filled)
arrayOfArrays[0][0] = 1.f;
arrayOfArrays[0][1] = 2.f;
arrayOfArrays[1][0] = 3.f;
arrayOfArrays[1][1] = 4.f;
arrayOfArrays[1][2] = 4.f;

// deallocate the arrays: order is important
delete[] arrayOfArrays[0];
delete[] arrayOfArrays[1];
delete[] arrayOfArrays;
```

### When memory allocation fails: `std::bad_alloc`

The above code has a problem; if the second or the third allocation fails (for example, because our computer has run out of memory), `std::bad_alloc` exception will be thrown so the lines with `delete[]` won’t be executed and we will have a memory leak.

Remember that memory allocations can fail. I have never seen this handled in practice but I did see that happen in practice. So again, avoid naked `new` because it can throw and cause a memory leak; use smart pointers instead.

### Audio Callbacks and `float**`

`float**` pops up very often in audio, especially in the audio callbacks.

Let’s take the JUCE C++ framework as an example. If you want to build a standalone desktop application with audio, you need to register your audio callback: the function that delivers you recorded audio data (if any) and allows you to supply the samples to be played out by the system’s audio device. JUCE greatly abstracts out the necessity to interact with various audio drivers directly.

JUCE requires the audio callback to be a class that inherits from `juce::AudioIODeviceCallback` and, thus, needs to override 3 methods.

```cpp
#include <juce_audio_devices/juce_audio_devices.h>

class AudioCallback : public juce::AudioIODeviceCallback {
public:
  void audioDeviceIOCallbackWithContext(
      const float* const* inputChannelData,
      int numInputChannels,
      float* const* outputChannelData,
      int numOutputChannels,
      int numSamples,
      const juce::AudioIODeviceCallbackContext& context) override;
  void audioDeviceAboutToStart(juce::AudioIODevice* device) override;
  void audioDeviceStopped() override;
};
```

You can then register your audio callback like this.

```cpp
juce::AudioDeviceManager audioDeviceManager;
audioDeviceManager.initialise(/* number of input channels: */ 1,
                              /* number of output channels: */ 2,
                              /* other: */ nullptr, true, {}, nullptr);
AudioCallback callback;
audioDeviceManager.addAudioCallback(&callback);
```

If you want to learn more about `juce::AudioDeviceManager` class, you can [check out its documentation.](https://docs.juce.com/master/classAudioDeviceManager.html)

The important bit here is the `audioDeviceIOCallbackWithContext()` function. It has 6 arguments:

1. `const float* const* inputChannelData`: an array of arrays of input samples, one array of immutable `float`s per channel. The sample values and the pointers inside of the array cannot be changed (because of the first and second `const` keywords respectively).
2. `int numInputChannels`: the number of input channels so the number of arrays in the `inputChannelData` array.
3. `float* const* outputChannelData`: an array of arrays to be filled with output samples. Here, the pointers to individual arrays cannot be changed but the samples themselves can be changed.
4. `int numOutputChannels`: the number of arrays in the `outputChannelData` array.
5. `int numSamples`: the number of samples in each input and output channel, the second dimension of both supplied arrays of arrays.
6. `const juce::AudioIODeviceCallbackContext& context`: additional data supplied by the host, not interesting at the moment.

How to handle these arrays of arrays? As before, with double indexing.

```cpp
void audioDeviceIOCallbackWithContext(
      const float* const* inputChannelData,
      int numInputChannels,
      float* const* outputChannelData,
      int numOutputChannels,
      int numSamples,
      const juce::AudioIODeviceCallbackContext& context) {
  for (auto channel = 0; channel < numInputChannels; ++channel) {
    for (auto i = 0; i < numSamples; ++i) {
      // inputChannelData[channel][i] holds the i-th sample
      // in the channel-th channel
    }
  }

  for (auto channel = 0; channel < numOutputChannels; ++channel) {
    for (auto i = 0; i < numSamples; ++i) {
      // set the i-th sample of the channel-th channel to 0 (silence)
      outputChannelData[channel][i] = 0.f;
    }
  }
  
}
```

But even JUCE’s examples show that we want to escape from raw pointers and fragmented size information as quickly as possible.

```cpp
// from juce/examples/Audio/AudioRecordingDemo.h, slightly changed by me
// Create an AudioBuffer to wrap our incoming data, note that this does
// no allocations or copies, it simply references our input data
juce::AudioBuffer<float> buffer(const_cast<float**>(inputChannelData),
                                numInputChannels, numSamples);
```

The `juce::AudioBuffer` class used in this code is a nice wrapper for multidimensional arrays containing samples.

Since the audio callback used the `const` keyword, I will discuss it next.

## Pointers and `const`

When it comes to pointers and the `const` keyword, the understanding can really get messy.

Typically, `const` means a variable that cannot be reassigned or mutated.

```cpp
const float immutable = 1.f;
// immutable = 0.f; // does not compile

class Foo {
public:
    void setBar(float bar) { m_bar = bar; }
private:
    float m_bar = 0.f;
};

const Foo immutableFoo{};
// immutableFoo.setBar(2.f); // would change internal state; does not compile
```

However, with pointers it gets a little bit more tricky.

People see the following types and are immediately confused:

- `const float*`
- `float const*`
- `const float* const`
- `const float* const*`

and I don’t blame them because I have been often confused myself.

The easiest way to approach this is to **read from right to left.**

In the following table is your guide. Remember that `float*` can be a pointer to a single `float` or a pointer to an array of `float`s... And you need to remember its meaning 😉

| Type | Meaning |
| --- | --- |
| `float*` | pointer to `float` (single or an array) |
| `const float*` | pointer to `const` `float` (the `float` cannot be modified) |
| `float const*` | same as `const float*` |
| `float* const` | `const` pointer to `float` (the pointer cannot be modified) |
| `float**` | pointer to a pointer to `float` or an array of arrays of `float`s |
| `const float**` | pointer to a pointer to `const` `float` or an array of arrays of `const` `float`s |
| `float const**` | same as `const float**` |
| `float* const*` | a pointer to a `const` pointer to `float` or (more probably) an array of `const` pointers to `float`s; the pointers in the array cannot be modified, the `float`s in the arrays can be modified; ideal for the “output samples” argument |
| `float** const` | a const pointer to a non-`const` pointer to `float` or a `const` pointer to an array of arrays, where all pointers and all `float`s can be modified |
| `const float const**` | duplicate `const`, malformed |
| `const float* const*` | a pointer to a const pointer to a `const` `float` or an array of `const` pointers to arrays of `const` `float`s; ideal for input samples that must not be mutated and where pointers to individual channels must not be mutated either |
| `float const* const*` | same as `const float* const*` |
| `float* const const*` | duplicate `const`, malformed |
| `float* const* const` | const pointer to an array of `const` pointers to non-`const` `float`(s) |
| `const float* const* const` | `const` pointer to an array of `const` pointers to `const` `float`(s) |
| `float const* const* const` | same as `const float* const* const` |

Here are examples of how each of these work that you can [check out on Compiler Explorer.](https://godbolt.org/z/j89hEc1rK)

```cpp
void arrayTest(float* arr) {
    float* arr1 = arr;
    arr1[0] = 1.f;
    arr1 = nullptr;

    const float* arr2 = arr;
    // arr2[0] = 1.f; // does not compile: float is immutable
    arr2 = nullptr;

    float const* arr3 = arr;
    // arr3[0] = 1.f; // does not compile: float is immutable
    arr3 = nullptr;

    float* const arr4 = arr;
    arr4[0] = 1.f;
    // arr4 = nullptr; // does not compile: pointer is immutable
}

void multidimensionalArrayTest(float** arr, const float** constArr)  {
    float** arr1 = arr;
    arr1[0][0] = 1.f;
    arr1[0] = nullptr;
    arr1 = nullptr;

    const float** arr2 = constArr;
    // arr2[0][0] = 1.f; // does not compile: float is immutable
    arr2[0] = nullptr;
    arr2 = nullptr;

    float const** arr3 = constArr;
    // arr3[0][0] = 1.f; // does not compile: float is immutable
    arr3[0] = nullptr;
    arr3 = nullptr;

    float* const* arr4 = arr;
    arr4[0][0] = 1.f;
    // arr4[0] = nullptr; // does not compile: pointer to float is immutable
    arr4 = nullptr;

    float** const arr5 = arr;
    arr5[0][0] = 1.f;
    arr5[0] = nullptr;
    // arr5 = nullptr; // does not compile: pointer is immutable

    // const float const** arr6 = arr; // does not comiple: malformed

    const float* const* arr7 = arr;
    // arr7[0][0] = 1.f; // does not compile: float is immutable
    // arr7[0] = nullptr; // does not compile: pointer to float is immutable
    arr7 = nullptr;

    float const* const* arr8 = arr;
    // arr8[0][0] = 1.f; // does not compile: float is immutable
    // arr8[0] = nullptr; // does not compile: pointer to float is immutable
    arr8 = nullptr;

    // float* const const* arr9 = arr; // does not compile: malformed

    float* const* const arr10 = arr;
    arr10[0][0] = 1.f;
    // arr10[0] = nullptr; // does not compile: pointer to float is immutable
    // arr10 = nullptr; // does not compile: pointer is immutable

    const float* const* const arr11 = arr;
    // arr11[0][0] = 1.f; // does not compile: float is immutable
    // arr11[0] = nullptr; // does not compile: pointer to float is immutable
    // arr11 = nullptr; // does not compile: pointer is immutable
    
    float const* const* const arr12 = arr;
    // arr12[0][0] = 1.f; // does not compile: float is immutable
    // arr12[0] = nullptr; // does not compile: pointer to float is immutable
    // arr12 = nullptr; // does not compile: pointer is immutable
}
```

### Why cannot we cast from `float**` to `const float**`?

While constructing the above examples, I’ve run into a problem when trying to compile the following code.

```cpp
void multidimensionalArrayTest(float** arr)  {
  // error: invalid conversion from 'float**' to 'const float**'  
  const float** arr2 = arr;
}
```

Why cannot we convert `float**` to `const float**`?

I quickly found an answer on [StackOverflow](https://stackoverflow.com/questions/2463473/why-am-i-getting-an-error-converting-a-float-to-const-float) which pointed to [ISO C++’s FAQ](https://isocpp.org/wiki/faq/const-correctness#constptrptr-conversion).

The short answer is: because if we could, we could secretly modify `const` data without even realizing it.

Adapting the examples listed there to our needs, the following code would be really problematic.

```cpp
const float x = 1.f;
float* p;
const float** q = &p;// q now points to p; this is (fortunately!) an error
*q = &x;             // p now points to x
*p = 0.f;            // Ouch: we changed the value of a const variable x!
```

So if we could assign an address of a pointer to non-`const` `float` (`&p`) to a pointer to a pointer to `const float` (`q`), we could then reassign the value of the initial pointer `p` through the pointer to pointer to `const float` `q` to point to some `const` data and then use the initial pointer `p` (which is not bound by `const`) to modify the value.

Yes, that’s quite complicated. No, I would not be able to detect such a bug in a codebase comprising of hundreds of thousands of lines of code.

In the audio callback and in the above examples, you could see another problem…

## Why passing a raw pointer to an array and its size to a function is problematic?

In other words, why a function like this

```cpp
void process1(float* samples, int samplesCount) {
  for (auto i = 0; i < samplesCount; ++i) {
    samples[i] = 0.f; // modify the sample
  }
}
```

can cause problems in our code?

I can think of 3 reasons:

1. Having a separate argument for the array and its size decouples information. And where information that must be held together is decoupled, errors are likely to occur.
2. The pointer to the array can be `nullptr`; we need to check and explicitly handle it or hope that it’s always non-null. Of course, the pointer to the array inevitably will be `nullptr` at some point according to the [Murphy’s law](https://en.wikipedia.org/wiki/Murphy%27s_law). Well, the pointer can even point to not-owned memory, which means that accessing it will cause undefined behavior.
3. `samplesCount` may be inaccurate. If that’s the case, we have an out-of-memory access so undefined behavior.

Such functions were very common before the C++ 20 standard because they allowed to handle `vector`’s and `array`’s data in the same way.

```cpp
std::array<float, 4> samplesArray { 1.f, 1.f, 1.f, 1.f};
std::vector<float> samplesVector = std::vector<float>(4, 1.f);

// decoupled information, error-prone
process1(samplesArray.data(), samplesArray.size());
process1(samplesVector.data(), samplesVector.size());
process1(nullptr, 0); // also possible! yuk!
```

We can avoid ALL of the above problems, yet keep the flexibility and not incur any memory overhead by introducing a very simple yet profound change to our API that is available since C++ 20: `std::span`.

Here’s the new function.

```cpp
#include <span>

void process2(std::span<float> samples) {
  for (auto i = 0; i < std::ssize(samples); ++i) {
    samples[i] = 0.f; // modify the sample
  }
}
```

It can be called as the first version but with one (great!) exception.

```cpp
std::array<float, 4> samplesArray { 1.f, 1.f, 1.f, 1.f};
std::vector<float> samplesVector = std::vector<float>(4, 1.f);
process2(samplesArray);
process2(samplesVector);

// explicit, not necessary, and error-prone
process2(std::span{samplesArray.data(), samplesArray.size()});
process2(std::span{samplesVector.data(), samplesVector.size()});

// process2(std::span{nullptr, 0}); // haha, does not compile!
```

In this way, we are sure that we can safely access the samples in the `process2()`  function without undefined behavior (well, unless we really want to…). We also get the for-each loop syntax for free!

```cpp
#include <span>

void process2(std::span<float> samples) {
  for (auto& sample : samples) {
    sample = 0.f;
  }
}
```

With the above code, you are guaranteed not to access not-owned memory. The above code cannot produce undefined behavior.

In case you ask: no, using `float*` directly is **not** more performant or optimal than using `std::span`. Just use `std::span` and everything will be fine.

If you cannot use C++ 20, you can always use a 3rd-party library that adds the `std::span` functionality, like [this one.](https://github.com/tcbrindle/span)

## Summary

This was a long article so I have summarized the key takeaways here 😉

1. In C++, a pointer to type `T` has type `T*`.
2. `T*` can point to an instance of `T` or to an array of `T`s; we need to know what is the case.
3. `T**` can point to a pointer to a pointer to `T` but can also signify an array of arrays of `T`s.
4. If a pointer is equal to `nullptr` it does not point to any memory and should not be dereferenced.
5. Memory allocated on the heap must be deallocated before we lose the last pointer to this memory.
6. Prefer stack-allocated variables to heap-allocated variables.
7. Use standard containers instead of manually allocated dynamic memory:
    1. `std::array<T>` for arrays whose size is known at compile time,
    2. `std::vector<T>` for arrays whose size is known only at run time.
8. Do not use `new` or `delete`; use `std::unique_ptr<T>`, `std::shared_ptr<T>` with `std::make_shared` and `std::make_unique` factory functions.
9. If you need to manually allocate memory, wrap it in a class so that the destructor will deallocate the memory.
10. Use `std::span` as an argument to functions that should take an array of objects and you don’t care if they are present on the stack or on the heap.
11. If you need to interact with C-style APIs, convert the relevant data to `std::span` or a dedicated resource-managing class ASAP (see point 9).