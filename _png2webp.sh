#!/bin/bash

for file in $1/*.png
do
    cwebp -resize 550 0 -preset drawing $file -o ${file::-4}.webp
done
