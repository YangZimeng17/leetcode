# 11. Container With Most Water
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_a = 0
        start = 0
        n = len(height)  
        end = n - 1

        while start < end:
            w = end - start
            min_h = min(height[start], height[end])
            max_a = max(max_a, min_h * w)

            if height[start] < height[end]:
                start = start + 1
            else:
                end = end - 1

        return max_a