# 119. Pascal's Triangle II
# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

# Example 1:

# Input: rowIndex = 3
# Output: [1,3,3,1]

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        mem = []
        numRows = rowIndex + 1
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

        return mem[rowIndex]