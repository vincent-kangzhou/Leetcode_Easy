class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
 
        S=list(S)
        T=list(T)
        while '#' in S:
            idx=S.index('#')
            del S[idx]
            if idx-1>=0:
                del S[idx-1]
            
        while '#' in T:
            idx=T.index('#')
            del T[idx]
            if idx-1>=0:
                del T[idx-1]

        return S==T
        
        
class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def sim(st):
            ans=''
            for char in st:
                if char=='#':
                    if len(ans)>= 0: ans=ans[:-1]
                else:
                    ans+=char
            return ans
        return sim(S)==sim(T)
        
        
        
        
class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        stopS, stopT=0,0
        S=list(S)
        T=list(T)
        for char in S:
            if char=='#':
                if stopS>0:
                    stopS-=1
            else:
                S[stopS]=char
                stopS+=1
                
        for char in T:
            if char=='#':
                if stopT>0:
                    stopT-=1
            else:
                T[stopT]=char
                stopT+=1
                
        return S[:stopS]==T[:stopT]
        
        
        
class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def toString(st):
            ans=[]
            for char in st:
                if char=='#':
                    ans and ans.pop()
                else:
                    ans.append(char)
            return ans
        return toString(S)==toString(T)
