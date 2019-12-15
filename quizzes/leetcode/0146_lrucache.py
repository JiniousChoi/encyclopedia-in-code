class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.d = {}
        self.ll = LinkedList()

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        n = self.d[key]
        self.ll.movetoend(n)
        return n.data[1]

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            n = self.d[key]
            self.ll.movetoend(n)
            n.data = (key, value)
            return
        if self.cap <= self.ll.sz:
            old = self.ll.popleft()
            self.d.pop(old.data[0])
        node = Node((key, value))
        self.ll.append(node)
        self.d[key] = node
        
class Node:
    __slots__ = ['data', 'prev', 'next']
    def __init__(self, data):
        self.data = data
        self.prev, self.next = None, None

class LinkedList:
    def __init__(self):
        self.head, self.tail= None, None
        self.sz = 0
        
    def popleft(self):
        if self.sz == 0:
            return None
        elif self.sz == 1:
            n1 = self.head
            self.head = self.tail = None
            self.sz = 0
            n1.next = None
            return n1
        else:
            n1 = self.head
            n2 = n1.next
            n1.next = None
            n2.prev = None
            self.head = n2
            self.sz -= 1
            return n1
        
    def append(self, node):
        if self.sz == 0:
            self.head = self.tail = node
            self.sz = 1
        else:
            t1 = self.tail
            t1.next = node
            node.prev = t1
            self.tail = node
            self.sz += 1
    
    def movetoend(self, node):
        if node == self.tail:
            return
        
        #assert node != self.tail
        if node == self.head:
            n1 = self.head
            n2 = n1.next
            n1.next = None
            n2.prev = None
            self.head = n2
            self.sz -= 1
            self.append(n1)
        else:
            #assert node.prev
            #assert node.next
            pr, nx = node.prev, node.next
            pr.next = nx
            nx.prev = pr
            node.next, node.prev = None, None
            self.sz -= 1
            self.append(node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

'''
Runtime: 140 ms, faster than 51.55% of Python3 online submissions for LRU Cache.
Memory Usage: 21.7 MB, less than 6.96% of Python3 online submissions for LRU Cache.
'''
