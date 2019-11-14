class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        dirs=[(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1),(0,0)]
        r=len(M)
        c=len(M[0])
        
        res=[[0]*c for _ in range(r)]
        
        for i in range(r):
            for j in range(c):
                sum_=0
                nums=0
                
                for d in dirs:
                    x=i+d[0]
                    y=j+d[1]
                    
                    if x>=0 and x<=r-1 and y>=0 and y<=c-1:
                        sum_+=M[x][y]
                        nums+=1
                
                
                res[i][j]=sum_//nums
        return res
