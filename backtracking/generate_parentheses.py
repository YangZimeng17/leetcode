# 22. Generate Parentheses
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

# Example 2:

# Input: n = 1
# Output: ["()"]

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        generate(res, '', 0,0,n)
        return res

def generate(res, s, op, cl, n):
    if op == n and cl == n:
        res.append(s)
        return
    if op < n:
        generate(res, s + '(', op + 1, cl, n)
    if cl < op:
        generate(res, s + ')', op, cl + 1, n)