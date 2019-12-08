class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        row, col=0,0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=='R':
                    row=i
                    col=j
                    break
                    
        res=0
        
        for i in range(row-1, -1,-1):
            if board[i][col]=='p':
                res+=1
                break
                
            if board[i][col]=='B':
                break
                
        for i in range(row+1, len(board)):
            if board[i][col]=='p':
                res+=1
                break
                
            if board[i][col]=='B':
                break
                
        for j in range(col-1,-1,-1):
            if board[row][j]=='p':
                res+=1
                break
                
            if board[row][j]=='B':
                break
                
        for j in range(col+1,len(board[0])):
            if board[row][j]=='p':
                res+=1
                break
                
            if board[row][j]=='B':
                break
        return res
