#!/usr/bin/env python3

import unittest
from math import inf
from itertools import combinations as comb

def get_next(seq, discovered):
    seq_len = len(seq)
    for c in comb(range(seq_len), 2):
        a,b = c
        next_node = seq[0:a] + list(reversed(seq[a:b+1])) + seq[b+1:seq_len]
        if next_node not in discovered:
            yield next_node

def sortgame(not_sorted):
    ''' return minimum cnt to sort `not_sorted` '''
    cnt = 0
    discovered = [not_sorted]
    q = [(0, not_sorted)]
    sorted_seq = sorted(not_sorted)
    while q:
        cnt, seq = q.pop(0)
        if sorted_seq == seq:
            return cnt

        for next_node in get_next(seq, discovered):
            discovered.append(next_node)
            q.append((cnt+1, next_node))
    
    assert False, "cannot reach here"

class ModuleTest(unittest.TestCase):
    def test_get_next(self):
        it = get_next([2,1,3,4], [])
        next_node = next(it)
        self.assertEqual(next_node, [1,2,3,4])

class SortGameTest(unittest.TestCase):
    def test_samples(self):
        self.assertSorted([1,2,3,4,8,7,6,5], 1)
        self.assertSorted([3,999,1,2], 2)
        self.assertSorted([1000, 2000, 3000], 0)

    def assertSorted(self, not_sorted, cnt):
        self.assertEqual(sortgame(not_sorted), cnt)

if __name__=="__main__":
    unittest.main()
