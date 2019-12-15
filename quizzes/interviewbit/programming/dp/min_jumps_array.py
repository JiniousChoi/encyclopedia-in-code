#!/usr/bin/python3
## author: jinchoiseoul@gmail.com
## brief: Given an array of non-negative integers,
## you are initially positioned at the first index of the array.
## Each element in the array represents your maximum jump length at that position.
## Your goal is to reach the last index in the minimum number of jumps.
## Example : Given array A = [2,3,1,1,4]
## The minimum number of jumps to reach the last index is 2.
## (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
## If it is not possible to reach the end index, return -1.
## Note: I can't tell which one is better btw GreedySolution vs DPSolution
## It must depend on the values of elements of given array `A`


from collections import deque
from itertools import chain


class GreedySolution:
    # Time Complexity: O(len(A) + sum(A))
    # @param A : list of integers
    # @return an integer
    def jump(self, A):
        n = len(A)
        here, target = 0, n-1
        jumps = 0
        while here < target:
            here_jump = A[here]
            theres = [here+dx for dx in range(1, here_jump+1) if here+dx < n]
            if theres == []:
                return -1
            if here+here_jump >= target:
                here = target
                jumps += 1
            else:
                new_here = max([(there+A[there], there) for there in theres])[1]
                here = new_here
                jumps += 1
                
        #assert here == target
        return jumps

        
class DPSolution:
    # Time Complexity: O(len(A) * max(A))
    # @param A : list of integers
    # @return an integer
    def jump(self, A):
        n = len(A)
        start, stop = 0, n-1
        #minjumps[i] := minimum jumps to reach ith position from starting point
        #minjumps[k] == -1 means it's not reachable from the starting point
        minjumps = [-1 for _ in range(n)]
        minjumps[start] = 0
        to_visit = deque([start])
        
        while to_visit:
            here = to_visit.popleft()
            if here == stop:
                return minjumps[here]
            for there in self.possible_theres(here, A[here], minjumps):
                if minjumps[there] >= 0:
                    continue
                assert minjumps[there] == -1
                minjumps[there] = 1 + minjumps[here]
                to_visit.append(there)

        return -1
       
    def possible_theres(self, here, maxjump, minjumps):
        n = len(minjumps)
        for dx in chain(range(-maxjump,0), range(1,maxjump+1)):
            there = here + dx
            if 0 <= there < n:
                yield there


import unittest


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.solutions = [GreedySolution(), DPSolution()]

    def test_basics(self):
        for sol in self.solutions:
            self.assertEqual(sol.jump([2,2,1,0,4]), -1)
            self.assertEqual(sol.jump([2,3,1,1,4]), 2)


if __name__ == "__main__":

    unittest.main()
