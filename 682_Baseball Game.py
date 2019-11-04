class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        res=[]
        for val in ops:
            if val not in ['C','D','+']:
                res.append(int(val))
            elif val=='C':
                res.pop()
            elif val=='D':
                res.append(res[-1]*2)
            elif val=='+':
                res.append(res[-1]+res[-2])
        return sum(res)
        
        
        
