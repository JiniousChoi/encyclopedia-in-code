#!/usr/bin/env python3

import unittest
from heap import MinHeap, MaxHeap
from treap import Treap

class HeapMedian:
    ''' solution using min-, max- heaps '''
    def __init__(self):
        self.upper = MinHeap()
        self.lower = MaxHeap()

    def add(self, i):
        assert self.lower.size() >= self.upper.size()

        if self.lower.size()==0 or\
                i <= self.lower.peek():
            self.lower.push(i)
        else:
            self.upper.push(i)

        if self.lower.size() < self.upper.size():
            self.lower.push(self.upper.pop())
        elif self.lower.size() > self.upper.size()+1:
            self.upper.push(self.lower.pop())

    def get(self):
        return self.lower.peek()

class TreapMedian:
    def __init__(self):
        self.treap = None
    
    def add(self, i):
        t = self.treap
        if t:
            from random import randint
            p = randint(0,100)
            self.treap = t.add(Treap, Treap(p,i))
        else:
            self.treap = Treap.make_treap(Treap, [i])

    def get(self):
        t = self.treap
        assert t
        sz = t.size()
        assert sz>0

        from math import floor
        i_mid = floor((sz-1)/2)
        return t.k_th(i_mid).val
        

#class RunningMedianTest(unittest.TestCase):
#    def test_heap_median_samples(self):
#        median = HeapMedian()
#        for i, m in zip([3,1,5,4,1], [3,1,3,3,3]):
#            median.add(i)
#            self.assertEqual(median.get(), m)
#
#    #그러고 보니, 나의 Treap구현에서는 value가 중복할 수 없는 제약을 넣었었다.
#    #이를 제거해야 할듯.
#    def test_treap_median_samples(self):
#        median = TreapMedian()
#        for i, m in zip([3,1,5,4,1], [3,1,3,3,3]):
#            median.add(i)
#            self.assertEqual(median.get(), m)

if __name__=="__main__":
    unittest.main()
