class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        
        one_round=sum(distance[min(start, destination):max(start, destination)])
        return min(one_round,sum(distance)-one_round)
