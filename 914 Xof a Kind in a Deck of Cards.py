class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        import collections
        
        count=collections.Counter(deck)
        N=len(deck)
        for i in range(2, N+1):
            if N%i==0:
                if all(v%i==0 for v in count.values()):
                    return True
                
        return False
        
        
        
class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        import collections
        
        count=collections.Counter(deck)
       
        
        if min(count.values())==1:
            return False
        gsb=[]
        for i in range(2, count.values()[0]+1):
            if count.values()[0]%i==0:
                gsb.append(i)
        for x in count.values(): 
            aa=gsb
            for a in aa:
                if x%a:
                    gsb.remove(a)
                    
        return True if len(gsb)>0 else False
