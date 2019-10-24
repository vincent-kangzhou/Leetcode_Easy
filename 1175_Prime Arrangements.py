class Solution(object):
    def numPrimeArrangements(self, n):
        """
        :type n: int
        :rtype: int
        """
        prime=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
        import bisect
        
        prime_count=bisect.bisect_right(prime,n)
        no_prime=n-prime_count
        def calc(num):
            factorial=1
            for i in range(1,num+1):
                factorial*=i
            return factorial
        
        total=calc(prime_count)*calc(no_prime)
        
        return total%(10**9+7)
                
