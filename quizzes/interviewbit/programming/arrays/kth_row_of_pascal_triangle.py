#!/usr/bin/python3
## author: jinchoiseoul@gmail.com
## brief: Given an index k, return the kth row of the Pascal’s triangle.


class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        K = 0
        arr = [1]
        
        while K < A:
            res = [1]
            for x,y in zip(arr, arr[1:]):
                res.append(x+y)
            res.append(1)
            arr = res
            K += 1
        assert K==A
        return arr


import unittest


class SolutionTest(unittest.TestCase):
    
    def test_basics(self):
        sol = Solution()
        self.assertEqual(sol.getRow(0), [1])
        self.assertEqual(sol.getRow(1), [1,1])
        self.assertEqual(sol.getRow(2), [1,2,1])
        self.assertEqual(sol.getRow(3), [1,3,3,1])
        self.assertEqual(sol.getRow(4), [1,4,6,4,1])
        self.assertEqual(sol.getRow(5), [1,5,10,10,5,1])


if __name__ == "__main__":

    unittest.main()
