# 437. Path Sum III
# Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.
# The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

# Example 1:

# Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
# Output: 3
# Explanation: The paths that sum to 8 are shown.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.result = 0
        mem = {0:1}
        
        self.dfs(root, targetSum, 0, mem)
        return self.result
    
    def dfs(self, root, targetSum, currPathSum, mem):
        if root is None:
            return  
        
        currPathSum = currPathSum + root.val
        oldPathSum = currPathSum - targetSum
        self.result = self.result + mem.get(oldPathSum, 0)
        mem[currPathSum] = mem.get(currPathSum, 0) + 1
        
        self.dfs(root.left, targetSum, currPathSum, mem)
        self.dfs(root.right, targetSum, currPathSum, mem)
        mem[currPathSum] = mem[currPathSum] - 1

    
        