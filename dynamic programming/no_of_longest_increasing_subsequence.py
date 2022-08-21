# 673. Number of Longest Increasing Subsequence
# Given an integer array nums, return the number of longest increasing subsequences.
# Notice that the sequence has to be strictly increasing.

# Example 1:

# Input: nums = [1,3,5,4,7]
# Output: 2
# Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        
        n = len(nums)
        m = 0
        mem = [1] * n
        count = [1] * n
        res = 0
        
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if mem[i] < mem[j] + 1:
                        mem[i] = mem[j] + 1
                        count[i] = count[j]
                    elif mem[i] == mem[j] + 1: 
                        count[i] += count[j]
                        
            m = max(m, mem[i])
            
        for l, c in zip(mem, count):
            if l == m:
                res += c
            
        return res