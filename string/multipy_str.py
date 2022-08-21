# 43. Multiply Strings
# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

# Example 1:
# Input: num1 = "2", num2 = "3"
# Output: "6"

# Example 2:
# Input: num1 = "123", num2 = "456"
# Output: "56088"

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0": 
            return "0"
        
        f_num = num1[::-1]
        s_num = num2[::-1]
        res = []
        
        for ind, dig in enumerate(s_num):
            res.append(self.multiply_digit(dig, ind, f_num))
        
        ans = self.sum_res(res)

        return ''.join(str(dig) for dig in reversed(ans))

    def multiply_digit(self,digit2, num_zeros, first_number):
        current = [0] * num_zeros
        carry = 0

        for dig1 in first_number:
            mult = int(dig1) * int(digit2) + carry
            carry = mult // 10
            current.append(mult % 10)

        if carry != 0:
            current.append(carry)
        return current
    
    def sum_res(self,results):
        ans = results.pop()

        for result in results:
            new_answer = []
            carry = 0

            for digit1, digit2 in zip_longest(result, ans, fillvalue=0):
                curr_sum = digit1 + digit2 + carry
                carry = curr_sum // 10
                new_answer.append(curr_sum % 10)

            if carry != 0:
                new_answer.append(carry)

            ans = new_answer
        return ans