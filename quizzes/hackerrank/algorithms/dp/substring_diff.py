#!/usr/bin/python3
## author: jinchoiseoul@gmail.com
## brief: Given two strings of length n, P = p1 p2 ... pn and Q = q1 q2 ... qn,
## we define M(i,j,k) as the number of mismatches btw p and q
## i.e. M(i,j,k) = len( [0 <= x < k | p[i+x] != q[j+x] ] )
## Task is to find the maximum L, such that there exists a pair of indices (i,j)
## for which we have M(i,j,L) <= S.
## Of course, we should also have i+L-1 <= n and j+L-1 <= n


from collections import deque


def substring_diff(S, P, Q):
    p_len = len(P)
    assert 0 <= S <= p_len
    
    p_len = len(P)
    ans = 0
    
    for j in range(p_len):
        ans = max(ans, diagonal_max_length(S, P, Q, 0, j))
    
    for i in range(1, p_len):
        ans = max(ans, diagonal_max_length(S, P, Q, i, 0))
    
    return ans


def diagonal_max_length(S, P, Q, i, j):
    p_len = len(P)
    ans = 0
    left = -1
    mismatches = deque() #offset for mismatches
    for right in range(p_len - max(i, j)):
        ni, nj = i+right, j+right
        if P[ni]==Q[nj]:
            pass
        elif S > 0:
            S -= 1
            mismatches.append(right)
        else:
            left = mismatches.popleft() if mismatches else right
            mismatches.append(right)

        length = right - left
        ans = max(ans, length)

    return ans


def main():
    t = int(input())
    for _ in range(t):
        _S, P, Q = input().split()
        S = int(_S)
        L = substring_diff(S, P, Q)
        print(L)


#main()


import unittest


class SolutionTest(unittest.TestCase):
    def test_basics(self):
        for S,P,Q,ANS in [(2,'tabriz','torino',4), \
                          (0,'abacba','abcaba',3), \
                          (3,'helloworld','yellowmarin',8)]:
            self.assertEqual(substring_diff(S, P, Q), ANS)


if __name__ == "__main__":

    unittest.main()
