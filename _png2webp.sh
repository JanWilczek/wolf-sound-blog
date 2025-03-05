#!/bin/bash

for file in $1/*
do
    filename="${file%.*}"
    cwebp -preset drawing -resize 550 0 "$file" -o "$filename.webp"
done
