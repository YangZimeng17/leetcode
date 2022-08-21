# 14. Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        n = len(strs)
        res = ''
        if n == 0:
            return res

        m = len(strs[0])

        for i in range(1,n):
            m = min(m, len(strs[i]))
        for i in range(m):
            for j in range(n):
                if strs[j][i] != strs[0][i]:
                    return res
            res = res + strs[0][i]

        return res
