# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root==None: return 0
        s=0
        if root.left and self.isLeaf(root.left):
            s=s+root.left.val  
        
        
        
        return s+self.sumOfLeftLeaves(root.left)+self.sumOfLeftLeaves(root.right)
    
    def isLeaf(self, root):
        if root.left ==None and root.right==None:
            return True
            
            
            
            
            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
        if not root: return 0
        self.sum=0
        self.findLeaf(root)
        return self.sum
        
        
        
    def findLeaf(self,node):
        if not node: return
        if node.left:
            self.findLeaf(node.left)
            if not node.left.left and not node.left.right:
                self.sum+=node.left.val
        if node.right:
            self.findLeaf(node.right)
            
            
            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root: return 0
        totalSum=0
        stack=[]
        stack.append(root)
        while stack:
            node=stack.pop()
            if not node: continue
            if node.left:
                if not node.left.left and not node.left.right:
                    totalSum+=node.left.val
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return totalSum
            
            
            
            
            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        ans=0
        if root:
            left, right= root.left, root.right
            
            if left and (left.left==None and left.right==None):
                ans+=left.val
            ans+=self.sumOfLeftLeaves(left)+self.sumOfLeftLeaves(right)
            
        return ans
