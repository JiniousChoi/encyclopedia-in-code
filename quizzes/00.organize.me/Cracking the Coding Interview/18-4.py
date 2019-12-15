#!/usr/bin/env python3
''' 0부터 n까지 수를 나열했을 때, 2가 몇번이나 등장하는지세는 메서드를 작성하라'''

import unittest

def count_2s_naive(n):
    ''' naive '''
    assert 0<n
    cnt = 0
    for i in range(1, n+1):
        cnt += str(i).count('2')
        #invariant: i까지 2의 개수를 모두 셈.

    return cnt

def count_2s_efficient(n):
    ''' efficient '''
    assert n>0
    cnt = 0
    for d in range(len(str(n))):
        i, rest = divmod(n % (10**(d+1)), 10**d)
        if i==1:
            cnt += d * (10**(d-1))
        elif i==2:
            cnt += 2*d*(10**(d-1)) + 1 + rest
        elif i>2:
            cnt += i*count_2s_efficient(10**d) + 10**d
    return cnt

def decimal_lshift(num, shift):
    if shift>0:
        return num * (10**shift)
    elif shift<0:
        return int(num // (10**-shift))
    else:
        return num

class Count2sTest(unittest.TestCase):
    def test_samples(self):
        self.count2s(1, 0)
        self.count2s(2, 1)
        self.count2s(10, 1)
        self.count2s(25, 9)
        self.count2s(26, 10)
        self.count2s(30, 13)
        self.count2s(100, 20)
        self.count2s(200, 41)
        self.count2s(300, 160)
        self.count2s(1000, 300)
        self.count2s(10000, 4000)
        self.count2s(100000, 50000)

    def count2s(self, n, twos_cnt):
        res = count_2s_naive(n)
        self.assertEqual(res, twos_cnt)

        res2 = count_2s_efficient(n)
        self.assertEqual(res2, twos_cnt)

    def test_randoms(self):
        from random import randint
        for i in range(100):
            ran_num = randint(2,9999)
            naive = count_2s_naive(ran_num)
            efficient = count_2s_efficient(ran_num)
            self.assertEqual(naive, efficient)

if __name__=="__main__":
    unittest.main()
