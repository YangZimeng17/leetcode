# 416. Partition Equal Subset Sum
# Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

# Example 1:

# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# Example 2:

# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        
        if total_sum & 1: 
            return False
        half_sum = total_sum // 2
        dp = [True] + [False] * half_sum
        
        for num in nums:
            for j in range(half_sum, num-1, -1):
                if dp[j - num]:
                    dp[j] = True
                    
        return dp[half_sum]