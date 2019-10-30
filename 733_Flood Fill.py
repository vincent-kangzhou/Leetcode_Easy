class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        flood=[(sr,sc)]
        orig=image[sr][sc]
        r=len(image)
        c=len(image[0])
        image[sr][sc]=newColor
        dirs=[(1,0),(-1,0),(0,1),(0,-1)]
        while flood:
            x, y = flood.pop(0)
            for d in dirs:
                xn=x+d[0]
                yn=y+d[1]
                if xn>=0 and xn<r and yn>=0 and yn<c and image[xn][yn]==orig and image[xn][yn]!=newColor:
                    image[xn][yn]=newColor
                    
                    flood.append((xn,yn))
        return image
        
        
        
        
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        self.oldColor=image[sr][sc]
        self.aa=[[0 for i in range(len(image[0]))] for j in range(len(image))]
        
        def search(image, i,j):
            self.aa[i][j]=1
            image[i][j]=newColor
            if i>=1:
                if image[i-1][j]==self.oldColor and self.aa[i-1][j]==0:
                    search (image, i-1, j)
            if j>=1:
                if image[i][j-1]==self.oldColor and self.aa[i][j-1]==0:
                    search (image, i, j-1)
            if i<=len(image)-2:
                if image[i+1][j]==self.oldColor and self.aa[i+1][j]==0:
                    search (image, i+1, j)
            if j<=len(image[0])-2:
                if image[i][j+1]==self.oldColor and self.aa[i][j+1]==0:
                    search (image, i, j+1)
        search(image, sr,sc)
        
        return image
        
        
        
        
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        rows, cols, oldcolor= len(image)-1, len(image[0])-1, image[sr][sc]
        def traverse(row, col):
            if (not(0<=row<=rows and 0<=col<=cols)) or image[row][col]!=oldcolor:
                return
            image[row][col]=newColor
            [traverse(row+x,col+y) for x, y in ((0,1),(0,-1),(1,0),(-1,0))]
        if oldcolor!=newColor:
            traverse(sr,sc)
        return image
            
            
            
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        color=image[sr][sc]
        
        def dfs(x, y, color, newcolor):
            if image[x][y]==color:
                image[x][y]=newColor
                if x-1>=0:
                    dfs(x-1, y, color, newcolor)
                if y-1>=0:
                    dfs(x, y-1, color, newcolor)
                if x+1<=len(image)-1:
                    dfs(x+1, y, color, newcolor)
                if y+1<=len(image[0])-1:
                    dfs(x, y+1, color, newcolor)
        if image[sr][sc]==newColor:
            return image
        dfs(sr, sc, color, newColor)
        return image
            
