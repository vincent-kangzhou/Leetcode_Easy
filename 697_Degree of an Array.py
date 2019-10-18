class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        if len(nums)==len(set(nums)): return 1
                
        count={}
        start={}
        end={}
        
        
        for i in range(len(nums)):
            if nums[i] not in count:
                count[nums[i]]=1
                start[nums[i]]=i
                end[nums[i]]=i
            else:
                count[nums[i]]+=1
                end[nums[i]]=i
        
        degree=max(count.values())
        res=100000
        
        for idx, val in enumerate(count.items()):
            if val[1]==degree:
                res=min(res, end[val[0]]-start[val[0]]+1)
                
        return res
        
        
        
        
        
import collections
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        if len(nums)==len(set(nums)): return 1
        
        counter=collections.Counter(nums)
        degree=max(counter.values())
        most_number=[i for i in list(set(nums)) if counter[i]==degree]
        
        scale=100000
        
        for num in most_number:
            appear=[i for i in range(len(nums)) if nums[i]==num ]
            
            scale_=max(appear)-min(appear)+1
            
            scale=min(scale,scale_)
            
        return scale
        
        
        
        
        
import collections
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
       
        
        nums_set=set(nums)
        if len(nums)==len(nums_set): return 1
        
        num_dict={}
        degree=-1
        for num in nums_set:
            _count=nums.count(num)
            num_dict[num]=_count
            if _count>degree:
                degree=_count
        
        
        most_number=[num for num in nums_set if num_dict[num]==degree]
        
        scale=1000000000
        for num in most_number:
            _min=nums.index(num)
            
            for i in range(len(nums)-1,-1,-1):
                if nums[i]==num:
                    _max=i
                    break
            scale_=_max-_min+1
            
            if scale>scale_:
                scale=scale_
            if scale==degree:
                break
            
        return scale
                
        
        
        
        
import collections
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        
        left, right=dict(),dict()
        count=collections.defaultdict(int)
        
        for i,num in enumerate(nums):
            if num not in left:
                left[num]=i
            right[num]=i
            
            count[num]+=1
            
        degree=max(count.values())
        
        res=float('inf')
        
        for idx, val in count.items():
            if val==degree:
                res=min(res, right[idx]-left[idx]+1)
            if res==degree:
                break
            
        return res
                
        
