#!/usr/bin/python3
## author: jinchoiseoul@gmail.com


from ._nodes import TreeNode
from random import random, randint, shuffle
import sys
sys.setrecursionlimit(10000)


class TreapNode(TreeNode):

    def __init__(self, val, priority):
        super().__init__(val)
        self.priority = priority
        self.size = 1

    def set_left(self, left):
        self.left = left
        self.resize()
        return self

    def set_right(self, right):
        self.right = right
        self.resize()
        return self

    def resize(self):
        self.size = 1
        if self.left:
            self.size += self.left.size
        if self.right:
            self.size += self.right.size


def insert(root, node, key=lambda n: n):
    ''' @return current node '''
    if not root: return node

    if root.priority < node.priority:
        lhs, rhs = split(root, node, key)
        node.set_left(lhs)
        node.set_right(rhs)
        return node
    elif key(root.val) < key(node.val):
        return root.set_right(insert(root.right, node, key))
    else:
        return root.set_left(insert(root.left, node, key))


def split(node, pivot_node, key=lambda n: n):
    ''' @return (left, right) '''
    if not node:
        return (None, None)
    if key(node.val) <= key(pivot_node.val): #todo: rather <= than <
        lhs, rhs = split(node.right, pivot_node, key)
        node.set_right(lhs)
        return (node, rhs)
    else:
        lhs, rhs = split(node.left, pivot_node, key)
        node.set_left(rhs)
        return (lhs, node)


def delete(node, val):
    ''' Note: User should not call this method unless self is root of the treap
        @return current node '''
    if not node:
        return None
    if node.val == val:
        return merge(node.left, node.right)
    elif node.val < val:
        return node.set_right(delete(node.right, val))
    elif node.val > val:
        return node.set_left(delete(node.left, val))
    return node


def merge(left, right):
    if not left: return right
    if not right: return left
    
    if left.priority >= right.priority: #todo: rather > than >=. test this with duplicate values
        return left.set_right(merge(left.right, right))
    else:
        return right.set_left(merge(left, right.left))


def find(node, val, key=lambda n: n):
    if not node: return None
    if key(node.val) == val:
        return node
    elif key(node.val) < val:
        return find(node.right, val, key)
    else:
        return find(node.left, val, key)


def get_size(root):
    return root.size if root else 0


def get_priority(root):
    return root.priority if root else 0


def kth(root, k):
    if k < 0 or not root: return None
    if root.size <= k: return None
    left_sz = get_size(root.left)
    if left_sz > k:
        return kth(root.left, k)
    elif left_sz == k:
        return root
    else:
        return kth(root.right, k-1-left_sz)


def split_first_k(root, k):
    if not root: return (None, None)
    #if k <= 0: return (None, root) #auxiliary for efficiency
    #if root.size <= k: return (root, None) #auxiliary efficiency

    left_size = get_size(root.left)
    if left_size >= k:
        ll, lr = split_first_k(root.left, k)
        root.set_left(lr)
        return (ll, root)
    else:
        rl,rr = split_first_k(root.right, k-1-left_size)
        root.set_right(rl)
        return (root, rr)


def insert_at(root, k, node):
    ''' this operation could cause skewed treap
        when called in particular orders because it incapacitates `priority`
        Use this with caution, or better yet, consider AVL, RBT, etc
        @return return new root '''
    if not root:
        return node
    assert root
    if k < 0: k = 0
    if k > root.size: k = root.size
    
    left_size = get_size(root.left)
    if left_size > k:
        return root.set_left(insert_at(root.left, k, node))
    elif left_size == k:
        l = root.left
        root.set_left(None)
        node.set_left(l)
        node.set_right(root)
        node.priority = max(map(get_priority, [node.left, node.right]))
        return node
    else:
        return root.set_right(insert_at(root.right, k-1-left_size, node))
        

def delete_at(root, k):
    ''' return new root after deleting kth node 
        @param k: 0-based '''
    if not root: return None
    if k < 0: k = 0
    if k >= root.size: k = root.size-1
    assert k in range(root.size)

    left_size = get_size(root.left)
    if left_size > k:
        return root.set_left(delete_at(root.left, k))
    elif left_size == k:
        return merge(root.left, root.right)
    else:
        return root.set_right(delete_at(root.right, k-1-left_size))


class Treap(object):

    ''' wrapper class for easier usage for treapnode '''

    def __init__(self):
        self.root = None

    def size(self):
        return 0 if not self.root else self.root.size

    def insert_val(self, val, priority=None, key=lambda n: n):
        node = TreapNode(val, random()) if priority == None else TreapNode(val, priority)
        if not self.root:
            self.root = node
        else:
            self.root = insert(self.root, node, key)
        return self

    def delete_val(self, val):
        self.root = delete(self.root, val)
        return self

    def find(self, val, key=lambda n: n):
        return find(self.root, val, key)

    def kth(self, k):
        ''' @param k: 0-based
            @return TreapNode if exists, None otherwise '''
        if not self.root: return None
        return kth(self.root, k)

    def rotate_left(self, k):
        ''' @param k: negative k means rotate_right '''
        if not self.root: return None
        k %= self.root.size
        l,r = split_first_k(self.root, k)
        self.root = merge(r, l)
        return self

    def rotate_right(self, k):
        return self.rotate_left(-k)

    def insert_at(self, k, val, priority=None):
        self.root = insert_at(self.root, k, TreapNode(val, random()  if priority==None else priority))
        return self

    def delete_at(self, k):
        self.root = delete_at(self.root, k)
        return self


import unittest
from math import inf, log
from ._tests import assertEqualTreeTopologies, is_bst
from ._tree_traversers import traverse_in_order


class TreapTestCase(unittest.TestCase):
    def assertSizeValid(self, root):
        self.assertTrue(self.is_size_valid(root))

    def is_size_valid(self, root):
        if not root: return True
        if not self.is_size_valid(root.left) or \
           not self.is_size_valid(root.right):
            return False
        if not root.size == 1 + get_size(root.left) + get_size(root.right):
            return False
        return True

    def assertBSTValid(self, root):
        self.assertTrue(self.is_bst_valid(root))

    def is_bst_valid(self, root):
        return is_bst(root)

    def assertPriorityValid(self, root):
        self.assertTrue(self.is_priority_valid(root))

    def is_priority_valid(self, root):
        if not root: return True
        if not self.is_priority_valid(root.left):
            return False
        if not self.is_priority_valid(root.right):
            return False
        if not get_priority(root.left) <= root.priority or \
           not get_priority(root.right) <= root.priority:
            return False
        return True

    def assertBSTreap(self, root):
        ''' Binary Search Treap '''
        self.assertSizeValid(root)
        self.assertBSTValid(root)
        self.assertPriorityValid(root)

    def assertHeightAlmostLog(self, root):
        expected_height = log(root.size, 1.5)
        #expected_height = log(root.size, 1.33) # by experiments
        actual_height = self.tree_height(root)
        self.assertAlmostEqual(expected_height, actual_height, delta=expected_height*0.8)
        #self.assertAlmostEqual(expected_height, actual_height, delta=expected_height*0.2) # by experiments

    #todo: extract this method into a module
    def tree_height(self, root):
        if not root: return -1
        return 1 + max(map(self.tree_height, [root.left, root.right]))

    def make_shuffled_treap(self, values):
        shuffle(values)
        treap = Treap()
        for v in values:
            treap.insert_val(v)
        return treap


class TreapBasicTest(TreapTestCase):

    def setUp(self):
        self.treap0 = Treap()
        self.treap1 = Treap().insert_val(1, 1)
        self.treap2 = Treap().insert_val(1, 1).insert_val(0,0)
        self.treap3 = Treap().insert_val(1, 1).insert_val(0,0).insert_val(2,0)
        self.treap4 = Treap().insert_val(1, 1).insert_val(0,0).insert_val(2,0).insert_val(3, 0.5)

    def test_add_and_size(self):
        self.assertEqual(self.treap0.root, None)
        self.assertEqual(self.treap0.size(), 0)

        assertEqualTreeTopologies(self.treap1.root, [1], [1])
        self.assertEqual(self.treap1.size(), 1)

        assertEqualTreeTopologies(self.treap2.root, [1,0], [0,1])
        self.assertEqual(self.treap2.size(), 2)

        assertEqualTreeTopologies(self.treap3.root, [1,0,2], [0,1,2])
        self.assertEqual(self.treap3.size(), 3)

        assertEqualTreeTopologies(self.treap4.root, [1,0,3,2], [0,1,2,3])
        self.assertEqual(self.treap4.size(), 4)

    def test_delete(self):
        self.treap0.delete_val(1)
        self.assertEqual(self.treap1.delete_val(1).delete_val(1).size(), 0)
        self.assertEqual(self.treap4.delete_val(1).delete_val(3).size(), 2)

    def test_find(self):
        self.assertTrue(self.treap4.find(2))
        self.assertFalse(self.treap4.find(99))


class TreapInsertUserDefinedType(unittest.TestCase):

    def test_basics(self):
        class Employee(object):
            def __init__(self, name, age):
                self.name = name
                self.age = age

            @classmethod
            def key(cls, emp):
                return (emp.age, emp.name)

        treap = Treap()
        treap.insert_val(Employee('jin', 33), 1, Employee.key)
        treap.insert_val(Employee('min', 30), 2, Employee.key)

        ages_in_order = list(n.val.age for n in traverse_in_order(treap.root))
        self.assertEqual(ages_in_order, [30,33])

        self.assertEqual(treap.root.val.name, 'min')
        self.assertEqual(treap.root.right.val.name, 'jin')
        self.assertTrue(treap.find((33, 'jin'), Employee.key))
        self.assertFalse(treap.find((-1, 'no_exist'), Employee.key))
        

class TreapDuplicateTest(TreapTestCase):

    def test_basics(self):
        treap = Treap()
        treap.insert_val(1, 1).insert_val(2, 0.5)
        treap.insert_val(2, 0.75)
        self.assertBSTreap(treap.root)
        self.assertEqual(treap.root.size, 3)


class TreapComplexTest(TreapTestCase):

    def test_fuzz1(self):
        mini, maxi, tree_size = 0, 1<<30, 10000
        treap = Treap()
        for _ in range(tree_size):
            treap.insert_val(randint(mini, maxi))

        self.assertEqual(treap.size(), tree_size)
        self.assertBSTreap(treap.root)
        self.assertHeightAlmostLog(treap.root)
        #print('fuzz1: ', treap.root.left.size, treap.root.right.size)

    def test_fuzz2(self):
        tree_size = 10000
        treap = Treap()
        for i in range(tree_size):
            treap.insert_val(i)

        self.assertEqual(treap.size(), tree_size)
        self.assertBSTreap(treap.root)
        self.assertHeightAlmostLog(treap.root)
        #print('fuzz2: ', treap.root.left.size, treap.root.right.size)

    def test_fuzz3(self):
        values = list(range(10000))
        treap = self.make_shuffled_treap(values)
        shuffle(values)
        treap = Treap()
        for v in values:
            treap.insert_val(v)
        
        shuffle(values)
        for v in values[:5000]:
            treap.delete_val(v)

        self.assertEqual(treap.size(), 5000)
        self.assertBSTreap(treap.root)
        self.assertHeightAlmostLog(treap.root)

    
class KTest(TreapTestCase):

    def test_kth_basics(self):
        treap = self.make_shuffled_treap(list(range(10000)))
        for k in [0,1,77,777,7777,9999]:
            self.assertEqual(treap.kth(k).val, k)
        for k in [10000, 10001, 987654321]:
            self.assertFalse(treap.kth(k))

        treap.delete_val(0)
        self.assertEqual(treap.kth(0).val, 1)
        self.assertEqual(treap.kth(99).val, 100)
        treap.delete_val(50)
        self.assertEqual(treap.kth(99).val, 101)
        
    def test_split_first_k(self):
        #within boundary
        for k in range(0, 11):
            treap = self.make_shuffled_treap(list(range(10)))
            l,r = split_first_k(treap.root, k)
            self.assertEqual(get_size(l), k)
            self.assertEqual(get_size(r), 10-k)
            self.assertBSTreap(l)
            self.assertBSTreap(r)
        
        #out of boundary
        treap = self.make_shuffled_treap(list(range(10)))
        l,r = split_first_k(treap.root, -99)
        self.assertEqual(get_size(l), 0)
        self.assertEqual(get_size(r), 10)
        self.assertBSTreap(l)
        self.assertBSTreap(r)

        treap = self.make_shuffled_treap(list(range(10)))
        l,r = split_first_k(treap.root, 99)
        self.assertEqual(get_size(l), 10)
        self.assertEqual(get_size(r), 0)
        self.assertBSTreap(l)
        self.assertBSTreap(r)


class RotateTest(TreapTestCase):
    def test_basics(self):
        treap = self.make_shuffled_treap(list(range(10)))

        treap.rotate_left(0)
        self.assertEqual(treap.root.size, 10)
        self.assertBSTreap(treap.root)

        treap.rotate_left(1)
        self.assertEqual(treap.root.size, 10)
        self.assertEqual(treap.kth(0).val, 1)
        self.assertEqual(treap.kth(8).val, 9)
        self.assertEqual(treap.kth(9).val, 0)

        self.assertSizeValid(treap.root)
        self.assertPriorityValid(treap.root)
        with self.assertRaises(AssertionError):
            self.assertBSTValid(treap.root)

        treap.rotate_left(3).rotate_left(3).rotate_left(3).rotate_right(3).rotate_left(3)
        self.assertBSTreap(treap.root)


class InsertAtAndDeleteAtTest(TreapTestCase):

    def test_insert_at(self):
        from itertools import chain
        for k in range(5):
            treap = self.make_shuffled_treap(list(range(5)))
            treap.insert_at(k, 9999)
            self.assertEqual(treap.kth(k).val, 9999)
            self.assertEqual(treap.root.size, 6)
            self.assertSizeValid(treap.root)
            self.assertPriorityValid(treap.root)
            with self.assertRaises(AssertionError):
                self.assertBSTValid(treap.root)

            for v,k in enumerate(chain(range(k), range(k+1, 6))):
                self.assertEqual(treap.kth(k).val, v)
            
    def test_delete_at(self):
        treap = self.make_shuffled_treap(list(range(5)))
        treap.delete_at(0)
        self.assertEqual(treap.kth(0).val, 1)
        treap.delete_at(3)
        self.assertEqual(treap.kth(2).val, 3)
        self.assertFalse(treap.kth(2).right)

        treap.delete_at(0).delete_at(0)
        self.assertFalse(treap.kth(0).left)
        self.assertFalse(treap.kth(0).right)
        self.assertEqual(treap.kth(0).val, 3)

        treap.delete_at(0)
        self.assertFalse(treap.root)

        
if __name__ == "__main__":
    
    unittest.main()
