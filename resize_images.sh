#!/bin/bash

FOLDER="."

OUTPUT_FOLDER="./resized_images"
mkdir -p "$OUTPUT_FOLDER"

for file in "$FOLDER"/*.png; do
    if [ -f "$file" ]; then
        output_file="$OUTPUT_FOLDER/$(basename "$file")"
        echo "Processing $file -> $output_file"
        convert "$file" -resize 1920x1080\! "$output_file"
    fi
done

echo "Tüm işlemler tamamlandı. Dosyalar $OUTPUT_FOLDER dizininde."

