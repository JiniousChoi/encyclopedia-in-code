from ._nodes import TreeNode, tree_builder

################
# tree samples #
################

''' sample1
 - binary, full, balanced, binary search

 2
/ \
1 3
'''
bst_true1 = tree_full_1to3 = sample1 = tree_builder([2,1,3])


''' 
sample2
 - binary, full, balanced, binary search

     4
    /  \
   2    6
   /\   /\
  1  3 5  7
'''
bst_true2 = tree_full_1to7 = sample2 = tree_builder([4,2,6,1,3,5,7])


''' 
sample3
 - binary, complete, balanced, binary search

     4
    /  \
   2    6
   /\   /
  1  3 5
'''
bst_true3 = tree_compelete_1to6 = sample3 = tree_builder([4,2,6,1,3,5])


''' 
sample4
 - binary, balanced, binary search

     4
    /  \
   2    6
   /\    \
  1  3    7
'''
bst_true4 = tree_no_complete1 = sample4 = tree_builder([4,2,6,1,3,None,7])


''' 
sample5
 - binary, balanced, binary search

     4
    /  \
   2    6
    \    \
     3    7
'''
bst_true5 = tree_no_complete2 = sample5 = tree_builder([4,2,6,None,3,None,7])


''' 
sample6
 - binary, binary search

     4
      \
       6
        \
         7
'''
bst_true6 = tree_no_complete3 = sample6 = tree_builder([4,None,6,None,7])


''' 
sample7
 - binary, balanced

        1
     /      \
    2        3
   /\      /    \
  4  5     6     7
 /\  /\    /\    /\
8 9 10 11 12 13 14 15
'''
bst_false1 = tree_full_1to15 = sample7 = tree_builder([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])


''' 
sample8
 - binary

        1
     /      \
    2        3
    \            
     5            
      \            
       11            
'''
bst_false2 = tree_no_complete4 = sample8 = tree_builder([1,2,3,None,5,None,None,None,11])


import unittest
from ._tests import assertEqualTreeTopologies as assertTreeTopology


class SamplesTest(unittest.TestCase):

    def test_basics(self):
        assertTreeTopology(sample1, [2,1,3], [1,2,3])
        assertTreeTopology(sample2, [4,2,1,3,6,5,7], [1,2,3,4,5,6,7])
        assertTreeTopology(sample3, [4,2,1,3,6,5], [1,2,3,4,5,6])
        assertTreeTopology(sample4, [4,2,1,3,6,7], [1,2,3,4,6,7])
        assertTreeTopology(sample5, [4,2,3,6,7], [2,3,4,6,7])
        assertTreeTopology(sample6, [4,6,7], [4,6,7])
        assertTreeTopology(sample7, [1,2,4,8,9,5,10,11,3,6,12,13,7,14,15], [8,4,9,2,10,5,11,1,12,6,13,3,14,7,15])
        assertTreeTopology(sample8, [1,2,5,11,3], [2,5,11,1,3])


if __name__ == "__main__":
    unittest.main()
