class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        max_=max(A)
        
        return A.index(max_)
        
        
class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        left, right=0, len(A)-1
        while left<right:
            mid=(left+right)//2
            if A[mid]>A[mid+1]:
                right=mid
            else:
                left=mid+1
        return right
        
        
        
class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        left, right=0, len(A)
        while left<right:
            mid=(left+right)//2
            if A[mid]>A[mid+1] and A[mid]>A[mid-1]: return mid
            
            if A[mid]>A[mid+1]:
                right=mid
            else:
                left=mid+1
        return -1
        
        
class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for i in range(len(A)-1):
            if A[i]>A[i+1]:
                return i
