# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.res=0
        def dfs(node):
            if not node:
                return None
            dfs(node.right)
            self.res+=node.val
            node.val=self.res
            dfs(node.left)
            
        dfs(root)
        
        return root
        
        
        
