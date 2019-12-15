#!/usr/bin/env python3
# p190

import unittest

class QuadTree:
    def __init__(self, bwx, one=None, two=None, three=None, four=None):
        self.bwx = bwx
        self.one = one
        self.two = two
        self.three = three
        self.four = four
    
    @classmethod
    def make_tree(cls, msg):
        qtree, _ = cls._make_tree(msg)
        return qtree

    @classmethod
    def _make_tree(cls, msg):
        assert len(msg) > 0
        head, tail0 = msg[0], msg[1:]

        #basis
        if head != 'x':
            return (QuadTree(head), tail0)
        
        else:
            one, tail1 = cls._make_tree(tail0)
            two, tail2 = cls._make_tree(tail1)
            three, tail3 = cls._make_tree(tail2)
            four, tail4 = cls._make_tree(tail3)
            return (QuadTree('x', one, two, three, four), tail4)

    def __str__(self):
        return self.bwx + (str(self.one) if self.one else '') \
                        + (str(self.two) if self.two else '') \
                        + (str(self.three) if self.three else '') \
                        + (str(self.four) if self.four else '')


def flip(qtree):
    ''' change in-place '''
    if qtree and qtree.bwx == 'x':
        flip(qtree.one)
        flip(qtree.two)
        flip(qtree.three)
        flip(qtree.four)

        qtree.three, qtree.four, qtree.one, qtree.two = qtree.one, qtree.two ,qtree.three, qtree.four


class QuadTreeStrTest(unittest.TestCase):

    def test_quadtree1(self):
        qtree = QuadTree.make_tree("w")
        self.assertEqual(str(qtree), 'w')

    def test_quadtree2(self):
        qtree = QuadTree.make_tree("xwwbb")
        self.assertEqual(str(qtree), 'xwwbb')


class QuadtreeFlipTest(unittest.TestCase):
    def assertFlipped(self, inp, out, msg=None):
        qtree = QuadTree.make_tree(inp)
        flip(qtree)
        self.assertEqual(str(qtree), out, msg)

    def test_flip1(self):
        self.assertFlipped("w", "w", "mono color should be identical")

    def test_flip2(self):
        self.assertFlipped("xbwwb", "xwbbw")

    def test_flip3(self):
        self.assertFlipped("xbwxwbbwb", "xxbwwbbbw")

    def test_flip4(self):
        self.assertFlipped("xxwwwbxwxwbbbwwxxxwwbbbwwwwbb", "xxwbxwwxbbwwbwbxwbwwxwwwxbbwb")


if __name__=="__main__":
    unittest.main()
