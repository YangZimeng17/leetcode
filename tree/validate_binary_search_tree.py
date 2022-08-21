# 98. Validate Binary Search Tree
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
# A valid BST is defined as follows:
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
 
# Example 1:

# Input: root = [2,1,3]
# Output: true

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        
        def check_order(root, order):
            if root == None:
                return
            check_order(root.left,order)
            order.append(root.val)
            check_order(root.right,order)
        
        order = []
        check_order(root, order)
        
        for i in range(1, len(order)):
            if order[i] <= order[i - 1]:
                return False
        return True