class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:return 0
        max_=0
        res=1
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                res+=1
                
            else:
                max_=max(max_,res)
                res=1
                
        return max(res, max_)
        
        
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums: return 0
        N=len(nums)
        dp=[1]*N
        
        for i in range(N-1):
            if nums[i]<nums[i+1]:
                dp[i+1]=dp[i]+1
                
        return max(dp)
