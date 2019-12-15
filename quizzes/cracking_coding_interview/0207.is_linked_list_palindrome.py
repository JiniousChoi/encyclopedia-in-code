#!/usr/bin/python3
## author: jinchoiseoul@gmail.com
## brief: Check if a given linked list is a palindrome.

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def is_palindrome(ls):
    if not ls:
        return True
    stack = []
    while ls:
        stack.append(ls.val)
        ls = ls.next
    return ''.join(stack) == ''.join(reversed(stack))

import unittest

class SolutionTest(unittest.TestCase):
    def test_no_palindrome(self):
        l = make_list("a->b->c")
        self.assertFalse(is_palindrome(l))

    def test_palindrome_odd(self):
        l = make_list("a->b->a")
        self.assertTrue(is_palindrome(l))

    def test_palindrome_even(self):
        l = make_list("a->b->b->a")
        self.assertTrue(is_palindrome(l))

def make_list(s):
    if not s:
        return
    vs = s.split("->")
    head = Node(vs[0])
    it = head
    for v in vs[1:]:
        it.next = Node(v)
        it = it.next
    return head

unittest.main()
