# 62. Unique Paths
# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mem = [[1]*n for i in range(m)]
        
        for i in range(1,m):
            for j in range(1,n):
                mem[i][j] = mem[i-1][j] + mem[i][j-1]
                
        return mem[-1][-1]