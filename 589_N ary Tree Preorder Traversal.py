"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res=[]
        if not root: return []
        def dfs(node):
            res.append(node.val)
            for child in node.children:
                dfs(child)
        dfs(root)
                
        return res
        
        
class Solution(object):

    
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root: return []
        stack=[root,]
        res=[]
        
        while stack:
            node=stack.pop()
            res.append(node.val)
            stack.extrend(node.children[::-1])
            
        return res
        
        
        
class Solution(object):

    
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root: return []
        stack=[root,]
        res=[]
        
        while stack:
            node=stack.pop(0)
            res.append(node.val)
            for i in node.children[::-1]:
                stack.insert(0, i)
            
        return res
        
