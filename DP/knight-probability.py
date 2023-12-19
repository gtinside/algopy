class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        self.dp = {}
        return self.moveKnight(row, column, n, k)
    
    
    
    def moveKnight(self, r, c, n, k):
        if r<0 or r>=n or c<0 or c>=n:
            return 0
        if k==0:
            return 1
        if (r,c, k) in self.dp:
            return self.dp[(r,c, k)]
        
        result = self.moveKnight(r+2,c+1,n,k-1) + self.moveKnight(r+2,c-1,n,k-1) + self.moveKnight(r-2,c-1,n,k-1) + self.moveKnight(r+1,c+2,n,k-1) + self.moveKnight(r+1,c-2,n,k-1) + self.moveKnight(r-1,c-2,n,k-1) + self.moveKnight(r-1,c+2,n,k-1) + self.moveKnight(r-2,c+1,n,k-1) 

        self.dp[(r,c, k)] = result/8
        
        return result/8

print(Solution().knightProbability(3, 2, 0, 0))