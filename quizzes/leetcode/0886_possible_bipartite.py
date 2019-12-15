from collections import defaultdict, deque

class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        sol = ColoringByBFS()
        return sol.possibleBipartition(N, dislikes)
    
def make_graph(n, dislikes):
    g = defaultdict(list)
    for (i,j) in dislikes:
        i,j = i-1, j-1
        g[i].append(j)
        g[j].append(i)
    return g

def two_coloring_all(n, g, color_one):
    visited = [False for _ in range(n)]
    colors = [False for _ in range(n)]
    for i in range(n):
        if not visited[i]:
            if not color_one(g, i, visited, colors):
                return False
    return True

class ColoringByBFS:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        g = make_graph(N, dislikes)
        success = two_coloring_all(N, g, self.two_coloring_one)
        return success
    
    def two_coloring_one(self, g, i, visited, colors):
        to_visit = deque([(i,True)])
        discovered = set([i])
        
        while to_visit:
            i,c = to_visit.popleft()
            visited[i] = True
            colors[i] = c
            
            for j in g[i]:
                if visited[j]:
                    if colors[i] == colors[j]:
                        return False
                elif j not in discovered:
                    discovered.add(j)
                    to_visit.append((j, not c))
                # do I need to do is_opposite_color(i, j) when j in to_visit?
                # not efficient since j could be either on the same level as i or one level deeper.
                # So, wait until is_opposite_color(j, i) occur when j in visited.
                # More efficient and same effect!
        return True
    
class ColoringByDFS:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        g = make_graph(N, dislikes)
        success = two_coloring_all(N, g, self.two_coloring_one)
        return success
    
    def two_coloring_one(self, g, i, visited, colors):
        # assert not visited[i]
        visited[i] = True
        for j in g[i]:
            if visited[j]:
                if colors[i] == colors[j]:
                    return False
            else:
                colors[j] = not colors[i]
                if not self.two_coloring_one(g, j, visited, colors):
                    return False
        return True

'''
Runtime: 152 ms, faster than 81.75% of Python3 online submissions for Possible Bipartition.
Memory Usage: 17 MB, less than 71.43% of Python3 online submissions for Possible Bipartition.
'''
