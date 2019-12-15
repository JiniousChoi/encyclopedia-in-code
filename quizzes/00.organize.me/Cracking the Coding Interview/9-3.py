#!/usr/bin/env python3
''' find magic index '''

import unittest

def find_magic_index(A):
    ''' li is in increasing order without duplicate elements '''
    assert len(A) > 0

    i,j = 0, len(A)-1

    while i<=j:
        half = (i+j)//2
        if A[half] == half:
            return half
        elif A[half] > half:
            j = half - 1
        else:
            i = half + 1
    
    assert i > j
    return -1

class FindMagicIndexTest(unittest.TestCase):
    def test_method1(self):
        self.assertMagicIndex([1])
        self.assertMagicIndex([0])
        self.assertMagicIndex([-1])

        self.assertMagicIndex([1,2,3])
        self.assertMagicIndex([0,2,3])
        self.assertMagicIndex([-1,1,3])

        self.assertMagicIndex([-1,0,2,3])

    def assertMagicIndex(self, A):
        index = find_magic_index(A)
        if index==-1:
            self.assertNoMagicIndex(A)
        else:
            self.assertEqual(A[index], index)

    def assertNoMagicIndex(self, A):
        for i,e in enumerate(A):
            assert i!=e, "This list(%s) is not supposed to have mgic index" % (A)

if __name__=="__main__":
    unittest.main()
