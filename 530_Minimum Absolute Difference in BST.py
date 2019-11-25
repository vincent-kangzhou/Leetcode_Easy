# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res=set()
        
        min_=float('inf')
        self.dfs(root)
        self.res=sorted(self.res)
        for j in range(1,len(self.res)):
            if min_>self.res[j]-self.res[j-1]:
                min_=self.res[j]-self.res[j-1]
        return min_
            
    
    def dfs(self, node):
        if not node:
            return None
        
        self.res.add(node.val)
        
        self.dfs(node.left)
        self.dfs(node.right)
