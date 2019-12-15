#!/usr/bin/python3
## author: jinchoiseoul@gmail.com


class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0
        n = len(A)
        i = n-1
        while i>=1:
            if A[i] == A[i-1]:
                A.pop(i)
                n -= 1
            i -= 1
        return n
        
    def removeDuplicatesReverseward(self, A):
        ''' this is too slow '''
        if not A:
            return 0
        n = len(A)
        i = 0
        while i < n-1:
            if A[i] == A[i+1]:
                n -= 1
                A.pop(i)
            else:
                i += 1
        return n


if __name__ == "__main__":
    
    import unittest

    class SolutionTest(unittest.TestCase):

        def test_basics(self):
            before, after = [], []
            self.assertDuplicatesRemoved(before, after)

            before, after = [1,2,2], [1,2]
            self.assertDuplicatesRemoved(before, after)

            before, after = [1,2,3,4,4,4,5,6,6,6,7], [1,2,3,4,5,6,7]
            self.assertDuplicatesRemoved(before, after)

        def assertDuplicatesRemoved(self, before, after):
            sol = Solution()
            methods_on_test = [sol.removeDuplicates, sol.removeDuplicatesReverseward]
            for method in methods_on_test:
                self.assertEqual(method(before), len(after))
                self.assertEqual(before, after)


    unittest.main()
