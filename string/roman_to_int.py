#13. Roman to Integer
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        res = 0
        roman = [['I', 1], ['V', 5], ['X', 10], ['L', 50], ['C', 100],['D', 500], ['M', 1000]]

        for i in range(n - 1):
                current = s[i]
                next = s[i + 1]
                current_i = [x for x in roman if current in x][0]
                current_i = roman.index(current_i)
                next_i = [x for x in roman if next in x][0]
                next_i = roman.index(next_i)
                if current_i < next_i:
                        res = res - roman[current_i][1]
                else:
                        res = res + roman[current_i][1]

        current_i = [x for x in roman if s[n-1] in x][0]
        current_i = roman.index(current_i)
        return res + roman[current_i][1]
        