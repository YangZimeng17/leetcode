# 227. Basic Calculator II
# Given a string s which represents an expression, evaluate this expression and return its value. 
# The integer division should truncate toward zero.
# You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].
# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

# Example 1:
# Input: s = "3+2*2"
# Output: 7

# Example 2:
# Input: s = " 3/2 "
# Output: 1

# Example 3:
# Input: s = " 3+5 / 2 "
# Output: 5

class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        
        stack = []
        num = 0
        sign = "+"
        n = len(s)
        
        for i in range(n):
            if s[i].isdigit():
                num = num * 10 + ord(s[i]) - ord("0")
                
            if (not s[i].isdigit() and not s[i].isspace()) or i == n-1:
                if sign == "-":
                    stack.append(-num)
                    
                elif sign == "+":
                    stack.append(num)
                    
                elif sign == "*":
                    stack.append(stack.pop()*num)
                    
                else:
                    temp = stack.pop()
                    if temp // num < 0 and temp % num != 0:
                        stack.append(temp // num + 1)
                    else:
                        stack.append(temp//num)
                        
                sign = s[i]
                num = 0
                
        return sum(stack)