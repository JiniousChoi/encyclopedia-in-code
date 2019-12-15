#!/usr/bin/python3
## author: jinchoiseoul@gmail.com


class Solution:
    # @param A : string
    # @param B : list of strings
    # @return an integer
    def wordBreak(self, A, B):
        Bdict = self.make_dict(B)
        memo = [None for _ in range(len(A))]
        return 1 if self.is_word_breakable(memo, A, 0, Bdict) else 0
    
    def make_dict(self, B):
        res = {}
        for w in B:
            c = w[0]
            if c not in res:
                res[c] = []
            #assert c in res
            res[c].append(w)
        return res
        
    def is_word_breakable(self, memo, A, i, Bdict):
        ''' @return True if A[i:] is breakable with words in Bdict. False otherwise '''
        #over the hedge
        if i==len(A):
            return True

        #on the hedge
        if memo[i] != None:
            return memo[i]

        c = A[i]
        for w in Bdict.get(c, []):
            if (A[i:i+len(w)]==w) and self.is_word_breakable(memo, A, i+len(w), Bdict):
                memo[i] = True
                return True
        memo[i] = False
        return False
        

import unittest


class SolutionTest(unittest.TestCase):

    def test_basics(self):
        self.assertTrue(Solution().wordBreak("myinterviewtrainer", ["trainer", "my", "interview"]))

        self.assertFalse(Solution().wordBreak("myinterviewtrainer", ["trainer", "my"]))
        self.assertFalse(Solution().wordBreak("myinterviewtrainer", []))


if __name__ == "__main__":

    unittest.main()
