class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        A=sorted(A,key=lambda x: abs(x))
        return [i**2 for i in A]
        
        
        class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        N=len(A)
        j=0
        while j<N and A[j]<0:
            j+=1
        i=j-1
        res=[]
        while i>=0 and j<N:
            if A[i]**2 <A[j]**2:
                res.append(A[i]**2)
                i-=1
            else:
                res.append(A[j]**2)
                j+=1
        while i>=0:
            res.append(A[i]**2)
            i-=1
        while j<N:
            res.append(A[j]**2)
            j+=1
        return res
