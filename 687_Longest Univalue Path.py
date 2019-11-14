# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans=0
        self.univaluePath(root)
        
        return self.ans
        
        
    def univaluePath(self, node):
        if not node: return 0
        
        l=self.univaluePath(node.left) if node.left else -1
        r=self.univaluePath(node.right) if node.right else -1
        
        pl=l+1 if l>=0 and node.val==node.left.val else 0
        pr=r+1 if r>=0 and node.val==node.right.val else 0
        self.ans=max(self.ans, pr+pl)
        
        return max(pl, pr)
