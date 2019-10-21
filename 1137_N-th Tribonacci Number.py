class Solution:
    def tribonacci(self, n: int) -> int:
        res=[]
        res.append(0)
        res.append(1)
        res.append(1)
        if n<=2:
            return res[n]
        for i in range(3,n+1):
            res.append(res[i-3]+res[i-2]+res[i-1])
            
        return res[n]
        
        res=[0]*38
        res=[]
        res[0]=0
        res[1]=1
        res[2]=1
        if n<=2:
            return res[n]
        for i in range(3,n+1):
            res[i]=res[i-3]+res[i-2]+res[i-1]
            
        return res[n]
        
        
#         if n==0:
#             return 0
#         if n==1:
#             return 1
#         if n==2:
#             return 1
        
#         return self.tribonacci(n-1)+self.tribonacci(n-2)+self.tribonacci(n-3)
