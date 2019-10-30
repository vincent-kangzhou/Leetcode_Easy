class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1: return 0
    
        nums_=sorted(nums)
        
        if nums_[-2]!=0 and nums_[-1]/nums_[-2]<2:
            return -1
        return nums.index(nums_[-1])
        
        
        
class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1: return 0
        
        largest=max(nums)
        
        idx=nums.index(largest)
        
        nums.pop(idx)
        if largest>=2 *max(nums):
            return idx
        else:
            return -1
            
            
class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest=max(nums)
        idx_=nums.index(largest)
        
        for idx, val in enumerate(nums):
            if idx==idx_:
                continue
            if val>largest/2:
                return -1
        return idx_
