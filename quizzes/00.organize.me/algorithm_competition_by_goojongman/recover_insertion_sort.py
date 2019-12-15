#!/usr/bin/env python3

import unittest
from treap import Treap

class RecoverInsertion:
    def __init__(self, hints):
        self.hints = hints

    def recover(self):
        treap = Treap.make_treap(Treap, range(1, len(self.hints)+1))
        res = []
        for hint in reversed(self.hints):
            node = treap.k_th(treap.size()-1-hint)
            treap = treap.delete_val(node.val)
            res.insert(0, node.val)
        return res
        
class RecoverInsertionTest(unittest.TestCase):
    def recover(self, hint, original):
        self.assertEqual(RecoverInsertion(hint).recover(), original)

    def test_samples(self):
        self.recover([0,1,1,2,3], [5,1,4,3,2])
        self.recover([0,1,2,3], [4,3,2,1])
        

if __name__=="__main__":
    unittest.main()
