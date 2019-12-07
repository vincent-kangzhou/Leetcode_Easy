class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        import collections
        
        count=[]
        for word in A:
            even=''
            odd=''
            
            for i in range(len(word)):
                if i%2==0:
                    even+=word[i]
                else:
                    odd+=word[i]
            count.append((''.join(sorted(even)), ''.join(sorted(odd))))
            
        return len(collections.Counter(count).keys())
