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
