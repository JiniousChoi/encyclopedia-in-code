#!/usr/bin/python3
## author: jinchoiseoul@gmail.com


def make_graph(edges, is_undirected=True):
    ''' @param edges: type of [(u::int, v::int)]
        @param is_undirected
        @return adjacent list '''
    G = {}

    for u,v in edges:
        G.setdefault(u, [])
        if is_undirected:
            G.setdefault(v, [])

        G[u].append(v)
        if is_undirected:
            G[v].append(u)
    return G
    

def dfs_iterative(n, G, start):
    ''' @param n: total number of nodes
        @param G: edges of adjacent list 
        @param start: where to start searching 
        @return None '''
    stack = [[start, -1]] # [(node_no, edge_pointer)]
    visited = [False for _ in range(n)]

    while stack:
        here, i = stack[-1]
        if i==-1:
            yield here
            visited[here] = True
            i += 1
        for j in range(i, len(G[here])):
            there = G[here][j]
            if visited[there]:
                continue
            #assert not visited[there]
            stack[-1][-1] = j+1
            stack.append([there,-1])
            break
        else:
            stack.pop(-1)
        

def count_components(n, G):
    return len(sorted_topologies(n, G))


def topological_sort(n, G, start):
    ''' @return [node_no::int] '''
    visited, topology_stack = [False for _ in range(n)], []
    _dfs(n, G, start, visited, topology_stack)
    return topology_stack[::-1]


def topological_sort_all(n, G):
    ''' @return [[node_no::int]] '''
    visited = [False for _ in range(n)]
    def dfs_all():
        topology_stacks = []
        for u in range(n):
            if not visited[u]:
                topology_stack = []
                _dfs(n, G, u, visited, topology_stack)
                topology_stacks.append(topology_stack[::-1])
        return topology_stacks

    return dfs_all()


def _dfs(n, G, here, visited, topology_stack):
    visited[here] = True
    for there in G.get(here, []):
        if visited[there]: continue
        _dfs(n, G, there, visited, topology_stack)
    topology_stack.append(here) #post-order


import unittest
import random


class DFSTest(unittest.TestCase):

    def setUp(self):
        self.n1, self.edges1 = 5, [(0, 1), (1, 3), (3, 2), (3, 4), (4, 2)]
        random.shuffle(self.edges1)

        self.n2, self.edges2 = 6, [(1, 2), (2, 4), (4, 3), (4, 5), (5, 3)]
        random.shuffle(self.edges2)

    def test_dfs_iterative_basics(self):
        G = make_graph([(0,1),(0,2),(0,3),(2,3)])

        self.assertEqual(list(dfs_iterative(4, G, 0)), [0,1,2,3])
        self.assertEqual(list(dfs_iterative(4, G, 1)), [1,0,2,3])
        self.assertEqual(list(dfs_iterative(4, G, 2)), [2,0,1,3])
        self.assertEqual(list(dfs_iterative(4, G, 3)), [3,0,1,2])

    def test_topological_sort_basics(self):
        n, G = self.n1, make_graph(self.edges1, is_undirected=False)
        self.assertEqual(topological_sort(n,G,0), [0,1,3,4,2])
        self.assertEqual(topological_sort(n,G,1), [1,3,4,2])
        self.assertEqual(topological_sort(n,G,3), [3,4,2])
        self.assertEqual(topological_sort(n,G,4), [4,2])
        self.assertEqual(topological_sort(n,G,2), [2])

    def test_topological_sort_undirected(self):
        n, G = self.n1, make_graph(self.edges1, is_undirected=True)
        self.assertTrue((topological_sort(n,G,0)==[0,1,3,2,4]) or (topological_sort(n,G,0)==[0,1,3,4,2]))

    def test_topological_sort_all_basics(self):
        n, G = self.n1, make_graph(self.edges1, is_undirected=False)
        self.assertEqual(topological_sort_all(n, G), [[0,1,3,4,2]])

        n, G = self.n2, make_graph(self.edges2, is_undirected=False)
        self.assertEqual(topological_sort_all(n, G), [[0],[1,2,4,5,3]])


if __name__=="__main__":
    unittest.main()
