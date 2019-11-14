class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        hashs=[0]*len(nums)
        
        for i in range(len(nums)):
            hashs[nums[i]-1]+=1
            
        return [hashs.index(2)+1, hashs.index(0)+1]
        
        
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nset=set(nums)
        
        N=len(nums)
        
        missing=(N+1)*N//2-sum(nset)
        
        duplicate=sum(nums)-sum(nset)
        
        return [duplicate, missing]
