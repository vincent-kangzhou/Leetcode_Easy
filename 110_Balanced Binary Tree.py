# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root==None: return True
        if abs(self.MaxHeight(root.right)-self.MaxHeight(root.left))<=1:
            return self.isBalanced(root.right) and self.isBalanced(root.left)
        else:
            return False
        
    
    def MaxHeight(self, root):
        if root==None: return 0
        return max(self.MaxHeight(root.left), self.MaxHeight(root.right))+1
    
