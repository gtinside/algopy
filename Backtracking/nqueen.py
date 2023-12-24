from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.ans=[]
        self.cols = set()
        self.posDiag = set()
        self.negDiag = set()

        board = [["."]*n for i in range(n)]

        self.backtracking(n, 0, board)
        return self.ans
        
    def backtracking(self, n, row, board):
        if row == n:
            copy = ["".join(r) for r in board]
            self.ans.append(copy)
            return
        
        for col in range(n):
            if col in self.cols or row+col in self.posDiag or row-col in self.negDiag:
                continue
            
            board[row][col]= "Q"
            self.cols.add(col)
            self.posDiag.add(row + col)
            self.negDiag.add(row - col)

            self.backtracking(n, row + 1, board)
            self.cols.remove(col)
            self.posDiag.remove(row + col)
            self.negDiag.remove(row - col)
            board[row][col]= "."
        

print(Solution().solveNQueens(4))
        
            