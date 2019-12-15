#!/usr/bin/env python3

import unittest

def seed(i):
    assert i>=0
    if i==0:
        return 1983
    return (seed(i-1)*214013 + 2531011) % (1<<32)

def A(i):
    return seed(i) % 10000 + 1

def AA():
    seed = 1983
    while True:
        ret = seed % (1<<32)
        seed = (seed * 214013 + 2531011) % (1<<32)
        yield ret % 10000 + 1


def ites(start, stop, K):
    assert K > 0
    assert start <= stop

    a = A(start)

    #basis
    if start == stop:
        return 1 if a==K else 0

    #recursive
    res = ites(start+1, stop, K)

    if a < K:
        res += ites(start+1, stop, K-a)
    elif a == K:
        res += 1

    return res


class ITESTest(unittest.TestCase):
    def ITESResult(self, K, N, count):
        self.assertEqual(ites(0, N-1, K), count)

    def test_A(self):
        al = [A(i) for i in range(5)]
        self.assertEqual(al, [1984, 8791, 4770, 7665, 3188])

    def test_AA(self):
        iter_aa = AA()
        aal = [next(iter_aa) for i in range(5)]
        self.assertEqual(aal, [1984, 8791, 4770, 7665, 3188])

    def test_samples(self):
        self.ITESResult(K=8791, N=20, count=1)
        self.ITESResult(K=5265, N=5000, count=4)
        #self.ITESResult(K=3578452, N=5000000, count=1049)

if __name__ == "__main__":
    unittest.main()
