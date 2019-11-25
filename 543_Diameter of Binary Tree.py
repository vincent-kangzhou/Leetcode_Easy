# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        dia=self.dfs(root.right)+self.dfs(root.left)
        left=self.diameterOfBinaryTree(root.left)
        right=self.diameterOfBinaryTree(root.right)
        
        return max(dia, left, right)
        
    
    
    def dfs(self, node):
        if not node:
            return 0
        
        return max(self.dfs(node.left),self.dfs(node.right))+1
