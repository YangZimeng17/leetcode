#.5 Longest Palindromic Substring
# Given a string s, return the longest palindromic substring in s.

#Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

#Example 2:
#Input: s = "cbbd"
#Output: "bb"

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        start = 0
        end = 0
        max = 1

        for i in range(n):
            if (n - i - 1) * 2 + 1 < max:
                break

            curent = 1
            next_i = i - 1
            next_j = i + 1
            while next_i >= 0 and next_j < n and s[next_i] == s[next_j]:
                curent = curent + 2
                next_i = next_i - 1
                next_j = next_j + 1
            if curent > max:
                max = curent
                start = next_i + 1
                end = next_j - 1

            curent = 0
            next_i = i
            next_j = i + 1
            while next_i >= 0 and next_j < n and s[next_i] == s[next_j]:
                curent = curent + 2
                next_i = next_i - 1
                next_j = next_j + 1
            if curent > max:
                max = curent
                start = next_i + 1
                end = next_j - 1

        return s[start:end + 1]