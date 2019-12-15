#!/usr/bin/python3


# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        # alternatives is a map (original_node -> cloned_node)
        # invariant: if a key node exists in the map, so is the alternative clone
        # alternatives is also for tracking original nodes if they are visited
        alternatives = {} 
        return self.cloneGraph0(node, alternatives)
        
    def cloneGraph0(self, node, alternatives):
        ''' @param node: original node
            @param alternatives: map of (original -> clone)
            @return cloned node of the given original `node` '''
        if not node:
            return None
        assert node
        
        node_clone = UndirectedGraphNode(node.label)
        alternatives[node] = node_clone
        
        for neighbor in node.neighbors:
            if neighbor in alternatives:
                neighbor_clone = alternatives[neighbor]
            else:
                neighbor_clone = self.cloneGraph0(neighbor, alternatives)
            node_clone.neighbors.append(neighbor_clone)
            
        return node_clone
            
            
if __name__ == "__main__":
    
    import unittest

    def make_graph(n, edges):
        if n == 0:
            return None

        nodes = []
        for i in range(n):
            node = UndirectedGraphNode(i)
            nodes.append(node)

        #integrity of edges is not checked
        #check at your own risk, test-doer
        for u,v in edges:
            n1, n2 = nodes[u], nodes[v]
            n1.neighbors.append(n2)
            n2.neighbors.append(n1)
        return nodes[0]

    def are_graphs_same(node1, node2):
        def are_graphs_same0(node1, node2, visited1, visited2):
            assert node1 not in visited1
            assert node2 not in visited2
            visited1[node1] = True
            visited2[node2] = True

            if node1 == None and node2 == None:
                return True
            elif (node1 == None) ^ (node2 == None):
                return False

            assert node1 != None and node2 != None

            if node1.label != node2.label:
                return False
            if len(node1.neighbors) != len(node2.neighbors):
                return False
            for neigh1, neigh2 in zip(node1.neighbors, node2.neighbors):
                if (neigh1 in visited1) ^ (neigh2 in visited2):
                    return False
                if neigh1 in visited1:
                    continue
                if not are_graphs_same0(neigh1, neigh2, visited1, visited2):
                    return False
            return True

        return are_graphs_same0(node1, node2, {}, {})


    class SolutionTest(unittest.TestCase):
        def test_basics(self):
            node0 = make_graph(0, [])
            cloned = Solution().cloneGraph(node0)
            self.assertGraphEqual(node0, cloned)

            node0 = make_graph(1, [])
            cloned = Solution().cloneGraph(node0)
            self.assertGraphEqual(node0, cloned)

            node0 = make_graph(2, [(0,1)])
            cloned = Solution().cloneGraph(node0)
            self.assertGraphEqual(node0, cloned)

            node0 = make_graph(4, [(0,1),(0,2),(2,3),(3,0)])
            cloned = Solution().cloneGraph(node0)
            self.assertGraphEqual(node0, cloned)

        def assertGraphEqual(self, original, cloned):
            self.assertTrue(are_graphs_same(original, cloned))

    unittest.main()
