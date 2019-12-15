#!/usr/bin/python3
## author: jinchoiseoul@gmail.com


from ._tree_traversers import traverse_pre_order, traverse_in_order
from queue import Queue
from math import inf


def assertEqualTreeTopologies(tree, nodes_in_preorder, nodes_in_inorder):
    ''' this tree topology comparison works only with tree with unique values '''
    actual_nodes_in_preorder = list(n.val for n in traverse_pre_order(tree))
    assert len(actual_nodes_in_preorder) == len(set(actual_nodes_in_preorder)), 'all values on the tree should be unique'
    assert actual_nodes_in_preorder == nodes_in_preorder, 'pre-order should be the same {} == {}'.format(actual_nodes_in_preorder, nodes_in_preorder)
    actual_nodes_in_inorder = list(n.val for n in traverse_in_order(tree))
    assert actual_nodes_in_inorder == nodes_in_inorder, 'in-order should be the same {} == {}'.format(actual_nodes_in_inorder, nodes_in_inorder)


def is_full_tree_bfs(tree):
    def all_has_both_children(nodes):
        assert nodes
        for node in nodes:
            if not node.left:
                return False
            if not node.right:
                return False

        return True
    def none_has_any_children(nodes):
        for node in nodes:
            if node.left:
                return False
            if node.right:
                return False

        return True
    def get_children(nodes):
        '''
        returns a list of children nodes
        ex) [n1, n2, ...]
        '''
        res = []
        for node in nodes:
            res.append(node.left)
            res.append(node.right)
        return res
    
    assert tree
    q = Queue()

    #level = 0
    root_level = [tree]
    q.put(root_level)
    while not q.empty():
        nodes = q.get()
        if all_has_both_children(nodes):
            all_children = get_children(nodes)
            q.put(all_children)
            continue
        elif none_has_any_children(nodes):
            return True
        else:
            return False
       
    assert False


def is_full_tree(node):
    ''' @param node
        @return True if all nil nodes are the same level '''
    def _is_full_tree(node, lv, nil_lv):
        if not node:
            if not nil_lv:
                nil_lv.append(lv)
                return True
            else:
                return nil_lv[0] == lv
        assert node
        if not _is_full_tree(node.left, lv+1, nil_lv):
            return False
        if not _is_full_tree(node.right, lv+1, nil_lv):
            return False
        return True
    return _is_full_tree(node, 0, [])


def is_complete_tree(node):
    def _is_complete_tree(node, lv, nil_lv):
        if not node:
            if not nil_lv:
                nil_lv.append(lv)
                return True
            else:
                #assert 1 <= len(nil_lv) <= 2
                if len(nil_lv) == 1:
                    lv0 = nil_lv[0]
                    if lv0 == lv:
                        return True
                    if lv0 == lv+1:
                        nil_lv.append(lv)
                        return True
                    else:
                        return False
                else:
                    _, lv1 = nil_lv
                    return lv1 == lv
        if not _is_complete_tree(node.left, lv+1, nil_lv):
            return False
        if not _is_complete_tree(node.right, lv+1, nil_lv):
            return False
        return True

    return _is_complete_tree(node, 0, [])


def is_bst1(node, left_boundary=-inf, right_boundary=inf):
    if not node: return True
    if not left_boundary < node.val <= right_boundary:
        return False
    return is_bst1(node.left, left_boundary, node.val) \
            and is_bst1(node.right, node.val, right_boundary)


def is_bst2(node):
    ''' Space Complexity (except stackframe): O(n) '''
    vals = list(n.val for n in traverse_in_order(node))
    for a,b in zip(vals, vals[1:]):
        if not a<=b:
            return False
    return True


def is_bst3(node):
    ''' Space Complexity (except stackframe): O(1) '''
    from collections import deque

    if not node:
        return True

    q = deque()
    it = traverse_in_order(node)
    for _ in range(2):
        try:
            q.append(next(it))
        except:
            return True

    while len(q) == 2:
        if not q[0].val <= q[1].val:
            return False
        q.popleft()
        try:
            next_val = next(it)
            q.append(next_val)
        except StopIteration:
            pass

    return True


is_bst = is_bst1


import unittest
from ._nodes import tree_builder
from .tree_samples import tree_full_1to3, tree_full_1to7, tree_full_1to15, \
                         tree_compelete_1to6, tree_no_complete2, tree_no_complete4, \
                         bst_true1, bst_true2, bst_true3, bst_true4, bst_true5, bst_true6, \
                         bst_false1, bst_false2


class IsFullTreeTest(unittest.TestCase):

    def test_is_full_tree_bfs1(self):
        self.assertTrue(is_full_tree_bfs(tree_full_1to3))
        self.assertTrue(is_full_tree_bfs(tree_full_1to7))
        self.assertTrue(is_full_tree_bfs(tree_full_1to15))

        self.assertFalse(is_full_tree_bfs(tree_no_complete2))
        self.assertFalse(is_full_tree_bfs(tree_no_complete4))


    def test_is_full_tree(self):
        self.assertTrue(is_full_tree(tree_full_1to3))
        self.assertTrue(is_full_tree(tree_full_1to7))
        self.assertTrue(is_full_tree(tree_full_1to15))

        self.assertFalse(is_full_tree(tree_builder([1,2])))
        self.assertFalse(is_full_tree(tree_compelete_1to6))


class IsCompleteTree(unittest.TestCase):

    def test_is_complete_tree(self):
        self.assertTrue(is_complete_tree(tree_builder([])))
        self.assertTrue(is_complete_tree(tree_builder([1])))
        self.assertTrue(is_complete_tree(tree_builder([1,2])))
        self.assertTrue(is_complete_tree(tree_builder([1,2,3,4])))
        self.assertTrue(is_complete_tree(tree_builder([1,2,3,4,5])))
        self.assertTrue(is_complete_tree(tree_compelete_1to6))
        self.assertTrue(is_complete_tree(tree_full_1to7))

        self.assertFalse(is_complete_tree(tree_builder([1,None,3])))
        self.assertFalse(is_complete_tree(tree_builder([1,2,3,4,None,6,7])))
        self.assertFalse(is_complete_tree(tree_no_complete2))
        self.assertFalse(is_complete_tree(tree_no_complete4))


class IsBinarySearchTreeTest(unittest.TestCase):

    def test_basics(self):
        methods_on_test = [is_bst1, is_bst2, is_bst3]
        for method in methods_on_test:
            self.assertTrue(method(bst_true1))
            self.assertTrue(method(bst_true2))
            self.assertTrue(method(bst_true3))
            self.assertTrue(method(bst_true4))
            self.assertTrue(method(bst_true5))
            self.assertTrue(method(bst_true6))
            self.assertTrue(method(tree_builder([4,2,6,2,4])))

            self.assertFalse(method(bst_false1))
            self.assertFalse(method(bst_false2))
            self.assertFalse(method(tree_builder([4,2,6,1,5])))


if __name__=='__main__':

    unittest.main()
