class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<=0: return False
        if num==1: return True
        if num%2==0:
            return self.isUgly(num//2)
        
        if num%3==0:
            return self.isUgly(num//3)
        if num%5==0:
            return self.isUgly(num//5)
        
        return False
        
        
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<=0: return False
        for i in [2,3,5]:
            while num%i==0:
                num=num//i
        return True if num==1 else False
