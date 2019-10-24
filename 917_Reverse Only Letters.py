class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        S=list(S)
        left, right=0, len(S)-1
        while left<right:
            if not (ord(S[left])>=65 and ord(S[left])<=90) and not (ord(S[left])>=97 and ord(S[left])<=122):
                left +=1
                
                continue
            if not (ord(S[right])>=65 and ord(S[right])<=90) and not (ord(S[right])>=97 and ord(S[right])<=122):
                right-=1
                continue
                
            S[right], S[left]=S[left], S[right]
            
            left+=1
            right-=1
            
        return ''.join(S)
                
                
                
class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        S=list(S)
        left, right=0, len(S)-1
        while left<right:
            if not S[left].isalpha():
                left +=1
                
                continue
            if not S[right].isalpha():
                right-=1
                continue
                
            S[right], S[left]=S[left], S[right]
            
            left+=1
            right-=1
            
        return ''.join(S)
        
        
        
   class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        letters=[]
        N=len(S)
        
        for i in S:
            if i.isalpha():
                letters.append(i)
                
        res=''
        for j in S:
            if j.isalpha():
                res+=letters.pop()
            else:
                res+=j
                
        return res     





class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        
        l=len(S)-1
        
        res=''
        
        for i ,s in enumerate(S):
            if s.isalpha():
                while not S[l].isalpha():
                    l-=1
                    
                res+=S[l]
                l-=1
                
            else:
                res+=s
                
        return res
