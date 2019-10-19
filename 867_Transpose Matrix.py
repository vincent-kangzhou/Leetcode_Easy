class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        
        res=[]
        
        row=len(A)
        col=len(A[0])
        
        for i in range(col):
            row_=[]
            for j in range(row):
                row_.append(A[j][i])
            res.append(row_)
        return res
        
        
        
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        row=len(A)
        col=len(A[0])
        res=[[0]*row for _ in range(col)]
        
        for i in range(row):
            for j in range(col):
                res[j][i]=A[i][j]
                
        return res
        
