class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        import collections
        wordDict=collections.defaultdict(int)
        count=0
        
        for word in s:
            wordDict[word]+=1
        odd=False
        for i in wordDict:
            if wordDict[i]%2==0:
                count+=wordDict[i]
            else:
                count+=(wordDict[i]-1)
                odd=True
        return count+1 if odd else count
        
        
        
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq=[0]*128
        for c in s:
            freq[ord(c)]+=1
            
        ans=0
        odd=0
        for fre in freq:
            ans+=fre&(~1)
            odd |=fre&1
            
        return ans+odd
