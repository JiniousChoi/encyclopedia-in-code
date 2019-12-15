#!/usr/bin/python3
## author: jinchoiseoul@gmail.com


from collections import defaultdict
from math import inf
from jpylib.jqueues import PriorityQueue


def solution(n, g, s):
    ''' return shortest distance from `s` to 
        other edges in ascending order of node id
        return [ distance :: int ] '''
    dists = [inf] * (n+1) # dist[0] is dummy
    dists[s] = 0
    pq = PriorityQueue([(0,s)])
    
    while pq.not_empty():
        dist, here = pq.pop()
        if dists[here] < dist:
            # pq에 들어온 후, here에 닿는
            # 더 짧은 루트 방법이 생긴 셈.
            # 따라서 here는 진행하지 않음.
            continue
        for there, cost in g[here].items():
            next_dist = dists[here]+cost
            if dists[there] > next_dist:
                # bfs의 discovered 역할
                # 즉, there에 도착할 더 짧은
                # 방법이 발견 됐을 때만 실행됨
                dists[there] = next_dist
                pq.push((next_dist, there))
                
    return dist_in_order(n, s, dists)
        

def dist_in_order(n, s, dists):
    res = []
    for u in range(1, n+1):
        if u==s: continue
        d = -1 if dists[u] == inf else dists[u]
        res.append(d)
    return res


def g_add(g, x, y, r):
    g[x][y] = min(r, g[x].get(y, inf))
    g[y][x] = min(r, g[y].get(x, inf))


def main():
    t = int(input().strip())
    for a0 in range(t):
        g = defaultdict(dict) # {u: {v:r} }
        n,m = input().strip().split(' ')
        n,m = [int(n),int(m)]
        for a1 in range(m):
            x,y,r = input().strip().split(' ')
            x,y,r = [int(x),int(y),int(r)]
            g_add(g, x, y, r)
        s = int(input().strip())
        print(*solution(n, g, s))
        

#main()


import unittest


class SolutionTest(unittest.TestCase):
    
    def test_basics(self):
        n, m = 4, 4
        g = defaultdict(dict)
        g_add(g, 1, 2, 24)
        g_add(g, 1, 4, 20)
        g_add(g, 3, 1, 3)
        g_add(g, 4, 3, 12)
        s = 1
        self.assertEqual(solution(n, g, s), [24,3,15])


if __name__ == "__main__":

    unittest.main()
