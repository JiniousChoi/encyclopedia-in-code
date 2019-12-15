#!/usr/bin/python3
## author: jinchoiseoul@gmail.com


class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):
        l = bin_search_leftward(A, B)
        r = bin_search_rightward(A, B)
        return (l, r)

    def searchRange2(self, A, B):
        from bisect import bisect_left, bisect_right
        l, r = bisect_left(A, B), bisect_right(A, B)
        if l==r:
            return (-1,-1)
        else:
            return l, r-1
        

def bin_search_leftward(arr, x):
    i, j = 0, len(arr)-1
    res = -1
    while i <= j:
        mid = i+j>>1
        if arr[mid] == x:
            res = mid
            j = mid - 1
        elif arr[mid] > x:
            j = mid - 1
        else:
            i = mid + 1
    return res


def bin_search_rightward(arr, x):
    i, j = 0, len(arr)-1
    res = -1
    while i <= j:
        mid = i+j>>1
        if arr[mid] == x:
            res = mid
            i = mid + 1
        elif arr[mid] > x:
            j = mid - 1
        else:
            i = mid + 1
    return res


if __name__ == "__main__":

    import unittest

    class SolutionTest(unittest.TestCase):
        def test_basics(self):
            sol = Solution()
            methods_on_test = [sol.searchRange, sol.searchRange2]
            for search_range in methods_on_test:
                self.assertEqual(search_range([5, 7, 7, 8, 8, 10], 1), (-1,-1))
                self.assertEqual(search_range([5, 7, 7, 8, 8, 10], 5), (0,0))
                self.assertEqual(search_range([5, 7, 7, 8, 8, 10], 7), (1,2))
                self.assertEqual(search_range([5, 7, 7, 8, 8, 10], 8), (3,4))
                self.assertEqual(search_range([5, 7, 7, 8, 8, 10], 9), (-1,-1))
                self.assertEqual(search_range([5, 7, 7, 8, 8, 10], 10), (5,5))
            self.assertEqual(search_range([5, 7, 7, 8, 8, 10], 99), (-1,-1))

    unittest.main()
