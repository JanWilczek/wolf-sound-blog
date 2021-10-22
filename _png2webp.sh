#!/bin/bash

for file in $1/*.png
do
    cwebp -q 20 $file -o ${file::-4}.webp
done
