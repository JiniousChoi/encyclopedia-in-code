#!/usr/bin/env python3

import unittest

def wildcard(pat, word):
    #most specific basis
    if pat=='*' and word=='':
        return True

    #general basis
    if pat=='' and word=='':
        return True
    if pat!='' and word=='':
        return False
    if pat=='' and word!='':
        return False

    #recursive logic
    if pat[0]=='?':
        return wildcard(pat[1:], word[1:])
    if pat[0]=='*':
        return wildcard(pat[1:], word) or wildcard(pat, word[1:])
    else:
        return pat[0]==word[0] and wildcard(pat[1:], word[1:])
    

class WildcardTest(unittest.TestCase):
    def test_boundary1(self):
        self.assertTrue(wildcard("", ""))
        self.assertFalse(wildcard("", "a"))
        self.assertFalse(wildcard("a", ""))
        res = wildcard('*', '')

    def test_no_wildcard(self):
        self.assertTrue(wildcard("abc", "abc"))
        self.assertFalse(wildcard("abc", "a"))

    def test_questionmark_1(self):
        self.assertTrue(wildcard("he?p", "help"))
        self.assertTrue(wildcard("h??p", "help"))
        self.assertFalse(wildcard("h??p", "hell"))

    def test_asterisk_1(self):
        self.assertTrue(wildcard("h*", "h"))
        self.assertTrue(wildcard("h*p", "help"))
        self.assertFalse(wildcard("h*p", "hell"))
        self.assertTrue(wildcard("h**p", "help"))
        self.assertTrue(wildcard("h**p", "hep"))
        self.assertTrue(wildcard("h**p", "hp"))

    def test_complex_1(self):
        self.assertTrue(wildcard("*nsung choi", "jinsung choi"))
        self.assertTrue(wildcard("*nsung?choi", "jinsung choi"))
        self.assertTrue(wildcard("*e*p m?", "help me"))

if __name__=="__main__":
    unittest.main()
