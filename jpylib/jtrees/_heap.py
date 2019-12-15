#!/usr/bin/python3
## author: jinchoiseoul@gmail.com


from math import inf


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


class MinHeap(object):

    def __init__(self):
        self.__tree = []

    def push(self, val):
        tree = self.__tree
        tree.append(val)
        ci = len(tree)-1
        pi = (ci-1)>>1
        while ci > 0 and tree[pi] > tree[ci]:
            swap(tree, ci, pi)
            ci = pi
            pi = (ci-1)>>1
        #assert ci==0 or tree[pi] <= tree[ci]
        return self

    def pop(self):
        tree = self.__tree
        if len(tree) == 0:
            return None
        elif len(tree) == 1:
            return tree.pop(-1)
        else:
            #adjustment needed
            res = tree[0]
            tree[0] = tree.pop(-1)
            ci, cv = 0, tree[0]
            li, ri = self._get_children_indice(ci)
            lv, rv = self._get_children_values(ci)
            while ci < len(tree) and not self.is_stable_triangle(cv, lv, rv):
                if rv==inf or lv <= rv:
                    swap(tree, ci, li)
                    ci = li
                else:
                    swap(tree, ci, ri)
                    ci = ri
                li, ri = self._get_children_indice(ci)
                lv, rv = self._get_children_values(ci)
            return res

    def _get_children_indice(self, ci):
        li, ri = 2*ci+1, 2*ci+2
        return li, ri

    def _get_children_values(self, ci):

        def _get_val(idx):
            tree = self.__tree
            n = len(tree)
            if idx >= n: return inf
            return tree[idx]

        li, ri = self._get_children_indice(ci)
        lv, rv = map(_get_val, [li, ri])
        return lv, rv

    def is_stable_triangle(self, cv, lv, rv):
        assert cv != inf
        if lv == rv == inf:
            return True
        elif rv == inf:
            return cv <= lv
        else:
            return cv <= lv and cv <= rv

    def size(self):
        return len(self.__tree)


class MaxHeap(object):

    def __init__(self):
        self.minheap = MinHeap()

    def push(self, val):
        return self.minheap.push(-val)

    def pop(self):
        return -self.minheap.pop()

    def size(self):
        return self.minheap.size()


import unittest


class HeapTest(unittest.TestCase):

    def test_minheap_basics(self):
        minheap = MinHeap()
        minheap.push(1)
        self.assertEqual(minheap.pop(), 1)
        self.assertEqual(minheap.pop(), None)

        minheap.push(2).push(1)
        self.assertEqual(minheap.pop(), 1)
        self.assertEqual(minheap.pop(), 2)
        self.assertEqual(minheap.pop(), None)


    def test_minheap_complex(self):
        from random import shuffle
        arr = list(range(10))
        shuffle(arr)

        minheap = MinHeap()
        for v in arr:
            minheap.push(v)

        for i in range(10):
            self.assertEqual(minheap.pop(), i)

    def test_maxheap_complex(self):
        from random import shuffle
        arr = list(range(10))
        shuffle(arr)

        maxheap = MaxHeap()
        for v in arr:
            maxheap.push(v)

        for i in range(9,-1,-1):
            self.assertEqual(maxheap.pop(), i)

    def test_size(self):
        for Heap in [MinHeap, MaxHeap]:
            heap = Heap()
            for i in range(10):
                self.assertEqual(heap.size(), i)
                heap.push(i)


if __name__ == "__main__":

    unittest.main()
