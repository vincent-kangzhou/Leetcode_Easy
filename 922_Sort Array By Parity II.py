class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        
        odd, even=1,0
        
        size=len(A)
        
        while odd<size and even<size:
            while odd<size and A[odd]%2==1:
                odd+=2
                
            while even<size and A[even]%2==0:
                even+=2
                
            if odd<size and even<size:
                A[even], A[odd]=A[odd], A[even]
                
                odd+=2
                even+=2
                
        return A
        
        
        
class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        N=len(A)
        result=[0]*N
        
        result[::2]=[x for x in A if x %2==0 ]
        result[1::2]=[x for x in A if x%2==1 ] 
        return result
        
        
        
        
class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i=0
        for j in range(1, len(A),2):
            if A[j]%2==0:
                while A[i]%2==0:
                    i+=2
                    
                A[j],A[i]=A[i],A[j]
        return A
        
