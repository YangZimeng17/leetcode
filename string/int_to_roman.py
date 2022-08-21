# 12. Integer to Roman
class Solution:
    def intToRoman(self, num: int) -> str:
        num_sys = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        roman_sys = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
        i = 12
        res = ''
        while num > 0:
            dig = num // num_sys[i]
            num = num % num_sys[i]

            while dig > 0:
                res = res + roman_sys[i]
                dig = dig - 1

            i = i - 1

        return res