#!/usr/bin/python3
## author: jinchoiseoul@gmail.com
## brief: Find a starting gas station for a trip around the circle with enough gas
## If there is no such a gas station, return -1


class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return an integer
    def canCompleteCircuit(self, A, B):
        n = len(A)
        start = 0
        while start < n:
            success, new_start = self.reachable_from(A, B, start)
            if success:
                return start
            start = new_start
                
        return -1
        
    def reachable_from(self, A, B, start):
        ''' @return (success::bool, new_start::int) '''
        i,t = start, 0
        n = len(A)
        tank = 0
        while t < n:
            gas, cost = A[i%n], B[i%n]
            tank += gas - cost
            if tank < 0: break
            i, t = i+1, t+1
        if t >= n:
            return (True, n)
        else:
            return (False, i+1)
        

import unittest


class SolutionTest(unittest.TestCase):
    def test_basics(self):
        sol = Solution()
        self.assertEqual(sol.canCompleteCircuit([1,2], [2,1]), 1)
        self.assertEqual(sol.canCompleteCircuit([1,2], [99,99]), -1)


if __name__ == "__main__":

    unittest.main()
