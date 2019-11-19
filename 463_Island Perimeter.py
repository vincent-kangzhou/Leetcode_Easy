class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count=0
        
        r=len(grid)
        c=len(grid[0])
        dirs=[(1,0),(-1,0),(0,1),(0,-1)]
        
        for i in range(r):
            for j in range(c):
                tot=4
                if grid[i][j]==0:
                    continue
                for x, y in dirs:
                    if i+x>=0 and i+x<r and j+y>=0 and j+y<c and grid[i+x][j+y]==1:
                        tot-=1
                count+=(tot)
                
        return count
        
        
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count=0
        intersection=0
        r=len(grid)
        c=len(grid[0])
        for i in range(r):
            for j in range(c):
                if grid[i][j]==1:
                    count+=1
                
                    if i<r-1:
                        intersection+=(grid[i+1][j])
                    if j<c-1:
                        intersection+=(grid[i][j+1])
        return 4*count-2*intersection
        
        
        
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def is_water(i, j):
            return i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0

        directions = ((0, -1), (0, 1), (-1, 0), (1, 0))
        perimeter = 0
        for (i, row) in enumerate(grid):
            for (j, item) in enumerate(row):
                if item == 1:
                    for direction in directions:
                        if is_water(i + direction[0], j + direction[1]):
                            perimeter += 1
        return perimeter
