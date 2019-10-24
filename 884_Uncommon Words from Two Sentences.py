class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        A_=A.split()
        B_=B.split()
        res=[]
        
        import collections
        count_A=collections.Counter(A_)
        count_B=collections.Counter(B_)
        
        for i, j in count_A.items():
            if i not in count_B and j==1:
                res.append(i)
        for idx, val in count_B.items():
            if idx not in count_A and val==1:
                res.append(idx)
        return res
            
            
            
            
class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        A_=A.split()
        B_=B.split()
        res=[]
        dic_A={}
        dic_B={}
        
        for i in A_:
            dic_A[i]=dic_A.setdefault(i,0)+1
            
        for j in B_:
            dic_B[j]=dic_B.setdefault(j,0)+1
            
        for key in dic_A:
            if key not in dic_B and dic_A[key]==1:
                res.append(key)
                
        for key in dic_B:
            if key not in dic_A and dic_B[key]==1:
                res.append(key)

                
        return res
        
        
        
        
class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        A_=A.split()
        B_=B.split()
        
        import collections
        count=collections.Counter(A_)
        count+=collections.Counter(B_)
        
        return [idx for idx, val in count.items() if val==1]
