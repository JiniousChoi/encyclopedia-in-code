#!/usr/bin/env python3

import unittest

class Tree:
    def __init__(self, v):
        self.v = v
        self.left = None
        self.right = None

    def is_terminal(self):
        return self.left==None and self.right==None

def preorder(root):
    ''' return [node.v] '''

    stack = [root]
    visited = set()

    res = []
    while stack:
        node = stack[-1]

        if node not in visited:
            visited.add(node)
            res.append(node.v)
        if node.left and node.left not in visited:
            stack.append(node.left)
            continue
        if node.right and node.right not in visited:
            stack.append(node.right)
            continue
        stack.pop(-1)
    return res

def inorder(root):
    ''' return [node.v] '''

    stack = [root]
    visited = set()

    res = []
    while stack:
        node = stack[-1]
        if node.left and node.left not in visited:
            stack.append(node.left)
            continue
        if node not in visited:
            visited.add(node)
            res.append(node.v)
        if node.right and node.right not in visited:
            stack.append(node.right)
            continue
        stack.pop(-1)
    return res

def postorder(root):
    ''' return [node.v] '''

    stack = [root]
    visited = set()

    res = []
    while stack:
        node = stack[-1]
        if node.left and node.left not in visited:
            stack.append(node.left)
            continue
        if node.right and node.right not in visited:
            stack.append(node.right)
            continue
        if node not in visited:
            visited.add(node)
            res.append(node.v)
        stack.pop(-1)
    return res

class XTest(unittest.TestCase):
    def test_sample1(self):
        root, left, right = Tree(0), Tree(1), Tree(2)
        root.left, root.right = left, right
        self.assertEqual(preorder(root), [0,1,2])
        self.assertEqual(inorder(root), [1,0,2])
        self.assertEqual(postorder(root), [1,2,0])

    def test_dfs_and_bfs2(self):
        n1, n2, n3, n4, n5 = Tree(1), Tree(2), Tree(3), Tree(4), Tree(5)
        n1.left = n2
        n2.left = n3
        n2.right = n4
        n4.right = n5

        self.assertEqual(preorder(n1), [1,2,3,4,5])
        self.assertEqual(inorder(n1), [3,2,4,5,1])
        self.assertEqual(postorder(n1), [3,5,4,2,1])

if __name__=="__main__":
    unittest.main()
