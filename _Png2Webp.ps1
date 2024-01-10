foreach ($file in Get-ChildItem $args[0]) {
    cwebp -resize 550 0 -preset drawing $file -o $([System.IO.Path]::ChangeExtension($file, '.webp'))
}
