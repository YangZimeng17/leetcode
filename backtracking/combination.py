# 77. Combinations
# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
# You may return the answer in any order.

# Example 1:
# Input: n = 4, k = 2
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
# Explanation: There are 4 choose 2 = 6 total combinations.
# Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        stack = [(1, [])]
        
        while stack:
            start, combination = stack.pop()
            
            if len(combination) == k:
                res.append(combination)

            else: 
                for i in range(start, n+1):
                    newcombination = combination + [i]
                    stack.append((i+1, newcombination)) # -- go deeper
        return res