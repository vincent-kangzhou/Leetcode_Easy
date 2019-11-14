# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        res=[]
        que=collections.deque()
        que.append(root)
        while que:
            sum_=0
            num=0
            size=len(que)
            for _ in range(size):
                node=que.popleft()
                if not node: continue
                sum_+=node.val
                num+=1
                que.append(node.left)
                que.append(node.right)
            if num>0:
                res.append(sum_/float(num))
        return res
        
        
        
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        info=[]
        
        def dfs(node, depth):
            if not node:
                return None
            
            if len(info)<=depth:
                info.append([0,0])
            
            info[depth][0]+=node.val
            info[depth][1]+=1
            
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
        dfs(root, 0)
        
        return [i/float(j) for i , j in info]
        
        
        
        
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        res=[]
        
        
        
        def dfs(node, level, res):
            if not node:
                return None
            
            if len(res)<=level:
                res.append([])
            res[level].append(node.val)
            
            dfs(node.left, level+1, res)
            dfs(node.right, level+1, res)
            
        dfs(root, 0, res)
        
        return [sum(line)/float(len(line)) for line in res]
