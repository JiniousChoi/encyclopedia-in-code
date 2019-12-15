#!/usr/bin/python3
## author: jinchoiseoul@gmail.com


from math import inf
from jpylib.jmath import single_bit_ceil


class RMQ(object):
    ''' Range Minimum Query '''

    def __init__(self, arr):
        self.arr_sz = arr_sz = len(arr)
        self.tree_sz = tree_sz = self.__calc_tree_sz(arr_sz)
        self.range_min = range_min = [None] * tree_sz # complete binary tree
        self.__initialize(arr, 0, 0, arr_sz-1)

    def __initialize(self, arr, root, root_left, root_right):
        ''' @param arr
            @param root: 0-based
            @param root_left: 0-based
            @param root_right: 0-based
            @return range_min of root after setting in post-order '''
        if root_left == root_right:
            self.range_min[root] = arr[root_left]
            return self.range_min[root]

        mid = (root_left + root_right) >> 1
        left_min = self.__initialize(arr, root*2+1, root_left, mid)
        right_min = self.__initialize(arr, root*2+2, mid+1, root_right)
        self.range_min[root] = min(left_min, right_min)
        return self.range_min[root]
    
    def __calc_tree_sz(self, arr_sz):
        ''' @return tree_sz::int '''
        return single_bit_ceil(arr_sz) * 2

    def query(self, left, right):
        assert left <= right
        return self.__query(left, right, 0, 0, self.arr_sz-1)

    def __query(self, left, right, root, root_left, root_right):
        range_min = self.range_min
        if (right < root_left) or (root_right < left):
            return inf
        elif left <= root_left <= root_right <= right:
            return range_min[root]
        mid = (root_left + root_right) >> 1
        return min(self.__query(left, right, root*2+1, root_left, mid),
                   self.__query(left, right, root*2+2, mid+1, root_right))

    def update(self, arr_idx, new_val):
        return self.__update(arr_idx, new_val, 0, 0, self.arr_sz-1)

    def __update(self, arr_idx, new_val, root, root_left, root_right):
        ''' @return newly updated value for the `root` '''
        range_min = self.range_min

        #over the hedge
        if (arr_idx < root_left) or (root_right < arr_idx):
            # no need to update
            return range_min[root]

        #on the hedge
        if root_left == root_right:
            range_min[root] = new_val
            return range_min[root]
        
        mid = (root_left + root_right) >> 1
        range_min[root] = min(self.__update(arr_idx, new_val, 2*root+1, root_left, mid),
                              self.__update(arr_idx, new_val, 2*root+2, mid+1, root_right))
        return range_min[root]


import unittest


def naive_min(arr, l, r):
    return min(arr[l:r+1])


class RMQTest(unittest.TestCase):

    def test_query(self):
        arr = [5,2,1,4,3]
        rmq = RMQ(arr)
        for l in range(len(arr)):
            for r in range(l, len(arr)):
                self.assertEqual(rmq.query(l,r), naive_min(arr,l,r))

    def test_update(self):
        arr = [5,2,1,4,3]
        rmq = RMQ(arr)
        for arr_idx, new_val in [(0,3),(2,-1),(4,-2)]:
            arr[arr_idx] = new_val
            rmq.update(arr_idx, new_val)

            for l in range(len(arr)):
                for r in range(l, len(arr)):
                    self.assertEqual(rmq.query(l,r), naive_min(arr,l,r))


if __name__ == "__main__":

    unittest.main()
