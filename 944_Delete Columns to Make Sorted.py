class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        r=len(A)
        c=len(A[0])

        count=0
        for i in range(c):
            res=[]
            for j in range(r):
                res.append(A[j][i])
                
            res_=sorted(res)
            if res_!=res:
                count+=1
                
        return count
        
        
        
class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        res = 0
        N = len(A[0])
        for i in range(N):
            col = [a[i] for a in A]
            if col != sorted(col):
                res += 1
        return res
        
        
class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        m, n = len(A), len(A[0])
        count = 0
        for i in xrange(n):
            for j in xrange(1, m):
                if A[j][i] < A[j-1][i]:
                    count += 1
                    break
        return count
