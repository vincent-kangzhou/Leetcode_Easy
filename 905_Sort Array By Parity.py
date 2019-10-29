    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd=[]
        even=[]
        for i in A:
            if i%2==0:
                even.append(i)
            else:
                odd.append(i)
                
        return even+odd
        
        
        
class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return sorted(A,key=lambda x: x%2)
        
        
class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        
        res=[]
        for i in A:
            if i%2==0:
                res.insert(0,i)
            else:
                res.append(i)
                
        return res
