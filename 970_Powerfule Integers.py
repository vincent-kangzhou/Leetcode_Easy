class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        res = set()
        i = 0
        while x ** i <= bound and i <= bound:
            j = 0
            while j <= bound:
                target = x ** i + y ** j
                if target > bound:
                    break
                res.add(target)
                j += 1
            i += 1
        return list(res)



class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        x_max,y_max=1 if x==1 else 20, 1 if y==1 else 20
        
        res=set()
        
        for i in range(x_max):
            for j in range(y_max):
                if x**i+y**j<=bound:
                    res.add(x**i+y**j)
                    
        return list(res)
