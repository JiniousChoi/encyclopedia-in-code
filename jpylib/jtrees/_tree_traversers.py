#!/usr/bin/python3
## author: jinchoiseoul@gmail.com


from ._nodes import TreeNode as Tree


def traverse_pre_order(tree):
    '''returns string'''
    if not tree:
        return
    yield tree

    if tree.left:
        yield from traverse_pre_order(tree.left)

    if tree.right:
        yield from traverse_pre_order(tree.right)


def traverse_in_order(tree):
    if not tree:
        return

    if tree.left:
        yield from traverse_in_order(tree.left)

    yield tree

    if tree.right:
        yield from traverse_in_order(tree.right)


def traverse_post_order(tree):
    '''returns string'''
    if not tree:
        return

    if tree.left:
        yield from traverse_post_order(tree.left)

    if tree.right:
        yield from traverse_post_order(tree.right)
    
    yield tree


def traverse_BFS(tree):
    '''returns string'''
    from queue import Queue

    if not tree:
        return

    q = Queue()
    q.put(tree)
    while not q.empty():
        t = q.get()
        yield t
        l,r = t.left, t.right
        if l: q.put(l)
        if r: q.put(r)


import unittest
from .tree_samples import sample1, sample2


class TraverserTest(unittest.TestCase):

    def test_traverse_in_order1(self):
        root = Tree(1)
        result = list(n.val for n in traverse_in_order(root))
        self.assertEqual(result, [1])

    def test_traverse_in_order2(self):
        root = Tree('-')
        root.left = Tree('1')
        root.right = Tree('3')
        result = ''.join(list(n.val for n in traverse_in_order(root)))
        self.assertEqual(result, '1-3')

    def test_traverse_sample1_pre_order(self):
        res = list(n.val for n in traverse_pre_order(sample1))
        self.assertEqual(res, [2,1,3])

    def test_traverse_sample1_in_order(self):
        res = list(n.val for n in traverse_in_order(sample1))
        self.assertEqual(res, [1,2,3])

    def test_traverse_sample1_post_order(self):
        res = list(node.val for node in traverse_post_order(sample1))
        self.assertEqual(res, [1,3,2])

    def test_traverse_sample1_BFS1(self):
        res = list(n.val for n in traverse_BFS(sample1))
        self.assertEqual(res, [2,1,3])

    def test_traverse_sample1_BFS2(self):
        res = list(n.val for n in traverse_BFS(sample2))
        self.assertEqual(res, [4,2,6,1,3,5,7])

if __name__=='__main__':
    unittest.main()
