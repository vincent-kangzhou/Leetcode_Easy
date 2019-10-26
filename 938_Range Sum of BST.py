# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        self.res=0
        if root==None: return 0
        self.L=L
        self.R=R
        self.sumTree(root)
        return self.res
        
        
    def sumTree(self, node):
        if node.val>=self.L and node.val<=self.R:
            self.res+=node.val
        if node.left:
    
            self.sumTree(node.left)
        if node.right:
      
            self.sumTree(node.right)
