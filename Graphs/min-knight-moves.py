from collections import deque

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x = abs(x)
        y = abs(y)
        visited = set()
        moves = [(1, 2), (2, 1), (1, -2), (-1, 2), (-1, -2), (-2, 1), (2, -1), (-2, -1)]


        myQ = deque()
        myQ.append((0,0,0))

        while myQ:
            curr_x, curr_y, num_of_moves = myQ.popleft()
            if curr_x == x and curr_y == y:
                return num_of_moves
            for moveX, moveY in moves:
                up_x = curr_x + moveX
                up_y = curr_y + moveY
                if self.isValid(up_x, up_y, visited):
                    visited.add((up_x, up_y))
                    myQ.append((up_x, up_y, num_of_moves+1))

        return -1
        
    
    def isValid(self, x, y, visited):
        return (x,y) not in visited

print(Solution().minKnightMoves(4,2))