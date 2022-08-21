# 46. Permutations
# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# Example 2:
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        
        for n in nums:
            size = len(res)
            
            for i in range(size):
                prev = res.pop(0)
                prev.append(n)
                
                for j in range(len(prev)):
                    prev[j], prev[-1] = prev[-1], prev[j]
                    res.append(prev[:])
                    prev[j], prev[-1] = prev[-1], prev[j]
                    
        return res