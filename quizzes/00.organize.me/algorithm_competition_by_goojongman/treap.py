#!/usr/bin/env python3

import unittest
from functools import reduce
from random import shuffle, randint

class Treap:
    def __init__(self, priority, val):
        self.priority = priority
        self.val = val
        self.left = None
        self.right = None
        self.__size = 1

    def __iter__(self):
        yield from self.iter_preorder()

    def iter_preorder(self):
        yield self
        if self.left:
            yield from self.left.iter_preorder()
        if self.right:
            yield from self.right.iter_preorder()

    def iter_inorder(self):
        if self.left:
            yield from self.left.iter_inorder()
        yield self
        if self.right:
            yield from self.right.iter_inorder()

    def iter_postorder(self):
        if self.left:
            yield from self.left.iter_postorder()
        if self.right:
            yield from self.right.iter_postorder()
        yield self

    def print_inorder(self):
        for node in self.iter_inorder():
            print(node.val, end=', ')

    def size(self):
        return self.__size

    def size2(self):
        def getLeftSize(tree):
            left = tree.left
            return left.size2() if left else 0
        def getRightSize(tree):
            right = tree.right
            return right.size2() if right else 0

        return 1 + getLeftSize(self) + getRightSize(self)


    def resize(self):
        self.__size = 1
        if self.left:
            self.__size += self.left.__size
        if self.right:
            self.__size += self.right.__size

    def measure_depth(self):
        return self.measure_height() - 1

    def measure_height(self):
        left_height = 0
        right_height = 0

        if self.left:
            left_height = self.left.measure_height()
        if self.right:
            right_height = self.right.measure_height()

        return 1 + max(left_height, right_height)

    def make_treap(cls, values):
        def next_int():
            return randint(0, len(values))

        assert values
        tree = Treap(next_int(), values[0])
        for val in values[1:]:
            tree = Treap.add(Treap, tree, Treap(next_int(), val))
        return tree

    def ify(cls, nodes):
        if not nodes:
            return None

        nodes.sort(key=lambda n: n.priority, reverse=True)

        root = nodes.pop(0)
        for child in nodes:
            cls.__ify(cls, root, child)

        #calculate size by postorder
        for node in root.iter_postorder():
            node.__size = 1
            node.__size += node.left.__size if node.left else 0
            node.__size += node.right.__size if node.right else 0

        return root
    
    def __ify(cls, root, child):
        if root.val < child.val:
            if root.right:
                cls.__ify(cls, root.right, child)
            else:
                root.right = child

        else:
            if root.left:
                cls.__ify(cls, root.left, child)
            else:
                root.left = child

    def delete_val(self, val):
        '''return new treap after deleing `val` node'''
        _, new_root = self.__delete_val(val)
        return new_root

    def __delete_val(self, val):
        ''' return (Bool::Found, Treap::new root '''
        if self.val == val:
            return (True, self.delete_top())

        if self.left:
            found, new_left = self.left.__delete_val(val)
            if found:
                self.left = new_left
                self.resize()
                return (True, self)

        if self.right:
            found, new_right = self.right.__delete_val(val)
            if found:
                self.right = new_right
                self.resize()
                return (True, self)

        return (False, self)

    def delete_top(self):
        ''' delete top node from treap and then return new top node'''
        return self.join_treaps(self.left, self.right)

    def join_treaps(self, one, two):
        ''' join two trees and return top node '''
        #basis
        if not one: return two
        if not two: return one

        #recursive
        if one.priority > two.priority:
            ll, lr = one.left, one.right
            one.right = self.join_treaps(lr, two)
            one.right.resize(); one.resize()
            return one
        else:
            rl, rr = two.left, two.right
            two.left = self.join_treaps(one, rl)
            two.left.resize(); two.resize()
            return two

    def find(self, val):
        '''return if val is found in tree'''
        if self.val == val:
            return True

        if self.left and self.left.find(val):
            return True

        if self.right and self.right.find(val):
            return True

        return False

    def count_less_than(self, key):
        if key <= self.val:
            if self.left:
                return self.left.count_less_than(key)
            return 0
        else:
            left_size = self.left.size() if self.left else 0
            right_cnt = self.right.count_less_than(key) if self.right else 0
            return left_size + 1 + right_cnt

    def k_th(self, k):
        assert 0<= k < self.size(), "0<= %s < %s" %(k, self.size())
        
        left_size = self.left.size() if self.left else 0

        if k < left_size:
            return self.left.k_th(k)

        if left_size == k:
            return self

        #assert self.right
        return self.right.k_th(k-left_size-1)

    def add(cls, tree, node):
        '''return new tree with node added'''
        assert not tree.find(node.val)

        return cls.__add(cls, tree, node)

    def __add(cls, tree, new_node):
        ''' return Treap::root '''
        def get_child(tree, new_node):
            if tree.val < new_node.val:
                return tree.right
            else:
                return tree.left

        def set_child(tree, new_child):
            if tree.val < new_child.val:
                tree.right = new_child
            else:
                tree.left = new_child

        #code starts here
        if not tree:
            return new_node

        if tree.priority > new_node.priority:
            new_child = cls.__add(cls, get_child(tree, new_node), new_node)
            set_child(tree, new_child)
            tree.resize()
            return tree
        else:
            left_child, right_child = tree.split_and_merge(new_node.val)
            new_node.left = left_child
            new_node.right = right_child
            new_node.resize()
            return new_node

        assert False, "cannot reach here"

    def reduce_lq(self, lq):
        def merge_lq(left_side, right_side):
            ''' return left_side '''
            if left_side.right:
                merge_lq(left_side.right, right_side)
            else:
                left_side.right = right_side
            left_side.resize()
            return left_side

        #code starts here
        stack = lq
        if not stack:
            return None

        res = None
        while stack:
            res = merge_lq(stack.pop(-1), res)

        return res

    def reduce_rq(self, rq):
        def merge_rq(right_side, res):
            ''' return right_side'''
            if right_side.left:
                merge_rq(right_side.left, res)
            else:
                right_side.left = res
            right_side.resize()
            return right_side

        stack = rq
        if not stack:
            return None

        res = None
        while stack:
            res = merge_rq(stack.pop(-1), res)

        return res

    def split_and_merge(self, key):
        #code starts here
        lq, rq = self.split(key)
        left_child = self.reduce_lq(lq)
        right_child = self.reduce_rq(rq)

        return left_child, right_child

    def split(self, key):
        lq = []
        rq = []
        Treap.__split(Treap, self, key, lq, rq)
        return lq, rq

    def __split(cls, tree, key, lq, rq):
        def node_sign(tree, key):
            ''' '<' if lesser, '>' if greater '''
            if tree.val < key:
                return '<'
            elif tree.val > key:
                return '>'
            assert False, "unreachable, '='"

        def child_sign(sign, tree, key):
            if not tree:
                return 'n/a'
            if sign=='<':
                return node_sign(tree.right, key)
            else:
                return node_sign(tree.left, key)

        def next_child(sign, tree):
            if sign=='<':
                return tree.right
            else:
                return tree.left

        def get_queue(sign, lq, rq):
            if sign=='<': return lq
            else: return rq

        def cut_unknown_child(sign, tree):
            if sign=='<':
                res = tree.right
                tree.right = None
            else:
                res = tree.left
                tree.left = None
            return res

        #code starts here
        if not tree:
            return

        ptr = tree
        sign = node_sign(tree, key)

        while True:
            if not ptr:
                break
            nc = next_child(sign, ptr)
            if not nc:
                break
            if sign != child_sign(sign, ptr, key):
                break
            ptr = nc
        
        q = get_queue(sign, lq, rq)
        q.append(tree)
        c = cut_unknown_child(sign, ptr)

        cls.__split(cls, c, key, lq, rq)


############
### TEST ###
############

class TreapTestUtil(unittest.TestCase):
    def make_tree2(self, values):
        '''values are in order of priority '''
        return Treap.ify(Treap, [Treap(priority=-p, val=v) for p,v in enumerate(values)])

    def assertTerminal(self, tree):
        self.assertEqual(tree.left, None)
        self.assertEqual(tree.right, None)

    def assertAllTerminals(self, trees):
        for tree in trees:
            self.assertTerminal(tree)

    def assertChildren(self, node, left_val, val, right_val):
        self.assertEqual(node.val, val)

        if not left_val:
            self.assertEqual(node.left, None)
        else:
            self.assertEqual(node.left.val, left_val)

        if not right_val:
            self.assertEqual(node.right, None)
        else:
            self.assertEqual(node.right.val, right_val)

    def verifyTreap(self, tree, values=None):
        self.verify_heapness(tree)
        self.verify_BTSness(tree)
        if values:
            self.verify_values(tree, values)
        self.assertEqual(tree.size2(), len(values))
        self.assertEqual(tree.size(), len(values))

    def verify_heapness(self, tree):
        if not tree:
            return
        if tree.left:
            assert tree.priority >= tree.left.priority, "%s > %s" %(tree.priority, tree.left.priority)
            self.verify_heapness(tree.left)
        if tree.right:
            assert tree.priority >= tree.right.priority
            self.verify_heapness(tree.right)

    def verify_BTSness(self, tree):
        #if not tree:
        #    return

        #res = []
        #stack = [tree]
        #while stack:
        #    top = stack.pop(-1)
        #    if isinstance(top, Treap):
        #        if top.right:
        #            stack.append(top.right)
        #        stack.append(top.val)
        #        if top.left:
        #            stack.append(top.left)
        #    else:
        #        res.append(top)
        #
        #for a,b in zip(res[:-1], res[1:]):
        #    assert a<b, "assert %s < %s" % (a,b)

        largest = None
        for node in tree.iter_inorder():
            if largest:
                assert largest < node.val, "%s !< %s" %(largest, node.val)
            largest = node.val

    def verify_values(self, tree, values):
        '''verify that sorted(sorted_tree_values) == sorted(values)'''
        if not tree:
            assert len(values)==0, "tree should NOT be empty"

        node_cnt = 0
        for node in tree:
            assert node.val in values
            node_cnt += 1
        assert node_cnt == len(values)

        #nodes = [tree]
        #while nodes:
        #    node = nodes.pop(0)
        #    if node.left: nodes.append(node.left)
        #    if node.right: nodes.append(node.right)
        #    assert node.val in values, "%s in %s" %(node.val, values)
        #    values.remove(node.val)

        #assert len(values)==0, "leftover %s" % values

class MakeTreapTest(TreapTestUtil):
    def test_treapify_skewed_to_the_right(self):
        tree = self.make_tree2([80,90,100])
        
        self.assertChildren(tree, None, 80, 90)
        self.assertChildren(tree.right, None, 90, 100)
        self.assertTerminal(tree.right.right)

    def test_make_treap_balanced(self):
        tree = self.make_tree2([5,4,6])
        self.assertChildren(tree, 4,5,6)

class DeleteTopTreapTest(TreapTestUtil):
    def test_delete_tree_with_one_left_child_should_return_the_child_as_new_root(self):
        tree = self.make_tree2([10,5])
        new_tree = tree.delete_top()
        self.assertChildren(new_tree, None, 5, None)

    def test_delete_tree_with_one_right_child_should_return_the_child_as_new_root(self):
        tree = self.make_tree2([5,10])
        new_tree = tree.delete_top()

        self.assertChildren(new_tree, None, 10, None)

    def test_delete_root_once_should_return_new_root(self):
        balance_tree = self.make_tree2([5,4,6])
        new_tree = balance_tree.delete_top()

        self.assertChildren(new_tree, None, 4, 6)

    def test_delete_tree_with_3height_1(self):
        values = [100,200,50,250,150,75,25]
        depth_2_tree = self.make_tree2(values)

        new_tree = depth_2_tree.delete_top()

        self.verifyTreap(new_tree, values[1:])
    
    def test_delete_tree_with_3height_2(self):
        values = [100,50,200,25,75,150,250]
        depth_2_tree = self.make_tree2(values)
        new_tree = depth_2_tree.delete_top()

        self.verifyTreap(new_tree, values[1:])
    
class DeleteValTreapTest(TreapTestUtil):
    def test_delete_only_one_node_should_return_None(self):
        one_node = self.make_tree2([1])
        new_tree = one_node.delete_val(1)

        self.assertEqual(new_tree, None)

    def test_delete_non_existent_value_should_remain_the_same(self):
        one_node = self.make_tree2([1])
        new_tree = one_node.delete_val(9999)

        self.verifyTreap(new_tree, [1])

    def test_delete_left_leap_node(self):
        values = [100, 50]
        tree = self.make_tree2(values)

        assert tree.size() == 2
        assert 50 in [n.val for n in tree]
        assert 100 in [n.val for n in tree]

        tree = tree.delete_val(50)

        assert tree.size() == 1
        assert tree.val == 100
        assert 100 in [n.val for n in tree]
        assert 50 not in [n.val for n in tree]

    def test_delete_right_leap_node(self):
        values = [100, 200]
        tree = self.make_tree2(values)

        assert tree.size() == 2
        assert 100 in [n.val for n in tree]
        assert 200 in [n.val for n in tree]

        tree = tree.delete_val(200)

        assert tree.val == 100
        assert tree.size() == 1
        assert 100 in [n.val for n in tree]
        assert 200 not in [n.val for n in tree]

    def test_delete_left_bottom_terminal_node(self):
        depth_2_tree = self.make_tree2([100, 50, 200, 25, 75, 150, 250])

        t = depth_2_tree.delete_val(25)
        self.verifyTreap(t, [100, 50, 200, 75, 150, 250])

    def test_delete_left_first_child(self):
        depth_2_tree = self.make_tree2([100, 50, 200, 25, 75, 150, 250])
        t = depth_2_tree.delete_val(50)

        self.verifyTreap(t, [100, 200, 25, 75, 150, 250])

    def test_delete_top_most_node(self):
        values = [100, 50, 200, 25, 75, 150, 250]
        depth_2_tree = self.make_tree2(values)
        new_tree = depth_2_tree.delete_val(100)

        self.verifyTreap(new_tree, values[1:])

    def test_delete_top_nodes_one_by_one(self):
        values = [100, 50, 200, 25, 75, 150, 250]
        tree = self.make_tree2(values)

        tree = self.verifyAfterDeleteVal(tree, remove=100, top=50)
        tree = self.verifyAfterDeleteVal(tree, remove=50, top=200)
        tree = self.verifyAfterDeleteVal(tree, remove=200, top=25)
        tree = self.verifyAfterDeleteVal(tree, remove=25, top=75)
        tree = self.verifyAfterDeleteVal(tree, remove=75, top=150)
        tree = self.verifyAfterDeleteVal(tree, remove=150, top=250)
        assert tree.size() == 1

    def test_delete_leap_nodes_one_by_one(self):
        values = [100, 50, 200, 25, 75, 150, 250]
        tree = self.make_tree2(values)

        tree = self.verifyAfterDeleteVal(tree, remove=250, top=100)
        tree = self.verifyAfterDeleteVal(tree, remove=150, top=100)
        tree = self.verifyAfterDeleteVal(tree, remove=200, top=100)
        tree = self.verifyAfterDeleteVal(tree, remove=25, top=100)
        tree = self.verifyAfterDeleteVal(tree, remove=75, top=100)
        tree = self.verifyAfterDeleteVal(tree, remove=50, top=100)
        assert tree.size() == 1

    def verifyAfterDeleteVal(self, tree, remove, top):
        values_in_tree = set(node.val for node in tree)
        tree = tree.delete_val(remove)
        self.verifyTreap(tree, values_in_tree - {remove})
        assert tree.val == top, "%s == %s" %(tree.val, top)
        return tree

    def test_randomly_deleting_val_from_tree_should_keep_treapness(self):
        size = 100

        values = list(range(size))
        values_in_deleting_order = values[:]
        
        shuffle(values)
        shuffle(values_in_deleting_order)

        tree = self.make_tree2(values)
        self.verifyTreap(tree, values)

        while len(values_in_deleting_order) > 0:
            v = values_in_deleting_order.pop(0)
            tree = tree.delete_val(v)
            if tree:
                assert tree.size() == len(values_in_deleting_order),\
                    "%s == %s" %(tree.size(), len(values_in_deleting_order))
                self.verifyTreap(tree, values_in_deleting_order)

        assert len(values_in_deleting_order) == 0,\
                "len is %s" %(len(values_in_deleting_order))

class TreapAddTest(TreapTestUtil):
    def test_simple_add1(self):
        t = self.make_tree2([1])
        n = Treap(-999, 999)
        nt = Treap.add(Treap, t, n)
        
        self.assertChildren(nt, None, 1, 999)

        self.verifyTreap(nt, [1, 999])

    def test_simple_add2(self):
        t = self.make_tree2([1])
        n = Treap(-999, -999)
        nt = Treap.add(Treap, t, n)
        
        self.verifyTreap(nt, [-999, 1])

    def test_simple_add3(self):
        t = self.make_tree2([1])
        n = Treap(999, 999)
        nt = Treap.add(Treap, t, n)
        
        self.verifyTreap(nt, [1, 999])

    def test_complex_add1(self):
        t = self.make_tree2([5,3,7,2,4,6,8])
        n = Treap(999, 999)
        nt = Treap.add(Treap, t, n)
        
        self.verifyTreap(nt, [999, 5, 3, 7, 2, 4, 6, 8])

    def test_add_size_error(self):
        t = self.make_tree2([1,3])
        n = Treap(33, 2)
        nt = Treap.add(Treap, t, n)

        #print("print inorder", )
        #nt.print_inorder()
        self.assertChildren(nt, 1,2,3)
        self.assertAllTerminals([nt.left, nt.right])
        #self.assertEqual(nt.size(), 3)
        self.assertEqual(nt.left.size(), 1)
        self.assertEqual(nt.right.size(), 1)
        #self.verifyTreap(nt, [1,2,3])

    def test_complex_add2(self):
        t = self.make_tree2([5,3,7,2,4,6,8888])
        n = Treap(999, 999)
        nt = Treap.add(Treap, t, n)

        self.verifyTreap(nt, [5,3,7,2,4,6,8888,999])

    def test_randomly_adding_nodes_should_keep_treapiness(self):
        size = 200
        half = int(size/2)
        values = list(range(size))
        shuffle(values)

        tree = self.make_tree2(values[:half])
        self.verifyTreap(tree, values[:half])

        self.assertEqual(tree.size(), half)

        for i in range(half, size):
            n = Treap(randint(-size, 0), values[i])
            tree = Treap.add(Treap, tree, n)
            self.verifyTreap(tree, values[:i+1])

        self.assertEqual(tree.size(), tree.size2())
        #test #delete me later
        cnt = 0
        for node in tree:
            cnt +=1
        self.assertEqual(cnt, 200)
        self.assertEqual(tree.size2(), size)
        self.verifyTreap(tree, values)

class SplitTest(TreapTestUtil):
    def assert_sanity_queues_by_key(self, key, lq, rq):
        def debug_assert_lq_is_all_lesser(key, lq):
            for each_tree in lq:
                for each_node in iter(each_tree):
                    assert each_node.val <= key

        def debug_assert_rq_is_all_greater(key, rq):
            for each_tree in rq:
                for each_node in iter(each_tree):
                    assert key <= each_node.val

        debug_assert_lq_is_all_lesser(key, lq)
        debug_assert_rq_is_all_greater(key, rq)

    def test_split_one_node_1(self):
        tree = self.make_tree2([9])
        split_key = 5
        lq, rq = tree.split(split_key)

        self.assertEqual(len(lq), 0)
        self.assertEqual(len(rq), 1)

        self.assert_sanity_queues_by_key(split_key, lq, rq)

    def test_split_one_node_2(self):
        tree = self.make_tree2([1])
        split_key = 5
        lq, rq = tree.split(split_key)

        self.assertEqual(len(lq), 1)
        self.assertEqual(len(rq), 0)

        self.assert_sanity_queues_by_key(split_key, lq, rq)

    def test_split_None_should_return_None(self):
        lq, rq = [], []
        tree = self.make_tree2([5,1,9])
        split_key = 6
        lq, rq = tree.split(split_key)

        self.assertEqual(len(lq), 1)
        self.assertEqual(len(rq), 1)
        self.assert_sanity_queues_by_key(split_key, lq, rq)

        lesser = lq.pop()
        greater = rq.pop()

        self.assertEqual(lesser.val, 5)
        self.assertEqual(lesser.left.val, 1)
        self.assertEqual(greater.val, 9)

    def test_split_complex(self):
        lq, rq = [], []
        tree = self.make_tree2([50, 10, 70, 60, 66, 100, 110, 71, 78])

        split_key = 75
        lq, rq = tree.split(split_key)

        self.assertEqual(len(lq), 2)
        self.assertEqual(len(rq), 2)
        self.assert_sanity_queues_by_key(split_key, lq, rq)

class IterTest(TreapTestUtil):
    def test_recursive_iter(self):
        t = self.make_tree2([2,1,3,4,5])
        for n in t:
            assert n.val in [2,1,3,4,5]

class DepthTest(TreapTestUtil):
    def make_random_tree(self, size):
        values = list(range(1, size+1))
        shuffle(values)
        return Treap.ify(Treap, [Treap(-p,v) for p,v in enumerate(values)])

    def test_depth_should_be_about_2_3rd_of_N(self):
        size = 5000
        tree = self.make_random_tree(size)
        self.assertDepthAlmostLog(tree)

    def test_deleting_random_node_should_keep_logarithmic_height(self):
        size = 5000
        tree = self.make_random_tree(size)
        vals = list(range(1,size+1))
        shuffle(vals)

        self.assertDepthAlmostLog(tree)
        for del_me in vals[:10]:
            tree = tree.delete_val(del_me)
            self.assertDepthAlmostLog(tree)
            
    def assertDepthAlmostLog(self, tree):
        from math import log
        depth = tree.measure_depth()
        size = tree.size()
        theoretical_depth = log(size, 1.5)
        self.assertAlmostEqual(theoretical_depth, depth, delta=size*0.01)

class TreapSizeTest(TreapTestUtil):
    def test_size(self):
        for vals in ([1], [1,2], [2,1], [1,2,3], [2,1,3], [3,2,1]):
            tree = self.make_tree2(vals)
            self.assertEqual(tree.size(), len(vals))

class TreapIterPreorderTest(TreapTestUtil):
    def test_preorder(self):
        values = list(range(10))
        shuffle(values)
        tree = self.make_tree2(values)
        #tree.print_inorder()
        self.verifyTreap(tree, values)

class FindTreapsTest(TreapTestUtil):
    def test_find_value(self):
        tree = self.make_tree2([3,4,1,2])

        self.assertTrue(tree.find(3))
        self.assertTrue(tree.find(4))
        self.assertTrue(tree.find(1))
        self.assertTrue(tree.find(2))

        self.assertFalse(tree.find(0))
        self.assertFalse(tree.find(5))
        self.assertFalse(tree.find(10))

class TreapSizeTestUtil(TreapTestUtil):
    def treeSizeEqual(self, tree, size):
        self.assertEqual(tree.size2(), size)

    def assertTreapSize2Updated(self, tree):
        for node in tree:
            self.assertEqual(node.size(), node.size2())

class SizeTreapifyTest(TreapSizeTestUtil):
    def test_one_node(self):
        tree = self.make_tree2([1])
        
        self.treeSizeEqual(tree, 1)

    def test_two_node(self):
        self.treeSizeEqual(self.make_tree2([1,2]), 2)
        self.treeSizeEqual(self.make_tree2([2,1]), 2)

    def test_triangle(self):
        self.treeSizeEqual(self.make_tree2([1,2,3]), 3)
        self.treeSizeEqual(self.make_tree2([1,3,2]), 3)
        self.treeSizeEqual(self.make_tree2([2,1,3]), 3)
        self.treeSizeEqual(self.make_tree2([3,1,2]), 3)
        self.treeSizeEqual(self.make_tree2([3,2,1]), 3)

class SizeTreapDeleteTest(TreapSizeTestUtil, unittest.TestCase):
    def assertTreeDeleteUpdateSize(self, tree_vals, del_val):
        tree_vals_size = len(tree_vals)

        tree = self.make_tree2(tree_vals)
        tree = tree.delete_val(del_val)

        for node in tree:
            self.assertEqual(node.size(), node.size2())

        self.assertEqual(tree.size2(), tree_vals_size-1)

        return tree

    def test_del_one_leaf(self):
        self.assertTreeDeleteUpdateSize([1,2], 2)
        self.assertTreeDeleteUpdateSize([2,1], 1)

    def test_del_root(self):
        self.assertTreeDeleteUpdateSize([1,2], 1)
        self.assertTreeDeleteUpdateSize([2,1], 2)

    def test_del_random(self):
        size = 50
        for i in range(10):
            vals = list(range(size))
            shuffle(vals)
            tree = self.make_tree2(vals)
            shuffle(vals)
            for v in vals[:-1]:
                tree = tree.delete_val(v)
                self.assertTreapSize2Updated(tree)

class SizeTreapAddTest(TreapSizeTestUtil, unittest.TestCase):
    def make_tree_by_add(self, vals):
        assert vals
        
        tree = Treap(0, vals[0])
        for p,v in enumerate(vals[1:], 1):
            node = Treap(-p, v)
            tree = Treap.add(Treap, tree, node)
            
        return tree

    def assertTreapAddUpdateSize(self, vals):
        tree = self.make_tree_by_add(vals)
        self.assertEqual(tree.size(), len(vals))
        self.assertEqual(tree.size2(), len(vals))
        self.assertTreapSize2Updated(tree)

    def test_two_node(self):
        self.assertTreapAddUpdateSize([1,2])
        self.assertTreapAddUpdateSize([2,1])

    def test_triangle(self):
        self.assertTreapAddUpdateSize([1,2,3])
        self.assertTreapAddUpdateSize([1,3,2])
        self.assertTreapAddUpdateSize([2,1,3])
        self.assertTreapAddUpdateSize([3,1,2])
        self.assertTreapAddUpdateSize([3,2,1])

class ReduceLQTest(TreapTestUtil):
    def test_reduce_lq_one(self):
        tree = Treap(0, 0)
        left_child = tree.reduce_lq([tree])
        self.assertTerminal(left_child)
        self.assertEqual(left_child.size(), 1)

    def test_reduce_lq_two(self):
        node1 = Treap(0, 0)
        node2 = Treap(-1, 1)
        tree = node1.reduce_lq([node1, node2])
        self.assertChildren(tree, None, 0, 1)
        self.assertTerminal(tree.right)
        self.assertEqual(tree.size(), 2)
        self.assertEqual(tree.right.size(), 1)

class SplitAndMergeIssueReproductionTest(TreapTestUtil):
    def test_split_and_merge_issue_reproduction(self):
        tree = self.make_tree2([1,3])
        left_child, right_child = tree.split_and_merge(2)
        
        self.assertChildren(left_child, None, 1, None)
        self.assertTerminal(left_child)
        self.assertEqual(left_child.size(), 1)

        self.assertChildren(right_child, None, 3, None)
        self.assertTerminal(right_child)
        self.assertEqual(right_child.size(), 1)

    def test_reduce_lq_issue_reproduction(self):
        tree = self.make_tree2([1,3])
        lq, _ = tree.split(2)
        left_child = tree.reduce_lq(lq)

        self.assertChildren(left_child, None, 1, None)
        self.assertEqual(left_child.size(), 1)
        self.assertTerminal(left_child)

    def test_reduce_rq_issue_reproduction(self):
        tree = self.make_tree2([3,1])
        _, rq = tree.split(2)
        right_child = tree.reduce_rq(rq)

        self.assertChildren(right_child, None, 3, None)
        self.assertEqual(right_child.size(), 1)
        self.assertTerminal(right_child)

class TreapFindKthNode(TreapTestUtil):
    def test_tree_size1_0th(self):
        tree = self.make_tree2([1])
        self.assertEqual(tree.k_th(0), tree)

    def test_tree_size1_1st(self):
        tree = self.make_tree2([1])
        with self.assertRaises(AssertionError):
            tree.k_th(1)
        
    def test_tree_size3(self):
        tree = self.make_tree2([2,1,3])
        self.assertEqual(tree.k_th(0).val, 1)
        self.assertEqual(tree.k_th(1).val, 2)
        self.assertEqual(tree.k_th(2).val, 3)
        with self.assertRaises(AssertionError):
            tree.k_th(5)

    def test_tree_random_kth(self):
        test_count = 20
        size = 20
        for _ in range(test_count):
            vals = list(range(size))
            shuffle(vals)
            tree = self.make_tree2(vals)
            for k in range(len(vals)):
                node = tree.k_th(k)
                self.assertEqual(node.val, k)

            with self.assertRaises(AssertionError):
                tree.k_th(size*10)

class TreapCountLessThanTest(TreapTestUtil):
    def assertCountLessThan(self, vals, key, cnt):
        tree = self.make_tree2(vals)
        self.assertEqual(tree.count_less_than(key), cnt)

    def test_hard_cases(self):
        self.assertCountLessThan([3], 1, 0)
        self.assertCountLessThan([3], 5, 1)

        self.assertCountLessThan([3,1,5], 2, 1)
        self.assertCountLessThan([3,1,5], 3, 1)
        self.assertCountLessThan([3,1,5], 4, 2)

    def test_random_cases(self):
        test_count = 20
        size = 20
        for _ in range(test_count):
            vals = list(range(size))
            shuffle(vals)
            tree = self.make_tree2(vals)
            for x in range(-100,0):
                self.assertEqual(tree.count_less_than(x), 0)
            for x in range(size):
                self.assertEqual(tree.count_less_than(x), x)
            for x in range(size, size*2):
                self.assertEqual(tree.count_less_than(x), size)

class MakeTreapTest(TreapTestUtil):
    def test_maketreap(self):
        tree = Treap.make_treap(Treap, [1,2,3])
        self.verifyTreap(tree, [1,2,3])

if __name__=="__main__":
    unittest.main()
