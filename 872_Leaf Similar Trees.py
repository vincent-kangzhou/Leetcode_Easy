# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        list1=[]
        list2=[]
        
        self.dfs(root1, list1)
        self.dfs(root2,list2)
        
        if list1==list2:
            return True
        else:
            return False
        
        
        
    def dfs (self, node, leaves):
        if not node:
            return None
        if not node.left and not node.right:
            leaves.append(node.val)
            
        if node.left:
            self.dfs(node.left, leaves)
            
        if node.right:
            self.dfs(node.right,leaves)
