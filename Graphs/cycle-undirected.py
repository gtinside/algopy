from typing import List
from collections import deque

class Solution:
    # Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        # Code here
        visited = [False] * V
        for i in range(V):
            if not visited[i] and self.checkForCycle(i, visited, adj, V):
                return True
        return False

    def checkForCycle(self, node, visited, adj, V):
        myQ = deque()
        myQ.append((node, -1))
        visited[node] = True

        while len(myQ) != 0:
            current, parent = myQ.popleft()
            for neighbor in adj[current]:
                if visited[neighbor] and neighbor != parent:
                    return True
                elif not visited[neighbor]:
                    visited[neighbor] = True
                    myQ.append((neighbor, current))
        return False


print(Solution().isCycle(5, [[1], [0, 2, 4], [1, 3], [2, 4], [1, 3]]))