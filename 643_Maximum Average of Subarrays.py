class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums)==k: return sum(nums)/k
        largest=sum_=sum(nums[:k])
        
        
        for i in range(k,len(nums)):
            
            sum_=sum_+nums[i]-nums[i-k]
            
            largest=max(sum_,largest)
            
        return largest/k
        
        
        
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums)==k: return sum(nums)/k
        
        sum_=[nums[0]]*len(nums)
        for i in range(1,len(nums)):
            sum_[i]=sum_[i-1]+nums[i]
        res=sum_[k-1]
        for i in range(k, len(sum_)):
            res=max(res, sum_[i]-sum_[i-k])
        return res/k
