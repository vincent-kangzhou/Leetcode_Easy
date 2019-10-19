class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        m=len(nums)
        n=len(nums[0])
        
        if m*n !=r*c: return nums
        
        res=[]
        lis=[]
        for i in range(m):
            for j in range(n):
                lis.append(nums[i][j])
                
                if len(lis)==c:
                    res.append(lis)
                    lis=[]
                    
        return res
        
        
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        m=len(nums)
        n=len(nums[0])
        
        if m*n !=r*c: return nums
        count=0
        res=[[0]*c for _ in range(r)]
        for i in range(m):
            for j in range(n):
                res[count//c][count%c]=nums[i][j]
                count+=1
                
        return res
        
        
        
        
        
        
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        m=len(nums)
        n=len(nums[0])
        
        if m*n !=r*c: return nums
        count=0
        res=[[0]*c for _ in range(r)]
        row=0
        col=0
        for i in range(m):
            for j in range(n):
                res[row][col]=nums[i][j]
                col+=1
                if col%c==0:
                    col=0
                    row+=1
                
        return res
