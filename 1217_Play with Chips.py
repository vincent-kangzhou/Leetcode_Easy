class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        odd_=sum([chip%2 for chip in chips])
        return min(odd_, len(chips)-odd_)
        
