#!/usr/bin/env python3

import unittest

class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def print_postorder(cls, root):
        l = cls.print_postorder(cls, root.left) if root.left else []
        r = cls.print_postorder(cls, root.right) if root.right else []
        return [] + l + r + [root.val]

def get_tree(preorder, inorder):
    if len(preorder)==0:
        return None

    root = preorder[0]
    rootidx = inorder.index(root)
    left2, right2 = inorder[:rootidx], inorder[rootidx+1:]
    left1, right1 = preorder[1:1+len(left2)], preorder[1+len(left2):]

    return Tree(root, left=get_tree(left1, left2), right=get_tree(right1, right2))

class TraversalTest(unittest.TestCase):
    def test_Tree(self):
        l = Tree(2)
        r = Tree(3)
        tree = Tree(1,l,r)
        res = Tree.print_postorder(Tree, tree)
        self.assertEqual(res, [2,3,1])

    def test_samples(self):
        preorder = [27, 16, 9, 12, 54, 36, 72]
        inorder = [9, 12, 16, 27, 36, 54, 72]
        tree = get_tree(preorder, inorder)
        self.assertEqual(Tree.print_postorder(Tree, tree), [12, 9, 16, 36, 72, 54, 27])

if __name__=="__main__":
    unittest.main()
