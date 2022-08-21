# 2131. Longest Palindrome by Concatenating Two Letter Words
# You are given an array of strings words. Each element of words consists of two lowercase English letters.
# Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.
# Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.
# A palindrome is a string that reads the same forward and backward.

# Example 1:

# Input: words = ["lc","cl","gg"]
# Output: 6
# Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
# Note that "clgglc" is another longest palindrome that can be created.

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        mem = defaultdict(int)
        unpaired = 0
        res = 0
        
        for word in words:
            if word[0] == word[1]:
                if mem[word] > 0:
                    unpaired -= 1
                    mem[word] -= 1
                    res += 4
                else: 
                    mem[word] += 1
                    unpaired += 1
            else:
                if mem[word[::-1]] > 0:  # w[::-1] -> reversed w
                    res += 4
                    mem[word[::-1]] -= 1
                else: 
                    mem[word] += 1
        if unpaired > 0: 
            res += 2
        return res