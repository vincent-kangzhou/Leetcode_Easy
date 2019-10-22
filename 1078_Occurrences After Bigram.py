class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        text=text.split()
        len_=len(text)
        res=[]
        idx=0
        while idx<len_-2:
            if text[idx]==first and text[idx+1]==second:
                res.append(text[idx+2])
                idx+=2
            else:
                idx+=1
                
        return res
        
        
        words = text.split()
        res = []
        L = len(words)
        for i in range(L - 2):
            f, s, t = words[i], words[i + 1], words[i + 2]
            if f == first and s == second:
                res.append(t)
        return res
