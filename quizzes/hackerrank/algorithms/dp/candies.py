#!/usr/bin/python3
## author: jinchoiseoul@gmail.com
## brief: Give candies to children in a line. All children will get at least 1 candy.
## If two children sit next to each other, then the one with the higher rating must get more candies.
## Minimize the total number of candies given to the children.


from math import inf
import sys
sys.setrecursionlimit(200000)


def solution_naive(n, arr):
    arr = [inf] + arr + [inf]
    candy = [0] + [None] * n + [0]
    for i in range(len(candy)):
        alloc_candy(candy, arr, i)
    return sum(candy)


def solution_with_index_table(n, arr):
    ''' build index table of arr regarding in acending order of arr elements
        to minimize the depth of recursive call - alloc_candy '''
    arr = [inf] + arr + [inf]
    candy = [0] + [None] * n + [0]
    arr_tuple = sorted((a,i) for i,a in enumerate(arr[1:-1], 1))
    for a,i in arr_tuple:
        alloc_candy(candy, arr, i)
    return sum(candy)


def alloc_candy(candy, arr, i):
    if candy[i] != None:
        return
    if arr[i-1] >= arr[i] and arr[i] <= arr[i+1]:
        candy[i] = 1
        return
    elif arr[i-1] < arr[i] and arr[i] <= arr[i+1]:
        alloc_candy(candy, arr, i-1)
        candy[i] = candy[i-1] + 1
    elif arr[i-1] >= arr[i] and arr[i] > arr[i+1]:
        alloc_candy(candy, arr, i+1)
        candy[i] = candy[i+1] + 1
    else:
        alloc_candy(candy, arr, i-1)
        alloc_candy(candy, arr, i+1)
        candy[i] = max(candy[i-1], candy[i+1]) + 1
        

def main():
    n = int(input().strip())
    arr = []
    arr_i = 0
    for arr_i in range(n):
       arr_t = int(input().strip())
       arr.append(arr_t)
    result = candies(n, arr)
    print(result)


#main()


import unittest


class SolutionTest(unittest.TestCase):
    def test_basics(self):
        arr = [2, 4, 2, 6, 1, 7, 8, 9, 2, 1]
        self.assertEqual(solution_naive(len(arr), arr), 19)
        self.assertEqual(solution_with_index_table(len(arr), arr), 19)


if __name__ == "__main__":

    unittest.main()
