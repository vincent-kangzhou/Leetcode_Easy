class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """

        if sum(A)%3: return False
        total=sum(A)//3
        sum_=0
        total_i=0
        for i in A:
            sum_+=i
            if sum_==total:
                total_i+=1
                sum_=0
        return total_i==3
        
        
        
        
class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        s = sum(A)
        if s % 3 > 0:
            return False
        s /= 3
        size = len(A)
        t = 0
        a, b = -1, -1
        for i in range(size):
            t += A[i]
            if t == s:
                a = i
                break
        t = 0
        for j in range(size - 1, -1, -1):
            t += A[j]
            if t == s:
                b = j
                break
        if a == -1 or b == -1 or a + 1 >= b:
            return False
        return True
