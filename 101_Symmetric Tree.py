# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            return self.sameTree(root.left, root.right)
        return True
        
        
    def sameTree (self, le, rig):
        if le==None and rig==None: return True
        if le and rig and le.val==rig.val:
            return self.sameTree(le.left, rig.right) and self.sameTree(le.right, rig.left)
        
        return False
