# 343. Integer Break
# Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.
# Return the maximum product you can get.

# Example 1:

# Input: n = 2
# Output: 1
# Explanation: 2 = 1 + 1, 1 × 1 = 1.
# Example 2:

# Input: n = 10
# Output: 36
# Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.

class Solution:
    def integerBreak(self, n: int) -> int:
        mem = [None, 1]
        
        for m in range (2, n + 1):
            j = m - 1
            i = 1
            max_product = 0
            
            while i <= j:
                max_product = max(max_product, max(i, mem[i]) * max(j, mem[j]))
                j -= 1
                i += 1
                
            mem.append(max_product)
            
        return mem[n]