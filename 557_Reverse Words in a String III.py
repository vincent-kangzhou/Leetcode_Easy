class Solution:
    def reverseWords(self, s: str) -> str:
        if s=='': return ''
        res=''
        s=s.split()
        for i in range(len(s)-1):
            res+=(s[i][::-1]+' ')
        res+=s[-1][::-1]
            
            
        return res
        
        
        
class Solution:
    def reverseWords(self, s: str) -> str:
        res=[]
        s=s.split()
        for i in s:
            res.append(i[::-1])            
        return ' '.join(res)
