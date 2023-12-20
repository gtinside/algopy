from collections import defaultdict
from typing import List

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        adj = defaultdict(set)

        for edge1, edge2 in edges:
            adj[edge1].add(edge2)
            adj[edge2].add(edge1)
        
        
        leaf_nodes = []
        while n>2:
            leaf_nodes = [node for node in adj if len(adj[node]) == 1]
            n = n - len(leaf_nodes)
            while leaf_nodes:
                leaf_node = leaf_nodes.pop()
                neighbor = adj.pop(leaf_node)
                adj[list(neighbor)[0]].remove(leaf_node)
        
        return list(adj.keys())
               
print(Solution().findMinHeightTrees(n=4, edges=[[1,0],[1,2],[1,3]]))

        


