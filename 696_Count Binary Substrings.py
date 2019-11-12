class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        N=len(s)
        res=0
        for i in range(N):
            c1,c0=0,0
            if s[i]=='1':
                c1+=1
            else:
                c0+=1
            
            for j in range(i+1, N):
                if s[j]=='1':
                    c1+=1
                else:
                    c0+=1
                
                if c1==c0:
                    res+=1
                    break
                    
        return res
        
        
        N=len(s)
        curlen=1
        res=[]
        
        for i in range(1,N):
            if s[i]==s[i-1]:
                curlen+=1
                
            else:
                res.append(curlen)
                curlen=1
        
        res.append(curlen)
        
        return sum(min(x,y) for x, y in zip(res[1:],res[:-1]))
        
        
        
class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_=map(len, s.replace('01','0 1').replace('10','1 0').split())
        
        return sum(min(x, y) for x, y in zip(s_[:-1],s_[1:]))
        
        
        
class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        N=len(s)
        pre_len=0
        cur_len=1
        res=0
        for i in range(1,N):
            if s[i]==s[i-1]:
                cur_len+=1
                
            else:
                pre_len=cur_len
                cur_len=1
            if pre_len>=cur_len:
                res+=1
        return res
        
        
