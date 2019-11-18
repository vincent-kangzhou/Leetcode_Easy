class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        count=1
        while (count+1)*count/2<=n:
            count+=1
        return count-1
        
        
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        import numpy as np
        return int((np.sqrt(1+8*n)-1)/2)
