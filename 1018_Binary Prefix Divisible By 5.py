class Solution(object):
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        res=[]
        val=0
        for i in A:
            
            if i==1:
                val+=1
            res.append(val%5==0)
            val=val<<1
        return res
                
                
                
class Solution(object):
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        res=[]
        prefix=0
        for i in range(len(A)):
            prefix*=2
            int_=int(str(A[i]),2)+prefix
            
            res.append(int_%5==0)
            prefix=int_%5
            
        return res
            
            
            
class Solution(object):
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        res = []
        prefix = 0
        for a in A:
            prefix = (prefix * 2 + a) % 5
            res.append(prefix == 0)
        return res
        
