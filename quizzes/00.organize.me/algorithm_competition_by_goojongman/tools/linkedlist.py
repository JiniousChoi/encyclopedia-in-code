#!/usr/bin/env python3

import unittest

class LinkedList:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

    def set_next(self, node):
        self.next = node

    def get_next(self):
        return self.next

    def remove(self):
        말이 안되나?...


class LinkedListTest(unittest.TestCase):
    def test_setnextnode(self):
        ll2 = LinkedList(2)
        ll1 = LinkedList(1, ll2)
        
        self.assertEqual(ll1.val, 1)
        self.assertEqual(ll1.get_next().val, 2)
        self.assertEqual(ll1.get_next().get_next(), None)

    def test_remove_next_node(self):
        ll2 = LinkedList(2)
        ll1 = LinkedList(1, ll2)

        whatsnext = ll1.remove()
        self.assertEqual(whatsnext, ll2)

if __name__ == "__main__":
    unittest.main()
