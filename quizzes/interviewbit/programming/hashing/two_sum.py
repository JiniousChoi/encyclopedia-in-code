#!/usr/bin/python3
## author: jinchoiseoul@gmail.com


class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def twoSum(self, A, B):
        failmap = {}
        for ai, av in enumerate(A, 1):
            if B-av in failmap:
                return [failmap[B-av], ai]
            failmap[av] = ai
        return []


import unittest
from math import nan


class SolutionTest(unittest.TestCase):

    def test_basics(self):
        sol = Solution()
        self.assertEqual(sol.twoSum([], nan), [])
        self.assertEqual(sol.twoSum([2, 7, 11, 15], 9), [1,2])


if __name__ == "__main__":
    
    unittest.main()
