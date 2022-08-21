# 567. Permutation in String
# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.

# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mem = [0] * 26
        for c in s1:
            mem[ord(c) - 97] += 1
        i = 0
        j = 0
        count = len(s1)
        
        while j < len(s2):
            if mem[ord(s2[j]) - 97] > 0:   
                count = count - 1
            mem[ord(s2[j]) - 97] -= 1
            j = j + 1
            
            if count == 0:
                return True
            
            if j - i == len(s1):
                if mem[ord(s2[i]) - 97] >= 0:
                    count = count + 1
                mem[ord(s2[i]) - 97] += 1
                i = i + 1
                
        return False