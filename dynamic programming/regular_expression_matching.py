# 10. Regular Expression Matching
# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

# Example 1:
# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".

# Example 2:
# Input: s = "aa", p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

# Example 3:
# Input: s = "ab", p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        r = len(s)
        c = len(p)
        if r == 0 and c == 0:
            return True
        if c == 0:
            return False

        mem = []
        for i in range(r + 1):
            mem.append([])
            for j in range(c + 1):
                mem[i].append(False)
        mem[0][0] = True

        for i in range(2, c + 1):
            if p[i - 1] == '*':
                mem[0][i] = mem[0][i - 2]

        for i in range(1, r + 1):
            for j in range(1, c + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    mem[i][j] = mem[i - 1][j - 1]
                elif j > 1 and p[j - 1] == '*':
                    mem[i][j] = mem[i][j - 2]
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        mem[i][j] = mem[i][j] or mem[i - 1][j]
        return mem[r][c]