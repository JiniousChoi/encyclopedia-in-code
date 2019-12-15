#!/usr/bin/env python3

import unittest

class Tree:
    def __init__(self, v):
        self.v = v
        self.left = None
        self.right = None

    def is_terminal(self):
        return self.left==None and self.right==None

def tree_path_expander_DFS(path):
    ''' path : [node]
        return : [(node.val)] '''
    assert path and len(path) > 0

    last_node = path[-1]
    if last_node.is_terminal():
        return [tuple(n.v for n in path)]

    res = []

    if last_node.left:
        res += tree_path_expander_DFS(path[:] + [last_node.left])

    if last_node.right:
        res += tree_path_expander_DFS(path[:] + [last_node.right])

    return res

def tree_path_expander_DFS2(node):
    ''' node: node to search below
        return [(node.val)]'''
    assert node != None

    if node.is_terminal():
        return [(node.v,)]
    
    #assert node is not terminal
    res = []

    if node.left:
        res_left = tree_path_expander_DFS2(node.left)
        res += [(node.v,) + vals for vals in res_left]

    if node.right:
        res_right = tree_path_expander_DFS2(node.right)
        res += [(node.v,) + vals for vals in res_right]

    return res

def tree_path_expander_BFS(node):
    ''' node: node as root to search below
        return: [(node.val)]'''
    
    paths = [[node]]
    res_paths = []

    while paths:
        path = paths.pop(0)
        last_node = path[-1]
        if last_node.is_terminal():
            res_paths.append(path)
            continue
        if last_node.left:
            new_path = path[:] + [last_node.left]
            paths.append(new_path)
        if last_node.right:
            new_path = path[:] + [last_node.right]
            paths.append(new_path)

    return [tuple(n.v for n in path) for path in res_paths]

class TreePathExpanderTest(unittest.TestCase):
    def test_dfs_and_bfs1(self):
        root, left, right = Tree(0), Tree(1), Tree(2)
        root.left, root.right = left, right

        self.assertEqual(tree_path_expander_DFS([root]), [(0,1),(0,2)])
        self.assertEqual(tree_path_expander_DFS2(root), [(0,1),(0,2)])
        self.assertEqual(tree_path_expander_BFS(root), [(0,1),(0,2)])

    def test_dfs_and_bfs2(self):
        n1, n2, n3, n4, n5 = Tree(1), Tree(2), Tree(3), Tree(4), Tree(5)
        n1.left = n2
        n2.left = n3
        n2.right = n4
        n4.right = n5

        self.assertEqual(tree_path_expander_DFS([n1]), [(1,2,3),(1,2,4,5)])
        self.assertEqual(tree_path_expander_DFS2(n1), [(1,2,3),(1,2,4,5)])
        self.assertEqual(tree_path_expander_BFS(n1), [(1,2,3),(1,2,4,5)])

if __name__=="__main__":
    unittest.main()
