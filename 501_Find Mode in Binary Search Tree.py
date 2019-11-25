# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    import collections

    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        self.dic=collections.defaultdict(int)
        self.dfs(root)
        max_=max(self.dic.values())

        res=[]
        for idx, val in self.dic.items():
            if val==max_:
                res.append(idx)
        return res
        
        
        
    def dfs(self, node):
        if not node:
            return None
        
        self.dic[node.val]+=1
        
        self.dfs(node.left)
        self.dfs(node.right)
