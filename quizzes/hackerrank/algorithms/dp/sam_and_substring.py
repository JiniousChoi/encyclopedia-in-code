#!/usr/bin/python3
## author: jinchoiseoul@gmail.com
## brief: Given a string of length n.
## first charactor is numbered from 1 to 9
## the rest are numbered from 0 to 9
## Add stings in the following manner till it becomes one string
## e.g. ['1','2','3'] -> ['3','5'] -> ['8']


MOD = 1000000007


def sam(n):
    nlen = len(n)
    X = int(n[0])
    ans = X
    for i in range(1, nlen):
        X = (10*X % MOD) + int(n[i])*(i+1)
        ans += X
        ans %= MOD
    return ans
    

def main():
    n = input().strip()
    print(sam(n))
    

#main()


import unittest


class SolutionTest(unittest.TestCase):
    def test_basics(self):
        self.assertEqual(sam('16'), 23)
        self.assertEqual(sam('123'), 164)


if __name__ == "__main__":

    unittest.main()
