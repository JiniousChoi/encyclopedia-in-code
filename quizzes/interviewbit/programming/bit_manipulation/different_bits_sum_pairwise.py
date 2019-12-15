#!/usr/bin/python3
## author: jinchoiseoul@gmail.com


MOD = 1000000007


class Solution_Efficient:
    # @param A : list of integers
    # @return an integer
    # Time Complexity : O(len(A))
    def cntBits(self, A):
        def count_bits(ones_map, a):
            i = 0
            while a > 0:
                ones_map.setdefault(i, 0)
                if a & 1 == 1:
                    ones_map[i] += 1
                i += 1
                a >>= 1
            return ones_map

        def whole_cnt(n, ones_map):
            res = 0
            for ones in ones_map.values():
                zeroes = n - ones
                res += 2 * ones * zeroes
                res %= MOD
            return res

        n = len(A)
        ones_map = {}
        for a in A:
            count_bits(ones_map, a)
        return whole_cnt(len(A), ones_map)
        


class Solution_Naive:
    # Time Complexity: O( len(A) * len(A) )
    # @param A : list of integers
    # @return an integer
    def cntBits(self, A):
        def count_bits(a, b):
            xor = a ^ b
            cnt = 0
            while xor > 0:
                cnt += 1
                xor &= xor - 1
            return cnt

        whole_cnt = 0
        n = len(A)
        for i in range(n):
            for j in range(i+1, n):
                whole_cnt += 2*count_bits(A[i], A[j])
                whole_cnt %= MOD
        return whole_cnt


import unittest


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.sols = [Solution_Efficient(), Solution_Naive()]

    def test_basics(self):
        for sol in self.sols:
            A = [1, 3, 5]
            self.assertEqual(sol.cntBits(A), 8)


if __name__ == "__main__":

    unittest.main()
