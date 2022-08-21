# 844. Backspace String Compare
# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
# Note that after backspacing an empty text, the text will continue empty.

# Example 1:

# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".
# Example 2:

# Input: s = "ab##", t = "c#d#"
# Output: true
# Explanation: Both s and t become "".

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def skip(s):
            res = []
            for x in s:
                if x != '#':
                    res.append(x)
                elif res:
                    res.pop()
            return "".join(res)
        
        return skip(s) == skip(t)