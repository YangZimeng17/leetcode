# 394. Decode String
# Given an encoded string, return its decoded string.
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
# You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].
# The test cases are generated so that the length of the output will never exceed 105.

# Example 1:

# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
# Example 2:

# Input: s = "3[a2[c]]"
# Output: "accaccacc"
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        currant_num = 0
        currant_str = ''
        
        for c in s:
            if c == '[':
                stack.append(currant_str)
                stack.append(currant_num)
                currant_str = ''
                currant_num = 0
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                currant_str = prevString + num * currant_str
            elif c.isdigit():
                currant_num = currant_num * 10 + int(c)
            else:
                currant_str  = currant_str + c
        return currant_str