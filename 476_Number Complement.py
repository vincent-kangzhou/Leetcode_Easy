class Solution:
    def findComplement(self, num: int) -> int:
        res=list(map(int, list(bin(num)[2:])))
        res=[str(1-i) for i in res]
        res=''.join(res)
        return int(res,2)
        
        
        
        
        
class Solution:
    def findComplement(self, num: int) -> int:
        orlist=list(bin(num)[2:])
        rList=list()
        for i in orlist:
            if i =='0':
                rList.append('1')
            else:
                rList.append('0')
        r=''.join(rList)
        return int(r,2)
        
        
        
        
class Solution:
    def findComplement(self, num: int) -> int:
        binary=bin(num)[2:]
        ans=0
        
        for idx, val in enumerate(binary[::-1]):
            if val=='0':
                ans+=2**idx
        return ans
        
