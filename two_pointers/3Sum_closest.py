# 16. 3Sum Closest
# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.

# Example 1:

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        res = nums[0] + nums[1] + nums[n - 1]
        for i in range(0, n - 2):
            j = i + 1
            k = n - 1
            while j < k:
                current = nums[i] + nums[j] + nums[k]
                if current == target:
                    return current
                if abs(res - target) > abs(current - target):
                    res = current
                if current < target:
                    j += 1
                else:
                    k -= 1
        return res