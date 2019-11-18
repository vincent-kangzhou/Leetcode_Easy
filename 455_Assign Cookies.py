class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        count=0
        g.sort()
        s.sort()
        while g and s:
            if g[0]<=s[0]:
                g.pop(0)
                s.pop(0)
                count+=1
            else:
                s.pop(0)
                
        return count
        
        
        
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        count=0
        g.sort()
        s.sort()
        sp=0
        for gi in g:
            
            while sp<len(s) and gi>s[sp]:
                sp+=1
            if sp<len(s) and s[sp]>=gi:
                count+=1
                sp+=1
        return count
        
        
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        count=0
        g.sort()
        s.sort()
        sp=0
        for gi in g:
            while sp<len(s):
                if s[sp]>=gi:
                    sp+=1
                    count+=1
                    break
                
                sp+=1
            # else:
            #     break
        return count
