#!/usr/bin/env python3

import unittest
from main import *

class StreamTest(unittest.TestCase):
    def assertStreamIs(self, stream, col):
        self.assertEqual(stream_reduce(stream, lambda z,v: z+[v], []), col)

    def assertStreamIsNot(self, stream, col):
        self.assertNotEqual(stream_reduce(stream, lambda z,v: z+[v], []), col)

    def test_main(self):
        assert True

    def test_primes(self):
        all_primes = stream_filter(natural(1), is_prime)
        ten_primes = stream_take(all_primes, 10)
        self.assertStreamIs(ten_primes, [2,3,5,7,11,13,17,19,23,29])

    def test_test(self):
        nat = natural(1)
        take10 = stream_take(nat, 10)
        take5 = stream_take(take10, 5)
        take15 = stream_take(take5, 15)
        self.assertStreamIs(take15, [1,2,3,4,5])

    def test_stream_sum(self):
        ''' to make nat10 usable in builtin sum fn,
            it should be of an Iterator type,
            implementing: __iter__, __next__ methods,
            However, for simplicity, I prefer to make 
            a general reduce fn for such accumulating ones '''
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

    def test_streamify_col(self):
        some_nums = stream([3,6,9])
        self.assertStreamIs(some_nums, [3,6,9])
        self.assertEqual(stream_sum(some_nums), 18)
        self.assertEqual(stream_mult(some_nums), 162)

    @unittest.skip("doesn't work yet")
    def test_chain(self):
        some_nums = stream([3,6,9])
        some_chars = stream(list("abc"))
        chained1 = stream_chain(some_nums)
        chained2 = stream_chain(some_nums, some_chars)
        self.assertStreamIs(chained1, [3, 6, 9])
        self.assertStreamIs(chained2, [3, 6, 9, 'a', 'b', 'c'])

if __name__=='__main__':
    unittest.main()
