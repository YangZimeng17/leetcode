# 417. Pacific Atlantic Water Flow
# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. 
# The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's 
# right and bottom edges.

# The island is partitioned into a grid of square cells. You are given an m x n integer matrix 
# heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

# The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, 
# south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. 
# Water can flow from any cell adjacent to an ocean into the ocean.

# Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can 
# flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if heights == None:
            return []
        
        self.directions = [(1,0),(-1,0),(0,1),(0,-1)]
        m = len(heights)
        n = len(heights[0])
        
        p_visited = [[False for _ in range(n)] for _ in range(m)]
        a_visited = [[False for _ in range(n)] for _ in range(m)]
        res = []
        
        for i in range(m):
            # p_visited[i][0] = True
            # a_visited[i][n-1] = True
            self.dfs(heights, i, 0, p_visited, m, n)
            self.dfs(heights, i, n-1, a_visited, m, n)
        for j in range(n):
            # p_visited[0][j] = True
            # a_visited[m-1][j] = True
            self.dfs(heights, 0, j, p_visited, m, n)
            self.dfs(heights, m-1, j, a_visited, m, n)
            
        for i in range(m):
            for j in range(n):
                if p_visited[i][j] and a_visited[i][j]:
                    res.append([i,j])
        return res
                
                
    def dfs(self, heights, i, j, visited, m, n):
        # when dfs called, meaning its caller already verified this point 
        visited[i][j] = True
        for direc in self.directions:
            x, y = i + direc[0], j + direc[1]
            if x < 0 or x >= m or y < 0 or y >= n or visited[x][y] or heights[x][y] < heights[i][j]:
                continue
            self.dfs(heights, x, y, visited, m, n)