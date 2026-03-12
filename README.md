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

## Running Python code

To run Python code, create a virtual environment first.

```bash
python -m venv venv # create virtual environment

# activate it
source venv/bin/activate # or .\venv\bin\Scripts\Activate.ps1 if you're using PowerShell

pip install . # install dependencies
```

You can then run the scripts like usual.

```bash
python _py/posts/synthesis/2025-03-01-fm-synthesis/fm_synthesis.py
```

## Eleventy Snippets ✂️

### Including an include

```liquid
{% include 'podcast_cta' %}
{% include 'youtube-video', video_id: '5DFUH0zCn3Y' %}
```

### Linking to a post

```liquid
[Partitioned convolution]({% post_url collections.posts, '2021-05-14-fast-convolution' %})
```

### Linking to a page

```liquid
[About me]({% link collections.all, 'about.md' %})
```

### Embedding an audio file

```liquid
{% render 'embed-audio.html', src: "/assets/wav/posts/synthesis/2022-06-26-sine-saw-square-triangle-basic-waveforms-in-synthesis/sine_example.flac" %}
```

### Embedding an image

```liquid
{% image "assets/img/posts/synthesis/2025-03-01-fm-synthesis/partials_amplitudes_in_3d.png", "alt text for you to fill" %}
```

This will generate optimized versions of images, no need to add any sizes or similar.

### Adding a caption to a figure

At the top of the article (but after the first line) paste:

```liquid
{% capture _ %}{% increment figureId20211022  %}{% endcapture %}
```

Then immediately underneath each image, paste:

```liquid
_Figure {% increment figureId20211022 %}. Block diagram of an FIR allpass filter._
```

## All tags used

- accessibility
- acoustics
- ai
- aliasing
- amplifiers
- android
- audio generation
- book review
- c
- career
- cmajor
- cmake
- convolution
- correlation
- cpp
- deep learning
- design principles
- digital audio workstation
- effects
- envelope
- filtering
- flutter
- fourier
- hardware
- impulse
- iplug2
- java
- javascript
- juce
- kotlin
- laplace
- learning
- maths
- matlab
- plugin
- probability
- puredata
- python
- quantization
- research
- reverb
- rust
- sample rate
- sampling (A/D conversion)
- sampling (sound generation)
- simd
- software architecture
- sound wave
- spatial audio
- swift
- template metaprogramming
- testing
- transform
- typescript
- virtual analog
- virtual reality
- waveform
- wavetable
- web audio
