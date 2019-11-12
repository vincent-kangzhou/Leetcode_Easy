class Solution(object):

    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1 and not t2:
            return None
        res=TreeNode(0)
        
        
        if t1 and t2:
            res.val+=t1.val+t2.val
            if t1. left and t2.left:
                res.left=self.mergeTrees(t1.left, t2.left)
            elif t1.left:
                res.left=self.mergeTrees(t1.left, None)
            elif t2.left:
                res.left=self.mergeTrees(None, t2.left)
            
            
            if t1.right and t2.right:
            
                res.right=self.mergeTrees(t1.right, t2.right)
            
            elif t1. right:
                res.right=self.mergeTrees(t1.right, None)
            elif t2.right:
                res.right=self.mergeTrees(None, t2.right)
                
        elif t1:
            res.val+=t1.val
        
            if t1.left:
                res.left=self.mergeTrees(t1.left, None)
            if t1.right:
                res.right=self.mergeTrees(t1.right, None)
                     
            
        elif t2:
            res.val+=t2.val
            if t2.left:
                res.left=self.mergeTrees(None, t2.left)
            if t2.right:
                res.right=self.mergeTrees(None, t2.right)
        
        return res
        
        
        
        
        if t1 is None or t2 is None:
            return t1 if t2 is None else t2
        else:
            newNode = TreeNode(t1.val + t2.val)
            newNode.left = self.mergeTrees(t1.left, t2.left)
            newNode.right = self.mergeTrees(t1.right, t2.right)
            return newNode
            
            
            
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1 and not t2:
            return None
        newnode=TreeNode((t1.val if t1 else 0)+(t2.val if t2 else 0))
        newnode.left=self.mergeTrees(t1.left if t1 else None, t2.left if t2 else None)
        newnode.right=self.mergeTrees(t1.right if t1 else None, t2.right if t2 else None)
        return newnode
        
        

        
        
