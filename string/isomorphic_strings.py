# 205. Isomorphic Strings
# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

# Example 1:
# Input: s = "egg", t = "add"
# Output: true

# Example 2:
# Input: s = "foo", t = "bar"
# Output: false

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.transform(s) == self.transform(t)
        
    def transform(self, s):
        map = {}
        new_str = []
        
        for i,v in enumerate(s):
            if v not in map:
                map[v] = i
            new_str.append(map[v])
            
        return new_str