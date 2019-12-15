#!/usr/bin/python3
## author: jinchoiseoul@gmail.com


from jpylib.jtrees import MinHeap
import heapq


class PriorityQueue0:

    def __init__(self, default=[]):
        self.heap = MinHeap()
        for val in default:
            self.heap.push(val)

    def pop(self):
        return self.heap.pop()

    def push(self, item):
        self.heap.push(item)

    def not_empty(self):
        return self.heap.size() > 0


class PriorityQueue1:

    def __init__(self, default=[]):
        self.pq = []
        for item in default:
            heapq.heappush(self.pq, item)
    
    def pop(self): 
        return heapq.heappop(self.pq)
    
    def push(self, item):
        heapq.heappush(self.pq, item)
       
    def not_empty(self):
        return len(self.pq) > 0


PriorityQueue = PriorityQueue0


import unittest


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.PQs = [PriorityQueue0, PriorityQueue1]

    def test_basics(self):
        from random import shuffle
        for PQ in self.PQs:
            data_in_order = list(range(10))
            data_in_chaos = data_in_order[:]
            shuffle(data_in_chaos)

            pq = PQ(data_in_chaos)

            self.assertEqual([pq.pop() for _ in range(10)], data_in_order, msg=PQ)


if __name__ == "__main__":

    unittest.main()
