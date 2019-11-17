class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums=nums

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return sum(self.nums[i:j+1])
        
        
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """

        
        self.sums=[0]*len(nums)
        total=0
        for x, num in enumerate(nums):
            total+=num
            self.sums[x]=total
            

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
       
        if i==0:
            return self.sums[j]
        if i>0:
            return self.sums[j]-self.sums[i-1]
