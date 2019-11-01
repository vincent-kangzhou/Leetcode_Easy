class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        res=[]
        S=S.split()
        
        for idx, st in enumerate(S):
            if st[0] in ['A','E','I','O','U', 'a','e','i','o','u']:
                res.append(st+'ma'+(idx+1)*'a')
                
            else:
                res.append(st[1:]+st[0]+'ma'+(idx+1)*'a')
                
        return ' '.join(res)
        
        
        
