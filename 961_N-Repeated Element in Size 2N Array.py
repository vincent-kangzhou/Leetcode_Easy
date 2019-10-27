class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        import collections
        count={}
        for i in A:
            count[i]=count.setdefault(i,1)-1
            if count[i]<0:
                return i
            
            
            
class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        import random
        while 1:
            s=random.sample(A,2)
            if s[0]==s[1]:
                return s[0]
