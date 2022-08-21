# 994. Rotting Oranges
# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

# Example 1:

# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        if not row: 
            return -1
        
        col = len(grid[0])
        fresh = 0
        minutes= 0
        
        rotten = deque()
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    rotten.append((r, c))
                elif grid[r][c] == 1:
                    fresh = fresh + 1
        
        while rotten and fresh > 0:
            minutes = minutes + 1
            for i in range(len(rotten)):
                x, y = rotten.popleft()
                
                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    xx, yy = x + dx, y + dy
                    if xx < 0 or xx == row or yy < 0 or yy == col:
                        continue
                    if grid[xx][yy] == 0 or grid[xx][yy] == 2:
                        continue
                        
                    fresh = fresh - 1
                    grid[xx][yy] = 2
                    rotten.append((xx, yy))
        if fresh == 0:
            return minutes
        return -1
