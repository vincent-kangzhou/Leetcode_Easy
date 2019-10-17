class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        import numpy as np
        
        rank=np.argsort(nums)[::-1]
        res=list(map(str,rank))
        
        for i in range(len(nums)):
            if i==0:
                res[rank[i]]='Gold Medal'
                continue
            if i==1:
                res[rank[i]]='Silver Medal'
                continue
            if i==2:
                res[rank[i]]='Bronze Medal'
                continue
 
            res[rank[i]]=str(i+1)
        return res
        
        
        
class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        
        dmap = {v : k for k, v in enumerate(sorted(nums, reverse=True))}
        return [str(dmap[n] + 1) \
               if dmap[n] > 2 \
               else ['Gold', 'Silver', 'Bronze'][dmap[n]] + ' Medal' for n in nums]
#         ranks={k:v for k, v in enumerate(sorted(nums, reverse=True))}
        
#         return [str(ranks[n]+1) if ranks[n]>2 else ['Gold Medal','Silver Medal','Bronze Medal'][ranks[n]] for n in nums]
