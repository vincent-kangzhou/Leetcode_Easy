class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        import numpy as np
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]>0:
                    count+=1
        return count+sum(np.max(grid,axis=0))+sum(np.max(grid,axis=1))
