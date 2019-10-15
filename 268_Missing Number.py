class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if nums==[]: 
        #     return 0
        max_num=max(nums)
        if len(set(range(max_num))-set(nums))==0:
            return max_num+1
        else:
        
            return list(set(range(max_num))-set(nums))[0]
            
            







class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(len(nums)):
            if nums[i]!=i:
                return i
            else:
                i+=1
        return i
        
        
  





class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp_sum=(len(nums)+1)*len(nums)/2
        cur_sum=sum(nums)
        return temp_sum-cur_sum
        
        



class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=len(nums)
        
        for i in range(len(nums)):
            res^= (i^nums[i])
        return res
