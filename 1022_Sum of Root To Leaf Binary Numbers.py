# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        self.res=0
        self.dfs(root, root.val)
        return self.res
    
    def dfs(self, root, presum):
        if not root.right and not root.left:
            self.res=(self.res+presum)%(10**9+7)
        if root.right:
            self.dfs(root.right, presum*2+root.right.val)
            
        if root.left:
            self.dfs(root.left, presum*2+root.left.val)
            
            
            
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res=0
        if not root: return 0
        self.recursive(root,'')
        return self.res%(10**9+7)
    
    def recursive(self, root,path):
        path+=str(root.val)
        if not root.right and not root.left:
            self.res+=int(path,2)
            return 
        
        if root.right:
            self.recursive(root.right, path)
        if root.left:
            self.recursive(root.left, path)
        
