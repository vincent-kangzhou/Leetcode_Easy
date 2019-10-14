class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        now= last =  0
        for i in nums:
            last, now = now, max(i+last, now)
        return now
        
        
        
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) < 2:
            return max(nums[0], nums[-1])
        money = [0]*len(nums)
        money[0], money[1] = nums[0], max(nums[0], nums[1])
        for i in xrange(2, len(nums)):
            money[i] = max(nums[i] + money[i-2], money[i-1])
        return money[len(nums)-1]
