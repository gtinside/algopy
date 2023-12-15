from typing import List, Optional

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adj = []
        visited = [False]*len(isConnected)
        for i, conns in enumerate(isConnected):
            adj.append([])
            for j, c in enumerate(conns):
                if i!=j and c == 1:
                    adj[i].append(j)
        
        print(adj)
        ans = 0
        for i in range(0, len(isConnected)):
            if not visited[i]:
                ans +=1
                visited[i] = True
                self.dfs(i, adj, visited)
        
        return ans
    
    def dfs(self, node, adj, visited):
        for child in adj[node]:
            if not visited[child]:
                visited[child] = True
                self.dfs(child, adj, visited)


print(Solution().findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))