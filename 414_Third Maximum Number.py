class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        new_nums=list(set(nums))
        if len(new_nums)<=2: return max(new_nums)
        
        new_nums.remove(max(new_nums))
        new_nums.remove(max(new_nums))
        
        return max(new_nums)
        
        
        
        
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        a=b=c=None
        for n in nums:
            if n > a:
                a,b,c=n,a,b
            elif a>n>b:
                b,c=n,b
            elif b>n>c:
                c=n
                
        return c if c is not None else a
            
            
            
            
            
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
            
        
        def setMax(nums):
            _max=max(nums)
            for idx, val in enumerate(nums):
                if val == _max:
                    nums[idx]=float('-inf')
            return _max
        
        max1=setMax(nums)
        max2=setMax(nums)
        max3=setMax(nums)
        
        return max3 if max3!=float('-inf') else max1
