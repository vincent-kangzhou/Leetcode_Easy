class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        return list(set(collections.Counter(t) - collections.Counter(s)))[0]
        
        
        
        
        
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        mapping={}
        for j in t:
            mapping[j]=mapping[j]+1 if j in mapping else 1
            
        for i in s:
            if i in mapping:
                mapping[i]= mapping[i]-1
            if mapping[i]==0:
                del mapping[i]
        return mapping.keys()[0]
                
                
                
                
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        letters=[0]*26
        
        for i in s:
            letters[ord(i)-97]+=1
            
        for j in t:
            letters[ord(j)-97]-=1
            if letters[ord(j)-97]==-1:
                return j
        
        
        
        
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        mapping={}
        for i in s:
            mapping[i]=mapping[i]+1 if i in mapping else 1
            
        for j in t:
            if j not in mapping:
                return j
            mapping[j]-=1
            
            if mapping[j]<0:
                return j
        
        
        
        
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        res=ord(t[-1])
        for i in range(len(s)):
            res=res+ord(t[i])-ord(s[i])
        return chr(res)
        
        
