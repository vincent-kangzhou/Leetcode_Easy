class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return len(set(s))==len(set(t)) and len(set(s))==len(set(zip(s,t)))
        
        
        
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        c1,c2=[0]*200,[0]*200
        
        if len(s)!=len(t):return False
        for i in range (len(s)):
            ord1, ord2=ord(s[i]),ord(t[i])
            
            if c1[ord1]!=c2[ord2]:return False
            c1[ord1]=i+1
            c2[ord2]=i+1
            
        return True
        
        
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):return False
        hashmap={}
        for i in range(len(s)):
            if s[i] not in hashmap:
                hashmap[s[i]]=t[i]
                
            elif hashmap[s[i]]!=t[i]:
                return False
        mapval=[hashmap[j] for j in hashmap]
        
        return len(set(mapval))==len(hashmap)
        
        
        
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashmap={}
        mapval={}
        
        for i in range(len(s)):
            if s[i] in hashmap:
                if hashmap[s[i]]!=t[i]:
                    return False
                
            elif t[i] in mapval:
                return False
            
            else:
                hashmap[s[i]]=t[i]
                mapval[t[i]]=True
        return True
        
        
        
        class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return map(s.find,s)==map(t.find,t)
