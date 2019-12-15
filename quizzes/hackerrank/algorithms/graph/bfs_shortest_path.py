#!/usr/bin/python3
## author: jinchoiseoul@gmail.com


def shortest_to_all_node(node_cnt, roads, s):
    ''' return [distance::Int] in sorted order of # of node
        s: starting node point '''
    dists = {}
    
    to_visit = [(s,0)] # optimizable by using deque
    discovered = set([s]) # to_vist + visited
    while to_visit:
        here, dist = to_visit.pop(0)
        dists[here] = dist
        for neigh in roads.get(here, set()):
            if neigh in discovered:
                continue
            to_visit.append((neigh, dist+1))
            discovered.add(neigh)
        
    return [-1 if n not in dists else 6*dists[n] for n in range(1, node_cnt+1) if n != s]
    

def main():
    TCs = int(input().strip())
    for TC in range(TCs):
        node_cnt, edge_cnt = map(int, input().strip().split())
        roads = {}
        for _ in range(edge_cnt):
            n1,n2 = map(int, input().strip().split())
            roads.setdefault(n1, set())
            roads.setdefault(n2, set())
            roads[n1].add(n2)
            roads[n2].add(n1)
            
        s = int(input().strip())
        print(*shortest_to_all_node(node_cnt, roads, s))
 

#main()


import unittest
from unittest.mock import patch
from io import StringIO


class SolutionTest(unittest.TestCase):

    def test_shortest_to_all_node(self):
        node_cnt, edge_cnt = 4, 2
        roads = {1:{2,3}, 4:{2}}
        self.assertEqual(shortest_to_all_node(node_cnt, roads, 1), [6, 6, -1])

        node_cnt, edge_cnt = 3, 1
        roads = {2:{3}}
        self.assertEqual(shortest_to_all_node(node_cnt, roads, 2), [-1, 6])

    def test_main(self):
        user_input = [ '2',
                       '4 2', '1 2', '1 3', '1',
                       '3 1', '2 3', '2']
        expected = "6 6 -1\n-1 6\n"
        with patch('builtins.input', side_effect=user_input):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                main()
                self.assertEqual(fake_out.getvalue(), expected)



if __name__ == "__main__":

    unittest.main()
