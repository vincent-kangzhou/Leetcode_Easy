class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N==0: return 0
        if N==1: return 1
        if N>=2:
            return self.fib(N-1)+self.fib(N-2)
            
            
class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        array=[i for i in range(N+1)]
        for i in range(2, N+1):
            array[i]=array[i-1]+array[i-2]
        return array[-1]
        
        
class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N<=1:
            return N
        pre=0
        cur=1
        for i in range(2, N+1):
            pre,cur=cur, pre+cur
        return cur
