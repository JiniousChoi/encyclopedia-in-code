#!/usr/bin/env python3

import unittest
from math import factorial
from functools import reduce
from operator import mul
from itertools import combinations_with_replacement as comb_r

def prisoners(days):
    '''아... comb_r이 경우의 수가 지수적으로 증가하는 관꼐로 현실적 계산이 불가하다.'''
    if days < 100:
        return 0
    up1 = factorial(100)
    down1 = 100**100
    up2 = sum(reduce(mul, each) for each in comb_r(range(1, 101), days-100)) if days>100 else 1
    down2 = 100 ** (days-100)

    return up1 / down1 * up2 / down2

def stats():
    days = 1
    while True:
        person = 1 - (0.99)**days
        yield days, person**100
        days += 1

def prisoners_simple():
    it_stats = stats()
    thresholds = [0.5, 0.6, 0.70, 0.80, 0.90, 0.95,\
            0.99, 0.999, 0.9999, 0.99999, 0.999999, 0.9999999999, 1]
    for threshold in thresholds:
        while True:
            days, thres = next(it_stats)
            if threshold <= thres:
                print("threshold(%s): %s days" %(thres, days))
                break

class XTest(unittest.TestCase):
    def test_method1(self):
        s = stats()
        while True:
            days, p1 = next(s)
            if days==101:
                break

        p2 = prisoners(101)
        self.assertEqual(p1, p2)

if __name__=="__main__":
    prisoners_simple()
    unittest.main()
