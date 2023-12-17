from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        visited = [[False]*len(grid[0]) for i in range(len(grid))]
        ans = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and not visited[row][col]:
                    ans +=1
                    self.visit(row, col, grid, visited)
        
        return ans
            
    
    def visit(self, row, col, grid, visited):
        if row < 0 or row >=len(grid) or col < 0 or col >=len(grid[row]):
            return 
        
        if grid[row][col] == "0" or visited[row][col]:
            return
        visited[row][col] = True
        self.visit(row + 1, col, grid, visited)
        self.visit(row - 1, col, grid, visited)
        self.visit(row, col + 1, grid, visited)
        self.visit(row, col - 1, grid, visited)


print(Solution().numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))







        