#!/usr/bin/env python3
# usage: cmd <from.lst> <to.lst> [-suffix] [+suffix]

import os
import sys

def main(from_lst, to_lst, suffixes):
    with open(from_lst, 'r') as fp:
        lst1 = fp.read().strip().split('\n')
    with open(to_lst, 'r') as fp:
        lst2 = fp.read().strip().split('\n')
    assert len(lst1) == len(lst2)
    
    for f, t in zip(lst1, lst2):
        rename(f, t, suffixes)

def rename(frm, to, suffixes):
    to2 = apply_suffixes(to, suffixes)
    os.rename(frm, to2)

def apply_suffixes(to, suffixes):
    ss = suffixes
    res = to
    for s in ss:
        assert s and len(s)>0 and s[0] in '+-'
        if s[0]=='+':
            res += s[1:]
        else:
            res = res.rstrip(s[1:])
    return res

if __name__=='__main__':
    _, from_lst, to_lst, *suffixes = sys.argv
    main(from_lst, to_lst, suffixes)

