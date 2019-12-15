#!/usr/bin/python3
## author: jinchoiseoul@gmail.com
## brief: (Revised) Return the starting point of the loop entry node if it's circular linked list. Otherwise, None

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def find_loop_entry(ls):
    if ls == None:
        # None is not a circular lined list,
        # hence returning None
        return None
    assert ls

    slow, fast = ls, ls
    while True:
        if not fast.next or not fast.next.next:
            return None
        assert fast.next and fast.next.next
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break
    assert fast == slow

    it = ls
    while it != slow:
        it = it.next
        slow = slow.next
    assert it == slow

    return it

import unittest

class SolutionTest(unittest.TestCase):
    def test_no_loop(self):
        ls = make_list("1->2->3")
        self.assertIsNone(find_loop_entry(ls))

    def test_loop1(self):
        ls = make_list("1->2->3->4->2")
        actual = find_loop_entry(ls)
        expected = ls.next
        self.assertEqual(actual, expected)

    def test_loop1(self):
        ls = make_list("1->2->3->4->1")
        actual = find_loop_entry(ls)
        expected = ls
        self.assertEqual(actual, expected)

def make_list(s):
    m = {}
    vs = s.split("->")
    for v in vs:
        if v not in m:
            m[v] = Node(v)
    for v1,v2 in zip(vs, vs[1:]):
        n1, n2 = m[v1], m[v2]
        n1.next = n2
    return m[vs[0]]

unittest.main()
