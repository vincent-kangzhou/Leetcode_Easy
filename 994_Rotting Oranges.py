class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        import collections
        M,N=len(grid), len(grid[0])
        fresh=0
        
        q=collections.deque()
        for i in range(M):
            for j in range(N):
                if grid[i][j]==1:
                    fresh+=1
                elif grid[i][j]==2:
                    q.append((i,j))
        if fresh==0:
            return 0
        dirs=[(1,0),(-1,0),(0,1),(0,-1)]
        step=0
        while q:
            size=len(q)
            for i in range(size):
                x,y=q.popleft()
                for d in dirs:
                    nx,ny=x+d[0],y+d[1]
                    if nx<0 or ny<0  or nx>=M or ny>=N or grid[nx][ny]!=1:
                        continue
                    else:
                        grid[nx][ny]=2
                        q.append((nx,ny))
                        fresh-=1
            step+=1
        if fresh!=0:
            return -1
        return step-1
        
        
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        queue=[]
        fresh=0
        M,N=len(grid), len(grid[0])
        for i in range(M):
            for j in range(N):
                if grid[i][j]==1:
                    fresh+=1
                elif grid[i][j]==2:
                    queue.append((i,j,0))
                    
        dirs=[(0,1),(0,-1),(1,0),(-1,0)]
        res=0
        
        while len(queue)>0:
            x,y,c=queue.pop(0)
            for d in dirs:
                xn,yn=x+d[0],y+d[1]
                if xn>=0 and xn<M and yn>=0 and yn<N and grid[xn][yn]==1:
                    fresh-=1
                    res=max(res,c+1)
                    queue.append((xn,yn, res))
                    grid[xn][yn]=2
                    
        if fresh>0:
            return -1
        return res
                
