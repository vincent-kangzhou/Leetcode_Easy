# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root: return False
        self.flag=False
        
        self.ans=[]
        
        self.nodeAdd(root, k)

        
        return self.flag
        
    
    def nodeAdd(self, node,k):
        if not node: return None
        
        reminder=k-node.val
        
        
        if reminder in self.ans:
            self.flag=True
        self.ans.append(node.val)
            
        if not self.flag:
        
        
            self.nodeAdd(node.left,k)
            self.nodeAdd(node.right, k)
        
        
        
        
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        bstlist=list()
        def dfs(root):
            if root:
                dfs(root.left)
                bstlist.append(root.val)
                dfs(root.right)
                
                
        dfs(root)
        
        
        
        #for num in res:
         
         #if k != 2 * num and k - num in resset:
          #      return True
       # return False
        
        i,j=0, len(bstlist)-1
        
        while i<j:
            if bstlist[i]+bstlist[j]==k:
                return True
            if bstlist[i]+bstlist[j]<k:
                i+=1
            if bstlist[i]+bstlist[j]>k:
                j-=1
                
        return False
        
        
        
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        
        theSet=set()
        
        def findTarget(root, k):
            if root:
                if k-root.val in theSet:
                    return True
                
                
                theSet.add(root.val)
                
                return findTarget(root.left,k) or findTarget(root.right,k)
            return False
        
        
        return findTarget(root,k)
        
        
        
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        que=collections.deque()
        que.append(root)
        res=set()
        while que:
            size=len(que)
            for _ in range(size):
                node=que.popleft()
                
                if not node:
                    continue
                if k-node.val in res:
                    return True
                res.add(node.val)
                
                que.append(node.left)
                que.append(node.right)
                
        return False
        
        
        
