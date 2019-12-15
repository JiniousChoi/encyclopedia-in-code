#!/usr/bin/python3
## author: jinchoiseoul@gmail.com
## brief: Given a string s, partition s such that
## every substring of the partition is a palindrome.
## Return the minimum cuts needed for a palindrome partitioning of s.
## Example : Given s = "aab",
## Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.


from math import inf


class Solution:
    # @param A : string
    # @return an integer
    def minCut(self, A):
        n = len(A)
        self.A = A
        #memo for _minCut0
        self.memo = [[None for _ in range(n)] for _ in range(n)]
        #memo for _is_palindrome
        self.memo2 = [[None for _ in range(n)] for _ in range(n)]

        #Optional: You can comment this out
        self.iterative_setup(n)
        
        return self._minCut0(0, len(A)-1)
            
    def iterative_setup(self, n):
        for chunk in range(2, n):
            for i in range(n-chunk):
                j = i + chunk - 1
                self._is_palindrome(i, j)
                self._minCut0(i, j)

    def _is_palindrome(self, i, j):
        if i >= j:
            return True
        elif self.memo2[i][j] != None:
            return self.memo2[i][j]
        A = self.A
        if self._is_palindrome(i+1, j-1):
            ans = A[i] == A[j]
        else:
            ans = False
        self.memo2[i][j]=ans
        return ans
    
    def _minCut0(self, i, j):
        A = self.A
        if i>=j: return 0
        assert i<j
        if self._is_palindrome(i, j):
            return 0
        
        if self.memo[i][j] != None:
            return self.memo[i][j]
        res = inf
        for x in range(i, j):
            this = 1 + self._minCut0(i, x) + self._minCut0(x+1, j)
            res = min(res, this)
            
        self.memo[i][j] = res
        return res


import unittest


class SolutionTest(unittest.TestCase):
    def test_basics(self):
        sol = Solution()
        self.assertEqual(sol.minCut(""), 0)
        self.assertEqual(sol.minCut("aaa"), 0)
        self.assertEqual(sol.minCut("aab"), 1)
        self.assertEqual(sol.minCut("abc"), 2)
        self.assertEqual(sol.minCut("abcba"), 0)
        self.assertEqual(sol.minCut("abcbabb"), 1)
        self.assertEqual(sol.minCut("abcbabc"), 2)


if __name__ == "__main__":

    unittest.main()
