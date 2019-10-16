class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())
        
        
        
class Solution:
    def countSegments(self, s: str) -> int:
        
        count=0
        sum_=0
        
        for i in s:
            if i!=' ':
                count+=1
                
            else:
                sum_+=(count>0)
                count=0
        sum_=sum_+(count>0)
        return sum_
