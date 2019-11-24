class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        res=''
        if num==0:return '0'
        num_=abs(num)
        while num_:
            res+=str(num_%7)
            num_=num_//7
        return res[::-1] if num>0 else '-'+res[::-1]
