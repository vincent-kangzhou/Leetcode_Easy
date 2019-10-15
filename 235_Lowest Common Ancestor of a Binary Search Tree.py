# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        s,b=sorted([p.val, q.val])
        while not s<=root.val<=b:
            root=root.left if s<=root.val else root.right
        return root
        
        



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        if q.val<root.val and p.val<root.val:
            return self.lowestCommonAncestor(root.left, p,q)
        if p.val>root.val and q.val>root.val:
            return self.lowestCommonAncestor(root.right, p,q)
        else:
            return root