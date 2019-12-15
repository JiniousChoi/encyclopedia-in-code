#!/bin/bash
## author: jinchoiseoul@gmail.com

if [ -z $1 ]; then
    echo '[Error] argument is missing: enter `path/file`'
    exit -1
fi

if [ -f "${1}.hs" ]; then
    echo "[Skip] ${1}.hs exists already"
else
    echo -e "#!/usr/bin/runhaskell\n-- author: jinchoiseoul@gmail.com\n" >> "${1}.hs"
    echo "[+] ${1}.hs is created"
fi

if [ -f "${1}.scala" ]; then
    echo "[Skip] ${1}.scala exists already"
else
    echo -e "#!/usr/bin/env scala\n// author: jinchoiseoul@gmail.com\n" >> "${1}.scala"
    echo "[+] ${1}.scala is created"
fi
