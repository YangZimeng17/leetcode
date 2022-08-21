# 54. Spiral Matrix
# Given an m x n matrix, return all elements of the matrix in spiral order.

# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix[0])
        m = len(matrix)
        
        x = 0
        y = 0
        dx = 1
        dy = 0
        res = []
        
        for _ in range(m * n):
            if not 0 <= x + dx < n or not 0 <= y + dy < m or matrix[y+dy][x+dx] == "#":
                dx, dy = -dy, dx
                
            res.append(matrix[y][x])
            matrix[y][x] = "#"
            x = x + dx
            y = y + dy
        
        return res