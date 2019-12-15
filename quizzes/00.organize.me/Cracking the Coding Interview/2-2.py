class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

#    def __iter__(self):
#        while self:
#            yield self
#            self = self.next

def iterating_nodes(node):
    while node:
        yield node
        node = node.next

class Tracker(object):
    def __init__(self, k):
        self.k = k
        self.li = []

    def push(self, node):
        self.li.append(node)
        if len(self.li)>self.k:
            del(self.li[0])

def track(node, k):
    assert k>=0
    tracker = Tracker(k)
    #for nd in node:
    while node:
        tracker.push(node)
        node = node.next
    return tracker.li[0]

def main():
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)

    one.next = two
    two.next = three
    three.next = four
    four.next = five

    n_th_node_from_the_end = track(one, 3)
    print(n_th_node_from_the_end.val)

if __name__=="__main__":
    main()
