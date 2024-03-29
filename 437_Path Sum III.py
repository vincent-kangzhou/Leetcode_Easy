# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        return self.dfs(root,sum)+self.pathSum(root.left, sum)+self.pathSum(root.right,sum)
        
    def dfs(self, node, sum):
        res=0
        if not node:
            return res
        sum-=node.val
        if sum==0:
            res+=1
        res+=self.dfs(node.left,sum)
        res+=self.dfs(node.right,sum)
        
        return res
            
