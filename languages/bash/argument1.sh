#!/bin/bash

if [ -z "$1" ]
then
    echo "failed";
    echo "no argument";
    exit 1;
fi

echo "succeed"
echo "$1"

