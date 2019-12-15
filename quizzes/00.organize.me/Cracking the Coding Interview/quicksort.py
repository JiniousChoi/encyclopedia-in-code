#!/usr/bin/env python3

import unittest
from random import randint, shuffle

def quicksort(A, start=None, stop=None):
    if start==None: start = 0
    if stop==None: stop = len(A) - 1

    if stop - start <= 0:
        return

    if stop - start == 1:
        if A[start] > A[stop]:
            swap(A, start, stop)
        return
    
    #assert stop - start >= 2 

    j = sort_kth(A, start, stop)

    quicksort(A, start, j-1)
    quicksort(A, j+1, stop)

def quicksort_by_stack(A):
    start, stop = 0, len(A)-1
    stack = [(start, stop, None)]
    visited = set()
    
    while stack:
        #pi is sorted_kth_idx
        start, stop, pi = stack[-1]

        if (start, stop) not in visited:
            visited.add((start, stop))

            if stop - start <= 0:
                stack.pop(-1)
                continue #return 
            elif stop - start == 1:
                if A[start] > A[stop]:
                    swap(A, start, stop)
                stack.pop(-1)
                continue #return
            else:
                pi = sort_kth(A, start, stop)
                stack[-1] = (start, stop, pi)

        if (start, pi-1) not in visited:
            stack.append((start, pi-1, None))
            continue #DFS
        
        if (pi+1, stop) not in visited:
            stack.append((pi+1, stop, None))
            continue #DFS
        
        stack.pop(-1) #return
        
def quicksort_by_queue(A):
    start, stop = 0, len(A)-1
    q = [(start, stop)]

    while q:
        start, stop = q.pop(0)
        if start>=stop:
            continue
        if stop-start==1:
            if A[start] > A[stop]:
                swap(A, start, stop)
            continue
        #assert stop-start >= 2
        pi = sort_kth(A, start, stop)
        q.append((start, pi-1))
        q.append((pi+1, stop))

def sort_kth(A, start, stop, pi=None):
    ''' '''
    if pi==None:
        pi = randint(start, stop)
    pivot = A[pi]
    swap(A, pi, start)
    del pi
    i,j = start+1, stop

    #i<j로도 가능하지만 모두 i<=j로 통일하는게 더 편리해보임.
    while i<=j:
        #invariant: i 미만은 pivot보다 작거나 같다.
        #invariant: j 초과는 pivot보다 크다.
        while i<=j and A[i]<=pivot:
            i += 1
        while i<=j and pivot<A[j]:
            j -= 1
        if i<=j:
            swap(A, i, j)

    assert start <= j <= stop

    assert i > j
    assert i-1 == j
    #invariant: i > j 이므로, A[j](또는 A[i-1]) 와 피컷을 교환하면 kth가 소팅된 결과.
    swap(A, start, j)

    #assert j is sorted
    return j

def swap(A, i, j):
    A[i], A[j] = A[j], A[i]

class XTest(unittest.TestCase):
    def setUp(self):
        self.qsort_fns = [quicksort, quicksort_by_stack, quicksort_by_queue]

    def test_samples(self):
        self.assertQsortWorks([2])
        self.assertQsortWorks([2,1])
        self.assertQsortWorks([1,2])
        self.assertQsortWorks([2,1,3])
        self.assertQsortWorks([2,3,1])
        self.assertQsortWorks([1,2,3,4])
        self.assertQsortWorks([5,4,3,2,1])
        self.assertQsortWorks([3,4,1,5,2])

    def test_random(self):
        size = 100
        a = [randint(0,10) for _ in range(size)]
        self.assertQsortWorks(a)

    def assertQsortWorks(self, unsorted):
        for qsort in self.qsort_fns:
            a = unsorted[:]
            qsort(a)
            self.assertSorted(a)

    def assertSorted(self, A):
        #from math import inf
        #last = -inf
        #for i in A:
        #    assert last <= i
        #    last = i
        for i,j in zip(A, A[1:]):
            assert i<=j, "%s<=%s" %(i,j)

    def test_sort_kth(self):
        a = [2,1,3]
        j = sort_kth(a, 0, 2, pi=0)
        self.assertEqual(j, 1)
        self.assertEqual(a, [1,2,3])
            

if __name__=="__main__":
    unittest.main()
