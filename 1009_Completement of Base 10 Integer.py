class Solution:
    def bitwiseComplement(self, N: int) -> int:
        bin_=bin(N)[2:]
        bin_=[str(1-int(i)) for i in bin_]
        bin_=''.join(bin_)
        return int(bin_,base=2)
 
 
 
 
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        bin_=bin(N)[2:]
        bin_=[str(1^int(i)) for i in bin_]
        bin_=''.join(bin_)
        return int(bin_,base=2)
        
        
        
        
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        mask=1
        while N>mask:
            mask=mask*2+1
        return mask-N
