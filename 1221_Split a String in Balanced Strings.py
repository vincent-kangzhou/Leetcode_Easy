class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count=0
        start=0
        for i in range(2,len(s)+1,2):
            if s[start:i].count('R')==(i-start)//2:
                count+=1
                start=i
                
            else:
                continue
                
        return count
            
            



class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l=0
        r=0
        lst=0
        for st in s:
            if st=='L':
                l+=1
            elif st=='R':
                r+=1
                
            if l==r:
                lst+=1
                l=0
                r=0
                
        return lst
        
        
        
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        ch_num={'L':0,'R':0}
        lst=0
        for st in s:
            ch_num[st]+=1
            
            if ch_num['L']==ch_num['R']:
                lst+=1
                ch_num={'L':0,'R':0}
        return lst
                
                
                
                
                
                
