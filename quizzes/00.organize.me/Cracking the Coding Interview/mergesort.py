#!/usr/bin/env python3

import unittest

def mergesort_recur(A):
    ''' returns sorted(A) '''
    assert A != None

    if len(A)<=1:
        return A
    
    assert len(A) >= 2
    half = int(len(A)/2)
    
    first_half = mergesort_recur(A[:half])
    secon_half = mergesort_recur(A[half:])

    res = merge(first_half, secon_half)
    
    return res

def mergesort_by_stack(A):
    ''' returns sorted(A) '''
    assert A != None
    if len(A)==0:
        return A

    sorted_dic = {} #visited 겸직
    assert len(A) >= 1
    stack = [(0, len(A)-1)]
    while stack: #type: [(start,stop)]
        start, stop = stack[-1]
        assert start <= stop, "%s <= %s, %s" %(start, stop, A)

        if (start, stop) not in sorted_dic:
            if stop == start:
                sorted_dic[(start,stop)] = A[start:stop+1]
                stack.pop(-1)
                continue

        half = int((stop-start+1)/2)
        f_start, f_stop = start, start+half-1
        if (f_start, f_stop) not in sorted_dic:
            stack.append((f_start, f_stop))
            continue #recursive call

        s_start, s_stop = f_stop+1, stop
        if (s_start, s_stop) not in sorted_dic:
            stack.append((s_start, s_stop))
            continue #recursive call
        
        #merge
        f_half = sorted_dic[(f_start, f_stop)]
        s_half = sorted_dic[(s_start, s_stop)]
        sorted_dic[(start, stop)] = merge(f_half, s_half)

        stack.pop(-1) #return

    return sorted_dic[(0, len(A)-1)]

def mergesort_by_queue(A):
    ''' return sorted(A) '''
    
    assert A != None
    if len(A)<=1:
        return A

    q = [[i] for i in A]

    while len(q)>=2: #type [[int]]
        i,j = q.pop(0), q.pop(0)
        k = merge(i, j)
        q.append(k)

    assert len(q)==1
    return q

def merge(i, j):
    ''' type i: [int]
        type j: [int] 
        returns merged [int]'''
    res = []
    while len(i)>0 and len(j)>0:
        if i[0] < j[0]:
            res.append(i.pop(0))
        else:
            res.append(j.pop(0))
    if len(i) > 0:
        res.extend(i)
    elif len(j) > 0:
        res.extend(j)

    return res

class MergesortTest(unittest.TestCase):
    def setUp(self):
        self.mergesort_fns = [mergesort_recur, mergesort_by_queue, mergesort_by_stack]

    def test_method1(self):
        for mergesort_fn in self.mergesort_fns:
            for unsorted in ([], [1], [1,2], [2,1], [1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,2,1],[2,4,3,1]):
                self.assertSorted(mergesort_fn(unsorted))

    def test_random(self):
        test_size = 100
        for _ in range(test_size):
            unsorted = self.make_random_ints()
            for msort_fn in self.mergesort_fns:
                self.assertSorted(msort_fn(unsorted[:]))

    def assertSorted(self, A):
        for i,j in zip(A, A[1:]):
            self.assertTrue(i<=j)

    def make_random_ints(self):
        from random import randint
        size = randint(0, 100)
        maxi = randint(0, 10)
        res = []
        for _ in range(size):
            res.append(randint(0, maxi))

        return res

if __name__=="__main__":
    unittest.main()
