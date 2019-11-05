# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t: return ''
        res=str(t.val)
        
        if not t.left and not t.right:

            return res
        
        if t.left==None:
            res+='()'
        else:
            res+='('+self.tree2str(t.left)+')'
        
        if t.right:
            res+='('+self.tree2str(t.right)+')'
        
        return res
        
        
        
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    s=''
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        self.preOrder(t)
        return self.s
        
    def preOrder(self, node):
        if node:
            self.s+=str(node.val)
            
            if node.left:
                self.s+='('
                self.preOrder(node.left)
                self.s+=')'
            elif node.right:
                self.s+='()'
            if node.right:
                self.s+='('
                self.preOrder(node.right)
                self.s+=')'




class Solution(object):

    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t: return ''
        
        res=str(t.val)
        if  t.left or  t.right:
            res+='('+self.tree2str(t.left)+')'
        if t.right:
            res+='('+self.tree2str(t.right)+')'

        return res
