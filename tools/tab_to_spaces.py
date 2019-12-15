#!/usr/bin/python3
## author: jinchoiseoul@gmail.com

''' Mostly for converting python script with mixed tabs and spaces for indentation '''

import sys

def tab_to_spaces(lines):
    return lines.replace('\t', 4*' ')

if __name__=="__main__":
    s = sys.stdin.read()
    print(tab_to_spaces(s))
