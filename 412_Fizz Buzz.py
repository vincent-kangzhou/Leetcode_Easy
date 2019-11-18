class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res=['']*n
        for i in range(1,n+1):
            if i%3==0:
                res[i-1]+='Fizz'
            if i%5==0:
                res[i-1]+='Buzz'
            if i%3 and i%5:
                res[i-1]+=str(i)
        return res
                
                
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res=[]
        for i in range(1,n+1):
            if i%15==0:
                res.append('FizzBuzz')
            elif i%3==0:
                res.append('Fizz')
            elif i%5==0:
                res.append('Buzz')
            else:
                res.append(str(i))
        return res
        
        
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return [str(i) if (i%3!=0 and i%5!=0) else 'Fizz'*(i%3==0)+'Buzz'*(i%5==0) for i in range(1,n+1)]
