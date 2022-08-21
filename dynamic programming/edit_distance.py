# 72. Edit Distance
# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
# You have the following three operations permitted on a word:
# Insert a character
# Delete a character
# Replace a character

# Example 1:
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        mem = [[-1] * (n + 1) for _ in range(m + 1)]
        
        for i in range(m + 1):
            for j in range(n+1):
                if i == 0:
                    mem[i][j] = j 
                elif j == 0:
                    mem[i][j] = i  
                elif word1[i-1] == word2[j-1]:
                    mem[i][j] = mem[i-1][j-1]
                else:
                    mem[i][j] = min(mem[i-1][j], mem[i][j-1], mem[i-1][j-1]) + 1
                    
        return mem[m][n]