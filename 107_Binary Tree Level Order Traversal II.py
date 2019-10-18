# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res=[]
        level=0
        self.getNode(root, level, res)
        res.reverse()
        return res
        
        
        
    def getNode(self, root, level, res):
        if root:
            if len(res)<level+1: res.append([])
            res[level].append(root.val)
            if root.left !=None: self.getNode(root.left, level+1, res)
            if root.right !=None: self.getNode(root.right, level+1, res)
