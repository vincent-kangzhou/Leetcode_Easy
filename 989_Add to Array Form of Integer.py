class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        A=[str(i) for i in A]
        A=int(''.join(A))
        res=str(A+K)
        return [i for i in res]
        
        
        
class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        res=[]
        carrier=0
        for i in range(len(A)-1,-1,-1):
            reminder=K%10
            K=K//10
            
            
            res.insert(0,(A[i]+reminder+carrier)%10)
            carrier=(A[i]+reminder+carrier)//10
            
        carrier=carrier+K
        if carrier>0:
            carrier=[int(i) for i in str(carrier)]
            return carrier+res
        else:
            return res
            
            
class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        A[-1] += K
        for i in xrange(len(A) - 1, -1, -1):
            carry, A[i] = divmod(A[i], 10)
            if i: A[i-1] += carry
        if carry:
            carry=[int(i) for i in str(carry)]


            return carry+A
        else:
            
            return A
        
