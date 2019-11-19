class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums)-len(nums)*min(nums)
        
        
class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        nums.sort()
        while nums[0]!=nums[-1]:
            for i in range(len(nums)-1):
                nums[i]+=1
            count+=1
            nums.sort()
        return count
        
        
        
        
class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        nums.sort()
        for num in nums:
            count+=num-nums[0]
        return count
