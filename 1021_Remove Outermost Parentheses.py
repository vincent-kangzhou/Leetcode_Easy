class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        l=0
        r=0
        lst=[]
        part=''
        for i in S:
            if i=='(':
                l+=1
            elif i==')':
                r+=1
            part+=i
            if l==r:
                if l==1:
                    part=''
                else:
                    part=part[1:-1]
                lst.append(part)
                part=''
        return ''.join(lst) 
        
        
        
        
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        res,opener=[],0
        for s in S:
            if s=='(' and opener>0: 
                res.append(s)
            if s==')' and opener>1: 
                res.append(s) 
            opener+=1 if s=="(" else -1
            
        return ''.join(res)
