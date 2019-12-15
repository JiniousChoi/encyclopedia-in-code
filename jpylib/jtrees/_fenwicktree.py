#!/usr/bin/python3
## author: jinchoiseoul@gmail.com


class FenwickTree(object):
    ''' a.k.a. Binary Indexed Tree '''

    def __init__(self, sz):
        self.sz = sz + 1 # add dummy head
        self.tree = [0] * self.sz
    
    def add_all(self, vals):
        for pos, val in enumerate(vals):
            self.add(pos, val)
    
    def add(self, pos, val):
        ''' @param pos: 0-based
            @param val '''
        pos += 1 # 1-based
        while pos < self.sz:
            self.tree[pos] += val
            pos += (pos & -pos)

    def partial_sum(self, pos):
        ''' @param pos: 0-based
            @return sum of A[0...pos] '''
        if pos < 0: return 0
        assert 0 <= pos < self.sz-1
        pos += 1 # 1-based
        psum = 0
        while pos > 0:
            psum += self.tree[pos]
            pos &= pos-1
        return psum

    def range_sum(self, from0, to0):
        ''' both inclusive, both 0-based '''
        assert 0 <= from0 <= to0 < self.sz # 0-based
        return self.partial_sum(to0) - self.partial_sum(from0 - 1)


import unittest


def naive_sum(arr, l, r):
    return sum(arr[l:r+1])


class FenwickTreeTest(unittest.TestCase):

    def test_range_sum(self):
        arr = [5,2,1,4,3]
        sz = len(arr)
        fenwick = FenwickTree(sz)
        fenwick.add_all(arr)

        # explicit cases
        self.assertEqual(fenwick.range_sum(0,0), 5)
        self.assertEqual(fenwick.range_sum(0,1), 7)
        self.assertEqual(fenwick.range_sum(0,4), 15)

    def test_range_sum_all(self):
        arr = [5,2,1,4,3]
        sz = len(arr)
        fenwick = FenwickTree(sz)
        fenwick.add_all(arr)

        # all cases
        for l in range(sz):
            for r in range(l, sz):
                self.assertEqual(fenwick.range_sum(l,r), naive_sum(arr,l,r))


if __name__ == "__main__":
    unittest.main()
