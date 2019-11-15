class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        while nums and nums[0]==min(nums):
            nums.pop(0)
            
        while nums and nums[-1]==max(nums):
            nums.pop()
        return len(nums)
        
        
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N, _nums=len(nums),sorted(nums)
        if _nums==nums:
            return 0
        
        lis=[i for i in range(N) if _nums[i]!=nums[i]]
        return max(lis)-min(lis)+1
        
        
        
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        snums = sorted(nums)
        s = e = -1
        for i in range(len(nums)):
            if nums[i] != snums[i]:
                if s == -1: s = i
                e = i
        return e - s + 1 if e != s else 0
        
        
        
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        snums = sorted(nums)
        N=len(nums)
        s = e = -1
        for i in range(len(nums)):
            if s!=-1 and e!=-1:
                break
            if s==-1 and nums[i] != snums[i]:
                s = i
            if e==-1 and nums[N-1-i]!=snums[N-i-1]:
                e=N-1-i
        return e - s + 1 if e != s else 0
