# 572. Subtree of Another Tree
# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

# Example 1:

# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isEqual(root1, root2):
            if root1 == None or root2 == None: 
                return root1 == root2
            return root1.val == root2.val and isEqual(root1.left, root2.left) and isEqual(root1.right, root2.right)
        
        def dfs(root, subRoot):
            if root == None: 
                return False
            return isEqual(root, subRoot) or dfs(root.left, subRoot) or dfs(root.right, subRoot)
        
        return dfs(root, subRoot)