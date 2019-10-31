class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        r=len(matrix)
        c=len(matrix[0])
        
        sub_1=[matrix[i][:c-1] for i in range(r-1)]
        sub_2=[matrix[i][1:] for i in range(1, r)]
        return sub_1==sub_2
        
        
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        
        r=len(matrix)
        c=len(matrix[0])
        for i in range(1,r):
            for j in range(1,c):
                if matrix[i][j]!=matrix[i-1][j-1]: return False
        return True
        
        
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for i in range(1, len(matrix)):
            if matrix[i][1:]!=matrix[i-1][:len(matrix[0])-1]: return False
            
        return True
            
