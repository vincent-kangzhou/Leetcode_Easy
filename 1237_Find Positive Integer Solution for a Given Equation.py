"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""
class Solution(object):
    def findSolution(self, customfunction, z):
        """
        :type num: int
        :type z: int
        :rtype: List[List[int]]
        """
        ans=[]
        for x in range(1, 1001):
            for y in range(1,1001):
                if customfunction.f(x,y)==z:
                    ans.append([x,y])
                    break
                elif customfunction.f(x,y)>z:
                    break
        return ans
                    
                    
                    
                    
"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""
class Solution(object):
    def findSolution(self, customfunction, z):
        """
        :type num: int
        :type z: int
        :rtype: List[List[int]]
        """

        rst=[]
        x,y=1,1000
        while x<=1000 and y>=1 :
            f_xy=customfunction.f(x,y)
            if f_xy>z:
                y-=1
            elif f_xy<z:
                x+=1
            else:
                rst.append([x,y])
                x+=1
        return rst
