class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mapping={}
        for i in range(len(nums)):
            if nums[i] in mapping and i-mapping[nums[i]]<=k:
                return True
            else:
                
                mapping[nums[i]]=i
        return False
