#!/usr/bin/python3
## 임백준 100명 탈옥 문제
## 궁금한 점 코딩으로 확률 뽑아보기.

import unittest
from random import randint

def pick_prisoners(size, times):
    ls = [False]*size
    
    for _ in range(times):
        idx = randint(0,size-1)
        ls[idx] |= True

    return ls

def pick_prisoners_until(size):
    ls = [False]*size
    
    maximum = 1000000
    for x in range(maximum):
        idx = randint(0,size-1)
        ls[idx] |= True

        if ls.count(False) == 0:
            return x+1
    assert False, "Could not pick all prisoners within {} tries".format(maximum)
    

def true_ratio(ls):
    return ls.count(True)/len(ls)

def avg(ls):
    return sum(ls)/len(ls)

class TestPrisoners(unittest.TestCase):
    def test_one(self):
        ratio = true_ratio(pick_prisoners(100, 300))
        self.assertTrue(ratio>0.9, "Need more days")

    def test_pick_prisoners_until(self):
        rs = []
        for i in range(10000):
            days = pick_prisoners_until(100)
            rs.append(days)
        rs.sort()
        print("average days that took: ",sum(rs)/len(rs))
        print("min days that took: ",rs[0])
        print("max days that took: ",rs[-1])
        print("top 10% avg that took: ",avg(rs[-int(0.1*len(rs)):]))
        print("top 10%th that took: ",rs[-int(0.1*len(rs))])
        print("top 5%th that took: ",rs[-int(0.05*len(rs))])
        print("top 1%th that took: ",rs[-int(0.01*len(rs))])

'''
reference: https://en.wikipedia.org/wiki/Coupon_collector%27s_problem
average days that took:  516.5382
min days that took:  249
max days that took:  1694
top 10% avg that took:  784.542
top 10%th that took:  680
top 5%th that took:  753
top 1%th that took:  926
'''

if __name__ == "__main__":
    unittest.main()
