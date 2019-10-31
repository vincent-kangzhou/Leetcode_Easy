class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if A==B: return True
        
        if len(A)!=len(B): return False
        
        for i in range(len(A)):
            if A[i+1:]+A[:i+1]==B:
                return True
        return False
        
        
class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if A==B: return True
        
        for idx, val in enumerate(A):
            if val==B[0]:
                left, right=A[idx:], A[:idx]
                
                if left+right==B:
                    return True
        return False
        
        
        
class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A)!=len(B): return False
        if A==B: return True
        All=A+A
        
        return All.find(B)>=0
