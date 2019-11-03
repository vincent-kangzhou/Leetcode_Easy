class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        dp5=0
        dp10=0
        
        for i in bills:
            if i==5:
                dp5+=1
            elif i==10:
                if dp5>0:
                    dp10+=1
                    dp5-=1
                else:
                    return False
                    
            else:
                if dp10>0 and dp5>0:
                    dp10-=1
                    dp5-=1
                elif dp5>3:
                    dp5-=3
                else:
                    return False
        return True
