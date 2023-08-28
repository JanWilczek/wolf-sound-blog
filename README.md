# WolfSound Blog

Source code of my WolfSound audio programming blog. The site runs on Jekyll and can be found under www.thewolfsound.com.

## Useful commands

To run the test server

```bash
npx @11ty/eleventy --serve
```

To build pngs from latex files:

```bash
latexmk filename.tex -shell-escape
```

To resize a png image and convert it to a webp image:

```bash
cwebp Thumbnail.png -q 65 -s 1024 0 -o Thumbnail.webp
```
