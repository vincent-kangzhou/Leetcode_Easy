class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        matrix=[]
        for i in range(len(grid[0])):
            col=[]
            for j in range(len(grid)):
                col.append(grid[j][i])
            matrix.append(col)
            
        for i in range(k):
            aa=matrix.pop()
            
            bb=aa.pop()
            aa.insert(0, bb)
            matrix.insert(0, aa)
        res=[]
        for i in range(len(matrix[0])):
            row=[]
            for j in range(len(matrix)):
                row.append(matrix[j][i])
            res.append(row)
            
        return res
