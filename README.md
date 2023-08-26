# WolfSound Blog
Source code of my WolfSound audio programming blog. The site runs on Jekyll and can be found under www.thewolfsound.com.

# Useful commands

To run the test server
```
bundle exec jekyll serve
```

To run the test server when working on an article
```
bundle exec jekyll serve --incremental
```

To build pngs from latex files:
```
latexmk filename.tex -shell-escape
```

To resize a png image and convert it to a webp image:

```bash
cwebp Thumbnail.png -q 65 -s 1024 0 -o Thumbnail.webp
```
