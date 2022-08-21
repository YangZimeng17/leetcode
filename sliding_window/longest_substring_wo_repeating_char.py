# 3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)

        if s == '':
            return 0
        if n == 1:
            return 1

        store = []
        start = 0
        i = 0
        res = 0
        while i < n:
            
            if s[i] not in store:
                store.append(s[i])
                res = max(res, i - start + 1)
                i = i + 1
            else:
                start = start + 1
                store.remove(s[start - 1])

        return res