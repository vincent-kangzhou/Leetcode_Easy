class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return list(set(range(1,len(nums)+1))-set(nums))
        
        
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for n in nums:
            i=abs(n)-1
            nums[i]=-abs(nums[i])
            
        return [idx+1 for idx, val in enumerate(nums) if val>0]
