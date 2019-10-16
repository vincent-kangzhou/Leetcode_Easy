class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans=-1
        d=collections.Counter(s)
        for idx, val in enumerate(s):
            if d[val]==1:
                ans=idx
                break
        return ans
        
        
        
        
        
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapping={}
        for i in s:
            mapping[i]=mapping[i]+1 if i in mapping else 1
        
        for j in range(len(s)):
            if mapping[s[j]]==1:
                return j
        return -1
        
        
        
        
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters=[0]*26
        for c in s:
            letters[ord(c)-97]+=1
        
        for i in range(len(s)):
            if letters[ord(s[i])-97]==1:
                return i
        return -1
