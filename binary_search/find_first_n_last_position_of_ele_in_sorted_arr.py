# 34. Find First and Last Position of Element in Sorted Array
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums)-1
        
        start = self.findFirstIndex(nums, low, high, target)
        end = self.findLastIndex(nums, low, high, target)
        
        return [start, end]
    
    def findFirstIndex(self, nums, low, high, target):
        res = -1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                res = mid
                high = mid-1
            elif nums[mid] > target:
                high = mid-1
            else:
                low = mid + 1
        return res
    
    def findLastIndex(self, nums, low, high, target):
        res = -1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                res = mid
                low = mid+1
            elif nums[mid] > target:
                high = mid-1
            else:
                low = mid + 1
        return res