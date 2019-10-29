class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if len(bits)==1: return True
        idx=-1
        for i in range(len(bits)-2,-1,-1):
            if bits[i]==0:
                idx=i
                break
        return (len(bits)-1-idx)%2!=0
        
        
        
        
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        
        pointer=0
        while pointer<len(bits)-1:
            pointer+=2 if bits[pointer] else 1
            
        return pointer==len(bits)-1
        
        
