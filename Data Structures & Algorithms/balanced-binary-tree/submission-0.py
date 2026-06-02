# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isbalanced(self, root):
        if root is None:
            return 0
        
        left_height = self.isbalanced(root.left)
        right_height = self.isbalanced(root.right)

        if left_height == -1 or right_height == -1 :
            return -1 
        
        elif abs(left_height - right_height) >1 : 
            return -1 
        
        else:
            return max(left_height, right_height) + 1 
        
        

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balance_check = self.isbalanced(root)
        if balance_check != -1 :
            return True 
        else:
            return False 

        