"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res=[]
        ans=[]
        
        def dfs(node, level, res):
            if not node: return None
            
            if len(res)<=level:
                res.append([])
                
            res[level].append(node.val)
            
            for chil in node.children:
                dfs(chil,level+1, res)
                
        dfs(root, 0, res)
        
        for i in range(len(res)-1,-1,-1):
            for item in res[i]:
                ans.append(item)
        return ans
        
        
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res=[]
        if not root: return res
        for child in root.children:
            res.extend(self.postorder(child))
        res.append(root.val)
        return res
        
        
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res=[]
        if not root: return res
        stack=[root,]
        while stack:
            node=stack.pop()
            stack.extend(node.children)
            res.append(node.val)
            
        return res[::-1]
        
        
        
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
    
        res=[]
        if not root: return res
        que=collections.deque()
        que.append(root)
        
        while que:
            node=que.pop()
            que.extend(node.children)
            res.append(node.val)
            
        return res[::-1]
