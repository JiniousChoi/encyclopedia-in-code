#!/usr/bin/env python3

import unittest
from main import *

class StreamTest(unittest.TestCase):
    def setUp(self):
        self.some_nums = stream_from([3,6,9])
        self.some_chars = stream_from(list("abc"))
        self.some_primes = stream_from([7,11,19])

    def assertStreamIs(self, stream, col):
        self.assertEqual(stream_reduce(stream, lambda z,v: z+[v], []), col)

    def assertStreamIsNot(self, stream, col):
        self.assertNotEqual(stream_reduce(stream, lambda z,v: z+[v], []), col)

    def test_primes(self):
        all_primes = stream_filter(natural(1), is_prime)
        ten_primes = stream_take(all_primes, 10)
        self.assertStreamIs(ten_primes, [2,3,5,7,11,13,17,19,23,29])

    def test_take(self):
        nat = natural(1)
        take10 = stream_take(nat, 10)
        take5 = stream_take(take10, 5)
        take15 = stream_take(take5, 15)
        self.assertStreamIs(take15, [1,2,3,4,5])

    def test_stream_sum(self):
        nat = natural(1)
        take10 = stream_take(nat, 10)
        self.assertEqual(stream_sum(take10), 55)

    def test_stream_sum_with_dropping(self):
        nat = natural(1)
        nat_from_11 = stream_drop(nat, 10)
        nat_11_to_20 = stream_take(nat_from_11, 10)
        self.assertEqual(stream_sum(nat_11_to_20), 155)

    def test_stream_it(self):
        ns = (i for i in [1,2,3])
        s = stream_it(ns)
        self.assertEqual(stream_sum(s), 6)

    def test_stream_it_pitfall(self):
        ns = (i for i in [1,2,3])
        s = stream_it(ns)
        self.assertEqual(stream_sum(s), 6)
        self.assertStreamIs(s, []) # because it is all consumed

    def test_stream_sum_and_mult(self):
        self.assertEqual(stream_sum(self.some_nums), 18)
        self.assertEqual(stream_mult(self.some_nums), 162)

    def test_chain_simple(self):
        chained = stream_chain(self.some_nums)
        self.assertStreamIs(chained, [3,6,9])

    def test_chain_complex(self):
        chained = stream_chain(self.some_nums, self.some_chars, self.some_primes)
        self.assertStreamIs(chained, [3,6,9,'a','b','c',7,11,19])

    def test_chain_two(self):
        chained = stream_chain_two(self.some_nums, self.some_chars)
        self.assertStreamIs(chained, [3,6,9,'a','b','c'])

    def test_chain_two_twice(self):
        c2 = stream_chain_two(self.some_nums, self.some_chars)
        c3 = stream_chain_two(c2, self.some_primes)
        self.assertStreamIs(c3, [3,6,9,'a','b','c',7,11,19])
        
    def test_stream_chain_reduce(self):
        c4 = stream_chain_reduce(self.some_nums, self.some_chars, self.some_primes, self.some_nums)
        self.assertStreamIs(c4, [3,6,9,'a','b','c',7,11,19,3,6,9])


if __name__=='__main__':
    unittest.main()
