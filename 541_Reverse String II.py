class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if len(s)<k: return s[::-1]
        len_=len(s)//k
        reminder=len(s)%k
        res=''
        for i in range(len_):
            
            res=res+s[i*k:(i+1)*k][::-1] if i%2==0 else res+s[i*k:(i+1)*k]
        
        if reminder>0:
            
            res=res+s[-reminder:][::-1] if len_%2==0 else res+s[-reminder:]
            

        return res
        
        
        


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        N= len(s)
        res=''
        pos=0
        while pos<N:
            res=res+s[pos:pos+k][::-1]+s[pos+k:pos+2*k]
            pos+=2*k
        return res
        
