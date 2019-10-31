class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        index=[idx for idx , val in enumerate(S) if val ==C]
        
        return [min([abs(i-idx) for idx in index]) for i in range(len(S))]
        
        
        
class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        
        len_=len(S)
        dist=[0]*len_
        index=-100000
        
        for idx, val in enumerate(S):
            if val==C:
                index=idx
            dist[idx]=(idx-index)
        
        index=-100000
        for i in range(len_-1, -1,-1):
            if S[i]==C:
                index=i
            dist[i]=min(dist[i], abs(i-index))
        return dist
