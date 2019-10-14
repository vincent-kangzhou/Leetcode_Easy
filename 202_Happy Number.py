class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        happySet = set([1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97])

        while n>99:
            n = sum([int(x) * int(x) for x in list(str(n))])
        return n in happySet







class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        num_dict={}
        
        while True:
            num_dict[n]=True
            sum=0
            while (n>0):
                sum+=(n%10)**2
                n=n//10
            
            if sum==1:
                return True
            elif sum in num_dict:
                return False
            else:
                n=sum








class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        slow=fast=n
        while True:
            slow=self.squareSum(slow)
            fast=self.squareSum(fast)
            fast=self.squareSum(fast)
            
            if slow==fast:
                break
                
        return slow==1
            
        
        
    def squareSum(self,n):
        sum=0
        while (n>0):
            sum+=(n%10)**2
            
            n//=10
            
        return sum
