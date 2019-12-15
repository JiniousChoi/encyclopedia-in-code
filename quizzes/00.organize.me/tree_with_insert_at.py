class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def order(self, A, B):
        root = None
        for _id, k in zip(A,B):
            root = insert_at(root, k, Node(_id))
        return list(n._id for n in traverse_in_order(root))
    
class Node(object):
    def __init__(self, _id):
        self._id = _id
        self.left = self.right = None
        self.size = 1
        
    def set_left(self, left):
        self.left = left
        self.resize()
        return self
    
    def set_right(self, right):
        self.right = right
        self.resize()
        return self
    
    def resize(self):
        self.size = 1 + get_size(self.left) + get_size(self.right)
        
def get_size(node):
    if not node: return 0
    return node.size

def insert_at(root, k, node):
    assert node
    if not root: return node
    if k < 0: k = 0
    if k > root.size: k = root.size
    
    left_size = get_size(root.left)
    if left_size > k:
        return root.set_left(insert_at(root.left, k, node))
    elif left_size == k:
        l = root.left
        root.set_left(None)
        node.set_left(l)
        node.set_right(root)
        return node
    else:
        new_right = insert_at(root.right, k-1-left_size, node)
        root.set_right(new_right)
        return root

def traverse_in_order(node):
    if not node: return
    if node.left: yield from traverse_in_order(node.left)
    yield node
    if node.right: yield from traverse_in_order(node.right)

