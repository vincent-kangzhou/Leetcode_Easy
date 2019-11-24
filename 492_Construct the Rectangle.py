class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        import numpy as np
        sq=int(np.sqrt(area))
        
        
        while sq>0:
            if area%sq==0:
                return [area//sq,sq]
            else:
                sq-=1
                
