# 130. Surrounded Regions
# Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.
# A region is captured by flipping all 'O's into 'X's in that surrounded region.

# Example 1:

# Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# Explanation: Notice that an 'O' should not be flipped if:
# - It is on the border, or
# - It is adjacent to an 'O' that should not be flipped.
# The bottom 'O' is on the border, so it is not flipped.
# The other three 'O' form a surrounded region, so they are flipped.

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if board == None or board[0] == None:
            return
        
        row, col = len(board), len(board[0])
        if row <= 2 or col <= 2:
            return
        
        for r in range(row):
            self.dfs(board, r, 0, row, col)
            self.dfs(board, r, col-1, row, col)

        for c in range(col):
            self.dfs(board, 0, c, row, col)
            self.dfs(board, row-1, c, row, col)

        for r in range(row):
            for c in range(col):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "N":
                    board[r][c] = "O"
                    
    def dfs(self, board, r, c, row, col):
        if 0 <= r < row and 0 <= c < col and board[r][c] == "O":
            board[r][c] = "N"
            self.dfs(board, r, c+1, row, col)
            self.dfs(board, r, c-1, row, col)            
            self.dfs(board, r-1, c, row, col)            
            self.dfs(board, r+1, c, row, col)  