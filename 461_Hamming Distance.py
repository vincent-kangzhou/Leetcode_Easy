class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x^y).count('1')
        
        
        
        
        
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        binx=bin(x)[2:]
        biny=bin(y)[2:]
        if len(binx)<=len(biny):
            binx='0'*(len(biny)-len(binx))+binx
        else:
            biny='0'*(len(binx)-len(biny))+biny
            
        count=0
        
        for i in range(len(binx)):
            if binx[i]!=biny[i]:
                count+=1
                
        return count
        
