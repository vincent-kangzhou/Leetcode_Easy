class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        
        res=[]
        self.dfs(num, res, 0)
        
        return res
        
        
    def dfs(self, num, res, hours):
        while hours<=num:
            for hour in combinations([1,2,4,8], hours):
                hs=sum(hour)
                if hs>12:
                    continue
                for minu in combinations([1,2,4,8,16,32], num-hours):
                    mins=sum(minu)
                    if mins>60: continue
                    
                    res.append('%d:%02d' %(hs, mins))
            hours+=1
            
            
            
            
            
class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        ans=[]
        for x in range(1024):
            if bin(x).count('1')==num:
                h, m =x>>6, x&0x3F
                if h<12 and m<60:
                    ans.append('%d:%02d' %(h,m))
                    
        return ans
        
        
        
        
class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        ans=[]
        for h in range(12):
            for m in range(60):
                if (bin(h)+bin(m)).count('1')==num:
                    ans.append('%d:%02d' %(h,m))
        return ans
                
