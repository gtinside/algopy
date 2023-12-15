from typing import List
from collections import deque
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # code here
        myQ = deque()
        visited = [False]*V
        ans = [0]
        
        myQ.append(0)
        visited[0] = True
        
        while myQ:
            node = myQ.popleft()
            for child in adj[node]:
                if visited[child]:
                    continue
                visited[child] = True
                ans.append(child)
                myQ.append(child)
        
        return ans

print(Solution().bfsOfGraph(5,[[2,3,1] , [0], [0,4], [0], [2]]))