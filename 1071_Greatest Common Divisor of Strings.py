class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        l1=len(str1)
        l2=len(str2)
        
        shorter=min(l1,l2)
        
        for i in range(shorter,0,-1):
            if l1%i or l2%i:
                continue
            num1=l1//i
            num2=l2//i
            
            rebuild1=str1[:i]*num1
            rebuild2=str1[:i]*num2
            
            if rebuild1==str1 and rebuild2==str2:
                return str1[:i]
        return ''
        
        
        
        
        
