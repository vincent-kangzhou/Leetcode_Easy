class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        s = ''.join(i for i in s if i.isalnum()).lower()
        return s==s[::-1]
        
        
        
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s)-1
        
        while left<right:
            if not s[left].isalnum():
                left+=1
                continue
            if not s[right].isalnum():
                right-=1
                continue
                
            if s[left].lower()!=s[right].lower():
                break
            else:
                left+=1
                right-=1
                
        return right<=left
                
