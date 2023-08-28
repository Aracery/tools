#!/bin/bash

# Get the path to the text file
file_path=$1

# Read the lines of the text file
while read line; do

  # Get the path to the folder
  folder_path=$line

  # Recursively remove the folder
  rm -rf $folder_path

done < $file_path
