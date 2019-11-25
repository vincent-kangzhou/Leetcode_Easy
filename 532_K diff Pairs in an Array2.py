class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        import collections
        if k<0:
            return 0
        if k==0:
            return sum(v>1 for v in collections.Counter(nums).values())
        return len(set(nums)&set(v+k for v in nums))
