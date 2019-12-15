#!/usr/bin/python3
## author: jinchoiseoul@gmail.com


from jpylib.jtrees import tree_builder


class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def lca(self, root, val1, val2):
        s1, s2 = [], []
        tracking_stack(root, val1, s1)
        tracking_stack(root, val2, s2)
        return lca_from_stacks(s1, s2)
        
        
def tracking_stack(root, val, stack):
    if not root:
        return False
        
    stack.append(root)
    
    if root.val == val:
        return True
    elif tracking_stack(root.left, val, stack):
        return True
    elif tracking_stack(root.right, val, stack):
        return True
    
    stack.pop(-1)
    return False


def lca_from_stacks(s1, s2):
    if not s1 or not s2:
        return -1
    i = 0
    while i < min(len(s1), len(s2)) and s1[i] == s2[i]:
        i += 1
        
    return s1[i-1].val


if __name__ == "__main__":

    import unittest

    class SolutionTest(unittest.TestCase):
        def setUp(self):
            self.tree = tree_builder([3,5,1,6,2,0,8,-1,-1,7,4], nil=-1)

        def test_basics(self):
            sol, tree = Solution(), self.tree
            self.assertEqual(sol.lca(tree, 5, 1), 3)
            self.assertEqual(sol.lca(tree, 5, 4), 5)
            self.assertEqual(sol.lca(tree, 5, 99), -1)
            self.assertEqual(sol.lca(tree, 99, 5), -1)
            self.assertEqual(sol.lca(tree, 99, 99), -1)

    unittest.main()
