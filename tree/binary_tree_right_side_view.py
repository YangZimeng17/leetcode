# 199. Binary Tree Right Side View
# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# Example 1:

# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        
        def dfs(root, depth):
            if root == None: 
                return
            if depth == len(self.res): 
                self.res.append(root.val)
            dfs(root.right, depth + 1) 
            dfs(root.left, depth + 1)
            
        dfs(root, 0)
        return self.res