class Solution(object):
    def oddCells(self, n, m, indices):
        """
        :type n: int
        :type m: int
        :type indices: List[List[int]]
        :rtype: int
        """
        import numpy as np
        
        matrix=np.zeros((n,m))
        
        for idx in indices:
            matrix[idx[0],:]=matrix[idx[0],:]+1
            matrix[:,idx[1]]=matrix[:,idx[1]]+1
        count=0 
        for i in range(n):
            for j in range(m):
                if matrix[i,j]%2:
                    count+=1
                    
        return count
        
        
        
class Solution(object):
    def oddCells(self, n, m, indices):
        """
        :type n: int
        :type m: int
        :type indices: List[List[int]]
        :rtype: int
        """
        
        count_row={}
        count_col={}
        for idx in indices:
            count_row[idx[0]]=count_row.setdefault(idx[0],0)+1
            count_col[idx[1]]=count_col.setdefault(idx[1],0)+1
        res=0
        for i in range(n):
            for j in range(m):
                sum_=count_row.get(i,0)+count_col.get(j,0)
                
                if sum_%2:
                    res+=1
        return res
                
