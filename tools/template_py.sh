#!/bin/bash
## author: jinchoiseoul@gmail.com

if [ -z $1 ]; then
    echo '[Error] argument is missing: enter `path/file`'
    exit -1
fi

if [ -f "${1}.py" ]; then
    echo "[Skip] ${1}.py exists already"
else
	cat << EOF >> "${1}.py"
#!/usr/bin/python3
## author: jinchoiseoul@gmail.com


#code starts here


import unittest


class SolutionTest(unittest.TestCase):
    def test_basics(self):
        pass


if __name__ == "__main__":

    unittest.main()
EOF
	chmod u+x ${1}.py
    echo "[+] ${1}.py is created"
fi
