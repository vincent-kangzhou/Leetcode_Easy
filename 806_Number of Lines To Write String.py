class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        count=0
        sum_width=0
        for i in S:
            if sum_width+widths[ord(i)-97]>100:
                count+=1
                sum_width=widths[ord(i)-97]
            else:
                sum_width+=widths[ord(i)-97]
                     
        return [count+1, sum_width]
        
        
class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        count=0
        sum_width=0
        
        dic={k:v for v, k in enumerate('abcdefghijklmnopqrstuvwxyz')}
        for i in S:
            if sum_width+widths[dic[i]]>100:
                count+=1
                sum_width=widths[dic[i]]
            else:
                sum_width+=widths[dic[i]]
                     
        return [count+1, sum_width]
