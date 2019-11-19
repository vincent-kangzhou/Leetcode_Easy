class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S=S.replace('-','')
        S=S.upper()
        first=len(S)%K
        
        res=S[:first]
        
        for i in range(first,len(S),K):
            str=S[i:i+K] if i==0 else '-'+S[i:i+K]
            res+=str
        return res
        
        
        
        
class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        res=[]
        S=S.replace('-','').upper()
        first=len(S)%K
        if first!=0: res.append(S[:first])
        for i in range(first, len(S),K):
            res.append(S[i:i+K])
        return '-'.join(res)
