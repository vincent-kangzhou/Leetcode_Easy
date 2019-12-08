class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        grid=[[0]*3 for _ in range(3)]
        
        for i in range(len(moves)):
            x,y=moves[i]
            grid[x][y]=1 if i%2==0 else -1
        if sum(grid[0])==3 or sum(grid[1])==3 or sum(grid[2])==3:
            return 'A'
        
        if (grid[0][0]+grid[1][0]+grid[2][0])==3 or (grid[0][1]+grid[1][1]+grid[2][1])==3 or (grid[0][2]+grid[1][2]+grid[2][2])==3:
            return 'A'
        
        if (grid[0][0]+grid[1][1]+grid[2][2])==3 or (grid[0][2]+grid[1][1]+grid[2][0])==3:
            return 'A'
        
        if sum(grid[0])==-3 or sum(grid[1])==-3 or sum(grid[2])==-3:
            return 'B'
        
        if (grid[0][0]+grid[1][0]+grid[2][0])==-3 or (grid[0][1]+grid[1][1]+grid[2][1])==-3 or (grid[0][2]+grid[1][2]+grid[2][2])==-3:
            return 'B'
        
        if (grid[0][0]+grid[1][1]+grid[2][2])==-3 or (grid[0][2]+grid[1][1]+grid[2][0])==-3:
            return 'B'
        
        if len(moves)>=9:
            return 'Draw'
        
        return 'Pending'
