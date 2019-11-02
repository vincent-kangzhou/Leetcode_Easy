class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count=0
        
        r=len(grid)
        c=len(grid[0])
        
        
        mid_list=[[9,5,1],[1,5,9],[3,5,7],[7,5,3]]
        dic={0:[[4,3,8],[2,7,6]],1:[[8,3,4],[6,7,2]],2:[[4,9,2],[8,1,6]],3:[[2,9,4],[6,1,8]]}
        
        for i in range(r-2):
            for j in range(c-2):
                mid=grid[i+1][j:j+3]
                if  mid in mid_list:
                    idx=mid_list.index(mid)
                    
                    if (grid[i][j:j+3]==dic[idx][0] and grid[i+2][j:j+3]==dic[idx][1]) or (grid[i][j:j+3]==dic[idx][1] and grid[i+2][j:j+3]==dic[idx][0]):
                        count+=1
                else:
                    continue
                    
        return count
        
        
        
class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid)<3 and len(grid[0])<3:
            return 0
        counter=0
        for row in range(len(grid)-2):
            for col in range(len(grid[0])-2):
                sub_matrix=[[grid[row+i][col+j]for j in range(3)]for i in range(3)]
                if self.magic_square(sub_matrix):
                    counter+=1
        return counter
    
    def magic_square(self, matrix):
        is_number_right=all(1<=matrix[i][j]<=9 for i in range(3) for j in range(3))
        is_row_right=all(sum(row)==15 for row in matrix)
        is_col_right=all(sum(col)==15 for col in [[matrix[i][j]for i in range(3)]for j in range(3)])
        is_diagonal_right = matrix[1][1] == 5 and matrix[0][0] + matrix[-1][-1] == 10 and matrix[0][-1] + matrix[-1][0] == 10
        return is_number_right and is_row_right and is_col_right and is_diagonal_right
        
        
        
        
class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid)<3 and len(grid[0])<3:
            return 0
        counter=0
        for row in range(len(grid)-2):
            for col in range(len(grid[0])-2):
                sub_matrix=[[grid[row+i][col+j]for j in range(3)]for i in range(3)]
                if self.magic_square(sub_matrix):
                    counter+=1
        return counter
    
    def magic_square(self, matrix):
        
        
        is_number_right=all(1<=matrix[i][j]<=9 for i in range(3) for j in range(3))
        is_row_right=all(sum(row)==15 for row in matrix)
        is_col_right=all(sum(col)==15 for col in [[matrix[i][j]for i in range(3)]for j in range(3)])
        is_diagonal_right = matrix[1][1] == 5 and matrix[0][0] + matrix[-1][-1] == 10 and matrix[0][-1] + matrix[-1][0] == 10
        is_range=[matrix[i][j] for i in range(3) for j in range(3)]
        
        return is_number_right and is_row_right and is_col_right and is_diagonal_right and set(is_range)==set(range(1,10))
