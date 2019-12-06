class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum1=0
        sum2=sum(nums[1:])
        
        for i in range(1, len(nums)):
            if sum1==sum2:
                return i-1
            else:
                sum1+=nums[i-1]
                sum2-=nums[i]
                
        return len(nums)-1 if sum1==sum2 else -1
        
        
        
        
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        curr_sum = 0
        for i in xrange(len(nums)):
            if (curr_sum << 1) == total - nums[i]:
                return i
            curr_sum += nums[i]
        return -1
                
