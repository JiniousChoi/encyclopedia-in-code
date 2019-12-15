#!/usr/bin/python3

class Solution:
    # @param A : list of integers
    # @return an integer
    def largestRectangleArea(self, A):
        if not A:
            return 0
        max_area = 0
        n = len(A)
        stack = []
        for i,h in enumerate(A):
            if not stack or stack[-1][1] < h:
                stack.append((i,h))
            elif stack[-1][1] > h:
                while stack and stack[-1][1] >= h:
                    _, h0 = stack.pop(-1)
                    begin0, end0 = stack[-1][0]+1 if stack else 0, i
                    area0 = h0 * (end0-begin0)
                    max_area = max(max_area, area0)
                #assert not stack or stack[-1][1] < h
                stack.append((i,h))
            elif stack[-1][1] == h:
                stack.pop(-1)
                stack.append((i,h))
        
        while stack:
            _,h0 = stack.pop(-1)
            begin0, end0  = stack[-1][0]+1 if stack else 0, n
            area0 = h0 * (end0 - begin0)
            max_area = max(max_area, area0)
        #assert not stack
        return max_area

if __name__ == "__main__":
    import unittest

    class SolutionTest(unittest.TestCase):
        def test_basics(self):
            sol = Solution()
            self.assertEqual(sol.largestRectangleArea([]), 0)
            self.assertEqual(sol.largestRectangleArea([1]), 1)
            self.assertEqual(sol.largestRectangleArea([1,2,3]), 4)
            self.assertEqual(sol.largestRectangleArea([3,2,1]), 4)
            self.assertEqual(sol.largestRectangleArea([2,1,5,6,2,3]), 10)

    unittest.main()
