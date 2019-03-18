#!/bin/bash

# Ignore spaces in filenames
IFS='
'

i=577
for file in ./*.txt
do
  mv $file $i.txt
  echo $file, $i
  i=$((i+1))
done
