class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import itertools
        
        max_=0
        for digits, group in itertools.groupby(nums):
            len1=len(list(group))
            if digits==1 and max_<len1:
                max_=len1
                
        return max_
