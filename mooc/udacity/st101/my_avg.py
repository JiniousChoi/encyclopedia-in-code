#!/usr/bin/env python3

import unittest

def mean(A):
    return sum(A)/len(A)

def median(A):
    lenA = len(A)
    half = int(lenA/2)
    if lenA%2==0:
        return sum(A[half-1:half+1])/2
    else:
        return A[half]

def mode(A):
    from statistics import collections
    c = collections.Counter(A)
    return c.most_common()[0][0]

def mmm(A):
    A.sort()
    return mean(A), median(A), mode(A)

class MyAvgTest(unittest.TestCase):
    def test_method1(self):
        A = [5, 9, 100, 9, 97, 6, 9, 98, 9]
        self.assertEqual(mmm(A), (38.0, 9, 9))

if __name__=="__main__":
    unittest.main()
