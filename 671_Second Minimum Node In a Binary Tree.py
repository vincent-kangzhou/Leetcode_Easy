# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return -1
        self.nodelist=[]

        self.nodeAdd(root)
        self.nodelist=set(self.nodelist)
        
        return -1 if len(self.nodelist)==1 else sorted(list(self.nodelist))[1]
        
        
    def nodeAdd(self, node):
        if not node: return None
        self.nodelist.append(node.val)
        self.nodeAdd(node.left)
        self.nodeAdd(node.right)
