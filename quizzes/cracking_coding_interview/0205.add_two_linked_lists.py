#!/usr/bin/python3
## author: jinchoiseoul@gmail.com
## brief: a linked list represents digits of a number in reverse order. Add two linked lists.
## follow-up question: what if the linked list, now, represents digit of a number in normal order?

import unittest

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def make_reversed_list(n):
    if n == None:
        return
    s = list(reversed(str(n)))
    head = Node(int(s[0]))
    it = head
    for d in s[1:]:
        it.next = Node(int(d))
        it = it.next
    return head
    
def add_reversed_lists(l1, l2, c=0):
    if l1==None and l2==None and c==0:
        return
    v1 = l1.val if l1 else 0
    v2 = l2.val if l2 else 0
    v = v1 + v2 + c
    q,r = divmod(v, 10)
    n = Node(r)
    n.next = add_reversed_lists(l1.next if l1 else None,
                                l2.next if l2 else None,
                                q)
    return n

def make_forward_list(n):
    if n == None:
        return
    ds = [int(c) for c in str(n)]
    head = Node(ds[0])
    it = head
    for d in ds[1:]:
        it.next = Node(d)
        it = it.next
    return head
    
def pad_zeros(l1, l2):
    assert l1
    assert l2
    sz1, sz2 = 0, 0
    it1, it2 = l1, l2
    while it1:
        sz1 += 1
        it1 = it1.next
    while it2:
        sz2 += 1
        it2 = it2.next
    while sz1 < sz2:
        z = Node(0)
        z.next = l1
        l1 = z
        sz1 += 1
    while sz2 < sz1:
        z = Node(0)
        z.next = l2
        l2 = z
        sz2 += 1
    assert sz1 == sz2
    return l1, l2

def add_forward_lists(l1, l2):
    def f(l1, l2):
        if not l1:
            return
        assert l1 and l2
        n = Node(l1.val + l2.val)
        n.next = f(l1.next, l2.next)
        if n.next:
            q,r = divmod(n.next.val, 10)
            n.val += q
            n.next.val = r
        return n

    if l1 == None: l2
    if l2 == None: l1
    l1, l2 = pad_zeros(l1, l2)
    n = f(l1, l2)
    if n.val >= 10:
        n.val %= 10
        x = Node(1)
        x.next(n)
        return x
    else:
        return n

class SolutionTest(unittest.TestCase):
    def test_to_str(self):
        l1 = make_reversed_list(123)
        self.assertEqual(to_str(l1), "3->2->1")

    def test_make_reversed_list(self):
        l1 = make_reversed_list(111)
        l2 = make_reversed_list(111)
        assertListEqual(l1, l2)

    def test_reversed_same_digit_no_carry(self):
        l1 = make_reversed_list(111)
        l2 = make_reversed_list(222)
        actual = add_reversed_lists(l1, l2)
        expected = make_reversed_list(333)
        assertListEqual(actual, expected)

    def test_reversed_same_digit_with_carry(self):
        l1 = make_reversed_list(712)
        l2 = make_reversed_list(338)
        actual = add_reversed_lists(l1, l2)
        expected = make_reversed_list(1050)
        assertListEqual(actual, expected)

    def test_forward_same_digit_no_carry(self):
        l1 = make_forward_list(111)
        l2 = make_forward_list(222)
        actual = add_forward_lists(l1, l2)
        expected = make_forward_list(333)
        assertListEqual(actual, expected)

    def test_forward_same_digit_with_carry(self):
        l1 = make_forward_list(712)
        l2 = make_forward_list(3381)
        actual = add_forward_lists(l1, l2)
        expected = make_forward_list(4093)
        assertListEqual(actual, expected)

def assertListEqual(l1, l2):
    if l1 == l2 == None:
        return
    assert l1 != None and l2 != None
    assert l1.val == l2.val, "{} != {}".format(to_str(l1), to_str(l2))
    assertListEqual(l1.next, l2.next)

def to_str(l):
    res = []
    head = l
    while head:
        res.append(head.val)
        head = head.next
    return '->'.join(str(s) for s in res)

unittest.main()
