from collections import deque
from typing import List

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        myQ = deque()

        visited = [[False]*len(grid[0]) for i in range(len(grid))]

        for row in range(rows):
            for col in range(cols):
                if row == 0 or row == rows - 1 or col == 0 or col == cols - 1:
                    if grid[row][col] == 1:
                        myQ.append((row, col))
                        visited[row][col] = True
        
        while myQ:
            row, col = myQ.popleft()
            if self.isValid(row + 1, col, grid, visited):
                visited[row + 1][col] = True
                myQ.append((row + 1, col))
            
            if self.isValid(row - 1, col, grid, visited):
                visited[row - 1][col] = True
                myQ.append((row - 1, col))
            
            if self.isValid(row, col + 1, grid, visited):
                visited[row][col + 1] = True
                myQ.append((row, col + 1))

            if self.isValid(row, col - 1, grid, visited):
                visited[row][col - 1] = True
                myQ.append((row, col - 1))
        

        ans = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and not visited[row][col]:
                    ans +=1
        

        return ans
            


    def isValid(self, row, col, grid, visited):
        return row >=0 and row < len(grid) and col >=0 and col < len(grid[0]) and not visited[row][col] and grid[row][col] == 1

print(Solution().numEnclaves([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]))