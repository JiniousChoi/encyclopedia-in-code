import sys
sys.setrecursionlimit(500000)

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, parents):
        if not parents:
            return 0
        assert len(parents) >= 1
        tree = make_tree(parents)
        depth, max_dist = find_max_dist(tree)
        return max_dist

class TreeNode:
    __slots__ = ['childs']
    def __init__(self):
        self.childs = []
    def append(self, child):
        self.childs.append(child)
        
def make_tree(parents):
    n = len(parents)
    assert -1 in parents
    root = parents.index(-1)
    nodes = [TreeNode() for _id in range(n)]
    for i,p in enumerate(parents):
        if p==-1: continue
        nodes[p].append(nodes[i])
    assert parents[root] == -1
    return nodes[root]

def find_max_dist(tree):
    ''' @return (depth, max_dist) '''
    assert tree
    if len(tree.childs) == 0:
        return (0, 0)

    dms = [find_max_dist(child) for child in tree.childs]
    ds, ms = zip(*dms)
    max_depth_so_far = 1+max(ds)
    if len(tree.childs) == 1:
        assert len(ds) == 1
        max_dist_so_far = max(ds[0]+1, max(ms))
    else:
        max_dist_so_far = max(sum(top2_among(ds))+2, max(ms))
    return (max_depth_so_far, max_dist_so_far)

def top2_among(ds):
    top2 = Top2()
    for d in ds:
        top2.push(d)
    return top2.fst, top2.snd
    
class Top2:
    def __init__(self):
        self.fst, self.snd = 0, 0
    def push(self, n):
        if self.fst <= n:
            self.fst, self.snd = n, self.fst
        elif self.snd < n:
            self.snd = n

