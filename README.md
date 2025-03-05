# WolfSound Blog

Source code of my WolfSound audio programming blog. The site runs on Eleventy and can be found under [https://thewolfsound.com](https://thewolfsound.com).

## Useful commands

Before you build the website or run in dev mode, run

```bash
npm install

git lfs install
git lfs pull # to get the actual images locally

npx gulp # to package local dependencies
```

to copy the CSS assets to the right folders.

To run the test server

```bash
npx @11ty/eleventy --serve
# or
npm start
```

To build the website to the *_site* folder.

```bash
npm run build
```

To build pngs from latex files:

```bash
latexmk filename.tex -shell-escape
```

To resize a png image and convert it to a webp image:

```bash
cwebp Thumbnail.png -q 65 -s 1024 0 -o Thumbnail.webp
```

## Eleventy Snippets ✂️

### Including an include

```md
{% include 'podcast_cta' %}
{% include 'youtube-video', video_id: '5DFUH0zCn3Y' %}
```

### Linking to a post

```md
[Partitioned convolution]({% post_url collections.posts, '2021-05-14-fast-convolution' %})
```

### Linking to a page

```md
[About me]({% link collections.all, 'about.md' %})
```

### Embedding an audio file

```md
{% render 'embed-audio.html', src: "/assets/wav/posts/synthesis/2022-06-26-sine-saw-square-triangle-basic-waveforms-in-synthesis/sine_example.flac" %}
```

## All tags used

- sound wave
- sampling (A/D conversion)
- quantization
- sample rate
- aliasing
- effects
- python
- software architecture
- design principles
- testing
- c
- cpp
- convolution
- filtering
- maths
- fourier
- laplace
- transform
- impulse
- template metaprogramming
- correlation
- matlab
- probability
- wavetable
- waveform
- sampling (sound generation)
- juce
- rust
- career
- learning
- research
- reverb
- deep learning
- virtual analog
- amplifiers
- simd
- hardware
- envelope
- android
- kotlin
- java
- virtual reality
- spatial audio
- acoustics
- accessibility
- cmake
- plugin
- web audio
- javascript
- typescript
- book review
- puredata
- iplug2
- swift
- flutter
- cmajor
- digital audio workstation
- audio generation
