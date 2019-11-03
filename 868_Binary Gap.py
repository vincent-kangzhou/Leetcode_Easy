class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        N=bin(N)[2:]
        start=0
        end=0
        dis=0
        for i in range(1, len(N)):
            if N[i]=='1':
                dis=max(dis, i-start)
                
                start=i
        return dis
            
            
            
class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        N=bin(N)[2:]
        dis=0
        pre1=-1
        for i in range(len(N)):
            if N[i]=='1':
                if pre1==-1: pre1=i
                else:
                    dis=max(dis, i-pre1)
                    pre1=i
        return dis                
        
        
        
        
class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        binary = bin(N)[2:]
        dists = [0] * len(binary)
        left = 0
        for i, b in enumerate(binary):
            if b == '1':
                dists[i] = i - left
                left = i
        return max(dists)
