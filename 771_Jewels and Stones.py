class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count=0
        for i in S:
            if i in J:
                count+=1
        return count
        
        
        
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewels = {x: 0 for x in J}
        for char in S:
            if char in jewels.keys():
                jewels[char] += 1

        return sum(jewels.values())
        
        
        
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count=0
        for i in J:
            count+=S.count(i)
            
        return count
        
        
        
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        return sum(map(S.count, J))
