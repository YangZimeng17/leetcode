# 45. Jump Game II
# Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Your goal is to reach the last index in the minimum number of jumps.
# You can assume that you can always reach the last index.

# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. 
# Jump 1 step from index 0 to 1, then 3 steps to the last index.
import math

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        mem = [math.inf] * n
        mem[n - 1] = 0
        
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, min(i + nums[i], n-1) + 1):
                mem[i] = min(mem[i], mem[j] + 1)
                
        return mem[0]