class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        if rec2[0]>=rec1[2] or rec2[1]>=rec1[3] or rec1[0]>=rec2[2] or rec2[3]<=rec1[1]:
            return False
        return True

    
    
    class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        return max(0, min(rec2[3],rec1[3])-max(rec1[1],rec2[1]))*max(0,min(rec2[2],rec1[2])-max(rec2[0],rec1[0]))>0
