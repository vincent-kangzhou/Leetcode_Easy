class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        import numpy as np
        
        num=int(np.sqrt(c))
        
        l, r=0, num
        while l<=r:
            if l**2+r**2==c:
                return True
            
            elif l**2+r**2>c:
                r-=1
                
            elif l**2+r**2<c:
                l+=1
                
        return False
        
        
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        for i in range(int(c**0.5)+1):
            
            if int((c-i**2)**0.5)**2==(c-i**2):
                return True
            
        return False
