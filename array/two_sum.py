# 1. Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
#Input: nums = [2,7,11,15], target = 9
#Output: [0,1]
#Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        i = 0
        j = n - 1
        temp = []
        for k in range (n):
            temp.append(nums[k])
        temp.sort()
        
        while i <= j:
            sum = temp[i] + temp[j] 
            if sum > target:
                j = j - 1
            elif sum < target:
                i = i + 1
            else:
                res_i = i
                res_j = j
                break
        for i in range (n):
            if nums[i] == temp[res_i]:
                res_i = i
                break
        for j in range (n):
            if j == res_i:
                continue
            if nums[j] == temp[res_j]:
                res_j = j
                break
        
        return [res_i, res_j]