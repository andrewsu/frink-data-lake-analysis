#!/bin/bash

# Replace input.txt with the path to your text file
input="kg_list.txt"

while IFS=$'\t' read -r remotePath localPath
do
  # Use "$remotePath" for the source and "$localPath" for the destination in the rclone command
  echo "REMOTE: $remotePath\tLOCAL: $localPath"
  rclone sync "lakefs://$remotePath" "$localPath"
done < "$input"

