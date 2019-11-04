class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)==1: return True
        isIncrease=lambda nums: all(nums[i]<=nums[i+1] for i in range(len(nums)-1))
        
        one=nums[:]
        two=nums[:]
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                one[i]=one[i+1]
                two[i+1]=two[i]
                break
        return isIncrease(one) or isIncrease(two)
        
        
        
        
class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count=1
        for i in range(1, len(nums)):
            if nums[i]<nums[i-1]:
                if count==0:
                    return False
                if i==1 or nums[i]>=nums[i-2]:
                    nums[i-1]=nums[i]
                else:
                    nums[i]=nums[i-1]
                count-=1
        return True
