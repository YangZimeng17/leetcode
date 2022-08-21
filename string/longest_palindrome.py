# 409. Longest Palindrome
# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

# Example 1:

# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        
        count = Counter(s)
        
        odd = False
        res = 0
        
        for a,b in count.items():
            if b % 2 == 0:
                res = b + res
            else:
                res = res + b - 1
                odd = True
        
        if odd:
            res = res + 1
            
        return res