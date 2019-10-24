class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        count=(sum(A)+sum(B))/2-sum(A)
        set_b=set(B)
     


        for i in A:
            j=i+count
            if j in set_b and j>=1 and j<=100000:
                return [i, j]
                
                
                
class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sum_A=sum(A)
        sum_B=sum(B)
        B=set(B)
        for num in A:
            if num-(sum_A-sum_B)//2 in B:
                return [num,num-(sum_A-sum_B)//2]
                
                
                
                
                
  
