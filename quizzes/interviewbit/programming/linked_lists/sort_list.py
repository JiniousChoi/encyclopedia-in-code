#!/usr/bin/python3

# Definition for singly-linked list.
class ListNode:
   def __init__(self, x):
       self.val = x
       self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def sortList(self, head):
        if head == None:
            return None
        elif head.next == None:
            return head
            
        #nodes count is >= 2
        h1, h2 = self.split(head)
        h1, h2 = map(self.sortList, [h1, h2])
        #invariant: h1 and h2 are sorted
        assert h1 != None
        if h2==None:
            return h1
        
        new_head = None
        assert h2 != None
        if h1.val <= h2.val:
            new_head = h1
            h1 = h1.next
        else:
            new_head = h2
            h2 = h2.next
            
        it = new_head
        while h1 and h2:
            if h1.val <= h2.val:
                it.next = h1
                it = h1
                h1 = h1.next
            else:
                it.next = h2
                it = h2
                h2 = h2.next
        while h1:
            it.next = h1
            it = h1
            h1 = h1.next
        while h2:
            it.next = h2
            it = h2
            h2 = h2.next
        it.next = None
        return new_head
    
    def split(self, head):
        assert head and head.next

        h1, h2 = head, head
        while h2.next and h2.next.next:
            h2 = h2.next.next
            h1 = h1.next

        assert h2 and not h2.next or not h2.next.next
        
        head2 = h1.next
        #NOTE: tail of h1 must not refers to h2
        h1.next = None
        return (head, head2)


    def split_old(self, head):
        #assert nodes count is >= 2
        h1, h2 = head, head
        h1_prev = None
        while True:
            h1_prev, h1 = h1, h1.next
            if h2 != None and h2.next != None and h2.next.next != None:
                h2 = h2.next.next
            else:
                break
        #NOTE: tail of h1 must not refers to h2
        h1_prev.next = None
        return head, h1

if __name__ == "__main__":
    import unittest

    def from_list(A):
        head = None
        it = head
        for a in A:
            node = ListNode(a)
            if not head:
                it = head = node
            else:
                it.next = node
                it = node

        return head

    def to_list(head):
        ls = []
        while head:
            ls.append(head.val)
            head = head.next
        return ls

    class SolutionTest(unittest.TestCase):
        def setUp(self):
            self.sol = Solution()

        def test_split1(self):
            #self.assertSplit([], [], [])
            #self.assertSplit([1], [1], [])
            self.assertSplit([1,2], [1], [2])
            self.assertSplit([1,2,3], [1,2], [3])
            self.assertSplit([1,2,3,4], [1,2], [3,4])
            self.assertSplit([1,2,3,4,5], [1,2,3], [4,5])

        def assertSplit(self, orig_ls, h1_ls, h2_ls):
            head = from_list(orig_ls)
            h1,h2 = self.sol.split(head)
            self.assertEqual(to_list(h1), h1_ls)
            self.assertEqual(to_list(h2), h2_ls)

        def test_sort(self):
            self.assertSorted([], [])
            self.assertSorted([1], [1])
            self.assertSorted([1,2], [1,2])
            self.assertSorted([2,1], [1,2])
            self.assertSorted([1,3,2], [1,2,3])
            self.assertSorted([3,2,1], [1,2,3])
            self.assertSorted([3,1,2], [1,2,3])
            self.assertSorted([4,4,1,2], [1,2,4,4])

        def assertSorted(self, src_ls, dest_expected):
            head = from_list(src_ls)
            new_head = self.sol.sortList(head)
            dest_actual = to_list(new_head)
            self.assertEqual(dest_actual, dest_expected)

    unittest.main()
