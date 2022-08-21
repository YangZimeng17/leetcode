# 118. Pascal's Triangle
# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

# Example 1:
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        mem = []
        if numRows < 1:
            return mem

        for i in range(numRows):
            curr = []
            if i == 0:
                curr.append(1)
            else:
                curr.insert(0,1)

                for m in range(1,i):
                    curr.insert(m, mem[i - 1][m - 1] + mem[i - 1][m])

                curr.insert(i,1)
            mem.append(curr)

        return mem