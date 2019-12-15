#!/usr/bin/python3
## author: jinchoiseoul@gmail.com


class NaiveDisjointSets(object):

    def __init__(self, n):
        self.parents = [i for i in range(n)]
        
    def union(self, u, v):
        u,v = map(self.find, [u,v])
        if u==v:
            # This is not essential
            return
        self.parents[v] = u

    def find(self, u):
        while u != self.parents[u]:
            u = self.parents[u]
        return u

    def components_count(self):
        return len([i for i,p in enumerate(self.parents) if i==p])
            

class OptimizedDisjointSets(object):

    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.ranks = [1 for i in range(n)]
        
    def union(self, u, v):
        # optimization by rank comparison
        u,v = map(self.find, [u,v])
        if u==v:
            # this is essential for rank-adjusting optimization
            return
        u_rank, v_rank = self.ranks[u], self.ranks[v]
        if self.ranks[u] < self.ranks[v]:
            u, v = v, u
        self.parents[v] = u
        self.ranks[u] += self.ranks[v]

    def find(self, u):
        # optimization by path compression
        lineage = []
        while self.parents[u] != u:
            lineage.append(u)
            u = self.parents[u]
        root = u
        assert not lineage or lineage[-1] != u
        for v in lineage:
            self.parents[v] = root
        return root

    def components_count(self):
        return len([i for i,p in enumerate(self.parents) if i==p])


StaticDisjointSets = OptimizedDisjointSets


class DynamicDisjointSets(OptimizedDisjointSets):
    ''' add-union-find data structure 

        If the whole number of nodes count cannot be estimated beforehand,
        DynamicDisjointSets is preferable to the kind of StaticDIsjointSets above '''

    def __init__(self):
        self.parents = {}
        self.ranks = {}

    def add(self, u):
        assert u not in self.parents
        self.parents[u] = u
        self.ranks[u] = 1

    def has(self, u):
        return u in self.parents

    def components_count(self):
        return len([k for k,p in self.parents.items() if k==p])


import unittest


class DisjointSetsTest(unittest.TestCase):

    def setUp(self):
        n1, edges1, components1 = 4, [], 4
        n2, edges2, components2= 4, [(0,1),(2,1)], 2
        n3, edges3, components3 = 4, [(0,1),(3,1),(2,3)], 1
        self.test_set = [(n1, edges1, components1), (n2, edges2, components2), (n3, edges3, components3)]

    def test_basics(self):

        DSs = [NaiveDisjointSets, OptimizedDisjointSets]
        for DS in DSs:
            for n, edges, expected_components in self.test_set:
                dsets = self.make_disjoint_sets(DS, n, edges)
                self.assertEqual(dsets.components_count(), expected_components)

    def make_disjoint_sets(self, clazz, n, edges):
        dsets = clazz(n)
        for u,v in edges:
            dsets.union(u,v)
        return dsets


class DynamicDisjointSetsTest(unittest.TestCase):
    def test_find_largest_consecutive_sequence(self):
        numbers = [100, 4, 200, 1, 3, 2, 100]
        ddsets = DynamicDisjointSets()
        ddsets.add(100)
        for n in numbers:
            if ddsets.has(n):
                continue
            ddsets.add(n)
            if ddsets.has(n-1):
                ddsets.union(n-1, n)
            if ddsets.has(n+1):
                ddsets.union(n, n+1)
        
        max_seq = 0
        for i,p in ddsets.parents.items():
            if i==p:
                max_seq = max(max_seq, ddsets.ranks[i])

        self.assertEqual(max_seq, 4)


if __name__ == '__main__':
    unittest.main()
