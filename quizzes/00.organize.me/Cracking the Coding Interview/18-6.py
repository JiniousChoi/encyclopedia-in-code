#!/usr/bin/env python3
'''10억개의 수 가운데 100만 개의 가장 작은 수들을 추출하는 알고리즘을 설명하라.
메모리에 10억 개의 수들을 다 수용할 수 있다고 가정하라.'''

import unittest
import random
import heapq

def partition_nodup(A, left, right, pivot):
    ''' param: [left, right] '''
    assert 0<= left <= right
    assert pivot in A[left:right+1]

    while True:
        while (left <= right) and (A[left] <= pivot):
            left += 1
        while (left <= right) and (pivot < A[right]):
            right -= 1
        if left > right:
            assert left-1 == right
            assert A[right] <= pivot
            return right

        assert left <= right
        assert A[left] > pivot >= A[right]
        A[left],A[right] = A[right],A[left]
        assert A[left] <= pivot < A[right]

def rank_nodup(A, left, right, rank):
    ''' param: [left, right]
        param: rank is 0-based
        result: A is partially sorted. 
                all elements lower than or equal to `rank` are in A[:rank+1]
        '''
    assert left <= rank <= right
    pivot = random.sample(A[left:right+1], 1)[0]

    left_end = partition_nodup(A, left, right, pivot)
    assert 0 <= left <= left_end <= right, "%s<= %s <= %s <= %s" %(0, left, left_end, right)

    if rank < left_end:
        rank_nodup(A, left, left_end, rank)
    elif left_end < rank:
        rank_nodup(A, left_end+1, right, rank)
    else:
        assert left_end == rank
        #assert A[rank] < A[rank+1:]

def find_smallest_n_nodup(A, n):
    ''' A is to be partially modified '''
    assert 0 < n <= len(A)
    rank_nodup(A, 0, len(A)-1, n-1)
    return A[:n]

class PartitionNodupTest(unittest.TestCase):
    def test_partition1(self):
        self.assertPartitioned([5,2,7,3,10,0], 0, [0,2,7,3,10,5])
        self.assertPartitioned([5,2,7,3,10,0], 3, [0,2,3,7,10,5])
        self.assertPartitioned([5,2,7,3,10,0], 5, [5,2,0,3,10,7])
        
    def test_partition_random(self):
        A = [0,1,2,3,4,5,6,7,8,9]
        random.shuffle(A)

        for pivot in [0,1,2,3,4,5,6,7,8,9]:
            rank = pivot
            B = A[:]
            left, right = 0, len(B)-1
            left_end = partition_nodup(B, left, right, pivot)
            assert 0 <= left <= left_end <= right
            
            self.assertPartitionedByRank(B, rank)

    def test_selection_rank_nodup_first(self):
        A = [2,0,1]
        rank=0
        rank_nodup(A, 0, len(A)-1, rank)
        self.assertPartitionedByRank(A, rank)

        A = [2,0,1]
        rank=1
        rank_nodup(A, 0, len(A)-1, rank)
        self.assertPartitionedByRank(A, rank)

        A = [2,0,1]
        rank=2
        rank_nodup(A, 0, len(A)-1, 2)
        self.assertPartitionedByRank(A, rank)

    def test_selection_rank_nodup_random(self):
        A = [0,1,2,3,4,5,6,7,8,9]
        random.shuffle(A)

        for pivot in [0,1,2,3,4,5,6,7,8,9]:
            rank = pivot
            B = A[:]
            rank_nodup(B, 0, len(B)-1, pivot)
            
            self.assertPartitionedByRank(B, rank)

    def assertPartitionedByRank(self, B, rank):
        for lower in B[:rank+1]:
            self.assertTrue(lower <= rank, msg="%s <= %s" %(lower, rank))

        for higher in B[rank+1:]:
            self.assertTrue(rank < higher)

    def assertPartitioned(self, A, pivot, B):
        actual_left_end = partition_nodup(A, 0, len(A)-1, pivot)
        self.assertEqual(A, B)

class FindSmallestNNodupTest(unittest.TestCase):
    def test_samples(self):
        A = list(range(100))

        for smallest_n in range(1, len(A)):
            random.shuffle(A)
            res = find_smallest_n_nodup(A, smallest_n)
            self.assertEqual(len(res), smallest_n)
            self.assertSmallestNs(res, A)

    def assertSmallestNs(self, S, A):
        for s in S:
            self.assertTrue(s in A)

        for s in S:
            for a in A[len(S):]:
                self.assertTrue(s < a)

###################
### dup version ###
###################

def partition_dup(A, left, right, pivot):
    ''' param: [left, right] '''
    assert 0<= left <= right
    assert pivot in A[left:right+1]

    cnt = 0
    while True:
        while (left <= right) and (A[left] <= pivot):
            if (A[left] == pivot): #different part from no_dup ver.
                cnt += 1           #different part from no_dup ver.
            left += 1

        while (left <= right) and (pivot < A[right]):
            right -= 1

        if left > right:
            assert left-1 == right
            assert A[right] <= pivot
            return (right, cnt) #different part from no_dup ver.

        assert left <= right
        assert A[left] > pivot >= A[right]
        A[left],A[right] = A[right],A[left]
        assert A[left] <= pivot < A[right]

def rank_dup(A, left, right, rank):
    ''' param: [left, right]
        param: rank is 0-based
        result: A is partially sorted. 
                all elements lower than or equal to `rank` are in A[:rank+1]
        '''
    assert left <= rank <= right
    pivot = random.sample(A[left:right+1], 1)[0]

    left_end, pivot_cnt = partition_dup(A, left, right, pivot)
    assert 0 <= left <= left_end <= right, "%s<= %s <= %s <= %s" %(0, left, left_end, right)
    assert pivot_cnt >= 1 #different part from no_dup ver.
    
    if left_end - pivot_cnt < rank <= left_end:
        #assert left_end - pivot_cnt < left_end <= rank
        #assert A[left_end] < A[left_end+1:]
        return left_end #different part from no_dup ver.
    elif rank < left_end:
        return rank_dup(A, left, left_end, rank) #different part from no_dup ver.
    elif left_end < rank:
        return rank_dup(A, left_end+1, right, rank) #different part from no_dup ver.
    else:
        assert False, "Cannot reach here"

def find_smallest_n_dup(A, n):
    '''param n: number of elements count for the `n` smallest from A
       returns subset of A, smallest `n` elements; A should be modifiable'''
    assert 0 < n <= len(A)
    left_end = rank_dup(A, 0, len(A)-1, n-1)
    return sorted(A[:left_end+1])[:n] #different part from no_dup ver.

def find_smallest_n_minheap(A, n):
    smallests = []
    for a in A:
        heapq.heappush(smallests, -a)
        if len(smallests) > n:
            heapq.heappop(smallests)

    res = []
    while len(smallests)>0:
        res.insert(0, -heapq.heappop(smallests))
    return res

class FindSmallestNTest(unittest.TestCase):
    def test_samples(self):
        A = [1,1,1,1,1,5,6]
        cnt = 3
        random.shuffle(A)

        res = find_smallest_n_dup(A, cnt)
        A.sort()
        self.assertEqual(res, A[:cnt])

    def test_rank_random(self):
        for _ in range(100):
            A = self.make_random_list(1, 100)
            for cnt in range(1, len(A)+1):
                res = find_smallest_n_dup(A[:], cnt)
                self.assertItsSmallestSubset(res, A)

    def test_minheap_random(self):
        for _ in range(100):
            A = self.make_random_list(1, 100)
            for cnt in range(1, len(A)+1):
                res = find_smallest_n_minheap(A[:], cnt)
                self.assertItsSmallestSubset(res, A)

    def make_random_list(self, length_min, length_max):
        length = random.randint(length_min, length_max)
        res = []
        for _ in range(length):
            next_int = random.randint(0, length-1)
            res.append(next_int)
        return res

    def assertItsSmallestSubset(self, subset, A):
        self.assertEqual(subset, sorted(A)[:len(subset)])

if __name__=="__main__":
    unittest.main()
