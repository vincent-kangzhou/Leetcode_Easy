# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1 and not t2:
            return None
        newnode=TreeNode((t1.val if t1 else 0)+(t2.val if t2 else 0))
        newnode.left=self.mergeTrees(t1.left if t1 else None, t2.left if t2 else None)
        newnode.right=self.mergeTrees(t1.right if t1 else None, t2.right if t2 else None)
        return newnode
        
        
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1:
            return t2
        
        if t2:
            t1.val+=t2.val
            t1.left=self.mergeTrees(t1.left,t2.left)
            t1.right=self.mergeTrees(t1.right,t2.right)
            
        return t1
