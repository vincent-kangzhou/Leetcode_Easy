class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        steps=0
        for i in range(1, len(points)):
            start=points[i-1]
            end=points[i]
            
            vertical=abs(start[0]-end[0])
            horizontal=abs(start[1]-end[1])
            max_=max(vertical, horizontal)
            min_=min(vertical, horizontal)
            
            steps+=(min_+(max_-min_))
            
        return steps
