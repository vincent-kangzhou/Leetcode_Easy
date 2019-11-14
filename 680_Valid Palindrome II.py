class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_=s[::-1]
        N=len(s)
        for i in range(N):
            if s[i]!=s_[i]:
                break
        if i ==N-1: return True
        return s[i+1:]==(s_[i:N-1-i]+s_[N-i:]) or s[i:N-1-i]+s[N-i:]==s_[i+1:]
        
        
        
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        N= len(s)
        left , right=0 , N-1
        
        while (left<=right) and s[left]==s[right]:
            left+=1
            right-=1
        if left>right: return True
        
        return self.palindrome(s[left:right]) or self.palindrome(s[left+1:right+1])
        
     
    def palindrome(self, string):
        left, right=0, len(string)-1
        
        while (left<=right) and string[left]==string[right]:
            left+=1
            right-=1
            
        if left>right:return True
        return False
        
        
        
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        N=len(s)
        left, right=0, N-1
        while (left<right):
            if s[left]!=s[right]:
                return s[left:right]==s[left:right][::-1] or s[left+1: right+1]==s[left+1: right+1][::-1]
            
            left+=1
            right-=1
        return True
