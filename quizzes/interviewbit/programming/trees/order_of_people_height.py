#!/usr/bin/python3
## author: jinchoiseoul@gmail.com


from jpylib.jtrees import Treap


class Solution1:
    ''' Solution using treap '''
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def order(self, heights, infronts):
        n = len(heights)
        
        treap = Treap()
        for i in range(n):
            treap.insert_val(i)
        
        res = [None for _ in range(n)]
        
        for h, f in sorted(zip(heights, infronts)):
            idx = treap.kth(f).val
            res[idx] = h
            treap.delete_at(f)
        
        return res


class Solution2:
    ''' Solution using built-in list '''
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def order(self, heights, infronts):
        pairs = sorted(zip(heights, infronts), reverse=True)
        line = []
        for top, infront in pairs:
            line.insert(infront, top)
        return line


class Solution3:
    ''' Solution using segment tree '''
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def order(self, heights, infronts):
        n = len(heights)
        
        iptree = Solution3.InserterablePositionTree(n)
        
        res = [None for _ in range(n)]
        
        for h, f in sorted(zip(heights, infronts)):
            idx = iptree.kth(f)
            res[idx] = h
        
        return res

    class InserterablePositionTree(object):
        ''' Segment Tree for Insertion Position '''
        def __init__(self, arr_sz):
            self._arr_sz = arr_sz
            self._tree = [None] * (4*arr_sz)
            self._initialize(0, 0, arr_sz-1)
        
        def _initialize(self, root, root_left, root_right):
            tree = self._tree
            if root_left == root_right:
                tree[root] = 1
                return 1
            mid = (root_left + root_right) >> 1
            l_sz = self._initialize(2*root+1, root_left, mid)
            r_sz = self._initialize(2*root+2, mid+1, root_right)
           
            tree[root] = l_sz + r_sz
            return tree[root]

        def kth(self, k):
            ''' @param k: 0-based
                @return pos '''
            res = self._kth(k, 0, 0, self._arr_sz-1)
            return res

        def _kth(self, k, root, root_left, root_right):
            tree = self._tree
            assert 0 <= k < tree[root], "0 <= {} < {}".format(k, tree[root])

            # decr
            tree[root] -= 1

            if root_left == root_right:
                return root_left
            
            li = 2*root+1
            lv = tree[li]
            mid = (root_left + root_right) >> 1
            if k < lv:
                return self._kth(k, 2*root+1, root_left, mid)
            else:
                return self._kth(k-lv, 2*root+2, mid+1, root_right)
            

class Solution4:
    ''' Solution using segment tree '''
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def order(self, heights, infronts):
        n = len(heights)
        
        root = self.Node(0, n-1)
        self.build_tree(root)
        
        res = [None for _ in range(n)]
        
        for h, f in sorted(zip(heights, infronts)):
            idx = self.find_pos(root, f)
            res[idx] = h
        
        return res

    class Node:
        def __init__(self, start, stop):
            self.start = start
            self.stop = stop
            self.space = stop - start + 1
            self.left = self.right = None

    def build_tree(self, root):
        start, stop = root.start, root.stop
        if start == stop:
            return
        mid = (start + stop) >> 1
        root.left = self.Node(start, mid)
        root.right = self.Node(mid+1, stop)
        self.build_tree(root.left)
        self.build_tree(root.right)

    def find_pos(self, root, kth):
        ''' @return pos '''
        assert 0<= kth < root.space
        root.space -= 1
        if root.start == root.stop:
            return root.start
        if kth < root.left.space:
            return self.find_pos(root.left, kth)
        else:
            return self.find_pos(root.right, kth - root.left.space)
 

if __name__ == "__main__":

    import unittest

    class SolutionTest(unittest.TestCase):
        def setUp(self):
            self.sols = [Solution1(), Solution2(), Solution3(), Solution4()]

        def test_basics(self):
            for sol in self.sols:
                heights, infronts = [5,3,2,6,1,4], [0,1,2,0,3,2]
                actual = sol.order(heights, infronts)
                self.assertEqual(actual, [5,3,2,1,6,4])

    unittest.main()
