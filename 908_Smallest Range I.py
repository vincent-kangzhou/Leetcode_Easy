class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        if len(A)==1: return 0
        return max(0, max(A)-min(A)-2*K)
