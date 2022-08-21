# 120. Triangle
# Given a triangle array, return the minimum path sum from top to bottom.
# For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

# Example 1:
# Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# Output: 11
# Explanation: The triangle looks like:
#    2
#   3 4
#  6 5 7
# 4 1 8 3
# The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        mem = [[-1] * n for _ in range(n)]
        
        def dfs(i, j):
            if i == n:
                return 0
            if mem[i][j] != -1:
                return mem[i][j]

            lower_left = triangle[i][j] + dfs(i + 1, j)
            lower_right = triangle[i][j] + dfs(i + 1, j + 1)
            mem[i][j] = min(lower_left, lower_right)
            return mem[i][j]

        return dfs(0, 0)