class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num<=9: return num
        num=num//10+num%10
        return self.addDigits(num)
