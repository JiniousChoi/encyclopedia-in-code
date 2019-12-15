#!/usr/bin/python3

import unittest
from printer import pages_in_order, _pairing, _taking_odd, _taking_even, _flattening

class PrinterTest(unittest.TestCase):

    def test_even_pages(self):
        tot_pages, per_each_page = 4, 1
        fp, sp = pages_in_order(tot_pages, per_each_page)
        self.assertEqual(fp, [1,3])
        self.assertEqual(sp, [4,2])

    def test_odd_pages(self):
        tot_pages, per_each_page = 5, 1
        fp, sp = pages_in_order(tot_pages, per_each_page)
        self.assertEqual(fp, [1,3,5])
        self.assertEqual(sp, [4,2])

    def test_pairing_1(self):
        tot_pages, per_each_page = 5, 1
        paired = _pairing(tot_pages, per_each_page)
        self.assertEqual(paired, [[1], [2], [3], [4], [5]])

    def test_pairing_2(self):
        tot_pages, per_each_page = 5, 2
        paired = _pairing(tot_pages, per_each_page)
        self.assertEqual(paired, [[1,2], [3,4], [5]])

        tot_pages, per_each_page = 6, 2
        paired = _pairing(tot_pages, per_each_page)
        self.assertEqual(paired, [[1,2], [3,4], [5,6]])

    def test_pairing_3(self):
        tot_pages, per_each_page = 5, 4
        paired = _pairing(tot_pages, per_each_page)
        self.assertEqual(paired, [[1,2,3,4], [5]])

        tot_pages, per_each_page = 8, 4
        paired = _pairing(tot_pages, per_each_page)
        self.assertEqual(paired, [[1,2,3,4], [5,6,7,8]])

    def test_taking_odd(self):
        l = [[1],[2],[3],[4],[5]]
        o = _taking_odd(l)
        self.assertEqual(o, [[1],[3],[5]])
        
    def test_taking_even(self):
        l = [[1],[2],[3],[4],[5]]
        o = _taking_even(l)
        self.assertEqual(o, [[2],[4]])
        
    def test_flattening(self):
        l = [[1],[2],[3],[4],[5]]
        o = _flattening(l)
        self.assertEqual(o, [1,2,3,4,5])

if __name__=="__main__":
    unittest.main()
