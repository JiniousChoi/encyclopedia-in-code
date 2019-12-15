#!/bin/bash
while read line
do
    name=$line
    echo $name
    iconv -f $name -t utf8 ./motd.unknown
done < $1
