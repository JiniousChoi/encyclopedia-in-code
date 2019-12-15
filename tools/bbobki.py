#!/usr/bin/python3
'''
뽑기를 하는 유틸성 프로그램
예를 들어 ('A','a')가 들어있는 주머니와 ('B','b')가 들어있는 주머니에서 각각 하나씩 뽑을 때
나올 수 있는 모든 경우의 수를 나열한다.
결과는 (AB, Ab, aB, ab)이다.
'''
import unittest
from operator import mul, itemgetter
from functools import reduce

DEBUG=True

def bbobki(*args):
    for idx in adder(*args):
        yield [a[i] for i,a in zip(idx, args)]

def adder(*args):
    len_ls = [len(e) for e in args]
    _check_len_list(len_ls)

    #inital condition
    counter_list = [0]*len(len_ls)
    
    while True:
        #boundary check
        if not _carriable(len_ls, counter_list):
            return

        _carry_if_necessary(len_ls, counter_list)
        yield counter_list[:]
        _add(counter_list)

def _check_len_list(ls):
    for e in ls:
        assert e>0

def _carriable(len_ls, cnt_ls):
    #e.g. (2,2,2)/(0,1,2) is carriable
    #e.g. (2,2,2)/(1,1,2) is not carriable
    max_val = reduce(mul, len_ls, 1)
    weight_ls = []
    for i in range(len(len_ls)):
        v = reduce(mul, len_ls[i+1:], 1)
        weight_ls.append(v)

    cur_val = sum([a*b for a,b in zip(weight_ls, cnt_ls)])
    return max_val > cur_val

def _carry_if_necessary(len_ls, cnt_ls):
    #assume cnt_ls is carriable
    for i in range(len(cnt_ls)):
        idx = len(cnt_ls)-1-i
        if cnt_ls[idx]==len_ls[idx]:
            cnt_ls[idx]=0
            cnt_ls[idx-1]=cnt_ls[idx-1]+1
        elif cnt_ls[idx]>len_ls[idx]:
            assert False, "out of bound error"

def _add(cnt_ls):
    cnt_ls[-1] = cnt_ls[-1] + 1

### testing part
class BbobkiTest(unittest.TestCase):
    def test_adder_basic1(self):
        S=(0.66, 1-0.66)
        K=(0.5, 0.5)
        M=(0.53, 1-0.53)
        res = list(adder(S,K,M))
        if DEBUG:
            print(res)
        self.assertEqual(len(res), 8)

    def test_adder_basic2(self):
        S=(0.66, 1-0.66)
        K=(0.5, 0.5, 0)
        M=(0.53, 1-0.53, 0, 0)
        res = list(adder(S,K,M))
        if DEBUG:
            print(res)
        self.assertEqual(len(res), 24)

    def test_carriable(self):
        len_ls = (2,2,2)
        cnt_ls = (0,1,1)
        self.assertTrue(_carriable(len_ls, cnt_ls))

        len_ls = (2,2,2)
        cnt_ls = (0,1,2)
        self.assertTrue(_carriable(len_ls, cnt_ls))

        len_ls = (2,2,2)
        cnt_ls = (0,2,1)
        self.assertTrue(_carriable(len_ls, cnt_ls))

        len_ls = (2,2,2)
        cnt_ls = (1,1,2)
        self.assertFalse(_carriable(len_ls, cnt_ls))

        len_ls = (2,2,2)
        cnt_ls = (2,1,1)
        self.assertFalse(_carriable(len_ls, cnt_ls))

    def test_carry_if_necessary(self):
        len_ls = [2,2,2]
        cnt_ls = [0,0,2]
        _carry_if_necessary(len_ls, cnt_ls)
        self.assertEqual(cnt_ls, [0,1,0], "carry didn't operate")

        len_ls = [2,2,2]
        cnt_ls = [0,1,2]
        _carry_if_necessary(len_ls, cnt_ls)
        self.assertEqual(cnt_ls, [1,0,0], "carry didn't operate")

    def test_add(self):
        cnt_ls = [1,2,3]
        _add(cnt_ls)
        self.assertEqual(cnt_ls, [1,2,4], "_add didn't operate well")

    def test_bbobki_basic1(self):
        S=('A','a')
        K=('B','b')
        M=('C','c')
        res = list(bbobki(S,K,M))
        if DEBUG:
            print(res)
        self.assertEqual(res, [['A','B','C'], ['A','B','c'], ['A','b','C'], ['A','b','c'], ['a','B','C'], ['a','B','c'], ['a','b','C'], ['a','b','c']])
        
    def test_bbobki_basic1(self):
        S=(0.66, 1-0.66)
        K=(0.5, 0.5)
        M=(0.53, 1-0.53)
        res = list(bbobki(S,K,M))
        if DEBUG:
            print(res)
        

if __name__=="__main__":
    unittest.main()

