class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()
        mindist=0
        pos=0
        heaters=[float('-inf')]+heaters+[float('inf')]
        
        for house in houses:
            while house>=heaters[pos]:
                pos+=1
            dist=min(abs(heaters[pos-1]-house), heaters[pos]-house)
            mindist=max(mindist, dist)
        return mindist
        
        
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()
        mindist=0
        pos=0
        for i in range(len(houses)):
            while pos<len(heaters)-1 and abs(heaters[pos]-houses[i])>=abs(heaters[pos+1]-houses[i]):
                pos+=1
            mindist=max(mindist, abs(heaters[pos]-houses[i]))
        return mindist
