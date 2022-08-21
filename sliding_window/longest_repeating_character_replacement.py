# 424. Longest Repeating Character Replacement
# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
# Return the length of the longest substring containing the same letter you can get after performing the above operations.

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_n = 0
        res = 0
        count = collections.Counter()
        
        for i in range(len(s)):
            count[s[i]] = count[s[i]] + 1
            max_n = max(max_n, count[s[i]])
            if res - max_n < k:
                res = res + 1
            else:
                count[s[i - res]]  = count[s[i - res]] - 1
        return res