class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        A_=A.copy()
        
        A.sort()
        return A==A_ or A==A_[::-1]
        
        
        
        
