#!/usr/bin/python3
## author: jinchoiseoul@gmail.com


from math import inf


def single_bit_ceil(n):
    ''' @return largest `1<<m` satisfying `2**m >= n`
        Note: 1<<m == 2**m '''
    if n==0: return 0
    p = 1
    while p < n:
        p <<= 1
    assert p >= n
    return p


def single_bit_floor(n):
    ''' @return largest `1<<m` satisfying `2**m <= n`
        Note: 1<<m == 2**m '''
    if n==0: return 0
    assert n > 0
    nxt, cur = n, inf
    while 0 < nxt:
        cur = nxt
        nxt &= nxt-1
    assert 0 == nxt < cur <= n
    return cur


import unittest


class BitsTest(unittest.TestCase):

    def test_single_bit_ceil(self):
        self.assertEqual(single_bit_floor(0), 0)

        self.assertEqual(single_bit_ceil(1), 1)
        self.assertEqual(single_bit_ceil(2), 2)

        self.assertEqual(single_bit_ceil(3), 4)
        self.assertEqual(single_bit_ceil(4), 4)

        self.assertEqual(single_bit_ceil(5), 8)
        self.assertEqual(single_bit_ceil(6), 8)
        self.assertEqual(single_bit_ceil(7), 8)
        self.assertEqual(single_bit_ceil(8), 8)

    def test_single_bit_floor(self):
        self.assertEqual(single_bit_floor(0), 0)

        self.assertEqual(single_bit_floor(1), 1)

        self.assertEqual(single_bit_floor(2), 2)
        self.assertEqual(single_bit_floor(3), 2)

        self.assertEqual(single_bit_floor(4), 4)
        self.assertEqual(single_bit_floor(5), 4)
        self.assertEqual(single_bit_floor(6), 4)
        self.assertEqual(single_bit_floor(7), 4)

        self.assertEqual(single_bit_floor(8), 8)


if __name__ == "__main__":

    unittest.main()
