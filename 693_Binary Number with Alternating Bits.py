class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n=bin(n)[2:]
        
        for i in range(1, len(n)):
            if n[i]==n[i-1]:
                return False
        return True
        
        
class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n=bin(n)[2:]
        return all(int(n[i])+int(n[i+1])==1 for i in range(len(n)-1))
        
        
        
class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n=bin(n)[2:]
        return all(int(n[i])!=int(n[i+1]) for i in range(len(n)-1))
        
        
class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        b = 0b1010101010101010101010101010101010101010101010101010101010101010
        
        while b>0:
            if b==n:
                return True
            b=b>>1
            
        return False
        
        
        
class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n^=(n>>1)
        
        return not(n&n+1)
