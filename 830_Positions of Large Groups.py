class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        res=[]
        st=S[0]
        start=0
        for idx, val in enumerate(S):
            
            if val==st:
                end=idx
            else:
                
                if end-start>=2:
                    res.append([start, end])
                start=idx
                st=val
        if end-start>=2:
            res.append([start, end])
                
        return res
        
        
class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        res=[]
        st=S[0]
        start=0
        for idx, val in enumerate(S):
            if val!=st:
                if idx-start>=3:
                    res.append([start,idx-1])
                
                start=idx
                st=val
            

        if idx-start>=2:
            res.append([start, idx])
                
        return res
        
        
        
class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        res=[]
        st=S[0]
        start=0
        S=S+'A'
        for idx, val in enumerate(S):
            if val!=st:
                if idx-start>=3:
                    res.append([start,idx-1])
                
                start=idx
                st=val

        return res
        
        
        
class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        res=[]
        i=0
        for j in range(len(S)):
            if j==len(S)-1 or S[j]!=S[j+1]:
                if j-i>=2:
                    res.append([i,j])
                i=j+1
                    
        return res
        
