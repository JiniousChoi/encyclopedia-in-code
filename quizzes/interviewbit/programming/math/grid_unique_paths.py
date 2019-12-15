#!/usr/bin/python3
## author: jinchoiseoul@gmail.com
## brief : Find total number of possible ways to reach from top-left corner
## to the bottom-right corner in a 2-d grid.


#code starts here


import unittest


class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):
        memo = [[None for _ in range(B)] for _ in range(A)]
        for r in range(A):
            memo[r][0] = 1
        for c in range(B):
            memo[0][c] = 1
        
        return uniquePaths0(memo, A-1, B-1)
        
def uniquePaths0(memo, r, c):
    if memo[r][c] != None:
        return memo[r][c]
    memo[r][c] = uniquePaths0(memo, r, c-1) + uniquePaths0(memo, r-1, c)
    return memo[r][c]


class SolutionTest(unittest.TestCase):
    def test_basics(self):
        sol = Solution()
        self.assertEqual(sol.uniquePaths(2, 2), 2)
        self.assertEqual(sol.uniquePaths(4, 4), 20)
        self.assertEqual(sol.uniquePaths(4, 5), 35)


if __name__ == "__main__":

    unittest.main()
