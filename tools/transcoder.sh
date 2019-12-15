#!/bin/bash
## author: jinchoiseoul@gmail.com
## brief: fix broken windows-cp949-encoded files to utf8-encoded

while IFS='' read -r line || [[ -n "$line" ]]; do
    iconv -f cp949 -t utf-8 $line --output "${line}.new"
    mv "${line}.new" "$line"
    
done < "$1"
