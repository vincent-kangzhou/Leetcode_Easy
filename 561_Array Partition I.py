class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        count=0
        for i in range(0,len(nums),2):
            count+=nums[i]
        return count
        
        
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])
