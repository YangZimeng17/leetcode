# 1143. Longest Common Subsequence
# Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.

# Example 1:

# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  
# Explanation: The longest common subsequence is "ace" and its length is 3.

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        mem = [[0] * (m + 1) for _ in range(n + 1)]
        
        for i, c in enumerate(text1):
            for j, d in enumerate(text2):
                if c == d:
                    mem[i + 1][j + 1] = 1 + mem[i][j]
                else:
                    mem[i + 1][j + 1] = max(mem[i][j + 1], mem[i + 1][j])
                    
        return mem[-1][-1]