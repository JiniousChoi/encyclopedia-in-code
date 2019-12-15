#!/usr/bin/python3
## author: jinchoiseoul@gmail.com


class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def __init__(self, min_index):
        self.min_index = min_index

    def search(self, arr, target):
        n = len(arr)
        r = self.min_index(arr)
        i, j = r, r+n-1
        while i<=j:
            k = i+j>>1
            if arr[k%n] == target:
                return k%n
            elif arr[k%n] > target:
                j = k-1
            else:
                i = k+1
        return -1


def min_index_nodup_1(arr):
    ''' @param arr: unique elements 
        @return min index of the smallest value in arr
        Time Complexity O(lgn) '''
    n = len(arr)
    i, j = 0, n-1
    if arr[i] < arr[j]:
        return 0
        
    assert arr[i] > arr[j]
    while j-i > 1:
        k = i+j>>1
        if arr[i] < arr[k]: i = k
        elif arr[k] < arr[j]: j = k
    #assert j-i <= 1
    return j


def min_index_nodup_2(arr):
    ''' @param arr: unique elements 
        @return min index of the smallest value in arr
        Time Complexity O(lgn) '''
    n = len(arr)
    i, j = 0, n-1
    if arr[i] < arr[j]:
        return 0
        
    assert arr[i] > arr[j]
    while i < j:
        k = i+j>>1
        if arr[i] < arr[k]: i = k+1
        else: j = k
    return i
            

# NOTE : Think about the case when there are duplicates.
# Q: Does your current solution work? A: No
# Q: How does the time complexity change? A: Yes
def min_index_dup_1(arr, i, j):
    ''' @param arr: duplicate elements
        @return min index of the smallest value in arr
        Time Complexity Omega(lgn) ~ O(n) '''
    n = j-i+1
    assert n > 0
    if n==1: return 0
    if n==2: return 0 if arr[i] <= arr[j] else j

    if arr[i] < arr[j]:
        return 0
    elif arr[i] > arr[j]:
        while i+1 < j:
            k = i+j>>1
            if arr[i] <= arr[k]:
                i = k
            else:
                j = k
        return j
    else:
        k = i+j>>1
        res1 = min_index_dup_1(arr, i, k)
        if res1 > 0:
            return res1
        return min_index_dup_1(arr, k, j)
        

import unittest


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.sols = [Solution(min_index_nodup_1), Solution(min_index_nodup_2)]

    def test_basics(self):
        for sol in self.sols:
            arr = [194,195,196,197,198,199,201,203,204,1,
                   2,3,4,5,6,7,8,9,11,12,
                   13,14,15,16,17,18,20,21,22,23,
                   24,25,26,27,29,30,31,32,33,34,
                   35,36,37,39,40,42,43,44,45,47,
                   48,49,50,51,52,53,54,55,57,58,
                   59,60,61,63,65,66,68,69,70,71,
                   73,74,76,77,79,80,81,82,83,84,
                   86,87,88,89,91,92,93,94,95,97,
                   98,99,101,103,104,105,106,107,108,109,
                   110,113,114,115,117,118,120,121,122,123,
                   124,127,128,130,131,133,134,135,136,137,
                   139,140,141,142,143,144,146,147,148,149,
                   150,151,152,153,154,155,158,159,160,161,
                   162,163,164,166,167,169,170,171,172,174,
                   175,177,178,179,181,182,184,185,187,189,
                   190,192,193]
            
            self.assertEqual(sol.search(arr, 1), 9)


class DuplicateArrayTest(unittest.TestCase):
    def test_basics(self):
        arrays = [[1], [1,1], [1,2,3,4,5,6], [2,3,1,1], [3,3,3,3,3,3], [3,3,3,3,3,3,2,3]]
        indexes = [0, 0, 0, 2, 0, 6]
        for arr, idx in zip(arrays, indexes):
            i, j = 0, len(arr)-1
            self.assertEqual(min_index_dup_1(arr, i, j), idx)


if __name__ == "__main__":

    unittest.main()
