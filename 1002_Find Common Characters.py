class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        import collections
        count=collections.Counter(A[0])
        for i in range(1, len(A)):
            count&=collections.Counter(A[i])
        res=[]
        for i,j in count.items():
            for l in range(j):
                res.append(i)
        return res
        
        
        
class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        col=[101]*26
        for word in A:
            for char in range(97,123):
                idx=char-ord('a')
                col[idx]=min(col[idx],word.count(chr(char)))
                
        res=[]
        for i in range(26):
            res+=[chr(i+97)]*col[i]
            
        return res
        
        
        
class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        return list(reduce(collections.Counter.__and__, map(collections.Counter, A)).elements())
        
        
        
class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        A_count = map(lambda x : collections.Counter(x), A)
        res = []
        for i in range(26):
            c = chr(ord('a') + i)
            min_count = min([a_count[c] for a_count in A_count])
            if min_count:
                res.extend([c] * min_count)
        return res
