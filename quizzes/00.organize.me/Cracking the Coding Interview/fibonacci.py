#!/usr/bin/env python3

import unittest

def fib_recur(n):
    assert n>=0
    if n==0 or n==1: return 1
    return fib_recur(n-1) + fib_recur(n-2)

def fib_iter1(n):
    assert n>=0
    if n==0 or n==1: return 1
    i, j, k= 0, 1, 2
    Ai, Aj, Ak=1, 1, 2
    while k<n:
        i, j, k= i+1, j+1, k+1
        Ai, Aj, Ak = Aj, Ak, Aj+Ak
    assert k==n
    return Ak

def fib_iter2(n):
    assert n>=0
    if n==0 or n==1: return 1
    i, j, k= 0, 1, 2
    Ai, Aj, Ak=1, 1, 2
    while True:
        if k==n:
            break
        i, j, k= i+1, j+1, k+1
        Ai, Aj, Ak = Aj, Ak, Aj+Ak
    assert k==n
    return Ak

""" case1 == case2 == case3

[case1]
while cond:
    logic
assert not cond

[case2]
while True:
    if cond:
        logic
    else:
        break
assert not cond

[case3]
while True:
    if not cond:
        break
    logic
assert not cond
"""
class FibTest(unittest.TestCase):
    def test_amples(self):
        self.assertFib(0, 1)
        self.assertFib(1, 1)
        self.assertFib(2, 2)
        self.assertFib(3, 3)
        self.assertFib(4, 5)
        self.assertFib(5, 8)
        self.assertFib(6, 13)

    def assertFib(self, n, res):
        fibs = [fib_recur, fib_iter1, fib_iter2]
        for fib in fibs:
            self.assertEqual(res, fib(n))

    def test_samples2(self):
        res1 = fib_recur(10)
        res2 = fib_iter1(10)
        res3 = fib_iter2(10)
        self.assertEqual(res1, res2)
        self.assertEqual(res1, res3)
        self.assertEqual(res2, res3)


if __name__=="__main__":
    unittest.main()
