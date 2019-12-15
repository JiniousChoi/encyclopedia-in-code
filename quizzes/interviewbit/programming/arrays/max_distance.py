#!/usr/bin/python3
## author: jinchoiseoul@gmail.com

from itertools import accumulate
from collections import deque
from math import inf

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        ''' Time Complexity: O(nlogn) '''
        if not A:
            return -1
            
        n = len(A)
        sortedA, index = zip(*sorted((a,i) for i,a in enumerate(A)))
        ## no.1
        #  index_max = list(accumulate(index[::-1], max))[::-1] # index max from i to n
        ## no.2
        #  index_max = deque() # index max from i to n
        #  for i in index[::-1]:
        #  this = index_max[0] if index_max else -inf
        #  index_max.appendleft(max(i, this))
        ## no.3
        index_max = [index[-1]] * n # index max from i to n 
        for i in range(n-2,-1,-1):
            index_max[i] = max(index[i], index_max[i+1])

        res = 0
        for i,j in zip(index, index_max):
            res = max(res, j-i)
        return res
        

    def naiveMaximumGap(self, A):
        ''' Time Complexity: O(n*n) '''
        if not A:
            return -1
        n = len(A)
        i = 0
        res = 0
        for i in range(n):
            j = i + 1 + res
            while j < n:
                if A[i] <= A[j]:
                    res = max(res, j-i)
                j += 1
        return res
        

if __name__ == "__main__":

    import unittest

    class SolutionTest(unittest.TestCase):
        def test_basics(self):
            sol = Solution()
            self.assertEqual(sol.maximumGap([]), -1)
            self.assertEqual(sol.maximumGap([1]), 0)
            self.assertEqual(sol.maximumGap([1,2,3,4]), 3)
            self.assertEqual(sol.maximumGap([3,5,4,2]), 2)
            self.assertEqual(sol.maximumGap([4,3,2,1]), 0)

        def test_naive_basics(self):
            sol = Solution()
            self.assertEqual(sol.naiveMaximumGap([]), -1)
            self.assertEqual(sol.naiveMaximumGap([1]), 0)
            self.assertEqual(sol.naiveMaximumGap([1,2,3,4]), 3)
            self.assertEqual(sol.naiveMaximumGap([3,5,4,2]), 2)
            self.assertEqual(sol.naiveMaximumGap([4,3,2,1]), 0)

    unittest.main()
