#!/bin/bash

docker run --rm -it --name SICP -v $(pwd):/source nacyot/scheme-guile:apt /bin/bash
