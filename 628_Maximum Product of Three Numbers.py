from functools import reduce
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        
        return max(reduce((lambda x, y:x*y), nums[-3:]),nums[-1]*nums[0]*nums[1])
#         if nums[-1]<=0:
#             return reduce((lambda x,y: x*y), nums[-3:])
        
#         if nums[-1]>0 and nums[-2]<0:
#             return nums[-1]*nums[0]*nums[1]



from functools import reduce
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        right=nums[-3]*nums[-2]*nums[-1]
        left=nums[-1]*nums[0]*nums[1]
        
        return max(right, left)
