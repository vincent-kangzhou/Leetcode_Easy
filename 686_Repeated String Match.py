class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        lenA=len(A)
        lenB=len(B)
        count=lenB//lenA
        if lenB%lenA:
            A_=A*(count+1)
            count+=1
        else:
            A_=A*count
        
        if B in A_:
            return count
        for i in range(1, count+1):
            A_+=A
            if B in A_:
                return count+i
        return -1
        
        
        
class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        m=len(A)
        n=len(B)
        x=1
        while (x-1)*m<=2*max(m,n):
            if B in A*x:
                return x
            else:
                x+=1
        return -1
        
        
        
class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        lenB=len(B)
        lenA=len(A)
        for i in range(lenB//lenA, lenB//lenA+3):
            if (A*i).find(B)!=-1:
                return i
        return -1
