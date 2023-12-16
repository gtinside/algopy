from collections import deque
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        myQ = deque()

        visited = [[False]*len(board[0]) for i in range(len(board))]
        
        rows = len(board)
        cols = len(board[0])
        for i in range(rows):
            for j in range(cols):
                if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                    if board[i][j] == 'O':
                        myQ.append((i,j))
                        visited[i][j] = True

        while myQ:
            row, col = myQ.popleft()

            if self.isValid(row + 1, col, board, visited):
                visited[row + 1][col] = True
                myQ.append((row + 1,col))
            
            if self.isValid(row - 1, col, board, visited):
                visited[row - 1][col] = True
                myQ.append((row - 1,col))
            
            if self.isValid(row, col+ 1, board, visited):
                visited[row][col + 1] = True
                myQ.append((row,col + 1))

            if self.isValid(row, col - 1, board, visited):
                visited[row][col - 1] = True
                myQ.append((row,col - 1))
                
            
        for i in range(rows):
            for j in range(cols):
                if not visited[i][j]:
                    board[i][j] = 'X'
    

    def isValid(self, row, col, board, visited):
        return row >=0 and row < len(board) and col >=0 and col < len(board[row]) and not visited[row][col] and board[row][col] == 'O'

input = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Solution().solve(input)
print(input)
        

