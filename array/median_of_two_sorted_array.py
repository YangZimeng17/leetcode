# 4. Median of Two Sorted Arrays
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

# Example 1:
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# Example 2:
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        res = []

        i = 0
        j = 0
        
        while i < n and j < m:
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i = i + 1
            else:
                res.append(nums2[j])
                j = j + 1

        while i < n:
            res.append(nums1[i])
            i = i + 1

        while j < m:
            res.append(nums2[j])
            j = j + 1
        l = len(res)
     
        if l % 2 != 0:
            return res[l//2]
        else:
            return (res[l//2-1] + res[l//2])/2