class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words= str.split(' ')
        if len(words) !=len(pattern):
            return False
        hashmap={}
        mapval={}
        for i in range(len(pattern)):
            if pattern[i] in hashmap:
                if hashmap[pattern[i]] != words[i]:
                    return False
                
            else:
                if words[i] in mapval:
                    return False
                hashmap[pattern[i]]=words[i]
                mapval[words[i]]=True

        
        return True
        
        
        
        
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words= str.split(' ')
        if len(words) !=len(pattern):
            return False
        
        return map(pattern.find, pattern)==map(words.index, words)
            
            
            
            
            
            
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words= str.split(' ')
        if len(words) !=len(pattern):
            return False
        
        return len(set(pattern))==len(set(words))==len(set(zip(pattern, words)))
                
