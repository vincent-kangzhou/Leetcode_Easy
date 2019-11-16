# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res, pathlist=[],[]
        self.dfs(root, res, pathlist)
        
        return res
        
    def dfs(self, node, res, pathlist):
        
        if not node: return None
        pathlist.append(str(node.val))
        
        if not node.left and not node.right:
            res.append('->'.join(pathlist))
        if node.left:
            self.dfs(node.left, res, pathlist)
        if node.right:
            self.dfs(node.right, res, pathlist)
            
            
        pathlist.pop()
        
        
        
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        
        res=[]
        beg=''
        
        def dfs(node, beg):
            if not node: return None
            beg+=str(node.val)
            
            
            if not node.left and not node.right:
                res.append(beg)
            beg+='->'
            if node.left:
                dfs(node.left, beg)
            if node.right:
                dfs(node.right, beg)
        dfs(root, beg)
        
        return res
        
