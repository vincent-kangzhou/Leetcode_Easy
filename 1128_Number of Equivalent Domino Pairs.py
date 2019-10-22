class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        import collections 
        res=0
        dominoes=map(tuple, map(sorted, dominoes))
        
        d=collections.Counter(dominoes)
        
        for idx, val in d.items():
            if val>=2:
                res+=(val)*(val-1)//2
        return res
            
            
            
            
            
            
class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        dic = {}
        res = 0
        for (i,j) in dominoes:
            if (i,j) in dic:
                res += dic[(i,j)]
            if i !=j and (j,i) in dic:
                res += dic[(j,i)]
            dic[(i,j)] = dic.setdefault((i,j),0) + 1
        return res
