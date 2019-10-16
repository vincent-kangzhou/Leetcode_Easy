class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        res=[]
        i,j, carry= len(num1)-1, len(num2)-1, 0
        
        while i>=0 or j>=0 or carry:
            if i>=0:
                carry+=ord(num1[i])-48
                i-=1
            if j>=0:
                carry+=ord(num2[j])-48
                j-=1
            
            res.insert(0, str(carry%10))
            
            carry=carry//10
            
        return ''.join(res)
        
        
        
        
        
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
            res=''
            carry=0
            M,N= len(num1), len(num2)
            if M>=N:
                num2='0'*(M-N)+num2
            else:
                num1='0'*(N-M)+num1
            
            len_=max(M,N)
            
            for i in range(len_-1,-1,-1):
                carry=ord(num1[i])-48+ord(num2[i])-48+carry
                
                res=str(carry%10)+res
                
                carry=carry//10
                
            if carry==1:
                res='1'+res
            return res
        
