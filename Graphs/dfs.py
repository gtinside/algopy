class Solution:
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # code here
        visited = [False]*V
        self.ans = [0]
        visited[0] = True
        self.dfs(0, adj, visited)
        return self.ans
    
    def dfs(self, node, adj, visited):
        arr = adj[node]
        
        for child in arr:
            if visited[child]:
                continue
            visited[child] = True
            self.ans.append(child)
            self.dfs(child, adj, visited)

print(Solution().dfsOfGraph(5,[[2,3,1] , [0], [0,4], [0], [2]]))
