#!/usr/bin/env python3
''' 길이가 n인 배열에서 m개의 원소를 무작위로 추출하는
메서드를 작성하라. 각 원소가 선택될 확률은 동일해야 한다. '''

import unittest
from random import randint

def shuffled_index(cnt):
    ''' iterator '''
    res = list(range(cnt))
    for i in range(cnt):
        #invariant #res[0:i] is selected
        nextint = randint(i, cnt-1)
        res[nextint], res[i] = res[i], res[nextint]
        yield res[i]
        #invariant #res[0:i+1] is selected

def select_random(m, n):
    assert 0<=n<=m
    it = shuffled_index(m)
    return [next(it) for _ in range(n)]

class SelectRandomTest(unittest.TestCase):
    def test_assertionError(self):
        with self.assertRaises(AssertionError):
            self.assertRandomlySelected(10, -1)

        with self.assertRaises(AssertionError):
            self.assertRandomlySelected(10, 111)

    def test_samples(self):
        self.assertRandomlySelected(10, 0)
        self.assertRandomlySelected(10, 5)
        self.assertRandomlySelected(10, 8)
        self.assertRandomlySelected(10, 10)

    def assertRandomlySelected(self, m, n):
        res = select_random(m, n)
        self.assertEqual(len(res), n)
        for i in res:
            self.assertTrue( 0<= i < m)

if __name__=="__main__":
    unittest.main()
