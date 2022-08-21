# 583. Delete Operation for Two Strings
# Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.
# In one step, you can delete exactly one character in either string.

# Example 1:

# Input: word1 = "sea", word2 = "eat"
# Output: 2
# Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
# Example 2:

# Input: word1 = "leetcode", word2 = "etco"
# Output: 4

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        mem = [[0] * (m + 1) for _ in range(n + 1)]
        
        for i, c in enumerate(word1):
            for j, d in enumerate(word2):
                if c == d:
                    mem[i + 1][j + 1] = 1 + mem[i][j]
                else:
                    mem[i + 1][j + 1] = max(mem[i][j + 1], mem[i + 1][j])
        common = mem[-1][-1]
        return n + m - common * 2
    
    