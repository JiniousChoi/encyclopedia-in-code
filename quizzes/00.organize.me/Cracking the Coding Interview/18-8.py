#!/usr/bin/env python3
''' 문자열 s와 s보다 짧은 길이를 갖는 문자열의 배열인 T가 주어졌을 때,
T에 있는 각 문자열을 s에서 찾는 메서드를 작성하라.'''

import unittest

class TreeRoot:
    def __init__(self, s):
        self.root = SuffixTreeNode()
        root = self.root
        for i in range(len(s)):
            root.insertString(s[i:], i)
    
    def search(self, s):
        return self.root.search(s)

class SuffixTreeNode:
    def __init__(self):
        self.indexes = []
        #self.value는 self.children의 key로 존재한다.
        self.children = {}

    def insertString(self, s, i):
        ''' build a sub-tree(children) for characters of `s`
            i indicates starting index of sub-string `s` in original string `s` '''
        if not s:
            return

        first = s[0]
        remainder = s[1:]

        if first not in self.children:
            child = SuffixTreeNode()
            self.children[first] = child

        child = self.children[first]
        child.indexes.append(i)
        child.insertString(remainder, i)

    def search(self, s):
        ''' follow through sub-nodes for `s` path.
            Return indexes of the path if there was.
            Otherwise, None'''
        #invariant: there is a path in the tree so far.
        if not s:
            return self.indexes

        first = s[0]
        remainder = s[1:]

        if first in self.children:
            return self.children[first].search(remainder)
        #invariant: Path cuts here.
        return None

    #def search(self, s):
    #    ''' follow through sub-nodes for `s` path.
    #        Return indexes of the path if there was.
    #        Otherwise, None'''
    #    assert s

    #    #invariant: there is a path in the tree so far.
    #    first = s[0]
    #    remainder = s[1:]

    #    if first not in self.children:
    #        return None

    #    child = self.children[first]
    #    if remainder:
    #        return child.search(remainder)
    #    else:
    #        return child.indexes

class SUffixTreeTest(unittest.TestCase):
    def test_sample(self):
        root = TreeRoot("bibs")
        #self.assertEqual(root.search(""), [])
        self.assertEqual(root.search("b"), [0,2])
        self.assertEqual(root.search("bi"), [0])
        self.assertEqual(root.search("bib"), [0])
        self.assertEqual(root.search("bibs"), [0])
        self.assertEqual(root.search("i"), [1])
        self.assertEqual(root.search("ib"), [1])
        self.assertEqual(root.search("ibs"), [1])
        self.assertEqual(root.search("bs"), [2])
        self.assertEqual(root.search("s"), [3])
        self.assertEqual(root.search("not-exist"), None)

if __name__=="__main__":
    unittest.main()
