#!/bin/bash

# Replace input.txt with the path to your text file
input="kg_list.txt"

while IFS= read -r line
do
  echo $line
  rclone sync "lakefs://$line" "./lakefs/$line"
done < "$input"

