# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        dummy = TreeNode(0)
        
        self.prev=dummy
        
        def inorder(root):
            if not root:
                return None
            
            inorder(root.left)
            
            root.left=None
            self.prev.right=root
            self.prev=root
            inorder(root.right)
        inorder(root)
        
        return dummy.right
