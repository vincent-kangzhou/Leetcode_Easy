class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        total, div=1,2
        while div**2<=num:
            if num%div==0:
                total+=div
                if div**2!=num:
                    total+=num//div
                    
            div+=1
            
        return num>1 and total==num
        
        
        
        
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        if num <= 1:
            return False
        total = 1
        for i in range(2, int(math.sqrt(num))+1):
            if num % i ==0:
                total = total + i + num//i   
        return total == num
