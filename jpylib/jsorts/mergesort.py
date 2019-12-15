#!/usr/bin/python3
## author: jinchoiseoul@gmail.com 


from math import ceil
import sys
sys.setrecursionlimit(10000)


def mergesort_iter(arr):
    n = len(arr)
    tmp = [None] * n
    if n%2==1:
        #optimization
        tmp[-1] = arr[-1]
    unit = 1
    while unit < n:
        for i in range(int(ceil(n/2/unit))):
            begin, end = 2*i*unit, 2*(i+1)*unit
            
            b1, e1 = begin, begin + unit
            b2, e2 = begin + unit, min(end, n)
            i1, i2, i3 = b1, b2, b1

            if e1 >= n:
                #optimization
                continue

            while i1 < e1 and i2 < e2:
                if arr[i1] <= arr[i2]:
                    tmp[i3] = arr[i1]
                    i1 += 1
                    i3 += 1
                else:
                    tmp[i3] = arr[i2]
                    i2 += 1
                    i3 += 1

            while i1 < e1:
                tmp[i3] = arr[i1]
                i1 += 1
                i3 += 1
            #assert i1 == e1 #

            while i2 < e2:
                tmp[i3] = arr[i2]
                i2 += 1
                i3 += 1
            #assert i2 == e2 #

        #assert len(tmp) == n, 'tmp({})'.format(tmp) #
        arr, tmp = tmp, arr
        unit *= 2

    #assert unit >= n #
    return arr


def mergesort_recur(arr):
    n = len(arr)
    half = n >> 1

    if n <= 1:
        return arr

    first = mergesort_recur(arr[:half])
    secon = mergesort_recur(arr[half:])

    i1, j1 = 0, half
    i2, j2 = 0, n-half
    
    res = []
    while i1 < j1 and i2 < j2:
        if first[i1] <= secon[i2]:
            res.append(first[i1])
            i1 += 1
        else:
            res.append(secon[i2])
            i2 += 1

    while i1 < j1:
        res.append(first[i1])
        i1 += 1
    while i2 < j2:
        res.append(secon[i2])
        i2 += 1

    return res


mergesort = mergesort_recur


import unittest


class MergeTest(unittest.TestCase):
    def setUp(self):
        self.methods = [mergesort_iter, mergesort_recur]

    def test_basics(self):
        for mergesort in self.methods:
            self.assertEqual(mergesort([1]), [1])
            self.assertEqual(mergesort([1,2]), [1,2])
            self.assertEqual(mergesort([2,1]), [1,2])
            self.assertEqual(mergesort([2,1,3]), [1,2,3])

    def test_complex(self):
        import random
        data = [random.randint(0,10) for _ in range(100)]
        for mergesort in self.methods:
            self.assertEqual(mergesort(data), sorted(data), msg=mergesort)


if __name__ == "__main__":

    unittest.main()
