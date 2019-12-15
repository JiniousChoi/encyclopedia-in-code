#!/usr/bin/python3
## author: jinchoiseoul@gmail.com


import sys
sys.setrecursionlimit(100000)


MOD = 1000000007
ROW_COMBIS = [1, 1, 2, 4, 8]
TOT_COMBIS = [1, 1]
SOL_COMBIS = []
NOTSOL_COMBIS = []


def lego(n, m):
    assert 1<=n<=1000 and 1<=m<=1000
    global TOT_COMBIS, SOL_COMBIS, NOTSOL_COMBIS
    TOT_COMBIS = [1, 1]
    SOL_COMBIS = [1, 1] + [None] * (m-1)
    NOTSOL_COMBIS = [0, 0] + [None] * (m-1)
    for x in range(m+1):
        solid(n, x)
    return solid(n, m)


def solid(n, m):
    if SOL_COMBIS[m] == None:
        ans = total(n, m) - not_solid(n, m)
        ans %= MOD # in case it becomes negative
        SOL_COMBIS[m] = ans
    
    return SOL_COMBIS[m]


def total(n, m):
    while m >= len(ROW_COMBIS):
        val = sum(ROW_COMBIS[-4:]) % MOD
        ROW_COMBIS.append(val)
    
    while m >= len(TOT_COMBIS):
        l = len(TOT_COMBIS)
        val = pow(ROW_COMBIS[l], n, MOD)
        TOT_COMBIS.append(val)

    return TOT_COMBIS[m]


def not_solid(n, m):
    if NOTSOL_COMBIS[m] == None:
        parts = 0
        for i in range(1, m):
            parts += solid(n, i) * total(n, m-i)
            parts %= MOD
        NOTSOL_COMBIS[m] = parts
    return NOTSOL_COMBIS[m]
    

def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        print(lego(n, m))    


#main()


import unittest


class SolutionTest(unittest.TestCase):
    def test_basics(self):
        self.assertEqual(lego(2,2), 3)
        self.assertEqual(lego(3,2), 7)
        self.assertEqual(lego(2,3), 9)
        self.assertEqual(lego(4,4), 3375)


if __name__ == "__main__":

    unittest.main()
