# 15. 3Sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        nums.sort()
        res = []

        for i in range(n):
            j = i + 1
            k = n - 1

            if i > 0 and nums[i] == nums[i-1]:
                continue

            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    res.append([nums[i],nums[j],nums[k]])
                    j = j + 1
                    while j < k and nums[j] == nums[j - 1]:
                        j = j + 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j = j + 1
                else:
                    k = k - 1
        return res