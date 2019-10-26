class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A)<=2: return False
        idx=A.index(max(A))
        before=sorted(A[:idx])
        if idx==0 or before!=A[:idx] or len(before)!=len(set(before)): return False
        after=sorted(A[idx:],reverse=True)
        if idx==len(A)-1 or after!=A[idx:] or len(after)!=len(set(after)): return False
        
        return True
        
        
        
class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A)<=2: return False
        N=len(A)
        i=0
        
        while i <N-1:
            if A[i]<A[i+1]:
                i+=1
            else:
                break
        if i==0 or i==N-1: return False
        while i<N-1:
            if A[i]>A[i+1]:
                i+=1
            else:
                break
        return i==N-1
        
        
        
class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A)<=2: return False
        N=len(A)
        i=0
        
        while i <N-1 and A[i]<A[i+1]:
            i+=1
        if i==0 or i==N-1: return False
        while i<N-1 and A[i]>A[i+1]:
            i+=1

        return i==N-1
