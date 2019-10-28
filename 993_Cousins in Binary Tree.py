# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        self.px, self.dx=None, -1
        self.py, self.dy=None, -2
        
        def preorder(node, parent, d):
            if not node:
                return 
            if node.val==x:
                self.px=parent
                self.dx=d
            if node.val==y:
                self.py=parent
                self.dy=d
            preorder(node.left, node, d+1)
            preorder(node.right, node, d+1)
        preorder(root, None, 0)
        
        return self.px!=self.py and self.dx==self.dy
        
        
        
        
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        import collections
        self.m=collections.defaultdict(tuple)
        self.dfs(root, None, 0)
        return self.m[x][0]!=self.m[y][0] and self.m[y][1]==self.m[x][1]
            
        
    def dfs(self, node, parent, depth):
        if not node: return
        self.m[node.val]=(parent, depth)
        self.dfs(node.left, node, depth+1)
        self.dfs(node.right, node, depth+1)
        
        
        
        
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        import collections
        m=collections.defaultdict(tuple)
        q=collections.deque()
        q.append((root, None))
        depth=0
        
        while q:
            size=len(q)
            for i in range(size):
                node, parent=q.popleft()
                if not node: continue
                q.append((node.left, node))
                q.append((node.right, node))
                if node.val==x:
                    m[x]=(parent, depth)

                    continue
                if node.val==y:
                    m[y]=(parent, depth)

                    continue

            if x in m and y in m:
                return m[x][0]!=m[y][0] and m[x][1]==m[y][1]
            else:
                depth+=1
            
            
            
            
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        import collections
        m=collections.defaultdict(tuple)
        q=collections.deque()
        q.append((root, None))
        depth=0
        
        while q:
            size=len(q)
            for i in range(size):
                node, parent=q.popleft()
                if not node: continue
                m[node.val]=(parent, depth)
                q.append((node.left, node))
                q.append((node.right, node))
            depth+=1
            
        return m[x][0]!=m[y][0] and m[x][1]==m[y][1]
            
  
