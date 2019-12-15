#!/usr/bin/python3
## author: jinchoiseoul@gmail.com
## brief: Given an array of n elements, find the maximum possible sum among
## 1. all nonempty subarrays.
## 2. all nonempty subsequences.
## We define a subarray as a contiguous subsequence.
## Note that empty subarrays/subsequences should not be considered. 


from math import inf


def find_maxs(n, arr):
    return max_subarray2(n, arr), max_subsequnce(n, arr)


def max_subarray1(n, arr):
    ''' recursive-dp approach - rightwards '''
    def _max_subarray1(n, arr, i, memo):
        if i == n: return 0
        if i in memo: return memo[i]
        memo[i] = max(arr[i], arr[i] + _max_subarray1(n, arr, i+1, memo))
        return memo[i]
    memo = {}
    _max_subarray1(n, arr, 0, memo)
    return max(memo[i] for i in range(n))


def max_subarray2(n, arr):
    ''' iterative-dp approach - rightwards '''
    maxi = -inf
    a_part = 0
    for a in arr[::-1]:
        a_part = max(a, a + a_part)
        maxi = max(maxi, a_part)
            
    return maxi


def max_subarray3(n, arr):
    ''' recursive-dp approach - leftwards '''
    def _max_subarray3(arr, i, memo):
        if i < 0: return 0
        if i in memo: return memo[i]
        memo[i] = max(arr[i], _max_subarray3(arr, i-1, memo) + arr[i])
        return memo[i]
    memo = {}
    _max_subarray3(arr, n-1, memo)
    return max(memo[i] for i in range(n))


def max_subarray4(n, arr):
    ''' iterative-dp approach - leftwards '''
    maxi = -inf
    a_part = 0
    for a in arr:
        a_part = max(a, a_part + a)
        maxi = max(maxi, a_part)
            
    return maxi


def max_subsequnce(n, arr):
    non_negatives = [a for a in arr if a >= 0]
    if non_negatives:
        return sum(non_negatives)
    return max(arr)
    

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(*find_maxs(n, arr))
        

#main()


import unittest


class SolutionTest(unittest.TestCase):

    def test_maxs(self):
        self.assertEqual(find_maxs(4, [1,2,3,4]), (10,10))
        self.assertEqual(find_maxs(6, [2,-1,2,3,4,-9]), (10,11))

    def test_max_subarrays(self):
        for max_subarray in [max_subarray1, max_subarray2, max_subarray3, max_subarray4]:
            self.assertEqual(max_subarray(4, [1,2,3,4]), 10)


if __name__ == "__main__":

    unittest.main()
