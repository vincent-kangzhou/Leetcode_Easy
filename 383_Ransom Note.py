class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        import collections
        dict1=collections.Counter(ransomNote)
        dict2=collections.Counter(magazine)
        
        for idx in dict1:
            if idx not in dict2 or dict1[idx]>dict2[idx]:
                return False
            
        return True
        



class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        import collections
        dict1=collections.Counter(ransomNote)
        dict2=collections.Counter(magazine)
        
        dict3=dict1&dict2
        return dict3==dict1
        
        
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        import collections

        dict2=collections.Counter(magazine)
        for i in ransomNote:
            if i not in dict2 or dict2[i]==0:
                return False
            else:
                dict2[i]-=1
                
        return True
        
        
        
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dic = {}
        for i in magazine:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
                
        for j in ransomNote:
            if j in dic:
                dic[j] -= 1
                if dic[j] < 0:
                    return False
            else:
                return False
        return True
        
        
        
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for i in set(ransomNote):
            if ransomNote.count(i) > magazine.count(i):
                return False
        return True
        
        
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        return not collections.Counter(ransomNote) - collections.Counter(magazine)
