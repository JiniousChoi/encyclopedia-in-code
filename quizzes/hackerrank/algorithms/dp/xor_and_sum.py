#!/usr/bin/python3
## author: jinchoiseoul@gmail.com


MOD = 1000000007


def solution(a, b):
    a = int(a, base=2)
    b = int(b, base=2)
    return xor_and_sum(a, b)


def xor_and_sum(a, b):
    s = 0
    for i in range(314159+1):
        s += a ^ (b<<i)
    return s % MOD
    

def main():
    a, b = input(), input()
    print(solution(a, b))
    

#main()


import unittest


class SolutionTest(unittest.TestCase):
    def test_basics(self):
        a, b = '10', '1010'
        self.assertEqual(solution(a, b), 489429555)


if __name__ == "__main__":

    unittest.main()
