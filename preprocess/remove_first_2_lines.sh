#!/usr/local/bin/bash

for file in ./*.txt
  do
    tail -n+3 $file > tmp
    mv tmp $file
  done
