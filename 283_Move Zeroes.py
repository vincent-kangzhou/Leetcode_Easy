class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums.sort(key=lambda x: 1 if x==0 else 0)
        
        
        
        
        
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i=0
        for num in nums:
            if num!=0:
                nums[i]=num
                i+=1
                
        for j in range(i, len(nums)):
            nums[j]=0
            
            
            
            
            
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        slow=fast=0
        while fast<len(nums):
            if nums[fast]!=0:
                if slow!=fast:
                    nums[slow]=nums[fast]
                    nums[fast]=0
                slow+=1
            fast+=1
