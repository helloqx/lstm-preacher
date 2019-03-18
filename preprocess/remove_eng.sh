#!/bin/bash
# Removes english characters and spaces.
IFS='
'

for file in ./*.txt
do
  cat $file | sed 's/[A-Za-z]//g' | sed 's/\s//g' > tmp
  mv tmp $file
done
