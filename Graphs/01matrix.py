from collections import deque
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        myQ = deque()
        ans = [[0]*len(mat[0]) for i in range(len(mat))]
        visited = [[False]*len(mat[0]) for i in range(len(mat))]

        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 0:
                    visited[i][j] = True
                    myQ.append((i,j,0))
        
        while myQ:
            i, j, distance = myQ.popleft()
            if self.isValid(i + 1, j, mat) and not visited[i + 1][j]:
                visited[i + 1][j] = True
                ans[i + 1][j] = distance + 1
                myQ.append((i + 1, j, distance + 1))
            
            if self.isValid(i - 1, j, mat) and not visited[i - 1][j]:
                visited[i - 1][j] = True
                ans[i - 1][j] = distance + 1
                myQ.append((i - 1, j, distance + 1))

            if self.isValid(i, j + 1, mat) and not visited[i][j + 1]:
                visited[i][j + 1] = True
                ans[i][j + 1] = distance + 1
                myQ.append((i, j + 1, distance + 1))
            
            if self.isValid(i, j - 1, mat) and not visited[i][j - 1]:
                visited[i][j - 1] = True
                ans[i][j - 1] = distance + 1
                myQ.append((i, j - 1, distance + 1))
        
        return ans
            

    def isValid(self, i, j, mat):
        return i < len(mat) and i>=0 and j >=0 and j<len(mat[i])

print(Solution().updateMatrix([[0,0,0],[0,1,0],[0,0,0]]))