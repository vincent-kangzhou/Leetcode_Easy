class Solution(object):
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        import itertools
        res=['%d%d:%d%d' % t for t in itertools.permutations(A) if t[:2]<(2,4) and t[2]<=5]
        return max(res or [''])
        
        
class Solution(object):
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        import itertools
        ans=-1
        for h1, h2, m1,m2 in itertools.permutations(A):
            hours=10*h1+h2
            minutes=10*m1+m2
            
            time=60*hours+minutes
            
            if hours<24 and minutes<60 and time>=ans:
                ans=time
                
        return '{:02d}:{:02d}'.format(*divmod(ans,60)) if ans>=0 else ''
        
        
        
class Solution(object):
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        A.sort()
        for h in range(23,-1,-1):
            for m in range(59,-1,-1):
                t=[h//10, h%10, m//10, m%10]
                ts=sorted(t)
                if ts==A:
                    return str(t[0])+str(t[1])+':'+str(t[2])+str(t[3])
        return ''
