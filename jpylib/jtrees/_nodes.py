#!/usr/bin/python3
## author: jinchoiseoul@gmail.com


from collections import deque


# Definition for a binary tree node
class TreeNode(object):
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None


def tree_builder(vals, nil=None):
    if not vals:
        return None

    i = 0
    root = TreeNode(vals[i])
    i += 1

    q = deque([root])
    while q and i < len(vals):
        here = q.popleft()
        if vals[i] != nil:
            here.left = TreeNode(vals[i])
            q.append(here.left)
        i += 1
        
        if i < len(vals) and vals[i] != nil:
            here.right = TreeNode(vals[i])
            q.append(here.right)
        i += 1

    return root


def find_tree_depth(tree, depth=0):
    assert tree
    
    depth_of_tree = depth

    if tree.left:
        l_depth = find_tree_depth(tree.left, depth+1)
        depth_of_tree = max(depth_of_tree, l_depth)
    
    if tree.right:
        r_depth = find_tree_depth(tree.right, depth+1)
        depth_of_tree = max(depth_of_tree, r_depth)

    return depth_of_tree


import unittest


class TreeBuilderTest(unittest.TestCase):

    def test_basics(self):
        root = tree_builder([3])
        self.assertEqual(root.val, 3)
        self.assertEqual(root.left, None)
        self.assertEqual(root.right, None)

        root = tree_builder([3,1,2])
        self.assertEqual(root.val, 3)
        self.assertEqual(root.left.val, 1)
        self.assertEqual(root.right.val, 2)

        root = tree_builder([3,None,2])
        self.assertEqual(root.val, 3)
        self.assertEqual(root.left, None)
        self.assertEqual(root.right.val, 2)

        root = tree_builder([3,5,None,None,2,6,7])
        self.assertEqual(root.val, 3)
        self.assertEqual(root.left.val, 5)
        self.assertEqual(root.right, None)
        self.assertEqual(root.left.left, None)
        self.assertEqual(root.left.right.val, 2)
        self.assertEqual(root.left.right.left.val, 6)
        self.assertEqual(root.left.right.right.val, 7)
        self.assertEqual(root.left.right.left.left, None)
        self.assertEqual(root.left.right.right.right, None)


from .tree_samples import sample1, sample2, sample7, sample8


class HelloTest(unittest.TestCase):

    def test_find_tree_depth1(self):
        res = find_tree_depth(sample1)
        self.assertEqual(res, 1)

    def test_find_tree_depth2(self):
        res = find_tree_depth(sample2)
        self.assertEqual(res, 2)

    def test_find_tree_depth3(self):
        res = find_tree_depth(sample7)
        self.assertEqual(res, 3)

    def test_find_tree_depth4(self):
        res = find_tree_depth(sample8)
        self.assertEqual(res, 3)


if __name__ == "__main__":

    unittest.main()
