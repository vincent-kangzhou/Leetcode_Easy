class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        import copy
        h_org=copy.copy((heights))
        heights.sort()
        count=0
        for i in range(len(heights)):
            if heights[i]!=h_org[i]:
                count+=1
                
        return count
        
        
        
class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        return sum(a!=b for a, b in zip(sorted(heights),heights))
        
