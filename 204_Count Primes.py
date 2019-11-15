class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <3:
            return 0

        digits = [1]*n
        digits[0] = digits[1] = 0

        for i in xrange(2, int(n**0.5)+1):
            if digits[i] == 1:
                for j in xrange(i+i, n, i):
                    digits[j] = 0

        return sum(digits)
        
        
        
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<3: return 0
        digits=[0]*n
        count=1
        sq=int(n**0.5)+1
        
        for i in range(3, n,2):
            if not digits[i]:
                count+=1
                
                if i>sq:
                    continue
                    
                
                for j in range(i+i, n, i):
                    digits[j]=1
                    
        return count
        
        
        
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        primes=0
        def isPrime(num):
            for i in range(2,int(num**0.5)+1):
                if not num%i:
                    return False
            return True
        
        for i in range(2, n):
            if isPrime(i):
                primes+=1
        return primes
        
