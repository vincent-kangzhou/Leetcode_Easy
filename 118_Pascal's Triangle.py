class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==0: return []
        if numRows==1: return [[1]]
        if numRows==2: return [[1],[1,1]]
        
        list=[[] for j in range(numRows)]
        list[0]=[1]
        list[1]=[1,1]
        for j in range(2, numRows):
            
            list[j]=[1 for i in range(j+1)]
            
            for i in range(1, j):
                list[j][i]=list[j-1][i]+list[j-1][i-1]
        return list
        
