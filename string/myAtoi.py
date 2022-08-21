# 8. String to Integer (atoi)

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        n = len(s)
        if s == None or n < 1:
            return 0
        neg = False
        pos = False
        res = 0
        i = 0

        if s[0] == '-':
            neg = True
            i = i + 1
        elif s[0] == '+':
            pos = True
            i = i + 1


        while i < n and '0' <= s[i] <= '9':
            res = res * 10 + int(s[i])
            i = i + 1

        if neg:
            res = -1 * res

        if res < -2**31:
            return -2 ** 31
        if res > 2 ** 31 - 1:
            return 2 ** 31 - 1
        return res