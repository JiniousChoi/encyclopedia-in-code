#!/usr/bin/python3
## author: jinchoiseoul@gmail.com
## brief: A file is given which contains 4 billion integers.
## case1) Assume 1GB memory is available.
## case2) Assume 10MB memory is available.


from array import array
from math import ceil


def case1_sufficient_memory(data):
    ''' 8Gbit is good enough for 4 billion interger bit vector '''
    n = ceil(len(data) / 8)
    arr = array('B', [0 for _ in range(n)])

    # insert
    for d in data:
        q,r = divmod(d, 8)
        arr[q] |= (1<<r)

    # query for most cases
    for i,a in enumerate(arr):
        if a == 255:
            continue
        for j in range(8):
            if (a & (1<<j)) > 0:
                continue
            return 8*i+j
        else:
            assert False, 'cannot reach here'

    # query for edge case
    return len(arr)*8


def case2_insufficient_memory():
    pass


import unittest


class SolutionTest(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(case1_sufficient_memory([1]), 0)
        self.assertEqual(case1_sufficient_memory([0,1,3]), 2)
        self.assertEqual(case1_sufficient_memory([1,0,3]), 2)
        self.assertEqual(case1_sufficient_memory([0,5,6,2,1,7,3]), 4)

        self.assertEqual(case1_sufficient_memory([]), 0)
        self.assertEqual(case1_sufficient_memory([0]), 1)
        self.assertEqual(case1_sufficient_memory([0,1]), 2)
        self.assertEqual(case1_sufficient_memory([0,1,2]), 3)
        self.assertEqual(case1_sufficient_memory([0,1,2,3,4,5,6,7]), 8)


if __name__ == "__main__":

    unittest.main()
