#!/bin/bash

: ${NAME:?"Name must not be empty"}

bash -c ./step1.sh

bash ./step2.sh

export | grep -i name
