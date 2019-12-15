#!/usr/bin/env python3

import unittest

def brackets2(brackets):
    length = len(brackets)
    if(length==0 or length%2==1):
        return False
    stack = []
    for b in brackets:
        if is_opening(b):
            stack.append(b)
        else:
            opening = stack.pop(-1)
            closing = b
            if not is_pair(opening, closing):
                return False

    return len(stack)==0

def is_opening(b):
    if b in '([{':
        return True
    return False

def is_pair(opening, closing):
    return '([{'.index(opening) == ')]}'.index(closing)

class BracketsTest(unittest.TestCase):
    def assertMatches(self, brackets, res):
        self.assertEqual(brackets2(brackets), res)

    def test_samples(self):
        self.assertMatches('', False)
        self.assertMatches('()()', True)
        self.assertMatches('({[}])', False)
        self.assertMatches('({}[(){}])', True)


if __name__=="__main__":
    unittest.main()
