class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        row=len(A)
        col=len(A[0])
        res=[]
        for i in range(row):
            row_=self.reverseList(A[i])
            row_=[1-i for i in row_]
            res.append(row_)
        return res
    
    def reverseList(self,root):
        mid=len(root)//2
        
        if mid==0:
            return root
        if len(root)%2==1:
            
            return self.reverseList(root[mid+1:])+[root[mid]]+self.reverseList(root[:mid])
        else:
            return self.reverseList(root[mid:])+self.reverseList(root[:mid])
        
        
        
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        row=len(A)
        col=len(A[0])
        for i in range(row):
            A[i]=A[i][::-1]
            for j in range(col):
                A[i][j]^=1
                
        return A
        
        
        
        
        
        
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        row=len(A)
        col=len(A[0])
        res=[[0]*col for _ in range(row)]
        
        for i in range(row):
            for j in range(col):
                res[i][j]=1-A[i][col-1-j]
        return res
        
        
        
