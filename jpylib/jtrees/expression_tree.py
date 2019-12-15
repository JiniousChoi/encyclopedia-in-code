#!/usr/bin/python3
## author: jinchoiseoul@gmail.com


from . import TreeNode as Tree


def traverse_in_order(tree):
    '''returns string'''
    result = ''
    if tree.left:
        result += traverse_in_order(tree.left)

    result += tree.val

    if tree.right:
        result += traverse_in_order(tree.right)
    
    return result

operators = ['+', '-', '*', '/']

def expression_tree(expression):
    if len(expression) == 1:
        assert expression not in operators
        return Tree(expression)
    
    if '+' in expression:
        idx = expression.find('+')
        left = expression_tree(expression[:idx])
        right = expression_tree(expression[idx+1:])
        root = Tree('+')
        root.left = left
        root.right = right
        return root

    if '*' in expression:
        idx = expression.rfind('*')
        left = expression_tree(expression[:idx])
        right = expression_tree(expression[idx+1:])
        root = Tree('*')
        root.left = left
        root.right = right
        return root
    
    assert false


import unittest


class ExpressionTreeTest(unittest.TestCase):

    def test_boundary1(self):
        expression = '1'
        rootNode = expression_tree(expression)
        self.assertEqual(rootNode.val, '1')
        self.assertEqual(rootNode.left, None)
        self.assertEqual(rootNode.right, None)

    def test_plus1(self):
        expression = '1+2'
        root = expression_tree(expression)
        self.assertEqual(expression, traverse_in_order(root))

    def test_plus2(self):
        expression = '1+2+3'
        root = expression_tree(expression)
        self.assertEqual(expression, traverse_in_order(root))

    def test_multiply1(self):
        expression = '1*2'
        root = expression_tree(expression)
        self.assertEqual(expression, traverse_in_order(root))

    def test_multiply2(self):
        expression = '1*2*3'
        root = expression_tree(expression)
        self.assertEqual(expression, traverse_in_order(root))

    def test_all_in_one1(self):
        expression = '1+2*3'
        root = expression_tree(expression)
        self.assertEqual(expression, traverse_in_order(root))

    def test_all_in_one2(self):
        expression = '1*2+3'
        root = expression_tree(expression)
        self.assertEqual(expression, traverse_in_order(root))

    def test_all_in_one3(self):
        expression = '1*2+4+3*1'
        root = expression_tree(expression)
        self.assertEqual(expression, traverse_in_order(root))

    def test_traverse_in_order1(self):
        root = Tree('1')
        result = traverse_in_order(root)
        self.assertEqual(result, '1')

    def test_traverse_in_order2(self):
        root = Tree('-')
        root.left = Tree('1')
        root.right = Tree('3')
        result = traverse_in_order(root)
        self.assertEqual(result, '1-3')


if __name__=='__main__':
    unittest.main()
