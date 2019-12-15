#!/usr/bin/env python3

import unittest
import random as rng
from math import inf

class MaxHeap:
    def __init__(self, raw=[]):
        self.minheap = MinHeap(raw)

    def pop(self):
        return -self.minheap.pop()

    def push(self, i):
        self.minheap.push(-i)

    def peek(self):
        v = self.minheap.peek()
        return -v if v else None
    
    def size(self):
        return self.minheap.size()

class MinHeap:
    def __init__(self, raw=[]):
        assert isinstance(raw, list)
        self.raw = raw

    def peek(self):
        A = self.raw
        return A[0] if A else None

    def pop(self):
        A = self.raw
        size = self.size()
        if not A:
            return None

        if size==1:
            return A.pop(0)

        #assert len(A)>1
        minimum = A[0]
        A[0] = A.pop(-1)
        self.bubble_down(0)

        return minimum

    def bubble_down(self, i):
        '''return None '''
        A = self.raw
        ilc = self.ilc(i)
        irc = self.irc(i)
        size = self.size()

        smallest = i
        if ilc < size and A[i] > A[ilc]:
            smallest = ilc
        if irc < size and A[smallest] > A[irc]:
            smallest = irc
        
        if smallest == i:
            return
        else:
            A[i], A[smallest] = A[smallest], A[i]
            self.bubble_down(smallest)

    def push(self, i):
        self.raw.append(i)
        size = self.size()
        
        ilast = size - 1
        self.bubble_up(ilast)

    def bubble_up(self, idx):
        ipar = self.ipar(idx)
        if ipar < 0:
            return
        A = self.raw
        if A[idx] < A[ipar]:
            A[idx], A[ipar] = A[ipar], A[idx]
            self.bubble_up(ipar)

    def size(self):
        return len(self.raw)

    def ilc(self, i):
        ''' index left child'''
        return 2*i + 1

    def irc(self, i):
        ''' index righ child '''
        return 2*i + 2
    
    def ipar(self, i):
        ''' index parent '''
        from math import floor
        return floor( (i-1) / 2)

class MinHeapTest(unittest.TestCase):
    def test_bubbledown(self):
        self.bubbledowned([0], [0])

        self.bubbledowned([0,1], [0,1])
        self.bubbledowned([1,0], [0,1])

        self.bubbledowned([0,1,2], [0,1,2])
        self.bubbledowned([0,2,1], [0,2,1])

        self.bubbledowned([1,0,2], [0,1,2])
        self.bubbledowned([1,2,0], [0,2,1])

        self.bubbledowned([2,0,1], [0,2,1])
        self.bubbledowned([2,1,0], [0,1,2])

    def bubbledowned(self, raw, res):
        heap = MinHeap(raw)
        heap.bubble_down(0)
        self.assertEqual(heap.raw, res)

    def test_pop(self):
        self.assertPop([], None, [])
        self.assertPop([0], 0, [])
        self.assertPop([0,1], 0, [1])
        self.assertPop([0,1,2], 0, [1,2])
        self.assertPop([0,2,1], 0, [1,2])
        self.assertPop([0,2,1,4,3,5,6], 0, [1,2,5,4,3,6])

    def assertPop(self, raw, val, new_raw):
        minheap = MinHeap(raw)
        self.assertEqual(minheap.pop(), val)
        self.assertEqual(minheap.raw, new_raw)

    def test_push(self):
        self.assertPush([], 0, [0])

        self.assertPush([0], 1, [0,1])
        self.assertPush([0], 0, [0,0])
        self.assertPush([0], -1, [-1,0])

        self.assertPush([0,2], 3, [0,2,3])
        self.assertPush([0,2], 2, [0,2,2])
        self.assertPush([0,2], 1, [0,2,1])
        self.assertPush([0,2], 0, [0,2,0])
        self.assertPush([0,2], -1, [-1,2,0])

        self.assertPush([0,4,2], 5, [0,4,2,5])
        self.assertPush([0,4,2], 4, [0,4,2,4])
        self.assertPush([0,4,2], 3, [0,3,2,4])
        self.assertPush([0,4,2], 2, [0,2,2,4])
        self.assertPush([0,4,2], 1, [0,1,2,4])
        self.assertPush([0,4,2], 0, [0,0,2,4])
        self.assertPush([0,4,2], -1, [-1,0,2,4])

    def assertPush(self, heap_before, new_val, heap_after):
        heap = MinHeap(heap_before)
        heap.push(new_val)
        self.assertEqual(heap.raw, heap_after)

    def test_random_minheap(self):
        size = 1000
        range_start, range_stop = 0, 100

        minheap = MinHeap([])
        for i in [rng.randint(range_start, range_stop) for _ in range(size)]:
            minheap.push(i)
        assert minheap.size() == size

        last = -inf
        while minheap.size()>0:
            m = minheap.pop()
            assert last <= m
            last = m

        assert minheap.size() == 0

    def test_peek(self):
        minheap = MinHeap([])
        self.assertEqual(minheap.peek(), None)

        minheap.push(8)
        self.assertEqual(minheap.peek(), 8)

        minheap.push(5)
        self.assertEqual(minheap.peek(), 5)

class MaxHeapTest(unittest.TestCase):
    def test_random_maxheap(self):
        size = 1000
        range_start, range_stop = 0, 100

        maxheap = MaxHeap([])
        for i in [rng.randint(range_start, range_stop) for _ in range(size)]:
            maxheap.push(i)
        assert maxheap.size() == size

        last = inf
        while maxheap.size()>0:
            m = maxheap.pop()
            assert last >= m
            last = m

        assert maxheap.size() == 0

if __name__=="__main__":
    unittest.main()
