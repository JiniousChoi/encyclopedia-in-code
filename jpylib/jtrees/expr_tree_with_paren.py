#!/usr/bin/python3
## author: jinchoiseoul@gmail.com


from . import TreeNode as Tree
from . import traverse_in_order, traverse_post_order


def join_in_order(tree):
    return ''.join([str(n.val) for n in traverse_in_order(tree)])


def join_post_order(tree):
    return ''.join([str(n.val) for n in traverse_post_order(tree)])


operators = ['+', '-', '*', '/']


def expression_tree(expression):
    if len(expression) == 1:
        assert expression not in operators
        return Tree(expression)

    plus_idx = find_plus_in_expr(expression)
    if plus_idx >= 0:
        idx = plus_idx
        left = expression_tree(expression[:idx])
        right = expression_tree(expression[idx+1:])
        root = Tree('+')
        root.left = left
        root.right = right
        return root

    multiple_idx = find_multiple_in_expr(expression)
    if multiple_idx>= 0:
        idx = multiple_idx
        left = expression_tree(expression[:idx])
        right = expression_tree(expression[idx+1:])
        root = Tree('*')
        root.left = left
        root.right = right
        return root
    
    if '(' in expression:
        opening_idx, closing_idx = find_paren_idx(expression)
        expr_in_paren = expression[opening_idx+1:closing_idx]
        return expression_tree(expr_in_paren)
    
    #not reachable
    assert false


def find_plus_in_expr(expr):
    open_paren_cnt = 0
    for i,c in enumerate(expr):
        if c == '(':
            open_paren_cnt += 1
        elif c == ')':
            open_paren_cnt -= 1
        elif c == '+' and open_paren_cnt == 0:
            return i
    return -1 


def find_multiple_in_expr(expr):
    open_paren_cnt = 0
    for i,c in enumerate(reversed(expr)):
        if c == '(':
            open_paren_cnt += 1
        elif c == ')':
            open_paren_cnt -= 1
        elif c == '*' and open_paren_cnt == 0:
            return len(expr)-i-1
    return -1 


def find_paren_idx(expression):
    open_paren_cnt = 0
    result = []
    for i,c in enumerate(expression):
        if c == '(':
            open_paren_cnt += 1
            result.append(i)
        elif c == ')':
            open_paren_cnt -= 1
            if open_paren_cnt == 0:
                result.append(i)
                return result #[x,y]
    #not reachable
    if open_paren_cnt != 0:
        assert False, "not paired parentheses"
    
    assert False


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
        self.assertEqual(expression, join_in_order(root))

    def test_plus2(self):
        expression = '1+2+3'
        root = expression_tree(expression)
        self.assertEqual(expression, join_in_order(root))

    def test_multiply1(self):
        expression = '1*2'
        root = expression_tree(expression)
        self.assertEqual(expression, join_in_order(root))

    def test_multiply2(self):
        expression = '1*2*3'
        root = expression_tree(expression)
        self.assertEqual(expression, join_in_order(root))

    def test_all_in_one1(self):
        expression = '1+2*3'
        root = expression_tree(expression)
        self.assertEqual(expression, join_in_order(root))

    def test_all_in_one2(self):
        expression = '1*2+3'
        root = expression_tree(expression)
        self.assertEqual(expression, join_in_order(root))

    def test_all_in_one3(self):
        expression = '1*2+4+3*1'
        root = expression_tree(expression)
        self.assertEqual(expression, join_in_order(root))

    def test_parentheses_boundary1(self):
        expression = '(1)'
        root = expression_tree(expression)
        result = join_in_order(root)
        self.assertEqual(result, '1')

    def test_parentheses_plus1(self):
        expression = '(1+2)'
        root = expression_tree(expression)
        result = join_in_order(root)
        self.assertEqual(result, '1+2')

    def test_parentheses_multiply1(self):
        expression = '(1*2)'
        root = expression_tree(expression)
        result = join_in_order(root)
        self.assertEqual(result, '1*2')

    def test_parentheses_combi1(self):
        expression = '(1*2)+3'
        root = expression_tree(expression)

        result = join_in_order(root)
        self.assertEqual(result, '1*2+3')

        result2 = join_post_order(root)
        self.assertEqual(result2, '12*3+')

    def test_parentheses_combi2(self):
        expression = '(1+2)*3'
        root = expression_tree(expression)

        result = join_in_order(root)
        self.assertEqual(result, '1+2*3')

        result2 = join_post_order(root)
        self.assertEqual(result2, '12+3*')

    def test_parentheses_combi3(self):
        expression = '1+2*3*(4+5)+6'
        root = expression_tree(expression)

        result = join_in_order(root)
        self.assertEqual(result, '1+2*3*4+5+6')

        result2 = join_post_order(root)
        self.assertEqual(result2, '123*45+*6++')

    def test_parentheses_combi4(self):
        expression = '1+2*3*4+5+6'
        root = expression_tree(expression)

        result = join_in_order(root)
        self.assertEqual(result, '1+2*3*4+5+6')

        result2 = join_post_order(root)
        self.assertEqual(result2, '123*4*56+++')


if __name__=='__main__':
    unittest.main()
