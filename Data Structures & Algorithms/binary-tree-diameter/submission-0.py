# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0 
        def longestPath(node):
            nonlocal diameter 
            if node is None:
                return 0 

            left_height = longestPath(node.left)
            right_height = longestPath(node.right)

            diameter = max(left_height + right_height, diameter)

            height = max(left_height, right_height) + 1 
            return height 
        
        longestPath(root)
        return diameter 



        