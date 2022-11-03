---
title: "Android Synthesizer App Tutorial Part 3: ViewModel Using Coroutines"
description: "A tutorial for beginners on how to implement a ViewModel in your Android app on the example of a sound synthesizer app."
date: 2022-09-11
author: Jan Wilczek
layout: post
permalink: /android-synthesizer-3-view-model-using-kotlin-coroutines/
images: /assets/img/posts/synthesis/android-wavetable-synthesizer
background: /assets/img/posts/synthesis/android-wavetable-synthesizer/Thumbnail.webp
categories:
  - Sound Synthesis
tags:
  - android
  - wavetable
  - kotlin
discussion_id: 2022-09-11-view-model
custom_js:
 - /assets/vendor/lazyload/lazyload.min.js
 - /assets/js/wolfsound/modules/load_lazyload.js
---
Modern Android architecture in its glory!

<iframe width="560" height="315" src="https://www.youtube.com/embed/Vxk9e82GY6c" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

{% capture _ %}{% increment figureId20220911 %}{% endcapture %}
{% capture _ %}{% increment listingId20220911 %}{% endcapture %}

### Android Wavetable Synthesizer Tutorial Series

1. [App Architecture]({% post_url synthesis/android-wavetable-synthesizer/2022-08-02-app-architecture %})
2. [UI with Jetpack Compose]({% post_url synthesis/android-wavetable-synthesizer/2022-08-10-ui %})
3. [ViewModel (this one)]({% post_url synthesis/android-wavetable-synthesizer/2022-09-11-view-model %})
4. [Calling C++ Code From Kotlin with JNI]({% post_url synthesis/android-wavetable-synthesizer/2022-10-09-jni %})
5. [Playing Back Audio on Android with C++]({% post_url synthesis/android-wavetable-synthesizer/2022-10-23-oboe %})
6. [Wavetable Synthesis Algorithm in C++]({% post_url synthesis/android-wavetable-synthesizer/2022-11-03-cpp-synth %})

## Introduction

Welcome to the 3rd part of the Android wavetable synthesizer app tutorial!

In this tutorial series, we want to design and implement a synthesizer app on Android using all the modern technologies and best practices.

<div markdown="0">
<img class="lazyload" data-src="{{ page.images | absolute_url | append: "/SynthesizerUI.webp" }}" alt="Graphical user interface of the synthesizer app">
</div>

_Figure {% increment figureId20220911 %}. Graphical user interface of the synthesizer app we are going to build._

In the [first part of this tutorial]({% post_url synthesis/android-wavetable-synthesizer/2022-08-02-app-architecture %}), we discussed the architecture of our app.

In the [previous part of this tutorial]({% post_url synthesis/android-wavetable-synthesizer/2022-08-10-ui %}), we discussed how to create its user interface (UI) using Jetpack Compose.

In this part, we will implement the bridge between the UI and the core logic of our app.

The best way, to my knowledge, how to do it is to use the so-called **ViewModel**.

As a reminder, the full source code is available on [my GitHub page](https://github.com/JanWilczek/android-wavetable-synthesizer).

### Table of Contents

1. [What Is a ViewModel?](#what-is-a-viewmodel)
2. [What Is a Model in the Synthesizer App?](#what-is-a-model-in-the-synthesizer-app)
3. [Wavetable Synthesizer Model Implementation](#wavetable-synthesizer-model-implementation)
4. [Wavetable Class](#wavetable-class)
5. [LoggingWavetableSynthesizer](#loggingwavetablesynthesizer)
6. [WavetableSynthesizerViewModel Class](#wavetablesynthesizerviewmodel-class)
   1. [The Synthesizer Reference](#the-synthesizer-reference)
   2. [Setting the Frequency](#setting-the-frequency)
   3. [Slider Position to Frequency Value](#slider-position-to-frequency-value)
   4. [Calculating the Logarithmic Frequency Value from Slider Position](#calculating-the-logarithmic-frequency-value-from-slider-position)
   5. [Updating the View](#updating-the-view)
   6. [Updating the Model](#updating-the-model)
   7. [What Is a Coroutine in Kotlin?](#what-is-a-coroutine-in-kotlin)
   8. [When Do We Use Kotlin Coroutines?](#when-do-we-use-kotlin-coroutines)
   9. [Why Do We Have to Use a Coroutine Here?](#why-do-we-have-to-use-a-coroutine-here)
   10. [What Are Suspended Functions in Kotlin?](#what-are-suspended-functions-in-kotlin)
   11. [Setting the Volume](#setting-the-volume)
   12. [Setting the Wavetable](#setting-the-wavetable)
   13. [Changing the Play State](#changing-the-play-state)
   14. [Applying the Parameters](#applying-the-parameters)
7. [Updating the Composable Hierarchy](#updating-the-composable-hierarchy)
8. [Wiring in the MainActivity Class](#wiring-in-the-mainactivity-class)
9. [Running the Synthesizer in the Emulator.](#running-the-synthesizer-in-the-emulator)
10. [Part 3 Summary](#summary)

## What Is a ViewModel?

A **ViewModel** is a part of the **Model-View-ViewModel (MVVM)** design pattern.

MVVM is a convenient way to represent the interaction of the UI and the core (business logic of our app):

1. A **View** is a part of our code that generates what a user sees (not to be confused with Android’s `View` class but we could say that `View` personalizes the idea of the View).
2. A **Model** is a part of our code that represents what our application does. It typically exposes some interface regarding its functionality.
3. A **ViewModel** connects the two: it translates user actions in the interface (the View) into function calls of the Model.

Figure 2 illustrates these dependencies.

<div markdown="0">
<img class="lazyload" data-src="{{ page.images | absolute_url | append: "/MVVM.svg" }}" alt="MVVM pattern diagram">
</div>

_Figure {% increment figureId20220911 %}. Model-View-ViewModel (MVVM) pattern._

An important point is that the Model mustn’t know that the ViewModel exists. On the same note, the ViewModel mustn’t know that the View exists. After all, the logic of our applications (what it does) should not depend on the design of the interface.

This is called a **Unidirectional Data Flow** and is further discussed in [Google's official Android architecture guidelines](https://developer.android.com/topic/architecture/ui-layer#udf).

MVVM is an alternative to another design pattern called **Model-View-Controller (MVC).**

Even if you don’t fully understand what the ViewModel is, after going through this tutorial, you will definitely understand it!

<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6611455743195468"
     crossorigin="anonymous"></script><ins class="adsbygoogle"
     style="display:block; text-align:center;"
     data-ad-layout="in-article"
     data-ad-format="fluid"
     data-ad-client="ca-pub-6611455743195468"
     data-ad-slot="7289385396"></ins><script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>

## What Is a Model in the Synthesizer App?

To recap, here is the architecture of our app with parts that will be created in this part of the tutorial.

<div markdown="0">
<img class="lazyload" data-src="{{ page.images | absolute_url | append: "/SynthesizerArchitecture.svg" }}" alt="Component diagram of the app">
</div>

_Figure {% increment figureId20220911 %}. Synthesizer app architecture._

As you can see, `WavetableSynthesizerViewModel` depends on the `WavetableSynthesizer` interface. That allows us to decouple the Model and the ViewModel because the ViewModel will use the interface rather than a concrete implementation.

That also allows us to write the `WavetableSynthesizerViewModel` class before we implement our Model! As you can see in Figure 3, we will create a `LoggingWavetableSynthesizer` that simply logs that its methods were called.

## Wavetable Synthesizer Model Implementation

We’ll start by defining the interface of our synthesizer:

_Listing {% increment listingId20220911 %}. WavetableSynthesizer interface._

```kotlin
interface WavetableSynthesizer {
  suspend fun play()
  suspend fun stop()
  suspend fun isPlaying() : Boolean
  suspend fun setFrequency(frequencyInHz: Float)
  suspend fun setVolume(volumeInDb: Float)
  suspend fun setWavetable(wavetable: Wavetable)
}
```

What do particular methods do?

1. `play()` will start the sound playback.
2. `stop()` will stop it.
3. `isPlaying()` will return `true` if the synthesizer is playing and `false` otherwise.
4. `setFrequency()` will set the frequency of the synthesizer that is being played back.
5. `setVolume()` will set the volume of the sound that is being played back.
6. `setWavetable()` will set the played-back wavetable. If you don’t know what a wavetable is or why do we need it, I have described it thoroughly in my [wavetable synthesis algorithm article]({% post_url synthesis/2021-08-13-wavetable-synthesis-theory %}). I have also already shown how to implement a wavetable synthesizer [in Python]({% post_url synthesis/2021-08-27-wavetable-synthesis-python %}), [in C++]({% post_url synthesis/2021-09-24-wavetable-synthesis-juce %}), and [in Rust]({% post_url synthesis/2021-10-15-wavetable-synthesis-rust %}) so feel free to check out those articles.

You may be wondering why are the methods marked with `suspend`. Well… I will explain it later on 😉

## Wavetable Class

As you could notice in Listing 1, we used a `Wavetable` class but we didn’t define it. Let’s do it now.

_Listing {% increment listingId20220911 %}. WavetableSynthesizer.kt file._

```kotlin
package com.thewolfsound.wavetablesynthesizer

import androidx.annotation.StringRes

enum class Wavetable {
SINE{
    @StringRes
    override fun toResourceString(): Int {
      return R.string.sine
    }
  },

TRIANGLE{
    @StringRes
    override fun toResourceString(): Int {
      return R.string.triangle
    }
  },

SQUARE{
    @StringRes
    override fun toResourceString(): Int {
      return R.string.square
    }
  },

SAW{
    @StringRes
    override fun toResourceString(): Int {
      return R.string.sawtooth
    }
  };

  @StringRes
  abstract fun toResourceString(): Int
}

// below follows the WavetableSynthesizer interface.
```

For this code to work, we need to define the following string resources in the _res/values/strings.xml_ file.

_Listing {% increment listingId20220911 %}. strings.xml file._

```xml
<string name="sine">Sine</string>
<string name="triangle">Triangle</string>
<string name="square">Square</string>
<string name="sawtooth">Sawtooth</string>
```

One nice feature of Kotlin is that `enum`s can have abstract methods that we override in the concrete enum cases. In our code, `toResourceString()` is exactly such a method.

It is annotated with the `@StringRes` annotation, to indicate that the method should return a string resource id.

And that’s it when it comes to our Model’s interface! Now, let’s provide some dummy implementation.

## LoggingWavetableSynthesizer

To check that the correct methods of our synthesizer’s interface are called, we will implement a `LoggingWavetableSynthesizer` that implements the `WavetableSynthesizer` interface and logs the function of the called method along with the passed-in parameters.

_Listing {% increment listingId20220911 %}. LoggingWavetableSynthesizer.kt._

```kotlin
package com.thewolfsound.wavetablesynthesizer

import android.util.Log

class LoggingWavetableSynthesizer : WavetableSynthesizer {

  private var isPlaying = false

  override suspend fun play() {
    Log.d("LoggingWavetableSynthesizer", "play() called.")
    isPlaying = true
  }

  override suspend fun stop() {
    Log.d("LoggingWavetableSynthesizer", "stop() called.")
    isPlaying = false
  }

  override suspend fun isPlaying(): Boolean {
    return isPlaying
  }

  override suspend fun setFrequency(frequencyInHz: Float) {
    Log.d("LoggingWavetableSynthesizer", "Frequency set to $frequencyInHz Hz.")
  }

  override suspend fun setVolume(volumeInDb: Float) {
    Log.d("LoggingWavetableSynthesizer", "Volume set to $volumeInDb dB.")
  }

  override suspend fun setWavetable(wavetable: Wavetable) {
    Log.d("LoggingWavetableSynthesizer", "Wavetable set to $wavetable")
  }
}
```

As you can see, each method logs what is happening using the `Log.d` method from the `android.util`package. That ensures that these messages will appear in the Logcat of Android Studio when the application runs and the message level is set to "Debug".

<div markdown="0">
<img class="lazyload" data-src="{{ page.images | absolute_url | append: "/SampleLogcatOutput.webp" }}" alt="Sample output of the synthesizer app in the Logcat of Android Studio.">
</div>

_Figure {% increment figureId20220911 %}. Log messages in the Logcat of Android Studio._

With this code in place, we can finally implement our ViewModel!

## WavetableSynthesizerViewModel Class

Our ViewModel class inherits from the `ViewModel` class from the `androidx.lifecycle` package.

_Listing {% increment listingId20220911 %}. WavetableSynthesizerViewModel.kt._

```kotlin
package com.thewolfsound.wavetablesynthesizer

import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import kotlinx.coroutines.launch
import kotlin.math.exp
import kotlin.math.ln

class WavetableSynthesizerViewModel : ViewModel() {
```

That will allow us to obtain a reference to the correct ViewModel from our `MainActivity` class and also take advantage of the `viewModelScope` `CoroutineScope` of the `ViewModel` class.

### The Synthesizer Reference

To interact with the Model we need a reference to it. Therefore, we need a `WavetableSynthesizer` field in our ViewModel.

_Listing {% increment listingId20220911 %}. WavetableSynthesizerViewModel.kt._

```kotlin
var wavetableSynthesizer: WavetableSynthesizer? = null
set(value) {
  field = value
  applyParameters()
}
```

On the first line, we define the field containing the reference to our `WavetableSynthesizer`. The question mark `?` means that this field is nullable. Indeed, we initially assign it the `null` value. It is of a `var` type because we can reassign it later on.

The setter below the field is a purely Kotlin construct.

It allows to set the value of the `wavetableSynthesizer` through a "backing field" (`field` context keyword). That saves us some typing 😄

After the assignment we call `applyParameters()` to update the synthesizer’s parameters. I will show you the implementation of this method later in this tutorial.

### Setting the Frequency

Next up there is code related to frequency handling.

First, we declare the UI state variable holding the frequency state.

_Listing {% increment listingId20220911 %}. WavetableSynthesizerViewModel.kt._

```kotlin
private val _frequency = MutableLiveData(300f)
val frequency: LiveData<Float>
  get() {
    return _frequency
  }
```

If you don’t know what state hoisting is, you can read about it in the [previous tutorial part]({% post_url synthesis/android-wavetable-synthesizer/2022-08-10-ui %}).

The private `_frequency` field is of type `MutableLiveData` , which represents an **observable, mutable state**.

On the other hand, `frequency`, which is a public property, is of type `LiveData` , which represents an immutable state.

`LiveData` instances can be **observed** so that the observer is notified when the value of the observed state changes. However, the observer cannot directly modify the value of the observed state.

As you can see in the Kotlin-style getter, the clients of our ViewModel can observe a `LiveData` instance that is actually of type `MutableLiveData` under the hood.

This is an example of **state hoisting in the ViewModel.**

Ain’t that elegant?

### Slider Position to Frequency Value

As you remember, the user controls the frequency of the synthesizer via a slider.

<div markdown="0">
<img class="lazyload" data-src="{{ page.images | absolute_url | append: "/FrequencySlider.webp" }}" alt="Frequency control slider of the synthesizer app.">
</div>

_Figure {% increment figureId20220911 %}. Frequency control slider._

This slider value is in the [0, 1] range for simplicity. In the ViewModel, we take the slider value and convert it to frequency what can be seen in Listing 8.

_Listing {% increment listingId20220911 %}. WavetableSynthesizerViewModel.kt._

```kotlin
/**
 * @param frequencySliderPosition slider position in [0, 1] range
 */
fun setFrequencySliderPosition(frequencySliderPosition: Float) {
  val frequencyInHz = frequencyInHzFromSliderPosition(frequencySliderPosition)
  _frequency.value = frequencyInHz
  viewModelScope.launch {
    wavetableSynthesizer?.setFrequency(frequencyInHz)
  }
}
```

3 things happen in this function:

1. We calculate the synthesizer’s frequency in Hz from the slider position.
2. We set the calculated frequency to the `value` property of the `MutableLiveData` instance representing the frequency which **causes the composable containing the slider to recompose**.
3. We set the frequency of the `wavetableSynthesizer` instance in a **Kotlin coroutine**.

Let’s tackle these issues one by one.

### Calculating the Logarithmic Frequency Value from Slider Position

**Human perception of frequency is logarithmic.**

That’s why we need to map the slider position from the [0, 1] range to the same range but with a different "distribution" of values. I have discussed the logarithmic approach to musical parameters in the [envelope article]({% post_url synthesis/2022-07-03-envelopes %}) so please refer to it for more information.

To convert the slider position to a frequency value, we

1. convert the value from the linear to the exponential distribution, and
2. convert the relative position in the [0, 1] range to a value within in a specified frequency range.

_Listing {% increment listingId20220911 %}. WavetableSynthesizerViewModel.kt._

```kotlin
// The range of generated frequencies
private val frequencyRange = 40f..3000f

private fun frequencyInHzFromSliderPosition(sliderPosition: Float): Float {
  val rangePosition = linearToExponential(sliderPosition)
  return valueFromRangePosition(frequencyRange, rangePosition)
}
```

The inverse operation (frequency value to slider position) is analogous:

_Listing {% increment listingId20220911 %}. WavetableSynthesizerViewModel.kt._

```kotlin
fun sliderPositionFromFrequencyInHz(frequencyInHz: Float): Float {
  val rangePosition = rangePositionFromValue(frequencyRange, frequencyInHz)
  return exponentialToLinear(rangePosition)
}
```

The referenced functions are contained in a small helper class that I wrote as a `companion object`. All functions in a companion object are equivalent to Java’s static methods.

_Listing {% increment listingId20220911 %}. WavetableSynthesizerViewModel.kt._

```kotlin
companion object LinearToExponentialConverter {

  private const val MINIMUM_VALUE = 0.001f
  fun linearToExponential(value: Float): Float {
    assert(value in 0f..1f)

    if (value < MINIMUM_VALUE) {
      return 0f
    }

    return exp(ln(MINIMUM_VALUE) - ln(MINIMUM_VALUE) * value)
  }

  fun valueFromRangePosition(range: ClosedFloatingPointRange<Float>,
    rangePosition: Float) =
    range.start + (range.endInclusive - range.start) * rangePosition

  fun rangePositionFromValue(range: ClosedFloatingPointRange<Float>,
    value: Float): Float {
    assert(value in range)

    return (value - range.start) / (range.endInclusive - range.start)
  }

  fun exponentialToLinear(rangePosition: Float): Float {
    assert(rangePosition in 0f..1f)

    if (rangePosition < MINIMUM_VALUE) {
      return rangePosition
    }

    return (ln(rangePosition) - ln(MINIMUM_VALUE)) / (-ln(MINIMUM_VALUE))
  }
}
```

### Updating the View

The assignment  `_frequency.value = frequencyInHz` sets the value of the `MutableLiveData` instance that holds the UI frequency value. This causes the UI to recompose and display the new value. We will see how the composables observe `LiveData` later on.

### Updating the Model

The lines

_Listing {% increment listingId20220911 %}. WavetableSynthesizerViewModel.kt._

```kotlin
  viewModelScope.launch{
    wavetableSynthesizer?.setFrequency(frequencyInHz)
  }
```

launch a coroutine in the `viewModelScope` `CoroutineScope` . Inside the coroutine our wavetable synthesizer model has its frequency set.

The `viewModelScope` is a `CoroutineScope` that ships with every `ViewModel`-extending class. It is recommended by Google to use `viewModelScope` rather than introduce a new scope. In essence, it makes the developers’ life easier because we don’t have to define it ourselves.

### What Is a Coroutine in Kotlin?

A **coroutine** in Kotlin is a piece of code that is being executed in a certain environment. This environment takes care of the coroutine lifetime; for example, the execution of the coroutine code may be aborted when the parent scope is destroyed.

The coroutine may be executed on a different thread but does not have to be. The coroutine concept does not enforce the way its code is executed which is a great advantage.

### When Do We Use Kotlin Coroutines?

We use Kotlin Coroutines mostly when we want to execute some piece of code that will take a longer time to process in a controlled environment.

Coroutines make it easy to specify which code should be executed after the time-costly operation concludes. If not for the coroutines, we would need to use some sort of a callback to achieve the same effect.

### Why Do We Have to Use a Coroutine Here?

Only because we marked `setFrequency()` method of the `WavetableSynthesizer` interface as a suspended function by using the `suspend` keyword. Suspended function must always be executed in a coroutine scope.

### What Are Suspended Functions in Kotlin?

Suspended functions can be terminated by their parent scope. That is why they need to be executed in a `CoroutineScope`.

To mark a function or a method as suspended, we write the `suspend` keyword before `fun`.

We marked the method of the `WavetableSynthesizer` interface as suspended because we assume that they **may** be costly in terms of execution time.

Marking them as suspended does not mean that they will be executed on a different thread but it gives them a chance to do so if it’s deemed necessary by the programmer. You will see what I mean when we start to implement the `NativeWavetableSynthesizer` class in the next part of the tutorial.

### Setting the Volume

Having explained the UI state in the ViewModel and Kotlin coroutines, the code for controlling the volume in decibels should be clear.

_Listing {% increment listingId20220911 %}. WavetableSynthesizerViewModel.kt._

```kotlin
private val _volume = MutableLiveData(-24f)
val volume: LiveData<Float>
  get() {
    return _volume
  }
val volumeRange = (-60f)..0f

fun setVolume(volumeInDb: Float) {
    _volume.value = volumeInDb
    viewModelScope.launch {
      wavetableSynthesizer?.setVolume(volumeInDb)
    }
  }
```

### Setting the Wavetable

Setting the wavetable is even simpler than the volume.

_Listing {% increment listingId20220911 %}. WavetableSynthesizerViewModel.kt._

```kotlin
private var wavetable = Wavetable.***SINE***

fun setWavetable(newWavetable: Wavetable) {
    wavetable = newWavetable
    viewModelScope.launch {
      wavetableSynthesizer?.setWavetable(newWavetable)
    }
  }
```

### Changing the Play State

When a user clicks on the "Play" button the playing state changes.

Ideally, the label of the button should change as well.

The following code states this idea.

_Listing {% increment listingId20220911 %}. WavetableSynthesizerViewModel.kt._

```kotlin
private val _playButtonLabel = MutableLiveData(R.string.play)
val playButtonLabel: LiveData<Int>
  get() {
    return _playButtonLabel
  }

fun playClicked() {
  // play() and stop() are suspended functions => we must launch a coroutine
  viewModelScope.launch {
    if (wavetableSynthesizer?.isPlaying() == true) {
      wavetableSynthesizer?.stop()
    } else {
      wavetableSynthesizer?.play()
    }
    // Only when the synthesizer changed its state, update the button label.
    updatePlayButtonLabel()
  }
}

private fun updatePlayButtonLabel() {
    viewModelScope.launch {
      if (wavetableSynthesizer?.isPlaying() == true) {
        _playButtonLabel.value = R.string.stop
      } else {
        _playButtonLabel.value = R.string.play
      }
    }
  }
```

For the above code to work we must update our _strings.xml_ file with the following entry:

_Listing {% increment listingId20220911 %}. Update to the strings.xml file._

```xml
<string name="stop">Stop</string>
```

### Applying the Parameters

At certain points in the execution, we may wish to update all the synthesizer parameters. For example, when we resume the app from the background.

For this, we have the `applyParameters()` method, which is shown next.

_Listing {% increment listingId20220911 %}. WavetableSynthesizerViewModel.kt._

```kotlin
fun applyParameters() {
  viewModelScope.launch{
    wavetableSynthesizer?.setFrequency(frequency.value!!)
    wavetableSynthesizer?.setVolume(volume.value!!)
    wavetableSynthesizer?.setWavetable(wavetable)
    updatePlayButtonLabel()
  }
}
```

The `!!` operator states that we are sure that the given variable is not `null` . Because we initialize `volume` and `frequency` with default values, we are sure that their `value` properties are not `null`.

Without the `!!` , Kotlin compiler would complain that we don’t check for `null`. That is because the `value` property of `LiveData` has been marked with the `?` sign (it is a nullable property).

Again, we must call the above methods in a `CoroutineScope`.

## Updating the Composable Hierarchy

How to integrate the `ViewModel` into composables?

In essence,

- the composables should call `ViewModel` methods in its event handlers, and
- the state-hoisting composables should observe `ViewModel`'s properties rather than define their own state. In this way, the state will be hoisted by the `ViewModel` and the composables will just be observers. This makes them even "thinner" and more testable.

How to achieve it?

By passing the `WavetableSynthesizerViewModel` down the composables’ hierarchy as an additional argument.

Below you will find just the state-hoisting composables and how they changed in comparison to the [previous tutorial part]({% post_url synthesis/android-wavetable-synthesizer/2022-08-10-ui %}).

Note that you have to modify the signatures of the composable functions to account for the ViewModel argument.

_Listing {% increment listingId20220911 %}. MainActivity.kt._

```kotlin
@Composable
private fun VolumeControl(modifier: Modifier,
    synthesizerViewModel: WavetableSynthesizerViewModel) {
  // volume value is now an observable state; that means 
  // that the composable will be
  // recomposed (redrawn) when the observed state changes.
  val volume = synthesizerViewModel.volume.observeAsState()

  VolumeControlContent(
    modifier = modifier,
    // volume value should never be null; if it is, 
    // there's a serious implementation issue
    volume = volume.value!!,
    // use the value range from the ViewModel
    volumeRange = synthesizerViewModel.volumeRange,
    // on volume slider change, just update the ViewModel
    onValueChange = {synthesizerViewModel.setVolume(it)}
  )
}
```

*Note:* To be able to use `observeAsState()` of `LiveData`, you need to import an additional dependency. To do this, add the following line to your app module's *build.gradle* file ("dependencies" section):

_Listing {% increment listingId20220911 %}. MainActivity.kt._
```gradle
dependencies {
  //...
  implementation "androidx.compose.runtime:runtime-livedata:$compose_version"
}
```

As a reminder, `compose_version` is equal to `'1.1.1'` in this project.

_Listing {% increment listingId20220911 %}. MainActivity.kt._

```kotlin
@Composable
private fun PlayControl(modifier: Modifier,
    synthesizerViewModel: WavetableSynthesizerViewModel) {
  // The label of the play button is now an observable state,
  // an instance of State<Int?>.
  // State<Int?> is used because the label is the id value of the resource string.
  // Thanks to the fact that the composable observes the label,
  // the composable will be recomposed (redrawn) when the observed state changes.
  val playButtonLabel = synthesizerViewModel.playButtonLabel.observeAsState()

  PlayControlContent(modifier = modifier,
    // onClick handler now simply notifies the ViewModel that it has been clicked
    onClick = {
        synthesizerViewModel.playClicked()
    },
    // playButtonLabel will never be null;
    // if it is, then we have a serious implementation issue
    buttonLabel = stringResource(playButtonLabel.value!!))
}
```

_Listing {% increment listingId20220911 %}. MainActivity.kt._

```kotlin
@Composable
private fun WavetableSelectionButtons(
  modifier: Modifier,
  synthesizerViewModel: WavetableSynthesizerViewModel
) {
  Row(
    modifier = modifier.fillMaxWidth(),
    horizontalArrangement = Arrangement.SpaceEvenly
  ) {
   for (wavetable in Wavetable.values()) {
      WavetableButton(
        modifier = modifier,
        // update the ViewModel when the given wavetable is clicked
        onClick = {
            synthesizerViewModel.setWavetable(wavetable)
        },
        // set the label to the resource string that corresponds to the wavetable
        label = stringResource(wavetable.toResourceString()),
      )
    }
  }
}
```

_Listing {% increment listingId20220911 %}. MainActivity.kt._

```kotlin
@Composable
private fun PitchControl(
  modifier: Modifier,
  synthesizerViewModel: WavetableSynthesizerViewModel
) {
  // if the frequency changes, recompose this composable
  val frequency = synthesizerViewModel.frequency.observeAsState()
  // the slider position state is hoisted by this composable;
  // no need to embed it into
  // the ViewModel, which, ideally, shouldn't be aware of the UI.
  // When the slider position changes, this composable will be
  // recomposed as we explained in
  // the UI tutorial.
  val sliderPosition = rememberSaveable{
      mutableStateOf(
        // we use the ViewModel's convenience function
        // to get the initial slider position
        synthesizerViewModel.sliderPositionFromFrequencyInHz(frequency.value!!)
      )
    }

    PitchControlContent(
      modifier = modifier,
      pitchControlLabel = stringResource(R.string.frequency),
      value = sliderPosition.value,
      // on slider position change, update the slider position and the ViewModel
      onValueChange = {
        sliderPosition.value = it
        synthesizerViewModel.setFrequencySliderPosition(it)
      },
    // this range is now [0, 1] because the ViewModel is
    // responsible for calculating the frequency
    // out of the slider position
    valueRange = 0F..1F,
    // this label could be moved into the ViewModel but
    // it doesn't have to be because this
    // composable will anyway be recomposed on a frequency change
    frequencyValueLabel = stringResource(R.string.frequency_value,
        frequency.value!!)
  )
}
```

## Wiring in the MainActivity Class

The final thing to do is to instantiate a `WavetableSynthesizer` and a `ViewModel` in the `MainActivity` class.

It is ok to name concrete classes here (rather than interfaces) because `MainActivity` is regarded as a "dirty" class, where the whole initialization takes place.

_Listing {% increment listingId20220911 %}. MainActivity.kt._

```kotlin
//...
// These are the new imports in to MainActivity.kt
import androidx.activity.viewModels
import androidx.compose.runtime.livedata.observeAsState
import androidx.lifecycle.viewmodel.compose.viewModel
//...

class MainActivity : ComponentActivity() {

  private val synthesizer = LoggingWavetableSynthesizer()
  private val synthesizerViewModel: WavetableSynthesizerViewModel by viewModels()
//...
```

Because of the way activities are set up, we can use the convenient `by viewModels()` call to get a reference to the the `WavetableSynthesizerViewModel` instance.

We instantiate the synthesizer as a `LoggingWavetableSynthesizer` because we haven’t implemented the native one yet.

We should also update the parameters in the `onResume()` method of `MainActivity`.

_Listing {% increment listingId20220911 %}. MainActivity.kt._

```kotlin
override fun onResume() {
  super.onResume()
  synthesizerViewModel.applyParameters()
}
```

This ensures that we have a correct state when we resume the app.

Finally, the wiring in `onCreate()` method looks as follows.

_Listing {% increment listingId20220911 %}. MainActivity.kt._

```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
  super.onCreate(savedInstanceState)
  requestedOrientation = ActivityInfo.SCREEN_ORIENTATION_LANDSCAPE
  // pass the synthesizer to the ViewModel
  synthesizerViewModel.wavetableSynthesizer = synthesizer
  setContent{
    WavetableSynthesizerTheme{
        Surface(modifier = Modifier.fillMaxSize(),
            color = MaterialTheme.colors.background) {
            // pass the ViewModel down the composables' hierarchy
            WavetableSynthesizerApp(Modifier, synthesizerViewModel)
        }
      }
  }
}
```

And that’s it! You should be able to build and run your synthesizer in an emulator now.

## Running the Synthesizer in the Emulator

When you now build and run the synthesizer in the emulator, you should be able to click the "play" button, the wavetable buttons, and change the sliders’ values. Each change should generate an appropriate entry in the Logcat.

A sample Logcat output may look as follows.

_Listing {% increment listingId20220911 %}. Sample Logcat output._

```text
2022-09-09 20:00:18.845 6484-6484/com.thewolfsound.wavetablesynthesizer D/LoggingWavetableSynthesizer: play() called.
2022-09-09 20:00:19.807 6484-6484/com.thewolfsound.wavetablesynthesizer D/LoggingWavetableSynthesizer: Frequency set to 73.56122 Hz.
2022-09-09 20:00:20.643 6484-6484/com.thewolfsound.wavetablesynthesizer D/LoggingWavetableSynthesizer: Frequency set to 163.21312 Hz.
2022-09-09 20:00:21.469 6484-6484/com.thewolfsound.wavetablesynthesizer D/LoggingWavetableSynthesizer: Wavetable set to TRIANGLE
2022-09-09 20:00:22.466 6484-6484/com.thewolfsound.wavetablesynthesizer D/LoggingWavetableSynthesizer: Wavetable set to SAW
2022-09-09 20:00:23.951 6484-6484/com.thewolfsound.wavetablesynthesizer D/LoggingWavetableSynthesizer: Volume set to -13.3431 dB.
2022-09-09 20:00:24.823 6484-6484/com.thewolfsound.wavetablesynthesizer D/LoggingWavetableSynthesizer: Volume set to -44.528576 dB.
2022-09-09 20:00:26.524 6484-6484/com.thewolfsound.wavetablesynthesizer D/LoggingWavetableSynthesizer: stop() called.
```

If you cannot see these logs for some of the changes or controls or your app crashes that means that you’ve made an error along the way or I forgot to include something in the tutorial 🙃

Congratulations! You have just implemented the modern Android architecture guidelines! 👏

## Part 3 Summary

In this part of the Android wavetable synthesizer app tutorial we have

- explained what the Model-View-ViewModel (MVVM) architecture is about,
- implemented the ViewModel of our app,
- converted linear sliders into exponential sliders,
- explained what are Kotlin coroutines,
- used Kotlin coroutines in the `viewModelScope` to update the state of the Model,
- created a `LoggingWavetableSynthesizer` class for testing purposes,
- updated the UI to rely mostly on the state in the ViewModel,
- tested our app with logs in the Logcat.

And all this according to the [modern Android architecture guidelines](https://developer.android.com/topic/architecture).

Whew! We’re awesome 😎

Next up: [making a bridge between the Kotlin code and the C++ code using Java Native Interface (JNI)!]({% post_url synthesis/android-wavetable-synthesizer/2022-10-09-jni %})
