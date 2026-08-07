#!/bin/bash

for fruit in apple banana cherry; do
    echo "I like $fruit"
done

for file in old_website/*.htm; do
    name=$(basename "$file" .htm)
    #echo mv "$file" "new_website/$name.html" for testing purposes

    mv "$file" "new_website/$name.html"

done