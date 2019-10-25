class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A=sorted(A, reverse=True)
        for i in range(len(A)-2):
            if A[i]<A[i+1]+A[i+2]:
                return A[i]+A[i+1]+A[i+2]
            else:
                i+=1
        return 0
        
        
        
        class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        N=len(A)
        res=0
        
        for i in range(N-1,1,-1):
            if A[i-2]+A[i-1]>A[i]:
                return A[i-2]+A[i-1]+A[i]
        return 0
