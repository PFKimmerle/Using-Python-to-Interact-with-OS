#!/bin/bash
# Clear the contents of oldFiles.txt or create it if it doesn't exist
> oldFiles.txt

# Search for lines containing ' jane ' in the file at ../data/list.txt,
# then cut out the third field in each line, which is assumed to be the filename.
files=$(grep " jane " ../data/list.txt | cut -d ' ' -f 3)

# Iterate through the list of filenames found
for f in $files; do
  # Check if a file exists in the home directory
  if [ -e $HOME$f ]; then
    # If the file exists, append the full path to the file to oldFiles.txt
    echo $HOME$f >> oldFiles.txt
  fi
done

