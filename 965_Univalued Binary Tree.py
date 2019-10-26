# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root.right and not root.left:
            return True
        if not root.right:
            return (root.val==root.left.val) and self.isUnivalTree(root.left)
        if not root.left:
            return (root.val==root.right.val) and self.isUnivalTree(root.right)
        else:
            return (root.val==root.left.val) and self.isUnivalTree(root.left) and (root.val==root.right.val) and self.isUnivalTree(root.right)
