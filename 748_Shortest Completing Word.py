class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        import collections
        ans=''
        
        str1=''
        for word in licensePlate.lower():
            if word.isalpha():
                str1+=word
                
        count=collections.Counter(str1)
        
        for word in words:
            c1=count-collections.Counter(word)
            if len(c1)==0:
                    
                if len(ans)==0 or len(ans)>len(word):
                    ans=word
                    
        return ans
        
        
        
        
from collections import Counter
import re
class Solution(object):

    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """

        regex = re.compile('[^a-zA-Z]')
        license = regex.sub('',licensePlate)
        counter1 = Counter(license.lower())
        res = ''
        for word in words:
            if self.count(counter1, word):
                if res == '' or len(word) < len(res):
                    res = word
        return res
        
    def count(self, counter1, word):
        counter2 = Counter(word)
        counter2.subtract(counter1)
        return all([c >= 0 for c in counter2.values()])
