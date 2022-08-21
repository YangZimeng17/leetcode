# 733. Flood Fill
# An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.
# You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].
# To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.
# Return the modified image after performing the flood fill.

# Example 1:

# Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
# Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row = len(image)
        col = len(image[0])
        
        init = image[sr][sc]
        
        if init == color:
            return image
        
        def search(r, c):
            if image[r][c] == init:
                image[r][c] = color
                if r >= 1:
                    search(r-1, c)
                if r + 1 < row:
                    search(r+1, c)
                if c >= 1: 
                    search(r, c-1)
                if c + 1 < col:
                    search(r, c+1)
                    
        search(sr, sc)
        return image