class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        N=len(S)
        ni, nd=0,N
        res=[]
        for s in S:
            if s=='I':
                res.append(ni)
                ni+=1
            else:
                res.append(nd)
                nd-=1
                
        if s=='I': res.append(ni)
        else:
            res.append(nd)
        
        return res
            
