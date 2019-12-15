#!/usr/bin/python3
## author: jinchoiseoul@gmail.com
## reference: https://www.youtube.com/watch?v=XKu_SEDAykw
## brief: Given a sorted collection of numbers and a target_sum,
## determine if a pair of numbers exists that adds up to `target_sum`
## Note 1: You cannot pick an element twice
## Note 2: Time Complexity should be O(n)


def pair_sum_in_sorted_arr(arr, target_sum):
    ''' Time Complexity: O(n)
        Space Complexity: O(1)
        @param arr: an sorted array of numbers
        @param target_sum
        @return True if a pair for target_sum exists '''

    l,r = 0, len(arr)-1
    while l<r:
        this_sum = arr[l] + arr[r]
        if this_sum == target_sum:
            return True
        elif this_sum > target_sum:
            r -= 1
        else:
            l += 1

    assert l>=r
    return False


## What if the given array is not sorted?


def pair_sum_in_unsorted_arr(arr, target_sum):
    ''' Time Complexity: O(n)
        Space Complexity: O(n)
        @param arr: an unsorted array of numbers
        @param target_sum
        @return True if a pair for target_sum exists '''

    n = len(arr)
    lookup = set()
    for a in arr:
        b = target_sum - a 
        if b in lookup:
            return True
        lookup.add(a)
    return False 


import unittest


class SolutionTest(unittest.TestCase):

    def test_pair_sum_in_sorted_arr(self):
        self.assertFalse(pair_sum_in_sorted_arr([1,2,3,9], 8))
        self.assertFalse(pair_sum_in_sorted_arr([4], 7))
        self.assertFalse(pair_sum_in_sorted_arr([4], 8))

        self.assertTrue(pair_sum_in_sorted_arr([4,4], 8))
        self.assertTrue(pair_sum_in_sorted_arr([-1,2,3,9], 8))

    def test_pair_sum_in_unsorted_arr(self):
        self.assertFalse(pair_sum_in_unsorted_arr([2,3,1,9], 8))
        self.assertFalse(pair_sum_in_unsorted_arr([4], 7))
        self.assertFalse(pair_sum_in_unsorted_arr([4], 8))

        self.assertTrue(pair_sum_in_unsorted_arr([4,4], 8))
        self.assertTrue(pair_sum_in_unsorted_arr([-1,2,9,3], 8))


if __name__ == "__main__":

    unittest.main()
