#!/usr/bin/python3
## author: jinchoiseoul@gmail.com
## breaf: Maximize the following cost function:
## S = Sigma (i <- 2..n) abs(A[i] - A[i-1]) 
## where A[i] <- 1..B[i]


import sys
sys.setrecursionlimit(1000000)


def max_cost_wrapper(n, B):
    ''' Design pseudo iterative dp out of recursive dp
        max-2-depth recursive calls is as efficient as iterative calls '''
    if n==1: return 0
    assert n >= 2
    memo = {}
    for i in range(n-1, -1, -1):
        max_cost(memo, n, B, i, False)
        max_cost(memo, n, B, i, True)
        
    return max(memo[(False, 0)], memo[(True, 0)])
    

def max_cost(memo, n, B, i, lo):
    ''' @param memo
        @param n
        @param B
        @param i: 
        @param lo: select whether 1 or B[i] for A[i].
        @return max cost '''
    if n-1 <= i:
        return 0
    if (lo,i) in memo:
        return memo[(lo,i)]

    if lo:
        memo[(lo,i)] = max(abs(1-1) + max_cost(memo, n, B, i+1, True),
                           abs(1-B[i+1]) + max_cost(memo, n, B, i+1, False))
    else:
        memo[(lo,i)] =  max(abs(B[i]-1) + max_cost(memo, n, B, i+1, True),
                            abs(B[i]-B[i+1]) + max_cost(memo, n, B, i+1, False))
    return memo[(lo,i)]


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        B = list(map(int, input().split()))
        print(max_cost_wrapper(n, B))

#main()


import unittest


class SolutionTest(unittest.TestCase):
    def test_basics(self):
        self.assertEqual(max_cost_wrapper(5, [10,1,10,1,10]), 36)


if __name__ == "__main__":

    unittest.main()
