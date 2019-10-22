class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        import collections
        count=0
        
        for a in words:
            if (collections.Counter(a)&collections.Counter(list(chars)))==collections.Counter(a):
                count+=len(a)
                
        return count
        
        
        
class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        import collections
        char_dict=collections.Counter(chars)
        
        def isValid(word):
            word_dict=collections.Counter(word)
            for i in word_dict:
                if i not in char_dict or word_dict[i]>char_dict[i]:
                    return False
            return True
        sum_=0
        for word in words:
            sum_+=len(word) if isValid(word) else 0
            
        return sum_
            
            
            
            
class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        res=0
        for word in words:
            flag=True
            for i in word:
                if word.count(i)>chars.count(i):
                    flag=False
                    break
                
            res+=len(word) if flag else 0
        return res
