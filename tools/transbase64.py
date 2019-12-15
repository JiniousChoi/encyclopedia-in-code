#!/usr/bin/python3
## author: jinchoiseoul@gmail.com
## brief: transform plain_text/binary <-> text_in_base64


import sys
import base64
import argparse


## parsing args
parser = argparse.ArgumentParser(description='encode/decode sequence in base64')

parser.add_argument('type', choices=['decode', 'encode'])

group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-f', '--filein', help='file input')
group.add_argument('-s', '--stdin', help='standard input')

args = parser.parse_args()


## prepare target sequence to be encoded/decoded
if args.filein:
    filename = args.filein
    seq = open(filename, 'rb').read()
elif args.stdin:
    seq = args.stdin
else:
    raise Exception("unreachable")


## process encoding/decoding

if args.type == 'decode':
    b_res = base64.b64decode(seq)
elif args.type == 'encode':
    b_res = base64.b64encode(seq)
else:
    raise Exception("unreachable")

sys.stdout.buffer.write(b_res)
print()
