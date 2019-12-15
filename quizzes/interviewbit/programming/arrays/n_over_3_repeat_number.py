#!/usr/bin/python3
## author: jinchoiseoul@gmail.com


from collections import Counter


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        c = Counter(A)
        most_freq = c.most_common(1)
        if not most_freq:
            return -1
        i, cnt = most_freq[0]
        return i if len(A)/3 < cnt else -1


import unittest


class SolutionTest(unittest.TestCase):
    def test_basics(self):
        sol = Solution()
        self.assertEqual(sol.repeatedNumber([]), -1)
        self.assertEqual(sol.repeatedNumber([1,2,3,1,1]), 1)
        self.assertEqual(sol.repeatedNumber([3,3,3]), 3)
        self.assertEqual(sol.repeatedNumber([1,2,3]), -1)
        self.assertEqual(sol.repeatedNumber([1,2,3,4,5]), -1)


if __name__ == "__main__":

    unittest.main()
