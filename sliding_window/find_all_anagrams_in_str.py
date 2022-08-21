# 438. Find All Anagrams in a String
# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:

# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        mem = defaultdict(int)
        res = []
        p_len = len(p)
        s_len = len(s)
      
        if p_len > s_len: 
            return res

        for c in p: 
            mem[c] = mem[c] + 1

        for i in range(p_len - 1):
            if s[i] in mem: 
                mem[s[i]] = mem[s[i]] - 1
            
        for i in range(-1, s_len - p_len + 1):
            if i > -1 and s[i] in mem:
                mem[s[i]] = mem[s[i]] + 1
            if i + p_len < s_len and s[i + p_len] in mem: 
                mem[s[i + p_len]] = mem[s[i + p_len]] -1
                
            if all(v == 0 for v in mem.values()): 
                res.append(i + 1)
                
        return res