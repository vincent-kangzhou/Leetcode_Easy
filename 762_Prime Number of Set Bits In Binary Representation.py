class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        prime=[2,3,5,7,11,13,17,19,23,29,31]
        count=0
        
        for i in range(L, R+1):
            str1=bin(i)
            if str1.count('1') in prime:
                count+=1
                
        return count
